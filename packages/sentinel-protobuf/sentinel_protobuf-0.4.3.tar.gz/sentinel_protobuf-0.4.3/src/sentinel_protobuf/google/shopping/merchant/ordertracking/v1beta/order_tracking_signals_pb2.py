"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/ordertracking/v1beta/order_tracking_signals.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.shopping.type import types_pb2 as google_dot_shopping_dot_type_dot_types__pb2
from ......google.type import datetime_pb2 as google_dot_type_dot_datetime__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nJgoogle/shopping/merchant/ordertracking/v1beta/order_tracking_signals.proto\x12-google.shopping.merchant.ordertracking.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/shopping/type/types.proto\x1a\x1agoogle/type/datetime.proto"\xed\x01\n CreateOrderTrackingSignalRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account\x12%\n\x18order_tracking_signal_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12f\n\x15order_tracking_signal\x18\x03 \x01(\x0b2B.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignalB\x03\xe0A\x02"\xe3\x0c\n\x13OrderTrackingSignal\x12%\n\x18order_tracking_signal_id\x18\x0b \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bmerchant_id\x18\x0c \x01(\x03B\x03\xe0A\x01\x126\n\x12order_created_time\x18\x01 \x01(\x0b2\x15.google.type.DateTimeB\x03\xe0A\x02\x12\x15\n\x08order_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12k\n\rshipping_info\x18\x03 \x03(\x0b2O.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfoB\x03\xe0A\x02\x12k\n\nline_items\x18\x04 \x03(\x0b2R.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.LineItemDetailsB\x03\xe0A\x02\x12\x83\x01\n\x1ashipment_line_item_mapping\x18\x05 \x03(\x0b2Z.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShipmentLineItemMappingB\x03\xe0A\x01\x12D\n\x15customer_shipping_fee\x18\x06 \x01(\x0b2\x1b.google.shopping.type.PriceB\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x14delivery_postal_code\x18\t \x01(\tB\x03\xe0A\x01\x12!\n\x14delivery_region_code\x18\n \x01(\tB\x03\xe0A\x01\x1a\xf4\x04\n\x0cShippingInfo\x12\x18\n\x0bshipment_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0btracking_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07carrier\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x0fcarrier_service\x18\x04 \x01(\tB\x03\xe0A\x01\x120\n\x0cshipped_time\x18\x05 \x01(\x0b2\x15.google.type.DateTimeB\x03\xe0A\x01\x12B\n\x1eearliest_delivery_promise_time\x18\x06 \x01(\x0b2\x15.google.type.DateTimeB\x03\xe0A\x01\x12@\n\x1clatest_delivery_promise_time\x18\x07 \x01(\x0b2\x15.google.type.DateTimeB\x03\xe0A\x01\x128\n\x14actual_delivery_time\x18\x08 \x01(\x0b2\x15.google.type.DateTimeB\x03\xe0A\x01\x12{\n\x0fshipping_status\x18\t \x01(\x0e2].google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal.ShippingInfo.ShippingStateB\x03\xe0A\x02\x12\x1f\n\x12origin_postal_code\x18\n \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12origin_region_code\x18\x0b \x01(\tB\x03\xe0A\x02"K\n\rShippingState\x12\x1e\n\x1aSHIPPING_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07SHIPPED\x10\x01\x12\r\n\tDELIVERED\x10\x02\x1a\xd7\x01\n\x0fLineItemDetails\x12\x19\n\x0cline_item_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nproduct_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04gtin\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03mpn\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x1f\n\rproduct_title\x18\x05 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x17\n\x05brand\x18\x06 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12\x15\n\x08quantity\x18\x07 \x01(\x03B\x03\xe0A\x02B\x10\n\x0e_product_titleB\x08\n\x06_brand\x1ae\n\x17ShipmentLineItemMapping\x12\x18\n\x0bshipment_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cline_item_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08quantity\x18\x03 \x01(\x03B\x03\xe0A\x02B\x18\n\x16_customer_shipping_fee2\x9a\x03\n\x1bOrderTrackingSignalsService\x12\xb1\x02\n\x19CreateOrderTrackingSignal\x12O.google.shopping.merchant.ordertracking.v1beta.CreateOrderTrackingSignalRequest\x1aB.google.shopping.merchant.ordertracking.v1beta.OrderTrackingSignal"\x7f\xdaA\x1fparent,order_tracking_signal_id\x82\xd3\xe4\x93\x02W">/ordertracking/v1beta/{parent=accounts/*}/ordertrackingsignals:\x15order_tracking_signal\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xfe\x02\n1com.google.shopping.merchant.ordertracking.v1betaB\x19OrderTrackingSignalsProtoP\x01Z]cloud.google.com/go/shopping/merchant/ordertracking/apiv1beta/ordertrackingpb;ordertrackingpb\xaa\x02-Google.Shopping.Merchant.OrderTracking.V1Beta\xca\x02-Google\\Shopping\\Merchant\\OrderTracking\\V1beta\xea\x021Google::Shopping::Merchant::OrderTracking::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.ordertracking.v1beta.order_tracking_signals_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n1com.google.shopping.merchant.ordertracking.v1betaB\x19OrderTrackingSignalsProtoP\x01Z]cloud.google.com/go/shopping/merchant/ordertracking/apiv1beta/ordertrackingpb;ordertrackingpb\xaa\x02-Google.Shopping.Merchant.OrderTracking.V1Beta\xca\x02-Google\\Shopping\\Merchant\\OrderTracking\\V1beta\xea\x021Google::Shopping::Merchant::OrderTracking::V1beta\xeaA8\n"merchantapi.googleapis.com/Account\x12\x12accounts/{account}'
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\n"merchantapi.googleapis.com/Account'
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['order_tracking_signal_id']._loaded_options = None
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['order_tracking_signal_id']._serialized_options = b'\xe0A\x03'
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['order_tracking_signal']._loaded_options = None
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST'].fields_by_name['order_tracking_signal']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipment_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipment_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['tracking_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['tracking_id']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['carrier']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['carrier']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['carrier_service']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['carrier_service']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipped_time']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipped_time']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['earliest_delivery_promise_time']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['earliest_delivery_promise_time']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['latest_delivery_promise_time']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['latest_delivery_promise_time']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['actual_delivery_time']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['actual_delivery_time']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipping_status']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['shipping_status']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['origin_postal_code']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['origin_postal_code']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['origin_region_code']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO'].fields_by_name['origin_region_code']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['line_item_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['line_item_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['product_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['product_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['gtin']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['gtin']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['mpn']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['mpn']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['product_title']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['product_title']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['brand']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['brand']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['quantity']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS'].fields_by_name['quantity']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['shipment_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['shipment_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['line_item_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['line_item_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['quantity']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING'].fields_by_name['quantity']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_tracking_signal_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_tracking_signal_id']._serialized_options = b'\xe0A\x03'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['merchant_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['merchant_id']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_created_time']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_created_time']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_id']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['order_id']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['shipping_info']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['shipping_info']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['line_items']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['line_items']._serialized_options = b'\xe0A\x02'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['shipment_line_item_mapping']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['shipment_line_item_mapping']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['customer_shipping_fee']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['customer_shipping_fee']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['delivery_postal_code']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['delivery_postal_code']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['delivery_region_code']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNAL'].fields_by_name['delivery_region_code']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERTRACKINGSIGNALSSERVICE']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNALSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_ORDERTRACKINGSIGNALSSERVICE'].methods_by_name['CreateOrderTrackingSignal']._loaded_options = None
    _globals['_ORDERTRACKINGSIGNALSSERVICE'].methods_by_name['CreateOrderTrackingSignal']._serialized_options = b'\xdaA\x1fparent,order_tracking_signal_id\x82\xd3\xe4\x93\x02W">/ordertracking/v1beta/{parent=accounts/*}/ordertrackingsignals:\x15order_tracking_signal'
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST']._serialized_start = 303
    _globals['_CREATEORDERTRACKINGSIGNALREQUEST']._serialized_end = 540
    _globals['_ORDERTRACKINGSIGNAL']._serialized_start = 543
    _globals['_ORDERTRACKINGSIGNAL']._serialized_end = 2178
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO']._serialized_start = 1203
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO']._serialized_end = 1831
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO_SHIPPINGSTATE']._serialized_start = 1756
    _globals['_ORDERTRACKINGSIGNAL_SHIPPINGINFO_SHIPPINGSTATE']._serialized_end = 1831
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS']._serialized_start = 1834
    _globals['_ORDERTRACKINGSIGNAL_LINEITEMDETAILS']._serialized_end = 2049
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING']._serialized_start = 2051
    _globals['_ORDERTRACKINGSIGNAL_SHIPMENTLINEITEMMAPPING']._serialized_end = 2152
    _globals['_ORDERTRACKINGSIGNALSSERVICE']._serialized_start = 2181
    _globals['_ORDERTRACKINGSIGNALSSERVICE']._serialized_end = 2591