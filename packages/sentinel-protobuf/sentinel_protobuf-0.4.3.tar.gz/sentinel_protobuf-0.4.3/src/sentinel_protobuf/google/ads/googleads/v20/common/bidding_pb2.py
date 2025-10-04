"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/common/bidding.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import fixed_cpm_goal_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_fixed__cpm__goal__pb2
from ......google.ads.googleads.v20.enums import fixed_cpm_target_frequency_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_fixed__cpm__target__frequency__time__unit__pb2
from ......google.ads.googleads.v20.enums import target_frequency_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_target__frequency__time__unit__pb2
from ......google.ads.googleads.v20.enums import target_impression_share_location_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_target__impression__share__location__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/ads/googleads/v20/common/bidding.proto\x12\x1fgoogle.ads.googleads.v20.common\x1a3google/ads/googleads/v20/enums/fixed_cpm_goal.proto\x1aIgoogle/ads/googleads/v20/enums/fixed_cpm_target_frequency_time_unit.proto\x1a?google/ads/googleads/v20/enums/target_frequency_time_unit.proto\x1aEgoogle/ads/googleads/v20/enums/target_impression_share_location.proto"L\n\nCommission\x12#\n\x16commission_rate_micros\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x19\n\x17_commission_rate_micros"\r\n\x0bEnhancedCpc"\x0b\n\tManualCpa"G\n\tManualCpc\x12!\n\x14enhanced_cpc_enabled\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_enhanced_cpc_enabled"\x0b\n\tManualCpm"\x0b\n\tManualCpv"n\n\x13MaximizeConversions\x12\x1e\n\x16cpc_bid_ceiling_micros\x18\x02 \x01(\x03\x12\x1c\n\x14cpc_bid_floor_micros\x18\x03 \x01(\x03\x12\x19\n\x11target_cpa_micros\x18\x04 \x01(\x03"l\n\x17MaximizeConversionValue\x12\x13\n\x0btarget_roas\x18\x02 \x01(\x01\x12\x1e\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x03\x12\x1c\n\x14cpc_bid_floor_micros\x18\x04 \x01(\x03"\xbd\x01\n\tTargetCpa\x12\x1e\n\x11target_cpa_micros\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12!\n\x14cpc_bid_floor_micros\x18\x06 \x01(\x03H\x02\x88\x01\x01B\x14\n\x12_target_cpa_microsB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros"s\n\tTargetCpm\x12^\n\x15target_frequency_goal\x18\x01 \x01(\x0b2=.google.ads.googleads.v20.common.TargetCpmTargetFrequencyGoalH\x00B\x06\n\x04goal"\x9c\x01\n\x1cTargetCpmTargetFrequencyGoal\x12\x14\n\x0ctarget_count\x18\x01 \x01(\x03\x12f\n\ttime_unit\x18\x02 \x01(\x0e2S.google.ads.googleads.v20.enums.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnit"\x8e\x02\n\x15TargetImpressionShare\x12q\n\x08location\x18\x01 \x01(\x0e2_.google.ads.googleads.v20.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocation\x12%\n\x18location_fraction_micros\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01B\x1b\n\x19_location_fraction_microsB\x19\n\x17_cpc_bid_ceiling_micros"\xb2\x01\n\nTargetRoas\x12\x18\n\x0btarget_roas\x18\x04 \x01(\x01H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12!\n\x14cpc_bid_floor_micros\x18\x06 \x01(\x03H\x02\x88\x01\x01B\x0e\n\x0c_target_roasB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros"\x8b\x01\n\x0bTargetSpend\x12$\n\x13target_spend_micros\x18\x03 \x01(\x03B\x02\x18\x01H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x16\n\x14_target_spend_microsB\x19\n\x17_cpc_bid_ceiling_micros"\x88\x01\n\nPercentCpc\x12#\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12!\n\x14enhanced_cpc_enabled\x18\x04 \x01(\x08H\x01\x88\x01\x01B\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_enhanced_cpc_enabled"\xc7\x01\n\x08FixedCpm\x12K\n\x04goal\x18\x01 \x01(\x0e2=.google.ads.googleads.v20.enums.FixedCpmGoalEnum.FixedCpmGoal\x12a\n\x15target_frequency_info\x18\x02 \x01(\x0b2@.google.ads.googleads.v20.common.FixedCpmTargetFrequencyGoalInfoH\x00B\x0b\n\tgoal_info"\xaf\x01\n\x1fFixedCpmTargetFrequencyGoalInfo\x12\x14\n\x0ctarget_count\x18\x01 \x01(\x03\x12v\n\ttime_unit\x18\x02 \x01(\x0e2c.google.ads.googleads.v20.enums.FixedCpmTargetFrequencyTimeUnitEnum.FixedCpmTargetFrequencyTimeUnit"\x0b\n\tTargetCpvB\xec\x01\n#com.google.ads.googleads.v20.commonB\x0cBiddingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.common.bidding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v20.commonB\x0cBiddingProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v20/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V20.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V20\\Common\xea\x02#Google::Ads::GoogleAds::V20::Common'
    _globals['_TARGETSPEND'].fields_by_name['target_spend_micros']._loaded_options = None
    _globals['_TARGETSPEND'].fields_by_name['target_spend_micros']._serialized_options = b'\x18\x01'
    _globals['_COMMISSION']._serialized_start = 346
    _globals['_COMMISSION']._serialized_end = 422
    _globals['_ENHANCEDCPC']._serialized_start = 424
    _globals['_ENHANCEDCPC']._serialized_end = 437
    _globals['_MANUALCPA']._serialized_start = 439
    _globals['_MANUALCPA']._serialized_end = 450
    _globals['_MANUALCPC']._serialized_start = 452
    _globals['_MANUALCPC']._serialized_end = 523
    _globals['_MANUALCPM']._serialized_start = 525
    _globals['_MANUALCPM']._serialized_end = 536
    _globals['_MANUALCPV']._serialized_start = 538
    _globals['_MANUALCPV']._serialized_end = 549
    _globals['_MAXIMIZECONVERSIONS']._serialized_start = 551
    _globals['_MAXIMIZECONVERSIONS']._serialized_end = 661
    _globals['_MAXIMIZECONVERSIONVALUE']._serialized_start = 663
    _globals['_MAXIMIZECONVERSIONVALUE']._serialized_end = 771
    _globals['_TARGETCPA']._serialized_start = 774
    _globals['_TARGETCPA']._serialized_end = 963
    _globals['_TARGETCPM']._serialized_start = 965
    _globals['_TARGETCPM']._serialized_end = 1080
    _globals['_TARGETCPMTARGETFREQUENCYGOAL']._serialized_start = 1083
    _globals['_TARGETCPMTARGETFREQUENCYGOAL']._serialized_end = 1239
    _globals['_TARGETIMPRESSIONSHARE']._serialized_start = 1242
    _globals['_TARGETIMPRESSIONSHARE']._serialized_end = 1512
    _globals['_TARGETROAS']._serialized_start = 1515
    _globals['_TARGETROAS']._serialized_end = 1693
    _globals['_TARGETSPEND']._serialized_start = 1696
    _globals['_TARGETSPEND']._serialized_end = 1835
    _globals['_PERCENTCPC']._serialized_start = 1838
    _globals['_PERCENTCPC']._serialized_end = 1974
    _globals['_FIXEDCPM']._serialized_start = 1977
    _globals['_FIXEDCPM']._serialized_end = 2176
    _globals['_FIXEDCPMTARGETFREQUENCYGOALINFO']._serialized_start = 2179
    _globals['_FIXEDCPMTARGETFREQUENCYGOALINFO']._serialized_end = 2354
    _globals['_TARGETCPV']._serialized_start = 2356
    _globals['_TARGETCPV']._serialized_end = 2367