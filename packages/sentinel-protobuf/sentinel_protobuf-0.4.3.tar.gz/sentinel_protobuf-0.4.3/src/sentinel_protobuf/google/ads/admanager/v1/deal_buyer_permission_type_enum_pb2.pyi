from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DealBuyerPermissionTypeEnum(_message.Message):
    __slots__ = ()

    class DealBuyerPermissionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEAL_BUYER_PERMISSION_TYPE_UNSPECIFIED: _ClassVar[DealBuyerPermissionTypeEnum.DealBuyerPermissionType]
        NEGOTIATOR_ONLY: _ClassVar[DealBuyerPermissionTypeEnum.DealBuyerPermissionType]
        BIDDER: _ClassVar[DealBuyerPermissionTypeEnum.DealBuyerPermissionType]
    DEAL_BUYER_PERMISSION_TYPE_UNSPECIFIED: DealBuyerPermissionTypeEnum.DealBuyerPermissionType
    NEGOTIATOR_ONLY: DealBuyerPermissionTypeEnum.DealBuyerPermissionType
    BIDDER: DealBuyerPermissionTypeEnum.DealBuyerPermissionType

    def __init__(self) -> None:
        ...