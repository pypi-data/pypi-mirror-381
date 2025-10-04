from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class LocalServicesLeadSurveySatisfiedReasonEnum(_message.Message):
    __slots__ = ()

    class SurveySatisfiedReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        UNKNOWN: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        OTHER_SATISFIED_REASON: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        BOOKED_CUSTOMER: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        LIKELY_BOOKED_CUSTOMER: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        SERVICE_RELATED: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
        HIGH_VALUE_SERVICE: _ClassVar[LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason]
    UNSPECIFIED: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    UNKNOWN: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    OTHER_SATISFIED_REASON: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    BOOKED_CUSTOMER: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    LIKELY_BOOKED_CUSTOMER: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    SERVICE_RELATED: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    HIGH_VALUE_SERVICE: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason

    def __init__(self) -> None:
        ...