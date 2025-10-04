from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import example_pb2 as _example_pb2
from google.cloud.aiplatform.v1beta1 import example_store_pb2 as _example_store_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateExampleStoreRequest(_message.Message):
    __slots__ = ('parent', 'example_store')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    example_store: _example_store_pb2.ExampleStore

    def __init__(self, parent: _Optional[str]=..., example_store: _Optional[_Union[_example_store_pb2.ExampleStore, _Mapping]]=...) -> None:
        ...

class CreateExampleStoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetExampleStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateExampleStoreRequest(_message.Message):
    __slots__ = ('example_store', 'update_mask')
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    example_store: _example_store_pb2.ExampleStore
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, example_store: _Optional[_Union[_example_store_pb2.ExampleStore, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateExampleStoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeleteExampleStoreRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class DeleteExampleStoreOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ListExampleStoresRequest(_message.Message):
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

class ListExampleStoresResponse(_message.Message):
    __slots__ = ('example_stores', 'next_page_token')
    EXAMPLE_STORES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    example_stores: _containers.RepeatedCompositeFieldContainer[_example_store_pb2.ExampleStore]
    next_page_token: str

    def __init__(self, example_stores: _Optional[_Iterable[_Union[_example_store_pb2.ExampleStore, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Example(_message.Message):
    __slots__ = ('stored_contents_example', 'display_name', 'example_id', 'create_time')
    STORED_CONTENTS_EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_ID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    stored_contents_example: _example_pb2.StoredContentsExample
    display_name: str
    example_id: str
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, stored_contents_example: _Optional[_Union[_example_pb2.StoredContentsExample, _Mapping]]=..., display_name: _Optional[str]=..., example_id: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class UpsertExamplesRequest(_message.Message):
    __slots__ = ('example_store', 'examples', 'overwrite')
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    example_store: str
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    overwrite: bool

    def __init__(self, example_store: _Optional[str]=..., examples: _Optional[_Iterable[_Union[Example, _Mapping]]]=..., overwrite: bool=...) -> None:
        ...

class UpsertExamplesResponse(_message.Message):
    __slots__ = ('results',)

    class UpsertResult(_message.Message):
        __slots__ = ('example', 'status')
        EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        example: Example
        status: _status_pb2.Status

        def __init__(self, example: _Optional[_Union[Example, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
            ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[UpsertExamplesResponse.UpsertResult]

    def __init__(self, results: _Optional[_Iterable[_Union[UpsertExamplesResponse.UpsertResult, _Mapping]]]=...) -> None:
        ...

class RemoveExamplesRequest(_message.Message):
    __slots__ = ('stored_contents_example_filter', 'example_store', 'example_ids')
    STORED_CONTENTS_EXAMPLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_IDS_FIELD_NUMBER: _ClassVar[int]
    stored_contents_example_filter: _example_store_pb2.StoredContentsExampleFilter
    example_store: str
    example_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, stored_contents_example_filter: _Optional[_Union[_example_store_pb2.StoredContentsExampleFilter, _Mapping]]=..., example_store: _Optional[str]=..., example_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class RemoveExamplesResponse(_message.Message):
    __slots__ = ('example_ids',)
    EXAMPLE_IDS_FIELD_NUMBER: _ClassVar[int]
    example_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, example_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class SearchExamplesRequest(_message.Message):
    __slots__ = ('stored_contents_example_parameters', 'example_store', 'top_k')
    STORED_CONTENTS_EXAMPLE_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    TOP_K_FIELD_NUMBER: _ClassVar[int]
    stored_contents_example_parameters: _example_store_pb2.StoredContentsExampleParameters
    example_store: str
    top_k: int

    def __init__(self, stored_contents_example_parameters: _Optional[_Union[_example_store_pb2.StoredContentsExampleParameters, _Mapping]]=..., example_store: _Optional[str]=..., top_k: _Optional[int]=...) -> None:
        ...

class SearchExamplesResponse(_message.Message):
    __slots__ = ('results',)

    class SimilarExample(_message.Message):
        __slots__ = ('example', 'similarity_score')
        EXAMPLE_FIELD_NUMBER: _ClassVar[int]
        SIMILARITY_SCORE_FIELD_NUMBER: _ClassVar[int]
        example: Example
        similarity_score: float

        def __init__(self, example: _Optional[_Union[Example, _Mapping]]=..., similarity_score: _Optional[float]=...) -> None:
            ...
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[SearchExamplesResponse.SimilarExample]

    def __init__(self, results: _Optional[_Iterable[_Union[SearchExamplesResponse.SimilarExample, _Mapping]]]=...) -> None:
        ...

class FetchExamplesRequest(_message.Message):
    __slots__ = ('stored_contents_example_filter', 'example_store', 'page_size', 'page_token', 'example_ids')
    STORED_CONTENTS_EXAMPLE_FILTER_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_STORE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_IDS_FIELD_NUMBER: _ClassVar[int]
    stored_contents_example_filter: _example_store_pb2.StoredContentsExampleFilter
    example_store: str
    page_size: int
    page_token: str
    example_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, stored_contents_example_filter: _Optional[_Union[_example_store_pb2.StoredContentsExampleFilter, _Mapping]]=..., example_store: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., example_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class FetchExamplesResponse(_message.Message):
    __slots__ = ('examples', 'next_page_token')
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    examples: _containers.RepeatedCompositeFieldContainer[Example]
    next_page_token: str

    def __init__(self, examples: _Optional[_Iterable[_Union[Example, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...