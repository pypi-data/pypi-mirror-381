from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ThirdPartyBrandSafetyIntegrationPartnerEnum(_message.Message):
    __slots__ = ()

    class ThirdPartyBrandSafetyIntegrationPartner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner]
        UNKNOWN: _ClassVar[ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner]
        DOUBLE_VERIFY: _ClassVar[ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner]
        INTEGRAL_AD_SCIENCE: _ClassVar[ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner]
        ZEFR: _ClassVar[ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner]
    UNSPECIFIED: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    UNKNOWN: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    DOUBLE_VERIFY: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    INTEGRAL_AD_SCIENCE: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    ZEFR: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner

    def __init__(self) -> None:
        ...