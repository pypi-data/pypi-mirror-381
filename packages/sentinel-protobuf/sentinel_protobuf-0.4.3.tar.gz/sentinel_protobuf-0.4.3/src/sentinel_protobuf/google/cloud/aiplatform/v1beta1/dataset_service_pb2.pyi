from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import annotation_pb2 as _annotation_pb2
from google.cloud.aiplatform.v1beta1 import annotation_spec_pb2 as _annotation_spec_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import data_item_pb2 as _data_item_pb2
from google.cloud.aiplatform.v1beta1 import dataset_pb2 as _dataset_pb2
from google.cloud.aiplatform.v1beta1 import dataset_version_pb2 as _dataset_version_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.cloud.aiplatform.v1beta1 import saved_query_pb2 as _saved_query_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateDatasetRequest(_message.Message):
    __slots__ = ('parent', 'dataset')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset: _dataset_pb2.Dataset

    def __init__(self, parent: _Optional[str]=..., dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=...) -> None:
        ...

class CreateDatasetOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GetDatasetRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateDatasetRequest(_message.Message):
    __slots__ = ('dataset', 'update_mask')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset: _dataset_pb2.Dataset
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset: _Optional[_Union[_dataset_pb2.Dataset, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class UpdateDatasetVersionRequest(_message.Message):
    __slots__ = ('dataset_version', 'update_mask')
    DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    dataset_version: _dataset_version_pb2.DatasetVersion
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, dataset_version: _Optional[_Union[_dataset_version_pb2.DatasetVersion, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListDatasetsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDatasetsResponse(_message.Message):
    __slots__ = ('datasets', 'next_page_token')
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.Dataset]
    next_page_token: str

    def __init__(self, datasets: _Optional[_Iterable[_Union[_dataset_pb2.Dataset, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteDatasetRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ImportDataRequest(_message.Message):
    __slots__ = ('name', 'import_configs')
    NAME_FIELD_NUMBER: _ClassVar[int]
    IMPORT_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    import_configs: _containers.RepeatedCompositeFieldContainer[_dataset_pb2.ImportDataConfig]

    def __init__(self, name: _Optional[str]=..., import_configs: _Optional[_Iterable[_Union[_dataset_pb2.ImportDataConfig, _Mapping]]]=...) -> None:
        ...

class ImportDataResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ImportDataOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ExportDataRequest(_message.Message):
    __slots__ = ('name', 'export_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EXPORT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    export_config: _dataset_pb2.ExportDataConfig

    def __init__(self, name: _Optional[str]=..., export_config: _Optional[_Union[_dataset_pb2.ExportDataConfig, _Mapping]]=...) -> None:
        ...

class ExportDataResponse(_message.Message):
    __slots__ = ('exported_files',)
    EXPORTED_FILES_FIELD_NUMBER: _ClassVar[int]
    exported_files: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, exported_files: _Optional[_Iterable[str]]=...) -> None:
        ...

class ExportDataOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata', 'gcs_output_directory')
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata
    gcs_output_directory: str

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=..., gcs_output_directory: _Optional[str]=...) -> None:
        ...

class CreateDatasetVersionRequest(_message.Message):
    __slots__ = ('parent', 'dataset_version')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DATASET_VERSION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    dataset_version: _dataset_version_pb2.DatasetVersion

    def __init__(self, parent: _Optional[str]=..., dataset_version: _Optional[_Union[_dataset_version_pb2.DatasetVersion, _Mapping]]=...) -> None:
        ...

class CreateDatasetVersionOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class DeleteDatasetVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetDatasetVersionRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListDatasetVersionsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDatasetVersionsResponse(_message.Message):
    __slots__ = ('dataset_versions', 'next_page_token')
    DATASET_VERSIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    dataset_versions: _containers.RepeatedCompositeFieldContainer[_dataset_version_pb2.DatasetVersion]
    next_page_token: str

    def __init__(self, dataset_versions: _Optional[_Iterable[_Union[_dataset_version_pb2.DatasetVersion, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class RestoreDatasetVersionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RestoreDatasetVersionOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class ListDataItemsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListDataItemsResponse(_message.Message):
    __slots__ = ('data_items', 'next_page_token')
    DATA_ITEMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_items: _containers.RepeatedCompositeFieldContainer[_data_item_pb2.DataItem]
    next_page_token: str

    def __init__(self, data_items: _Optional[_Iterable[_Union[_data_item_pb2.DataItem, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchDataItemsRequest(_message.Message):
    __slots__ = ('order_by_data_item', 'order_by_annotation', 'dataset', 'saved_query', 'data_labeling_job', 'data_item_filter', 'annotations_filter', 'annotation_filters', 'field_mask', 'annotations_limit', 'page_size', 'order_by', 'page_token')

    class OrderByAnnotation(_message.Message):
        __slots__ = ('saved_query', 'order_by')
        SAVED_QUERY_FIELD_NUMBER: _ClassVar[int]
        ORDER_BY_FIELD_NUMBER: _ClassVar[int]
        saved_query: str
        order_by: str

        def __init__(self, saved_query: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
            ...
    ORDER_BY_DATA_ITEM_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_ANNOTATION_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    SAVED_QUERY_FIELD_NUMBER: _ClassVar[int]
    DATA_LABELING_JOB_FIELD_NUMBER: _ClassVar[int]
    DATA_ITEM_FILTER_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FILTER_FIELD_NUMBER: _ClassVar[int]
    ANNOTATION_FILTERS_FIELD_NUMBER: _ClassVar[int]
    FIELD_MASK_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_LIMIT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    order_by_data_item: str
    order_by_annotation: SearchDataItemsRequest.OrderByAnnotation
    dataset: str
    saved_query: str
    data_labeling_job: str
    data_item_filter: str
    annotations_filter: str
    annotation_filters: _containers.RepeatedScalarFieldContainer[str]
    field_mask: _field_mask_pb2.FieldMask
    annotations_limit: int
    page_size: int
    order_by: str
    page_token: str

    def __init__(self, order_by_data_item: _Optional[str]=..., order_by_annotation: _Optional[_Union[SearchDataItemsRequest.OrderByAnnotation, _Mapping]]=..., dataset: _Optional[str]=..., saved_query: _Optional[str]=..., data_labeling_job: _Optional[str]=..., data_item_filter: _Optional[str]=..., annotations_filter: _Optional[str]=..., annotation_filters: _Optional[_Iterable[str]]=..., field_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., annotations_limit: _Optional[int]=..., page_size: _Optional[int]=..., order_by: _Optional[str]=..., page_token: _Optional[str]=...) -> None:
        ...

class SearchDataItemsResponse(_message.Message):
    __slots__ = ('data_item_views', 'next_page_token')
    DATA_ITEM_VIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    data_item_views: _containers.RepeatedCompositeFieldContainer[DataItemView]
    next_page_token: str

    def __init__(self, data_item_views: _Optional[_Iterable[_Union[DataItemView, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DataItemView(_message.Message):
    __slots__ = ('data_item', 'annotations', 'has_truncated_annotations')
    DATA_ITEM_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    HAS_TRUNCATED_ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    data_item: _data_item_pb2.DataItem
    annotations: _containers.RepeatedCompositeFieldContainer[_annotation_pb2.Annotation]
    has_truncated_annotations: bool

    def __init__(self, data_item: _Optional[_Union[_data_item_pb2.DataItem, _Mapping]]=..., annotations: _Optional[_Iterable[_Union[_annotation_pb2.Annotation, _Mapping]]]=..., has_truncated_annotations: bool=...) -> None:
        ...

class ListSavedQueriesRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListSavedQueriesResponse(_message.Message):
    __slots__ = ('saved_queries', 'next_page_token')
    SAVED_QUERIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    saved_queries: _containers.RepeatedCompositeFieldContainer[_saved_query_pb2.SavedQuery]
    next_page_token: str

    def __init__(self, saved_queries: _Optional[_Iterable[_Union[_saved_query_pb2.SavedQuery, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteSavedQueryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetAnnotationSpecRequest(_message.Message):
    __slots__ = ('name', 'read_mask')
    NAME_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    name: str
    read_mask: _field_mask_pb2.FieldMask

    def __init__(self, name: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListAnnotationsRequest(_message.Message):
    __slots__ = ('parent', 'filter', 'page_size', 'page_token', 'read_mask', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    READ_MASK_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    filter: str
    page_size: int
    page_token: str
    read_mask: _field_mask_pb2.FieldMask
    order_by: str

    def __init__(self, parent: _Optional[str]=..., filter: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., read_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListAnnotationsResponse(_message.Message):
    __slots__ = ('annotations', 'next_page_token')
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    annotations: _containers.RepeatedCompositeFieldContainer[_annotation_pb2.Annotation]
    next_page_token: str

    def __init__(self, annotations: _Optional[_Iterable[_Union[_annotation_pb2.Annotation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class AssessDataRequest(_message.Message):
    __slots__ = ('tuning_validation_assessment_config', 'tuning_resource_usage_assessment_config', 'batch_prediction_validation_assessment_config', 'batch_prediction_resource_usage_assessment_config', 'name', 'gemini_request_read_config')

    class TuningValidationAssessmentConfig(_message.Message):
        __slots__ = ('model_name', 'dataset_usage')

        class DatasetUsage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DATASET_USAGE_UNSPECIFIED: _ClassVar[AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage]
            SFT_TRAINING: _ClassVar[AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage]
            SFT_VALIDATION: _ClassVar[AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage]
        DATASET_USAGE_UNSPECIFIED: AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage
        SFT_TRAINING: AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage
        SFT_VALIDATION: AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        DATASET_USAGE_FIELD_NUMBER: _ClassVar[int]
        model_name: str
        dataset_usage: AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage

        def __init__(self, model_name: _Optional[str]=..., dataset_usage: _Optional[_Union[AssessDataRequest.TuningValidationAssessmentConfig.DatasetUsage, str]]=...) -> None:
            ...

    class TuningResourceUsageAssessmentConfig(_message.Message):
        __slots__ = ('model_name',)
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        model_name: str

        def __init__(self, model_name: _Optional[str]=...) -> None:
            ...

    class BatchPredictionValidationAssessmentConfig(_message.Message):
        __slots__ = ('model_name',)
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        model_name: str

        def __init__(self, model_name: _Optional[str]=...) -> None:
            ...

    class BatchPredictionResourceUsageAssessmentConfig(_message.Message):
        __slots__ = ('model_name',)
        MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
        model_name: str

        def __init__(self, model_name: _Optional[str]=...) -> None:
            ...
    TUNING_VALIDATION_ASSESSMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TUNING_RESOURCE_USAGE_ASSESSMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_VALIDATION_ASSESSMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_RESOURCE_USAGE_ASSESSMENT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEMINI_REQUEST_READ_CONFIG_FIELD_NUMBER: _ClassVar[int]
    tuning_validation_assessment_config: AssessDataRequest.TuningValidationAssessmentConfig
    tuning_resource_usage_assessment_config: AssessDataRequest.TuningResourceUsageAssessmentConfig
    batch_prediction_validation_assessment_config: AssessDataRequest.BatchPredictionValidationAssessmentConfig
    batch_prediction_resource_usage_assessment_config: AssessDataRequest.BatchPredictionResourceUsageAssessmentConfig
    name: str
    gemini_request_read_config: GeminiRequestReadConfig

    def __init__(self, tuning_validation_assessment_config: _Optional[_Union[AssessDataRequest.TuningValidationAssessmentConfig, _Mapping]]=..., tuning_resource_usage_assessment_config: _Optional[_Union[AssessDataRequest.TuningResourceUsageAssessmentConfig, _Mapping]]=..., batch_prediction_validation_assessment_config: _Optional[_Union[AssessDataRequest.BatchPredictionValidationAssessmentConfig, _Mapping]]=..., batch_prediction_resource_usage_assessment_config: _Optional[_Union[AssessDataRequest.BatchPredictionResourceUsageAssessmentConfig, _Mapping]]=..., name: _Optional[str]=..., gemini_request_read_config: _Optional[_Union[GeminiRequestReadConfig, _Mapping]]=...) -> None:
        ...

class AssessDataResponse(_message.Message):
    __slots__ = ('tuning_validation_assessment_result', 'tuning_resource_usage_assessment_result', 'batch_prediction_validation_assessment_result', 'batch_prediction_resource_usage_assessment_result')

    class TuningValidationAssessmentResult(_message.Message):
        __slots__ = ('errors',)
        ERRORS_FIELD_NUMBER: _ClassVar[int]
        errors: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, errors: _Optional[_Iterable[str]]=...) -> None:
            ...

    class TuningResourceUsageAssessmentResult(_message.Message):
        __slots__ = ('token_count', 'billable_character_count')
        TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        BILLABLE_CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
        token_count: int
        billable_character_count: int

        def __init__(self, token_count: _Optional[int]=..., billable_character_count: _Optional[int]=...) -> None:
            ...

    class BatchPredictionValidationAssessmentResult(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class BatchPredictionResourceUsageAssessmentResult(_message.Message):
        __slots__ = ('token_count', 'audio_token_count')
        TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        token_count: int
        audio_token_count: int

        def __init__(self, token_count: _Optional[int]=..., audio_token_count: _Optional[int]=...) -> None:
            ...
    TUNING_VALIDATION_ASSESSMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    TUNING_RESOURCE_USAGE_ASSESSMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_VALIDATION_ASSESSMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    BATCH_PREDICTION_RESOURCE_USAGE_ASSESSMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    tuning_validation_assessment_result: AssessDataResponse.TuningValidationAssessmentResult
    tuning_resource_usage_assessment_result: AssessDataResponse.TuningResourceUsageAssessmentResult
    batch_prediction_validation_assessment_result: AssessDataResponse.BatchPredictionValidationAssessmentResult
    batch_prediction_resource_usage_assessment_result: AssessDataResponse.BatchPredictionResourceUsageAssessmentResult

    def __init__(self, tuning_validation_assessment_result: _Optional[_Union[AssessDataResponse.TuningValidationAssessmentResult, _Mapping]]=..., tuning_resource_usage_assessment_result: _Optional[_Union[AssessDataResponse.TuningResourceUsageAssessmentResult, _Mapping]]=..., batch_prediction_validation_assessment_result: _Optional[_Union[AssessDataResponse.BatchPredictionValidationAssessmentResult, _Mapping]]=..., batch_prediction_resource_usage_assessment_result: _Optional[_Union[AssessDataResponse.BatchPredictionResourceUsageAssessmentResult, _Mapping]]=...) -> None:
        ...

class AssessDataOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class GeminiTemplateConfig(_message.Message):
    __slots__ = ('gemini_example', 'field_mapping')

    class FieldMappingEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    GEMINI_EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    FIELD_MAPPING_FIELD_NUMBER: _ClassVar[int]
    gemini_example: GeminiExample
    field_mapping: _containers.ScalarMap[str, str]

    def __init__(self, gemini_example: _Optional[_Union[GeminiExample, _Mapping]]=..., field_mapping: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class GeminiRequestReadConfig(_message.Message):
    __slots__ = ('template_config', 'assembled_request_column_name')
    TEMPLATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ASSEMBLED_REQUEST_COLUMN_NAME_FIELD_NUMBER: _ClassVar[int]
    template_config: GeminiTemplateConfig
    assembled_request_column_name: str

    def __init__(self, template_config: _Optional[_Union[GeminiTemplateConfig, _Mapping]]=..., assembled_request_column_name: _Optional[str]=...) -> None:
        ...

class GeminiExample(_message.Message):
    __slots__ = ('model', 'contents', 'system_instruction', 'cached_content', 'tools', 'tool_config', 'labels', 'safety_settings', 'generation_config')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    MODEL_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CACHED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    TOOL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SAFETY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    model: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    system_instruction: _content_pb2.Content
    cached_content: str
    tools: _containers.RepeatedCompositeFieldContainer[_tool_pb2.Tool]
    tool_config: _tool_pb2.ToolConfig
    labels: _containers.ScalarMap[str, str]
    safety_settings: _containers.RepeatedCompositeFieldContainer[_content_pb2.SafetySetting]
    generation_config: _content_pb2.GenerationConfig

    def __init__(self, model: _Optional[str]=..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., system_instruction: _Optional[_Union[_content_pb2.Content, _Mapping]]=..., cached_content: _Optional[str]=..., tools: _Optional[_Iterable[_Union[_tool_pb2.Tool, _Mapping]]]=..., tool_config: _Optional[_Union[_tool_pb2.ToolConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., safety_settings: _Optional[_Iterable[_Union[_content_pb2.SafetySetting, _Mapping]]]=..., generation_config: _Optional[_Union[_content_pb2.GenerationConfig, _Mapping]]=...) -> None:
        ...

class AssembleDataRequest(_message.Message):
    __slots__ = ('name', 'gemini_request_read_config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    GEMINI_REQUEST_READ_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    gemini_request_read_config: GeminiRequestReadConfig

    def __init__(self, name: _Optional[str]=..., gemini_request_read_config: _Optional[_Union[GeminiRequestReadConfig, _Mapping]]=...) -> None:
        ...

class AssembleDataResponse(_message.Message):
    __slots__ = ('bigquery_destination',)
    BIGQUERY_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    bigquery_destination: str

    def __init__(self, bigquery_destination: _Optional[str]=...) -> None:
        ...

class AssembleDataOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...