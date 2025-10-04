"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/dynamic_search_ads_search_term_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nNgoogle/ads/searchads360/v0/resources/dynamic_search_ads_search_term_view.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xeb\x02\n\x1eDynamicSearchAdsSearchTermView\x12Y\n\rresource_name\x18\x01 \x01(\tBB\xe0A\x03\xfaA<\n:searchads360.googleapis.com/DynamicSearchAdsSearchTermView\x12\x1e\n\x0clanding_page\x18\x0b \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01:\xbc\x01\xeaA\xb8\x01\n:searchads360.googleapis.com/DynamicSearchAdsSearchTermView\x12zcustomers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{query_fp}~{line1_fp}~{url_fp}~{feed_item_lp_url_fp}B\x0f\n\r_landing_pageB\xa3\x02\n(com.google.ads.searchads360.v0.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.dynamic_search_ads_search_term_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA<\n:searchads360.googleapis.com/DynamicSearchAdsSearchTermView'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['landing_page']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['landing_page']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_options = b'\xeaA\xb8\x01\n:searchads360.googleapis.com/DynamicSearchAdsSearchTermView\x12zcustomers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{query_fp}~{line1_fp}~{url_fp}~{feed_item_lp_url_fp}'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_start = 181
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_end = 544