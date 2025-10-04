from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataDiscoverySpec(_message.Message):
    __slots__ = ('bigquery_publishing_config', 'storage_config')

    class BigQueryPublishingConfig(_message.Message):
        __slots__ = ('table_type', 'connection', 'location', 'project')

        class TableType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TABLE_TYPE_UNSPECIFIED: _ClassVar[DataDiscoverySpec.BigQueryPublishingConfig.TableType]
            EXTERNAL: _ClassVar[DataDiscoverySpec.BigQueryPublishingConfig.TableType]
            BIGLAKE: _ClassVar[DataDiscoverySpec.BigQueryPublishingConfig.TableType]
        TABLE_TYPE_UNSPECIFIED: DataDiscoverySpec.BigQueryPublishingConfig.TableType
        EXTERNAL: DataDiscoverySpec.BigQueryPublishingConfig.TableType
        BIGLAKE: DataDiscoverySpec.BigQueryPublishingConfig.TableType
        TABLE_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONNECTION_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        PROJECT_FIELD_NUMBER: _ClassVar[int]
        table_type: DataDiscoverySpec.BigQueryPublishingConfig.TableType
        connection: str
        location: str
        project: str

        def __init__(self, table_type: _Optional[_Union[DataDiscoverySpec.BigQueryPublishingConfig.TableType, str]]=..., connection: _Optional[str]=..., location: _Optional[str]=..., project: _Optional[str]=...) -> None:
            ...

    class StorageConfig(_message.Message):
        __slots__ = ('include_patterns', 'exclude_patterns', 'csv_options', 'json_options')

        class CsvOptions(_message.Message):
            __slots__ = ('header_rows', 'delimiter', 'encoding', 'type_inference_disabled', 'quote')
            HEADER_ROWS_FIELD_NUMBER: _ClassVar[int]
            DELIMITER_FIELD_NUMBER: _ClassVar[int]
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            TYPE_INFERENCE_DISABLED_FIELD_NUMBER: _ClassVar[int]
            QUOTE_FIELD_NUMBER: _ClassVar[int]
            header_rows: int
            delimiter: str
            encoding: str
            type_inference_disabled: bool
            quote: str

            def __init__(self, header_rows: _Optional[int]=..., delimiter: _Optional[str]=..., encoding: _Optional[str]=..., type_inference_disabled: bool=..., quote: _Optional[str]=...) -> None:
                ...

        class JsonOptions(_message.Message):
            __slots__ = ('encoding', 'type_inference_disabled')
            ENCODING_FIELD_NUMBER: _ClassVar[int]
            TYPE_INFERENCE_DISABLED_FIELD_NUMBER: _ClassVar[int]
            encoding: str
            type_inference_disabled: bool

            def __init__(self, encoding: _Optional[str]=..., type_inference_disabled: bool=...) -> None:
                ...
        INCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        EXCLUDE_PATTERNS_FIELD_NUMBER: _ClassVar[int]
        CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        JSON_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        include_patterns: _containers.RepeatedScalarFieldContainer[str]
        exclude_patterns: _containers.RepeatedScalarFieldContainer[str]
        csv_options: DataDiscoverySpec.StorageConfig.CsvOptions
        json_options: DataDiscoverySpec.StorageConfig.JsonOptions

        def __init__(self, include_patterns: _Optional[_Iterable[str]]=..., exclude_patterns: _Optional[_Iterable[str]]=..., csv_options: _Optional[_Union[DataDiscoverySpec.StorageConfig.CsvOptions, _Mapping]]=..., json_options: _Optional[_Union[DataDiscoverySpec.StorageConfig.JsonOptions, _Mapping]]=...) -> None:
            ...
    BIGQUERY_PUBLISHING_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STORAGE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    bigquery_publishing_config: DataDiscoverySpec.BigQueryPublishingConfig
    storage_config: DataDiscoverySpec.StorageConfig

    def __init__(self, bigquery_publishing_config: _Optional[_Union[DataDiscoverySpec.BigQueryPublishingConfig, _Mapping]]=..., storage_config: _Optional[_Union[DataDiscoverySpec.StorageConfig, _Mapping]]=...) -> None:
        ...

class DataDiscoveryResult(_message.Message):
    __slots__ = ('bigquery_publishing', 'scan_statistics')

    class BigQueryPublishing(_message.Message):
        __slots__ = ('dataset', 'location')
        DATASET_FIELD_NUMBER: _ClassVar[int]
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        location: str

        def __init__(self, dataset: _Optional[str]=..., location: _Optional[str]=...) -> None:
            ...

    class ScanStatistics(_message.Message):
        __slots__ = ('scanned_file_count', 'data_processed_bytes', 'files_excluded', 'tables_created', 'tables_deleted', 'tables_updated', 'filesets_created', 'filesets_deleted', 'filesets_updated')
        SCANNED_FILE_COUNT_FIELD_NUMBER: _ClassVar[int]
        DATA_PROCESSED_BYTES_FIELD_NUMBER: _ClassVar[int]
        FILES_EXCLUDED_FIELD_NUMBER: _ClassVar[int]
        TABLES_CREATED_FIELD_NUMBER: _ClassVar[int]
        TABLES_DELETED_FIELD_NUMBER: _ClassVar[int]
        TABLES_UPDATED_FIELD_NUMBER: _ClassVar[int]
        FILESETS_CREATED_FIELD_NUMBER: _ClassVar[int]
        FILESETS_DELETED_FIELD_NUMBER: _ClassVar[int]
        FILESETS_UPDATED_FIELD_NUMBER: _ClassVar[int]
        scanned_file_count: int
        data_processed_bytes: int
        files_excluded: int
        tables_created: int
        tables_deleted: int
        tables_updated: int
        filesets_created: int
        filesets_deleted: int
        filesets_updated: int

        def __init__(self, scanned_file_count: _Optional[int]=..., data_processed_bytes: _Optional[int]=..., files_excluded: _Optional[int]=..., tables_created: _Optional[int]=..., tables_deleted: _Optional[int]=..., tables_updated: _Optional[int]=..., filesets_created: _Optional[int]=..., filesets_deleted: _Optional[int]=..., filesets_updated: _Optional[int]=...) -> None:
            ...
    BIGQUERY_PUBLISHING_FIELD_NUMBER: _ClassVar[int]
    SCAN_STATISTICS_FIELD_NUMBER: _ClassVar[int]
    bigquery_publishing: DataDiscoveryResult.BigQueryPublishing
    scan_statistics: DataDiscoveryResult.ScanStatistics

    def __init__(self, bigquery_publishing: _Optional[_Union[DataDiscoveryResult.BigQueryPublishing, _Mapping]]=..., scan_statistics: _Optional[_Union[DataDiscoveryResult.ScanStatistics, _Mapping]]=...) -> None:
        ...