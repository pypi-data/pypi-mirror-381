from google.ads.admanager.v1 import private_auction_messages_pb2 as _private_auction_messages_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetPrivateAuctionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPrivateAuctionsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by', 'skip')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    SKIP_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str
    skip: int

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=..., skip: _Optional[int]=...) -> None:
        ...

class ListPrivateAuctionsResponse(_message.Message):
    __slots__ = ('private_auctions', 'next_page_token', 'total_size')
    PRIVATE_AUCTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TOTAL_SIZE_FIELD_NUMBER: _ClassVar[int]
    private_auctions: _containers.RepeatedCompositeFieldContainer[_private_auction_messages_pb2.PrivateAuction]
    next_page_token: str
    total_size: int

    def __init__(self, private_auctions: _Optional[_Iterable[_Union[_private_auction_messages_pb2.PrivateAuction, _Mapping]]]=..., next_page_token: _Optional[str]=..., total_size: _Optional[int]=...) -> None:
        ...

class CreatePrivateAuctionRequest(_message.Message):
    __slots__ = ('parent', 'private_auction')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_AUCTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    private_auction: _private_auction_messages_pb2.PrivateAuction

    def __init__(self, parent: _Optional[str]=..., private_auction: _Optional[_Union[_private_auction_messages_pb2.PrivateAuction, _Mapping]]=...) -> None:
        ...

class UpdatePrivateAuctionRequest(_message.Message):
    __slots__ = ('private_auction', 'update_mask')
    PRIVATE_AUCTION_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    private_auction: _private_auction_messages_pb2.PrivateAuction
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, private_auction: _Optional[_Union[_private_auction_messages_pb2.PrivateAuction, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...