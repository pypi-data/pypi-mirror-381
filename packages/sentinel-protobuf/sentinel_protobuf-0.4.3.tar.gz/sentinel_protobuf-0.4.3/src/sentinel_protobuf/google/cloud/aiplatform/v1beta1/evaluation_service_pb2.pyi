from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import io_pb2 as _io_pb2
from google.cloud.aiplatform.v1beta1 import operation_pb2 as _operation_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PairwiseChoice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PAIRWISE_CHOICE_UNSPECIFIED: _ClassVar[PairwiseChoice]
    BASELINE: _ClassVar[PairwiseChoice]
    CANDIDATE: _ClassVar[PairwiseChoice]
    TIE: _ClassVar[PairwiseChoice]
PAIRWISE_CHOICE_UNSPECIFIED: PairwiseChoice
BASELINE: PairwiseChoice
CANDIDATE: PairwiseChoice
TIE: PairwiseChoice

class EvaluateDatasetOperationMetadata(_message.Message):
    __slots__ = ('generic_metadata',)
    GENERIC_METADATA_FIELD_NUMBER: _ClassVar[int]
    generic_metadata: _operation_pb2.GenericOperationMetadata

    def __init__(self, generic_metadata: _Optional[_Union[_operation_pb2.GenericOperationMetadata, _Mapping]]=...) -> None:
        ...

class EvaluateDatasetResponse(_message.Message):
    __slots__ = ('aggregation_output', 'output_info')
    AGGREGATION_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_INFO_FIELD_NUMBER: _ClassVar[int]
    aggregation_output: AggregationOutput
    output_info: OutputInfo

    def __init__(self, aggregation_output: _Optional[_Union[AggregationOutput, _Mapping]]=..., output_info: _Optional[_Union[OutputInfo, _Mapping]]=...) -> None:
        ...

class OutputInfo(_message.Message):
    __slots__ = ('gcs_output_directory',)
    GCS_OUTPUT_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    gcs_output_directory: str

    def __init__(self, gcs_output_directory: _Optional[str]=...) -> None:
        ...

class AggregationOutput(_message.Message):
    __slots__ = ('dataset', 'aggregation_results')
    DATASET_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    dataset: EvaluationDataset
    aggregation_results: _containers.RepeatedCompositeFieldContainer[AggregationResult]

    def __init__(self, dataset: _Optional[_Union[EvaluationDataset, _Mapping]]=..., aggregation_results: _Optional[_Iterable[_Union[AggregationResult, _Mapping]]]=...) -> None:
        ...

class AggregationResult(_message.Message):
    __slots__ = ('pointwise_metric_result', 'pairwise_metric_result', 'exact_match_metric_value', 'bleu_metric_value', 'rouge_metric_value', 'aggregation_metric')
    POINTWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    BLEU_METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    ROUGE_METRIC_VALUE_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METRIC_FIELD_NUMBER: _ClassVar[int]
    pointwise_metric_result: PointwiseMetricResult
    pairwise_metric_result: PairwiseMetricResult
    exact_match_metric_value: ExactMatchMetricValue
    bleu_metric_value: BleuMetricValue
    rouge_metric_value: RougeMetricValue
    aggregation_metric: Metric.AggregationMetric

    def __init__(self, pointwise_metric_result: _Optional[_Union[PointwiseMetricResult, _Mapping]]=..., pairwise_metric_result: _Optional[_Union[PairwiseMetricResult, _Mapping]]=..., exact_match_metric_value: _Optional[_Union[ExactMatchMetricValue, _Mapping]]=..., bleu_metric_value: _Optional[_Union[BleuMetricValue, _Mapping]]=..., rouge_metric_value: _Optional[_Union[RougeMetricValue, _Mapping]]=..., aggregation_metric: _Optional[_Union[Metric.AggregationMetric, str]]=...) -> None:
        ...

class EvaluateDatasetRequest(_message.Message):
    __slots__ = ('location', 'dataset', 'metrics', 'output_config', 'autorater_config')
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    DATASET_FIELD_NUMBER: _ClassVar[int]
    METRICS_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    AUTORATER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    location: str
    dataset: EvaluationDataset
    metrics: _containers.RepeatedCompositeFieldContainer[Metric]
    output_config: OutputConfig
    autorater_config: AutoraterConfig

    def __init__(self, location: _Optional[str]=..., dataset: _Optional[_Union[EvaluationDataset, _Mapping]]=..., metrics: _Optional[_Iterable[_Union[Metric, _Mapping]]]=..., output_config: _Optional[_Union[OutputConfig, _Mapping]]=..., autorater_config: _Optional[_Union[AutoraterConfig, _Mapping]]=...) -> None:
        ...

class OutputConfig(_message.Message):
    __slots__ = ('gcs_destination',)
    GCS_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    gcs_destination: _io_pb2.GcsDestination

    def __init__(self, gcs_destination: _Optional[_Union[_io_pb2.GcsDestination, _Mapping]]=...) -> None:
        ...

