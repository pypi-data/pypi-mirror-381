from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.cloud.aiplatform.v1beta1 import explanation_pb2 as _explanation_pb2
from google.cloud.aiplatform.v1beta1 import tool_pb2 as _tool_pb2
from google.cloud.aiplatform.v1beta1 import types_pb2 as _types_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ('endpoint', 'instances', 'parameters')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    parameters: _struct_pb2.Value

    def __init__(self, endpoint: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class PredictResponse(_message.Message):
    __slots__ = ('predictions', 'deployed_model_id', 'model', 'model_version_id', 'model_display_name', 'metadata')
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    MODEL_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    deployed_model_id: str
    model: str
    model_version_id: str
    model_display_name: str
    metadata: _struct_pb2.Value

    def __init__(self, predictions: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., deployed_model_id: _Optional[str]=..., model: _Optional[str]=..., model_version_id: _Optional[str]=..., model_display_name: _Optional[str]=..., metadata: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class RawPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'http_body')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    http_body: _httpbody_pb2.HttpBody

    def __init__(self, endpoint: _Optional[str]=..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=...) -> None:
        ...

class StreamRawPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'http_body')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    http_body: _httpbody_pb2.HttpBody

    def __init__(self, endpoint: _Optional[str]=..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=...) -> None:
        ...

class DirectPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'inputs', 'parameters')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    inputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, endpoint: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class DirectPredictResponse(_message.Message):
    __slots__ = ('outputs', 'parameters')
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, outputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class DirectRawPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'method_name', 'input')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    method_name: str
    input: bytes

    def __init__(self, endpoint: _Optional[str]=..., method_name: _Optional[str]=..., input: _Optional[bytes]=...) -> None:
        ...

class DirectRawPredictResponse(_message.Message):
    __slots__ = ('output',)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: bytes

    def __init__(self, output: _Optional[bytes]=...) -> None:
        ...

class StreamDirectPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'inputs', 'parameters')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    inputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, endpoint: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class StreamDirectPredictResponse(_message.Message):
    __slots__ = ('outputs', 'parameters')
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, outputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class StreamDirectRawPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'method_name', 'input')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    method_name: str
    input: bytes

    def __init__(self, endpoint: _Optional[str]=..., method_name: _Optional[str]=..., input: _Optional[bytes]=...) -> None:
        ...

class StreamDirectRawPredictResponse(_message.Message):
    __slots__ = ('output',)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: bytes

    def __init__(self, output: _Optional[bytes]=...) -> None:
        ...

class StreamingPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'inputs', 'parameters')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    inputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, endpoint: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class StreamingPredictResponse(_message.Message):
    __slots__ = ('outputs', 'parameters')
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    outputs: _containers.RepeatedCompositeFieldContainer[_types_pb2.Tensor]
    parameters: _types_pb2.Tensor

    def __init__(self, outputs: _Optional[_Iterable[_Union[_types_pb2.Tensor, _Mapping]]]=..., parameters: _Optional[_Union[_types_pb2.Tensor, _Mapping]]=...) -> None:
        ...

class StreamingRawPredictRequest(_message.Message):
    __slots__ = ('endpoint', 'method_name', 'input')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    method_name: str
    input: bytes

    def __init__(self, endpoint: _Optional[str]=..., method_name: _Optional[str]=..., input: _Optional[bytes]=...) -> None:
        ...

class StreamingRawPredictResponse(_message.Message):
    __slots__ = ('output',)
    OUTPUT_FIELD_NUMBER: _ClassVar[int]
    output: bytes

    def __init__(self, output: _Optional[bytes]=...) -> None:
        ...

