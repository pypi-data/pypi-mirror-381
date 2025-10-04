from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Chunk(_message.Message):
    __slots__ = ('name', 'id', 'content', 'relevance_score', 'document_metadata', 'derived_struct_data', 'page_span', 'chunk_metadata', 'data_urls', 'annotation_contents', 'annotation_metadata')

    class StructureType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STRUCTURE_TYPE_UNSPECIFIED: _ClassVar[Chunk.StructureType]
        SHAREHOLDER_STRUCTURE: _ClassVar[Chunk.StructureType]
        SIGNATURE_STRUCTURE: _ClassVar[Chunk.StructureType]
        CHECKBOX_STRUCTURE: _ClassVar[Chunk.StructureType]
    STRUCTURE_TYPE_UNSPECIFIED: Chunk.StructureType
    SHAREHOLDER_STRUCTURE: Chunk.StructureType
    SIGNATURE_STRUCTURE: Chunk.StructureType
    CHECKBOX_STRUCTURE: Chunk.StructureType

    class DocumentMetadata(_message.Message):
        __slots__ = ('uri', 'title', 'struct_data')
        URI_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
        uri: str
        title: str
        struct_data: _struct_pb2.Struct

        def __init__(self, uri: _Optional[str]=..., title: _Optional[str]=..., struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=...) -> None:
            ...

    class PageSpan(_message.Message):
        __slots__ = ('page_start', 'page_end')
        PAGE_START_FIELD_NUMBER: _ClassVar[int]
        PAGE_END_FIELD_NUMBER: _ClassVar[int]
        page_start: int
        page_end: int

        def __init__(self, page_start: _Optional[int]=..., page_end: _Optional[int]=...) -> None:
            ...

    class ChunkMetadata(_message.Message):
        __slots__ = ('previous_chunks', 'next_chunks')
        PREVIOUS_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        NEXT_CHUNKS_FIELD_NUMBER: _ClassVar[int]
        previous_chunks: _containers.RepeatedCompositeFieldContainer[Chunk]
        next_chunks: _containers.RepeatedCompositeFieldContainer[Chunk]

        def __init__(self, previous_chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]]=..., next_chunks: _Optional[_Iterable[_Union[Chunk, _Mapping]]]=...) -> None:
            ...

    class StructuredContent(_message.Message):
        __slots__ = ('structure_type', 'content')
        STRUCTURE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        structure_type: Chunk.StructureType
        content: str

        def __init__(self, structure_type: _Optional[_Union[Chunk.StructureType, str]]=..., content: _Optional[str]=...) -> None:
            ...

    class AnnotationMetadata(_message.Message):
        __slots__ = ('structured_content', 'image_id')
        STRUCTURED_CONTENT_FIELD_NUMBER: _ClassVar[int]
        IMAGE_ID_FIELD_NUMBER: _ClassVar[int]
        structured_content: Chunk.StructuredContent
        image_id: str

        def __init__(self, structured_content: _Optional[_Union[Chunk.StructuredContent, _Mapping]]=..., image_id: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    RELEVANCE_SCORE_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_METADATA_FIELD_NUMBER: _ClassVar[int]
    DERIVED_STRUCT_DATA_FIELD_NUMBER: _ClassVar[int]
    PAGE_SPAN_FIELD_NUMBER: _ClassVar[int]
    CHUNK_METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_URLS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    id: str
    content: str
    relevance_score: float
    document_metadata: Chunk.DocumentMetadata
    derived_struct_data: _struct_pb2.Struct
    page_span: Chunk.PageSpan
    chunk_metadata: Chunk.ChunkMetadata
    data_urls: _containers.RepeatedScalarFieldContainer[str]
    annotation_contents: _containers.RepeatedScalarFieldContainer[str]
    annotation_metadata: _containers.RepeatedCompositeFieldContainer[Chunk.AnnotationMetadata]

    def __init__(self, name: _Optional[str]=..., id: _Optional[str]=..., content: _Optional[str]=..., relevance_score: _Optional[float]=..., document_metadata: _Optional[_Union[Chunk.DocumentMetadata, _Mapping]]=..., derived_struct_data: _Optional[_Union[_struct_pb2.Struct, _Mapping]]=..., page_span: _Optional[_Union[Chunk.PageSpan, _Mapping]]=..., chunk_metadata: _Optional[_Union[Chunk.ChunkMetadata, _Mapping]]=..., data_urls: _Optional[_Iterable[str]]=..., annotation_contents: _Optional[_Iterable[str]]=..., annotation_metadata: _Optional[_Iterable[_Union[Chunk.AnnotationMetadata, _Mapping]]]=...) -> None:
        ...