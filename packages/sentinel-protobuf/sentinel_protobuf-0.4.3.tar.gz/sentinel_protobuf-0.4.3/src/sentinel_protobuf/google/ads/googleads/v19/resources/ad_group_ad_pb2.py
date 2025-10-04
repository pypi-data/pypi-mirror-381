"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/ad_group_ad.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_policy__pb2
from ......google.ads.googleads.v19.enums import ad_group_ad_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_ad__group__ad__primary__status__pb2
from ......google.ads.googleads.v19.enums import ad_group_ad_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_ad__group__ad__primary__status__reason__pb2
from ......google.ads.googleads.v19.enums import ad_group_ad_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_ad__group__ad__status__pb2
from ......google.ads.googleads.v19.enums import ad_strength_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_ad__strength__pb2
from ......google.ads.googleads.v19.enums import asset_automation_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__automation__status__pb2
from ......google.ads.googleads.v19.enums import asset_automation_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_asset__automation__type__pb2
from ......google.ads.googleads.v19.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_policy__approval__status__pb2
from ......google.ads.googleads.v19.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_policy__review__status__pb2
from ......google.ads.googleads.v19.resources import ad_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_ad__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v19/resources/ad_group_ad.proto\x12"google.ads.googleads.v19.resources\x1a,google/ads/googleads/v19/common/policy.proto\x1a?google/ads/googleads/v19/enums/ad_group_ad_primary_status.proto\x1aFgoogle/ads/googleads/v19/enums/ad_group_ad_primary_status_reason.proto\x1a7google/ads/googleads/v19/enums/ad_group_ad_status.proto\x1a0google/ads/googleads/v19/enums/ad_strength.proto\x1a<google/ads/googleads/v19/enums/asset_automation_status.proto\x1a:google/ads/googleads/v19/enums/asset_automation_type.proto\x1a;google/ads/googleads/v19/enums/policy_approval_status.proto\x1a9google/ads/googleads/v19/enums/policy_review_status.proto\x1a+google/ads/googleads/v19/resources/ad.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x80\x08\n\tAdGroupAd\x12A\n\rresource_name\x18\x01 \x01(\tB*\xe0A\x05\xfaA$\n"googleads.googleapis.com/AdGroupAd\x12S\n\x06status\x18\x03 \x01(\x0e2C.google.ads.googleads.v19.enums.AdGroupAdStatusEnum.AdGroupAdStatus\x12?\n\x08ad_group\x18\t \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroupH\x00\x88\x01\x01\x127\n\x02ad\x18\x05 \x01(\x0b2&.google.ads.googleads.v19.resources.AdB\x03\xe0A\x05\x12W\n\x0epolicy_summary\x18\x06 \x01(\x0b2:.google.ads.googleads.v19.resources.AdGroupAdPolicySummaryB\x03\xe0A\x03\x12S\n\x0bad_strength\x18\x07 \x01(\x0e29.google.ads.googleads.v19.enums.AdStrengthEnum.AdStrengthB\x03\xe0A\x03\x12\x19\n\x0caction_items\x18\r \x03(\tB\x03\xe0A\x03\x12?\n\x06labels\x18\n \x03(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/AdGroupAdLabel\x12n\n\x0eprimary_status\x18\x10 \x01(\x0e2Q.google.ads.googleads.v19.enums.AdGroupAdPrimaryStatusEnum.AdGroupAdPrimaryStatusB\x03\xe0A\x03\x12\x82\x01\n\x16primary_status_reasons\x18\x11 \x03(\x0e2].google.ads.googleads.v19.enums.AdGroupAdPrimaryStatusReasonEnum.AdGroupAdPrimaryStatusReasonB\x03\xe0A\x03\x12r\n%ad_group_ad_asset_automation_settings\x18\x12 \x03(\x0b2C.google.ads.googleads.v19.resources.AdGroupAdAssetAutomationSetting:a\xeaA^\n"googleads.googleapis.com/AdGroupAd\x128customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}B\x0b\n\t_ad_group"\xc2\x02\n\x16AdGroupAdPolicySummary\x12T\n\x14policy_topic_entries\x18\x01 \x03(\x0b21.google.ads.googleads.v19.common.PolicyTopicEntryB\x03\xe0A\x03\x12e\n\rreview_status\x18\x02 \x01(\x0e2I.google.ads.googleads.v19.enums.PolicyReviewStatusEnum.PolicyReviewStatusB\x03\xe0A\x03\x12k\n\x0fapproval_status\x18\x03 \x01(\x0e2M.google.ads.googleads.v19.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\x03\xe0A\x03"\xbf\x02\n\x1fAdGroupAdAssetAutomationSetting\x12o\n\x15asset_automation_type\x18\x01 \x01(\x0e2K.google.ads.googleads.v19.enums.AssetAutomationTypeEnum.AssetAutomationTypeH\x00\x88\x01\x01\x12u\n\x17asset_automation_status\x18\x02 \x01(\x0e2O.google.ads.googleads.v19.enums.AssetAutomationStatusEnum.AssetAutomationStatusH\x01\x88\x01\x01B\x18\n\x16_asset_automation_typeB\x1a\n\x18_asset_automation_statusB\x80\x02\n&com.google.ads.googleads.v19.resourcesB\x0eAdGroupAdProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.ad_group_ad_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x0eAdGroupAdProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ADGROUPAD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA$\n"googleads.googleapis.com/AdGroupAd'
    _globals['_ADGROUPAD'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPAD'].fields_by_name['ad']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['ad']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPAD'].fields_by_name['policy_summary']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['policy_summary']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['ad_strength']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['ad_strength']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['action_items']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['action_items']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['labels']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/AdGroupAdLabel"
    _globals['_ADGROUPAD'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ADGROUPAD'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD']._loaded_options = None
    _globals['_ADGROUPAD']._serialized_options = b'\xeaA^\n"googleads.googleapis.com/AdGroupAd\x128customers/{customer_id}/adGroupAds/{ad_group_id}~{ad_id}'
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._loaded_options = None
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['policy_topic_entries']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['review_status']._loaded_options = None
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['review_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['approval_status']._loaded_options = None
    _globals['_ADGROUPADPOLICYSUMMARY'].fields_by_name['approval_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPAD']._serialized_start = 730
    _globals['_ADGROUPAD']._serialized_end = 1754
    _globals['_ADGROUPADPOLICYSUMMARY']._serialized_start = 1757
    _globals['_ADGROUPADPOLICYSUMMARY']._serialized_end = 2079
    _globals['_ADGROUPADASSETAUTOMATIONSETTING']._serialized_start = 2082
    _globals['_ADGROUPADASSETAUTOMATIONSETTING']._serialized_end = 2401