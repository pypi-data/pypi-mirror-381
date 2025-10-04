from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadCreditIssuanceDecisionEnum(_message.Message):
    __slots__ = ()

    class CreditIssuanceDecision(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
        UNKNOWN: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
        SUCCESS_NOT_REACHED_THRESHOLD: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
        SUCCESS_REACHED_THRESHOLD: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
        FAIL_OVER_THRESHOLD: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
        FAIL_NOT_ELIGIBLE: _ClassVar[LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision]
    UNSPECIFIED: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    UNKNOWN: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    SUCCESS_NOT_REACHED_THRESHOLD: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    SUCCESS_REACHED_THRESHOLD: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    FAIL_OVER_THRESHOLD: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    FAIL_NOT_ELIGIBLE: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision

    def __init__(self) -> None:
        ...