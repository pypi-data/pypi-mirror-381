"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import asset_types_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_asset__types__pb2
from ......google.ads.googleads.v21.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_custom__parameter__pb2
from ......google.ads.googleads.v21.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_policy__pb2
from ......google.ads.googleads.v21.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v21.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__source__pb2
from ......google.ads.googleads.v21.enums import asset_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__type__pb2
from ......google.ads.googleads.v21.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_policy__approval__status__pb2
from ......google.ads.googleads.v21.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_policy__review__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/googleads/v21/resources/asset.proto\x12"google.ads.googleads.v21.resources\x1a1google/ads/googleads/v21/common/asset_types.proto\x1a6google/ads/googleads/v21/common/custom_parameter.proto\x1a,google/ads/googleads/v21/common/policy.proto\x1a5google/ads/googleads/v21/enums/asset_field_type.proto\x1a1google/ads/googleads/v21/enums/asset_source.proto\x1a/google/ads/googleads/v21/enums/asset_type.proto\x1a;google/ads/googleads/v21/enums/policy_approval_status.proto\x1a9google/ads/googleads/v21/enums/policy_review_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfe\x19\n\x05Asset\x12=\n\rresource_name\x18\x01 \x01(\tB&\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset\x12\x14\n\x02id\x18\x0b \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0c \x01(\tH\x02\x88\x01\x01\x12J\n\x04type\x18\x04 \x01(\x0e27.google.ads.googleads.v21.enums.AssetTypeEnum.AssetTypeB\x03\xe0A\x03\x12\x12\n\nfinal_urls\x18\x0e \x03(\t\x12\x19\n\x11final_mobile_urls\x18\x10 \x03(\t\x12"\n\x15tracking_url_template\x18\x11 \x01(\tH\x03\x88\x01\x01\x12O\n\x15url_custom_parameters\x18\x12 \x03(\x0b20.google.ads.googleads.v21.common.CustomParameter\x12\x1d\n\x10final_url_suffix\x18\x13 \x01(\tH\x04\x88\x01\x01\x12P\n\x06source\x18& \x01(\x0e2;.google.ads.googleads.v21.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03\x12S\n\x0epolicy_summary\x18\r \x01(\x0b26.google.ads.googleads.v21.resources.AssetPolicySummaryB\x03\xe0A\x03\x12i\n\x1bfield_type_policy_summaries\x18( \x03(\x0b2?.google.ads.googleads.v21.resources.AssetFieldTypePolicySummaryB\x03\xe0A\x03\x12V\n\x13youtube_video_asset\x18\x05 \x01(\x0b22.google.ads.googleads.v21.common.YoutubeVideoAssetB\x03\xe0A\x05H\x00\x12T\n\x12media_bundle_asset\x18\x06 \x01(\x0b21.google.ads.googleads.v21.common.MediaBundleAssetB\x03\xe0A\x05H\x00\x12G\n\x0bimage_asset\x18\x07 \x01(\x0b2+.google.ads.googleads.v21.common.ImageAssetB\x03\xe0A\x03H\x00\x12E\n\ntext_asset\x18\x08 \x01(\x0b2*.google.ads.googleads.v21.common.TextAssetB\x03\xe0A\x05H\x00\x12I\n\x0flead_form_asset\x18\t \x01(\x0b2..google.ads.googleads.v21.common.LeadFormAssetH\x00\x12R\n\x14book_on_google_asset\x18\n \x01(\x0b22.google.ads.googleads.v21.common.BookOnGoogleAssetH\x00\x12J\n\x0fpromotion_asset\x18\x0f \x01(\x0b2/.google.ads.googleads.v21.common.PromotionAssetH\x00\x12F\n\rcallout_asset\x18\x14 \x01(\x0b2-.google.ads.googleads.v21.common.CalloutAssetH\x00\x12[\n\x18structured_snippet_asset\x18\x15 \x01(\x0b27.google.ads.googleads.v21.common.StructuredSnippetAssetH\x00\x12H\n\x0esitelink_asset\x18\x16 \x01(\x0b2..google.ads.googleads.v21.common.SitelinkAssetH\x00\x12I\n\x0fpage_feed_asset\x18\x17 \x01(\x0b2..google.ads.googleads.v21.common.PageFeedAssetH\x00\x12Y\n\x17dynamic_education_asset\x18\x18 \x01(\x0b26.google.ads.googleads.v21.common.DynamicEducationAssetH\x00\x12K\n\x10mobile_app_asset\x18\x19 \x01(\x0b2/.google.ads.googleads.v21.common.MobileAppAssetH\x00\x12Q\n\x13hotel_callout_asset\x18\x1a \x01(\x0b22.google.ads.googleads.v21.common.HotelCalloutAssetH\x00\x12@\n\ncall_asset\x18\x1b \x01(\x0b2*.google.ads.googleads.v21.common.CallAssetH\x00\x12B\n\x0bprice_asset\x18\x1c \x01(\x0b2+.google.ads.googleads.v21.common.PriceAssetH\x00\x12W\n\x14call_to_action_asset\x18\x1d \x01(\x0b22.google.ads.googleads.v21.common.CallToActionAssetB\x03\xe0A\x05H\x00\x12\\\n\x19dynamic_real_estate_asset\x18\x1e \x01(\x0b27.google.ads.googleads.v21.common.DynamicRealEstateAssetH\x00\x12S\n\x14dynamic_custom_asset\x18\x1f \x01(\x0b23.google.ads.googleads.v21.common.DynamicCustomAssetH\x00\x12i\n dynamic_hotels_and_rentals_asset\x18  \x01(\x0b2=.google.ads.googleads.v21.common.DynamicHotelsAndRentalsAssetH\x00\x12U\n\x15dynamic_flights_asset\x18! \x01(\x0b24.google.ads.googleads.v21.common.DynamicFlightsAssetH\x00\x12j\n\x1edemand_gen_carousel_card_asset\x182 \x01(\x0b2;.google.ads.googleads.v21.common.DemandGenCarouselCardAssetB\x03\xe0A\x05H\x00\x12S\n\x14dynamic_travel_asset\x18# \x01(\x0b23.google.ads.googleads.v21.common.DynamicTravelAssetH\x00\x12Q\n\x13dynamic_local_asset\x18$ \x01(\x0b22.google.ads.googleads.v21.common.DynamicLocalAssetH\x00\x12O\n\x12dynamic_jobs_asset\x18% \x01(\x0b21.google.ads.googleads.v21.common.DynamicJobsAssetH\x00\x12M\n\x0elocation_asset\x18\' \x01(\x0b2..google.ads.googleads.v21.common.LocationAssetB\x03\xe0A\x03H\x00\x12X\n\x14hotel_property_asset\x18) \x01(\x0b23.google.ads.googleads.v21.common.HotelPropertyAssetB\x03\xe0A\x05H\x00\x12W\n\x16business_message_asset\x183 \x01(\x0b25.google.ads.googleads.v21.common.BusinessMessageAssetH\x00\x12U\n\x13app_deep_link_asset\x184 \x01(\x0b21.google.ads.googleads.v21.common.AppDeepLinkAssetB\x03\xe0A\x05H\x00\x12_\n\x18youtube_video_list_asset\x185 \x01(\x0b26.google.ads.googleads.v21.common.YouTubeVideoListAssetB\x03\xe0A\x05H\x00:N\xeaAK\n\x1egoogleads.googleapis.com/Asset\x12)customers/{customer_id}/assets/{asset_id}B\x0c\n\nasset_dataB\x05\n\x03_idB\x07\n\x05_nameB\x18\n\x16_tracking_url_templateB\x13\n\x11_final_url_suffix"\xfe\x02\n\x1bAssetFieldTypePolicySummary\x12e\n\x10asset_field_type\x18\x01 \x01(\x0e2A.google.ads.googleads.v21.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03H\x00\x88\x01\x01\x12[\n\x0casset_source\x18\x02 \x01(\x0e2;.google.ads.googleads.v21.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03H\x01\x88\x01\x01\x12]\n\x13policy_summary_info\x18\x03 \x01(\x0b26.google.ads.googleads.v21.resources.AssetPolicySummaryB\x03\xe0A\x03H\x02\x88\x01\x01B\x13\n\x11_asset_field_typeB\x0f\n\r_asset_sourceB\x16\n\x14_policy_summary_info"\xbe\x02\n\x12AssetPolicySummary\x12T\n\x14policy_topic_entries\x18\x01 \x03(\x0b21.google.ads.googleads.v21.common.PolicyTopicEntryB\x03\xe0A\x03\x12e\n\rreview_status\x18\x02 \x01(\x0e2I.google.ads.googleads.v21.enums.PolicyReviewStatusEnum.PolicyReviewStatusB\x03\xe0A\x03\x12k\n\x0fapproval_status\x18\x03 \x01(\x0e2M.google.ads.googleads.v21.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x03\xe0A\x03B\xfc\x01\n&com.google.ads.googleads.v21.resourcesB\nAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\nAssetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_ASSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ASSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_ASSET'].fields_by_name['id']._loaded_options = None
    _globals['_ASSET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['type']._loaded_options = None
    _globals['_ASSET'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['source']._loaded_options = None
    _globals['_ASSET'].fields_by_name['source']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['policy_summary']._loaded_options = None
    _globals['_ASSET'].fields_by_name['policy_summary']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['field_type_policy_summaries']._loaded_options = None
    _globals['_ASSET'].fields_by_name['field_type_policy_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['youtube_video_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['youtube_video_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['media_bundle_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['media_bundle_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['image_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['image_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['text_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['text_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['call_to_action_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['call_to_action_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['demand_gen_carousel_card_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['demand_gen_carousel_card_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['location_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['location_asset']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET'].fields_by_name['hotel_property_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['hotel_property_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['app_deep_link_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['app_deep_link_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET'].fields_by_name['youtube_video_list_asset']._loaded_options = None
    _globals['_ASSET'].fields_by_name['youtube_video_list_asset']._serialized_options = b'\xe0A\x05'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaAK\n\x1egoogleads.googleapis.com/Asset\x12)customers/{customer_id}/assets/{asset_id}'
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['asset_field_type']._loaded_options = None
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['asset_field_type']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['asset_source']._loaded_options = None
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['asset_source']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['policy_summary_info']._loaded_options = None
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY'].fields_by_name['policy_summary_info']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._loaded_options = None
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['review_status']._loaded_options = None
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['review_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['approval_status']._loaded_options = None
    _globals['_ASSETPOLICYSUMMARY'].fields_by_name['approval_status']._serialized_options = b'\xe0A\x03'
    _globals['_ASSET']._serialized_start = 575
    _globals['_ASSET']._serialized_end = 3901
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY']._serialized_start = 3904
    _globals['_ASSETFIELDTYPEPOLICYSUMMARY']._serialized_end = 4286
    _globals['_ASSETPOLICYSUMMARY']._serialized_start = 4289
    _globals['_ASSETPOLICYSUMMARY']._serialized_end = 4607