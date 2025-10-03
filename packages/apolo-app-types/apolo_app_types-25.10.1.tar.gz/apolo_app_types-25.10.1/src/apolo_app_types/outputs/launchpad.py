import typing as t

import httpx

from apolo_app_types.clients.kube import get_service_host_port
from apolo_app_types.outputs.common import INSTANCE_LABEL
from apolo_app_types.outputs.utils.ingress import get_ingress_host_port
from apolo_app_types.protocols.apps import AppInstance
from apolo_app_types.protocols.common.networking import HttpApi, ServiceAPI, WebApp
from apolo_app_types.protocols.launchpad import (
    InstalledApps,
    KeycloakConfig,
    LaunchpadAppOutputs,
)


async def _get_installed_apps(admin_password: str, api: HttpApi) -> InstalledApps:
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{api.protocol}://{api.host}:{api.port}{api.base_path}instances",
            auth=httpx.BasicAuth("admin", admin_password),
        )
        response.raise_for_status()
        apps_data = response.json()

        installed_apps = []
        for app in apps_data:
            app_instance = AppInstance(
                app_id=app.get("app_id", ""),
                app_name=app.get("app_name", ""),
            )
            installed_apps.append(app_instance)

        return InstalledApps(app_list=installed_apps)


async def get_launchpad_outputs(
    helm_values: dict[str, t.Any],
    app_instance_id: str,
) -> dict[str, t.Any]:
    labels = {
        "application": "launchpad",
        INSTANCE_LABEL: app_instance_id,
    }

    launchpad_labels = {
        **labels,
        "service": "client",
    }
    internal_host, internal_port = await get_service_host_port(
        match_labels=launchpad_labels
    )
    internal_web_app_url = None
    if internal_host:
        internal_web_app_url = WebApp(
            host=internal_host,
            port=int(internal_port),
            base_path="/",
            protocol="http",
        )

    host_port = await get_ingress_host_port(match_labels=launchpad_labels)
    external_web_app_url = None
    if host_port:
        host, port = host_port
        external_web_app_url = WebApp(
            host=host,
            port=int(port),
            base_path="/",
            protocol="https",
        )

    # keycloak urls
    keycloak_labels = {
        **labels,
        "service": "keycloak",
    }

    host_port = await get_ingress_host_port(match_labels=keycloak_labels)
    keycloak_external_web_app_url = None
    if host_port:
        host, port = host_port
        keycloak_external_web_app_url = HttpApi(
            host=host,
            port=int(port),
            base_path="/",
            protocol="https",
        )

    internal_host, internal_port = await get_service_host_port(
        match_labels=keycloak_labels
    )
    keycloak_internal_web_app_url = None
    if internal_host:
        keycloak_internal_web_app_url = HttpApi(
            host=internal_host,
            port=int(internal_port),
            base_path="/",
            protocol="http",
        )

    keycloak_password = helm_values["keycloak"]["auth"]["adminPassword"]

    # getting Launchpad API url
    api_labels = {**labels, "service": "launchpad"}
    internal_host, internal_port = await get_service_host_port(match_labels=api_labels)
    api_http_url = None
    if internal_host:
        api_http_url = HttpApi(
            host=internal_host,
            port=int(internal_port),
            base_path="/",
            protocol="http",
        )
    launchpad_admin_password = helm_values.get("LAUNCHPAD_ADMIN_PASSWORD", None)

    outputs = LaunchpadAppOutputs(
        app_url=ServiceAPI[WebApp](
            internal_url=internal_web_app_url,
            external_url=external_web_app_url,
        ),
        keycloak_config=KeycloakConfig(
            web_app_url=ServiceAPI[HttpApi](
                internal_url=keycloak_internal_web_app_url,
                external_url=keycloak_external_web_app_url,
            ),
            auth_admin_password=keycloak_password,
        ),
        installed_apps=await _get_installed_apps(
            admin_password=launchpad_admin_password,
            api=api_http_url,
        )
        if api_http_url and launchpad_admin_password
        else None,
    )
    return outputs.model_dump()
