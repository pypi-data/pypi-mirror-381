from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class PrivateMarketplaceDealStatusEnum(_message.Message):
    __slots__ = ()

    class PrivateMarketplaceDealStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PRIVATE_MARKETPLACE_DEAL_STATUS_UNSPECIFIED: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
        PENDING: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
        ACTIVE: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
        CANCELED: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
        SELLER_PAUSED: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
        BUYER_PAUSED: _ClassVar[PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus]
    PRIVATE_MARKETPLACE_DEAL_STATUS_UNSPECIFIED: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    PENDING: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    ACTIVE: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    CANCELED: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    SELLER_PAUSED: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    BUYER_PAUSED: PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus

    def __init__(self) -> None:
        ...