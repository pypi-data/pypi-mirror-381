"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/ad_unit_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import ad_unit_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_ad__unit__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ads/admanager/v1/ad_unit_service.proto\x12\x17google.ads.admanager.v1\x1a.google/ads/admanager/v1/ad_unit_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"I\n\x10GetAdUnitRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/AdUnit"\xbe\x01\n\x12ListAdUnitsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"u\n\x13ListAdUnitsResponse\x121\n\x08ad_units\x18\x01 \x03(\x0b2\x1f.google.ads.admanager.v1.AdUnit\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xc2\x01\n\x16ListAdUnitSizesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\x82\x01\n\x17ListAdUnitSizesResponse\x12:\n\rad_unit_sizes\x18\x01 \x03(\x0b2#.google.ads.admanager.v1.AdUnitSize\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xac\x04\n\rAdUnitService\x12\x87\x01\n\tGetAdUnit\x12).google.ads.admanager.v1.GetAdUnitRequest\x1a\x1f.google.ads.admanager.v1.AdUnit".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=networks/*/adUnits/*}\x12\x9a\x01\n\x0bListAdUnits\x12+.google.ads.admanager.v1.ListAdUnitsRequest\x1a,.google.ads.admanager.v1.ListAdUnitsResponse"0\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=networks/*}/adUnits\x12\xaa\x01\n\x0fListAdUnitSizes\x12/.google.ads.admanager.v1.ListAdUnitSizesRequest\x1a0.google.ads.admanager.v1.ListAdUnitSizesResponse"4\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=networks/*}/adUnitSizes\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xc6\x01\n\x1bcom.google.ads.admanager.v1B\x12AdUnitServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.ad_unit_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x12AdUnitServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETADUNITREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETADUNITREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/AdUnit'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTADUNITSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTADUNITSIZESREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNITSERVICE']._loaded_options = None
    _globals['_ADUNITSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_ADUNITSERVICE'].methods_by_name['GetAdUnit']._loaded_options = None
    _globals['_ADUNITSERVICE'].methods_by_name['GetAdUnit']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=networks/*/adUnits/*}'
    _globals['_ADUNITSERVICE'].methods_by_name['ListAdUnits']._loaded_options = None
    _globals['_ADUNITSERVICE'].methods_by_name['ListAdUnits']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=networks/*}/adUnits'
    _globals['_ADUNITSERVICE'].methods_by_name['ListAdUnitSizes']._loaded_options = None
    _globals['_ADUNITSERVICE'].methods_by_name['ListAdUnitSizes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02%\x12#/v1/{parent=networks/*}/adUnitSizes'
    _globals['_GETADUNITREQUEST']._serialized_start = 237
    _globals['_GETADUNITREQUEST']._serialized_end = 310
    _globals['_LISTADUNITSREQUEST']._serialized_start = 313
    _globals['_LISTADUNITSREQUEST']._serialized_end = 503
    _globals['_LISTADUNITSRESPONSE']._serialized_start = 505
    _globals['_LISTADUNITSRESPONSE']._serialized_end = 622
    _globals['_LISTADUNITSIZESREQUEST']._serialized_start = 625
    _globals['_LISTADUNITSIZESREQUEST']._serialized_end = 819
    _globals['_LISTADUNITSIZESRESPONSE']._serialized_start = 822
    _globals['_LISTADUNITSIZESRESPONSE']._serialized_end = 952
    _globals['_ADUNITSERVICE']._serialized_start = 955
    _globals['_ADUNITSERVICE']._serialized_end = 1511