class ExplainRequest(_message.Message):
    __slots__ = ('endpoint', 'instances', 'parameters', 'explanation_spec_override', 'concurrent_explanation_spec_override', 'deployed_model_id')

    class ConcurrentExplanationSpecOverrideEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _explanation_pb2.ExplanationSpecOverride

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_explanation_pb2.ExplanationSpecOverride, _Mapping]]=...) -> None:
            ...
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    EXPLANATION_SPEC_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_EXPLANATION_SPEC_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    parameters: _struct_pb2.Value
    explanation_spec_override: _explanation_pb2.ExplanationSpecOverride
    concurrent_explanation_spec_override: _containers.MessageMap[str, _explanation_pb2.ExplanationSpecOverride]
    deployed_model_id: str

    def __init__(self, endpoint: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]]=..., explanation_spec_override: _Optional[_Union[_explanation_pb2.ExplanationSpecOverride, _Mapping]]=..., concurrent_explanation_spec_override: _Optional[_Mapping[str, _explanation_pb2.ExplanationSpecOverride]]=..., deployed_model_id: _Optional[str]=...) -> None:
        ...

class ExplainResponse(_message.Message):
    __slots__ = ('explanations', 'concurrent_explanations', 'deployed_model_id', 'predictions')

    class ConcurrentExplanation(_message.Message):
        __slots__ = ('explanations',)
        EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
        explanations: _containers.RepeatedCompositeFieldContainer[_explanation_pb2.Explanation]

        def __init__(self, explanations: _Optional[_Iterable[_Union[_explanation_pb2.Explanation, _Mapping]]]=...) -> None:
            ...

    class ConcurrentExplanationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: ExplainResponse.ConcurrentExplanation

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[ExplainResponse.ConcurrentExplanation, _Mapping]]=...) -> None:
            ...
    EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    CONCURRENT_EXPLANATIONS_FIELD_NUMBER: _ClassVar[int]
    DEPLOYED_MODEL_ID_FIELD_NUMBER: _ClassVar[int]
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    explanations: _containers.RepeatedCompositeFieldContainer[_explanation_pb2.Explanation]
    concurrent_explanations: _containers.MessageMap[str, ExplainResponse.ConcurrentExplanation]
    deployed_model_id: str
    predictions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]

    def __init__(self, explanations: _Optional[_Iterable[_Union[_explanation_pb2.Explanation, _Mapping]]]=..., concurrent_explanations: _Optional[_Mapping[str, ExplainResponse.ConcurrentExplanation]]=..., deployed_model_id: _Optional[str]=..., predictions: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=...) -> None:
        ...

class CountTokensRequest(_message.Message):
    __slots__ = ('endpoint', 'model', 'instances', 'contents', 'system_instruction', 'tools', 'generation_config')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    TOOLS_FIELD_NUMBER: _ClassVar[int]
    GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    model: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    system_instruction: _content_pb2.Content
    tools: _containers.RepeatedCompositeFieldContainer[_tool_pb2.Tool]
    generation_config: _content_pb2.GenerationConfig

    def __init__(self, endpoint: _Optional[str]=..., model: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., system_instruction: _Optional[_Union[_content_pb2.Content, _Mapping]]=..., tools: _Optional[_Iterable[_Union[_tool_pb2.Tool, _Mapping]]]=..., generation_config: _Optional[_Union[_content_pb2.GenerationConfig, _Mapping]]=...) -> None:
        ...

class CountTokensResponse(_message.Message):
    __slots__ = ('total_tokens', 'total_billable_characters', 'prompt_tokens_details')
    TOTAL_TOKENS_FIELD_NUMBER: _ClassVar[int]
    TOTAL_BILLABLE_CHARACTERS_FIELD_NUMBER: _ClassVar[int]
    PROMPT_TOKENS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    total_tokens: int
    total_billable_characters: int
    prompt_tokens_details: _containers.RepeatedCompositeFieldContainer[_content_pb2.ModalityTokenCount]

    def __init__(self, total_tokens: _Optional[int]=..., total_billable_characters: _Optional[int]=..., prompt_tokens_details: _Optional[_Iterable[_Union[_content_pb2.ModalityTokenCount, _Mapping]]]=...) -> None:
        ...

