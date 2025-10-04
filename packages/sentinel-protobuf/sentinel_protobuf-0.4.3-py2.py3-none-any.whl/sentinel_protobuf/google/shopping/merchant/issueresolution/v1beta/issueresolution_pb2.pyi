from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Severity(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEVERITY_UNSPECIFIED: _ClassVar[Severity]
    ERROR: _ClassVar[Severity]
    WARNING: _ClassVar[Severity]
    INFO: _ClassVar[Severity]

class ContentOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CONTENT_OPTION_UNSPECIFIED: _ClassVar[ContentOption]
    PRE_RENDERED_HTML: _ClassVar[ContentOption]

class UserInputActionRenderingOption(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED: _ClassVar[UserInputActionRenderingOption]
    REDIRECT_TO_MERCHANT_CENTER: _ClassVar[UserInputActionRenderingOption]
    BUILT_IN_USER_INPUT_ACTIONS: _ClassVar[UserInputActionRenderingOption]
SEVERITY_UNSPECIFIED: Severity
ERROR: Severity
WARNING: Severity
INFO: Severity
CONTENT_OPTION_UNSPECIFIED: ContentOption
PRE_RENDERED_HTML: ContentOption
USER_INPUT_ACTION_RENDERING_OPTION_UNSPECIFIED: UserInputActionRenderingOption
REDIRECT_TO_MERCHANT_CENTER: UserInputActionRenderingOption
BUILT_IN_USER_INPUT_ACTIONS: UserInputActionRenderingOption

class RenderAccountIssuesResponse(_message.Message):
    __slots__ = ('rendered_issues',)
    RENDERED_ISSUES_FIELD_NUMBER: _ClassVar[int]
    rendered_issues: _containers.RepeatedCompositeFieldContainer[RenderedIssue]

    def __init__(self, rendered_issues: _Optional[_Iterable[_Union[RenderedIssue, _Mapping]]]=...) -> None:
        ...

class RenderAccountIssuesRequest(_message.Message):
    __slots__ = ('name', 'language_code', 'time_zone', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    time_zone: str
    payload: RenderIssuesRequestPayload

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=..., time_zone: _Optional[str]=..., payload: _Optional[_Union[RenderIssuesRequestPayload, _Mapping]]=...) -> None:
        ...

class RenderIssuesRequestPayload(_message.Message):
    __slots__ = ('content_option', 'user_input_action_option')
    CONTENT_OPTION_FIELD_NUMBER: _ClassVar[int]
    USER_INPUT_ACTION_OPTION_FIELD_NUMBER: _ClassVar[int]
    content_option: ContentOption
    user_input_action_option: UserInputActionRenderingOption

    def __init__(self, content_option: _Optional[_Union[ContentOption, str]]=..., user_input_action_option: _Optional[_Union[UserInputActionRenderingOption, str]]=...) -> None:
        ...

class RenderProductIssuesResponse(_message.Message):
    __slots__ = ('rendered_issues',)
    RENDERED_ISSUES_FIELD_NUMBER: _ClassVar[int]
    rendered_issues: _containers.RepeatedCompositeFieldContainer[RenderedIssue]

    def __init__(self, rendered_issues: _Optional[_Iterable[_Union[RenderedIssue, _Mapping]]]=...) -> None:
        ...

class RenderProductIssuesRequest(_message.Message):
    __slots__ = ('name', 'language_code', 'time_zone', 'payload')
    NAME_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    language_code: str
    time_zone: str
    payload: RenderIssuesRequestPayload

    def __init__(self, name: _Optional[str]=..., language_code: _Optional[str]=..., time_zone: _Optional[str]=..., payload: _Optional[_Union[RenderIssuesRequestPayload, _Mapping]]=...) -> None:
        ...

class RenderedIssue(_message.Message):
    __slots__ = ('prerendered_content', 'prerendered_out_of_court_dispute_settlement', 'title', 'impact', 'actions')
    PRERENDERED_CONTENT_FIELD_NUMBER: _ClassVar[int]
    PRERENDERED_OUT_OF_COURT_DISPUTE_SETTLEMENT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    IMPACT_FIELD_NUMBER: _ClassVar[int]
    ACTIONS_FIELD_NUMBER: _ClassVar[int]
    prerendered_content: str
    prerendered_out_of_court_dispute_settlement: str
    title: str
    impact: Impact
    actions: _containers.RepeatedCompositeFieldContainer[Action]

    def __init__(self, prerendered_content: _Optional[str]=..., prerendered_out_of_court_dispute_settlement: _Optional[str]=..., title: _Optional[str]=..., impact: _Optional[_Union[Impact, _Mapping]]=..., actions: _Optional[_Iterable[_Union[Action, _Mapping]]]=...) -> None:
        ...

class Impact(_message.Message):
    __slots__ = ('message', 'severity', 'breakdowns')
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEVERITY_FIELD_NUMBER: _ClassVar[int]
    BREAKDOWNS_FIELD_NUMBER: _ClassVar[int]
    message: str
    severity: Severity
    breakdowns: _containers.RepeatedCompositeFieldContainer[Breakdown]

    def __init__(self, message: _Optional[str]=..., severity: _Optional[_Union[Severity, str]]=..., breakdowns: _Optional[_Iterable[_Union[Breakdown, _Mapping]]]=...) -> None:
        ...

class Breakdown(_message.Message):
    __slots__ = ('regions', 'details')

    class Region(_message.Message):
        __slots__ = ('code', 'name')
        CODE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        code: str
        name: str

        def __init__(self, code: _Optional[str]=..., name: _Optional[str]=...) -> None:
            ...
    REGIONS_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    regions: _containers.RepeatedCompositeFieldContainer[Breakdown.Region]
    details: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, regions: _Optional[_Iterable[_Union[Breakdown.Region, _Mapping]]]=..., details: _Optional[_Iterable[str]]=...) -> None:
        ...

class Action(_message.Message):
    __slots__ = ('builtin_simple_action', 'external_action', 'builtin_user_input_action', 'button_label', 'is_available', 'reasons')

    class Reason(_message.Message):
        __slots__ = ('message', 'detail', 'action')
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        DETAIL_FIELD_NUMBER: _ClassVar[int]
        ACTION_FIELD_NUMBER: _ClassVar[int]
        message: str
        detail: str
        action: Action

        def __init__(self, message: _Optional[str]=..., detail: _Optional[str]=..., action: _Optional[_Union[Action, _Mapping]]=...) -> None:
            ...
    BUILTIN_SIMPLE_ACTION_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACTION_FIELD_NUMBER: _ClassVar[int]
    BUILTIN_USER_INPUT_ACTION_FIELD_NUMBER: _ClassVar[int]
    BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    REASONS_FIELD_NUMBER: _ClassVar[int]
    builtin_simple_action: BuiltInSimpleAction
    external_action: ExternalAction
    builtin_user_input_action: BuiltInUserInputAction
    button_label: str
    is_available: bool
    reasons: _containers.RepeatedCompositeFieldContainer[Action.Reason]

    def __init__(self, builtin_simple_action: _Optional[_Union[BuiltInSimpleAction, _Mapping]]=..., external_action: _Optional[_Union[ExternalAction, _Mapping]]=..., builtin_user_input_action: _Optional[_Union[BuiltInUserInputAction, _Mapping]]=..., button_label: _Optional[str]=..., is_available: bool=..., reasons: _Optional[_Iterable[_Union[Action.Reason, _Mapping]]]=...) -> None:
        ...

class BuiltInSimpleAction(_message.Message):
    __slots__ = ('type', 'attribute_code', 'additional_content')

    class BuiltInSimpleActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        VERIFY_PHONE: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        CLAIM_WEBSITE: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        ADD_PRODUCTS: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        ADD_CONTACT_INFO: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        LINK_ADS_ACCOUNT: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        ADD_BUSINESS_REGISTRATION_NUMBER: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        EDIT_ITEM_ATTRIBUTE: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        FIX_ACCOUNT_ISSUE: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
        SHOW_ADDITIONAL_CONTENT: _ClassVar[BuiltInSimpleAction.BuiltInSimpleActionType]
    BUILT_IN_SIMPLE_ACTION_TYPE_UNSPECIFIED: BuiltInSimpleAction.BuiltInSimpleActionType
    VERIFY_PHONE: BuiltInSimpleAction.BuiltInSimpleActionType
    CLAIM_WEBSITE: BuiltInSimpleAction.BuiltInSimpleActionType
    ADD_PRODUCTS: BuiltInSimpleAction.BuiltInSimpleActionType
    ADD_CONTACT_INFO: BuiltInSimpleAction.BuiltInSimpleActionType
    LINK_ADS_ACCOUNT: BuiltInSimpleAction.BuiltInSimpleActionType
    ADD_BUSINESS_REGISTRATION_NUMBER: BuiltInSimpleAction.BuiltInSimpleActionType
    EDIT_ITEM_ATTRIBUTE: BuiltInSimpleAction.BuiltInSimpleActionType
    FIX_ACCOUNT_ISSUE: BuiltInSimpleAction.BuiltInSimpleActionType
    SHOW_ADDITIONAL_CONTENT: BuiltInSimpleAction.BuiltInSimpleActionType

    class AdditionalContent(_message.Message):
        __slots__ = ('title', 'paragraphs')
        TITLE_FIELD_NUMBER: _ClassVar[int]
        PARAGRAPHS_FIELD_NUMBER: _ClassVar[int]
        title: str
        paragraphs: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, title: _Optional[str]=..., paragraphs: _Optional[_Iterable[str]]=...) -> None:
            ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ATTRIBUTE_CODE_FIELD_NUMBER: _ClassVar[int]
    ADDITIONAL_CONTENT_FIELD_NUMBER: _ClassVar[int]
    type: BuiltInSimpleAction.BuiltInSimpleActionType
    attribute_code: str
    additional_content: BuiltInSimpleAction.AdditionalContent

    def __init__(self, type: _Optional[_Union[BuiltInSimpleAction.BuiltInSimpleActionType, str]]=..., attribute_code: _Optional[str]=..., additional_content: _Optional[_Union[BuiltInSimpleAction.AdditionalContent, _Mapping]]=...) -> None:
        ...

