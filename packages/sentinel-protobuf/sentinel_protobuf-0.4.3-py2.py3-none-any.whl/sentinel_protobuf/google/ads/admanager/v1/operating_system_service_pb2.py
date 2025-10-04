"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/operating_system_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import operating_system_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_operating__system__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/ads/admanager/v1/operating_system_service.proto\x12\x17google.ads.admanager.v1\x1a7google/ads/admanager/v1/operating_system_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"[\n\x19GetOperatingSystemRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(admanager.googleapis.com/OperatingSystem"\xc7\x01\n\x1bListOperatingSystemsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"\x90\x01\n\x1cListOperatingSystemsResponse\x12C\n\x11operating_systems\x18\x01 \x03(\x0b2(.google.ads.admanager.v1.OperatingSystem\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x052\xd0\x03\n\x16OperatingSystemService\x12\xab\x01\n\x12GetOperatingSystem\x122.google.ads.admanager.v1.GetOperatingSystemRequest\x1a(.google.ads.admanager.v1.OperatingSystem"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=networks/*/operatingSystems/*}\x12\xbe\x01\n\x14ListOperatingSystems\x124.google.ads.admanager.v1.ListOperatingSystemsRequest\x1a5.google.ads.admanager.v1.ListOperatingSystemsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=networks/*}/operatingSystems\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xcf\x01\n\x1bcom.google.ads.admanager.v1B\x1bOperatingSystemServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.operating_system_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1bOperatingSystemServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_GETOPERATINGSYSTEMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETOPERATINGSYSTEMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(admanager.googleapis.com/OperatingSystem'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTOPERATINGSYSTEMSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATINGSYSTEMSERVICE']._loaded_options = None
    _globals['_OPERATINGSYSTEMSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_OPERATINGSYSTEMSERVICE'].methods_by_name['GetOperatingSystem']._loaded_options = None
    _globals['_OPERATINGSYSTEMSERVICE'].methods_by_name['GetOperatingSystem']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=networks/*/operatingSystems/*}'
    _globals['_OPERATINGSYSTEMSERVICE'].methods_by_name['ListOperatingSystems']._loaded_options = None
    _globals['_OPERATINGSYSTEMSERVICE'].methods_by_name['ListOperatingSystems']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=networks/*}/operatingSystems'
    _globals['_GETOPERATINGSYSTEMREQUEST']._serialized_start = 255
    _globals['_GETOPERATINGSYSTEMREQUEST']._serialized_end = 346
    _globals['_LISTOPERATINGSYSTEMSREQUEST']._serialized_start = 349
    _globals['_LISTOPERATINGSYSTEMSREQUEST']._serialized_end = 548
    _globals['_LISTOPERATINGSYSTEMSRESPONSE']._serialized_start = 551
    _globals['_LISTOPERATINGSYSTEMSRESPONSE']._serialized_end = 695
    _globals['_OPERATINGSYSTEMSERVICE']._serialized_start = 698
    _globals['_OPERATINGSYSTEMSERVICE']._serialized_end = 1162