from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1beta import document_pb2 as _document_pb2
from google.cloud.discoveryengine.v1beta import import_config_pb2 as _import_config_pb2
from google.cloud.discoveryengine.v1beta import purge_config_pb2 as _purge_config_pb2
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

class GetDocumentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListDocumentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListDocumentsResponse(_message.Message):
    __slots__ = ('documents', 'next_page_token')
    DOCUMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    documents: _containers.RepeatedCompositeFieldContainer[_document_pb2.Document]
    next_page_token: str

    def __init__(self, documents: _Optional[_Iterable[_Union[_document_pb2.Document, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateDocumentRequest(_message.Message):
    __slots__ = ('parent', 'document', 'document_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    document: _document_pb2.Document
    document_id: str

    def __init__(self, parent: _Optional[str]=..., document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., document_id: _Optional[str]=...) -> None:
        ...

class UpdateDocumentRequest(_message.Message):
    __slots__ = ('document', 'allow_missing', 'update_mask')
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    document: _document_pb2.Document
    allow_missing: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, document: _Optional[_Union[_document_pb2.Document, _Mapping]]=..., allow_missing: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteDocumentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class BatchGetDocumentsMetadataRequest(_message.Message):
    __slots__ = ('parent', 'matcher')

    class UrisMatcher(_message.Message):
        __slots__ = ('uris',)
        URIS_FIELD_NUMBER: _ClassVar[int]
        uris: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, uris: _Optional[_Iterable[str]]=...) -> None:
            ...

    class FhirMatcher(_message.Message):
        __slots__ = ('fhir_resources',)
        FHIR_RESOURCES_FIELD_NUMBER: _ClassVar[int]
        fhir_resources: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, fhir_resources: _Optional[_Iterable[str]]=...) -> None:
            ...

    class Matcher(_message.Message):
        __slots__ = ('uris_matcher', 'fhir_matcher')
        URIS_MATCHER_FIELD_NUMBER: _ClassVar[int]
        FHIR_MATCHER_FIELD_NUMBER: _ClassVar[int]
        uris_matcher: BatchGetDocumentsMetadataRequest.UrisMatcher
        fhir_matcher: BatchGetDocumentsMetadataRequest.FhirMatcher

        def __init__(self, uris_matcher: _Optional[_Union[BatchGetDocumentsMetadataRequest.UrisMatcher, _Mapping]]=..., fhir_matcher: _Optional[_Union[BatchGetDocumentsMetadataRequest.FhirMatcher, _Mapping]]=...) -> None:
            ...
    PARENT_FIELD_NUMBER: _ClassVar[int]
    MATCHER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    matcher: BatchGetDocumentsMetadataRequest.Matcher

    def __init__(self, parent: _Optional[str]=..., matcher: _Optional[_Union[BatchGetDocumentsMetadataRequest.Matcher, _Mapping]]=...) -> None:
        ...

class BatchGetDocumentsMetadataResponse(_message.Message):
    __slots__ = ('documents_metadata',)

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[BatchGetDocumentsMetadataResponse.State]
        INDEXED: _ClassVar[BatchGetDocumentsMetadataResponse.State]
        NOT_IN_TARGET_SITE: _ClassVar[BatchGetDocumentsMetadataResponse.State]
        NOT_IN_INDEX: _ClassVar[BatchGetDocumentsMetadataResponse.State]
    STATE_UNSPECIFIED: BatchGetDocumentsMetadataResponse.State
    INDEXED: BatchGetDocumentsMetadataResponse.State
    NOT_IN_TARGET_SITE: BatchGetDocumentsMetadataResponse.State
    NOT_IN_INDEX: BatchGetDocumentsMetadataResponse.State

    class DocumentMetadata(_message.Message):
        __slots__ = ('matcher_value', 'state', 'last_refreshed_time', 'data_ingestion_source')

        class MatcherValue(_message.Message):
            __slots__ = ('uri', 'fhir_resource')
            URI_FIELD_NUMBER: _ClassVar[int]
            FHIR_RESOURCE_FIELD_NUMBER: _ClassVar[int]
            uri: str
            fhir_resource: str

            def __init__(self, uri: _Optional[str]=..., fhir_resource: _Optional[str]=...) -> None:
                ...
        MATCHER_VALUE_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        LAST_REFRESHED_TIME_FIELD_NUMBER: _ClassVar[int]
        DATA_INGESTION_SOURCE_FIELD_NUMBER: _ClassVar[int]
        matcher_value: BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue
        state: BatchGetDocumentsMetadataResponse.State
        last_refreshed_time: _timestamp_pb2.Timestamp
        data_ingestion_source: str

        def __init__(self, matcher_value: _Optional[_Union[BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue, _Mapping]]=..., state: _Optional[_Union[BatchGetDocumentsMetadataResponse.State, str]]=..., last_refreshed_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_ingestion_source: _Optional[str]=...) -> None:
            ...
    DOCUMENTS_METADATA_FIELD_NUMBER: _ClassVar[int]
    documents_metadata: _containers.RepeatedCompositeFieldContainer[BatchGetDocumentsMetadataResponse.DocumentMetadata]

    def __init__(self, documents_metadata: _Optional[_Iterable[_Union[BatchGetDocumentsMetadataResponse.DocumentMetadata, _Mapping]]]=...) -> None:
        ...