class BuiltInUserInputAction(_message.Message):
    __slots__ = ('action_context', 'flows')
    ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    FLOWS_FIELD_NUMBER: _ClassVar[int]
    action_context: str
    flows: _containers.RepeatedCompositeFieldContainer[ActionFlow]

    def __init__(self, action_context: _Optional[str]=..., flows: _Optional[_Iterable[_Union[ActionFlow, _Mapping]]]=...) -> None:
        ...

class ActionFlow(_message.Message):
    __slots__ = ('id', 'label', 'inputs', 'dialog_title', 'dialog_message', 'dialog_callout', 'dialog_button_label')
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    DIALOG_TITLE_FIELD_NUMBER: _ClassVar[int]
    DIALOG_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DIALOG_CALLOUT_FIELD_NUMBER: _ClassVar[int]
    DIALOG_BUTTON_LABEL_FIELD_NUMBER: _ClassVar[int]
    id: str
    label: str
    inputs: _containers.RepeatedCompositeFieldContainer[InputField]
    dialog_title: str
    dialog_message: TextWithTooltip
    dialog_callout: Callout
    dialog_button_label: str

    def __init__(self, id: _Optional[str]=..., label: _Optional[str]=..., inputs: _Optional[_Iterable[_Union[InputField, _Mapping]]]=..., dialog_title: _Optional[str]=..., dialog_message: _Optional[_Union[TextWithTooltip, _Mapping]]=..., dialog_callout: _Optional[_Union[Callout, _Mapping]]=..., dialog_button_label: _Optional[str]=...) -> None:
        ...

