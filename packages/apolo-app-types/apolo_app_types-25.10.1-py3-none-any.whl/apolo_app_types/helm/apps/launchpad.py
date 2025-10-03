import json
import random
import string
import typing as t

from apolo_app_types import LLMInputs, TextEmbeddingsInferenceAppInputs
from apolo_app_types.app_types import AppType
from apolo_app_types.helm.apps.base import BaseChartValueProcessor
from apolo_app_types.helm.apps.common import gen_extra_values
from apolo_app_types.helm.apps.ingress import (
    _get_ingress_name_template,
)
from apolo_app_types.helm.utils.dictionaries import get_nested_values
from apolo_app_types.protocols.common.hugging_face import (
    HuggingFaceCache,
    HuggingFaceModel,
)
from apolo_app_types.protocols.common.storage import ApoloFilesPath
from apolo_app_types.protocols.launchpad import (
    CustomLLMModel,
    HuggingFaceEmbeddingsModel,
    HuggingFaceLLMModel,
    LaunchpadAppInputs,
    PreConfiguredEmbeddingsModels,
    PreConfiguredHuggingFaceLLMModel,
    PreConfiguredLLMModels,
)
from apolo_app_types.protocols.postgres import (
    PGBackupConfig,
    PGBouncer,
    PostgresConfig,
    PostgresDBUser,
    PostgresInputs,
)


PASSWORD_CHAR_POOL = string.ascii_letters + string.digits


def _generate_password(length: int = 12) -> str:
    if length < 4:
        err_msg = "Password length must be at least 4"
        raise ValueError(err_msg)

    return "".join([random.choice(PASSWORD_CHAR_POOL) for _ in range(length)])


