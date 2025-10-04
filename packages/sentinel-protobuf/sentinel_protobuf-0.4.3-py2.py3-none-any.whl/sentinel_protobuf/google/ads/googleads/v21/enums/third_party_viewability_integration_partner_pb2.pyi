from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ThirdPartyViewabilityIntegrationPartnerEnum(_message.Message):
    __slots__ = ()

    class ThirdPartyViewabilityIntegrationPartner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner]
        UNKNOWN: _ClassVar[ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner]
        DOUBLE_VERIFY: _ClassVar[ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner]
        INTEGRAL_AD_SCIENCE: _ClassVar[ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner]
    UNSPECIFIED: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    UNKNOWN: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    DOUBLE_VERIFY: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    INTEGRAL_AD_SCIENCE: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner

    def __init__(self) -> None:
        ...