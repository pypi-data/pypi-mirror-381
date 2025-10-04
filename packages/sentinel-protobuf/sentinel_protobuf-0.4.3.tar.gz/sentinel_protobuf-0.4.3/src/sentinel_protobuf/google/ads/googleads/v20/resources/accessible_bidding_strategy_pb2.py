"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/accessible_bidding_strategy.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_bidding__strategy__type__pb2
from ......google.ads.googleads.v20.enums import target_impression_share_location_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_target__impression__share__location__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/ads/googleads/v20/resources/accessible_bidding_strategy.proto\x12"google.ads.googleads.v20.resources\x1a:google/ads/googleads/v20/enums/bidding_strategy_type.proto\x1aEgoogle/ads/googleads/v20/enums/target_impression_share_location.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x90\x0e\n\x19AccessibleBiddingStrategy\x12Q\n\rresource_name\x18\x01 \x01(\tB:\xe0A\x03\xfaA4\n2googleads.googleapis.com/AccessibleBiddingStrategy\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x03\x12^\n\x04type\x18\x04 \x01(\x0e2K.google.ads.googleads.v20.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeB\x03\xe0A\x03\x12\x1e\n\x11owner_customer_id\x18\x05 \x01(\x03B\x03\xe0A\x03\x12#\n\x16owner_descriptive_name\x18\x06 \x01(\tB\x03\xe0A\x03\x12\x7f\n\x19maximize_conversion_value\x18\x07 \x01(\x0b2U.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.MaximizeConversionValueB\x03\xe0A\x03H\x00\x12v\n\x14maximize_conversions\x18\x08 \x01(\x0b2Q.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.MaximizeConversionsB\x03\xe0A\x03H\x00\x12b\n\ntarget_cpa\x18\t \x01(\x0b2G.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.TargetCpaB\x03\xe0A\x03H\x00\x12{\n\x17target_impression_share\x18\n \x01(\x0b2S.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.TargetImpressionShareB\x03\xe0A\x03H\x00\x12d\n\x0btarget_roas\x18\x0b \x01(\x0b2H.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.TargetRoasB\x03\xe0A\x03H\x00\x12f\n\x0ctarget_spend\x18\x0c \x01(\x0b2I.google.ads.googleads.v20.resources.AccessibleBiddingStrategy.TargetSpendB\x03\xe0A\x03H\x00\x1a3\n\x17MaximizeConversionValue\x12\x18\n\x0btarget_roas\x18\x01 \x01(\x01B\x03\xe0A\x03\x1a5\n\x13MaximizeConversions\x12\x1e\n\x11target_cpa_micros\x18\x02 \x01(\x03B\x03\xe0A\x03\x1aF\n\tTargetCpa\x12#\n\x11target_cpa_micros\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01B\x14\n\x12_target_cpa_micros\x1a\x98\x02\n\x15TargetImpressionShare\x12v\n\x08location\x18\x01 \x01(\x0e2_.google.ads.googleads.v20.enums.TargetImpressionShareLocationEnum.TargetImpressionShareLocationB\x03\xe0A\x03\x12%\n\x18location_fraction_micros\x18\x02 \x01(\x03H\x00\x88\x01\x01\x12(\n\x16cpc_bid_ceiling_micros\x18\x03 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01B\x1b\n\x19_location_fraction_microsB\x19\n\x17_cpc_bid_ceiling_micros\x1a;\n\nTargetRoas\x12\x1d\n\x0btarget_roas\x18\x01 \x01(\x01B\x03\xe0A\x03H\x00\x88\x01\x01B\x0e\n\x0c_target_roas\x1a\x93\x01\n\x0bTargetSpend\x12\'\n\x13target_spend_micros\x18\x01 \x01(\x03B\x05\x18\x01\xe0A\x03H\x00\x88\x01\x01\x12(\n\x16cpc_bid_ceiling_micros\x18\x02 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01B\x16\n\x14_target_spend_microsB\x19\n\x17_cpc_bid_ceiling_micros:\x82\x01\xeaA\x7f\n2googleads.googleapis.com/AccessibleBiddingStrategy\x12Icustomers/{customer_id}/accessibleBiddingStrategies/{bidding_strategy_id}B\x08\n\x06schemeB\x90\x02\n&com.google.ads.googleads.v20.resourcesB\x1eAccessibleBiddingStrategyProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.accessible_bidding_strategy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1eAccessibleBiddingStrategyProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONVALUE'].fields_by_name['target_roas']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONVALUE'].fields_by_name['target_roas']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONS'].fields_by_name['target_cpa_micros']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONS'].fields_by_name['target_cpa_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETCPA'].fields_by_name['target_cpa_micros']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETCPA'].fields_by_name['target_cpa_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE'].fields_by_name['location']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE'].fields_by_name['cpc_bid_ceiling_micros']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE'].fields_by_name['cpc_bid_ceiling_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETROAS'].fields_by_name['target_roas']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETROAS'].fields_by_name['target_roas']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND'].fields_by_name['target_spend_micros']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND'].fields_by_name['target_spend_micros']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND'].fields_by_name['cpc_bid_ceiling_micros']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND'].fields_by_name['cpc_bid_ceiling_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA4\n2googleads.googleapis.com/AccessibleBiddingStrategy'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['id']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['type']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['owner_customer_id']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['owner_customer_id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['owner_descriptive_name']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['owner_descriptive_name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['maximize_conversion_value']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['maximize_conversion_value']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['maximize_conversions']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['maximize_conversions']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_cpa']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_cpa']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_impression_share']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_impression_share']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_roas']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_roas']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_spend']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY'].fields_by_name['target_spend']._serialized_options = b'\xe0A\x03'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY']._loaded_options = None
    _globals['_ACCESSIBLEBIDDINGSTRATEGY']._serialized_options = b'\xeaA\x7f\n2googleads.googleapis.com/AccessibleBiddingStrategy\x12Icustomers/{customer_id}/accessibleBiddingStrategies/{bidding_strategy_id}'
    _globals['_ACCESSIBLEBIDDINGSTRATEGY']._serialized_start = 300
    _globals['_ACCESSIBLEBIDDINGSTRATEGY']._serialized_end = 2108
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONVALUE']._serialized_start = 1293
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONVALUE']._serialized_end = 1344
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONS']._serialized_start = 1346
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_MAXIMIZECONVERSIONS']._serialized_end = 1399
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETCPA']._serialized_start = 1401
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETCPA']._serialized_end = 1471
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE']._serialized_start = 1474
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETIMPRESSIONSHARE']._serialized_end = 1754
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETROAS']._serialized_start = 1756
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETROAS']._serialized_end = 1815
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND']._serialized_start = 1818
    _globals['_ACCESSIBLEBIDDINGSTRATEGY_TARGETSPEND']._serialized_end = 1965