class GenerateContentRequest(_message.Message):
    __slots__ = ('model', 'contents', 'system_instruction', 'cached_content', 'tools', 'tool_config', 'labels', 'safety_settings', 'model_armor_config', 'generation_config')

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
    MODEL_ARMOR_CONFIG_FIELD_NUMBER: _ClassVar[int]
    GENERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    model: str
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    system_instruction: _content_pb2.Content
    cached_content: str
    tools: _containers.RepeatedCompositeFieldContainer[_tool_pb2.Tool]
    tool_config: _tool_pb2.ToolConfig
    labels: _containers.ScalarMap[str, str]
    safety_settings: _containers.RepeatedCompositeFieldContainer[_content_pb2.SafetySetting]
    model_armor_config: _content_pb2.ModelArmorConfig
    generation_config: _content_pb2.GenerationConfig

    def __init__(self, model: _Optional[str]=..., contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., system_instruction: _Optional[_Union[_content_pb2.Content, _Mapping]]=..., cached_content: _Optional[str]=..., tools: _Optional[_Iterable[_Union[_tool_pb2.Tool, _Mapping]]]=..., tool_config: _Optional[_Union[_tool_pb2.ToolConfig, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., safety_settings: _Optional[_Iterable[_Union[_content_pb2.SafetySetting, _Mapping]]]=..., model_armor_config: _Optional[_Union[_content_pb2.ModelArmorConfig, _Mapping]]=..., generation_config: _Optional[_Union[_content_pb2.GenerationConfig, _Mapping]]=...) -> None:
        ...

class GenerateContentResponse(_message.Message):
    __slots__ = ('candidates', 'model_version', 'create_time', 'response_id', 'prompt_feedback', 'usage_metadata')

    class PromptFeedback(_message.Message):
        __slots__ = ('block_reason', 'safety_ratings', 'block_reason_message')

        class BlockedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BLOCKED_REASON_UNSPECIFIED: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
            SAFETY: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
            OTHER: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
            BLOCKLIST: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
            PROHIBITED_CONTENT: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
            MODEL_ARMOR: _ClassVar[GenerateContentResponse.PromptFeedback.BlockedReason]
        BLOCKED_REASON_UNSPECIFIED: GenerateContentResponse.PromptFeedback.BlockedReason
        SAFETY: GenerateContentResponse.PromptFeedback.BlockedReason
        OTHER: GenerateContentResponse.PromptFeedback.BlockedReason
        BLOCKLIST: GenerateContentResponse.PromptFeedback.BlockedReason
        PROHIBITED_CONTENT: GenerateContentResponse.PromptFeedback.BlockedReason
        MODEL_ARMOR: GenerateContentResponse.PromptFeedback.BlockedReason
        BLOCK_REASON_FIELD_NUMBER: _ClassVar[int]
        SAFETY_RATINGS_FIELD_NUMBER: _ClassVar[int]
        BLOCK_REASON_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        block_reason: GenerateContentResponse.PromptFeedback.BlockedReason
        safety_ratings: _containers.RepeatedCompositeFieldContainer[_content_pb2.SafetyRating]
        block_reason_message: str

        def __init__(self, block_reason: _Optional[_Union[GenerateContentResponse.PromptFeedback.BlockedReason, str]]=..., safety_ratings: _Optional[_Iterable[_Union[_content_pb2.SafetyRating, _Mapping]]]=..., block_reason_message: _Optional[str]=...) -> None:
            ...

    class UsageMetadata(_message.Message):
        __slots__ = ('prompt_token_count', 'candidates_token_count', 'thoughts_token_count', 'total_token_count', 'cached_content_token_count', 'prompt_tokens_details', 'cache_tokens_details', 'candidates_tokens_details')
        PROMPT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        THOUGHTS_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        TOTAL_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        CACHED_CONTENT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
        PROMPT_TOKENS_DETAILS_FIELD_NUMBER: _ClassVar[int]
        CACHE_TOKENS_DETAILS_FIELD_NUMBER: _ClassVar[int]
        CANDIDATES_TOKENS_DETAILS_FIELD_NUMBER: _ClassVar[int]
        prompt_token_count: int
        candidates_token_count: int
        thoughts_token_count: int
        total_token_count: int
        cached_content_token_count: int
        prompt_tokens_details: _containers.RepeatedCompositeFieldContainer[_content_pb2.ModalityTokenCount]
        cache_tokens_details: _containers.RepeatedCompositeFieldContainer[_content_pb2.ModalityTokenCount]
        candidates_tokens_details: _containers.RepeatedCompositeFieldContainer[_content_pb2.ModalityTokenCount]

        def __init__(self, prompt_token_count: _Optional[int]=..., candidates_token_count: _Optional[int]=..., thoughts_token_count: _Optional[int]=..., total_token_count: _Optional[int]=..., cached_content_token_count: _Optional[int]=..., prompt_tokens_details: _Optional[_Iterable[_Union[_content_pb2.ModalityTokenCount, _Mapping]]]=..., cache_tokens_details: _Optional[_Iterable[_Union[_content_pb2.ModalityTokenCount, _Mapping]]]=..., candidates_tokens_details: _Optional[_Iterable[_Union[_content_pb2.ModalityTokenCount, _Mapping]]]=...) -> None:
            ...
    CANDIDATES_FIELD_NUMBER: _ClassVar[int]
    MODEL_VERSION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_ID_FIELD_NUMBER: _ClassVar[int]
    PROMPT_FEEDBACK_FIELD_NUMBER: _ClassVar[int]
    USAGE_METADATA_FIELD_NUMBER: _ClassVar[int]
    candidates: _containers.RepeatedCompositeFieldContainer[_content_pb2.Candidate]
    model_version: str
    create_time: _timestamp_pb2.Timestamp
    response_id: str
    prompt_feedback: GenerateContentResponse.PromptFeedback
    usage_metadata: GenerateContentResponse.UsageMetadata

    def __init__(self, candidates: _Optional[_Iterable[_Union[_content_pb2.Candidate, _Mapping]]]=..., model_version: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., response_id: _Optional[str]=..., prompt_feedback: _Optional[_Union[GenerateContentResponse.PromptFeedback, _Mapping]]=..., usage_metadata: _Optional[_Union[GenerateContentResponse.UsageMetadata, _Mapping]]=...) -> None:
        ...

class ChatCompletionsRequest(_message.Message):
    __slots__ = ('endpoint', 'http_body')
    ENDPOINT_FIELD_NUMBER: _ClassVar[int]
    HTTP_BODY_FIELD_NUMBER: _ClassVar[int]
    endpoint: str
    http_body: _httpbody_pb2.HttpBody

    def __init__(self, endpoint: _Optional[str]=..., http_body: _Optional[_Union[_httpbody_pb2.HttpBody, _Mapping]]=...) -> None:
        ...

class PredictLongRunningResponse(_message.Message):
    __slots__ = ('generate_video_response',)
    GENERATE_VIDEO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    generate_video_response: GenerateVideoResponse

    def __init__(self, generate_video_response: _Optional[_Union[GenerateVideoResponse, _Mapping]]=...) -> None:
        ...

class PredictLongRunningMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class GenerateVideoResponse(_message.Message):
    __slots__ = ('generated_samples', 'rai_media_filtered_count', 'rai_media_filtered_reasons')
    GENERATED_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    RAI_MEDIA_FILTERED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RAI_MEDIA_FILTERED_REASONS_FIELD_NUMBER: _ClassVar[int]
    generated_samples: _containers.RepeatedScalarFieldContainer[str]
    rai_media_filtered_count: int
    rai_media_filtered_reasons: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, generated_samples: _Optional[_Iterable[str]]=..., rai_media_filtered_count: _Optional[int]=..., rai_media_filtered_reasons: _Optional[_Iterable[str]]=...) -> None:
        ...