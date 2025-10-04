from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as _encryption_spec_pb2
from google.cloud.aiplatform.v1beta1 import evaluation_service_pb2 as _evaluation_service_pb2
from google.cloud.aiplatform.v1beta1 import job_state_pb2 as _job_state_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class TuningJob(_message.Message):
    __slots__ = ('base_model', 'pre_tuned_model', 'supervised_tuning_spec', 'distillation_spec', 'partner_model_tuning_spec', 'veo_tuning_spec', 'name', 'tuned_model_display_name', 'description', 'custom_base_model', 'state', 'create_time', 'start_time', 'end_time', 'update_time', 'error', 'labels', 'experiment', 'tuned_model', 'tuning_data_stats', 'pipeline_job', 'encryption_spec', 'service_account', 'output_uri', 'evaluate_dataset_runs')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    PRE_TUNED_MODEL_FIELD_NUMBER: _ClassVar[int]
    SUPERVISED_TUNING_SPEC_FIELD_NUMBER: _ClassVar[int]
    DISTILLATION_SPEC_FIELD_NUMBER: _ClassVar[int]
    PARTNER_MODEL_TUNING_SPEC_FIELD_NUMBER: _ClassVar[int]
    VEO_TUNING_SPEC_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TUNED_MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
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
    PIPELINE_JOB_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTION_SPEC_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_URI_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_DATASET_RUNS_FIELD_NUMBER: _ClassVar[int]
    base_model: str
    pre_tuned_model: PreTunedModel
    supervised_tuning_spec: SupervisedTuningSpec
    distillation_spec: DistillationSpec
    partner_model_tuning_spec: PartnerModelTuningSpec
    veo_tuning_spec: VeoTuningSpec
    name: str
    tuned_model_display_name: str
    description: str
    custom_base_model: str
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
    pipeline_job: str
    encryption_spec: _encryption_spec_pb2.EncryptionSpec
    service_account: str
    output_uri: str
    evaluate_dataset_runs: _containers.RepeatedCompositeFieldContainer[EvaluateDatasetRun]

    def __init__(self, base_model: _Optional[str]=..., pre_tuned_model: _Optional[_Union[PreTunedModel, _Mapping]]=..., supervised_tuning_spec: _Optional[_Union[SupervisedTuningSpec, _Mapping]]=..., distillation_spec: _Optional[_Union[DistillationSpec, _Mapping]]=..., partner_model_tuning_spec: _Optional[_Union[PartnerModelTuningSpec, _Mapping]]=..., veo_tuning_spec: _Optional[_Union[VeoTuningSpec, _Mapping]]=..., name: _Optional[str]=..., tuned_model_display_name: _Optional[str]=..., description: _Optional[str]=..., custom_base_model: _Optional[str]=..., state: _Optional[_Union[_job_state_pb2.JobState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., experiment: _Optional[str]=..., tuned_model: _Optional[_Union[TunedModel, _Mapping]]=..., tuning_data_stats: _Optional[_Union[TuningDataStats, _Mapping]]=..., pipeline_job: _Optional[str]=..., encryption_spec: _Optional[_Union[_encryption_spec_pb2.EncryptionSpec, _Mapping]]=..., service_account: _Optional[str]=..., output_uri: _Optional[str]=..., evaluate_dataset_runs: _Optional[_Iterable[_Union[EvaluateDatasetRun, _Mapping]]]=...) -> None:
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

class DatasetDistribution(_message.Message):
    __slots__ = ('sum', 'min', 'max', 'mean', 'median', 'p5', 'p95', 'buckets')

    class DistributionBucket(_message.Message):
        __slots__ = ('count', 'left', 'right')
        COUNT_FIELD_NUMBER: _ClassVar[int]
        LEFT_FIELD_NUMBER: _ClassVar[int]
        RIGHT_FIELD_NUMBER: _ClassVar[int]
        count: int
        left: float
        right: float

        def __init__(self, count: _Optional[int]=..., left: _Optional[float]=..., right: _Optional[float]=...) -> None:
            ...
    SUM_FIELD_NUMBER: _ClassVar[int]
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    MEAN_FIELD_NUMBER: _ClassVar[int]
    MEDIAN_FIELD_NUMBER: _ClassVar[int]
    P5_FIELD_NUMBER: _ClassVar[int]
    P95_FIELD_NUMBER: _ClassVar[int]
    BUCKETS_FIELD_NUMBER: _ClassVar[int]
    sum: float
    min: float
    max: float
    mean: float
    median: float
    p5: float
    p95: float
    buckets: _containers.RepeatedCompositeFieldContainer[DatasetDistribution.DistributionBucket]

    def __init__(self, sum: _Optional[float]=..., min: _Optional[float]=..., max: _Optional[float]=..., mean: _Optional[float]=..., median: _Optional[float]=..., p5: _Optional[float]=..., p95: _Optional[float]=..., buckets: _Optional[_Iterable[_Union[DatasetDistribution.DistributionBucket, _Mapping]]]=...) -> None:
        ...

class DatasetStats(_message.Message):
    __slots__ = ('tuning_dataset_example_count', 'total_tuning_character_count', 'total_billable_character_count', 'tuning_step_count', 'user_input_token_distribution', 'user_output_token_distribution', 'user_message_per_example_distribution', 'user_dataset_examples')
    TUNING_DATASET_EXAMPLE_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_TUNING_CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_CHARACTER_COUNT_FIELD_NUMBER: _ClassVar[int]
    TUNING_STEP_COUNT_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_TOKEN_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_OUTPUT_TOKEN_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_MESSAGE_PER_EXAMPLE_DISTRIBUTION_FIELD_NUMBER: _ClassVar[int]
    USER_DATASET_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    tuning_dataset_example_count: int
    total_tuning_character_count: int
    total_billable_character_count: int
    tuning_step_count: int
    user_input_token_distribution: DatasetDistribution
    user_output_token_distribution: DatasetDistribution
    user_message_per_example_distribution: DatasetDistribution
    user_dataset_examples: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]

    def __init__(self, tuning_dataset_example_count: _Optional[int]=..., total_tuning_character_count: _Optional[int]=..., total_billable_character_count: _Optional[int]=..., tuning_step_count: _Optional[int]=..., user_input_token_distribution: _Optional[_Union[DatasetDistribution, _Mapping]]=..., user_output_token_distribution: _Optional[_Union[DatasetDistribution, _Mapping]]=..., user_message_per_example_distribution: _Optional[_Union[DatasetDistribution, _Mapping]]=..., user_dataset_examples: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=...) -> None:
        ...

class DistillationDataStats(_message.Message):
    __slots__ = ('training_dataset_stats',)
    TRAINING_DATASET_STATS_FIELD_NUMBER: _ClassVar[int]
    training_dataset_stats: DatasetStats

    def __init__(self, training_dataset_stats: _Optional[_Union[DatasetStats, _Mapping]]=...) -> None:
        ...

class TuningDataStats(_message.Message):
    __slots__ = ('supervised_tuning_data_stats', 'distillation_data_stats')
    SUPERVISED_TUNING_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    DISTILLATION_DATA_STATS_FIELD_NUMBER: _ClassVar[int]
    supervised_tuning_data_stats: SupervisedTuningDataStats
    distillation_data_stats: DistillationDataStats

    def __init__(self, supervised_tuning_data_stats: _Optional[_Union[SupervisedTuningDataStats, _Mapping]]=..., distillation_data_stats: _Optional[_Union[DistillationDataStats, _Mapping]]=...) -> None:
        ...

class SupervisedHyperParameters(_message.Message):
    __slots__ = ('epoch_count', 'learning_rate_multiplier', 'learning_rate', 'adapter_size', 'batch_size')

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
    LEARNING_RATE_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    BATCH_SIZE_FIELD_NUMBER: _ClassVar[int]
    epoch_count: int
    learning_rate_multiplier: float
    learning_rate: float
    adapter_size: SupervisedHyperParameters.AdapterSize
    batch_size: int

    def __init__(self, epoch_count: _Optional[int]=..., learning_rate_multiplier: _Optional[float]=..., learning_rate: _Optional[float]=..., adapter_size: _Optional[_Union[SupervisedHyperParameters.AdapterSize, str]]=..., batch_size: _Optional[int]=...) -> None:
        ...

class SupervisedTuningSpec(_message.Message):
    __slots__ = ('training_dataset_uri', 'validation_dataset_uri', 'hyper_parameters', 'export_last_checkpoint_only', 'evaluation_config', 'tuning_mode')

    class TuningMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TUNING_MODE_UNSPECIFIED: _ClassVar[SupervisedTuningSpec.TuningMode]
        TUNING_MODE_FULL: _ClassVar[SupervisedTuningSpec.TuningMode]
        TUNING_MODE_PEFT_ADAPTER: _ClassVar[SupervisedTuningSpec.TuningMode]
    TUNING_MODE_UNSPECIFIED: SupervisedTuningSpec.TuningMode
    TUNING_MODE_FULL: SupervisedTuningSpec.TuningMode
    TUNING_MODE_PEFT_ADAPTER: SupervisedTuningSpec.TuningMode
    TRAINING_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    HYPER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPORT_LAST_CHECKPOINT_ONLY_FIELD_NUMBER: _ClassVar[int]
    EVALUATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TUNING_MODE_FIELD_NUMBER: _ClassVar[int]
    training_dataset_uri: str
    validation_dataset_uri: str
    hyper_parameters: SupervisedHyperParameters
    export_last_checkpoint_only: bool
    evaluation_config: EvaluationConfig
    tuning_mode: SupervisedTuningSpec.TuningMode

    def __init__(self, training_dataset_uri: _Optional[str]=..., validation_dataset_uri: _Optional[str]=..., hyper_parameters: _Optional[_Union[SupervisedHyperParameters, _Mapping]]=..., export_last_checkpoint_only: bool=..., evaluation_config: _Optional[_Union[EvaluationConfig, _Mapping]]=..., tuning_mode: _Optional[_Union[SupervisedTuningSpec.TuningMode, str]]=...) -> None:
        ...

class DistillationSpec(_message.Message):
    __slots__ = ('base_teacher_model', 'tuned_teacher_model_source', 'training_dataset_uri', 'validation_dataset_uri', 'hyper_parameters', 'student_model', 'pipeline_root_directory')
    BASE_TEACHER_MODEL_FIELD_NUMBER: _ClassVar[int]
    TUNED_TEACHER_MODEL_SOURCE_FIELD_NUMBER: _ClassVar[int]
    TRAINING_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    HYPER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    STUDENT_MODEL_FIELD_NUMBER: _ClassVar[int]
    PIPELINE_ROOT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    base_teacher_model: str
    tuned_teacher_model_source: str
    training_dataset_uri: str
    validation_dataset_uri: str
    hyper_parameters: DistillationHyperParameters
    student_model: str
    pipeline_root_directory: str

    def __init__(self, base_teacher_model: _Optional[str]=..., tuned_teacher_model_source: _Optional[str]=..., training_dataset_uri: _Optional[str]=..., validation_dataset_uri: _Optional[str]=..., hyper_parameters: _Optional[_Union[DistillationHyperParameters, _Mapping]]=..., student_model: _Optional[str]=..., pipeline_root_directory: _Optional[str]=...) -> None:
        ...

class DistillationHyperParameters(_message.Message):
    __slots__ = ('epoch_count', 'learning_rate_multiplier', 'adapter_size')
    EPOCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    ADAPTER_SIZE_FIELD_NUMBER: _ClassVar[int]
    epoch_count: int
    learning_rate_multiplier: float
    adapter_size: SupervisedHyperParameters.AdapterSize

    def __init__(self, epoch_count: _Optional[int]=..., learning_rate_multiplier: _Optional[float]=..., adapter_size: _Optional[_Union[SupervisedHyperParameters.AdapterSize, str]]=...) -> None:
        ...

class PartnerModelTuningSpec(_message.Message):
    __slots__ = ('training_dataset_uri', 'validation_dataset_uri', 'hyper_parameters')

    class HyperParametersEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _struct_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
            ...
    TRAINING_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    HYPER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    training_dataset_uri: str
    validation_dataset_uri: str
    hyper_parameters: _containers.MessageMap[str, _struct_pb2.Value]

    def __init__(self, training_dataset_uri: _Optional[str]=..., validation_dataset_uri: _Optional[str]=..., hyper_parameters: _Optional[_Mapping[str, _struct_pb2.Value]]=...) -> None:
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

class VeoHyperParameters(_message.Message):
    __slots__ = ('epoch_count', 'learning_rate_multiplier', 'tuning_task')

    class TuningTask(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TUNING_TASK_UNSPECIFIED: _ClassVar[VeoHyperParameters.TuningTask]
        TUNING_TASK_I2V: _ClassVar[VeoHyperParameters.TuningTask]
        TUNING_TASK_T2V: _ClassVar[VeoHyperParameters.TuningTask]
    TUNING_TASK_UNSPECIFIED: VeoHyperParameters.TuningTask
    TUNING_TASK_I2V: VeoHyperParameters.TuningTask
    TUNING_TASK_T2V: VeoHyperParameters.TuningTask
    EPOCH_COUNT_FIELD_NUMBER: _ClassVar[int]
    LEARNING_RATE_MULTIPLIER_FIELD_NUMBER: _ClassVar[int]
    TUNING_TASK_FIELD_NUMBER: _ClassVar[int]
    epoch_count: int
    learning_rate_multiplier: float
    tuning_task: VeoHyperParameters.TuningTask

    def __init__(self, epoch_count: _Optional[int]=..., learning_rate_multiplier: _Optional[float]=..., tuning_task: _Optional[_Union[VeoHyperParameters.TuningTask, str]]=...) -> None:
        ...

class VeoTuningSpec(_message.Message):
    __slots__ = ('training_dataset_uri', 'validation_dataset_uri', 'hyper_parameters')
    TRAINING_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_DATASET_URI_FIELD_NUMBER: _ClassVar[int]
    HYPER_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    training_dataset_uri: str
    validation_dataset_uri: str
    hyper_parameters: VeoHyperParameters

    def __init__(self, training_dataset_uri: _Optional[str]=..., validation_dataset_uri: _Optional[str]=..., hyper_parameters: _Optional[_Union[VeoHyperParameters, _Mapping]]=...) -> None:
        ...

class EvaluationConfig(_message.Message):
    __slots__ = ('metrics', 'output_config', 'autorater_config')
    METRICS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTORATER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metrics: _containers.RepeatedCompositeFieldContainer[_evaluation_service_pb2.Metric]
    output_config: _evaluation_service_pb2.OutputConfig
    autorater_config: _evaluation_service_pb2.AutoraterConfig

    def __init__(self, metrics: _Optional[_Iterable[_Union[_evaluation_service_pb2.Metric, _Mapping]]]=..., output_config: _Optional[_Union[_evaluation_service_pb2.OutputConfig, _Mapping]]=..., autorater_config: _Optional[_Union[_evaluation_service_pb2.AutoraterConfig, _Mapping]]=...) -> None:
        ...

class EvaluateDatasetRun(_message.Message):
    __slots__ = ('operation_name', 'checkpoint_id', 'evaluate_dataset_response', 'error')
    OPERATION_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    EVALUATE_DATASET_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    operation_name: str
    checkpoint_id: str
    evaluate_dataset_response: _evaluation_service_pb2.EvaluateDatasetResponse
    error: _status_pb2.Status

    def __init__(self, operation_name: _Optional[str]=..., checkpoint_id: _Optional[str]=..., evaluate_dataset_response: _Optional[_Union[_evaluation_service_pb2.EvaluateDatasetResponse, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
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

class PreTunedModel(_message.Message):
    __slots__ = ('tuned_model_name', 'checkpoint_id', 'base_model')
    TUNED_MODEL_NAME_FIELD_NUMBER: _ClassVar[int]
    CHECKPOINT_ID_FIELD_NUMBER: _ClassVar[int]
    BASE_MODEL_FIELD_NUMBER: _ClassVar[int]
    tuned_model_name: str
    checkpoint_id: str
    base_model: str

    def __init__(self, tuned_model_name: _Optional[str]=..., checkpoint_id: _Optional[str]=..., base_model: _Optional[str]=...) -> None:
        ...