class Metric(_message.Message):
    __slots__ = ('pointwise_metric_spec', 'pairwise_metric_spec', 'exact_match_spec', 'bleu_spec', 'rouge_spec', 'aggregation_metrics')

    class AggregationMetric(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AGGREGATION_METRIC_UNSPECIFIED: _ClassVar[Metric.AggregationMetric]
        AVERAGE: _ClassVar[Metric.AggregationMetric]
        MODE: _ClassVar[Metric.AggregationMetric]
        STANDARD_DEVIATION: _ClassVar[Metric.AggregationMetric]
        VARIANCE: _ClassVar[Metric.AggregationMetric]
        MINIMUM: _ClassVar[Metric.AggregationMetric]
        MAXIMUM: _ClassVar[Metric.AggregationMetric]
        MEDIAN: _ClassVar[Metric.AggregationMetric]
        PERCENTILE_P90: _ClassVar[Metric.AggregationMetric]
        PERCENTILE_P95: _ClassVar[Metric.AggregationMetric]
        PERCENTILE_P99: _ClassVar[Metric.AggregationMetric]
    AGGREGATION_METRIC_UNSPECIFIED: Metric.AggregationMetric
    AVERAGE: Metric.AggregationMetric
    MODE: Metric.AggregationMetric
    STANDARD_DEVIATION: Metric.AggregationMetric
    VARIANCE: Metric.AggregationMetric
    MINIMUM: Metric.AggregationMetric
    MAXIMUM: Metric.AggregationMetric
    MEDIAN: Metric.AggregationMetric
    PERCENTILE_P90: Metric.AggregationMetric
    PERCENTILE_P95: Metric.AggregationMetric
    PERCENTILE_P99: Metric.AggregationMetric
    POINTWISE_METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    EXACT_MATCH_SPEC_FIELD_NUMBER: _ClassVar[int]
    BLEU_SPEC_FIELD_NUMBER: _ClassVar[int]
    ROUGE_SPEC_FIELD_NUMBER: _ClassVar[int]
    AGGREGATION_METRICS_FIELD_NUMBER: _ClassVar[int]
    pointwise_metric_spec: PointwiseMetricSpec
    pairwise_metric_spec: PairwiseMetricSpec
    exact_match_spec: ExactMatchSpec
    bleu_spec: BleuSpec
    rouge_spec: RougeSpec
    aggregation_metrics: _containers.RepeatedScalarFieldContainer[Metric.AggregationMetric]

    def __init__(self, pointwise_metric_spec: _Optional[_Union[PointwiseMetricSpec, _Mapping]]=..., pairwise_metric_spec: _Optional[_Union[PairwiseMetricSpec, _Mapping]]=..., exact_match_spec: _Optional[_Union[ExactMatchSpec, _Mapping]]=..., bleu_spec: _Optional[_Union[BleuSpec, _Mapping]]=..., rouge_spec: _Optional[_Union[RougeSpec, _Mapping]]=..., aggregation_metrics: _Optional[_Iterable[_Union[Metric.AggregationMetric, str]]]=...) -> None:
        ...

class EvaluationDataset(_message.Message):
    __slots__ = ('gcs_source', 'bigquery_source')
    GCS_SOURCE_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_SOURCE_FIELD_NUMBER: _ClassVar[int]
    gcs_source: _io_pb2.GcsSource
    bigquery_source: _io_pb2.BigQuerySource

    def __init__(self, gcs_source: _Optional[_Union[_io_pb2.GcsSource, _Mapping]]=..., bigquery_source: _Optional[_Union[_io_pb2.BigQuerySource, _Mapping]]=...) -> None:
        ...

class AutoraterConfig(_message.Message):
    __slots__ = ('sampling_count', 'flip_enabled', 'autorater_model')
    SAMPLING_COUNT_FIELD_NUMBER: _ClassVar[int]
    FLIP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    AUTORATER_MODEL_FIELD_NUMBER: _ClassVar[int]
    sampling_count: int
    flip_enabled: bool
    autorater_model: str

    def __init__(self, sampling_count: _Optional[int]=..., flip_enabled: bool=..., autorater_model: _Optional[str]=...) -> None:
        ...

class EvaluateInstancesRequest(_message.Message):
    __slots__ = ('exact_match_input', 'bleu_input', 'rouge_input', 'fluency_input', 'coherence_input', 'safety_input', 'groundedness_input', 'fulfillment_input', 'summarization_quality_input', 'pairwise_summarization_quality_input', 'summarization_helpfulness_input', 'summarization_verbosity_input', 'question_answering_quality_input', 'pairwise_question_answering_quality_input', 'question_answering_relevance_input', 'question_answering_helpfulness_input', 'question_answering_correctness_input', 'pointwise_metric_input', 'pairwise_metric_input', 'tool_call_valid_input', 'tool_name_match_input', 'tool_parameter_key_match_input', 'tool_parameter_kv_match_input', 'comet_input', 'metricx_input', 'trajectory_exact_match_input', 'trajectory_in_order_match_input', 'trajectory_any_order_match_input', 'trajectory_precision_input', 'trajectory_recall_input', 'trajectory_single_tool_use_input', 'rubric_based_instruction_following_input', 'location', 'autorater_config')
    EXACT_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    BLEU_INPUT_FIELD_NUMBER: _ClassVar[int]
    ROUGE_INPUT_FIELD_NUMBER: _ClassVar[int]
    FLUENCY_INPUT_FIELD_NUMBER: _ClassVar[int]
    COHERENCE_INPUT_FIELD_NUMBER: _ClassVar[int]
    SAFETY_INPUT_FIELD_NUMBER: _ClassVar[int]
    GROUNDEDNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_SUMMARIZATION_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_HELPFULNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_VERBOSITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_QUESTION_ANSWERING_QUALITY_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_RELEVANCE_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_HELPFULNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_CORRECTNESS_INPUT_FIELD_NUMBER: _ClassVar[int]
    POINTWISE_METRIC_INPUT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_VALID_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KEY_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KV_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    COMET_INPUT_FIELD_NUMBER: _ClassVar[int]
    METRICX_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_EXACT_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_IN_ORDER_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_ANY_ORDER_MATCH_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_PRECISION_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_RECALL_INPUT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_SINGLE_TOOL_USE_INPUT_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_BASED_INSTRUCTION_FOLLOWING_INPUT_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    AUTORATER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    exact_match_input: ExactMatchInput
    bleu_input: BleuInput
    rouge_input: RougeInput
    fluency_input: FluencyInput
    coherence_input: CoherenceInput
    safety_input: SafetyInput
    groundedness_input: GroundednessInput
    fulfillment_input: FulfillmentInput
    summarization_quality_input: SummarizationQualityInput
    pairwise_summarization_quality_input: PairwiseSummarizationQualityInput
    summarization_helpfulness_input: SummarizationHelpfulnessInput
    summarization_verbosity_input: SummarizationVerbosityInput
    question_answering_quality_input: QuestionAnsweringQualityInput
    pairwise_question_answering_quality_input: PairwiseQuestionAnsweringQualityInput
    question_answering_relevance_input: QuestionAnsweringRelevanceInput
    question_answering_helpfulness_input: QuestionAnsweringHelpfulnessInput
    question_answering_correctness_input: QuestionAnsweringCorrectnessInput
    pointwise_metric_input: PointwiseMetricInput
    pairwise_metric_input: PairwiseMetricInput
    tool_call_valid_input: ToolCallValidInput
    tool_name_match_input: ToolNameMatchInput
    tool_parameter_key_match_input: ToolParameterKeyMatchInput
    tool_parameter_kv_match_input: ToolParameterKVMatchInput
    comet_input: CometInput
    metricx_input: MetricxInput
    trajectory_exact_match_input: TrajectoryExactMatchInput
    trajectory_in_order_match_input: TrajectoryInOrderMatchInput
    trajectory_any_order_match_input: TrajectoryAnyOrderMatchInput
    trajectory_precision_input: TrajectoryPrecisionInput
    trajectory_recall_input: TrajectoryRecallInput
    trajectory_single_tool_use_input: TrajectorySingleToolUseInput
    rubric_based_instruction_following_input: RubricBasedInstructionFollowingInput
    location: str
    autorater_config: AutoraterConfig

    def __init__(self, exact_match_input: _Optional[_Union[ExactMatchInput, _Mapping]]=..., bleu_input: _Optional[_Union[BleuInput, _Mapping]]=..., rouge_input: _Optional[_Union[RougeInput, _Mapping]]=..., fluency_input: _Optional[_Union[FluencyInput, _Mapping]]=..., coherence_input: _Optional[_Union[CoherenceInput, _Mapping]]=..., safety_input: _Optional[_Union[SafetyInput, _Mapping]]=..., groundedness_input: _Optional[_Union[GroundednessInput, _Mapping]]=..., fulfillment_input: _Optional[_Union[FulfillmentInput, _Mapping]]=..., summarization_quality_input: _Optional[_Union[SummarizationQualityInput, _Mapping]]=..., pairwise_summarization_quality_input: _Optional[_Union[PairwiseSummarizationQualityInput, _Mapping]]=..., summarization_helpfulness_input: _Optional[_Union[SummarizationHelpfulnessInput, _Mapping]]=..., summarization_verbosity_input: _Optional[_Union[SummarizationVerbosityInput, _Mapping]]=..., question_answering_quality_input: _Optional[_Union[QuestionAnsweringQualityInput, _Mapping]]=..., pairwise_question_answering_quality_input: _Optional[_Union[PairwiseQuestionAnsweringQualityInput, _Mapping]]=..., question_answering_relevance_input: _Optional[_Union[QuestionAnsweringRelevanceInput, _Mapping]]=..., question_answering_helpfulness_input: _Optional[_Union[QuestionAnsweringHelpfulnessInput, _Mapping]]=..., question_answering_correctness_input: _Optional[_Union[QuestionAnsweringCorrectnessInput, _Mapping]]=..., pointwise_metric_input: _Optional[_Union[PointwiseMetricInput, _Mapping]]=..., pairwise_metric_input: _Optional[_Union[PairwiseMetricInput, _Mapping]]=..., tool_call_valid_input: _Optional[_Union[ToolCallValidInput, _Mapping]]=..., tool_name_match_input: _Optional[_Union[ToolNameMatchInput, _Mapping]]=..., tool_parameter_key_match_input: _Optional[_Union[ToolParameterKeyMatchInput, _Mapping]]=..., tool_parameter_kv_match_input: _Optional[_Union[ToolParameterKVMatchInput, _Mapping]]=..., comet_input: _Optional[_Union[CometInput, _Mapping]]=..., metricx_input: _Optional[_Union[MetricxInput, _Mapping]]=..., trajectory_exact_match_input: _Optional[_Union[TrajectoryExactMatchInput, _Mapping]]=..., trajectory_in_order_match_input: _Optional[_Union[TrajectoryInOrderMatchInput, _Mapping]]=..., trajectory_any_order_match_input: _Optional[_Union[TrajectoryAnyOrderMatchInput, _Mapping]]=..., trajectory_precision_input: _Optional[_Union[TrajectoryPrecisionInput, _Mapping]]=..., trajectory_recall_input: _Optional[_Union[TrajectoryRecallInput, _Mapping]]=..., trajectory_single_tool_use_input: _Optional[_Union[TrajectorySingleToolUseInput, _Mapping]]=..., rubric_based_instruction_following_input: _Optional[_Union[RubricBasedInstructionFollowingInput, _Mapping]]=..., location: _Optional[str]=..., autorater_config: _Optional[_Union[AutoraterConfig, _Mapping]]=...) -> None:
        ...

class EvaluateInstancesResponse(_message.Message):
    __slots__ = ('exact_match_results', 'bleu_results', 'rouge_results', 'fluency_result', 'coherence_result', 'safety_result', 'groundedness_result', 'fulfillment_result', 'summarization_quality_result', 'pairwise_summarization_quality_result', 'summarization_helpfulness_result', 'summarization_verbosity_result', 'question_answering_quality_result', 'pairwise_question_answering_quality_result', 'question_answering_relevance_result', 'question_answering_helpfulness_result', 'question_answering_correctness_result', 'pointwise_metric_result', 'pairwise_metric_result', 'tool_call_valid_results', 'tool_name_match_results', 'tool_parameter_key_match_results', 'tool_parameter_kv_match_results', 'comet_result', 'metricx_result', 'trajectory_exact_match_results', 'trajectory_in_order_match_results', 'trajectory_any_order_match_results', 'trajectory_precision_results', 'trajectory_recall_results', 'trajectory_single_tool_use_results', 'rubric_based_instruction_following_result')
    EXACT_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    BLEU_RESULTS_FIELD_NUMBER: _ClassVar[int]
    ROUGE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    FLUENCY_RESULT_FIELD_NUMBER: _ClassVar[int]
    COHERENCE_RESULT_FIELD_NUMBER: _ClassVar[int]
    SAFETY_RESULT_FIELD_NUMBER: _ClassVar[int]
    GROUNDEDNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    FULFILLMENT_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_SUMMARIZATION_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_HELPFULNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    SUMMARIZATION_VERBOSITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_QUESTION_ANSWERING_QUALITY_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_RELEVANCE_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_HELPFULNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    QUESTION_ANSWERING_CORRECTNESS_RESULT_FIELD_NUMBER: _ClassVar[int]
    POINTWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    PAIRWISE_METRIC_RESULT_FIELD_NUMBER: _ClassVar[int]
    TOOL_CALL_VALID_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_NAME_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KEY_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TOOL_PARAMETER_KV_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    COMET_RESULT_FIELD_NUMBER: _ClassVar[int]
    METRICX_RESULT_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_EXACT_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_IN_ORDER_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_ANY_ORDER_MATCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_PRECISION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_RECALL_RESULTS_FIELD_NUMBER: _ClassVar[int]
    TRAJECTORY_SINGLE_TOOL_USE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_BASED_INSTRUCTION_FOLLOWING_RESULT_FIELD_NUMBER: _ClassVar[int]
    exact_match_results: ExactMatchResults
    bleu_results: BleuResults
    rouge_results: RougeResults
    fluency_result: FluencyResult
    coherence_result: CoherenceResult
    safety_result: SafetyResult
    groundedness_result: GroundednessResult
    fulfillment_result: FulfillmentResult
    summarization_quality_result: SummarizationQualityResult
    pairwise_summarization_quality_result: PairwiseSummarizationQualityResult
    summarization_helpfulness_result: SummarizationHelpfulnessResult
    summarization_verbosity_result: SummarizationVerbosityResult
    question_answering_quality_result: QuestionAnsweringQualityResult
    pairwise_question_answering_quality_result: PairwiseQuestionAnsweringQualityResult
    question_answering_relevance_result: QuestionAnsweringRelevanceResult
    question_answering_helpfulness_result: QuestionAnsweringHelpfulnessResult
    question_answering_correctness_result: QuestionAnsweringCorrectnessResult
    pointwise_metric_result: PointwiseMetricResult
    pairwise_metric_result: PairwiseMetricResult
    tool_call_valid_results: ToolCallValidResults
    tool_name_match_results: ToolNameMatchResults
    tool_parameter_key_match_results: ToolParameterKeyMatchResults
    tool_parameter_kv_match_results: ToolParameterKVMatchResults
    comet_result: CometResult
    metricx_result: MetricxResult
    trajectory_exact_match_results: TrajectoryExactMatchResults
    trajectory_in_order_match_results: TrajectoryInOrderMatchResults
    trajectory_any_order_match_results: TrajectoryAnyOrderMatchResults
    trajectory_precision_results: TrajectoryPrecisionResults
    trajectory_recall_results: TrajectoryRecallResults
    trajectory_single_tool_use_results: TrajectorySingleToolUseResults
    rubric_based_instruction_following_result: RubricBasedInstructionFollowingResult

    def __init__(self, exact_match_results: _Optional[_Union[ExactMatchResults, _Mapping]]=..., bleu_results: _Optional[_Union[BleuResults, _Mapping]]=..., rouge_results: _Optional[_Union[RougeResults, _Mapping]]=..., fluency_result: _Optional[_Union[FluencyResult, _Mapping]]=..., coherence_result: _Optional[_Union[CoherenceResult, _Mapping]]=..., safety_result: _Optional[_Union[SafetyResult, _Mapping]]=..., groundedness_result: _Optional[_Union[GroundednessResult, _Mapping]]=..., fulfillment_result: _Optional[_Union[FulfillmentResult, _Mapping]]=..., summarization_quality_result: _Optional[_Union[SummarizationQualityResult, _Mapping]]=..., pairwise_summarization_quality_result: _Optional[_Union[PairwiseSummarizationQualityResult, _Mapping]]=..., summarization_helpfulness_result: _Optional[_Union[SummarizationHelpfulnessResult, _Mapping]]=..., summarization_verbosity_result: _Optional[_Union[SummarizationVerbosityResult, _Mapping]]=..., question_answering_quality_result: _Optional[_Union[QuestionAnsweringQualityResult, _Mapping]]=..., pairwise_question_answering_quality_result: _Optional[_Union[PairwiseQuestionAnsweringQualityResult, _Mapping]]=..., question_answering_relevance_result: _Optional[_Union[QuestionAnsweringRelevanceResult, _Mapping]]=..., question_answering_helpfulness_result: _Optional[_Union[QuestionAnsweringHelpfulnessResult, _Mapping]]=..., question_answering_correctness_result: _Optional[_Union[QuestionAnsweringCorrectnessResult, _Mapping]]=..., pointwise_metric_result: _Optional[_Union[PointwiseMetricResult, _Mapping]]=..., pairwise_metric_result: _Optional[_Union[PairwiseMetricResult, _Mapping]]=..., tool_call_valid_results: _Optional[_Union[ToolCallValidResults, _Mapping]]=..., tool_name_match_results: _Optional[_Union[ToolNameMatchResults, _Mapping]]=..., tool_parameter_key_match_results: _Optional[_Union[ToolParameterKeyMatchResults, _Mapping]]=..., tool_parameter_kv_match_results: _Optional[_Union[ToolParameterKVMatchResults, _Mapping]]=..., comet_result: _Optional[_Union[CometResult, _Mapping]]=..., metricx_result: _Optional[_Union[MetricxResult, _Mapping]]=..., trajectory_exact_match_results: _Optional[_Union[TrajectoryExactMatchResults, _Mapping]]=..., trajectory_in_order_match_results: _Optional[_Union[TrajectoryInOrderMatchResults, _Mapping]]=..., trajectory_any_order_match_results: _Optional[_Union[TrajectoryAnyOrderMatchResults, _Mapping]]=..., trajectory_precision_results: _Optional[_Union[TrajectoryPrecisionResults, _Mapping]]=..., trajectory_recall_results: _Optional[_Union[TrajectoryRecallResults, _Mapping]]=..., trajectory_single_tool_use_results: _Optional[_Union[TrajectorySingleToolUseResults, _Mapping]]=..., rubric_based_instruction_following_result: _Optional[_Union[RubricBasedInstructionFollowingResult, _Mapping]]=...) -> None:
        ...

class ExactMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ExactMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ExactMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[ExactMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[ExactMatchInstance, _Mapping]]]=...) -> None:
        ...

class ExactMatchInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class ExactMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ExactMatchResults(_message.Message):
    __slots__ = ('exact_match_metric_values',)
    EXACT_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    exact_match_metric_values: _containers.RepeatedCompositeFieldContainer[ExactMatchMetricValue]

    def __init__(self, exact_match_metric_values: _Optional[_Iterable[_Union[ExactMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class ExactMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class BleuInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: BleuSpec
    instances: _containers.RepeatedCompositeFieldContainer[BleuInstance]

    def __init__(self, metric_spec: _Optional[_Union[BleuSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[BleuInstance, _Mapping]]]=...) -> None:
        ...

class BleuInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class BleuSpec(_message.Message):
    __slots__ = ('use_effective_order',)
    USE_EFFECTIVE_ORDER_FIELD_NUMBER: _ClassVar[int]
    use_effective_order: bool

    def __init__(self, use_effective_order: bool=...) -> None:
        ...

class BleuResults(_message.Message):
    __slots__ = ('bleu_metric_values',)
    BLEU_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    bleu_metric_values: _containers.RepeatedCompositeFieldContainer[BleuMetricValue]

    def __init__(self, bleu_metric_values: _Optional[_Iterable[_Union[BleuMetricValue, _Mapping]]]=...) -> None:
        ...

class BleuMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class RougeInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: RougeSpec
    instances: _containers.RepeatedCompositeFieldContainer[RougeInstance]

    def __init__(self, metric_spec: _Optional[_Union[RougeSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[RougeInstance, _Mapping]]]=...) -> None:
        ...

class RougeInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class RougeSpec(_message.Message):
    __slots__ = ('rouge_type', 'use_stemmer', 'split_summaries')
    ROUGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    USE_STEMMER_FIELD_NUMBER: _ClassVar[int]
    SPLIT_SUMMARIES_FIELD_NUMBER: _ClassVar[int]
    rouge_type: str
    use_stemmer: bool
    split_summaries: bool

    def __init__(self, rouge_type: _Optional[str]=..., use_stemmer: bool=..., split_summaries: bool=...) -> None:
        ...

class RougeResults(_message.Message):
    __slots__ = ('rouge_metric_values',)
    ROUGE_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    rouge_metric_values: _containers.RepeatedCompositeFieldContainer[RougeMetricValue]

    def __init__(self, rouge_metric_values: _Optional[_Iterable[_Union[RougeMetricValue, _Mapping]]]=...) -> None:
        ...

class RougeMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class CoherenceInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: CoherenceSpec
    instance: CoherenceInstance

    def __init__(self, metric_spec: _Optional[_Union[CoherenceSpec, _Mapping]]=..., instance: _Optional[_Union[CoherenceInstance, _Mapping]]=...) -> None:
        ...

class CoherenceInstance(_message.Message):
    __slots__ = ('prediction',)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str

    def __init__(self, prediction: _Optional[str]=...) -> None:
        ...

class CoherenceSpec(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int

    def __init__(self, version: _Optional[int]=...) -> None:
        ...

class CoherenceResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class FluencyInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: FluencySpec
    instance: FluencyInstance

    def __init__(self, metric_spec: _Optional[_Union[FluencySpec, _Mapping]]=..., instance: _Optional[_Union[FluencyInstance, _Mapping]]=...) -> None:
        ...

class FluencyInstance(_message.Message):
    __slots__ = ('prediction',)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str

    def __init__(self, prediction: _Optional[str]=...) -> None:
        ...

class FluencySpec(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int

    def __init__(self, version: _Optional[int]=...) -> None:
        ...

class FluencyResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class SafetyInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SafetySpec
    instance: SafetyInstance

    def __init__(self, metric_spec: _Optional[_Union[SafetySpec, _Mapping]]=..., instance: _Optional[_Union[SafetyInstance, _Mapping]]=...) -> None:
        ...

class SafetyInstance(_message.Message):
    __slots__ = ('prediction',)
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str

    def __init__(self, prediction: _Optional[str]=...) -> None:
        ...

class SafetySpec(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int

    def __init__(self, version: _Optional[int]=...) -> None:
        ...

class SafetyResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class GroundednessInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: GroundednessSpec
    instance: GroundednessInstance

    def __init__(self, metric_spec: _Optional[_Union[GroundednessSpec, _Mapping]]=..., instance: _Optional[_Union[GroundednessInstance, _Mapping]]=...) -> None:
        ...

class GroundednessInstance(_message.Message):
    __slots__ = ('prediction', 'context')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    context: str

    def __init__(self, prediction: _Optional[str]=..., context: _Optional[str]=...) -> None:
        ...

class GroundednessSpec(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int

    def __init__(self, version: _Optional[int]=...) -> None:
        ...

class GroundednessResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class FulfillmentInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: FulfillmentSpec
    instance: FulfillmentInstance

    def __init__(self, metric_spec: _Optional[_Union[FulfillmentSpec, _Mapping]]=..., instance: _Optional[_Union[FulfillmentInstance, _Mapping]]=...) -> None:
        ...

class FulfillmentInstance(_message.Message):
    __slots__ = ('prediction', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class FulfillmentSpec(_message.Message):
    __slots__ = ('version',)
    VERSION_FIELD_NUMBER: _ClassVar[int]
    version: int

    def __init__(self, version: _Optional[int]=...) -> None:
        ...

class FulfillmentResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class SummarizationQualityInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationQualitySpec
    instance: SummarizationQualityInstance

    def __init__(self, metric_spec: _Optional[_Union[SummarizationQualitySpec, _Mapping]]=..., instance: _Optional[_Union[SummarizationQualityInstance, _Mapping]]=...) -> None:
        ...

class SummarizationQualityInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class SummarizationQualitySpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class SummarizationQualityResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class PairwiseSummarizationQualityInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseSummarizationQualitySpec
    instance: PairwiseSummarizationQualityInstance

    def __init__(self, metric_spec: _Optional[_Union[PairwiseSummarizationQualitySpec, _Mapping]]=..., instance: _Optional[_Union[PairwiseSummarizationQualityInstance, _Mapping]]=...) -> None:
        ...

class PairwiseSummarizationQualityInstance(_message.Message):
    __slots__ = ('prediction', 'baseline_prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    BASELINE_PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    baseline_prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., baseline_prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class PairwiseSummarizationQualitySpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class PairwiseSummarizationQualityResult(_message.Message):
    __slots__ = ('pairwise_choice', 'explanation', 'confidence')
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    confidence: float

    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class SummarizationHelpfulnessInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationHelpfulnessSpec
    instance: SummarizationHelpfulnessInstance

    def __init__(self, metric_spec: _Optional[_Union[SummarizationHelpfulnessSpec, _Mapping]]=..., instance: _Optional[_Union[SummarizationHelpfulnessInstance, _Mapping]]=...) -> None:
        ...

class SummarizationHelpfulnessInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class SummarizationHelpfulnessSpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class SummarizationHelpfulnessResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class SummarizationVerbosityInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: SummarizationVerbositySpec
    instance: SummarizationVerbosityInstance

    def __init__(self, metric_spec: _Optional[_Union[SummarizationVerbositySpec, _Mapping]]=..., instance: _Optional[_Union[SummarizationVerbosityInstance, _Mapping]]=...) -> None:
        ...

class SummarizationVerbosityInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class SummarizationVerbositySpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class SummarizationVerbosityResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class QuestionAnsweringQualityInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringQualitySpec
    instance: QuestionAnsweringQualityInstance

    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringQualitySpec, _Mapping]]=..., instance: _Optional[_Union[QuestionAnsweringQualityInstance, _Mapping]]=...) -> None:
        ...

class QuestionAnsweringQualityInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class QuestionAnsweringQualitySpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class QuestionAnsweringQualityResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class PairwiseQuestionAnsweringQualityInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseQuestionAnsweringQualitySpec
    instance: PairwiseQuestionAnsweringQualityInstance

    def __init__(self, metric_spec: _Optional[_Union[PairwiseQuestionAnsweringQualitySpec, _Mapping]]=..., instance: _Optional[_Union[PairwiseQuestionAnsweringQualityInstance, _Mapping]]=...) -> None:
        ...

class PairwiseQuestionAnsweringQualityInstance(_message.Message):
    __slots__ = ('prediction', 'baseline_prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    BASELINE_PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    baseline_prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., baseline_prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class PairwiseQuestionAnsweringQualitySpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class PairwiseQuestionAnsweringQualityResult(_message.Message):
    __slots__ = ('pairwise_choice', 'explanation', 'confidence')
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    confidence: float

    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class QuestionAnsweringRelevanceInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringRelevanceSpec
    instance: QuestionAnsweringRelevanceInstance

    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringRelevanceSpec, _Mapping]]=..., instance: _Optional[_Union[QuestionAnsweringRelevanceInstance, _Mapping]]=...) -> None:
        ...

class QuestionAnsweringRelevanceInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class QuestionAnsweringRelevanceSpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class QuestionAnsweringRelevanceResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class QuestionAnsweringHelpfulnessInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringHelpfulnessSpec
    instance: QuestionAnsweringHelpfulnessInstance

    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringHelpfulnessSpec, _Mapping]]=..., instance: _Optional[_Union[QuestionAnsweringHelpfulnessInstance, _Mapping]]=...) -> None:
        ...

class QuestionAnsweringHelpfulnessInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class QuestionAnsweringHelpfulnessSpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class QuestionAnsweringHelpfulnessResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class QuestionAnsweringCorrectnessInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: QuestionAnsweringCorrectnessSpec
    instance: QuestionAnsweringCorrectnessInstance

    def __init__(self, metric_spec: _Optional[_Union[QuestionAnsweringCorrectnessSpec, _Mapping]]=..., instance: _Optional[_Union[QuestionAnsweringCorrectnessInstance, _Mapping]]=...) -> None:
        ...

class QuestionAnsweringCorrectnessInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'context', 'instruction')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    CONTEXT_FIELD_NUMBER: _ClassVar[int]
    INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    context: str
    instruction: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., context: _Optional[str]=..., instruction: _Optional[str]=...) -> None:
        ...

