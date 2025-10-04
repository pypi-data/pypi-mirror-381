"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/common/asset_policy.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_policy__pb2
from ......google.ads.googleads.v21.enums import asset_link_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__link__primary__status__pb2
from ......google.ads.googleads.v21.enums import asset_link_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__link__primary__status__reason__pb2
from ......google.ads.googleads.v21.enums import asset_offline_evaluation_error_reasons_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_asset__offline__evaluation__error__reasons__pb2
from ......google.ads.googleads.v21.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_policy__approval__status__pb2
from ......google.ads.googleads.v21.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_policy__review__status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v21/common/asset_policy.proto\x12\x1fgoogle.ads.googleads.v21.common\x1a,google/ads/googleads/v21/common/policy.proto\x1a>google/ads/googleads/v21/enums/asset_link_primary_status.proto\x1aEgoogle/ads/googleads/v21/enums/asset_link_primary_status_reason.proto\x1aKgoogle/ads/googleads/v21/enums/asset_offline_evaluation_error_reasons.proto\x1a;google/ads/googleads/v21/enums/policy_approval_status.proto\x1a9google/ads/googleads/v21/enums/policy_review_status.proto"\xb1\x02\n\x14AdAssetPolicySummary\x12O\n\x14policy_topic_entries\x18\x01 \x03(\x0b21.google.ads.googleads.v21.common.PolicyTopicEntry\x12`\n\rreview_status\x18\x02 \x01(\x0e2I.google.ads.googleads.v21.enums.PolicyReviewStatusEnum.PolicyReviewStatus\x12f\n\x0fapproval_status\x18\x03 \x01(\x0e2M.google.ads.googleads.v21.enums.PolicyApprovalStatusEnum.PolicyApprovalStatus"\xec\x02\n\x1dAssetLinkPrimaryStatusDetails\x12r\n\x06reason\x18\x01 \x01(\x0e2].google.ads.googleads.v21.enums.AssetLinkPrimaryStatusReasonEnum.AssetLinkPrimaryStatusReasonH\x01\x88\x01\x01\x12f\n\x06status\x18\x02 \x01(\x0e2Q.google.ads.googleads.v21.enums.AssetLinkPrimaryStatusEnum.AssetLinkPrimaryStatusH\x02\x88\x01\x01\x12N\n\x11asset_disapproved\x18\x03 \x01(\x0b21.google.ads.googleads.v21.common.AssetDisapprovedH\x00B\t\n\x07detailsB\t\n\x07_reasonB\t\n\x07_status"\xa8\x01\n\x10AssetDisapproved\x12\x93\x01\n offline_evaluation_error_reasons\x18\x01 \x03(\x0e2i.google.ads.googleads.v21.enums.AssetOfflineEvaluationErrorReasonsEnum.AssetOfflineEvaluationErrorReasonsB\xf0\x01\n#com.google.ads.googleads.v21.commonB\x10AssetPolicyProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.common.asset_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v21.commonB\x10AssetPolicyProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Common'
    _globals['_ADASSETPOLICYSUMMARY']._serialized_start = 466
    _globals['_ADASSETPOLICYSUMMARY']._serialized_end = 771
    _globals['_ASSETLINKPRIMARYSTATUSDETAILS']._serialized_start = 774
    _globals['_ASSETLINKPRIMARYSTATUSDETAILS']._serialized_end = 1138
    _globals['_ASSETDISAPPROVED']._serialized_start = 1141
    _globals['_ASSETDISAPPROVED']._serialized_end = 1309