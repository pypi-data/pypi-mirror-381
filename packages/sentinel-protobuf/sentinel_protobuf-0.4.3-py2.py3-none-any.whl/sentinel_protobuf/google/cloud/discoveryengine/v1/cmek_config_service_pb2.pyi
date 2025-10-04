from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class UpdateCmekConfigRequest(_message.Message):
    __slots__ = ('config', 'set_default')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    SET_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    config: CmekConfig
    set_default: bool

    def __init__(self, config: _Optional[_Union[CmekConfig, _Mapping]]=..., set_default: bool=...) -> None:
        ...

class GetCmekConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class SingleRegionKey(_message.Message):
    __slots__ = ('kms_key',)
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    kms_key: str

    def __init__(self, kms_key: _Optional[str]=...) -> None:
        ...

class CmekConfig(_message.Message):
    __slots__ = ('name', 'kms_key', 'kms_key_version', 'state', 'is_default', 'last_rotation_timestamp_micros', 'single_region_keys', 'notebooklm_state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CmekConfig.State]
        CREATING: _ClassVar[CmekConfig.State]
        ACTIVE: _ClassVar[CmekConfig.State]
        KEY_ISSUE: _ClassVar[CmekConfig.State]
        DELETING: _ClassVar[CmekConfig.State]
        DELETE_FAILED: _ClassVar[CmekConfig.State]
        UNUSABLE: _ClassVar[CmekConfig.State]
        ACTIVE_ROTATING: _ClassVar[CmekConfig.State]
        DELETED: _ClassVar[CmekConfig.State]
    STATE_UNSPECIFIED: CmekConfig.State
    CREATING: CmekConfig.State
    ACTIVE: CmekConfig.State
    KEY_ISSUE: CmekConfig.State
    DELETING: CmekConfig.State
    DELETE_FAILED: CmekConfig.State
    UNUSABLE: CmekConfig.State
    ACTIVE_ROTATING: CmekConfig.State
    DELETED: CmekConfig.State

    class NotebookLMState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOTEBOOK_LM_STATE_UNSPECIFIED: _ClassVar[CmekConfig.NotebookLMState]
        NOTEBOOK_LM_NOT_READY: _ClassVar[CmekConfig.NotebookLMState]
        NOTEBOOK_LM_READY: _ClassVar[CmekConfig.NotebookLMState]
        NOTEBOOK_LM_NOT_ENABLED: _ClassVar[CmekConfig.NotebookLMState]
    NOTEBOOK_LM_STATE_UNSPECIFIED: CmekConfig.NotebookLMState
    NOTEBOOK_LM_NOT_READY: CmekConfig.NotebookLMState
    NOTEBOOK_LM_READY: CmekConfig.NotebookLMState
    NOTEBOOK_LM_NOT_ENABLED: CmekConfig.NotebookLMState
    NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    LAST_ROTATION_TIMESTAMP_MICROS_FIELD_NUMBER: _ClassVar[int]
    SINGLE_REGION_KEYS_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOKLM_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    kms_key: str
    kms_key_version: str
    state: CmekConfig.State
    is_default: bool
    last_rotation_timestamp_micros: int
    single_region_keys: _containers.RepeatedCompositeFieldContainer[SingleRegionKey]
    notebooklm_state: CmekConfig.NotebookLMState

    def __init__(self, name: _Optional[str]=..., kms_key: _Optional[str]=..., kms_key_version: _Optional[str]=..., state: _Optional[_Union[CmekConfig.State, str]]=..., is_default: bool=..., last_rotation_timestamp_micros: _Optional[int]=..., single_region_keys: _Optional[_Iterable[_Union[SingleRegionKey, _Mapping]]]=..., notebooklm_state: _Optional[_Union[CmekConfig.NotebookLMState, str]]=...) -> None:
        ...

class UpdateCmekConfigMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class ListCmekConfigsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListCmekConfigsResponse(_message.Message):
    __slots__ = ('cmek_configs',)
    CMEK_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    cmek_configs: _containers.RepeatedCompositeFieldContainer[CmekConfig]

    def __init__(self, cmek_configs: _Optional[_Iterable[_Union[CmekConfig, _Mapping]]]=...) -> None:
        ...

class DeleteCmekConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteCmekConfigMetadata(_message.Message):
    __slots__ = ('create_time', 'update_time')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...