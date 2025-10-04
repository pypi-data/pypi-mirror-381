"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/customer_manager_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import manager_link_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_manager__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v20/resources/customer_manager_link.proto\x12"google.ads.googleads.v20.resources\x1a8google/ads/googleads/v20/enums/manager_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdc\x03\n\x13CustomerManagerLink\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomerManagerLink\x12H\n\x10manager_customer\x18\x06 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01\x12!\n\x0fmanager_link_id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12W\n\x06status\x18\x05 \x01(\x0e2G.google.ads.googleads.v20.enums.ManagerLinkStatusEnum.ManagerLinkStatus:\x88\x01\xeaA\x84\x01\n,googleads.googleapis.com/CustomerManagerLink\x12Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}B\x13\n\x11_manager_customerB\x12\n\x10_manager_link_idB\x8a\x02\n&com.google.ads.googleads.v20.resourcesB\x18CustomerManagerLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.customer_manager_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x18CustomerManagerLinkProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/CustomerManagerLink'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_customer']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_link_id']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERMANAGERLINK']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK']._serialized_options = b'\xeaA\x84\x01\n,googleads.googleapis.com/CustomerManagerLink\x12Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}'
    _globals['_CUSTOMERMANAGERLINK']._serialized_start = 221
    _globals['_CUSTOMERMANAGERLINK']._serialized_end = 697