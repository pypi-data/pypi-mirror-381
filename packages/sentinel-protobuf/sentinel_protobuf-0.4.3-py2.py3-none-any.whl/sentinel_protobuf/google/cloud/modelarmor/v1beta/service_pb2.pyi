from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FilterMatchState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILTER_MATCH_STATE_UNSPECIFIED: _ClassVar[FilterMatchState]
    NO_MATCH_FOUND: _ClassVar[FilterMatchState]
    MATCH_FOUND: _ClassVar[FilterMatchState]

class FilterExecutionState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILTER_EXECUTION_STATE_UNSPECIFIED: _ClassVar[FilterExecutionState]
    EXECUTION_SUCCESS: _ClassVar[FilterExecutionState]
    EXECUTION_SKIPPED: _ClassVar[FilterExecutionState]

class RaiFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RAI_FILTER_TYPE_UNSPECIFIED: _ClassVar[RaiFilterType]
    SEXUALLY_EXPLICIT: _ClassVar[RaiFilterType]
    HATE_SPEECH: _ClassVar[RaiFilterType]
    HARASSMENT: _ClassVar[RaiFilterType]
    DANGEROUS: _ClassVar[RaiFilterType]

class DetectionConfidenceLevel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED: _ClassVar[DetectionConfidenceLevel]
    LOW_AND_ABOVE: _ClassVar[DetectionConfidenceLevel]
    MEDIUM_AND_ABOVE: _ClassVar[DetectionConfidenceLevel]
    HIGH: _ClassVar[DetectionConfidenceLevel]

