from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.type import datetime_pb2 as _datetime_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateOrderTrackingSignalRequest(_message.Message):
    __slots__ = ('parent', 'order_tracking_signal_id', 'order_tracking_signal')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_TRACKING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_TRACKING_SIGNAL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    order_tracking_signal_id: str
    order_tracking_signal: OrderTrackingSignal

    def __init__(self, parent: _Optional[str]=..., order_tracking_signal_id: _Optional[str]=..., order_tracking_signal: _Optional[_Union[OrderTrackingSignal, _Mapping]]=...) -> None:
        ...

class OrderTrackingSignal(_message.Message):
    __slots__ = ('order_tracking_signal_id', 'merchant_id', 'order_created_time', 'order_id', 'shipping_info', 'line_items', 'shipment_line_item_mapping', 'customer_shipping_fee', 'delivery_postal_code', 'delivery_region_code')

    class ShippingInfo(_message.Message):
        __slots__ = ('shipment_id', 'tracking_id', 'carrier', 'carrier_service', 'shipped_time', 'earliest_delivery_promise_time', 'latest_delivery_promise_time', 'actual_delivery_time', 'shipping_status', 'origin_postal_code', 'origin_region_code')

        class ShippingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SHIPPING_STATE_UNSPECIFIED: _ClassVar[OrderTrackingSignal.ShippingInfo.ShippingState]
            SHIPPED: _ClassVar[OrderTrackingSignal.ShippingInfo.ShippingState]
            DELIVERED: _ClassVar[OrderTrackingSignal.ShippingInfo.ShippingState]
        SHIPPING_STATE_UNSPECIFIED: OrderTrackingSignal.ShippingInfo.ShippingState
        SHIPPED: OrderTrackingSignal.ShippingInfo.ShippingState
        DELIVERED: OrderTrackingSignal.ShippingInfo.ShippingState
        SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
        TRACKING_ID_FIELD_NUMBER: _ClassVar[int]
        CARRIER_FIELD_NUMBER: _ClassVar[int]
        CARRIER_SERVICE_FIELD_NUMBER: _ClassVar[int]
        SHIPPED_TIME_FIELD_NUMBER: _ClassVar[int]
        EARLIEST_DELIVERY_PROMISE_TIME_FIELD_NUMBER: _ClassVar[int]
        LATEST_DELIVERY_PROMISE_TIME_FIELD_NUMBER: _ClassVar[int]
        ACTUAL_DELIVERY_TIME_FIELD_NUMBER: _ClassVar[int]
        SHIPPING_STATUS_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
        ORIGIN_REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        shipment_id: str
        tracking_id: str
        carrier: str
        carrier_service: str
        shipped_time: _datetime_pb2.DateTime
        earliest_delivery_promise_time: _datetime_pb2.DateTime
        latest_delivery_promise_time: _datetime_pb2.DateTime
        actual_delivery_time: _datetime_pb2.DateTime
        shipping_status: OrderTrackingSignal.ShippingInfo.ShippingState
        origin_postal_code: str
        origin_region_code: str

        def __init__(self, shipment_id: _Optional[str]=..., tracking_id: _Optional[str]=..., carrier: _Optional[str]=..., carrier_service: _Optional[str]=..., shipped_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., earliest_delivery_promise_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., latest_delivery_promise_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., actual_delivery_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., shipping_status: _Optional[_Union[OrderTrackingSignal.ShippingInfo.ShippingState, str]]=..., origin_postal_code: _Optional[str]=..., origin_region_code: _Optional[str]=...) -> None:
            ...

    class LineItemDetails(_message.Message):
        __slots__ = ('line_item_id', 'product_id', 'gtin', 'mpn', 'product_title', 'brand', 'quantity')
        LINE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
        GTIN_FIELD_NUMBER: _ClassVar[int]
        MPN_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_TITLE_FIELD_NUMBER: _ClassVar[int]
        BRAND_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        line_item_id: str
        product_id: str
        gtin: str
        mpn: str
        product_title: str
        brand: str
        quantity: int

        def __init__(self, line_item_id: _Optional[str]=..., product_id: _Optional[str]=..., gtin: _Optional[str]=..., mpn: _Optional[str]=..., product_title: _Optional[str]=..., brand: _Optional[str]=..., quantity: _Optional[int]=...) -> None:
            ...

    class ShipmentLineItemMapping(_message.Message):
        __slots__ = ('shipment_id', 'line_item_id', 'quantity')
        SHIPMENT_ID_FIELD_NUMBER: _ClassVar[int]
        LINE_ITEM_ID_FIELD_NUMBER: _ClassVar[int]
        QUANTITY_FIELD_NUMBER: _ClassVar[int]
        shipment_id: str
        line_item_id: str
        quantity: int

        def __init__(self, shipment_id: _Optional[str]=..., line_item_id: _Optional[str]=..., quantity: _Optional[int]=...) -> None:
            ...
    ORDER_TRACKING_SIGNAL_ID_FIELD_NUMBER: _ClassVar[int]
    MERCHANT_ID_FIELD_NUMBER: _ClassVar[int]
    ORDER_CREATED_TIME_FIELD_NUMBER: _ClassVar[int]
    ORDER_ID_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_INFO_FIELD_NUMBER: _ClassVar[int]
    LINE_ITEMS_FIELD_NUMBER: _ClassVar[int]
    SHIPMENT_LINE_ITEM_MAPPING_FIELD_NUMBER: _ClassVar[int]
    CUSTOMER_SHIPPING_FEE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_POSTAL_CODE_FIELD_NUMBER: _ClassVar[int]
    DELIVERY_REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    order_tracking_signal_id: int
    merchant_id: int
    order_created_time: _datetime_pb2.DateTime
    order_id: str
    shipping_info: _containers.RepeatedCompositeFieldContainer[OrderTrackingSignal.ShippingInfo]
    line_items: _containers.RepeatedCompositeFieldContainer[OrderTrackingSignal.LineItemDetails]
    shipment_line_item_mapping: _containers.RepeatedCompositeFieldContainer[OrderTrackingSignal.ShipmentLineItemMapping]
    customer_shipping_fee: _types_pb2.Price
    delivery_postal_code: str
    delivery_region_code: str

    def __init__(self, order_tracking_signal_id: _Optional[int]=..., merchant_id: _Optional[int]=..., order_created_time: _Optional[_Union[_datetime_pb2.DateTime, _Mapping]]=..., order_id: _Optional[str]=..., shipping_info: _Optional[_Iterable[_Union[OrderTrackingSignal.ShippingInfo, _Mapping]]]=..., line_items: _Optional[_Iterable[_Union[OrderTrackingSignal.LineItemDetails, _Mapping]]]=..., shipment_line_item_mapping: _Optional[_Iterable[_Union[OrderTrackingSignal.ShipmentLineItemMapping, _Mapping]]]=..., customer_shipping_fee: _Optional[_Union[_types_pb2.Price, _Mapping]]=..., delivery_postal_code: _Optional[str]=..., delivery_region_code: _Optional[str]=...) -> None:
        ...