"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/ai_max_search_term_ad_combination_view.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nOgoogle/ads/googleads/v21/resources/ai_max_search_term_ad_combination_view.proto\x12"google.ads.googleads.v21.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcb\x04\n AiMaxSearchTermAdCombinationView\x12X\n\rresource_name\x18\x01 \x01(\tBA\xe0A\x03\xfaA;\n9googleads.googleapis.com/AiMaxSearchTermAdCombinationView\x12?\n\x08ad_group\x18\x02 \x01(\tB(\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroupH\x00\x88\x01\x01\x12\x1d\n\x0bsearch_term\x18\x03 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1e\n\x0clanding_page\x18\x04 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1a\n\x08headline\x18\x05 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01:\xf5\x01\xeaA\xf1\x01\n9googleads.googleapis.com/AiMaxSearchTermAdCombinationView\x12ocustomers/{customer_id}/aiMaxSearchTermAdCombinationViews/{ad_group_id}~{search_term}~{landing_page}~{headline}*!aiMaxSearchTermAdCombinationViews2 aiMaxSearchTermAdCombinationViewB\x0b\n\t_ad_groupB\x0e\n\x0c_search_termB\x0f\n\r_landing_pageB\x0b\n\t_headlineB\x97\x02\n&com.google.ads.googleads.v21.resourcesB%AiMaxSearchTermAdCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.ai_max_search_term_ad_combination_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB%AiMaxSearchTermAdCombinationViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA;\n9googleads.googleapis.com/AiMaxSearchTermAdCombinationView'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['ad_group']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x03\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['search_term']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['search_term']._serialized_options = b'\xe0A\x03'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['landing_page']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['landing_page']._serialized_options = b'\xe0A\x03'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['headline']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW'].fields_by_name['headline']._serialized_options = b'\xe0A\x03'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW']._loaded_options = None
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW']._serialized_options = b'\xeaA\xf1\x01\n9googleads.googleapis.com/AiMaxSearchTermAdCombinationView\x12ocustomers/{customer_id}/aiMaxSearchTermAdCombinationViews/{ad_group_id}~{search_term}~{landing_page}~{headline}*!aiMaxSearchTermAdCombinationViews2 aiMaxSearchTermAdCombinationView'
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW']._serialized_start = 180
    _globals['_AIMAXSEARCHTERMADCOMBINATIONVIEW']._serialized_end = 767