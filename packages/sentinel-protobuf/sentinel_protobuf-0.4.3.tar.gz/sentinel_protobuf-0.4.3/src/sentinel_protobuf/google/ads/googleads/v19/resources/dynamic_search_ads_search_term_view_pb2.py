"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/dynamic_search_ads_search_term_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/ads/googleads/v19/resources/dynamic_search_ads_search_term_view.proto\x12"google.ads.googleads.v19.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd0\x05\n\x1eDynamicSearchAdsSearchTermView\x12V\n\rresource_name\x18\x01 \x01(\tB?\xe0A\x03\xfaA9\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\x1d\n\x0bsearch_term\x18\t \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1a\n\x08headline\x18\n \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1e\n\x0clanding_page\x18\x0b \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1a\n\x08page_url\x18\x0c \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12&\n\x14has_negative_keyword\x18\r \x01(\x08B\x03\xe0A\x03H\x04\x88\x01\x01\x12&\n\x14has_matching_keyword\x18\x0e \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01\x12"\n\x10has_negative_url\x18\x0f \x01(\x08B\x03\xe0A\x03H\x06\x88\x01\x01:\xe8\x01\xeaA\xe4\x01\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\xa8\x01customers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}B\x0e\n\x0c_search_termB\x0b\n\t_headlineB\x0f\n\r_landing_pageB\x0b\n\t_page_urlB\x17\n\x15_has_negative_keywordB\x17\n\x15_has_matching_keywordB\x13\n\x11_has_negative_urlB\x95\x02\n&com.google.ads.googleads.v19.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.dynamic_search_ads_search_term_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB#DynamicSearchAdsSearchTermViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA9\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['search_term']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['search_term']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['headline']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['headline']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['landing_page']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['landing_page']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['page_url']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['page_url']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_negative_keyword']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_negative_keyword']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_matching_keyword']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_matching_keyword']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_negative_url']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW'].fields_by_name['has_negative_url']._serialized_options = b'\xe0A\x03'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._loaded_options = None
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_options = b'\xeaA\xe4\x01\n7googleads.googleapis.com/DynamicSearchAdsSearchTermView\x12\xa8\x01customers/{customer_id}/dynamicSearchAdsSearchTermViews/{ad_group_id}~{search_term_fingerprint}~{headline_fingerprint}~{landing_page_fingerprint}~{page_url_fingerprint}'
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_start = 177
    _globals['_DYNAMICSEARCHADSSEARCHTERMVIEW']._serialized_end = 897