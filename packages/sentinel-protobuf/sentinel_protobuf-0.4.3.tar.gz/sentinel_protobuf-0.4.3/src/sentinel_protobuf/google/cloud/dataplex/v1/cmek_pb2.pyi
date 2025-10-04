from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import service_pb2 as _service_pb2
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

class EncryptionConfig(_message.Message):
    __slots__ = ('name', 'key', 'create_time', 'update_time', 'encryption_state', 'etag', 'failure_details')

    class EncryptionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ENCRYPTION_STATE_UNSPECIFIED: _ClassVar[EncryptionConfig.EncryptionState]
        ENCRYPTING: _ClassVar[EncryptionConfig.EncryptionState]
        COMPLETED: _ClassVar[EncryptionConfig.EncryptionState]
        FAILED: _ClassVar[EncryptionConfig.EncryptionState]
    ENCRYPTION_STATE_UNSPECIFIED: EncryptionConfig.EncryptionState
    ENCRYPTING: EncryptionConfig.EncryptionState
    COMPLETED: EncryptionConfig.EncryptionState
    FAILED: EncryptionConfig.EncryptionState

    class FailureDetails(_message.Message):
        __slots__ = ('error_code', 'error_message')

        class ErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UNKNOWN: _ClassVar[EncryptionConfig.FailureDetails.ErrorCode]
            INTERNAL_ERROR: _ClassVar[EncryptionConfig.FailureDetails.ErrorCode]
            REQUIRE_USER_ACTION: _ClassVar[EncryptionConfig.FailureDetails.ErrorCode]
        UNKNOWN: EncryptionConfig.FailureDetails.ErrorCode
        INTERNAL_ERROR: EncryptionConfig.FailureDetails.ErrorCode
        REQUIRE_USER_ACTION: EncryptionConfig.FailureDetails.ErrorCode
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        error_code: EncryptionConfig.FailureDetails.ErrorCode
        error_message: str

        def __init__(self, error_code: _Optional[_Union[EncryptionConfig.FailureDetails.ErrorCode, str]]=..., error_message: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    FAILURE_DETAILS_FIELD_NUMBER: _ClassVar[int]
    name: str
    key: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    encryption_state: EncryptionConfig.EncryptionState
    etag: str
    failure_details: EncryptionConfig.FailureDetails

    def __init__(self, name: _Optional[str]=..., key: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., encryption_state: _Optional[_Union[EncryptionConfig.EncryptionState, str]]=..., etag: _Optional[str]=..., failure_details: _Optional[_Union[EncryptionConfig.FailureDetails, _Mapping]]=...) -> None:
        ...

class CreateEncryptionConfigRequest(_message.Message):
    __slots__ = ('parent', 'encryption_config_id', 'encryption_config')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    parent: str
    encryption_config_id: str
    encryption_config: EncryptionConfig

    def __init__(self, parent: _Optional[str]=..., encryption_config_id: _Optional[str]=..., encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=...) -> None:
        ...

class GetEncryptionConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateEncryptionConfigRequest(_message.Message):
    __slots__ = ('encryption_config', 'update_mask')
    ENCRYPTION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    encryption_config: EncryptionConfig
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, encryption_config: _Optional[_Union[EncryptionConfig, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteEncryptionConfigRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class ListEncryptionConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListEncryptionConfigsResponse(_message.Message):
    __slots__ = ('encryption_configs', 'next_page_token', 'unreachable_locations')
    ENCRYPTION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    encryption_configs: _containers.RepeatedCompositeFieldContainer[EncryptionConfig]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, encryption_configs: _Optional[_Iterable[_Union[EncryptionConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...