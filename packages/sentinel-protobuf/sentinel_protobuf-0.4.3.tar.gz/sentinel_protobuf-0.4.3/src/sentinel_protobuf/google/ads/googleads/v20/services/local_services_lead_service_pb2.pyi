from google.ads.googleads.v20.enums import local_services_lead_credit_issuance_decision_pb2 as _local_services_lead_credit_issuance_decision_pb2
from google.ads.googleads.v20.enums import local_services_lead_survey_answer_pb2 as _local_services_lead_survey_answer_pb2
from google.ads.googleads.v20.enums import local_services_lead_survey_dissatisfied_reason_pb2 as _local_services_lead_survey_dissatisfied_reason_pb2
from google.ads.googleads.v20.enums import local_services_lead_survey_satisfied_reason_pb2 as _local_services_lead_survey_satisfied_reason_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AppendLeadConversationRequest(_message.Message):
    __slots__ = ('customer_id', 'conversations')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    CONVERSATIONS_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    conversations: _containers.RepeatedCompositeFieldContainer[Conversation]

    def __init__(self, customer_id: _Optional[str]=..., conversations: _Optional[_Iterable[_Union[Conversation, _Mapping]]]=...) -> None:
        ...

class AppendLeadConversationResponse(_message.Message):
    __slots__ = ('responses',)
    RESPONSES_FIELD_NUMBER: _ClassVar[int]
    responses: _containers.RepeatedCompositeFieldContainer[ConversationOrError]

    def __init__(self, responses: _Optional[_Iterable[_Union[ConversationOrError, _Mapping]]]=...) -> None:
        ...

class Conversation(_message.Message):
    __slots__ = ('local_services_lead', 'text')
    LOCAL_SERVICES_LEAD_FIELD_NUMBER: _ClassVar[int]
    TEXT_FIELD_NUMBER: _ClassVar[int]
    local_services_lead: str
    text: str

    def __init__(self, local_services_lead: _Optional[str]=..., text: _Optional[str]=...) -> None:
        ...

class ConversationOrError(_message.Message):
    __slots__ = ('local_services_lead_conversation', 'partial_failure_error')
    LOCAL_SERVICES_LEAD_CONVERSATION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    local_services_lead_conversation: str
    partial_failure_error: _status_pb2.Status

    def __init__(self, local_services_lead_conversation: _Optional[str]=..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class SurveySatisfied(_message.Message):
    __slots__ = ('survey_satisfied_reason', 'other_reason_comment')
    SURVEY_SATISFIED_REASON_FIELD_NUMBER: _ClassVar[int]
    OTHER_REASON_COMMENT_FIELD_NUMBER: _ClassVar[int]
    survey_satisfied_reason: _local_services_lead_survey_satisfied_reason_pb2.LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    other_reason_comment: str

    def __init__(self, survey_satisfied_reason: _Optional[_Union[_local_services_lead_survey_satisfied_reason_pb2.LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason, str]]=..., other_reason_comment: _Optional[str]=...) -> None:
        ...

class SurveyDissatisfied(_message.Message):
    __slots__ = ('survey_dissatisfied_reason', 'other_reason_comment')
    SURVEY_DISSATISFIED_REASON_FIELD_NUMBER: _ClassVar[int]
    OTHER_REASON_COMMENT_FIELD_NUMBER: _ClassVar[int]
    survey_dissatisfied_reason: _local_services_lead_survey_dissatisfied_reason_pb2.LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    other_reason_comment: str

    def __init__(self, survey_dissatisfied_reason: _Optional[_Union[_local_services_lead_survey_dissatisfied_reason_pb2.LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason, str]]=..., other_reason_comment: _Optional[str]=...) -> None:
        ...

class ProvideLeadFeedbackRequest(_message.Message):
    __slots__ = ('resource_name', 'survey_answer', 'survey_satisfied', 'survey_dissatisfied')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    SURVEY_ANSWER_FIELD_NUMBER: _ClassVar[int]
    SURVEY_SATISFIED_FIELD_NUMBER: _ClassVar[int]
    SURVEY_DISSATISFIED_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    survey_answer: _local_services_lead_survey_answer_pb2.LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    survey_satisfied: SurveySatisfied
    survey_dissatisfied: SurveyDissatisfied

    def __init__(self, resource_name: _Optional[str]=..., survey_answer: _Optional[_Union[_local_services_lead_survey_answer_pb2.LocalServicesLeadSurveyAnswerEnum.SurveyAnswer, str]]=..., survey_satisfied: _Optional[_Union[SurveySatisfied, _Mapping]]=..., survey_dissatisfied: _Optional[_Union[SurveyDissatisfied, _Mapping]]=...) -> None:
        ...

class ProvideLeadFeedbackResponse(_message.Message):
    __slots__ = ('credit_issuance_decision',)
    CREDIT_ISSUANCE_DECISION_FIELD_NUMBER: _ClassVar[int]
    credit_issuance_decision: _local_services_lead_credit_issuance_decision_pb2.LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision

    def __init__(self, credit_issuance_decision: _Optional[_Union[_local_services_lead_credit_issuance_decision_pb2.LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision, str]]=...) -> None:
        ...