"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/user_location_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/searchads360/v0/resources/user_location_view.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xec\x02\n\x10UserLocationView\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x03\xfaA.\n,searchads360.googleapis.com/UserLocationView\x12&\n\x14country_criterion_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12$\n\x12targeting_location\x18\x05 \x01(\x08B\x03\xe0A\x03H\x01\x88\x01\x01:\x8c\x01\xeaA\x88\x01\n,searchads360.googleapis.com/UserLocationView\x12Xcustomers/{customer_id}/userLocationViews/{country_criterion_id}~{is_targeting_location}B\x17\n\x15_country_criterion_idB\x15\n\x13_targeting_locationB\x95\x02\n(com.google.ads.searchads360.v0.resourcesB\x15UserLocationViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.user_location_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x15UserLocationViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_USERLOCATIONVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_USERLOCATIONVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA.\n,searchads360.googleapis.com/UserLocationView'
    _globals['_USERLOCATIONVIEW'].fields_by_name['country_criterion_id']._loaded_options = None
    _globals['_USERLOCATIONVIEW'].fields_by_name['country_criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_USERLOCATIONVIEW'].fields_by_name['targeting_location']._loaded_options = None
    _globals['_USERLOCATIONVIEW'].fields_by_name['targeting_location']._serialized_options = b'\xe0A\x03'
    _globals['_USERLOCATIONVIEW']._loaded_options = None
    _globals['_USERLOCATIONVIEW']._serialized_options = b'\xeaA\x88\x01\n,searchads360.googleapis.com/UserLocationView\x12Xcustomers/{customer_id}/userLocationViews/{country_criterion_id}~{is_targeting_location}'
    _globals['_USERLOCATIONVIEW']._serialized_start = 164
    _globals['_USERLOCATIONVIEW']._serialized_end = 528