class QuestionAnsweringCorrectnessSpec(_message.Message):
    __slots__ = ('use_reference', 'version')
    USE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    use_reference: bool
    version: int

    def __init__(self, use_reference: bool=..., version: _Optional[int]=...) -> None:
        ...

class QuestionAnsweringCorrectnessResult(_message.Message):
    __slots__ = ('score', 'explanation', 'confidence')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    confidence: float

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., confidence: _Optional[float]=...) -> None:
        ...

class PointwiseMetricInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PointwiseMetricSpec
    instance: PointwiseMetricInstance

    def __init__(self, metric_spec: _Optional[_Union[PointwiseMetricSpec, _Mapping]]=..., instance: _Optional[_Union[PointwiseMetricInstance, _Mapping]]=...) -> None:
        ...

class PointwiseMetricInstance(_message.Message):
    __slots__ = ('json_instance', 'content_map_instance')
    JSON_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MAP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    json_instance: str
    content_map_instance: ContentMap

    def __init__(self, json_instance: _Optional[str]=..., content_map_instance: _Optional[_Union[ContentMap, _Mapping]]=...) -> None:
        ...

class PointwiseMetricSpec(_message.Message):
    __slots__ = ('metric_prompt_template', 'system_instruction', 'custom_output_format_config')
    METRIC_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FORMAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metric_prompt_template: str
    system_instruction: str
    custom_output_format_config: CustomOutputFormatConfig

    def __init__(self, metric_prompt_template: _Optional[str]=..., system_instruction: _Optional[str]=..., custom_output_format_config: _Optional[_Union[CustomOutputFormatConfig, _Mapping]]=...) -> None:
        ...

