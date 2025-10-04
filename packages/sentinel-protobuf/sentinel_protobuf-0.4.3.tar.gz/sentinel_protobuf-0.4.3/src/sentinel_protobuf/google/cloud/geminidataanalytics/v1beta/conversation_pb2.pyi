from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Conversation(_message.Message):
    __slots__ = ('name', 'agents', 'create_time', 'last_used_time', 'labels')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    AGENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_USED_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    name: str
    agents: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp
    last_used_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]

    def __init__(self, name: _Optional[str]=..., agents: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_used_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CreateConversationRequest(_message.Message):
    __slots__ = ('parent', 'conversation_id', 'conversation', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    conversation_id: str
    conversation: Conversation
    request_id: str

    def __init__(self, parent: _Optional[str]=..., conversation_id: _Optional[str]=..., conversation: _Optional[_Union[Conversation, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetConversationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListConversationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListConversationsResponse(_message.Message):
    __slots__ = ('conversations', 'next_page_token')
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]
    next_page_token: str

    def __init__(self, conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...