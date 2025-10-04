"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/customer_client_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_manager__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v19/resources/customer_client_link.proto\x12"google.ads.googleads.v19.resources\x1a8google/ads/googleads/v19/enums/manager_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf5\x03\n\x12CustomerClientLink\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/CustomerClientLink\x12G\n\x0fclient_customer\x18\x07 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01\x12!\n\x0fmanager_link_id\x18\x08 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12W\n\x06status\x18\x05 \x01(\x0e2G.google.ads.googleads.v19.enums.ManagerLinkStatusEnum.ManagerLinkStatus\x12\x13\n\x06hidden\x18\t \x01(\x08H\x02\x88\x01\x01:\x85\x01\xeaA\x81\x01\n+googleads.googleapis.com/CustomerClientLink\x12Rcustomers/{customer_id}/customerClientLinks/{client_customer_id}~{manager_link_id}B\x12\n\x10_client_customerB\x12\n\x10_manager_link_idB\t\n\x07_hiddenB\x89\x02\n&com.google.ads.googleads.v19.resourcesB\x17CustomerClientLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.customer_client_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x17CustomerClientLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/CustomerClientLink'
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['client_customer']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['client_customer']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['manager_link_id']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINK'].fields_by_name['manager_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENTLINK']._loaded_options = None
    _globals['_CUSTOMERCLIENTLINK']._serialized_options = b'\xeaA\x81\x01\n+googleads.googleapis.com/CustomerClientLink\x12Rcustomers/{customer_id}/customerClientLinks/{client_customer_id}~{manager_link_id}'
    _globals['_CUSTOMERCLIENTLINK']._serialized_start = 220
    _globals['_CUSTOMERCLIENTLINK']._serialized_end = 721