class CustomOutputFormatConfig(_message.Message):
    __slots__ = ('return_raw_output',)
    RETURN_RAW_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    return_raw_output: bool

    def __init__(self, return_raw_output: bool=...) -> None:
        ...

class PointwiseMetricResult(_message.Message):
    __slots__ = ('score', 'explanation', 'custom_output')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    score: float
    explanation: str
    custom_output: CustomOutput

    def __init__(self, score: _Optional[float]=..., explanation: _Optional[str]=..., custom_output: _Optional[_Union[CustomOutput, _Mapping]]=...) -> None:
        ...

class CustomOutput(_message.Message):
    __slots__ = ('raw_outputs',)
    RAW_OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    raw_outputs: RawOutput

    def __init__(self, raw_outputs: _Optional[_Union[RawOutput, _Mapping]]=...) -> None:
        ...

class RawOutput(_message.Message):
    __slots__ = ('raw_output',)
    RAW_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    raw_output: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, raw_output: _Optional[_Iterable[str]]=...) -> None:
        ...

class PairwiseMetricInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: PairwiseMetricSpec
    instance: PairwiseMetricInstance

    def __init__(self, metric_spec: _Optional[_Union[PairwiseMetricSpec, _Mapping]]=..., instance: _Optional[_Union[PairwiseMetricInstance, _Mapping]]=...) -> None:
        ...

