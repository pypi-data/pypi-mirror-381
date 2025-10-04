from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LocalInventoryAttributes(_message.Message):
    __slots__ = ('price', 'sale_price', 'sale_price_effective_date', 'availability', 'quantity', 'pickup_method', 'pickup_sla', 'instore_product_location')

    class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED: _ClassVar[LocalInventoryAttributes.Availability]
        IN_STOCK: _ClassVar[LocalInventoryAttributes.Availability]
        LIMITED_AVAILABILITY: _ClassVar[LocalInventoryAttributes.Availability]
        ON_DISPLAY_TO_ORDER: _ClassVar[LocalInventoryAttributes.Availability]
        OUT_OF_STOCK: _ClassVar[LocalInventoryAttributes.Availability]
    LOCAL_INVENTORY_AVAILABILITY_UNSPECIFIED: LocalInventoryAttributes.Availability
    IN_STOCK: LocalInventoryAttributes.Availability
    LIMITED_AVAILABILITY: LocalInventoryAttributes.Availability
    ON_DISPLAY_TO_ORDER: LocalInventoryAttributes.Availability
    OUT_OF_STOCK: LocalInventoryAttributes.Availability

    class PickupMethod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PICKUP_METHOD_UNSPECIFIED: _ClassVar[LocalInventoryAttributes.PickupMethod]
        BUY: _ClassVar[LocalInventoryAttributes.PickupMethod]
        RESERVE: _ClassVar[LocalInventoryAttributes.PickupMethod]
        SHIP_TO_STORE: _ClassVar[LocalInventoryAttributes.PickupMethod]
        NOT_SUPPORTED: _ClassVar[LocalInventoryAttributes.PickupMethod]
    PICKUP_METHOD_UNSPECIFIED: LocalInventoryAttributes.PickupMethod
    BUY: LocalInventoryAttributes.PickupMethod
    RESERVE: LocalInventoryAttributes.PickupMethod
    SHIP_TO_STORE: LocalInventoryAttributes.PickupMethod
    NOT_SUPPORTED: LocalInventoryAttributes.PickupMethod

    class PickupSla(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PICKUP_SLA_UNSPECIFIED: _ClassVar[LocalInventoryAttributes.PickupSla]
        SAME_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        NEXT_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        TWO_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        THREE_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        FOUR_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        FIVE_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        SIX_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        SEVEN_DAY: _ClassVar[LocalInventoryAttributes.PickupSla]
        MULTI_WEEK: _ClassVar[LocalInventoryAttributes.PickupSla]
    PICKUP_SLA_UNSPECIFIED: LocalInventoryAttributes.PickupSla
    SAME_DAY: LocalInventoryAttributes.PickupSla
    NEXT_DAY: LocalInventoryAttributes.PickupSla
    TWO_DAY: LocalInventoryAttributes.PickupSla
    THREE_DAY: LocalInventoryAttributes.PickupSla
    FOUR_DAY: LocalInventoryAttributes.PickupSla
    FIVE_DAY: LocalInventoryAttributes.PickupSla
    SIX_DAY: LocalInventoryAttributes.PickupSla
    SEVEN_DAY: LocalInventoryAttributes.PickupSla
    MULTI_WEEK: LocalInventoryAttributes.PickupSla
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    QUANTITY_FIELD_NUMBER: _ClassVar[int]
    PICKUP_METHOD_FIELD_NUMBER: _ClassVar[int]
    PICKUP_SLA_FIELD_NUMBER: _ClassVar[int]
    INSTORE_PRODUCT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    price: _types_pb2.Price
    sale_price: _types_pb2.Price
    sale_price_effective_date: _interval_pb2.Interval
    availability: LocalInventoryAttributes.Availability
    quantity: int
    pickup_method: LocalInventoryAttributes.PickupMethod
    pickup_sla: LocalInventoryAttributes.PickupSla
    instore_product_location: str

    def __init__(self, price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sale_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sale_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., availability: _Optional[_Union[LocalInventoryAttributes.Availability, str]]=..., quantity: _Optional[int]=..., pickup_method: _Optional[_Union[LocalInventoryAttributes.PickupMethod, str]]=..., pickup_sla: _Optional[_Union[LocalInventoryAttributes.PickupSla, str]]=..., instore_product_location: _Optional[str]=...) -> None:
        ...

class RegionalInventoryAttributes(_message.Message):
    __slots__ = ('price', 'sale_price', 'sale_price_effective_date', 'availability')

    class Availability(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED: _ClassVar[RegionalInventoryAttributes.Availability]
        IN_STOCK: _ClassVar[RegionalInventoryAttributes.Availability]
        OUT_OF_STOCK: _ClassVar[RegionalInventoryAttributes.Availability]
    REGIONAL_INVENTORY_AVAILABILITY_UNSPECIFIED: RegionalInventoryAttributes.Availability
    IN_STOCK: RegionalInventoryAttributes.Availability
    OUT_OF_STOCK: RegionalInventoryAttributes.Availability
    PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_FIELD_NUMBER: _ClassVar[int]
    SALE_PRICE_EFFECTIVE_DATE_FIELD_NUMBER: _ClassVar[int]
    AVAILABILITY_FIELD_NUMBER: _ClassVar[int]
    price: _types_pb2.Price
    sale_price: _types_pb2.Price
    sale_price_effective_date: _interval_pb2.Interval
    availability: RegionalInventoryAttributes.Availability

    def __init__(self, price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sale_price: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., sale_price_effective_date: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., availability: _Optional[_Union[RegionalInventoryAttributes.Availability, str]]=...) -> None:
        ...