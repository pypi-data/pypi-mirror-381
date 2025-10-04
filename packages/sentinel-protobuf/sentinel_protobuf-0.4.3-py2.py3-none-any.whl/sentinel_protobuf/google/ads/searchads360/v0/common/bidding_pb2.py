"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/common/bidding.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import target_impression_share_location_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_target__impression__share__location__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/ads/searchads360/v0/common/bidding.proto\x12!google.ads.searchads360.v0.common\x1aGgoogle/ads/searchads360/v0/enums/target_impression_share_location.proto\x1a\x1egoogle/protobuf/wrappers.proto"\r\n\x0bEnhancedCpc"\x0b\n\tManualCpa"G\n\tManualCpc\x12!\n\x14enhanced_cpc_enabled\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_enhanced_cpc_enabled"\x0b\n\tManualCpm"n\n\x13MaximizeConversions\x12\x1e\n\x16cpc_bid_ceiling_micros\x18\x02 \x01(\x03\x12\x1c\n\x14cpc_bid_floor_micros\x18\x03 \x01(\x03\x12\x19\n\x11target_cpa_micros\x18\x04 \x01(\x03"\x81\x01\n\x17MaximizeConversionValue\x12\x18\n\x0btarget_roas\x18\x02 \x01(\x01H\x00\x88\x01\x01\x12\x1e\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x03\x12\x1c\n\x14cpc_bid_floor_micros\x18\x04 \x01(\x03B\x0e\n\x0c_target_roas"\xbd\x01\n\tTargetCpa\x12\x1e\n\x11target_cpa_micros\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12!\n\x14cpc_bid_floor_micros\x18\x06 \x01(\x03H\x02\x88\x01\x01B\x14\n\x12_target_cpa_microsB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros"\x0b\n\tTargetCpm"\x90\x02\n\x15TargetImpressionShare\x12s\n\x08location\x18\x01 \x01(\x0e2a.google.ads.searchads360.v0.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocation\x12%\n\x18location_fraction_micros\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01B\x1b\n\x19_location_fraction_microsB\x19\n\x17_cpc_bid_ceiling_micros"Q\n\x12TargetOutrankShare\x12;\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int64Value"\xb2\x01\n\nTargetRoas\x12\x18\n\x0btarget_roas\x18\x04 \x01(\x01H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x05 \x01(\x03H\x01\x88\x01\x01\x12!\n\x14cpc_bid_floor_micros\x18\x06 \x01(\x03H\x02\x88\x01\x01B\x0e\n\x0c_target_roasB\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_cpc_bid_floor_micros"\x8b\x01\n\x0bTargetSpend\x12$\n\x13target_spend_micros\x18\x03 \x01(\x03B\x02\x18\x01H\x00\x88\x01\x01\x12#\n\x16cpc_bid_ceiling_micros\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x16\n\x14_target_spend_microsB\x19\n\x17_cpc_bid_ceiling_micros"\x88\x01\n\nPercentCpc\x12#\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12!\n\x14enhanced_cpc_enabled\x18\x04 \x01(\x08H\x01\x88\x01\x01B\x19\n\x17_cpc_bid_ceiling_microsB\x17\n\x15_enhanced_cpc_enabledB\xfa\x01\n%com.google.ads.searchads360.v0.commonB\x0cBiddingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.common.bidding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.commonB\x0cBiddingProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Common'
    _globals['_TARGETSPEND'].fields_by_name['target_spend_micros']._loaded_options = None
    _globals['_TARGETSPEND'].fields_by_name['target_spend_micros']._serialized_options = b'\x18\x01'
    _globals['_ENHANCEDCPC']._serialized_start = 191
    _globals['_ENHANCEDCPC']._serialized_end = 204
    _globals['_MANUALCPA']._serialized_start = 206
    _globals['_MANUALCPA']._serialized_end = 217
    _globals['_MANUALCPC']._serialized_start = 219
    _globals['_MANUALCPC']._serialized_end = 290
    _globals['_MANUALCPM']._serialized_start = 292
    _globals['_MANUALCPM']._serialized_end = 303
    _globals['_MAXIMIZECONVERSIONS']._serialized_start = 305
    _globals['_MAXIMIZECONVERSIONS']._serialized_end = 415
    _globals['_MAXIMIZECONVERSIONVALUE']._serialized_start = 418
    _globals['_MAXIMIZECONVERSIONVALUE']._serialized_end = 547
    _globals['_TARGETCPA']._serialized_start = 550
    _globals['_TARGETCPA']._serialized_end = 739
    _globals['_TARGETCPM']._serialized_start = 741
    _globals['_TARGETCPM']._serialized_end = 752
    _globals['_TARGETIMPRESSIONSHARE']._serialized_start = 755
    _globals['_TARGETIMPRESSIONSHARE']._serialized_end = 1027
    _globals['_TARGETOUTRANKSHARE']._serialized_start = 1029
    _globals['_TARGETOUTRANKSHARE']._serialized_end = 1110
    _globals['_TARGETROAS']._serialized_start = 1113
    _globals['_TARGETROAS']._serialized_end = 1291
    _globals['_TARGETSPEND']._serialized_start = 1294
    _globals['_TARGETSPEND']._serialized_end = 1433
    _globals['_PERCENTCPC']._serialized_start = 1436
    _globals['_PERCENTCPC']._serialized_end = 1572