class LaunchpadChartValueProcessor(BaseChartValueProcessor[LaunchpadAppInputs]):
    async def get_vllm_inputs(
        self,
        input_: LaunchpadAppInputs,
    ) -> LLMInputs:
        llm_extra_args: list[str] = []
        if isinstance(
            input_.apps_config.llm_config.model, PreConfiguredHuggingFaceLLMModel
        ):
            llm_model = HuggingFaceModel(
                model_hf_name=input_.apps_config.llm_config.model.model.value,
                hf_token=input_.apps_config.llm_config.model.hf_token,
            )
            llm_extra_args = input_.apps_config.llm_config.model.server_extra_args
            match input_.apps_config.llm_config.model.model:
                case PreConfiguredLLMModels.MAGISTRAL_24B:
                    llm_extra_args.extend(
                        [
                            "--tokenizer_mode=mistral",
                            "--config_format=mistral",
                            "--load_format=mistral",
                            "--tool-call-parser=mistral",
                            "--enable-auto-tool-choice",
                            "--tensor-parallel-size=2",
                        ]
                    )
        elif isinstance(input_.apps_config.llm_config.model, HuggingFaceLLMModel):
            llm_model = input_.apps_config.llm_config.model.hf_model
            llm_extra_args = input_.apps_config.llm_config.model.server_extra_args
        elif isinstance(input_.apps_config.llm_config.model, CustomLLMModel):
            # For custom models, we use the model_name as both model and tokenizer
            llm_model = HuggingFaceModel(
                model_hf_name=input_.apps_config.llm_config.model.model_name,
            )
            llm_extra_args = input_.apps_config.llm_config.model.server_extra_args
        else:
            err = (
                "Unsupported LLM model type. Expected "
                "PreConfiguredHuggingFaceLLMModel, HuggingFaceLLMModel, "
                "or CustomLLMModel."
            )
            raise ValueError(err)

        # Determine cache configuration based on model type
        if isinstance(input_.apps_config.llm_config.model, CustomLLMModel):
            # For custom models, mount the model path as cache
            cache_config = HuggingFaceCache(
                files_path=input_.apps_config.llm_config.model.model_apolo_path
            )
        else:
            # For HuggingFace models, use the standard cache
            cache_config = HuggingFaceCache(
                files_path=ApoloFilesPath(path="storage:.apps/hugging-face-cache")
            )

        return LLMInputs(
            hugging_face_model=llm_model,
            tokenizer_hf_name=llm_model.model_hf_name,
            preset=input_.apps_config.llm_config.llm_preset,
            server_extra_args=llm_extra_args,
            cache_config=cache_config,
        )

    async def get_postgres_inputs(
        self,
        input_: LaunchpadAppInputs,
    ) -> PostgresInputs:
        return PostgresInputs(
            preset=input_.apps_config.postgres_config.preset,
            postgres_config=PostgresConfig(
                instance_replicas=input_.apps_config.postgres_config.replicas,
                db_users=[PostgresDBUser(name="launchpaduser", db_names=["launchpad"])],
            ),
            pg_bouncer=PGBouncer(
                preset=input_.apps_config.postgres_config.preset,
                replicas=input_.apps_config.postgres_config.replicas,
            ),
            backup=PGBackupConfig(enable=True),
        )

    async def get_text_embeddings_inputs(
        self,
        input_: LaunchpadAppInputs,
    ) -> TextEmbeddingsInferenceAppInputs:
        extra_args: list[str] = []
        if isinstance(
            input_.apps_config.embeddings_config.model,
            PreConfiguredEmbeddingsModels,
        ):
            model_name = input_.apps_config.embeddings_config.model.value
            model = HuggingFaceModel(
                model_hf_name=model_name,
            )
        elif isinstance(
            input_.apps_config.embeddings_config.model,
            HuggingFaceEmbeddingsModel,
        ):
            model = input_.apps_config.embeddings_config.model.hf_model
            extra_args = input_.apps_config.embeddings_config.model.server_extra_args
        else:
            err = "Unsupported embeddings model type."
            raise ValueError(err)

        return TextEmbeddingsInferenceAppInputs(
            model=model,
            preset=input_.apps_config.embeddings_config.preset,
            server_extra_args=extra_args,
        )

    async def gen_extra_values(
        self,
        input_: LaunchpadAppInputs,
        app_name: str,
        namespace: str,
        app_id: str,
        app_secrets_name: str,
        *_: t.Any,
        **kwargs: t.Any,
    ) -> dict[str, t.Any]:
        # may need storage later, especially as cache for pulling models
        # base_app_storage_path = get_app_data_files_path_url(
        #     client=self.client,
        #     app_type_name=str(AppType.Launchpad.value),
        #     app_name=app_name,
        # )
        llm_input = await self.get_vllm_inputs(
            input_,
        )
        postgres_inputs = await self.get_postgres_inputs(
            input_,
        )
        text_embeddings_inputs = await self.get_text_embeddings_inputs(
            input_,
        )

        values = await gen_extra_values(
            apolo_client=self.client,
            preset_type=input_.launchpad_config.preset,
            namespace=namespace,
            app_id=app_id,
            app_type=AppType.Launchpad,
        )
        ingress_template = await _get_ingress_name_template(
            client=self.client,
        )
        domain = ingress_template.split(".", 1)[1]
        keycloak_admin_password = _generate_password()
        db_secret_name = f"launchpad-{app_id}-db-secret"
        realm_import_config_map_name = f"launchpad-{app_id}-keycloak-realm"

        keycloak_values = {
            "fullnameOverride": f"launchpad-{app_id}-keycloak",
            "auth": {
                "adminPassword": keycloak_admin_password,
            },
            "externalDatabase": {"existingSecret": db_secret_name},
            **values,
            "labels": {
                "application": "launchpad",
            },
            "service": {
                "extraLabels": {
                    "service": "keycloak",
                }
            },
            "extraVolumes": [
                {
                    "name": "realm-import",
                    "configMap": {
                        "name": realm_import_config_map_name,
                        "items": [
                            {
                                "key": "realm.json",
                                "path": "realm.json",
                            }
                        ],
                    },
                }
            ],
        }

        return {
            **values,
            "dbSecretName": db_secret_name,
            "keycloakRealmImportConfigMapName": realm_import_config_map_name,
            "postgresql": {
                "fullnameOverride": f"launchpad-{app_id}-db",
                "auth": {
                    "existingSecret": db_secret_name,
                },
            },
            "dbPassword": _generate_password(),
            "domain": domain,
            "keycloak": keycloak_values,  # keeping this for backwards compatibility
            "mlops-keycloak": keycloak_values,
            "LAUNCHPAD_ADMIN_PASSWORD": _generate_password(),
            "LAUNCHPAD_INITIAL_CONFIG": json.dumps(
                {
                    "vllm": get_nested_values(
                        llm_input.model_dump(),
                        [
                            "hugging_face_model",
                            "preset",
                            "server_extra_args",
                            "cache_config",
                        ],
                    ),
                    "postgres": get_nested_values(
                        postgres_inputs.model_dump(),
                        ["preset", "pg_bouncer.preset"],
                    ),
                    "text-embeddings": get_nested_values(
                        text_embeddings_inputs.model_dump(),
                        ["model", "preset", "server_extra_args"],
                    ),
                }
            ),
        }