class PairwiseMetricInstance(_message.Message):
    __slots__ = ('json_instance', 'content_map_instance')
    JSON_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_MAP_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    json_instance: str
    content_map_instance: ContentMap

    def __init__(self, json_instance: _Optional[str]=..., content_map_instance: _Optional[_Union[ContentMap, _Mapping]]=...) -> None:
        ...

class PairwiseMetricSpec(_message.Message):
    __slots__ = ('metric_prompt_template', 'candidate_response_field_name', 'baseline_response_field_name', 'system_instruction', 'custom_output_format_config')
    METRIC_PROMPT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CANDIDATE_RESPONSE_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    BASELINE_RESPONSE_FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FORMAT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    metric_prompt_template: str
    candidate_response_field_name: str
    baseline_response_field_name: str
    system_instruction: str
    custom_output_format_config: CustomOutputFormatConfig

    def __init__(self, metric_prompt_template: _Optional[str]=..., candidate_response_field_name: _Optional[str]=..., baseline_response_field_name: _Optional[str]=..., system_instruction: _Optional[str]=..., custom_output_format_config: _Optional[_Union[CustomOutputFormatConfig, _Mapping]]=...) -> None:
        ...

class PairwiseMetricResult(_message.Message):
    __slots__ = ('pairwise_choice', 'explanation', 'custom_output')
    PAIRWISE_CHOICE_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_OUTPUT_FIELD_NUMBER: _ClassVar[int]
    pairwise_choice: PairwiseChoice
    explanation: str
    custom_output: CustomOutput

    def __init__(self, pairwise_choice: _Optional[_Union[PairwiseChoice, str]]=..., explanation: _Optional[str]=..., custom_output: _Optional[_Union[CustomOutput, _Mapping]]=...) -> None:
        ...

class ToolCallValidInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolCallValidSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolCallValidInstance]

    def __init__(self, metric_spec: _Optional[_Union[ToolCallValidSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[ToolCallValidInstance, _Mapping]]]=...) -> None:
        ...

class ToolCallValidSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ToolCallValidInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class ToolCallValidResults(_message.Message):
    __slots__ = ('tool_call_valid_metric_values',)
    TOOL_CALL_VALID_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_call_valid_metric_values: _containers.RepeatedCompositeFieldContainer[ToolCallValidMetricValue]

    def __init__(self, tool_call_valid_metric_values: _Optional[_Iterable[_Union[ToolCallValidMetricValue, _Mapping]]]=...) -> None:
        ...

class ToolCallValidMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class ToolNameMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolNameMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolNameMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[ToolNameMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[ToolNameMatchInstance, _Mapping]]]=...) -> None:
        ...

class ToolNameMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ToolNameMatchInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class ToolNameMatchResults(_message.Message):
    __slots__ = ('tool_name_match_metric_values',)
    TOOL_NAME_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_name_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolNameMatchMetricValue]

    def __init__(self, tool_name_match_metric_values: _Optional[_Iterable[_Union[ToolNameMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class ToolNameMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class ToolParameterKeyMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolParameterKeyMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolParameterKeyMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[ToolParameterKeyMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[ToolParameterKeyMatchInstance, _Mapping]]]=...) -> None:
        ...

class ToolParameterKeyMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ToolParameterKeyMatchInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class ToolParameterKeyMatchResults(_message.Message):
    __slots__ = ('tool_parameter_key_match_metric_values',)
    TOOL_PARAMETER_KEY_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_parameter_key_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolParameterKeyMatchMetricValue]

    def __init__(self, tool_parameter_key_match_metric_values: _Optional[_Iterable[_Union[ToolParameterKeyMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class ToolParameterKeyMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class ToolParameterKVMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: ToolParameterKVMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[ToolParameterKVMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[ToolParameterKVMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[ToolParameterKVMatchInstance, _Mapping]]]=...) -> None:
        ...

class ToolParameterKVMatchSpec(_message.Message):
    __slots__ = ('use_strict_string_match',)
    USE_STRICT_STRING_MATCH_FIELD_NUMBER: _ClassVar[int]
    use_strict_string_match: bool

    def __init__(self, use_strict_string_match: bool=...) -> None:
        ...

class ToolParameterKVMatchInstance(_message.Message):
    __slots__ = ('prediction', 'reference')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=...) -> None:
        ...

class ToolParameterKVMatchResults(_message.Message):
    __slots__ = ('tool_parameter_kv_match_metric_values',)
    TOOL_PARAMETER_KV_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    tool_parameter_kv_match_metric_values: _containers.RepeatedCompositeFieldContainer[ToolParameterKVMatchMetricValue]

    def __init__(self, tool_parameter_kv_match_metric_values: _Optional[_Iterable[_Union[ToolParameterKVMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class ToolParameterKVMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class CometInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: CometSpec
    instance: CometInstance

    def __init__(self, metric_spec: _Optional[_Union[CometSpec, _Mapping]]=..., instance: _Optional[_Union[CometInstance, _Mapping]]=...) -> None:
        ...

class CometSpec(_message.Message):
    __slots__ = ('version', 'source_language', 'target_language')

    class CometVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COMET_VERSION_UNSPECIFIED: _ClassVar[CometSpec.CometVersion]
        COMET_22_SRC_REF: _ClassVar[CometSpec.CometVersion]
    COMET_VERSION_UNSPECIFIED: CometSpec.CometVersion
    COMET_22_SRC_REF: CometSpec.CometVersion
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    version: CometSpec.CometVersion
    source_language: str
    target_language: str

    def __init__(self, version: _Optional[_Union[CometSpec.CometVersion, str]]=..., source_language: _Optional[str]=..., target_language: _Optional[str]=...) -> None:
        ...

class CometInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'source')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    source: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., source: _Optional[str]=...) -> None:
        ...

class CometResult(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class MetricxInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: MetricxSpec
    instance: MetricxInstance

    def __init__(self, metric_spec: _Optional[_Union[MetricxSpec, _Mapping]]=..., instance: _Optional[_Union[MetricxInstance, _Mapping]]=...) -> None:
        ...

class MetricxSpec(_message.Message):
    __slots__ = ('version', 'source_language', 'target_language')

    class MetricxVersion(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        METRICX_VERSION_UNSPECIFIED: _ClassVar[MetricxSpec.MetricxVersion]
        METRICX_24_REF: _ClassVar[MetricxSpec.MetricxVersion]
        METRICX_24_SRC: _ClassVar[MetricxSpec.MetricxVersion]
        METRICX_24_SRC_REF: _ClassVar[MetricxSpec.MetricxVersion]
    METRICX_VERSION_UNSPECIFIED: MetricxSpec.MetricxVersion
    METRICX_24_REF: MetricxSpec.MetricxVersion
    METRICX_24_SRC: MetricxSpec.MetricxVersion
    METRICX_24_SRC_REF: MetricxSpec.MetricxVersion
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SOURCE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    version: MetricxSpec.MetricxVersion
    source_language: str
    target_language: str

    def __init__(self, version: _Optional[_Union[MetricxSpec.MetricxVersion, str]]=..., source_language: _Optional[str]=..., target_language: _Optional[str]=...) -> None:
        ...

class MetricxInstance(_message.Message):
    __slots__ = ('prediction', 'reference', 'source')
    PREDICTION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    prediction: str
    reference: str
    source: str

    def __init__(self, prediction: _Optional[str]=..., reference: _Optional[str]=..., source: _Optional[str]=...) -> None:
        ...

class MetricxResult(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class RubricBasedInstructionFollowingInput(_message.Message):
    __slots__ = ('metric_spec', 'instance')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    metric_spec: RubricBasedInstructionFollowingSpec
    instance: RubricBasedInstructionFollowingInstance

    def __init__(self, metric_spec: _Optional[_Union[RubricBasedInstructionFollowingSpec, _Mapping]]=..., instance: _Optional[_Union[RubricBasedInstructionFollowingInstance, _Mapping]]=...) -> None:
        ...

class RubricBasedInstructionFollowingInstance(_message.Message):
    __slots__ = ('json_instance',)
    JSON_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    json_instance: str

    def __init__(self, json_instance: _Optional[str]=...) -> None:
        ...

class RubricBasedInstructionFollowingSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RubricBasedInstructionFollowingResult(_message.Message):
    __slots__ = ('score', 'rubric_critique_results')
    SCORE_FIELD_NUMBER: _ClassVar[int]
    RUBRIC_CRITIQUE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    score: float
    rubric_critique_results: _containers.RepeatedCompositeFieldContainer[RubricCritiqueResult]

    def __init__(self, score: _Optional[float]=..., rubric_critique_results: _Optional[_Iterable[_Union[RubricCritiqueResult, _Mapping]]]=...) -> None:
        ...

class RubricCritiqueResult(_message.Message):
    __slots__ = ('rubric', 'verdict')
    RUBRIC_FIELD_NUMBER: _ClassVar[int]
    VERDICT_FIELD_NUMBER: _ClassVar[int]
    rubric: str
    verdict: bool

    def __init__(self, rubric: _Optional[str]=..., verdict: bool=...) -> None:
        ...

class TrajectoryExactMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryExactMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryExactMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectoryExactMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectoryExactMatchInstance, _Mapping]]]=...) -> None:
        ...

class TrajectoryExactMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TrajectoryExactMatchInstance(_message.Message):
    __slots__ = ('predicted_trajectory', 'reference_trajectory')
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectoryExactMatchResults(_message.Message):
    __slots__ = ('trajectory_exact_match_metric_values',)
    TRAJECTORY_EXACT_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_exact_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryExactMatchMetricValue]

    def __init__(self, trajectory_exact_match_metric_values: _Optional[_Iterable[_Union[TrajectoryExactMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectoryExactMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class TrajectoryInOrderMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryInOrderMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryInOrderMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectoryInOrderMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectoryInOrderMatchInstance, _Mapping]]]=...) -> None:
        ...

class TrajectoryInOrderMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TrajectoryInOrderMatchInstance(_message.Message):
    __slots__ = ('predicted_trajectory', 'reference_trajectory')
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectoryInOrderMatchResults(_message.Message):
    __slots__ = ('trajectory_in_order_match_metric_values',)
    TRAJECTORY_IN_ORDER_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_in_order_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryInOrderMatchMetricValue]

    def __init__(self, trajectory_in_order_match_metric_values: _Optional[_Iterable[_Union[TrajectoryInOrderMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectoryInOrderMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class TrajectoryAnyOrderMatchInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryAnyOrderMatchSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryAnyOrderMatchInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectoryAnyOrderMatchSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectoryAnyOrderMatchInstance, _Mapping]]]=...) -> None:
        ...

class TrajectoryAnyOrderMatchSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TrajectoryAnyOrderMatchInstance(_message.Message):
    __slots__ = ('predicted_trajectory', 'reference_trajectory')
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectoryAnyOrderMatchResults(_message.Message):
    __slots__ = ('trajectory_any_order_match_metric_values',)
    TRAJECTORY_ANY_ORDER_MATCH_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_any_order_match_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryAnyOrderMatchMetricValue]

    def __init__(self, trajectory_any_order_match_metric_values: _Optional[_Iterable[_Union[TrajectoryAnyOrderMatchMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectoryAnyOrderMatchMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class TrajectoryPrecisionInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryPrecisionSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryPrecisionInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectoryPrecisionSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectoryPrecisionInstance, _Mapping]]]=...) -> None:
        ...

class TrajectoryPrecisionSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TrajectoryPrecisionInstance(_message.Message):
    __slots__ = ('predicted_trajectory', 'reference_trajectory')
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectoryPrecisionResults(_message.Message):
    __slots__ = ('trajectory_precision_metric_values',)
    TRAJECTORY_PRECISION_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_precision_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryPrecisionMetricValue]

    def __init__(self, trajectory_precision_metric_values: _Optional[_Iterable[_Union[TrajectoryPrecisionMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectoryPrecisionMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class TrajectoryRecallInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectoryRecallSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectoryRecallInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectoryRecallSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectoryRecallInstance, _Mapping]]]=...) -> None:
        ...

