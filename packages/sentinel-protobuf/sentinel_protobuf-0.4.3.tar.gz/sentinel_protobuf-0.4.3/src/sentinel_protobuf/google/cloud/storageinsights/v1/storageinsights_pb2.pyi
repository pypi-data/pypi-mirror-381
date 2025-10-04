from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import date_pb2 as _date_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListReportConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListReportConfigsResponse(_message.Message):
    __slots__ = ('report_configs', 'next_page_token', 'unreachable')
    REPORT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    report_configs: _containers.RepeatedCompositeFieldContainer[ReportConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, report_configs: _Optional[_Iterable[_Union[ReportConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReportConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReportConfigRequest(_message.Message):
    __slots__ = ('parent', 'report_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    report_config: ReportConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., report_config: _Optional[_Union[ReportConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateReportConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'report_config', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    report_config: ReportConfig
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., report_config: _Optional[_Union[ReportConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteReportConfigRequest(_message.Message):
    __slots__ = ('name', 'force', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool
    request_id: str

    def __init__(self, name: _Optional[str]=..., force: bool=..., request_id: _Optional[str]=...) -> None:
        ...

class ReportDetail(_message.Message):
    __slots__ = ('name', 'snapshot_time', 'report_path_prefix', 'shards_count', 'status', 'labels', 'target_datetime', 'report_metrics')

    class Metrics(_message.Message):
        __slots__ = ('processed_records_count',)
        PROCESSED_RECORDS_COUNT_FIELD_NUMBER: _ClassVar[int]
        processed_records_count: int

        def __init__(self, processed_records_count: _Optional[int]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    SNAPSHOT_TIME_FIELD_NUMBER: _ClassVar[int]
    REPORT_PATH_PREFIX_FIELD_NUMBER: _ClassVar[int]
    SHARDS_COUNT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TARGET_DATETIME_FIELD_NUMBER: _ClassVar[int]
    REPORT_METRICS_FIELD_NUMBER: _ClassVar[int]
    name: str
    snapshot_time: _timestamp_pb2.Timestamp
    report_path_prefix: str
    shards_count: int
    status: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    target_datetime: _datetime_pb2.DateTime
    report_metrics: ReportDetail.Metrics

    def __init__(self, name: _Optional[str]=..., snapshot_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., report_path_prefix: _Optional[str]=..., shards_count: _Optional[int]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., target_datetime: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., report_metrics: _Optional[_Union[ReportDetail.Metrics, _Mapping]]=...) -> None:
        ...

class ListReportDetailsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListReportDetailsResponse(_message.Message):
    __slots__ = ('report_details', 'next_page_token', 'unreachable')
    REPORT_DETAILS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    report_details: _containers.RepeatedCompositeFieldContainer[ReportDetail]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, report_details: _Optional[_Iterable[_Union[ReportDetail, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReportDetailRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class FrequencyOptions(_message.Message):
    __slots__ = ('frequency', 'start_date', 'end_date')

    class Frequency(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FREQUENCY_UNSPECIFIED: _ClassVar[FrequencyOptions.Frequency]
        DAILY: _ClassVar[FrequencyOptions.Frequency]
        WEEKLY: _ClassVar[FrequencyOptions.Frequency]
    FREQUENCY_UNSPECIFIED: FrequencyOptions.Frequency
    DAILY: FrequencyOptions.Frequency
    WEEKLY: FrequencyOptions.Frequency
    FREQUENCY_FIELD_NUMBER: _ClassVar[int]
    START_DATE_FIELD_NUMBER: _ClassVar[int]
    END_DATE_FIELD_NUMBER: _ClassVar[int]
    frequency: FrequencyOptions.Frequency
    start_date: _date_pb2.Date
    end_date: _date_pb2.Date

    def __init__(self, frequency: _Optional[_Union[FrequencyOptions.Frequency, str]]=..., start_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=..., end_date: _Optional[_Union[_date_pb2.Date, _Mapping]]=...) -> None:
        ...

class CSVOptions(_message.Message):
    __slots__ = ('record_separator', 'delimiter', 'header_required')
    RECORD_SEPARATOR_FIELD_NUMBER: _ClassVar[int]
    DELIMITER_FIELD_NUMBER: _ClassVar[int]
    HEADER_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    record_separator: str
    delimiter: str
    header_required: bool

    def __init__(self, record_separator: _Optional[str]=..., delimiter: _Optional[str]=..., header_required: bool=...) -> None:
        ...

class ParquetOptions(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CloudStorageFilters(_message.Message):
    __slots__ = ('bucket',)
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    bucket: str

    def __init__(self, bucket: _Optional[str]=...) -> None:
        ...

class CloudStorageDestinationOptions(_message.Message):
    __slots__ = ('bucket', 'destination_path')
    BUCKET_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_PATH_FIELD_NUMBER: _ClassVar[int]
    bucket: str
    destination_path: str

    def __init__(self, bucket: _Optional[str]=..., destination_path: _Optional[str]=...) -> None:
        ...

class ObjectMetadataReportOptions(_message.Message):
    __slots__ = ('metadata_fields', 'storage_filters', 'storage_destination_options')
    METADATA_FIELDS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_FILTERS_FIELD_NUMBER: _ClassVar[int]
    STORAGE_DESTINATION_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    metadata_fields: _containers.RepeatedScalarFieldContainer[str]
    storage_filters: CloudStorageFilters
    storage_destination_options: CloudStorageDestinationOptions

    def __init__(self, metadata_fields: _Optional[_Iterable[str]]=..., storage_filters: _Optional[_Union[CloudStorageFilters, _Mapping]]=..., storage_destination_options: _Optional[_Union[CloudStorageDestinationOptions, _Mapping]]=...) -> None:
        ...

class ReportConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'frequency_options', 'csv_options', 'parquet_options', 'object_metadata_report_options', 'labels', 'display_name')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FREQUENCY_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CSV_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    PARQUET_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    OBJECT_METADATA_REPORT_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    frequency_options: FrequencyOptions
    csv_options: CSVOptions
    parquet_options: ParquetOptions
    object_metadata_report_options: ObjectMetadataReportOptions
    labels: _containers.ScalarMap[str, str]
    display_name: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., frequency_options: _Optional[_Union[FrequencyOptions, _Mapping]]=..., csv_options: _Optional[_Union[CSVOptions, _Mapping]]=..., parquet_options: _Optional[_Union[ParquetOptions, _Mapping]]=..., object_metadata_report_options: _Optional[_Union[ObjectMetadataReportOptions, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., display_name: _Optional[str]=...) -> None:
        ...

class Identity(_message.Message):
    __slots__ = ('name', 'type')

    class IdentityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        IDENTITY_TYPE_UNSPECIFIED: _ClassVar[Identity.IdentityType]
        IDENTITY_TYPE_PER_CONFIG: _ClassVar[Identity.IdentityType]
        IDENTITY_TYPE_PER_PROJECT: _ClassVar[Identity.IdentityType]
    IDENTITY_TYPE_UNSPECIFIED: Identity.IdentityType
    IDENTITY_TYPE_PER_CONFIG: Identity.IdentityType
    IDENTITY_TYPE_PER_PROJECT: Identity.IdentityType
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: Identity.IdentityType

    def __init__(self, name: _Optional[str]=..., type: _Optional[_Union[Identity.IdentityType, str]]=...) -> None:
        ...

class DatasetConfig(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'uid', 'organization_number', 'source_projects', 'source_folders', 'organization_scope', 'cloud_storage_object_path', 'include_cloud_storage_locations', 'exclude_cloud_storage_locations', 'include_cloud_storage_buckets', 'exclude_cloud_storage_buckets', 'include_newly_created_buckets', 'skip_verification_and_ingest', 'retention_period_days', 'link', 'identity', 'status', 'dataset_config_state', 'description')

    class ConfigState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONFIG_STATE_UNSPECIFIED: _ClassVar[DatasetConfig.ConfigState]
        CONFIG_STATE_ACTIVE: _ClassVar[DatasetConfig.ConfigState]
        CONFIG_STATE_VERIFICATION_IN_PROGRESS: _ClassVar[DatasetConfig.ConfigState]
        CONFIG_STATE_CREATED: _ClassVar[DatasetConfig.ConfigState]
        CONFIG_STATE_PROCESSING: _ClassVar[DatasetConfig.ConfigState]
    CONFIG_STATE_UNSPECIFIED: DatasetConfig.ConfigState
    CONFIG_STATE_ACTIVE: DatasetConfig.ConfigState
    CONFIG_STATE_VERIFICATION_IN_PROGRESS: DatasetConfig.ConfigState
    CONFIG_STATE_CREATED: DatasetConfig.ConfigState
    CONFIG_STATE_PROCESSING: DatasetConfig.ConfigState

    class SourceProjects(_message.Message):
        __slots__ = ('project_numbers',)
        PROJECT_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        project_numbers: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, project_numbers: _Optional[_Iterable[int]]=...) -> None:
            ...

    class SourceFolders(_message.Message):
        __slots__ = ('folder_numbers',)
        FOLDER_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        folder_numbers: _containers.RepeatedScalarFieldContainer[int]

        def __init__(self, folder_numbers: _Optional[_Iterable[int]]=...) -> None:
            ...

    class CloudStorageLocations(_message.Message):
        __slots__ = ('locations',)
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        locations: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, locations: _Optional[_Iterable[str]]=...) -> None:
            ...

    class CloudStorageBuckets(_message.Message):
        __slots__ = ('cloud_storage_buckets',)

        class CloudStorageBucket(_message.Message):
            __slots__ = ('bucket_name', 'bucket_prefix_regex')
            BUCKET_NAME_FIELD_NUMBER: _ClassVar[int]
            BUCKET_PREFIX_REGEX_FIELD_NUMBER: _ClassVar[int]
            bucket_name: str
            bucket_prefix_regex: str

            def __init__(self, bucket_name: _Optional[str]=..., bucket_prefix_regex: _Optional[str]=...) -> None:
                ...
        CLOUD_STORAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
        cloud_storage_buckets: _containers.RepeatedCompositeFieldContainer[DatasetConfig.CloudStorageBuckets.CloudStorageBucket]

        def __init__(self, cloud_storage_buckets: _Optional[_Iterable[_Union[DatasetConfig.CloudStorageBuckets.CloudStorageBucket, _Mapping]]]=...) -> None:
            ...

    class Link(_message.Message):
        __slots__ = ('dataset', 'linked')
        DATASET_FIELD_NUMBER: _ClassVar[int]
        LINKED_FIELD_NUMBER: _ClassVar[int]
        dataset: str
        linked: bool

        def __init__(self, dataset: _Optional[str]=..., linked: bool=...) -> None:
            ...

    class BucketErrors(_message.Message):
        __slots__ = ('validated_count', 'permission_denied_count', 'permission_denied_bucket_ids', 'non_management_hub_entitled_count', 'internal_error_count', 'non_storage_intelligence_entitled_count', 'non_storage_intelligence_entitled_bucket_ids')
        VALIDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_COUNT_FIELD_NUMBER: _ClassVar[int]
        PERMISSION_DENIED_BUCKET_IDS_FIELD_NUMBER: _ClassVar[int]
        NON_MANAGEMENT_HUB_ENTITLED_COUNT_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        NON_STORAGE_INTELLIGENCE_ENTITLED_COUNT_FIELD_NUMBER: _ClassVar[int]
        NON_STORAGE_INTELLIGENCE_ENTITLED_BUCKET_IDS_FIELD_NUMBER: _ClassVar[int]
        validated_count: int
        permission_denied_count: int
        permission_denied_bucket_ids: _containers.RepeatedScalarFieldContainer[str]
        non_management_hub_entitled_count: int
        internal_error_count: int
        non_storage_intelligence_entitled_count: int
        non_storage_intelligence_entitled_bucket_ids: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, validated_count: _Optional[int]=..., permission_denied_count: _Optional[int]=..., permission_denied_bucket_ids: _Optional[_Iterable[str]]=..., non_management_hub_entitled_count: _Optional[int]=..., internal_error_count: _Optional[int]=..., non_storage_intelligence_entitled_count: _Optional[int]=..., non_storage_intelligence_entitled_bucket_ids: _Optional[_Iterable[str]]=...) -> None:
            ...

    class ProjectErrors(_message.Message):
        __slots__ = ('validated_count', 'outside_org_error_count', 'outside_org_project_numbers', 'non_management_hub_entitled_error_count', 'non_management_hub_entitled_project_numbers', 'non_storage_intelligence_entitled_error_count', 'non_storage_intelligence_entitled_project_numbers', 'internal_error_count', 'destination_project_org_error', 'destination_project_check_has_internal_error')
        VALIDATED_COUNT_FIELD_NUMBER: _ClassVar[int]
        OUTSIDE_ORG_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        OUTSIDE_ORG_PROJECT_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        NON_MANAGEMENT_HUB_ENTITLED_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        NON_MANAGEMENT_HUB_ENTITLED_PROJECT_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        NON_STORAGE_INTELLIGENCE_ENTITLED_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        NON_STORAGE_INTELLIGENCE_ENTITLED_PROJECT_NUMBERS_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_ERROR_COUNT_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_PROJECT_ORG_ERROR_FIELD_NUMBER: _ClassVar[int]
        DESTINATION_PROJECT_CHECK_HAS_INTERNAL_ERROR_FIELD_NUMBER: _ClassVar[int]
        validated_count: int
        outside_org_error_count: int
        outside_org_project_numbers: _containers.RepeatedScalarFieldContainer[int]
        non_management_hub_entitled_error_count: int
        non_management_hub_entitled_project_numbers: _containers.RepeatedScalarFieldContainer[int]
        non_storage_intelligence_entitled_error_count: int
        non_storage_intelligence_entitled_project_numbers: _containers.RepeatedScalarFieldContainer[int]
        internal_error_count: int
        destination_project_org_error: bool
        destination_project_check_has_internal_error: bool

        def __init__(self, validated_count: _Optional[int]=..., outside_org_error_count: _Optional[int]=..., outside_org_project_numbers: _Optional[_Iterable[int]]=..., non_management_hub_entitled_error_count: _Optional[int]=..., non_management_hub_entitled_project_numbers: _Optional[_Iterable[int]]=..., non_storage_intelligence_entitled_error_count: _Optional[int]=..., non_storage_intelligence_entitled_project_numbers: _Optional[_Iterable[int]]=..., internal_error_count: _Optional[int]=..., destination_project_org_error: bool=..., destination_project_check_has_internal_error: bool=...) -> None:
            ...

    class ValidationErrorsBeforeIngestion(_message.Message):
        __slots__ = ('bucket_errors', 'project_errors')
        BUCKET_ERRORS_FIELD_NUMBER: _ClassVar[int]
        PROJECT_ERRORS_FIELD_NUMBER: _ClassVar[int]
        bucket_errors: DatasetConfig.BucketErrors
        project_errors: DatasetConfig.ProjectErrors

        def __init__(self, bucket_errors: _Optional[_Union[DatasetConfig.BucketErrors, _Mapping]]=..., project_errors: _Optional[_Union[DatasetConfig.ProjectErrors, _Mapping]]=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_NUMBER_FIELD_NUMBER: _ClassVar[int]
    SOURCE_PROJECTS_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FOLDERS_FIELD_NUMBER: _ClassVar[int]
    ORGANIZATION_SCOPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_STORAGE_OBJECT_PATH_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOUD_STORAGE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CLOUD_STORAGE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_CLOUD_STORAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_CLOUD_STORAGE_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_NEWLY_CREATED_BUCKETS_FIELD_NUMBER: _ClassVar[int]
    SKIP_VERIFICATION_AND_INGEST_FIELD_NUMBER: _ClassVar[int]
    RETENTION_PERIOD_DAYS_FIELD_NUMBER: _ClassVar[int]
    LINK_FIELD_NUMBER: _ClassVar[int]
    IDENTITY_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    DATASET_CONFIG_STATE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    uid: str
    organization_number: int
    source_projects: DatasetConfig.SourceProjects
    source_folders: DatasetConfig.SourceFolders
    organization_scope: bool
    cloud_storage_object_path: str
    include_cloud_storage_locations: DatasetConfig.CloudStorageLocations
    exclude_cloud_storage_locations: DatasetConfig.CloudStorageLocations
    include_cloud_storage_buckets: DatasetConfig.CloudStorageBuckets
    exclude_cloud_storage_buckets: DatasetConfig.CloudStorageBuckets
    include_newly_created_buckets: bool
    skip_verification_and_ingest: bool
    retention_period_days: int
    link: DatasetConfig.Link
    identity: Identity
    status: _status_pb2.Status
    dataset_config_state: DatasetConfig.ConfigState
    description: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., uid: _Optional[str]=..., organization_number: _Optional[int]=..., source_projects: _Optional[_Union[DatasetConfig.SourceProjects, _Mapping]]=..., source_folders: _Optional[_Union[DatasetConfig.SourceFolders, _Mapping]]=..., organization_scope: bool=..., cloud_storage_object_path: _Optional[str]=..., include_cloud_storage_locations: _Optional[_Union[DatasetConfig.CloudStorageLocations, _Mapping]]=..., exclude_cloud_storage_locations: _Optional[_Union[DatasetConfig.CloudStorageLocations, _Mapping]]=..., include_cloud_storage_buckets: _Optional[_Union[DatasetConfig.CloudStorageBuckets, _Mapping]]=..., exclude_cloud_storage_buckets: _Optional[_Union[DatasetConfig.CloudStorageBuckets, _Mapping]]=..., include_newly_created_buckets: bool=..., skip_verification_and_ingest: bool=..., retention_period_days: _Optional[int]=..., link: _Optional[_Union[DatasetConfig.Link, _Mapping]]=..., identity: _Optional[_Union[Identity, _Mapping]]=..., status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., dataset_config_state: _Optional[_Union[DatasetConfig.ConfigState, str]]=..., description: _Optional[str]=...) -> None:
        ...

class ListDatasetConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDatasetConfigsResponse(_message.Message):
    __slots__ = ('dataset_configs', 'next_page_token', 'unreachable')
    DATASET_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    dataset_configs: _containers.RepeatedCompositeFieldContainer[DatasetConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, dataset_configs: _Optional[_Iterable[_Union[DatasetConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetDatasetConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateDatasetConfigRequest(_message.Message):
    __slots__ = ('parent', 'dataset_config_id', 'dataset_config', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset_config_id: str
    dataset_config: DatasetConfig
    request_id: str

    def __init__(self, parent: _Optional[str]=..., dataset_config_id: _Optional[str]=..., dataset_config: _Optional[_Union[DatasetConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateDatasetConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'dataset_config', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    DATASET_CONFIG_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    dataset_config: DatasetConfig
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., dataset_config: _Optional[_Union[DatasetConfig, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteDatasetConfigRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class LinkDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LinkDatasetResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class UnlinkDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class LocationMetadata(_message.Message):
    __slots__ = ('report_config_available', 'dataset_config_available')
    REPORT_CONFIG_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    DATASET_CONFIG_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    report_config_available: bool
    dataset_config_available: bool

    def __init__(self, report_config_available: bool=..., dataset_config_available: bool=...) -> None:
        ...