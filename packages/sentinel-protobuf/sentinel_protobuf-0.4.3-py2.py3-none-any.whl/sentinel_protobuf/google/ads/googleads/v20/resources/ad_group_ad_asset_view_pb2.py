"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_ad_asset_view.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_policy__pb2
from ......google.ads.googleads.v20.enums import asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__field__type__pb2
from ......google.ads.googleads.v20.enums import asset_performance_label_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__performance__label__pb2
from ......google.ads.googleads.v20.enums import asset_source_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_asset__source__pb2
from ......google.ads.googleads.v20.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_policy__approval__status__pb2
from ......google.ads.googleads.v20.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_policy__review__status__pb2
from ......google.ads.googleads.v20.enums import served_asset_field_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_served__asset__field__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v20/resources/ad_group_ad_asset_view.proto\x12"google.ads.googleads.v20.resources\x1a,google/ads/googleads/v20/common/policy.proto\x1a5google/ads/googleads/v20/enums/asset_field_type.proto\x1a<google/ads/googleads/v20/enums/asset_performance_label.proto\x1a1google/ads/googleads/v20/enums/asset_source.proto\x1a;google/ads/googleads/v20/enums/policy_approval_status.proto\x1a9google/ads/googleads/v20/enums/policy_review_status.proto\x1a<google/ads/googleads/v20/enums/served_asset_field_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x99\x07\n\x12AdGroupAdAssetView\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x03\xfaA-\n+googleads.googleapis.com/AdGroupAdAssetView\x12D\n\x0bad_group_ad\x18\t \x01(\tB*\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAdH\x00\x88\x01\x01\x12:\n\x05asset\x18\n \x01(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/AssetH\x01\x88\x01\x01\x12Z\n\nfield_type\x18\x02 \x01(\x0e2A.google.ads.googleads.v20.enums.AssetFieldTypeEnum.AssetFieldTypeB\x03\xe0A\x03\x12\x19\n\x07enabled\x18\x08 \x01(\x08B\x03\xe0A\x03H\x02\x88\x01\x01\x12\\\n\x0epolicy_summary\x18\x03 \x01(\x0b2?.google.ads.googleads.v20.resources.AdGroupAdAssetPolicySummaryB\x03\xe0A\x03\x12o\n\x11performance_label\x18\x04 \x01(\x0e2O.google.ads.googleads.v20.enums.AssetPerformanceLabelEnum.AssetPerformanceLabelB\x03\xe0A\x03\x12h\n\x0cpinned_field\x18\x0b \x01(\x0e2M.google.ads.googleads.v20.enums.ServedAssetFieldTypeEnum.ServedAssetFieldTypeB\x03\xe0A\x03\x12P\n\x06source\x18\x0c \x01(\x0e2;.google.ads.googleads.v20.enums.AssetSourceEnum.AssetSourceB\x03\xe0A\x03:\x8c\x01\xeaA\x88\x01\n+googleads.googleapis.com/AdGroupAdAssetView\x12Ycustomers/{customer_id}/adGroupAdAssetViews/{ad_group_id}~{ad_id}~{asset_id}~{field_type}B\x0e\n\x0c_ad_group_adB\x08\n\x06_assetB\n\n\x08_enabled"\xc7\x02\n\x1bAdGroupAdAssetPolicySummary\x12T\n\x14policy_topic_entries\x18\x01 \x03(\x0b21.google.ads.googleads.v20.common.PolicyTopicEntryB\x03\xe0A\x03\x12e\n\rreview_status\x18\x02 \x01(\x0e2I.google.ads.googleads.v20.enums.PolicyReviewStatusEnum.PolicyReviewStatusB\x03\xe0A\x03\x12k\n\x0fapproval_status\x18\x03 \x01(\x0e2M.google.ads.googleads.v20.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x03\xe0A\x03B\x89\x02\n&com.google.ads.googleads.v20.resourcesB\x17AdGroupAdAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_ad_asset_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x17AdGroupAdAssetViewProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA-\n+googleads.googleapis.com/AdGroupAdAssetView'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['ad_group_ad']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['ad_group_ad']._serialized_options = b'\xe0A\x03\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['asset']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['asset']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Asset'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['field_type']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['field_type']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['enabled']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['enabled']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['policy_summary']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['policy_summary']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['performance_label']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['performance_label']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['pinned_field']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['pinned_field']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['source']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW'].fields_by_name['source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW']._loaded_options = None
    _globals['_ADGROUPADASSETVIEW']._serialized_options = b'\xeaA\x88\x01\n+googleads.googleapis.com/AdGroupAdAssetView\x12Ycustomers/{customer_id}/adGroupAdAssetViews/{ad_group_id}~{ad_id}~{asset_id}~{field_type}'
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._loaded_options = None
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['review_status']._loaded_options = None
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['review_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['approval_status']._loaded_options = None
    _globals['_ADGROUPADASSETPOLICYSUMMARY'].fields_by_name['approval_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADASSETVIEW']._serialized_start = 560
    _globals['_ADGROUPADASSETVIEW']._serialized_end = 1481
    _globals['_ADGROUPADASSETPOLICYSUMMARY']._serialized_start = 1484
    _globals['_ADGROUPADASSETPOLICYSUMMARY']._serialized_end = 1811