class TrajectoryRecallSpec(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class TrajectoryRecallInstance(_message.Message):
    __slots__ = ('predicted_trajectory', 'reference_trajectory')
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory
    reference_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=..., reference_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectoryRecallResults(_message.Message):
    __slots__ = ('trajectory_recall_metric_values',)
    TRAJECTORY_RECALL_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_recall_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectoryRecallMetricValue]

    def __init__(self, trajectory_recall_metric_values: _Optional[_Iterable[_Union[TrajectoryRecallMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectoryRecallMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class TrajectorySingleToolUseInput(_message.Message):
    __slots__ = ('metric_spec', 'instances')
    METRIC_SPEC_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    metric_spec: TrajectorySingleToolUseSpec
    instances: _containers.RepeatedCompositeFieldContainer[TrajectorySingleToolUseInstance]

    def __init__(self, metric_spec: _Optional[_Union[TrajectorySingleToolUseSpec, _Mapping]]=..., instances: _Optional[_Iterable[_Union[TrajectorySingleToolUseInstance, _Mapping]]]=...) -> None:
        ...

class TrajectorySingleToolUseSpec(_message.Message):
    __slots__ = ('tool_name',)
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    tool_name: str

    def __init__(self, tool_name: _Optional[str]=...) -> None:
        ...

class TrajectorySingleToolUseInstance(_message.Message):
    __slots__ = ('predicted_trajectory',)
    PREDICTED_TRAJECTORY_FIELD_NUMBER: _ClassVar[int]
    predicted_trajectory: Trajectory

    def __init__(self, predicted_trajectory: _Optional[_Union[Trajectory, _Mapping]]=...) -> None:
        ...

class TrajectorySingleToolUseResults(_message.Message):
    __slots__ = ('trajectory_single_tool_use_metric_values',)
    TRAJECTORY_SINGLE_TOOL_USE_METRIC_VALUES_FIELD_NUMBER: _ClassVar[int]
    trajectory_single_tool_use_metric_values: _containers.RepeatedCompositeFieldContainer[TrajectorySingleToolUseMetricValue]

    def __init__(self, trajectory_single_tool_use_metric_values: _Optional[_Iterable[_Union[TrajectorySingleToolUseMetricValue, _Mapping]]]=...) -> None:
        ...

class TrajectorySingleToolUseMetricValue(_message.Message):
    __slots__ = ('score',)
    SCORE_FIELD_NUMBER: _ClassVar[int]
    score: float

    def __init__(self, score: _Optional[float]=...) -> None:
        ...

class Trajectory(_message.Message):
    __slots__ = ('tool_calls',)
    TOOL_CALLS_FIELD_NUMBER: _ClassVar[int]
    tool_calls: _containers.RepeatedCompositeFieldContainer[ToolCall]

    def __init__(self, tool_calls: _Optional[_Iterable[_Union[ToolCall, _Mapping]]]=...) -> None:
        ...

class ToolCall(_message.Message):
    __slots__ = ('tool_name', 'tool_input')
    TOOL_NAME_FIELD_NUMBER: _ClassVar[int]
    TOOL_INPUT_FIELD_NUMBER: _ClassVar[int]
    tool_name: str
    tool_input: str

    def __init__(self, tool_name: _Optional[str]=..., tool_input: _Optional[str]=...) -> None:
        ...

class ContentMap(_message.Message):
    __slots__ = ('values',)

    class Contents(_message.Message):
        __slots__ = ('contents',)
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]

        def __init__(self, contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=...) -> None:
            ...

    class ValuesEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ContentMap.Contents

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ContentMap.Contents, _Mapping]]=...) -> None:
            ...
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.MessageMap[str, ContentMap.Contents]

    def __init__(self, values: _Optional[_Mapping[str, ContentMap.Contents]]=...) -> None:
        ...