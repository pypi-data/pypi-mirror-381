from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.apihub.v1 import common_fields_pb2 as _common_fields_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ACTION_TYPE_UNSPECIFIED: _ClassVar[ActionType]
    SYNC_METADATA: _ClassVar[ActionType]
    SYNC_RUNTIME_DATA: _ClassVar[ActionType]

class GatewayType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GATEWAY_TYPE_UNSPECIFIED: _ClassVar[GatewayType]
    APIGEE_X_AND_HYBRID: _ClassVar[GatewayType]
    APIGEE_EDGE_PUBLIC_CLOUD: _ClassVar[GatewayType]
    APIGEE_EDGE_PRIVATE_CLOUD: _ClassVar[GatewayType]
    CLOUD_API_GATEWAY: _ClassVar[GatewayType]
    CLOUD_ENDPOINTS: _ClassVar[GatewayType]
    API_DISCOVERY: _ClassVar[GatewayType]
    OTHERS: _ClassVar[GatewayType]

class CurationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CURATION_TYPE_UNSPECIFIED: _ClassVar[CurationType]
    DEFAULT_CURATION_FOR_API_METADATA: _ClassVar[CurationType]
    CUSTOM_CURATION_FOR_API_METADATA: _ClassVar[CurationType]
ACTION_TYPE_UNSPECIFIED: ActionType
SYNC_METADATA: ActionType
SYNC_RUNTIME_DATA: ActionType
GATEWAY_TYPE_UNSPECIFIED: GatewayType
APIGEE_X_AND_HYBRID: GatewayType
APIGEE_EDGE_PUBLIC_CLOUD: GatewayType
APIGEE_EDGE_PRIVATE_CLOUD: GatewayType
CLOUD_API_GATEWAY: GatewayType
CLOUD_ENDPOINTS: GatewayType
API_DISCOVERY: GatewayType
OTHERS: GatewayType
CURATION_TYPE_UNSPECIFIED: CurationType
DEFAULT_CURATION_FOR_API_METADATA: CurationType
CUSTOM_CURATION_FOR_API_METADATA: CurationType