class InputField(_message.Message):
    __slots__ = ('text_input', 'choice_input', 'checkbox_input', 'id', 'label', 'required')

    class TextInput(_message.Message):
        __slots__ = ('type', 'additional_info', 'format_info', 'aria_label')

        class TextInputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TEXT_INPUT_TYPE_UNSPECIFIED: _ClassVar[InputField.TextInput.TextInputType]
            GENERIC_SHORT_TEXT: _ClassVar[InputField.TextInput.TextInputType]
            GENERIC_LONG_TEXT: _ClassVar[InputField.TextInput.TextInputType]
        TEXT_INPUT_TYPE_UNSPECIFIED: InputField.TextInput.TextInputType
        GENERIC_SHORT_TEXT: InputField.TextInput.TextInputType
        GENERIC_LONG_TEXT: InputField.TextInput.TextInputType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_INFO_FIELD_NUMBER: _ClassVar[int]
        FORMAT_INFO_FIELD_NUMBER: _ClassVar[int]
        ARIA_LABEL_FIELD_NUMBER: _ClassVar[int]
        type: InputField.TextInput.TextInputType
        additional_info: TextWithTooltip
        format_info: str
        aria_label: str

        def __init__(self, type: _Optional[_Union[InputField.TextInput.TextInputType, str]]=..., additional_info: _Optional[_Union[TextWithTooltip, _Mapping]]=..., format_info: _Optional[str]=..., aria_label: _Optional[str]=...) -> None:
            ...

    class ChoiceInput(_message.Message):
        __slots__ = ('options',)

        class ChoiceInputOption(_message.Message):
            __slots__ = ('id', 'label', 'additional_input')
            ID_FIELD_NUMBER: _ClassVar[int]
            LABEL_FIELD_NUMBER: _ClassVar[int]
            ADDITIONAL_INPUT_FIELD_NUMBER: _ClassVar[int]
            id: str
            label: TextWithTooltip
            additional_input: InputField

            def __init__(self, id: _Optional[str]=..., label: _Optional[_Union[TextWithTooltip, _Mapping]]=..., additional_input: _Optional[_Union[InputField, _Mapping]]=...) -> None:
                ...
        OPTIONS_FIELD_NUMBER: _ClassVar[int]
        options: _containers.RepeatedCompositeFieldContainer[InputField.ChoiceInput.ChoiceInputOption]

        def __init__(self, options: _Optional[_Iterable[_Union[InputField.ChoiceInput.ChoiceInputOption, _Mapping]]]=...) -> None:
            ...

    class CheckboxInput(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...
    TEXT_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHOICE_INPUT_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_INPUT_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_FIELD_NUMBER: _ClassVar[int]
    text_input: InputField.TextInput
    choice_input: InputField.ChoiceInput
    checkbox_input: InputField.CheckboxInput
    id: str
    label: TextWithTooltip
    required: bool

    def __init__(self, text_input: _Optional[_Union[InputField.TextInput, _Mapping]]=..., choice_input: _Optional[_Union[InputField.ChoiceInput, _Mapping]]=..., checkbox_input: _Optional[_Union[InputField.CheckboxInput, _Mapping]]=..., id: _Optional[str]=..., label: _Optional[_Union[TextWithTooltip, _Mapping]]=..., required: bool=...) -> None:
        ...

class TextWithTooltip(_message.Message):
    __slots__ = ('simple_value', 'simple_tooltip_value', 'tooltip_icon_style')

    class TooltipIconStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOOLTIP_ICON_STYLE_UNSPECIFIED: _ClassVar[TextWithTooltip.TooltipIconStyle]
        INFO: _ClassVar[TextWithTooltip.TooltipIconStyle]
        QUESTION: _ClassVar[TextWithTooltip.TooltipIconStyle]
    TOOLTIP_ICON_STYLE_UNSPECIFIED: TextWithTooltip.TooltipIconStyle
    INFO: TextWithTooltip.TooltipIconStyle
    QUESTION: TextWithTooltip.TooltipIconStyle
    SIMPLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    SIMPLE_TOOLTIP_VALUE_FIELD_NUMBER: _ClassVar[int]
    TOOLTIP_ICON_STYLE_FIELD_NUMBER: _ClassVar[int]
    simple_value: str
    simple_tooltip_value: str
    tooltip_icon_style: TextWithTooltip.TooltipIconStyle

    def __init__(self, simple_value: _Optional[str]=..., simple_tooltip_value: _Optional[str]=..., tooltip_icon_style: _Optional[_Union[TextWithTooltip.TooltipIconStyle, str]]=...) -> None:
        ...

class Callout(_message.Message):
    __slots__ = ('style_hint', 'full_message')

    class CalloutStyleHint(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CALLOUT_STYLE_HINT_UNSPECIFIED: _ClassVar[Callout.CalloutStyleHint]
        ERROR: _ClassVar[Callout.CalloutStyleHint]
        WARNING: _ClassVar[Callout.CalloutStyleHint]
        INFO: _ClassVar[Callout.CalloutStyleHint]
    CALLOUT_STYLE_HINT_UNSPECIFIED: Callout.CalloutStyleHint
    ERROR: Callout.CalloutStyleHint
    WARNING: Callout.CalloutStyleHint
    INFO: Callout.CalloutStyleHint
    STYLE_HINT_FIELD_NUMBER: _ClassVar[int]
    FULL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    style_hint: Callout.CalloutStyleHint
    full_message: TextWithTooltip

    def __init__(self, style_hint: _Optional[_Union[Callout.CalloutStyleHint, str]]=..., full_message: _Optional[_Union[TextWithTooltip, _Mapping]]=...) -> None:
        ...

class ExternalAction(_message.Message):
    __slots__ = ('type', 'uri')

    class ExternalActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        EXTERNAL_ACTION_TYPE_UNSPECIFIED: _ClassVar[ExternalAction.ExternalActionType]
        REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER: _ClassVar[ExternalAction.ExternalActionType]
        REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER: _ClassVar[ExternalAction.ExternalActionType]
        LEGAL_APPEAL_IN_HELP_CENTER: _ClassVar[ExternalAction.ExternalActionType]
        VERIFY_IDENTITY_IN_MERCHANT_CENTER: _ClassVar[ExternalAction.ExternalActionType]
    EXTERNAL_ACTION_TYPE_UNSPECIFIED: ExternalAction.ExternalActionType
    REVIEW_PRODUCT_ISSUE_IN_MERCHANT_CENTER: ExternalAction.ExternalActionType
    REVIEW_ACCOUNT_ISSUE_IN_MERCHANT_CENTER: ExternalAction.ExternalActionType
    LEGAL_APPEAL_IN_HELP_CENTER: ExternalAction.ExternalActionType
    VERIFY_IDENTITY_IN_MERCHANT_CENTER: ExternalAction.ExternalActionType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    type: ExternalAction.ExternalActionType
    uri: str

    def __init__(self, type: _Optional[_Union[ExternalAction.ExternalActionType, str]]=..., uri: _Optional[str]=...) -> None:
        ...

class TriggerActionRequest(_message.Message):
    __slots__ = ('name', 'payload', 'language_code')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    payload: TriggerActionPayload
    language_code: str

    def __init__(self, name: _Optional[str]=..., payload: _Optional[_Union[TriggerActionPayload, _Mapping]]=..., language_code: _Optional[str]=...) -> None:
        ...

class TriggerActionPayload(_message.Message):
    __slots__ = ('action_context', 'action_input')
    ACTION_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    ACTION_INPUT_FIELD_NUMBER: _ClassVar[int]
    action_context: str
    action_input: ActionInput

    def __init__(self, action_context: _Optional[str]=..., action_input: _Optional[_Union[ActionInput, _Mapping]]=...) -> None:
        ...

class TriggerActionResponse(_message.Message):
    __slots__ = ('message',)
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message: str

    def __init__(self, message: _Optional[str]=...) -> None:
        ...

class ActionInput(_message.Message):
    __slots__ = ('action_flow_id', 'input_values')
    ACTION_FLOW_ID_FIELD_NUMBER: _ClassVar[int]
    INPUT_VALUES_FIELD_NUMBER: _ClassVar[int]
    action_flow_id: str
    input_values: _containers.RepeatedCompositeFieldContainer[InputValue]

    def __init__(self, action_flow_id: _Optional[str]=..., input_values: _Optional[_Iterable[_Union[InputValue, _Mapping]]]=...) -> None:
        ...

class InputValue(_message.Message):
    __slots__ = ('text_input_value', 'choice_input_value', 'checkbox_input_value', 'input_field_id')

    class TextInputValue(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...

    class ChoiceInputValue(_message.Message):
        __slots__ = ('choice_input_option_id',)
        CHOICE_INPUT_OPTION_ID_FIELD_NUMBER: _ClassVar[int]
        choice_input_option_id: str

        def __init__(self, choice_input_option_id: _Optional[str]=...) -> None:
            ...

    class CheckboxInputValue(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: bool

        def __init__(self, value: bool=...) -> None:
            ...
    TEXT_INPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHOICE_INPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    CHECKBOX_INPUT_VALUE_FIELD_NUMBER: _ClassVar[int]
    INPUT_FIELD_ID_FIELD_NUMBER: _ClassVar[int]
    text_input_value: InputValue.TextInputValue
    choice_input_value: InputValue.ChoiceInputValue
    checkbox_input_value: InputValue.CheckboxInputValue
    input_field_id: str

    def __init__(self, text_input_value: _Optional[_Union[InputValue.TextInputValue, _Mapping]]=..., choice_input_value: _Optional[_Union[InputValue.ChoiceInputValue, _Mapping]]=..., checkbox_input_value: _Optional[_Union[InputValue.CheckboxInputValue, _Mapping]]=..., input_field_id: _Optional[str]=...) -> None:
        ...