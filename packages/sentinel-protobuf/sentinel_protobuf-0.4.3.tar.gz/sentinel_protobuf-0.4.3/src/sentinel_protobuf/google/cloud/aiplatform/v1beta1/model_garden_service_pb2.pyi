from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as _machine_resources_pb2
from google.cloud.aiplatform.v1beta1 import model_pb2 as _model_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import publisher_model_pb2 as _publisher_model_pb2
from google.cloud.aiplatform.v1beta1 import service_networking_pb2 as _service_networking_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PublisherModelView(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PUBLISHER_MODEL_VIEW_UNSPECIFIED: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VIEW_BASIC: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VIEW_FULL: _ClassVar[PublisherModelView]
    PUBLISHER_MODEL_VERSION_VIEW_BASIC: _ClassVar[PublisherModelView]
PUBLISHER_MODEL_VIEW_UNSPECIFIED: PublisherModelView
PUBLISHER_MODEL_VIEW_BASIC: PublisherModelView
PUBLISHER_MODEL_VIEW_FULL: PublisherModelView
PUBLISHER_MODEL_VERSION_VIEW_BASIC: PublisherModelView

class GetPublisherModelRequest(_message.Message):
    __slots__ = ('name', 'language_code', 'view', 'is_hugging_face_model', 'hugging_face_token', 'include_equivalent_model_garden_model_deployment_configs')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    IS_HUGGING_FACE_MODEL_FIELD_NUMBER: _ClassVar[int]
    HUGGING_FACE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_EQUIVALENT_MODEL_GARDEN_MODEL_DEPLOYMENT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    view: PublisherModelView
    is_hugging_face_model: bool
    hugging_face_token: str
    include_equivalent_model_garden_model_deployment_configs: bool

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=..., view: _Optional[_Union[PublisherModelView, str]]=..., is_hugging_face_model: bool=..., hugging_face_token: _Optional[str]=..., include_equivalent_model_garden_model_deployment_configs: bool=...) -> None:
        ...

class ListPublisherModelsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'view', 'order_by', 'language_code', 'list_all_versions')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    VIEW_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    LIST_ALL_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    view: PublisherModelView
    order_by: str
    language_code: str
    list_all_versions: bool

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., view: _Optional[_Union[PublisherModelView, str]]=..., order_by: _Optional[str]=..., language_code: _Optional[str]=..., list_all_versions: bool=...) -> None:
        ...

