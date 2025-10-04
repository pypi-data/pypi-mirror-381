from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import index_pb2 as _index_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateIndexRequest(_message.Message):
    __slots__ = ('parent', 'index')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    parent: str
    index: _index_pb2.Index

    def __init__(self, parent: _Optional[str]=..., index: _Optional[_Union[_index_pb2.Index, _Mapping]]=...) -> None:
        ...

class CreateIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'nearest_neighbor_search_operation_metadata')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEAREST_NEIGHBOR_SEARCH_OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    nearest_neighbor_search_operation_metadata: NearestNeighborSearchOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., nearest_neighbor_search_operation_metadata: _Optional[_Union[NearestNeighborSearchOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIndexesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListIndexesResponse(_message.Message):
    __slots__ = ('indexes', 'next_page_token')
    INDEXES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    indexes: _containers.RepeatedCompositeFieldContainer[_index_pb2.Index]
    next_page_token: str

    def __init__(self, indexes: _Optional[_Iterable[_Union[_index_pb2.Index, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateIndexRequest(_message.Message):
    __slots__ = ('index', 'update_mask')
    INDEX_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    index: _index_pb2.Index
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, index: _Optional[_Union[_index_pb2.Index, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'nearest_neighbor_search_operation_metadata')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    NEAREST_NEIGHBOR_SEARCH_OPERATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    nearest_neighbor_search_operation_metadata: NearestNeighborSearchOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., nearest_neighbor_search_operation_metadata: _Optional[_Union[NearestNeighborSearchOperationMetadata, _Mapping]]=...) -> None:
        ...

class ImportIndexRequest(_message.Message):
    __slots__ = ('name', 'is_complete_overwrite', 'config')

    class ConnectorConfig(_message.Message):
        __slots__ = ('big_query_source_config',)

        class DatapointFieldMapping(_message.Message):
            __slots__ = ('id_column', 'embedding_column', 'restricts', 'numeric_restricts', 'metadata_columns')

            class Restrict(_message.Message):
                __slots__ = ('namespace', 'allow_column', 'deny_column')
                NAMESPACE_FIELD_NUMBER: _ClassVar[int]
                ALLOW_COLUMN_FIELD_NUMBER: _ClassVar[int]
                DENY_COLUMN_FIELD_NUMBER: _ClassVar[int]
                namespace: str
                allow_column: _containers.RepeatedScalarFieldContainer[str]
                deny_column: _containers.RepeatedScalarFieldContainer[str]

                def __init__(self, namespace: _Optional[str]=..., allow_column: _Optional[_Iterable[str]]=..., deny_column: _Optional[_Iterable[str]]=...) -> None:
                    ...

            class NumericRestrict(_message.Message):
                __slots__ = ('namespace', 'value_column', 'value_type')

                class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    VALUE_TYPE_UNSPECIFIED: _ClassVar[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType]
                    INT: _ClassVar[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType]
                    FLOAT: _ClassVar[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType]
                    DOUBLE: _ClassVar[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType]
                VALUE_TYPE_UNSPECIFIED: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType
                INT: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType
                FLOAT: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType
                DOUBLE: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType
                NAMESPACE_FIELD_NUMBER: _ClassVar[int]
                VALUE_COLUMN_FIELD_NUMBER: _ClassVar[int]
                VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
                namespace: str
                value_column: str
                value_type: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType

                def __init__(self, namespace: _Optional[str]=..., value_column: _Optional[str]=..., value_type: _Optional[_Union[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict.ValueType, str]]=...) -> None:
                    ...
            ID_COLUMN_FIELD_NUMBER: _ClassVar[int]
            EMBEDDING_COLUMN_FIELD_NUMBER: _ClassVar[int]
            RESTRICTS_FIELD_NUMBER: _ClassVar[int]
            NUMERIC_RESTRICTS_FIELD_NUMBER: _ClassVar[int]
            METADATA_COLUMNS_FIELD_NUMBER: _ClassVar[int]
            id_column: str
            embedding_column: str
            restricts: _containers.RepeatedCompositeFieldContainer[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.Restrict]
            numeric_restricts: _containers.RepeatedCompositeFieldContainer[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict]
            metadata_columns: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, id_column: _Optional[str]=..., embedding_column: _Optional[str]=..., restricts: _Optional[_Iterable[_Union[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.Restrict, _Mapping]]]=..., numeric_restricts: _Optional[_Iterable[_Union[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping.NumericRestrict, _Mapping]]]=..., metadata_columns: _Optional[_Iterable[str]]=...) -> None:
                ...

        class BigQuerySourceConfig(_message.Message):
            __slots__ = ('table_path', 'datapoint_field_mapping')
            TABLE_PATH_FIELD_NUMBER: _ClassVar[int]
            DATAPOINT_FIELD_MAPPING_FIELD_NUMBER: _ClassVar[int]
            table_path: str
            datapoint_field_mapping: ImportIndexRequest.ConnectorConfig.DatapointFieldMapping

            def __init__(self, table_path: _Optional[str]=..., datapoint_field_mapping: _Optional[_Union[ImportIndexRequest.ConnectorConfig.DatapointFieldMapping, _Mapping]]=...) -> None:
                ...
        BIG_QUERY_SOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        big_query_source_config: ImportIndexRequest.ConnectorConfig.BigQuerySourceConfig

        def __init__(self, big_query_source_config: _Optional[_Union[ImportIndexRequest.ConnectorConfig.BigQuerySourceConfig, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    IS_COMPLETE_OVERWRITE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    is_complete_overwrite: bool
    config: ImportIndexRequest.ConnectorConfig

    def __init__(self, name: _Optional[str]=..., is_complete_overwrite: bool=..., config: _Optional[_Union[ImportIndexRequest.ConnectorConfig, _Mapping]]=...) -> None:
        ...

class ImportIndexOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeleteIndexRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpsertDatapointsRequest(_message.Message):
    __slots__ = ('index', 'datapoints', 'update_mask')
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DATAPOINTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    index: str
    datapoints: _containers.RepeatedCompositeFieldContainer[_index_pb2.IndexDatapoint]
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, index: _Optional[str]=..., datapoints: _Optional[_Iterable[_Union[_index_pb2.IndexDatapoint, _Mapping]]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpsertDatapointsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveDatapointsRequest(_message.Message):
    __slots__ = ('index', 'datapoint_ids')
    INDEX_FIELD_NUMBER: _ClassVar[int]
    DATAPOINT_IDS_FIELD_NUMBER: _ClassVar[int]
    index: str
    datapoint_ids: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, index: _Optional[str]=..., datapoint_ids: _Optional[_Iterable[str]]=...) -> None:
        ...

class RemoveDatapointsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class NearestNeighborSearchOperationMetadata(_message.Message):
    __slots__ = ('content_validation_stats', 'data_bytes_count')

    class RecordError(_message.Message):
        __slots__ = ('error_type', 'error_message', 'source_gcs_uri', 'embedding_id', 'raw_record')

        class RecordErrorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ERROR_TYPE_UNSPECIFIED: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            EMPTY_LINE: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_JSON_SYNTAX: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_CSV_SYNTAX: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_AVRO_SYNTAX: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_EMBEDDING_ID: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            EMBEDDING_SIZE_MISMATCH: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            NAMESPACE_MISSING: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            PARSING_ERROR: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            DUPLICATE_NAMESPACE: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            OP_IN_DATAPOINT: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            MULTIPLE_VALUES: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_NUMERIC_VALUE: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_ENCODING: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_SPARSE_DIMENSIONS: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_TOKEN_VALUE: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_SPARSE_EMBEDDING: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_EMBEDDING: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            INVALID_EMBEDDING_METADATA: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
            EMBEDDING_METADATA_EXCEEDS_SIZE_LIMIT: _ClassVar[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType]
        ERROR_TYPE_UNSPECIFIED: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        EMPTY_LINE: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_JSON_SYNTAX: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_CSV_SYNTAX: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_AVRO_SYNTAX: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_EMBEDDING_ID: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        EMBEDDING_SIZE_MISMATCH: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        NAMESPACE_MISSING: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        PARSING_ERROR: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        DUPLICATE_NAMESPACE: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        OP_IN_DATAPOINT: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        MULTIPLE_VALUES: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_NUMERIC_VALUE: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_ENCODING: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_SPARSE_DIMENSIONS: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_TOKEN_VALUE: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_SPARSE_EMBEDDING: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_EMBEDDING: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        INVALID_EMBEDDING_METADATA: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        EMBEDDING_METADATA_EXCEEDS_SIZE_LIMIT: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        ERROR_TYPE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        SOURCE_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        EMBEDDING_ID_FIELD_NUMBER: _ClassVar[int]
        RAW_RECORD_FIELD_NUMBER: _ClassVar[int]
        error_type: NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType
        error_message: str
        source_gcs_uri: str
        embedding_id: str
        raw_record: str

        def __init__(self, error_type: _Optional[_Union[NearestNeighborSearchOperationMetadata.RecordError.RecordErrorType, str]]=..., error_message: _Optional[str]=..., source_gcs_uri: _Optional[str]=..., embedding_id: _Optional[str]=..., raw_record: _Optional[str]=...) -> None:
            ...

    class ContentValidationStats(_message.Message):
        __slots__ = ('source_gcs_uri', 'valid_record_count', 'invalid_record_count', 'partial_errors', 'valid_sparse_record_count', 'invalid_sparse_record_count')
        SOURCE_GCS_URI_FIELD_NUMBER: _ClassVar[int]
        VALID_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        INVALID_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        PARTIAL_ERRORS_FIELD_NUMBER: _ClassVar[int]
        VALID_SPARSE_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        INVALID_SPARSE_RECORD_COUNT_FIELD_NUMBER: _ClassVar[int]
        source_gcs_uri: str
        valid_record_count: int
        invalid_record_count: int
        partial_errors: _containers.RepeatedCompositeFieldContainer[NearestNeighborSearchOperationMetadata.RecordError]
        valid_sparse_record_count: int
        invalid_sparse_record_count: int

        def __init__(self, source_gcs_uri: _Optional[str]=..., valid_record_count: _Optional[int]=..., invalid_record_count: _Optional[int]=..., partial_errors: _Optional[_Iterable[_Union[NearestNeighborSearchOperationMetadata.RecordError, _Mapping]]]=..., valid_sparse_record_count: _Optional[int]=..., invalid_sparse_record_count: _Optional[int]=...) -> None:
            ...
    CONTENT_VALIDATION_STATS_FIELD_NUMBER: _ClassVar[int]
    DATA_BYTES_COUNT_FIELD_NUMBER: _ClassVar[int]
    content_validation_stats: _containers.RepeatedCompositeFieldContainer[NearestNeighborSearchOperationMetadata.ContentValidationStats]
    data_bytes_count: int

    def __init__(self, content_validation_stats: _Optional[_Iterable[_Union[NearestNeighborSearchOperationMetadata.ContentValidationStats, _Mapping]]]=..., data_bytes_count: _Optional[int]=...) -> None:
        ...