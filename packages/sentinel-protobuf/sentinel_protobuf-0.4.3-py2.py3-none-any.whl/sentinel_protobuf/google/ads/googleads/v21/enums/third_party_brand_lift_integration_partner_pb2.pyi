from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class ThirdPartyBrandLiftIntegrationPartnerEnum(_message.Message):
    __slots__ = ()

    class ThirdPartyBrandLiftIntegrationPartner(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
        UNKNOWN: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
        KANTAR_MILLWARD_BROWN: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
        DYNATA: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
        INTAGE: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
        MACROMILL: _ClassVar[ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner]
    UNSPECIFIED: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    UNKNOWN: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    KANTAR_MILLWARD_BROWN: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    DYNATA: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    INTAGE: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    MACROMILL: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner

    def __init__(self) -> None:
        ...