class ListPublisherModelsResponse(_message.Message):
    __slots__ = ('publisher_models', 'next_page_token')
    PUBLISHER_MODELS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    publisher_models: _containers.RepeatedCompositeFieldContainer[_publisher_model_pb2.PublisherModel]
    next_page_token: str

    def __init__(self, publisher_models: _Optional[_Iterable[_Union[_publisher_model_pb2.PublisherModel, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeployRequest(_message.Message):
    __slots__ = ('publisher_model_name', 'hugging_face_model_id', 'custom_model', 'destination', 'model_config', 'endpoint_config', 'deploy_config')

    class CustomModel(_message.Message):
        __slots__ = ('gcs_uri',)
        GCS_URI_FIELD_NUMBER: _ClassVar[int]
        gcs_uri: str

        def __init__(self, gcs_uri: _Optional[str]=...) -> None:
            ...

    class ModelConfig(_message.Message):
        __slots__ = ('accept_eula', 'hugging_face_access_token', 'hugging_face_cache_enabled', 'model_display_name', 'container_spec', 'model_user_id')
        ACCEPT_EULA_FIELD_NUMBER: _ClassVar[int]
        HUGGING_FACE_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        HUGGING_FACE_CACHE_ENABLED_FIELD_NUMBER: _ClassVar[int]
        MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        CONTAINER_SPEC_FIELD_NUMBER: _ClassVar[int]
        MODEL_USER_ID_FIELD_NUMBER: _ClassVar[int]
        accept_eula: bool
        hugging_face_access_token: str
        hugging_face_cache_enabled: bool
        model_display_name: str
        container_spec: _model_pb2.ModelContainerSpec
        model_user_id: str

        def __init__(self, accept_eula: bool=..., hugging_face_access_token: _Optional[str]=..., hugging_face_cache_enabled: bool=..., model_display_name: _Optional[str]=..., container_spec: _Optional[_Union[_model_pb2.ModelContainerSpec, _Mapping]]=..., model_user_id: _Optional[str]=...) -> None:
            ...

    class EndpointConfig(_message.Message):
        __slots__ = ('endpoint_display_name', 'dedicated_endpoint_enabled', 'dedicated_endpoint_disabled', 'private_service_connect_config', 'endpoint_user_id')
        ENDPOINT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        DEDICATED_ENDPOINT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        DEDICATED_ENDPOINT_DISABLED_FIELD_NUMBER: _ClassVar[int]
        PRIVATE_SERVICE_CONNECT_CONFIG_FIELD_NUMBER: _ClassVar[int]
        ENDPOINT_USER_ID_FIELD_NUMBER: _ClassVar[int]
        endpoint_display_name: str
        dedicated_endpoint_enabled: bool
        dedicated_endpoint_disabled: bool
        private_service_connect_config: _service_networking_pb2.PrivateServiceConnectConfig
        endpoint_user_id: str

        def __init__(self, endpoint_display_name: _Optional[str]=..., dedicated_endpoint_enabled: bool=..., dedicated_endpoint_disabled: bool=..., private_service_connect_config: _Optional[_Union[_service_networking_pb2.PrivateServiceConnectConfig, _Mapping]]=..., endpoint_user_id: _Optional[str]=...) -> None:
            ...

    class DeployConfig(_message.Message):
        __slots__ = ('dedicated_resources', 'fast_tryout_enabled', 'system_labels')

        class SystemLabelsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        FAST_TRYOUT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SYSTEM_LABELS_FIELD_NUMBER: _ClassVar[int]
        dedicated_resources: _machine_resources_pb2.DedicatedResources
        fast_tryout_enabled: bool
        system_labels: _containers.ScalarMap[str, str]

        def __init__(self, dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]]=..., fast_tryout_enabled: bool=..., system_labels: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    PUBLISHER_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    HUGGING_FACE_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    MODEL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DEPLOY_CONFIG_FIELD_NUMBER: _ClassVar[int]
    publisher_model_name: str
    hugging_face_model_id: str
    custom_model: DeployRequest.CustomModel
    destination: str
    model_config: DeployRequest.ModelConfig
    endpoint_config: DeployRequest.EndpointConfig
    deploy_config: DeployRequest.DeployConfig

    def __init__(self, publisher_model_name: _Optional[str]=..., hugging_face_model_id: _Optional[str]=..., custom_model: _Optional[_Union[DeployRequest.CustomModel, _Mapping]]=..., destination: _Optional[str]=..., model_config: _Optional[_Union[DeployRequest.ModelConfig, _Mapping]]=..., endpoint_config: _Optional[_Union[DeployRequest.EndpointConfig, _Mapping]]=..., deploy_config: _Optional[_Union[DeployRequest.DeployConfig, _Mapping]]=...) -> None:
        ...

class DeployPublisherModelRequest(_message.Message):
    __slots__ = ('model', 'destination', 'endpoint_display_name', 'dedicated_resources', 'model_display_name', 'hugging_face_access_token', 'accept_eula')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DEDICATED_RESOURCES_FIELD_NUMBER: _ClassVar[int]
    MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    HUGGING_FACE_ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCEPT_EULA_FIELD_NUMBER: _ClassVar[int]
    model: str
    destination: str
    endpoint_display_name: str
    dedicated_resources: _machine_resources_pb2.DedicatedResources
    model_display_name: str
    hugging_face_access_token: str
    accept_eula: bool

    def __init__(self, model: _Optional[str]=..., destination: _Optional[str]=..., endpoint_display_name: _Optional[str]=..., dedicated_resources: _Optional[_Union[_machine_resources_pb2.DedicatedResources, _Mapping]]=..., model_display_name: _Optional[str]=..., hugging_face_access_token: _Optional[str]=..., accept_eula: bool=...) -> None:
        ...

class DeployResponse(_message.Message):
    __slots__ = ('publisher_model', 'endpoint', 'model')
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    publisher_model: str
    endpoint: str
    model: str

    def __init__(self, publisher_model: _Optional[str]=..., endpoint: _Optional[str]=..., model: _Optional[str]=...) -> None:
        ...

class DeployPublisherModelResponse(_message.Message):
    __slots__ = ('publisher_model', 'endpoint', 'model')
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    publisher_model: str
    endpoint: str
    model: str

    def __init__(self, publisher_model: _Optional[str]=..., endpoint: _Optional[str]=..., model: _Optional[str]=...) -> None:
        ...

class DeployOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'publisher_model', 'destination', 'project_number', 'model_id')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    publisher_model: str
    destination: str
    project_number: int
    model_id: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., publisher_model: _Optional[str]=..., destination: _Optional[str]=..., project_number: _Optional[int]=..., model_id: _Optional[str]=...) -> None:
        ...

class DeployPublisherModelOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'publisher_model', 'destination', 'project_number')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    publisher_model: str
    destination: str
    project_number: int

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., publisher_model: _Optional[str]=..., destination: _Optional[str]=..., project_number: _Optional[int]=...) -> None:
        ...

class ExportPublisherModelResponse(_message.Message):
    __slots__ = ('publisher_model', 'destination_uri')
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_URI_FIELD_NUMBER: _ClassVar[int]
    publisher_model: str
    destination_uri: str

    def __init__(self, publisher_model: _Optional[str]=..., destination_uri: _Optional[str]=...) -> None:
        ...

class ExportPublisherModelOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ExportPublisherModelRequest(_message.Message):
    __slots__ = ('name', 'destination', 'parent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    destination: _io_pb2.GcsDestination
    parent: str

    def __init__(self, name: _Optional[str]=..., destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=..., parent: _Optional[str]=...) -> None:
        ...

class CheckPublisherModelEulaAcceptanceRequest(_message.Message):
    __slots__ = ('parent', 'publisher_model')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    publisher_model: str

    def __init__(self, parent: _Optional[str]=..., publisher_model: _Optional[str]=...) -> None:
        ...

class AcceptPublisherModelEulaRequest(_message.Message):
    __slots__ = ('parent', 'publisher_model')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    publisher_model: str

    def __init__(self, parent: _Optional[str]=..., publisher_model: _Optional[str]=...) -> None:
        ...

class PublisherModelEulaAcceptance(_message.Message):
    __slots__ = ('project_number', 'publisher_model', 'publisher_model_eula_acked')
    PROJECT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_MODEL_EULA_ACKED_FIELD_NUMBER: _ClassVar[int]
    project_number: int
    publisher_model: str
    publisher_model_eula_acked: bool

    def __init__(self, project_number: _Optional[int]=..., publisher_model: _Optional[str]=..., publisher_model_eula_acked: bool=...) -> None:
        ...