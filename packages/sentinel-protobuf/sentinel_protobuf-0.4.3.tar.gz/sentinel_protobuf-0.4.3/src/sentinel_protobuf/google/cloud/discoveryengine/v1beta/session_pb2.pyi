from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import answer_pb2 as _answer_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Session(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'user_pseudo_id', 'turns', 'start_time', 'end_time', 'is_pinned')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Session.State]
        IN_PROGRESS: _ClassVar[Session.State]
    STATE_UNSPECIFIED: Session.State
    IN_PROGRESS: Session.State

    class Turn(_message.Message):
        __slots__ = ('query', 'answer', 'detailed_answer', 'query_config')

        class QueryConfigEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        DETAILED_ANSWER_FIELD_NUMBER: _ClassVar[int]
        QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        query: Query
        answer: str
        detailed_answer: _answer_pb2.Answer
        query_config: _containers.ScalarMap[str, str]

        def __init__(self, query: _Optional[_Union[Query, _Mapping]]=..., answer: _Optional[str]=..., detailed_answer: _Optional[_Union[_answer_pb2.Answer, _Mapping]]=..., query_config: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: Session.State
    user_pseudo_id: str
    turns: _containers.RepeatedCompositeFieldContainer[Session.Turn]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    is_pinned: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[Session.State, str]]=..., user_pseudo_id: _Optional[str]=..., turns: _Optional[_Iterable[_Union[Session.Turn, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., is_pinned: bool=...) -> None:
        ...

class Query(_message.Message):
    __slots__ = ('text', 'query_id')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    query_id: str

    def __init__(self, text: _Optional[str]=..., query_id: _Optional[str]=...) -> None:
        ...