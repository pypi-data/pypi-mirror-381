"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import ad_type_infos_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_ad__type__infos__pb2
from ......google.ads.googleads.v20.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_custom__parameter__pb2
from ......google.ads.googleads.v20.common import final_app_url_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_final__app__url__pb2
from ......google.ads.googleads.v20.common import url_collection_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_url__collection__pb2
from ......google.ads.googleads.v20.enums import ad_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_ad__type__pb2
from ......google.ads.googleads.v20.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_device__pb2
from ......google.ads.googleads.v20.enums import system_managed_entity_source_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_system__managed__entity__source__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/ads/googleads/v20/resources/ad.proto\x12"google.ads.googleads.v20.resources\x1a3google/ads/googleads/v20/common/ad_type_infos.proto\x1a6google/ads/googleads/v20/common/custom_parameter.proto\x1a3google/ads/googleads/v20/common/final_app_url.proto\x1a4google/ads/googleads/v20/common/url_collection.proto\x1a,google/ads/googleads/v20/enums/ad_type.proto\x1a+google/ads/googleads/v20/enums/device.proto\x1aAgoogle/ads/googleads/v20/enums/system_managed_entity_source.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe8\x18\n\x02Ad\x12:\n\rresource_name\x18% \x01(\tB#\xe0A\x05\xfaA\x1d\n\x1bgoogleads.googleapis.com/Ad\x12\x14\n\x02id\x18( \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x12\n\nfinal_urls\x18) \x03(\t\x12D\n\x0efinal_app_urls\x18# \x03(\x0b2,.google.ads.googleads.v20.common.FinalAppUrl\x12\x19\n\x11final_mobile_urls\x18* \x03(\t\x12"\n\x15tracking_url_template\x18+ \x01(\tH\x02\x88\x01\x01\x12\x1d\n\x10final_url_suffix\x18, \x01(\tH\x03\x88\x01\x01\x12O\n\x15url_custom_parameters\x18\n \x03(\x0b20.google.ads.googleads.v20.common.CustomParameter\x12\x18\n\x0bdisplay_url\x18- \x01(\tH\x04\x88\x01\x01\x12D\n\x04type\x18\x05 \x01(\x0e21.google.ads.googleads.v20.enums.AdTypeEnum.AdTypeB\x03\xe0A\x03\x12%\n\x13added_by_google_ads\x18. \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01\x12L\n\x11device_preference\x18\x14 \x01(\x0e21.google.ads.googleads.v20.enums.DeviceEnum.Device\x12G\n\x0furl_collections\x18\x1a \x03(\x0b2..google.ads.googleads.v20.common.UrlCollection\x12\x16\n\x04name\x18/ \x01(\tB\x03\xe0A\x05H\x06\x88\x01\x01\x12\x88\x01\n\x1esystem_managed_resource_source\x18\x1b \x01(\x0e2[.google.ads.googleads.v20.enums.SystemManagedResourceSourceEnum.SystemManagedResourceSourceB\x03\xe0A\x03\x12C\n\x07text_ad\x18\x06 \x01(\x0b2+.google.ads.googleads.v20.common.TextAdInfoB\x03\xe0A\x05H\x00\x12O\n\x10expanded_text_ad\x18\x07 \x01(\x0b23.google.ads.googleads.v20.common.ExpandedTextAdInfoH\x00\x12>\n\x07call_ad\x181 \x01(\x0b2+.google.ads.googleads.v20.common.CallAdInfoH\x00\x12g\n\x1aexpanded_dynamic_search_ad\x18\x0e \x01(\x0b2<.google.ads.googleads.v20.common.ExpandedDynamicSearchAdInfoB\x03\xe0A\x05H\x00\x12@\n\x08hotel_ad\x18\x0f \x01(\x0b2,.google.ads.googleads.v20.common.HotelAdInfoH\x00\x12Q\n\x11shopping_smart_ad\x18\x11 \x01(\x0b24.google.ads.googleads.v20.common.ShoppingSmartAdInfoH\x00\x12U\n\x13shopping_product_ad\x18\x12 \x01(\x0b26.google.ads.googleads.v20.common.ShoppingProductAdInfoH\x00\x12E\n\x08image_ad\x18\x16 \x01(\x0b2,.google.ads.googleads.v20.common.ImageAdInfoB\x03\xe0A\x05H\x00\x12@\n\x08video_ad\x18\x18 \x01(\x0b2,.google.ads.googleads.v20.common.VideoAdInfoH\x00\x12U\n\x13video_responsive_ad\x18\' \x01(\x0b26.google.ads.googleads.v20.common.VideoResponsiveAdInfoH\x00\x12W\n\x14responsive_search_ad\x18\x19 \x01(\x0b27.google.ads.googleads.v20.common.ResponsiveSearchAdInfoH\x00\x12f\n\x1clegacy_responsive_display_ad\x18\x1c \x01(\x0b2>.google.ads.googleads.v20.common.LegacyResponsiveDisplayAdInfoH\x00\x12<\n\x06app_ad\x18\x1d \x01(\x0b2*.google.ads.googleads.v20.common.AppAdInfoH\x00\x12]\n\x15legacy_app_install_ad\x18\x1e \x01(\x0b27.google.ads.googleads.v20.common.LegacyAppInstallAdInfoB\x03\xe0A\x05H\x00\x12Y\n\x15responsive_display_ad\x18\x1f \x01(\x0b28.google.ads.googleads.v20.common.ResponsiveDisplayAdInfoH\x00\x12@\n\x08local_ad\x18  \x01(\x0b2,.google.ads.googleads.v20.common.LocalAdInfoH\x00\x12Q\n\x11display_upload_ad\x18! \x01(\x0b24.google.ads.googleads.v20.common.DisplayUploadAdInfoH\x00\x12Q\n\x11app_engagement_ad\x18" \x01(\x0b24.google.ads.googleads.v20.common.AppEngagementAdInfoH\x00\x12j\n\x1eshopping_comparison_listing_ad\x18$ \x01(\x0b2@.google.ads.googleads.v20.common.ShoppingComparisonListingAdInfoH\x00\x12Q\n\x11smart_campaign_ad\x180 \x01(\x0b24.google.ads.googleads.v20.common.SmartCampaignAdInfoH\x00\x12\\\n\x17app_pre_registration_ad\x182 \x01(\x0b29.google.ads.googleads.v20.common.AppPreRegistrationAdInfoH\x00\x12_\n\x19demand_gen_multi_asset_ad\x18> \x01(\x0b2:.google.ads.googleads.v20.common.DemandGenMultiAssetAdInfoH\x00\x12Z\n\x16demand_gen_carousel_ad\x18? \x01(\x0b28.google.ads.googleads.v20.common.DemandGenCarouselAdInfoH\x00\x12i\n\x1edemand_gen_video_responsive_ad\x18@ \x01(\x0b2?.google.ads.googleads.v20.common.DemandGenVideoResponsiveAdInfoH\x00\x12X\n\x15demand_gen_product_ad\x18= \x01(\x0b27.google.ads.googleads.v20.common.DemandGenProductAdInfoH\x00\x12B\n\ttravel_ad\x186 \x01(\x0b2-.google.ads.googleads.v20.common.TravelAdInfoH\x00:E\xeaAB\n\x1bgoogleads.googleapis.com/Ad\x12#customers/{customer_id}/ads/{ad_id}B\t\n\x07ad_dataB\x05\n\x03_idB\x18\n\x16_tracking_url_templateB\x13\n\x11_final_url_suffixB\x0e\n\x0c_display_urlB\x16\n\x14_added_by_google_adsB\x07\n\x05_nameB\xf9\x01\n&com.google.ads.googleads.v20.resourcesB\x07AdProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x07AdProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_AD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_AD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA\x1d\n\x1bgoogleads.googleapis.com/Ad'
    _globals['_AD'].fields_by_name['id']._loaded_options = None
    _globals['_AD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['type']._loaded_options = None
    _globals['_AD'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['added_by_google_ads']._loaded_options = None
    _globals['_AD'].fields_by_name['added_by_google_ads']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['name']._loaded_options = None
    _globals['_AD'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['system_managed_resource_source']._loaded_options = None
    _globals['_AD'].fields_by_name['system_managed_resource_source']._serialized_options = b'\xe0A\x03'
    _globals['_AD'].fields_by_name['text_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['text_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['expanded_dynamic_search_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['expanded_dynamic_search_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['image_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['image_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD'].fields_by_name['legacy_app_install_ad']._loaded_options = None
    _globals['_AD'].fields_by_name['legacy_app_install_ad']._serialized_options = b'\xe0A\x05'
    _globals['_AD']._loaded_options = None
    _globals['_AD']._serialized_options = b'\xeaAB\n\x1bgoogleads.googleapis.com/Ad\x12#customers/{customer_id}/ads/{ad_id}'
    _globals['_AD']._serialized_start = 518
    _globals['_AD']._serialized_end = 3694