"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/policy_summary.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import policy_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_policy__pb2
from ......google.ads.googleads.v19.enums import policy_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_policy__approval__status__pb2
from ......google.ads.googleads.v19.enums import policy_review_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_policy__review__status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/googleads/v19/common/policy_summary.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a,google/ads/googleads/v19/common/policy.proto\x1a;google/ads/googleads/v19/enums/policy_approval_status.proto\x1a9google/ads/googleads/v19/enums/policy_review_status.proto"\xaa\x02\n\rPolicySummary\x12O\n\x14policy_topic_entries\x18\x01 \x03(\x0b21.google.ads.googleads.v19.common.PolicyTopicEntry\x12`\n\rreview_status\x18\x02 \x01(\x0e2I.google.ads.googleads.v19.enums.PolicyReviewStatusEnum.PolicyReviewStatus\x12f\n\x0fapproval_status\x18\x03 \x01(\x0e2M.google.ads.googleads.v19.enums.PolicyApprovalStatusEnum.PolicyApprovalStatusB\xf2\x01\n#com.google.ads.googleads.v19.commonB\x12PolicySummaryProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.policy_summary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x12PolicySummaryProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_POLICYSUMMARY']._serialized_start = 256
    _globals['_POLICYSUMMARY']._serialized_end = 554