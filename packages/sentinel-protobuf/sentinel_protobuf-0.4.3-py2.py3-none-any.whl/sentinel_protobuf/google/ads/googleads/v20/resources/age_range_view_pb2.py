"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/age_range_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v20/resources/age_range_view.proto\x12"google.ads.googleads.v20.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc4\x01\n\x0cAgeRangeView\x12D\n\rresource_name\x18\x01 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/AgeRangeView:n\xeaAk\n%googleads.googleapis.com/AgeRangeView\x12Bcustomers/{customer_id}/ageRangeViews/{ad_group_id}~{criterion_id}B\x83\x02\n&com.google.ads.googleads.v20.resourcesB\x11AgeRangeViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.age_range_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x11AgeRangeViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_AGERANGEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AGERANGEVIEW'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/AgeRangeView"
    _globals['_AGERANGEVIEW']._loaded_options = None
    _globals['_AGERANGEVIEW']._serialized_options = b'\xeaAk\n%googleads.googleapis.com/AgeRangeView\x12Bcustomers/{customer_id}/ageRangeViews/{ad_group_id}~{criterion_id}'
    _globals['_AGERANGEVIEW']._serialized_start = 156
    _globals['_AGERANGEVIEW']._serialized_end = 352