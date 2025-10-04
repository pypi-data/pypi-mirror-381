from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateProductTextSuggestionsRequest(_message.Message):
    __slots__ = ('name', 'product_info', 'output_spec', 'title_examples')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_SPEC_FIELD_NUMBER: _ClassVar[int]
    TITLE_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    name: str
    product_info: ProductInfo
    output_spec: OutputSpec
    title_examples: _containers.RepeatedCompositeFieldContainer[TitleExample]

    def __init__(self, name: _Optional[str]=..., product_info: _Optional[_Union[ProductInfo, _Mapping]]=..., output_spec: _Optional[_Union[OutputSpec, _Mapping]]=..., title_examples: _Optional[_Iterable[_Union[TitleExample, _Mapping]]]=...) -> None:
        ...

class GenerateProductTextSuggestionsResponse(_message.Message):
    __slots__ = ('title', 'description', 'attributes', 'metadata')

    class AttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    TITLE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    title: ProductTextGenerationSuggestion
    description: ProductTextGenerationSuggestion
    attributes: _containers.ScalarMap[str, str]
    metadata: ProductTextGenerationMetadata

    def __init__(self, title: _Optional[_Union[ProductTextGenerationSuggestion, _Mapping]]=..., description: _Optional[_Union[ProductTextGenerationSuggestion, _Mapping]]=..., attributes: _Optional[_Mapping[str, str]]=..., metadata: _Optional[_Union[ProductTextGenerationMetadata, _Mapping]]=...) -> None:
        ...

class TitleExample(_message.Message):
    __slots__ = ('product_info', 'category', 'title_format', 'final_product_info')

    class ProductInfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class FinalProductInfoEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    TITLE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    FINAL_PRODUCT_INFO_FIELD_NUMBER: _ClassVar[int]
    product_info: _containers.ScalarMap[str, str]
    category: str
    title_format: str
    final_product_info: _containers.ScalarMap[str, str]

    def __init__(self, product_info: _Optional[_Mapping[str, str]]=..., category: _Optional[str]=..., title_format: _Optional[str]=..., final_product_info: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class ProductTextGenerationMetadata(_message.Message):
    __slots__ = ('metadata',)
    METADATA_FIELD_NUMBER: _ClassVar[int]
    metadata: _struct_pb2.Struct

    def __init__(self, metadata: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
        ...

class Image(_message.Message):
    __slots__ = ('uri', 'data')
    URI_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    uri: str
    data: bytes

    def __init__(self, uri: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...

class ProductInfo(_message.Message):
    __slots__ = ('product_attributes', 'product_image')

    class ProductAttributesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    PRODUCT_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    product_attributes: _containers.ScalarMap[str, str]
    product_image: Image

    def __init__(self, product_attributes: _Optional[_Mapping[str, str]]=..., product_image: _Optional[_Union[Image, _Mapping]]=...) -> None:
        ...

class OutputSpec(_message.Message):
    __slots__ = ('workflow_id', 'tone', 'editorial_changes', 'target_language', 'attribute_order', 'attribute_separator')
    WORKFLOW_ID_FIELD_NUMBER: _ClassVar[int]
    TONE_FIELD_NUMBER: _ClassVar[int]
    EDITORIAL_CHANGES_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_ORDER_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    workflow_id: str
    tone: str
    editorial_changes: str
    target_language: str
    attribute_order: _containers.RepeatedScalarFieldContainer[str]
    attribute_separator: str

    def __init__(self, workflow_id: _Optional[str]=..., tone: _Optional[str]=..., editorial_changes: _Optional[str]=..., target_language: _Optional[str]=..., attribute_order: _Optional[_Iterable[str]]=..., attribute_separator: _Optional[str]=...) -> None:
        ...

class ProductTextGenerationSuggestion(_message.Message):
    __slots__ = ('text', 'score', 'change_summary')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    SCORE_FIELD_NUMBER: _ClassVar[int]
    CHANGE_SUMMARY_FIELD_NUMBER: _ClassVar[int]
    text: str
    score: float
    change_summary: str

    def __init__(self, text: _Optional[str]=..., score: _Optional[float]=..., change_summary: _Optional[str]=...) -> None:
        ...