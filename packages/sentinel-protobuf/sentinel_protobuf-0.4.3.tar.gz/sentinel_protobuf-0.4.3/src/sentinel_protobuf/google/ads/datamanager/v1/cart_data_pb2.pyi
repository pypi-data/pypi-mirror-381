from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CartData(_message.Message):
    __slots__ = ('merchant_id', 'merchant_feed_label', 'merchant_feed_language_code', 'transaction_discount', 'items')
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_FEED_LABEL_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_FEED_LANGUAGE_CODE_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_DISCOUNT_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    merchant_id: str
    merchant_feed_label: str
    merchant_feed_language_code: str
    transaction_discount: float
    items: _containers.RepeatedCompositeFieldContainer[Item]

    def __init__(self, merchant_id: _Optional[str]=..., merchant_feed_label: _Optional[str]=..., merchant_feed_language_code: _Optional[str]=..., transaction_discount: _Optional[float]=..., items: _Optional[_Iterable[_Union[Item, _Mapping]]]=...) -> None:
        ...

class Item(_message.Message):
    __slots__ = ('merchant_product_id', 'quantity', 'unit_price')
    MERCHANT_PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    UNIT_PRICE_FIELD_NUMBER: _ClassVar[int]
    merchant_product_id: str
    quantity: int
    unit_price: float

    def __init__(self, merchant_product_id: _Optional[str]=..., quantity: _Optional[int]=..., unit_price: _Optional[float]=...) -> None:
        ...