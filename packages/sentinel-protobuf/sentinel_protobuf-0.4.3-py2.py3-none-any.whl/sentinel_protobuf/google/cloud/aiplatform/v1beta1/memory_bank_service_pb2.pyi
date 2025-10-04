from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import memory_bank_pb2 as _memory_bank_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
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

class CreateMemoryRequest(_message.Message):
    __slots__ = ('parent', 'memory')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    memory: _memory_bank_pb2.Memory

    def __init__(self, parent: _Optional[str]=..., memory: _Optional[_Union[_memory_bank_pb2.Memory, _Mapping]]=...) -> None:
        ...

class CreateMemoryOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetMemoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateMemoryRequest(_message.Message):
    __slots__ = ('memory', 'update_mask')
    MEMORY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    memory: _memory_bank_pb2.Memory
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, memory: _Optional[_Union[_memory_bank_pb2.Memory, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateMemoryOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ListMemoriesRequest(_message.Message):
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

class ListMemoriesResponse(_message.Message):
    __slots__ = ('memories', 'next_page_token')
    MEMORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    memories: _containers.RepeatedCompositeFieldContainer[_memory_bank_pb2.Memory]
    next_page_token: str

    def __init__(self, memories: _Optional[_Iterable[_Union[_memory_bank_pb2.Memory, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteMemoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteMemoryOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GenerateMemoriesRequest(_message.Message):
    __slots__ = ('vertex_session_source', 'direct_contents_source', 'direct_memories_source', 'parent', 'disable_consolidation', 'scope')

    class VertexSessionSource(_message.Message):
        __slots__ = ('session', 'start_time', 'end_time')
        SESSION_FIELD_NUMBER: _ClassVar[int]
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        session: str
        start_time: _timestamp_pb2.Timestamp
        end_time: _timestamp_pb2.Timestamp

        def __init__(self, session: _Optional[str]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...

    class DirectContentsSource(_message.Message):
        __slots__ = ('events',)

        class Event(_message.Message):
            __slots__ = ('content',)
            CONTENT_FIELD_NUMBER: _ClassVar[int]
            content: _content_pb2.Content

            def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]]=...) -> None:
                ...
        EVENTS_FIELD_NUMBER: _ClassVar[int]
        events: _containers.RepeatedCompositeFieldContainer[GenerateMemoriesRequest.DirectContentsSource.Event]

        def __init__(self, events: _Optional[_Iterable[_Union[GenerateMemoriesRequest.DirectContentsSource.Event, _Mapping]]]=...) -> None:
            ...

    class DirectMemoriesSource(_message.Message):
        __slots__ = ('direct_memories',)

        class DirectMemory(_message.Message):
            __slots__ = ('fact',)
            FACT_FIELD_NUMBER: _ClassVar[int]
            fact: str

            def __init__(self, fact: _Optional[str]=...) -> None:
                ...
        DIRECT_MEMORIES_FIELD_NUMBER: _ClassVar[int]
        direct_memories: _containers.RepeatedCompositeFieldContainer[GenerateMemoriesRequest.DirectMemoriesSource.DirectMemory]

        def __init__(self, direct_memories: _Optional[_Iterable[_Union[GenerateMemoriesRequest.DirectMemoriesSource.DirectMemory, _Mapping]]]=...) -> None:
            ...

    class ScopeEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    VERTEX_SESSION_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_CONTENTS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    DIRECT_MEMORIES_SOURCE_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DISABLE_CONSOLIDATION_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    vertex_session_source: GenerateMemoriesRequest.VertexSessionSource
    direct_contents_source: GenerateMemoriesRequest.DirectContentsSource
    direct_memories_source: GenerateMemoriesRequest.DirectMemoriesSource
    parent: str
    disable_consolidation: bool
    scope: _containers.ScalarMap[str, str]

    def __init__(self, vertex_session_source: _Optional[_Union[GenerateMemoriesRequest.VertexSessionSource, _Mapping]]=..., direct_contents_source: _Optional[_Union[GenerateMemoriesRequest.DirectContentsSource, _Mapping]]=..., direct_memories_source: _Optional[_Union[GenerateMemoriesRequest.DirectMemoriesSource, _Mapping]]=..., parent: _Optional[str]=..., disable_consolidation: bool=..., scope: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class GenerateMemoriesResponse(_message.Message):
    __slots__ = ('generated_memories',)

    class GeneratedMemory(_message.Message):
        __slots__ = ('memory', 'action')

        class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_UNSPECIFIED: _ClassVar[GenerateMemoriesResponse.GeneratedMemory.Action]
            CREATED: _ClassVar[GenerateMemoriesResponse.GeneratedMemory.Action]
            UPDATED: _ClassVar[GenerateMemoriesResponse.GeneratedMemory.Action]
            DELETED: _ClassVar[GenerateMemoriesResponse.GeneratedMemory.Action]
        ACTION_UNSPECIFIED: GenerateMemoriesResponse.GeneratedMemory.Action
        CREATED: GenerateMemoriesResponse.GeneratedMemory.Action
        UPDATED: GenerateMemoriesResponse.GeneratedMemory.Action
        DELETED: GenerateMemoriesResponse.GeneratedMemory.Action
        MEMORY_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        memory: _memory_bank_pb2.Memory
        action: GenerateMemoriesResponse.GeneratedMemory.Action

        def __init__(self, memory: _Optional[_Union[_memory_bank_pb2.Memory, _Mapping]]=..., action: _Optional[_Union[GenerateMemoriesResponse.GeneratedMemory.Action, str]]=...) -> None:
            ...
    GENERATED_MEMORIES_FIELD_NUMBER: _ClassVar[int]
    generated_memories: _containers.RepeatedCompositeFieldContainer[GenerateMemoriesResponse.GeneratedMemory]

    def __init__(self, generated_memories: _Optional[_Iterable[_Union[GenerateMemoriesResponse.GeneratedMemory, _Mapping]]]=...) -> None:
        ...

class GenerateMemoriesOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class RetrieveMemoriesRequest(_message.Message):
    __slots__ = ('similarity_search_params', 'simple_retrieval_params', 'parent', 'scope')

    class SimilaritySearchParams(_message.Message):
        __slots__ = ('search_query', 'top_k')
        SEARCH_QUERY_FIELD_NUMBER: _ClassVar[int]
        TOP_K_FIELD_NUMBER: _ClassVar[int]
        search_query: str
        top_k: int

        def __init__(self, search_query: _Optional[str]=..., top_k: _Optional[int]=...) -> None:
            ...

    class SimpleRetrievalParams(_message.Message):
        __slots__ = ('page_size', 'page_token')
        PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
        PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
        page_size: int
        page_token: str

        def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
            ...

    class ScopeEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    SIMILARITY_SEARCH_PARAMS_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_RETRIEVAL_PARAMS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCOPE_FIELD_NUMBER: _ClassVar[int]
    similarity_search_params: RetrieveMemoriesRequest.SimilaritySearchParams
    simple_retrieval_params: RetrieveMemoriesRequest.SimpleRetrievalParams
    parent: str
    scope: _containers.ScalarMap[str, str]

    def __init__(self, similarity_search_params: _Optional[_Union[RetrieveMemoriesRequest.SimilaritySearchParams, _Mapping]]=..., simple_retrieval_params: _Optional[_Union[RetrieveMemoriesRequest.SimpleRetrievalParams, _Mapping]]=..., parent: _Optional[str]=..., scope: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class RetrieveMemoriesResponse(_message.Message):
    __slots__ = ('retrieved_memories', 'next_page_token')

    class RetrievedMemory(_message.Message):
        __slots__ = ('memory', 'distance')
        MEMORY_FIELD_NUMBER: _ClassVar[int]
        DISTANCE_FIELD_NUMBER: _ClassVar[int]
        memory: _memory_bank_pb2.Memory
        distance: float

        def __init__(self, memory: _Optional[_Union[_memory_bank_pb2.Memory, _Mapping]]=..., distance: _Optional[float]=...) -> None:
            ...
    RETRIEVED_MEMORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    retrieved_memories: _containers.RepeatedCompositeFieldContainer[RetrieveMemoriesResponse.RetrievedMemory]
    next_page_token: str

    def __init__(self, retrieved_memories: _Optional[_Iterable[_Union[RetrieveMemoriesResponse.RetrievedMemory, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...