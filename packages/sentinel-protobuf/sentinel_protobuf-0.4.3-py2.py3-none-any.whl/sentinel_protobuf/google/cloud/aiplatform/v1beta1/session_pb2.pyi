from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ('expire_time', 'ttl', 'name', 'create_time', 'update_time', 'display_name', 'session_state', 'user_id')
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    TTL_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SESSION_STATE_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    expire_time: _timestamp_pb2.Timestamp
    ttl: _duration_pb2.Duration
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    display_name: str
    session_state: _struct_pb2.Struct
    user_id: str

    def __init__(self, expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., ttl: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., session_state: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., user_id: _Optional[str]=...) -> None:
        ...

class SessionEvent(_message.Message):
    __slots__ = ('name', 'author', 'content', 'invocation_id', 'actions', 'timestamp', 'error_code', 'error_message', 'event_metadata')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_ID_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EVENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    author: str
    content: _content_pb2.Content
    invocation_id: str
    actions: EventActions
    timestamp: _timestamp_pb2.Timestamp
    error_code: str
    error_message: str
    event_metadata: EventMetadata

    def __init__(self, name: _Optional[str]=..., author: _Optional[str]=..., content: _Optional[_Union[_content_pb2.Content, _Mapping]]=..., invocation_id: _Optional[str]=..., actions: _Optional[_Union[EventActions, _Mapping]]=..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error_code: _Optional[str]=..., error_message: _Optional[str]=..., event_metadata: _Optional[_Union[EventMetadata, _Mapping]]=...) -> None:
        ...

class EventMetadata(_message.Message):
    __slots__ = ('grounding_metadata', 'partial', 'turn_complete', 'interrupted', 'long_running_tool_ids', 'branch', 'custom_metadata')
    GROUNDING_METADATA_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FIELD_NUMBER: _ClassVar[int]
    TURN_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    INTERRUPTED_FIELD_NUMBER: _ClassVar[int]
    LONG_RUNNING_TOOL_IDS_FIELD_NUMBER: _ClassVar[int]
    BRANCH_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_METADATA_FIELD_NUMBER: _ClassVar[int]
    grounding_metadata: _content_pb2.GroundingMetadata
    partial: bool
    turn_complete: bool
    interrupted: bool
    long_running_tool_ids: _containers.RepeatedScalarFieldContainer[str]
    branch: str
    custom_metadata: _struct_pb2.Struct

    def __init__(self, grounding_metadata: _Optional[_Union[_content_pb2.GroundingMetadata, _Mapping]]=..., partial: bool=..., turn_complete: bool=..., interrupted: bool=..., long_running_tool_ids: _Optional[_Iterable[str]]=..., branch: _Optional[str]=..., custom_metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class EventActions(_message.Message):
    __slots__ = ('skip_summarization', 'state_delta', 'artifact_delta', 'transfer_to_agent', 'escalate', 'requested_auth_configs', 'transfer_agent')

    class ArtifactDeltaEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: int

        def __init__(self, key: _Optional[str]=..., value: _Optional[int]=...) -> None:
            ...
    SKIP_SUMMARIZATION_FIELD_NUMBER: _ClassVar[int]
    STATE_DELTA_FIELD_NUMBER: _ClassVar[int]
    ARTIFACT_DELTA_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_TO_AGENT_FIELD_NUMBER: _ClassVar[int]
    ESCALATE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_AUTH_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    TRANSFER_AGENT_FIELD_NUMBER: _ClassVar[int]
    skip_summarization: bool
    state_delta: _struct_pb2.Struct
    artifact_delta: _containers.ScalarMap[str, int]
    transfer_to_agent: bool
    escalate: bool
    requested_auth_configs: _struct_pb2.Struct
    transfer_agent: str

    def __init__(self, skip_summarization: bool=..., state_delta: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., artifact_delta: _Optional[_Mapping[str, int]]=..., transfer_to_agent: bool=..., escalate: bool=..., requested_auth_configs: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., transfer_agent: _Optional[str]=...) -> None:
        ...