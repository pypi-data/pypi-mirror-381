"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/customer_manager_link.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import manager_link_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_manager__link__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/searchads360/v0/resources/customer_manager_link.proto\x12$google.ads.searchads360.v0.resources\x1a:google/ads/searchads360/v0/enums/manager_link_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x94\x04\n\x13CustomerManagerLink\x12N\n\rresource_name\x18\x01 \x01(\tB7\xe0A\x05\xfaA1\n/searchads360.googleapis.com/CustomerManagerLink\x12K\n\x10manager_customer\x18\x06 \x01(\tB,\xe0A\x03\xfaA&\n$searchads360.googleapis.com/CustomerH\x00\x88\x01\x01\x12!\n\x0fmanager_link_id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12Y\n\x06status\x18\x05 \x01(\x0e2I.google.ads.searchads360.v0.enums.ManagerLinkStatusEnum.ManagerLinkStatus\x12\x1c\n\nstart_time\x18\x08 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01:\x8b\x01\xeaA\x87\x01\n/searchads360.googleapis.com/CustomerManagerLink\x12Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}B\x13\n\x11_manager_customerB\x12\n\x10_manager_link_idB\r\n\x0b_start_timeB\x98\x02\n(com.google.ads.searchads360.v0.resourcesB\x18CustomerManagerLinkProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.customer_manager_link_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x18CustomerManagerLinkProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA1\n/searchads360.googleapis.com/CustomerManagerLink'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_customer']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_customer']._serialized_options = b'\xe0A\x03\xfaA&\n$searchads360.googleapis.com/Customer'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_link_id']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['manager_link_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['start_time']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERMANAGERLINK']._loaded_options = None
    _globals['_CUSTOMERMANAGERLINK']._serialized_options = b'\xeaA\x87\x01\n/searchads360.googleapis.com/CustomerManagerLink\x12Tcustomers/{customer_id}/customerManagerLinks/{manager_customer_id}~{manager_link_id}'
    _globals['_CUSTOMERMANAGERLINK']._serialized_start = 227
    _globals['_CUSTOMERMANAGERLINK']._serialized_end = 759