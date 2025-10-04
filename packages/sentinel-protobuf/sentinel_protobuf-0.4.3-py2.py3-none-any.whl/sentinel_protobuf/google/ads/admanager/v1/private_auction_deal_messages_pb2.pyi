from google.ads.admanager.v1 import deal_buyer_permission_type_enum_pb2 as _deal_buyer_permission_type_enum_pb2
from google.ads.admanager.v1 import private_marketplace_enums_pb2 as _private_marketplace_enums_pb2
from google.ads.admanager.v1 import size_pb2 as _size_pb2
from google.ads.admanager.v1 import targeting_pb2 as _targeting_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.type import money_pb2 as _money_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PrivateAuctionDeal(_message.Message):
    __slots__ = ('name', 'private_auction_deal_id', 'private_auction_id', 'private_auction_display_name', 'buyer_account_id', 'external_deal_id', 'targeting', 'end_time', 'floor_price', 'creative_sizes', 'status', 'auction_priority_enabled', 'block_override_enabled', 'buyer_permission_type', 'buyer_data', 'create_time', 'update_time')

    class BuyerData(_message.Message):
        __slots__ = ('buyer_emails',)
        BUYER_EMAILS_FIELD_NUMBER: _ClassVar[int]
        buyer_emails: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, buyer_emails: _Optional[_Iterable[str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_AUCTION_DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_AUCTION_ID_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_AUCTION_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BUYER_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_DEAL_ID_FIELD_NUMBER: _ClassVar[int]
    TARGETING_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    FLOOR_PRICE_FIELD_NUMBER: _ClassVar[int]
    CREATIVE_SIZES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    AUCTION_PRIORITY_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BLOCK_OVERRIDE_ENABLED_FIELD_NUMBER: _ClassVar[int]
    BUYER_PERMISSION_TYPE_FIELD_NUMBER: _ClassVar[int]
    BUYER_DATA_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    private_auction_deal_id: int
    private_auction_id: int
    private_auction_display_name: str
    buyer_account_id: int
    external_deal_id: int
    targeting: _targeting_pb2.Targeting
    end_time: _timestamp_pb2.Timestamp
    floor_price: _money_pb2.Money
    creative_sizes: _containers.RepeatedCompositeFieldContainer[_size_pb2.Size]
    status: _private_marketplace_enums_pb2.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus
    auction_priority_enabled: bool
    block_override_enabled: bool
    buyer_permission_type: _deal_buyer_permission_type_enum_pb2.DealBuyerPermissionTypeEnum.DealBuyerPermissionType
    buyer_data: PrivateAuctionDeal.BuyerData
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., private_auction_deal_id: _Optional[int]=..., private_auction_id: _Optional[int]=..., private_auction_display_name: _Optional[str]=..., buyer_account_id: _Optional[int]=..., external_deal_id: _Optional[int]=..., targeting: _Optional[_Union[_targeting_pb2.Targeting, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., floor_price: _Optional[_Union[_money_pb2.Money, _Mapping]]=..., creative_sizes: _Optional[_Iterable[_Union[_size_pb2.Size, _Mapping]]]=..., status: _Optional[_Union[_private_marketplace_enums_pb2.PrivateMarketplaceDealStatusEnum.PrivateMarketplaceDealStatus, str]]=..., auction_priority_enabled: bool=..., block_override_enabled: bool=..., buyer_permission_type: _Optional[_Union[_deal_buyer_permission_type_enum_pb2.DealBuyerPermissionTypeEnum.DealBuyerPermissionType, str]]=..., buyer_data: _Optional[_Union[PrivateAuctionDeal.BuyerData, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...