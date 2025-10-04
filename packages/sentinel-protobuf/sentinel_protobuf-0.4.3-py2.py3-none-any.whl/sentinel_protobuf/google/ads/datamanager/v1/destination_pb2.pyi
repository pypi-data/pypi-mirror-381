from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Product(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PRODUCT_UNSPECIFIED: _ClassVar[Product]
    GOOGLE_ADS: _ClassVar[Product]
    DISPLAY_VIDEO_PARTNER: _ClassVar[Product]
    DISPLAY_VIDEO_ADVERTISER: _ClassVar[Product]
    DATA_PARTNER: _ClassVar[Product]
PRODUCT_UNSPECIFIED: Product
GOOGLE_ADS: Product
DISPLAY_VIDEO_PARTNER: Product
DISPLAY_VIDEO_ADVERTISER: Product
DATA_PARTNER: Product

class Destination(_message.Message):
    __slots__ = ('reference', 'login_account', 'linked_account', 'operating_account', 'product_destination_id')
    REFERENCE_FIELD_NUMBER: _ClassVar[int]
    LOGIN_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    LINKED_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    OPERATING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    PRODUCT_DESTINATION_ID_FIELD_NUMBER: _ClassVar[int]
    reference: str
    login_account: ProductAccount
    linked_account: ProductAccount
    operating_account: ProductAccount
    product_destination_id: str

    def __init__(self, reference: _Optional[str]=..., login_account: _Optional[_Union[ProductAccount, _Mapping]]=..., linked_account: _Optional[_Union[ProductAccount, _Mapping]]=..., operating_account: _Optional[_Union[ProductAccount, _Mapping]]=..., product_destination_id: _Optional[str]=...) -> None:
        ...

class ProductAccount(_message.Message):
    __slots__ = ('product', 'account_id')
    PRODUCT_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    product: Product
    account_id: str

    def __init__(self, product: _Optional[_Union[Product, str]]=..., account_id: _Optional[str]=...) -> None:
        ...