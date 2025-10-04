from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import example_pb2 as _example_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ExampleStore(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'create_time', 'update_time', 'example_store_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_STORE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    example_store_config: ExampleStoreConfig

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., example_store_config: _Optional[_Union[ExampleStoreConfig, _Mapping]]=...) -> None:
        ...

class ExampleStoreConfig(_message.Message):
    __slots__ = ('vertex_embedding_model',)
    VERTEX_EMBEDDING_MODEL_FIELD_NUMBER: _ClassVar[int]
    vertex_embedding_model: str

    def __init__(self, vertex_embedding_model: _Optional[str]=...) -> None:
        ...

class StoredContentsExampleFilter(_message.Message):
    __slots__ = ('search_keys', 'function_names')
    SEARCH_KEYS_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    search_keys: _containers.RepeatedScalarFieldContainer[str]
    function_names: ExamplesArrayFilter

    def __init__(self, search_keys: _Optional[_Iterable[str]]=..., function_names: _Optional[_Union[ExamplesArrayFilter, _Mapping]]=...) -> None:
        ...

class StoredContentsExampleParameters(_message.Message):
    __slots__ = ('search_key', 'content_search_key', 'function_names')

    class ContentSearchKey(_message.Message):
        __slots__ = ('contents', 'search_key_generation_method')
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        SEARCH_KEY_GENERATION_METHOD_FIELD_NUMBER: _ClassVar[int]
        contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
        search_key_generation_method: _example_pb2.StoredContentsExample.SearchKeyGenerationMethod

        def __init__(self, contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., search_key_generation_method: _Optional[_Union[_example_pb2.StoredContentsExample.SearchKeyGenerationMethod, _Mapping]]=...) -> None:
            ...
    SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENT_SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_NAMES_FIELD_NUMBER: _ClassVar[int]
    search_key: str
    content_search_key: StoredContentsExampleParameters.ContentSearchKey
    function_names: ExamplesArrayFilter

    def __init__(self, search_key: _Optional[str]=..., content_search_key: _Optional[_Union[StoredContentsExampleParameters.ContentSearchKey, _Mapping]]=..., function_names: _Optional[_Union[ExamplesArrayFilter, _Mapping]]=...) -> None:
        ...

class ExamplesArrayFilter(_message.Message):
    __slots__ = ('values', 'array_operator')

    class ArrayOperator(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ARRAY_OPERATOR_UNSPECIFIED: _ClassVar[ExamplesArrayFilter.ArrayOperator]
        CONTAINS_ANY: _ClassVar[ExamplesArrayFilter.ArrayOperator]
        CONTAINS_ALL: _ClassVar[ExamplesArrayFilter.ArrayOperator]
    ARRAY_OPERATOR_UNSPECIFIED: ExamplesArrayFilter.ArrayOperator
    CONTAINS_ANY: ExamplesArrayFilter.ArrayOperator
    CONTAINS_ALL: ExamplesArrayFilter.ArrayOperator
    VALUES_FIELD_NUMBER: _ClassVar[int]
    ARRAY_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]
    array_operator: ExamplesArrayFilter.ArrayOperator

    def __init__(self, values: _Optional[_Iterable[str]]=..., array_operator: _Optional[_Union[ExamplesArrayFilter.ArrayOperator, str]]=...) -> None:
        ...