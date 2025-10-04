from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EnforcementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ENFORCEMENT_MODE_UNSPECIFIED: _ClassVar[EnforcementMode]
    PREVENTIVE: _ClassVar[EnforcementMode]
    DETECTIVE: _ClassVar[EnforcementMode]
    AUDIT: _ClassVar[EnforcementMode]

class FrameworkCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FRAMEWORK_CATEGORY_UNSPECIFIED: _ClassVar[FrameworkCategory]
    INDUSTRY_DEFINED_STANDARD: _ClassVar[FrameworkCategory]
    ASSURED_WORKLOADS: _ClassVar[FrameworkCategory]
    DATA_SECURITY: _ClassVar[FrameworkCategory]
    GOOGLE_BEST_PRACTICES: _ClassVar[FrameworkCategory]
    CUSTOM_FRAMEWORK: _ClassVar[FrameworkCategory]

class CloudControlCategory(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_CONTROL_CATEGORY_UNSPECIFIED: _ClassVar[CloudControlCategory]
    CC_CATEGORY_INFRASTRUCTURE: _ClassVar[CloudControlCategory]
    CC_CATEGORY_ARTIFICIAL_INTELLIGENCE: _ClassVar[CloudControlCategory]
    CC_CATEGORY_PHYSICAL_SECURITY: _ClassVar[CloudControlCategory]
    CC_CATEGORY_DATA_SECURITY: _ClassVar[CloudControlCategory]
    CC_CATEGORY_NETWORK_SECURITY: _ClassVar[CloudControlCategory]
    CC_CATEGORY_INCIDENT_MANAGEMENT: _ClassVar[CloudControlCategory]
    CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT: _ClassVar[CloudControlCategory]
    CC_CATEGORY_ENCRYPTION: _ClassVar[CloudControlCategory]
    CC_CATEGORY_LOGS_MANAGEMENT_AND_INFRASTRUCTURE: _ClassVar[CloudControlCategory]
    CC_CATEGORY_HR_ADMIN_AND_PROCESSES: _ClassVar[CloudControlCategory]
    CC_CATEGORY_THIRD_PARTY_AND_SUB_PROCESSOR_MANAGEMENT: _ClassVar[CloudControlCategory]
    CC_CATEGORY_LEGAL_AND_DISCLOSURES: _ClassVar[CloudControlCategory]
    CC_CATEGORY_VULNERABILITY_MANAGEMENT: _ClassVar[CloudControlCategory]
    CC_CATEGORY_PRIVACY: _ClassVar[CloudControlCategory]
    CC_CATEGORY_BCDR: _ClassVar[CloudControlCategory]

class CloudProvider(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLOUD_PROVIDER_UNSPECIFIED: _ClassVar[CloudProvider]
    AWS: _ClassVar[CloudProvider]
    AZURE: _ClassVar[CloudProvider]
    GCP: _ClassVar[CloudProvider]

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    CRITICAL: _ClassVar[Severity]
    HIGH: _ClassVar[Severity]
    MEDIUM: _ClassVar[Severity]
    LOW: _ClassVar[Severity]

class RuleActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RULE_ACTION_TYPE_UNSPECIFIED: _ClassVar[RuleActionType]
    RULE_ACTION_TYPE_PREVENTIVE: _ClassVar[RuleActionType]
    RULE_ACTION_TYPE_DETECTIVE: _ClassVar[RuleActionType]
    RULE_ACTION_TYPE_AUDIT: _ClassVar[RuleActionType]

class TargetResourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TARGET_RESOURCE_TYPE_UNSPECIFIED: _ClassVar[TargetResourceType]
    TARGET_RESOURCE_CRM_TYPE_ORG: _ClassVar[TargetResourceType]
    TARGET_RESOURCE_CRM_TYPE_FOLDER: _ClassVar[TargetResourceType]
    TARGET_RESOURCE_CRM_TYPE_PROJECT: _ClassVar[TargetResourceType]
    TARGET_RESOURCE_TYPE_APPLICATION: _ClassVar[TargetResourceType]
ENFORCEMENT_MODE_UNSPECIFIED: EnforcementMode
PREVENTIVE: EnforcementMode
DETECTIVE: EnforcementMode
AUDIT: EnforcementMode
FRAMEWORK_CATEGORY_UNSPECIFIED: FrameworkCategory
INDUSTRY_DEFINED_STANDARD: FrameworkCategory
ASSURED_WORKLOADS: FrameworkCategory
DATA_SECURITY: FrameworkCategory
GOOGLE_BEST_PRACTICES: FrameworkCategory
CUSTOM_FRAMEWORK: FrameworkCategory
CLOUD_CONTROL_CATEGORY_UNSPECIFIED: CloudControlCategory
CC_CATEGORY_INFRASTRUCTURE: CloudControlCategory
CC_CATEGORY_ARTIFICIAL_INTELLIGENCE: CloudControlCategory
CC_CATEGORY_PHYSICAL_SECURITY: CloudControlCategory
CC_CATEGORY_DATA_SECURITY: CloudControlCategory
CC_CATEGORY_NETWORK_SECURITY: CloudControlCategory
CC_CATEGORY_INCIDENT_MANAGEMENT: CloudControlCategory
CC_CATEGORY_IDENTITY_AND_ACCESS_MANAGEMENT: CloudControlCategory
CC_CATEGORY_ENCRYPTION: CloudControlCategory
CC_CATEGORY_LOGS_MANAGEMENT_AND_INFRASTRUCTURE: CloudControlCategory
CC_CATEGORY_HR_ADMIN_AND_PROCESSES: CloudControlCategory
CC_CATEGORY_THIRD_PARTY_AND_SUB_PROCESSOR_MANAGEMENT: CloudControlCategory
CC_CATEGORY_LEGAL_AND_DISCLOSURES: CloudControlCategory
CC_CATEGORY_VULNERABILITY_MANAGEMENT: CloudControlCategory
CC_CATEGORY_PRIVACY: CloudControlCategory
CC_CATEGORY_BCDR: CloudControlCategory
CLOUD_PROVIDER_UNSPECIFIED: CloudProvider
AWS: CloudProvider
AZURE: CloudProvider
GCP: CloudProvider
SEVERITY_UNSPECIFIED: Severity
CRITICAL: Severity
HIGH: Severity
MEDIUM: Severity
LOW: Severity
RULE_ACTION_TYPE_UNSPECIFIED: RuleActionType
RULE_ACTION_TYPE_PREVENTIVE: RuleActionType
RULE_ACTION_TYPE_DETECTIVE: RuleActionType
RULE_ACTION_TYPE_AUDIT: RuleActionType
TARGET_RESOURCE_TYPE_UNSPECIFIED: TargetResourceType
TARGET_RESOURCE_CRM_TYPE_ORG: TargetResourceType
TARGET_RESOURCE_CRM_TYPE_FOLDER: TargetResourceType
TARGET_RESOURCE_CRM_TYPE_PROJECT: TargetResourceType
TARGET_RESOURCE_TYPE_APPLICATION: TargetResourceType

class Framework(_message.Message):
    __slots__ = ('name', 'major_revision_id', 'display_name', 'description', 'type', 'cloud_control_details', 'category', 'supported_cloud_providers', 'supported_target_resource_types', 'supported_enforcement_modes')

    class FrameworkType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FRAMEWORK_TYPE_UNSPECIFIED: _ClassVar[Framework.FrameworkType]
        BUILT_IN: _ClassVar[Framework.FrameworkType]
        CUSTOM: _ClassVar[Framework.FrameworkType]
    FRAMEWORK_TYPE_UNSPECIFIED: Framework.FrameworkType
    BUILT_IN: Framework.FrameworkType
    CUSTOM: Framework.FrameworkType
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLOUD_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TARGET_RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ENFORCEMENT_MODES_FIELD_NUMBER: _ClassVar[int]
    name: str
    major_revision_id: int
    display_name: str
    description: str
    type: Framework.FrameworkType
    cloud_control_details: _containers.RepeatedCompositeFieldContainer[CloudControlDetails]
    category: _containers.RepeatedScalarFieldContainer[FrameworkCategory]
    supported_cloud_providers: _containers.RepeatedScalarFieldContainer[CloudProvider]
    supported_target_resource_types: _containers.RepeatedScalarFieldContainer[TargetResourceType]
    supported_enforcement_modes: _containers.RepeatedScalarFieldContainer[EnforcementMode]

    def __init__(self, name: _Optional[str]=..., major_revision_id: _Optional[int]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., type: _Optional[_Union[Framework.FrameworkType, str]]=..., cloud_control_details: _Optional[_Iterable[_Union[CloudControlDetails, _Mapping]]]=..., category: _Optional[_Iterable[_Union[FrameworkCategory, str]]]=..., supported_cloud_providers: _Optional[_Iterable[_Union[CloudProvider, str]]]=..., supported_target_resource_types: _Optional[_Iterable[_Union[TargetResourceType, str]]]=..., supported_enforcement_modes: _Optional[_Iterable[_Union[EnforcementMode, str]]]=...) -> None:
        ...

class CloudControlDetails(_message.Message):
    __slots__ = ('name', 'major_revision_id', 'parameters')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    name: str
    major_revision_id: int
    parameters: _containers.RepeatedCompositeFieldContainer[Parameter]

    def __init__(self, name: _Optional[str]=..., major_revision_id: _Optional[int]=..., parameters: _Optional[_Iterable[_Union[Parameter, _Mapping]]]=...) -> None:
        ...

class FrameworkReference(_message.Message):
    __slots__ = ('framework', 'major_revision_id')
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    framework: str
    major_revision_id: int

    def __init__(self, framework: _Optional[str]=..., major_revision_id: _Optional[int]=...) -> None:
        ...

class Parameter(_message.Message):
    __slots__ = ('name', 'parameter_value')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    parameter_value: ParamValue

    def __init__(self, name: _Optional[str]=..., parameter_value: _Optional[_Union[ParamValue, _Mapping]]=...) -> None:
        ...

class CloudControl(_message.Message):
    __slots__ = ('name', 'major_revision_id', 'description', 'display_name', 'supported_enforcement_modes', 'parameter_spec', 'rules', 'severity', 'finding_category', 'supported_cloud_providers', 'related_frameworks', 'remediation_steps', 'categories', 'create_time', 'supported_target_resource_types')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_ENFORCEMENT_MODES_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SPEC_FIELD_NUMBER: _ClassVar[int]
    RULES_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    FINDING_CATEGORY_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_CLOUD_PROVIDERS_FIELD_NUMBER: _ClassVar[int]
    RELATED_FRAMEWORKS_FIELD_NUMBER: _ClassVar[int]
    REMEDIATION_STEPS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    SUPPORTED_TARGET_RESOURCE_TYPES_FIELD_NUMBER: _ClassVar[int]
    name: str
    major_revision_id: int
    description: str
    display_name: str
    supported_enforcement_modes: _containers.RepeatedScalarFieldContainer[EnforcementMode]
    parameter_spec: _containers.RepeatedCompositeFieldContainer[ParameterSpec]
    rules: _containers.RepeatedCompositeFieldContainer[Rule]
    severity: Severity
    finding_category: str
    supported_cloud_providers: _containers.RepeatedScalarFieldContainer[CloudProvider]
    related_frameworks: _containers.RepeatedScalarFieldContainer[str]
    remediation_steps: str
    categories: _containers.RepeatedScalarFieldContainer[CloudControlCategory]
    create_time: _timestamp_pb2.Timestamp
    supported_target_resource_types: _containers.RepeatedScalarFieldContainer[TargetResourceType]

    def __init__(self, name: _Optional[str]=..., major_revision_id: _Optional[int]=..., description: _Optional[str]=..., display_name: _Optional[str]=..., supported_enforcement_modes: _Optional[_Iterable[_Union[EnforcementMode, str]]]=..., parameter_spec: _Optional[_Iterable[_Union[ParameterSpec, _Mapping]]]=..., rules: _Optional[_Iterable[_Union[Rule, _Mapping]]]=..., severity: _Optional[_Union[Severity, str]]=..., finding_category: _Optional[str]=..., supported_cloud_providers: _Optional[_Iterable[_Union[CloudProvider, str]]]=..., related_frameworks: _Optional[_Iterable[str]]=..., remediation_steps: _Optional[str]=..., categories: _Optional[_Iterable[_Union[CloudControlCategory, str]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., supported_target_resource_types: _Optional[_Iterable[_Union[TargetResourceType, str]]]=...) -> None:
        ...

class ParameterSpec(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'is_required', 'value_type', 'default_value', 'substitution_rules', 'sub_parameters', 'validation')

    class ValueType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        VALUE_TYPE_UNSPECIFIED: _ClassVar[ParameterSpec.ValueType]
        STRING: _ClassVar[ParameterSpec.ValueType]
        BOOLEAN: _ClassVar[ParameterSpec.ValueType]
        STRINGLIST: _ClassVar[ParameterSpec.ValueType]
        NUMBER: _ClassVar[ParameterSpec.ValueType]
        ONEOF: _ClassVar[ParameterSpec.ValueType]
    VALUE_TYPE_UNSPECIFIED: ParameterSpec.ValueType
    STRING: ParameterSpec.ValueType
    BOOLEAN: ParameterSpec.ValueType
    STRINGLIST: ParameterSpec.ValueType
    NUMBER: ParameterSpec.ValueType
    ONEOF: ParameterSpec.ValueType
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    IS_REQUIRED_FIELD_NUMBER: _ClassVar[int]
    VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_VALUE_FIELD_NUMBER: _ClassVar[int]
    SUBSTITUTION_RULES_FIELD_NUMBER: _ClassVar[int]
    SUB_PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    is_required: bool
    value_type: ParameterSpec.ValueType
    default_value: ParamValue
    substitution_rules: _containers.RepeatedCompositeFieldContainer[ParameterSubstitutionRule]
    sub_parameters: _containers.RepeatedCompositeFieldContainer[ParameterSpec]
    validation: Validation

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., is_required: bool=..., value_type: _Optional[_Union[ParameterSpec.ValueType, str]]=..., default_value: _Optional[_Union[ParamValue, _Mapping]]=..., substitution_rules: _Optional[_Iterable[_Union[ParameterSubstitutionRule, _Mapping]]]=..., sub_parameters: _Optional[_Iterable[_Union[ParameterSpec, _Mapping]]]=..., validation: _Optional[_Union[Validation, _Mapping]]=...) -> None:
        ...

class Validation(_message.Message):
    __slots__ = ('allowed_values', 'int_range', 'regexp_pattern')
    ALLOWED_VALUES_FIELD_NUMBER: _ClassVar[int]
    INT_RANGE_FIELD_NUMBER: _ClassVar[int]
    REGEXP_PATTERN_FIELD_NUMBER: _ClassVar[int]
    allowed_values: AllowedValues
    int_range: IntRange
    regexp_pattern: RegexpPattern

    def __init__(self, allowed_values: _Optional[_Union[AllowedValues, _Mapping]]=..., int_range: _Optional[_Union[IntRange, _Mapping]]=..., regexp_pattern: _Optional[_Union[RegexpPattern, _Mapping]]=...) -> None:
        ...

class AllowedValues(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedCompositeFieldContainer[ParamValue]

    def __init__(self, values: _Optional[_Iterable[_Union[ParamValue, _Mapping]]]=...) -> None:
        ...

class RegexpPattern(_message.Message):
    __slots__ = ('pattern',)
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    pattern: str

    def __init__(self, pattern: _Optional[str]=...) -> None:
        ...

class IntRange(_message.Message):
    __slots__ = ('min', 'max')
    MIN_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    min: int
    max: int

    def __init__(self, min: _Optional[int]=..., max: _Optional[int]=...) -> None:
        ...

class StringList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, values: _Optional[_Iterable[str]]=...) -> None:
        ...

class ParamValue(_message.Message):
    __slots__ = ('string_value', 'bool_value', 'string_list_value', 'number_value', 'oneof_value')
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_LIST_VALUE_FIELD_NUMBER: _ClassVar[int]
    NUMBER_VALUE_FIELD_NUMBER: _ClassVar[int]
    ONEOF_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    bool_value: bool
    string_list_value: StringList
    number_value: float
    oneof_value: Parameter

    def __init__(self, string_value: _Optional[str]=..., bool_value: bool=..., string_list_value: _Optional[_Union[StringList, _Mapping]]=..., number_value: _Optional[float]=..., oneof_value: _Optional[_Union[Parameter, _Mapping]]=...) -> None:
        ...

class ParameterSubstitutionRule(_message.Message):
    __slots__ = ('placeholder_substitution_rule', 'attribute_substitution_rule')
    PLACEHOLDER_SUBSTITUTION_RULE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_SUBSTITUTION_RULE_FIELD_NUMBER: _ClassVar[int]
    placeholder_substitution_rule: PlaceholderSubstitutionRule
    attribute_substitution_rule: AttributeSubstitutionRule

    def __init__(self, placeholder_substitution_rule: _Optional[_Union[PlaceholderSubstitutionRule, _Mapping]]=..., attribute_substitution_rule: _Optional[_Union[AttributeSubstitutionRule, _Mapping]]=...) -> None:
        ...

class AttributeSubstitutionRule(_message.Message):
    __slots__ = ('attribute',)
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attribute: str

    def __init__(self, attribute: _Optional[str]=...) -> None:
        ...

class PlaceholderSubstitutionRule(_message.Message):
    __slots__ = ('attribute',)
    ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    attribute: str

    def __init__(self, attribute: _Optional[str]=...) -> None:
        ...

class Rule(_message.Message):
    __slots__ = ('cel_expression', 'description', 'rule_action_types')
    CEL_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    RULE_ACTION_TYPES_FIELD_NUMBER: _ClassVar[int]
    cel_expression: CELExpression
    description: str
    rule_action_types: _containers.RepeatedScalarFieldContainer[RuleActionType]

    def __init__(self, cel_expression: _Optional[_Union[CELExpression, _Mapping]]=..., description: _Optional[str]=..., rule_action_types: _Optional[_Iterable[_Union[RuleActionType, str]]]=...) -> None:
        ...

class CELExpression(_message.Message):
    __slots__ = ('resource_types_values', 'expression')
    RESOURCE_TYPES_VALUES_FIELD_NUMBER: _ClassVar[int]
    EXPRESSION_FIELD_NUMBER: _ClassVar[int]
    resource_types_values: StringList
    expression: str

    def __init__(self, resource_types_values: _Optional[_Union[StringList, _Mapping]]=..., expression: _Optional[str]=...) -> None:
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