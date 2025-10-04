"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/ad_asset.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import asset_policy_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_asset__policy__pb2
from ......google.ads.googleads.v19.enums import asset_performance_label_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__performance__label__pb2
from ......google.ads.googleads.v19.enums import served_asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_served__asset__field__type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/googleads/v19/common/ad_asset.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a2google/ads/googleads/v19/common/asset_policy.proto\x1a<google/ads/googleads/v19/enums/asset_performance_label.proto\x1a<google/ads/googleads/v19/enums/served_asset_field_type.proto"\xd4\x02\n\x0bAdTextAsset\x12\x11\n\x04text\x18\x04 \x01(\tH\x00\x88\x01\x01\x12c\n\x0cpinned_field\x18\x02 \x01(\x0e2M.google.ads.googleads.v19.enums.ServedAssetFieldTypeEnum.ServedAssetFieldType\x12p\n\x17asset_performance_label\x18\x05 \x01(\x0e2O.google.ads.googleads.v19.enums.AssetPerformanceLabelEnum.AssetPerformanceLabel\x12R\n\x13policy_summary_info\x18\x06 \x01(\x0b25.google.ads.googleads.v19.common.AdAssetPolicySummaryB\x07\n\x05_text",\n\x0cAdImageAsset\x12\x12\n\x05asset\x18\x02 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_asset"\x99\x01\n\x0cAdVideoAsset\x12\x12\n\x05asset\x18\x02 \x01(\tH\x00\x88\x01\x01\x12S\n\x13ad_video_asset_info\x18\x04 \x01(\x0b21.google.ads.googleads.v19.common.AdVideoAssetInfoH\x01\x88\x01\x01B\x08\n\x06_assetB\x16\n\x14_ad_video_asset_info"\xb1\x01\n\x10AdVideoAssetInfo\x12t\n$ad_video_asset_inventory_preferences\x18\x01 \x01(\x0b2A.google.ads.googleads.v19.common.AdVideoAssetInventoryPreferencesH\x00\x88\x01\x01B\'\n%_ad_video_asset_inventory_preferences"\xcc\x01\n AdVideoAssetInventoryPreferences\x12\x1f\n\x12in_feed_preference\x18\x01 \x01(\x08H\x00\x88\x01\x01\x12!\n\x14in_stream_preference\x18\x02 \x01(\x08H\x01\x88\x01\x01\x12\x1e\n\x11shorts_preference\x18\x03 \x01(\x08H\x02\x88\x01\x01B\x15\n\x13_in_feed_preferenceB\x17\n\x15_in_stream_preferenceB\x14\n\x12_shorts_preference"2\n\x12AdMediaBundleAsset\x12\x12\n\x05asset\x18\x02 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_asset"<\n\x1cAdDemandGenCarouselCardAsset\x12\x12\n\x05asset\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_asset"3\n\x13AdCallToActionAsset\x12\x12\n\x05asset\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_asset"2\n\x12AdAppDeepLinkAsset\x12\x12\n\x05asset\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_assetB\xec\x01\n#com.google.ads.googleads.v19.commonB\x0cAdAssetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.ad_asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x0cAdAssetProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_ADTEXTASSET']._serialized_start = 260
    _globals['_ADTEXTASSET']._serialized_end = 600
    _globals['_ADIMAGEASSET']._serialized_start = 602
    _globals['_ADIMAGEASSET']._serialized_end = 646
    _globals['_ADVIDEOASSET']._serialized_start = 649
    _globals['_ADVIDEOASSET']._serialized_end = 802
    _globals['_ADVIDEOASSETINFO']._serialized_start = 805
    _globals['_ADVIDEOASSETINFO']._serialized_end = 982
    _globals['_ADVIDEOASSETINVENTORYPREFERENCES']._serialized_start = 985
    _globals['_ADVIDEOASSETINVENTORYPREFERENCES']._serialized_end = 1189
    _globals['_ADMEDIABUNDLEASSET']._serialized_start = 1191
    _globals['_ADMEDIABUNDLEASSET']._serialized_end = 1241
    _globals['_ADDEMANDGENCAROUSELCARDASSET']._serialized_start = 1243
    _globals['_ADDEMANDGENCAROUSELCARDASSET']._serialized_end = 1303
    _globals['_ADCALLTOACTIONASSET']._serialized_start = 1305
    _globals['_ADCALLTOACTIONASSET']._serialized_end = 1356
    _globals['_ADAPPDEEPLINKASSET']._serialized_start = 1358
    _globals['_ADAPPDEEPLINKASSET']._serialized_end = 1408