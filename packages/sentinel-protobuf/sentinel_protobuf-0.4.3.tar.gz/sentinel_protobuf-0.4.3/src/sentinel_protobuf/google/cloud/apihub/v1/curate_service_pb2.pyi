from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateCurationRequest(_message.Message):
    __slots__ = ('parent', 'curation_id', 'curation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CURATION_ID_FIELD_NUMBER: _ClassVar[int]
    CURATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    curation_id: str
    curation: Curation

    def __init__(self, parent: _Optional[str]=..., curation_id: _Optional[str]=..., curation: _Optional[_Union[Curation, _Mapping]]=...) -> None:
        ...

class GetCurationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateCurationRequest(_message.Message):
    __slots__ = ('curation', 'update_mask')
    CURATION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    curation: Curation
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, curation: _Optional[_Union[Curation, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCurationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCurationsRequest(_message.Message):
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

class ListCurationsResponse(_message.Message):
    __slots__ = ('curations', 'next_page_token')
    CURATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    curations: _containers.RepeatedCompositeFieldContainer[Curation]
    next_page_token: str

    def __init__(self, curations: _Optional[_Iterable[_Union[Curation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Curation(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'endpoint', 'plugin_instance_actions', 'last_execution_state', 'last_execution_error_code', 'last_execution_error_message', 'create_time', 'update_time')

    class LastExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAST_EXECUTION_STATE_UNSPECIFIED: _ClassVar[Curation.LastExecutionState]
        SUCCEEDED: _ClassVar[Curation.LastExecutionState]
        FAILED: _ClassVar[Curation.LastExecutionState]
    LAST_EXECUTION_STATE_UNSPECIFIED: Curation.LastExecutionState
    SUCCEEDED: Curation.LastExecutionState
    FAILED: Curation.LastExecutionState

    class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ERROR_CODE_UNSPECIFIED: _ClassVar[Curation.ErrorCode]
        INTERNAL_ERROR: _ClassVar[Curation.ErrorCode]
        UNAUTHORIZED: _ClassVar[Curation.ErrorCode]
    ERROR_CODE_UNSPECIFIED: Curation.ErrorCode
    INTERNAL_ERROR: Curation.ErrorCode
    UNAUTHORIZED: Curation.ErrorCode

    class PluginInstanceActionID(_message.Message):
        __slots__ = ('plugin_instance', 'action_id')
        PLUGIN_INSTANCE_FIELD_NUMBER: _ClassVar[int]
        ACTION_ID_FIELD_NUMBER: _ClassVar[int]
        plugin_instance: str
        action_id: str

        def __init__(self, plugin_instance: _Optional[str]=..., action_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    PLUGIN_INSTANCE_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    LAST_EXECUTION_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    endpoint: Endpoint
    plugin_instance_actions: _containers.RepeatedCompositeFieldContainer[Curation.PluginInstanceActionID]
    last_execution_state: Curation.LastExecutionState
    last_execution_error_code: Curation.ErrorCode
    last_execution_error_message: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., endpoint: _Optional[_Union[Endpoint, _Mapping]]=..., plugin_instance_actions: _Optional[_Iterable[_Union[Curation.PluginInstanceActionID, _Mapping]]]=..., last_execution_state: _Optional[_Union[Curation.LastExecutionState, str]]=..., last_execution_error_code: _Optional[_Union[Curation.ErrorCode, str]]=..., last_execution_error_message: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class Endpoint(_message.Message):
    __slots__ = ('application_integration_endpoint_details',)
    APPLICATION_INTEGRATION_ENDPOINT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    application_integration_endpoint_details: ApplicationIntegrationEndpointDetails

    def __init__(self, application_integration_endpoint_details: _Optional[_Union[ApplicationIntegrationEndpointDetails, _Mapping]]=...) -> None:
        ...

class ApplicationIntegrationEndpointDetails(_message.Message):
    __slots__ = ('uri', 'trigger_id')
    URI_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_ID_FIELD_NUMBER: _ClassVar[int]
    uri: str
    trigger_id: str

    def __init__(self, uri: _Optional[str]=..., trigger_id: _Optional[str]=...) -> None:
        ...