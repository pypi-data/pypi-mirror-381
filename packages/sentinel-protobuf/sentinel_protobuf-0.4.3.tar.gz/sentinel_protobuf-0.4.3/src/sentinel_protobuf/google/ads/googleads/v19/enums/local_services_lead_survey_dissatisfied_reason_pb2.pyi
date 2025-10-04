from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadSurveyDissatisfiedReasonEnum(_message.Message):
    __slots__ = ()

    class SurveyDissatisfiedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        UNKNOWN: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        OTHER_DISSATISFIED_REASON: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        GEO_MISMATCH: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        JOB_TYPE_MISMATCH: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        NOT_READY_TO_BOOK: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        SPAM: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        DUPLICATE: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
        SOLICITATION: _ClassVar[LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason]
    UNSPECIFIED: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    UNKNOWN: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    OTHER_DISSATISFIED_REASON: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    GEO_MISMATCH: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    JOB_TYPE_MISMATCH: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    NOT_READY_TO_BOOK: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    SPAM: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    DUPLICATE: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    SOLICITATION: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason

    def __init__(self) -> None:
        ...