"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import ad_type_infos_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_ad__type__infos__pb2
from ......google.ads.searchads360.v0.enums import ad_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ads/searchads360/v0/resources/ad.proto\x12$google.ads.searchads360.v0.resources\x1a5google/ads/searchads360/v0/common/ad_type_infos.proto\x1a.google/ads/searchads360/v0/enums/ad_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xcf\x06\n\x02Ad\x12=\n\rresource_name\x18% \x01(\tB&\xe0A\x05\xfaA \n\x1esearchads360.googleapis.com/Ad\x12\x14\n\x02id\x18( \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x12\n\nfinal_urls\x18) \x03(\t\x12\x18\n\x0bdisplay_url\x18- \x01(\tH\x02\x88\x01\x01\x12F\n\x04type\x18\x05 \x01(\x0e23.google.ads.searchads360.v0.enums.AdTypeEnum.AdTypeB\x03\xe0A\x03\x12\x16\n\x04name\x18/ \x01(\tB\x03\xe0A\x05H\x03\x88\x01\x01\x12Q\n\x07text_ad\x187 \x01(\x0b29.google.ads.searchads360.v0.common.SearchAds360TextAdInfoB\x03\xe0A\x05H\x00\x12b\n\x10expanded_text_ad\x188 \x01(\x0b2A.google.ads.searchads360.v0.common.SearchAds360ExpandedTextAdInfoB\x03\xe0A\x05H\x00\x12j\n\x14responsive_search_ad\x189 \x01(\x0b2E.google.ads.searchads360.v0.common.SearchAds360ResponsiveSearchAdInfoB\x03\xe0A\x05H\x00\x12W\n\nproduct_ad\x18: \x01(\x0b2<.google.ads.searchads360.v0.common.SearchAds360ProductAdInfoB\x03\xe0A\x05H\x00\x12u\n\x1aexpanded_dynamic_search_ad\x18; \x01(\x0b2J.google.ads.searchads360.v0.common.SearchAds360ExpandedDynamicSearchAdInfoB\x03\xe0A\x05H\x00:H\xeaAE\n\x1esearchads360.googleapis.com/Ad\x12#customers/{customer_id}/ads/{ad_id}B\t\n\x07ad_dataB\x05\n\x03_idB\x0e\n\x0c_display_urlB\x07\n\x05_nameB\x87\x02\n(com.google.ads.searchads360.v0.resourcesB\x07AdProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x07AdProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_AD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA \n\x1esearchads360.googleapis.com/Ad'
    _globals['_AD'].fields_by_name['id']._loaded_options = None
    _globals['_AD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['type']._loaded_options = None
    _globals['_AD'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['name']._loaded_options = None
    _globals['_AD'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['text_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['text_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['expanded_text_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['expanded_text_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['responsive_search_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['responsive_search_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['product_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['product_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['expanded_dynamic_search_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['expanded_dynamic_search_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD']._loaded_options = None
    _globals['_AD']._serialized_options = b'\xeaAE\n\x1esearchads360.googleapis.com/Ad\x12#customers/{customer_id}/ads/{ad_id}'
    _globals['_AD']._serialized_start = 251
    _globals['_AD']._serialized_end = 1098