class Plugin(_message.Message):
    __slots__ = ('name', 'display_name', 'type', 'description', 'state', 'ownership_type', 'hosting_service', 'actions_config', 'documentation', 'plugin_category', 'config_template', 'create_time', 'update_time', 'gateway_type')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Plugin.State]
        ENABLED: _ClassVar[Plugin.State]
        DISABLED: _ClassVar[Plugin.State]
    STATE_UNSPECIFIED: Plugin.State
    ENABLED: Plugin.State
    DISABLED: Plugin.State

    class OwnershipType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OWNERSHIP_TYPE_UNSPECIFIED: _ClassVar[Plugin.OwnershipType]
        SYSTEM_OWNED: _ClassVar[Plugin.OwnershipType]
        USER_OWNED: _ClassVar[Plugin.OwnershipType]
    OWNERSHIP_TYPE_UNSPECIFIED: Plugin.OwnershipType
    SYSTEM_OWNED: Plugin.OwnershipType
    USER_OWNED: Plugin.OwnershipType

    class HostingService(_message.Message):
        __slots__ = ('service_uri',)
        SERVICE_URI_FIELD_NUMBER: _ClassVar[int]
        service_uri: str

        def __init__(self, service_uri: _Optional[str]=...) -> None:
            ...

    class ConfigTemplate(_message.Message):
        __slots__ = ('auth_config_template', 'additional_config_template')

        class AuthConfigTemplate(_message.Message):
            __slots__ = ('supported_auth_types', 'service_account')
            SUPPORTED_AUTH_TYPES_FIELD_NUMBER: _ClassVar[int]
            SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
            supported_auth_types: _containers.RepeatedScalarFieldContainer[_common_fields_pb2.AuthType]
            service_account: _common_fields_pb2.GoogleServiceAccountConfig

            def __init__(self, supported_auth_types: _Optional[_Iterable[_Union[_common_fields_pb2.AuthType, str]]]=..., service_account: _Optional[_Union[_common_fields_pb2.GoogleServiceAccountConfig, _Mapping]]=...) -> None:
                ...
        AUTH_CONFIG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_CONFIG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
        auth_config_template: Plugin.ConfigTemplate.AuthConfigTemplate
        additional_config_template: _containers.RepeatedCompositeFieldContainer[_common_fields_pb2.ConfigVariableTemplate]

        def __init__(self, auth_config_template: _Optional[_Union[Plugin.ConfigTemplate.AuthConfigTemplate, _Mapping]]=..., additional_config_template: _Optional[_Iterable[_Union[_common_fields_pb2.ConfigVariableTemplate, _Mapping]]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OWNERSHIP_TYPE_FIELD_NUMBER: _ClassVar[int]
    HOSTING_SERVICE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_CONFIG_FIELD_NUMBER: _ClassVar[int]
    DOCUMENTATION_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    CONFIG_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    GATEWAY_TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    type: _common_fields_pb2.AttributeValues
    description: str
    state: Plugin.State
    ownership_type: Plugin.OwnershipType
    hosting_service: Plugin.HostingService
    actions_config: _containers.RepeatedCompositeFieldContainer[PluginActionConfig]
    documentation: _common_fields_pb2.Documentation
    plugin_category: _common_fields_pb2.PluginCategory
    config_template: Plugin.ConfigTemplate
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    gateway_type: GatewayType

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., type: _Optional[_Union[_common_fields_pb2.AttributeValues, _Mapping]]=..., description: _Optional[str]=..., state: _Optional[_Union[Plugin.State, str]]=..., ownership_type: _Optional[_Union[Plugin.OwnershipType, str]]=..., hosting_service: _Optional[_Union[Plugin.HostingService, _Mapping]]=..., actions_config: _Optional[_Iterable[_Union[PluginActionConfig, _Mapping]]]=..., documentation: _Optional[_Union[_common_fields_pb2.Documentation, _Mapping]]=..., plugin_category: _Optional[_Union[_common_fields_pb2.PluginCategory, str]]=..., config_template: _Optional[_Union[Plugin.ConfigTemplate, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., gateway_type: _Optional[_Union[GatewayType, str]]=...) -> None:
        ...

class PluginActionConfig(_message.Message):
    __slots__ = ('id', 'display_name', 'description', 'trigger_mode')

    class TriggerMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TRIGGER_MODE_UNSPECIFIED: _ClassVar[PluginActionConfig.TriggerMode]
        API_HUB_ON_DEMAND_TRIGGER: _ClassVar[PluginActionConfig.TriggerMode]
        API_HUB_SCHEDULE_TRIGGER: _ClassVar[PluginActionConfig.TriggerMode]
        NON_API_HUB_MANAGED: _ClassVar[PluginActionConfig.TriggerMode]
    TRIGGER_MODE_UNSPECIFIED: PluginActionConfig.TriggerMode
    API_HUB_ON_DEMAND_TRIGGER: PluginActionConfig.TriggerMode
    API_HUB_SCHEDULE_TRIGGER: PluginActionConfig.TriggerMode
    NON_API_HUB_MANAGED: PluginActionConfig.TriggerMode
    ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MODE_FIELD_NUMBER: _ClassVar[int]
    id: str
    display_name: str
    description: str
    trigger_mode: PluginActionConfig.TriggerMode

    def __init__(self, id: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., trigger_mode: _Optional[_Union[PluginActionConfig.TriggerMode, str]]=...) -> None:
        ...

class GetPluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class EnablePluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DisablePluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class PluginInstanceAction(_message.Message):
    __slots__ = ('hub_instance_action', 'action_id', 'state', 'schedule_cron_expression', 'curation_config', 'schedule_time_zone', 'service_account', 'resource_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PluginInstanceAction.State]
        ENABLED: _ClassVar[PluginInstanceAction.State]
        DISABLED: _ClassVar[PluginInstanceAction.State]
        ENABLING: _ClassVar[PluginInstanceAction.State]
        DISABLING: _ClassVar[PluginInstanceAction.State]
        ERROR: _ClassVar[PluginInstanceAction.State]
    STATE_UNSPECIFIED: PluginInstanceAction.State
    ENABLED: PluginInstanceAction.State
    DISABLED: PluginInstanceAction.State
    ENABLING: PluginInstanceAction.State
    DISABLING: PluginInstanceAction.State
    ERROR: PluginInstanceAction.State

    class ResourceConfig(_message.Message):
        __slots__ = ('action_type', 'pubsub_topic')
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        PUBSUB_TOPIC_FIELD_NUMBER: _ClassVar[int]
        action_type: ActionType
        pubsub_topic: str

        def __init__(self, action_type: _Optional[_Union[ActionType, str]]=..., pubsub_topic: _Optional[str]=...) -> None:
            ...
    HUB_INSTANCE_ACTION_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_CRON_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    CURATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    SCHEDULE_TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    hub_instance_action: ExecutionStatus
    action_id: str
    state: PluginInstanceAction.State
    schedule_cron_expression: str
    curation_config: CurationConfig
    schedule_time_zone: str
    service_account: str
    resource_config: PluginInstanceAction.ResourceConfig

    def __init__(self, hub_instance_action: _Optional[_Union[ExecutionStatus, _Mapping]]=..., action_id: _Optional[str]=..., state: _Optional[_Union[PluginInstanceAction.State, str]]=..., schedule_cron_expression: _Optional[str]=..., curation_config: _Optional[_Union[CurationConfig, _Mapping]]=..., schedule_time_zone: _Optional[str]=..., service_account: _Optional[str]=..., resource_config: _Optional[_Union[PluginInstanceAction.ResourceConfig, _Mapping]]=...) -> None:
        ...

class PluginInstance(_message.Message):
    __slots__ = ('name', 'display_name', 'auth_config', 'additional_config', 'state', 'error_message', 'actions', 'create_time', 'update_time', 'source_project_id')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PluginInstance.State]
        CREATING: _ClassVar[PluginInstance.State]
        ACTIVE: _ClassVar[PluginInstance.State]
        APPLYING_CONFIG: _ClassVar[PluginInstance.State]
        ERROR: _ClassVar[PluginInstance.State]
        FAILED: _ClassVar[PluginInstance.State]
        DELETING: _ClassVar[PluginInstance.State]
    STATE_UNSPECIFIED: PluginInstance.State
    CREATING: PluginInstance.State
    ACTIVE: PluginInstance.State
    APPLYING_CONFIG: PluginInstance.State
    ERROR: PluginInstance.State
    FAILED: PluginInstance.State
    DELETING: PluginInstance.State

    class AdditionalConfigEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_fields_pb2.ConfigVariable

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_common_fields_pb2.ConfigVariable, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    AUTH_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    auth_config: _common_fields_pb2.AuthConfig
    additional_config: _containers.MessageMap[str, _common_fields_pb2.ConfigVariable]
    state: PluginInstance.State
    error_message: str
    actions: _containers.RepeatedCompositeFieldContainer[PluginInstanceAction]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    source_project_id: str

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., auth_config: _Optional[_Union[_common_fields_pb2.AuthConfig, _Mapping]]=..., additional_config: _Optional[_Mapping[str, _common_fields_pb2.ConfigVariable]]=..., state: _Optional[_Union[PluginInstance.State, str]]=..., error_message: _Optional[str]=..., actions: _Optional[_Iterable[_Union[PluginInstanceAction, _Mapping]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., source_project_id: _Optional[str]=...) -> None:
        ...

class CurationConfig(_message.Message):
    __slots__ = ('custom_curation', 'curation_type')

    class CustomCuration(_message.Message):
        __slots__ = ('curation',)
        CURATION_FIELD_NUMBER: _ClassVar[int]
        curation: str

        def __init__(self, curation: _Optional[str]=...) -> None:
            ...
    CUSTOM_CURATION_FIELD_NUMBER: _ClassVar[int]
    CURATION_TYPE_FIELD_NUMBER: _ClassVar[int]
    custom_curation: CurationConfig.CustomCuration
    curation_type: CurationType

    def __init__(self, custom_curation: _Optional[_Union[CurationConfig.CustomCuration, _Mapping]]=..., curation_type: _Optional[_Union[CurationType, str]]=...) -> None:
        ...

class ExecutionStatus(_message.Message):
    __slots__ = ('current_execution_state', 'last_execution')

    class CurrentExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CURRENT_EXECUTION_STATE_UNSPECIFIED: _ClassVar[ExecutionStatus.CurrentExecutionState]
        RUNNING: _ClassVar[ExecutionStatus.CurrentExecutionState]
        NOT_RUNNING: _ClassVar[ExecutionStatus.CurrentExecutionState]
    CURRENT_EXECUTION_STATE_UNSPECIFIED: ExecutionStatus.CurrentExecutionState
    RUNNING: ExecutionStatus.CurrentExecutionState
    NOT_RUNNING: ExecutionStatus.CurrentExecutionState

    class LastExecution(_message.Message):
        __slots__ = ('result', 'error_message', 'start_time', 'end_time')

        class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RESULT_UNSPECIFIED: _ClassVar[ExecutionStatus.LastExecution.Result]
            SUCCEEDED: _ClassVar[ExecutionStatus.LastExecution.Result]
            FAILED: _ClassVar[ExecutionStatus.LastExecution.Result]
        RESULT_UNSPECIFIED: ExecutionStatus.LastExecution.Result
        SUCCEEDED: ExecutionStatus.LastExecution.Result
        FAILED: ExecutionStatus.LastExecution.Result
        RESULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        result: ExecutionStatus.LastExecution.Result
        error_message: str
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, result: _Optional[_Union[ExecutionStatus.LastExecution.Result, str]]=..., error_message: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    CURRENT_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_FIELD_NUMBER: _ClassVar[int]
    current_execution_state: ExecutionStatus.CurrentExecutionState
    last_execution: ExecutionStatus.LastExecution

    def __init__(self, current_execution_state: _Optional[_Union[ExecutionStatus.CurrentExecutionState, str]]=..., last_execution: _Optional[_Union[ExecutionStatus.LastExecution, _Mapping]]=...) -> None:
        ...

class CreatePluginRequest(_message.Message):
    __slots__ = ('parent', 'plugin_id', 'plugin')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    plugin_id: str
    plugin: Plugin

    def __init__(self, parent: _Optional[str]=..., plugin_id: _Optional[str]=..., plugin: _Optional[_Union[Plugin, _Mapping]]=...) -> None:
        ...

class DeletePluginRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPluginsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPluginsResponse(_message.Message):
    __slots__ = ('plugins', 'next_page_token')
    PLUGINS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    plugins: _containers.RepeatedCompositeFieldContainer[Plugin]
    next_page_token: str

    def __init__(self, plugins: _Optional[_Iterable[_Union[Plugin, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreatePluginInstanceRequest(_message.Message):
    __slots__ = ('parent', 'plugin_instance_id', 'plugin_instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    plugin_instance_id: str
    plugin_instance: PluginInstance

    def __init__(self, parent: _Optional[str]=..., plugin_instance_id: _Optional[str]=..., plugin_instance: _Optional[_Union[PluginInstance, _Mapping]]=...) -> None:
        ...

class ExecutePluginInstanceActionRequest(_message.Message):
    __slots__ = ('name', 'action_execution_detail')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_EXECUTION_DETAIL_FIELD_NUMBER: _ClassVar[int]
    name: str
    action_execution_detail: ActionExecutionDetail

    def __init__(self, name: _Optional[str]=..., action_execution_detail: _Optional[_Union[ActionExecutionDetail, _Mapping]]=...) -> None:
        ...

class ActionExecutionDetail(_message.Message):
    __slots__ = ('action_id',)
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    action_id: str

    def __init__(self, action_id: _Optional[str]=...) -> None:
        ...

class ExecutePluginInstanceActionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GetPluginInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPluginInstancesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPluginInstancesResponse(_message.Message):
    __slots__ = ('plugin_instances', 'next_page_token')
    PLUGIN_INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    plugin_instances: _containers.RepeatedCompositeFieldContainer[PluginInstance]
    next_page_token: str

    def __init__(self, plugin_instances: _Optional[_Iterable[_Union[PluginInstance, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class EnablePluginInstanceActionRequest(_message.Message):
    __slots__ = ('name', 'action_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    action_id: str

    def __init__(self, name: _Optional[str]=..., action_id: _Optional[str]=...) -> None:
        ...

class EnablePluginInstanceActionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class DisablePluginInstanceActionRequest(_message.Message):
    __slots__ = ('name', 'action_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    action_id: str

    def __init__(self, name: _Optional[str]=..., action_id: _Optional[str]=...) -> None:
        ...

class DisablePluginInstanceActionResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UpdatePluginInstanceRequest(_message.Message):
    __slots__ = ('plugin_instance', 'update_mask')
    PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    plugin_instance: PluginInstance
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, plugin_instance: _Optional[_Union[PluginInstance, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePluginInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...