class SdpFindingLikelihood(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SDP_FINDING_LIKELIHOOD_UNSPECIFIED: _ClassVar[SdpFindingLikelihood]
    VERY_UNLIKELY: _ClassVar[SdpFindingLikelihood]
    UNLIKELY: _ClassVar[SdpFindingLikelihood]
    POSSIBLE: _ClassVar[SdpFindingLikelihood]
    LIKELY: _ClassVar[SdpFindingLikelihood]
    VERY_LIKELY: _ClassVar[SdpFindingLikelihood]

class InvocationResult(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INVOCATION_RESULT_UNSPECIFIED: _ClassVar[InvocationResult]
    SUCCESS: _ClassVar[InvocationResult]
    PARTIAL: _ClassVar[InvocationResult]
    FAILURE: _ClassVar[InvocationResult]
FILTER_MATCH_STATE_UNSPECIFIED: FilterMatchState
NO_MATCH_FOUND: FilterMatchState
MATCH_FOUND: FilterMatchState
FILTER_EXECUTION_STATE_UNSPECIFIED: FilterExecutionState
EXECUTION_SUCCESS: FilterExecutionState
EXECUTION_SKIPPED: FilterExecutionState
RAI_FILTER_TYPE_UNSPECIFIED: RaiFilterType
SEXUALLY_EXPLICIT: RaiFilterType
HATE_SPEECH: RaiFilterType
HARASSMENT: RaiFilterType
DANGEROUS: RaiFilterType
DETECTION_CONFIDENCE_LEVEL_UNSPECIFIED: DetectionConfidenceLevel
LOW_AND_ABOVE: DetectionConfidenceLevel
MEDIUM_AND_ABOVE: DetectionConfidenceLevel
HIGH: DetectionConfidenceLevel
SDP_FINDING_LIKELIHOOD_UNSPECIFIED: SdpFindingLikelihood
VERY_UNLIKELY: SdpFindingLikelihood
UNLIKELY: SdpFindingLikelihood
POSSIBLE: SdpFindingLikelihood
LIKELY: SdpFindingLikelihood
VERY_LIKELY: SdpFindingLikelihood
INVOCATION_RESULT_UNSPECIFIED: InvocationResult
SUCCESS: InvocationResult
PARTIAL: InvocationResult
FAILURE: InvocationResult

class Template(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'filter_config', 'template_metadata')

    class TemplateMetadata(_message.Message):
        __slots__ = ('ignore_partial_invocation_failures', 'custom_prompt_safety_error_code', 'custom_prompt_safety_error_message', 'custom_llm_response_safety_error_code', 'custom_llm_response_safety_error_message', 'log_template_operations', 'log_sanitize_operations', 'enforcement_type', 'multi_language_detection')

        class EnforcementType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ENFORCEMENT_TYPE_UNSPECIFIED: _ClassVar[Template.TemplateMetadata.EnforcementType]
            INSPECT_ONLY: _ClassVar[Template.TemplateMetadata.EnforcementType]
            INSPECT_AND_BLOCK: _ClassVar[Template.TemplateMetadata.EnforcementType]
        ENFORCEMENT_TYPE_UNSPECIFIED: Template.TemplateMetadata.EnforcementType
        INSPECT_ONLY: Template.TemplateMetadata.EnforcementType
        INSPECT_AND_BLOCK: Template.TemplateMetadata.EnforcementType

        class MultiLanguageDetection(_message.Message):
            __slots__ = ('enable_multi_language_detection',)
            ENABLE_MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
            enable_multi_language_detection: bool

            def __init__(self, enable_multi_language_detection: bool=...) -> None:
                ...
        IGNORE_PARTIAL_INVOCATION_FAILURES_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PROMPT_SAFETY_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_PROMPT_SAFETY_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_LLM_RESPONSE_SAFETY_ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_LLM_RESPONSE_SAFETY_ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        LOG_TEMPLATE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        LOG_SANITIZE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        ENFORCEMENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
        ignore_partial_invocation_failures: bool
        custom_prompt_safety_error_code: int
        custom_prompt_safety_error_message: str
        custom_llm_response_safety_error_code: int
        custom_llm_response_safety_error_message: str
        log_template_operations: bool
        log_sanitize_operations: bool
        enforcement_type: Template.TemplateMetadata.EnforcementType
        multi_language_detection: Template.TemplateMetadata.MultiLanguageDetection

        def __init__(self, ignore_partial_invocation_failures: bool=..., custom_prompt_safety_error_code: _Optional[int]=..., custom_prompt_safety_error_message: _Optional[str]=..., custom_llm_response_safety_error_code: _Optional[int]=..., custom_llm_response_safety_error_message: _Optional[str]=..., log_template_operations: bool=..., log_sanitize_operations: bool=..., enforcement_type: _Optional[_Union[Template.TemplateMetadata.EnforcementType, str]]=..., multi_language_detection: _Optional[_Union[Template.TemplateMetadata.MultiLanguageDetection, _Mapping]]=...) -> None:
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
    FILTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    filter_config: FilterConfig
    template_metadata: Template.TemplateMetadata

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., filter_config: _Optional[_Union[FilterConfig, _Mapping]]=..., template_metadata: _Optional[_Union[Template.TemplateMetadata, _Mapping]]=...) -> None:
        ...

class FloorSetting(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'filter_config', 'enable_floor_setting_enforcement', 'integrated_services', 'ai_platform_floor_setting', 'floor_setting_metadata')

    class IntegratedService(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        INTEGRATED_SERVICE_UNSPECIFIED: _ClassVar[FloorSetting.IntegratedService]
        AI_PLATFORM: _ClassVar[FloorSetting.IntegratedService]
    INTEGRATED_SERVICE_UNSPECIFIED: FloorSetting.IntegratedService
    AI_PLATFORM: FloorSetting.IntegratedService

    class FloorSettingMetadata(_message.Message):
        __slots__ = ('multi_language_detection',)

        class MultiLanguageDetection(_message.Message):
            __slots__ = ('enable_multi_language_detection',)
            ENABLE_MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
            enable_multi_language_detection: bool

            def __init__(self, enable_multi_language_detection: bool=...) -> None:
                ...
        MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
        multi_language_detection: FloorSetting.FloorSettingMetadata.MultiLanguageDetection

        def __init__(self, multi_language_detection: _Optional[_Union[FloorSetting.FloorSettingMetadata.MultiLanguageDetection, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    FILTER_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ENABLE_FLOOR_SETTING_ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    INTEGRATED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    AI_PLATFORM_FLOOR_SETTING_FIELD_NUMBER: _ClassVar[int]
    FLOOR_SETTING_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    filter_config: FilterConfig
    enable_floor_setting_enforcement: bool
    integrated_services: _containers.RepeatedScalarFieldContainer[FloorSetting.IntegratedService]
    ai_platform_floor_setting: AiPlatformFloorSetting
    floor_setting_metadata: FloorSetting.FloorSettingMetadata

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., filter_config: _Optional[_Union[FilterConfig, _Mapping]]=..., enable_floor_setting_enforcement: bool=..., integrated_services: _Optional[_Iterable[_Union[FloorSetting.IntegratedService, str]]]=..., ai_platform_floor_setting: _Optional[_Union[AiPlatformFloorSetting, _Mapping]]=..., floor_setting_metadata: _Optional[_Union[FloorSetting.FloorSettingMetadata, _Mapping]]=...) -> None:
        ...

class AiPlatformFloorSetting(_message.Message):
    __slots__ = ('inspect_only', 'inspect_and_block', 'enable_cloud_logging')
    INSPECT_ONLY_FIELD_NUMBER: _ClassVar[int]
    INSPECT_AND_BLOCK_FIELD_NUMBER: _ClassVar[int]
    ENABLE_CLOUD_LOGGING_FIELD_NUMBER: _ClassVar[int]
    inspect_only: bool
    inspect_and_block: bool
    enable_cloud_logging: bool

    def __init__(self, inspect_only: bool=..., inspect_and_block: bool=..., enable_cloud_logging: bool=...) -> None:
        ...

class ListTemplatesRequest(_message.Message):
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

class ListTemplatesResponse(_message.Message):
    __slots__ = ('templates', 'next_page_token', 'unreachable')
    TEMPLATES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    templates: _containers.RepeatedCompositeFieldContainer[Template]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, templates: _Optional[_Iterable[_Union[Template, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetTemplateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateTemplateRequest(_message.Message):
    __slots__ = ('parent', 'template_id', 'template', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_ID_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    template_id: str
    template: Template
    request_id: str

    def __init__(self, parent: _Optional[str]=..., template_id: _Optional[str]=..., template: _Optional[_Union[Template, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class UpdateTemplateRequest(_message.Message):
    __slots__ = ('update_mask', 'template', 'request_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    template: Template
    request_id: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., template: _Optional[_Union[Template, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteTemplateRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class GetFloorSettingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateFloorSettingRequest(_message.Message):
    __slots__ = ('floor_setting', 'update_mask')
    FLOOR_SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    floor_setting: FloorSetting
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, floor_setting: _Optional[_Union[FloorSetting, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class FilterConfig(_message.Message):
    __slots__ = ('rai_settings', 'sdp_settings', 'pi_and_jailbreak_filter_settings', 'malicious_uri_filter_settings')
    RAI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SDP_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    PI_AND_JAILBREAK_FILTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    MALICIOUS_URI_FILTER_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    rai_settings: RaiFilterSettings
    sdp_settings: SdpFilterSettings
    pi_and_jailbreak_filter_settings: PiAndJailbreakFilterSettings
    malicious_uri_filter_settings: MaliciousUriFilterSettings

    def __init__(self, rai_settings: _Optional[_Union[RaiFilterSettings, _Mapping]]=..., sdp_settings: _Optional[_Union[SdpFilterSettings, _Mapping]]=..., pi_and_jailbreak_filter_settings: _Optional[_Union[PiAndJailbreakFilterSettings, _Mapping]]=..., malicious_uri_filter_settings: _Optional[_Union[MaliciousUriFilterSettings, _Mapping]]=...) -> None:
        ...

class PiAndJailbreakFilterSettings(_message.Message):
    __slots__ = ('filter_enforcement', 'confidence_level')

    class PiAndJailbreakFilterEnforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PI_AND_JAILBREAK_FILTER_ENFORCEMENT_UNSPECIFIED: _ClassVar[PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement]
        ENABLED: _ClassVar[PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement]
        DISABLED: _ClassVar[PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement]
    PI_AND_JAILBREAK_FILTER_ENFORCEMENT_UNSPECIFIED: PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement
    ENABLED: PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement
    DISABLED: PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement
    FILTER_ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    filter_enforcement: PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement
    confidence_level: DetectionConfidenceLevel

    def __init__(self, filter_enforcement: _Optional[_Union[PiAndJailbreakFilterSettings.PiAndJailbreakFilterEnforcement, str]]=..., confidence_level: _Optional[_Union[DetectionConfidenceLevel, str]]=...) -> None:
        ...

class MaliciousUriFilterSettings(_message.Message):
    __slots__ = ('filter_enforcement',)

    class MaliciousUriFilterEnforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MALICIOUS_URI_FILTER_ENFORCEMENT_UNSPECIFIED: _ClassVar[MaliciousUriFilterSettings.MaliciousUriFilterEnforcement]
        ENABLED: _ClassVar[MaliciousUriFilterSettings.MaliciousUriFilterEnforcement]
        DISABLED: _ClassVar[MaliciousUriFilterSettings.MaliciousUriFilterEnforcement]
    MALICIOUS_URI_FILTER_ENFORCEMENT_UNSPECIFIED: MaliciousUriFilterSettings.MaliciousUriFilterEnforcement
    ENABLED: MaliciousUriFilterSettings.MaliciousUriFilterEnforcement
    DISABLED: MaliciousUriFilterSettings.MaliciousUriFilterEnforcement
    FILTER_ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    filter_enforcement: MaliciousUriFilterSettings.MaliciousUriFilterEnforcement

    def __init__(self, filter_enforcement: _Optional[_Union[MaliciousUriFilterSettings.MaliciousUriFilterEnforcement, str]]=...) -> None:
        ...

class RaiFilterSettings(_message.Message):
    __slots__ = ('rai_filters',)

    class RaiFilter(_message.Message):
        __slots__ = ('filter_type', 'confidence_level')
        FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        filter_type: RaiFilterType
        confidence_level: DetectionConfidenceLevel

        def __init__(self, filter_type: _Optional[_Union[RaiFilterType, str]]=..., confidence_level: _Optional[_Union[DetectionConfidenceLevel, str]]=...) -> None:
            ...
    RAI_FILTERS_FIELD_NUMBER: _ClassVar[int]
    rai_filters: _containers.RepeatedCompositeFieldContainer[RaiFilterSettings.RaiFilter]

    def __init__(self, rai_filters: _Optional[_Iterable[_Union[RaiFilterSettings.RaiFilter, _Mapping]]]=...) -> None:
        ...

class SdpFilterSettings(_message.Message):
    __slots__ = ('basic_config', 'advanced_config')
    BASIC_CONFIG_FIELD_NUMBER: _ClassVar[int]
    ADVANCED_CONFIG_FIELD_NUMBER: _ClassVar[int]
    basic_config: SdpBasicConfig
    advanced_config: SdpAdvancedConfig

    def __init__(self, basic_config: _Optional[_Union[SdpBasicConfig, _Mapping]]=..., advanced_config: _Optional[_Union[SdpAdvancedConfig, _Mapping]]=...) -> None:
        ...

class SdpBasicConfig(_message.Message):
    __slots__ = ('filter_enforcement',)

    class SdpBasicConfigEnforcement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SDP_BASIC_CONFIG_ENFORCEMENT_UNSPECIFIED: _ClassVar[SdpBasicConfig.SdpBasicConfigEnforcement]
        ENABLED: _ClassVar[SdpBasicConfig.SdpBasicConfigEnforcement]
        DISABLED: _ClassVar[SdpBasicConfig.SdpBasicConfigEnforcement]
    SDP_BASIC_CONFIG_ENFORCEMENT_UNSPECIFIED: SdpBasicConfig.SdpBasicConfigEnforcement
    ENABLED: SdpBasicConfig.SdpBasicConfigEnforcement
    DISABLED: SdpBasicConfig.SdpBasicConfigEnforcement
    FILTER_ENFORCEMENT_FIELD_NUMBER: _ClassVar[int]
    filter_enforcement: SdpBasicConfig.SdpBasicConfigEnforcement

    def __init__(self, filter_enforcement: _Optional[_Union[SdpBasicConfig.SdpBasicConfigEnforcement, str]]=...) -> None:
        ...

class SdpAdvancedConfig(_message.Message):
    __slots__ = ('inspect_template', 'deidentify_template')
    INSPECT_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    DEIDENTIFY_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    inspect_template: str
    deidentify_template: str

    def __init__(self, inspect_template: _Optional[str]=..., deidentify_template: _Optional[str]=...) -> None:
        ...

class SanitizeUserPromptRequest(_message.Message):
    __slots__ = ('name', 'user_prompt_data', 'multi_language_detection_metadata')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_DATA_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_DETECTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    user_prompt_data: DataItem
    multi_language_detection_metadata: MultiLanguageDetectionMetadata

    def __init__(self, name: _Optional[str]=..., user_prompt_data: _Optional[_Union[DataItem, _Mapping]]=..., multi_language_detection_metadata: _Optional[_Union[MultiLanguageDetectionMetadata, _Mapping]]=...) -> None:
        ...

class SanitizeModelResponseRequest(_message.Message):
    __slots__ = ('name', 'model_response_data', 'user_prompt', 'multi_language_detection_metadata')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODEL_RESPONSE_DATA_FIELD_NUMBER: _ClassVar[int]
    USER_PROMPT_FIELD_NUMBER: _ClassVar[int]
    MULTI_LANGUAGE_DETECTION_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    model_response_data: DataItem
    user_prompt: str
    multi_language_detection_metadata: MultiLanguageDetectionMetadata

    def __init__(self, name: _Optional[str]=..., model_response_data: _Optional[_Union[DataItem, _Mapping]]=..., user_prompt: _Optional[str]=..., multi_language_detection_metadata: _Optional[_Union[MultiLanguageDetectionMetadata, _Mapping]]=...) -> None:
        ...

class SanitizeUserPromptResponse(_message.Message):
    __slots__ = ('sanitization_result',)
    SANITIZATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    sanitization_result: SanitizationResult

    def __init__(self, sanitization_result: _Optional[_Union[SanitizationResult, _Mapping]]=...) -> None:
        ...

class SanitizeModelResponseResponse(_message.Message):
    __slots__ = ('sanitization_result',)
    SANITIZATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    sanitization_result: SanitizationResult

    def __init__(self, sanitization_result: _Optional[_Union[SanitizationResult, _Mapping]]=...) -> None:
        ...

class SanitizationResult(_message.Message):
    __slots__ = ('filter_match_state', 'filter_results', 'invocation_result', 'sanitization_metadata')

    class SanitizationMetadata(_message.Message):
        __slots__ = ('error_code', 'error_message', 'ignore_partial_invocation_failures')
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
        IGNORE_PARTIAL_INVOCATION_FAILURES_FIELD_NUMBER: _ClassVar[int]
        error_code: int
        error_message: str
        ignore_partial_invocation_failures: bool

        def __init__(self, error_code: _Optional[int]=..., error_message: _Optional[str]=..., ignore_partial_invocation_failures: bool=...) -> None:
            ...

    class FilterResultsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FilterResult

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FilterResult, _Mapping]]=...) -> None:
            ...
    FILTER_MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    FILTER_RESULTS_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    SANITIZATION_METADATA_FIELD_NUMBER: _ClassVar[int]
    filter_match_state: FilterMatchState
    filter_results: _containers.MessageMap[str, FilterResult]
    invocation_result: InvocationResult
    sanitization_metadata: SanitizationResult.SanitizationMetadata

    def __init__(self, filter_match_state: _Optional[_Union[FilterMatchState, str]]=..., filter_results: _Optional[_Mapping[str, FilterResult]]=..., invocation_result: _Optional[_Union[InvocationResult, str]]=..., sanitization_metadata: _Optional[_Union[SanitizationResult.SanitizationMetadata, _Mapping]]=...) -> None:
        ...

class MultiLanguageDetectionMetadata(_message.Message):
    __slots__ = ('source_language', 'enable_multi_language_detection')
    SOURCE_LANGUAGE_FIELD_NUMBER: _ClassVar[int]
    ENABLE_MULTI_LANGUAGE_DETECTION_FIELD_NUMBER: _ClassVar[int]
    source_language: str
    enable_multi_language_detection: bool

    def __init__(self, source_language: _Optional[str]=..., enable_multi_language_detection: bool=...) -> None:
        ...

class FilterResult(_message.Message):
    __slots__ = ('rai_filter_result', 'sdp_filter_result', 'pi_and_jailbreak_filter_result', 'malicious_uri_filter_result', 'csam_filter_filter_result', 'virus_scan_filter_result')
    RAI_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    SDP_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    PI_AND_JAILBREAK_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    MALICIOUS_URI_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    CSAM_FILTER_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    VIRUS_SCAN_FILTER_RESULT_FIELD_NUMBER: _ClassVar[int]
    rai_filter_result: RaiFilterResult
    sdp_filter_result: SdpFilterResult
    pi_and_jailbreak_filter_result: PiAndJailbreakFilterResult
    malicious_uri_filter_result: MaliciousUriFilterResult
    csam_filter_filter_result: CsamFilterResult
    virus_scan_filter_result: VirusScanFilterResult

    def __init__(self, rai_filter_result: _Optional[_Union[RaiFilterResult, _Mapping]]=..., sdp_filter_result: _Optional[_Union[SdpFilterResult, _Mapping]]=..., pi_and_jailbreak_filter_result: _Optional[_Union[PiAndJailbreakFilterResult, _Mapping]]=..., malicious_uri_filter_result: _Optional[_Union[MaliciousUriFilterResult, _Mapping]]=..., csam_filter_filter_result: _Optional[_Union[CsamFilterResult, _Mapping]]=..., virus_scan_filter_result: _Optional[_Union[VirusScanFilterResult, _Mapping]]=...) -> None:
        ...

class RaiFilterResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'rai_filter_type_results')

    class RaiFilterTypeResult(_message.Message):
        __slots__ = ('filter_type', 'confidence_level', 'match_state')
        FILTER_TYPE_FIELD_NUMBER: _ClassVar[int]
        CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
        MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
        filter_type: RaiFilterType
        confidence_level: DetectionConfidenceLevel
        match_state: FilterMatchState

        def __init__(self, filter_type: _Optional[_Union[RaiFilterType, str]]=..., confidence_level: _Optional[_Union[DetectionConfidenceLevel, str]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=...) -> None:
            ...

    class RaiFilterTypeResultsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: RaiFilterResult.RaiFilterTypeResult

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[RaiFilterResult.RaiFilterTypeResult, _Mapping]]=...) -> None:
            ...
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    RAI_FILTER_TYPE_RESULTS_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    rai_filter_type_results: _containers.MessageMap[str, RaiFilterResult.RaiFilterTypeResult]

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., rai_filter_type_results: _Optional[_Mapping[str, RaiFilterResult.RaiFilterTypeResult]]=...) -> None:
        ...

class SdpFilterResult(_message.Message):
    __slots__ = ('inspect_result', 'deidentify_result')
    INSPECT_RESULT_FIELD_NUMBER: _ClassVar[int]
    DEIDENTIFY_RESULT_FIELD_NUMBER: _ClassVar[int]
    inspect_result: SdpInspectResult
    deidentify_result: SdpDeidentifyResult

    def __init__(self, inspect_result: _Optional[_Union[SdpInspectResult, _Mapping]]=..., deidentify_result: _Optional[_Union[SdpDeidentifyResult, _Mapping]]=...) -> None:
        ...

class SdpInspectResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'findings', 'findings_truncated')
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_FIELD_NUMBER: _ClassVar[int]
    FINDINGS_TRUNCATED_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    findings: _containers.RepeatedCompositeFieldContainer[SdpFinding]
    findings_truncated: bool

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., findings: _Optional[_Iterable[_Union[SdpFinding, _Mapping]]]=..., findings_truncated: bool=...) -> None:
        ...

class DataItem(_message.Message):
    __slots__ = ('text', 'byte_item')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    BYTE_ITEM_FIELD_NUMBER: _ClassVar[int]
    text: str
    byte_item: ByteDataItem

    def __init__(self, text: _Optional[str]=..., byte_item: _Optional[_Union[ByteDataItem, _Mapping]]=...) -> None:
        ...

class ByteDataItem(_message.Message):
    __slots__ = ('byte_data_type', 'byte_data')

    class ByteItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BYTE_ITEM_TYPE_UNSPECIFIED: _ClassVar[ByteDataItem.ByteItemType]
        PLAINTEXT_UTF8: _ClassVar[ByteDataItem.ByteItemType]
        PDF: _ClassVar[ByteDataItem.ByteItemType]
        WORD_DOCUMENT: _ClassVar[ByteDataItem.ByteItemType]
        EXCEL_DOCUMENT: _ClassVar[ByteDataItem.ByteItemType]
        POWERPOINT_DOCUMENT: _ClassVar[ByteDataItem.ByteItemType]
        TXT: _ClassVar[ByteDataItem.ByteItemType]
        CSV: _ClassVar[ByteDataItem.ByteItemType]
    BYTE_ITEM_TYPE_UNSPECIFIED: ByteDataItem.ByteItemType
    PLAINTEXT_UTF8: ByteDataItem.ByteItemType
    PDF: ByteDataItem.ByteItemType
    WORD_DOCUMENT: ByteDataItem.ByteItemType
    EXCEL_DOCUMENT: ByteDataItem.ByteItemType
    POWERPOINT_DOCUMENT: ByteDataItem.ByteItemType
    TXT: ByteDataItem.ByteItemType
    CSV: ByteDataItem.ByteItemType
    BYTE_DATA_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_DATA_FIELD_NUMBER: _ClassVar[int]
    byte_data_type: ByteDataItem.ByteItemType
    byte_data: bytes

    def __init__(self, byte_data_type: _Optional[_Union[ByteDataItem.ByteItemType, str]]=..., byte_data: _Optional[bytes]=...) -> None:
        ...

class SdpDeidentifyResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'data', 'transformed_bytes', 'info_types')
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    TRANSFORMED_BYTES_FIELD_NUMBER: _ClassVar[int]
    INFO_TYPES_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    data: DataItem
    transformed_bytes: int
    info_types: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., data: _Optional[_Union[DataItem, _Mapping]]=..., transformed_bytes: _Optional[int]=..., info_types: _Optional[_Iterable[str]]=...) -> None:
        ...

class SdpFinding(_message.Message):
    __slots__ = ('info_type', 'likelihood', 'location')

    class SdpFindingLocation(_message.Message):
        __slots__ = ('byte_range', 'codepoint_range')
        BYTE_RANGE_FIELD_NUMBER: _ClassVar[int]
        CODEPOINT_RANGE_FIELD_NUMBER: _ClassVar[int]
        byte_range: RangeInfo
        codepoint_range: RangeInfo

        def __init__(self, byte_range: _Optional[_Union[RangeInfo, _Mapping]]=..., codepoint_range: _Optional[_Union[RangeInfo, _Mapping]]=...) -> None:
            ...
    INFO_TYPE_FIELD_NUMBER: _ClassVar[int]
    LIKELIHOOD_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    info_type: str
    likelihood: SdpFindingLikelihood
    location: SdpFinding.SdpFindingLocation

    def __init__(self, info_type: _Optional[str]=..., likelihood: _Optional[_Union[SdpFindingLikelihood, str]]=..., location: _Optional[_Union[SdpFinding.SdpFindingLocation, _Mapping]]=...) -> None:
        ...

class PiAndJailbreakFilterResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'confidence_level')
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    CONFIDENCE_LEVEL_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    confidence_level: DetectionConfidenceLevel

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., confidence_level: _Optional[_Union[DetectionConfidenceLevel, str]]=...) -> None:
        ...

class MaliciousUriFilterResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'malicious_uri_matched_items')

    class MaliciousUriMatchedItem(_message.Message):
        __slots__ = ('uri', 'locations')
        URI_FIELD_NUMBER: _ClassVar[int]
        LOCATIONS_FIELD_NUMBER: _ClassVar[int]
        uri: str
        locations: _containers.RepeatedCompositeFieldContainer[RangeInfo]

        def __init__(self, uri: _Optional[str]=..., locations: _Optional[_Iterable[_Union[RangeInfo, _Mapping]]]=...) -> None:
            ...
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    MALICIOUS_URI_MATCHED_ITEMS_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    malicious_uri_matched_items: _containers.RepeatedCompositeFieldContainer[MaliciousUriFilterResult.MaliciousUriMatchedItem]

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., malicious_uri_matched_items: _Optional[_Iterable[_Union[MaliciousUriFilterResult.MaliciousUriMatchedItem, _Mapping]]]=...) -> None:
        ...

class VirusScanFilterResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state', 'scanned_content_type', 'scanned_size', 'virus_details')

    class ScannedContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCANNED_CONTENT_TYPE_UNSPECIFIED: _ClassVar[VirusScanFilterResult.ScannedContentType]
        UNKNOWN: _ClassVar[VirusScanFilterResult.ScannedContentType]
        PLAINTEXT: _ClassVar[VirusScanFilterResult.ScannedContentType]
        PDF: _ClassVar[VirusScanFilterResult.ScannedContentType]
    SCANNED_CONTENT_TYPE_UNSPECIFIED: VirusScanFilterResult.ScannedContentType
    UNKNOWN: VirusScanFilterResult.ScannedContentType
    PLAINTEXT: VirusScanFilterResult.ScannedContentType
    PDF: VirusScanFilterResult.ScannedContentType
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    SCANNED_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCANNED_SIZE_FIELD_NUMBER: _ClassVar[int]
    VIRUS_DETAILS_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState
    scanned_content_type: VirusScanFilterResult.ScannedContentType
    scanned_size: int
    virus_details: _containers.RepeatedCompositeFieldContainer[VirusDetail]

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=..., scanned_content_type: _Optional[_Union[VirusScanFilterResult.ScannedContentType, str]]=..., scanned_size: _Optional[int]=..., virus_details: _Optional[_Iterable[_Union[VirusDetail, _Mapping]]]=...) -> None:
        ...

class VirusDetail(_message.Message):
    __slots__ = ('vendor', 'names', 'threat_type')

    class ThreatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        THREAT_TYPE_UNSPECIFIED: _ClassVar[VirusDetail.ThreatType]
        UNKNOWN: _ClassVar[VirusDetail.ThreatType]
        VIRUS_OR_WORM: _ClassVar[VirusDetail.ThreatType]
        MALICIOUS_PROGRAM: _ClassVar[VirusDetail.ThreatType]
        POTENTIALLY_HARMFUL_CONTENT: _ClassVar[VirusDetail.ThreatType]
        POTENTIALLY_UNWANTED_CONTENT: _ClassVar[VirusDetail.ThreatType]
    THREAT_TYPE_UNSPECIFIED: VirusDetail.ThreatType
    UNKNOWN: VirusDetail.ThreatType
    VIRUS_OR_WORM: VirusDetail.ThreatType
    MALICIOUS_PROGRAM: VirusDetail.ThreatType
    POTENTIALLY_HARMFUL_CONTENT: VirusDetail.ThreatType
    POTENTIALLY_UNWANTED_CONTENT: VirusDetail.ThreatType
    VENDOR_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    THREAT_TYPE_FIELD_NUMBER: _ClassVar[int]
    vendor: str
    names: _containers.RepeatedScalarFieldContainer[str]
    threat_type: VirusDetail.ThreatType

    def __init__(self, vendor: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., threat_type: _Optional[_Union[VirusDetail.ThreatType, str]]=...) -> None:
        ...

class CsamFilterResult(_message.Message):
    __slots__ = ('execution_state', 'message_items', 'match_state')
    EXECUTION_STATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    MATCH_STATE_FIELD_NUMBER: _ClassVar[int]
    execution_state: FilterExecutionState
    message_items: _containers.RepeatedCompositeFieldContainer[MessageItem]
    match_state: FilterMatchState

    def __init__(self, execution_state: _Optional[_Union[FilterExecutionState, str]]=..., message_items: _Optional[_Iterable[_Union[MessageItem, _Mapping]]]=..., match_state: _Optional[_Union[FilterMatchState, str]]=...) -> None:
        ...

class MessageItem(_message.Message):
    __slots__ = ('message_type', 'message')

    class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MESSAGE_TYPE_UNSPECIFIED: _ClassVar[MessageItem.MessageType]
        INFO: _ClassVar[MessageItem.MessageType]
        WARNING: _ClassVar[MessageItem.MessageType]
        ERROR: _ClassVar[MessageItem.MessageType]
    MESSAGE_TYPE_UNSPECIFIED: MessageItem.MessageType
    INFO: MessageItem.MessageType
    WARNING: MessageItem.MessageType
    ERROR: MessageItem.MessageType
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_type: MessageItem.MessageType
    message: str

    def __init__(self, message_type: _Optional[_Union[MessageItem.MessageType, str]]=..., message: _Optional[str]=...) -> None:
        ...

class RangeInfo(_message.Message):
    __slots__ = ('start', 'end')
    START_FIELD_NUMBER: _ClassVar[int]
    END_FIELD_NUMBER: _ClassVar[int]
    start: int
    end: int

    def __init__(self, start: _Optional[int]=..., end: _Optional[int]=...) -> None:
        ...