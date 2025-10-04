"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/expanded_landing_page_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v21/resources/expanded_landing_page_view.proto\x12"google.ads.googleads.v21.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb3\x02\n\x17ExpandedLandingPageView\x12O\n\rresource_name\x18\x01 \x01(\tB8\xe0A\x03\xfaA2\n0googleads.googleapis.com/ExpandedLandingPageView\x12$\n\x12expanded_final_url\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01:\x89\x01\xeaA\x85\x01\n0googleads.googleapis.com/ExpandedLandingPageView\x12Qcustomers/{customer_id}/expandedLandingPageViews/{expanded_final_url_fingerprint}B\x15\n\x13_expanded_final_urlB\x8e\x02\n&com.google.ads.googleads.v21.resourcesB\x1cExpandedLandingPageViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.expanded_landing_page_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x1cExpandedLandingPageViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_EXPANDEDLANDINGPAGEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_EXPANDEDLANDINGPAGEVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA2\n0googleads.googleapis.com/ExpandedLandingPageView'
    _globals['_EXPANDEDLANDINGPAGEVIEW'].fields_by_name['expanded_final_url']._loaded_options = None
    _globals['_EXPANDEDLANDINGPAGEVIEW'].fields_by_name['expanded_final_url']._serialized_options = b'\xe0A\x03'
    _globals['_EXPANDEDLANDINGPAGEVIEW']._loaded_options = None
    _globals['_EXPANDEDLANDINGPAGEVIEW']._serialized_options = b'\xeaA\x85\x01\n0googleads.googleapis.com/ExpandedLandingPageView\x12Qcustomers/{customer_id}/expandedLandingPageViews/{expanded_final_url_fingerprint}'
    _globals['_EXPANDEDLANDINGPAGEVIEW']._serialized_start = 168
    _globals['_EXPANDEDLANDINGPAGEVIEW']._serialized_end = 475