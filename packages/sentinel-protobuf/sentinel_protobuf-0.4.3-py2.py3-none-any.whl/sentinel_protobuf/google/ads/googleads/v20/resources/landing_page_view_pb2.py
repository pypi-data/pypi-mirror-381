"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/landing_page_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v20/resources/landing_page_view.proto\x12"google.ads.googleads.v20.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x97\x02\n\x0fLandingPageView\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x03\xfaA*\n(googleads.googleapis.com/LandingPageView\x12&\n\x14unexpanded_final_url\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01:z\xeaAw\n(googleads.googleapis.com/LandingPageView\x12Kcustomers/{customer_id}/landingPageViews/{unexpanded_final_url_fingerprint}B\x17\n\x15_unexpanded_final_urlB\x86\x02\n&com.google.ads.googleads.v20.resourcesB\x14LandingPageViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.landing_page_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x14LandingPageViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_LANDINGPAGEVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LANDINGPAGEVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA*\n(googleads.googleapis.com/LandingPageView'
    _globals['_LANDINGPAGEVIEW'].fields_by_name['unexpanded_final_url']._loaded_options = None
    _globals['_LANDINGPAGEVIEW'].fields_by_name['unexpanded_final_url']._serialized_options = b'\xe0A\x03'
    _globals['_LANDINGPAGEVIEW']._loaded_options = None
    _globals['_LANDINGPAGEVIEW']._serialized_options = b'\xeaAw\n(googleads.googleapis.com/LandingPageView\x12Kcustomers/{customer_id}/landingPageViews/{unexpanded_final_url_fingerprint}'
    _globals['_LANDINGPAGEVIEW']._serialized_start = 159
    _globals['_LANDINGPAGEVIEW']._serialized_end = 438