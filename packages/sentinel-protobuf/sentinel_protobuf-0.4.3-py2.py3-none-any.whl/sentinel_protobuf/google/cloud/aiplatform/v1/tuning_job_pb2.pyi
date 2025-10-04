from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1 import job_state_pb2 as _job_state_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TuningJob(_message.Message):
    __slots__ = ('base_model', 'supervised_tuning_spec', 'name', 'tuned_model_display_name', 'description', 'state', 'create_time', 'start_time', 'end_time', 'update_time', 'error', 'labels', 'experiment', 'tuned_model', 'tuning_data_stats', 'encryption_spec', 'service_account')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    SUPERVISED_TUNING_SPEC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TUNED_MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENT_FIELD_NUMBER: _ClassVar[int]
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    TUNING_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    supervised_tuning_spec: SupervisedTuningSpec
    name: str
    tuned_model_display_name: str
    description: str
    state: _job_state_pb2.JobState
    create_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    error: _status_pb2.Status
    labels: _containers.ScalarMap[str, str]
    experiment: str
    tuned_model: TunedModel
    tuning_data_stats: TuningDataStats
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    service_account: str

    def __init__(self, base_model: _Optional[str]=..., supervised_tuning_spec: _Optional[_Union[SupervisedTuningSpec, _Mapping]]=..., name: _Optional[str]=..., tuned_model_display_name: _Optional[str]=..., description: _Optional[str]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., experiment: _Optional[str]=..., tuned_model: _Optional[_Union[TunedModel, _Mapping]]=..., tuning_data_stats: _Optional[_Union[TuningDataStats, _Mapping]]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., service_account: _Optional[str]=...) -> None:
        ...

class TunedModel(_message.Message):
    __slots__ = ('model', 'endpoint', 'checkpoints')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINTS_FIELD_NUMBER: _ClassVar[int]
    model: str
    endpoint: str
    checkpoints: _containers.RepeatedCompositeFieldContainer[TunedModelCheckpoint]

    def __init__(self, model: _Optional[str]=..., endpoint: _Optional[str]=..., checkpoints: _Optional[_Iterable[_Union[TunedModelCheckpoint, _Mapping]]]=...) -> None:
        ...

class SupervisedTuningDatasetDistribution(_message.Message):
    __slots__ = ('sum', 'billable_sum', 'min', 'max', 'mean', 'median', 'p5', 'p95', 'buckets')

    class DatasetBucket(_message.Message):
        __slots__ = ('count', 'left', 'right')
        COUNT_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        count: float
        left: float
        right: float

        def __init__(self, count: _Optional[float]=..., left: _Optional[float]=..., right: _Optional[float]=...) -> None:
            ...
    SUM_FIELD_NUMBER: _ClassVar[int]
    BILLABLE_SUM_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_FIELD_NUMBER: _ClassVar[int]
    P5_FIELD_NUMBER: _ClassVar[int]
    P95_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    sum: int
    billable_sum: int
    min: float
    max: float
    mean: float
    median: float
    p5: float
    p95: float
    buckets: _containers.RepeatedCompositeFieldContainer[SupervisedTuningDatasetDistribution.DatasetBucket]

    def __init__(self, sum: _Optional[int]=..., billable_sum: _Optional[int]=..., min: _Optional[float]=..., max: _Optional[float]=..., mean: _Optional[float]=..., median: _Optional[float]=..., p5: _Optional[float]=..., p95: _Optional[float]=..., buckets: _Optional[_Iterable[_Union[SupervisedTuningDatasetDistribution.DatasetBucket, _Mapping]]]=...) -> None:
        ...

