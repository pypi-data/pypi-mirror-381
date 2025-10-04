"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/order_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import order_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_order__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/admanager/v1/order_service.proto\x12\x17google.ads.admanager.v1\x1a,google/ads/admanager/v1/order_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"G\n\x0fGetOrderRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1eadmanager.googleapis.com/Order"\xbd\x01\n\x11ListOrdersRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"q\n\x12ListOrdersResponse\x12.\n\x06orders\x18\x01 \x03(\x0b2\x1e.google.ads.admanager.v1.Order\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xf6\x02\n\x0cOrderService\x12\x83\x01\n\x08GetOrder\x12(.google.ads.admanager.v1.GetOrderRequest\x1a\x1e.google.ads.admanager.v1.Order"-\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=networks/*/orders/*}\x12\x96\x01\n\nListOrders\x12*.google.ads.admanager.v1.ListOrdersRequest\x1a+.google.ads.admanager.v1.ListOrdersResponse"/\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=networks/*}/orders\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xc5\x01\n\x1bcom.google.ads.admanager.v1B\x11OrderServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.order_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x11OrderServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETORDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1eadmanager.googleapis.com/Order'
    _globals['_LISTORDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTORDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORDERSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORDERSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORDERSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTORDERSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_ORDERSERVICE']._loaded_options = None
    _globals['_ORDERSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_ORDERSERVICE'].methods_by_name['GetOrder']._loaded_options = None
    _globals['_ORDERSERVICE'].methods_by_name['GetOrder']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{name=networks/*/orders/*}'
    _globals['_ORDERSERVICE'].methods_by_name['ListOrders']._loaded_options = None
    _globals['_ORDERSERVICE'].methods_by_name['ListOrders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=networks/*}/orders'
    _globals['_GETORDERREQUEST']._serialized_start = 233
    _globals['_GETORDERREQUEST']._serialized_end = 304
    _globals['_LISTORDERSREQUEST']._serialized_start = 307
    _globals['_LISTORDERSREQUEST']._serialized_end = 496
    _globals['_LISTORDERSRESPONSE']._serialized_start = 498
    _globals['_LISTORDERSRESPONSE']._serialized_end = 611
    _globals['_ORDERSERVICE']._serialized_start = 614
    _globals['_ORDERSERVICE']._serialized_end = 988