class SupervisedTuningDataStats(_message.Message):
    __slots__ = ('tuning_dataset_example_count', 'total_tuning_character_count', 'total_billable_character_count', 'total_billable_token_count', 'tuning_step_count', 'user_input_token_distribution', 'user_output_token_distribution', 'user_message_per_example_distribution', 'user_dataset_examples', 'total_truncated_example_count', 'truncated_example_indices', 'dropped_example_reasons')
    TUNING_DATASET_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TUNING_CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    TUNING_STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_TOKEN_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_OUTPUT_TOKEN_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_PER_EXAMPLE_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_DATASET_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TRUNCATED_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TRUNCATED_EXAMPLE_INDICES_FIELD_NUMBER: _ClassVar[int]
    DROPPED_EXAMPLE_REASONS_FIELD_NUMBER: _ClassVar[int]
    tuning_dataset_example_count: int
    total_tuning_character_count: int
    total_billable_character_count: int
    total_billable_token_count: int
    tuning_step_count: int
    user_input_token_distribution: SupervisedTuningDatasetDistribution
    user_output_token_distribution: SupervisedTuningDatasetDistribution
    user_message_per_example_distribution: SupervisedTuningDatasetDistribution
    user_dataset_examples: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    total_truncated_example_count: int
    truncated_example_indices: _containers.RepeatedScalarFieldContainer[int]
    dropped_example_reasons: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, tuning_dataset_example_count: _Optional[int]=..., total_tuning_character_count: _Optional[int]=..., total_billable_character_count: _Optional[int]=..., total_billable_token_count: _Optional[int]=..., tuning_step_count: _Optional[int]=..., user_input_token_distribution: _Optional[_Union[SupervisedTuningDatasetDistribution, _Mapping]]=..., user_output_token_distribution: _Optional[_Union[SupervisedTuningDatasetDistribution, _Mapping]]=..., user_message_per_example_distribution: _Optional[_Union[SupervisedTuningDatasetDistribution, _Mapping]]=..., user_dataset_examples: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., total_truncated_example_count: _Optional[int]=..., truncated_example_indices: _Optional[_Iterable[int]]=..., dropped_example_reasons: _Optional[_Iterable[str]]=...) -> None:
        ...

class TuningDataStats(_message.Message):
    __slots__ = ('supervised_tuning_data_stats',)
    SUPERVISED_TUNING_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    supervised_tuning_data_stats: SupervisedTuningDataStats

    def __init__(self, supervised_tuning_data_stats: _Optional[_Union[SupervisedTuningDataStats, _Mapping]]=...) -> None:
        ...

class SupervisedHyperParameters(_message.Message):
    __slots__ = ('epoch_count', 'learning_rate_multiplier', 'adapter_size')

    class AdapterSize(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ADAPTER_SIZE_UNSPECIFIED: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_ONE: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_TWO: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_FOUR: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_EIGHT: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_SIXTEEN: _ClassVar[SupervisedHyperParameters.AdapterSize]
        ADAPTER_SIZE_THIRTY_TWO: _ClassVar[SupervisedHyperParameters.AdapterSize]
    ADAPTER_SIZE_UNSPECIFIED: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_ONE: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_TWO: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_FOUR: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_EIGHT: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_SIXTEEN: SupervisedHyperParameters.AdapterSize
    ADAPTER_SIZE_THIRTY_TWO: SupervisedHyperParameters.AdapterSize
    EPOCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    epoch_count: int
    learning_rate_multiplier: float
    adapter_size: SupervisedHyperParameters.AdapterSize

    def __init__(self, epoch_count: _Optional[int]=..., learning_rate_multiplier: _Optional[float]=..., adapter_size: _Optional[_Union[SupervisedHyperParameters.AdapterSize, str]]=...) -> None:
        ...

class SupervisedTuningSpec(_message.Message):
    __slots__ = ('training_dataset_uri', 'validation_dataset_uri', 'hyper_parameters', 'export_last_checkpoint_only')
    TRAINING_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    HYPER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_LAST_CHECKPOINT_ONLY_FIELD_NUMBER: _ClassVar[int]
    training_dataset_uri: str
    validation_dataset_uri: str
    hyper_parameters: SupervisedHyperParameters
    export_last_checkpoint_only: bool

    def __init__(self, training_dataset_uri: _Optional[str]=..., validation_dataset_uri: _Optional[str]=..., hyper_parameters: _Optional[_Union[SupervisedHyperParameters, _Mapping]]=..., export_last_checkpoint_only: bool=...) -> None:
        ...

class TunedModelRef(_message.Message):
    __slots__ = ('tuned_model', 'tuning_job', 'pipeline_job')
    TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    TUNING_JOB_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_JOB_FIELD_NUMBER: _ClassVar[int]
    tuned_model: str
    tuning_job: str
    pipeline_job: str

    def __init__(self, tuned_model: _Optional[str]=..., tuning_job: _Optional[str]=..., pipeline_job: _Optional[str]=...) -> None:
        ...

class TunedModelCheckpoint(_message.Message):
    __slots__ = ('checkpoint_id', 'epoch', 'step', 'endpoint')
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    EPOCH_FIELD_NUMBER: _ClassVar[int]
    STEP_FIELD_NUMBER: _ClassVar[int]
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    checkpoint_id: str
    epoch: int
    step: int
    endpoint: str

    def __init__(self, checkpoint_id: _Optional[str]=..., epoch: _Optional[int]=..., step: _Optional[int]=..., endpoint: _Optional[str]=...) -> None:
        ...