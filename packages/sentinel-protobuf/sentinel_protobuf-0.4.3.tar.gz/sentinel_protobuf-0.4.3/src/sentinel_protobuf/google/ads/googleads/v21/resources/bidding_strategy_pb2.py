"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/bidding_strategy.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import bidding_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_bidding__pb2
from ......google.ads.googleads.v21.enums import bidding_strategy_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_bidding__strategy__status__pb2
from ......google.ads.googleads.v21.enums import bidding_strategy_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_bidding__strategy__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v21/resources/bidding_strategy.proto\x12"google.ads.googleads.v21.resources\x1a-google/ads/googleads/v21/common/bidding.proto\x1a<google/ads/googleads/v21/enums/bidding_strategy_status.proto\x1a:google/ads/googleads/v21/enums/bidding_strategy_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfe\t\n\x0fBiddingStrategy\x12G\n\rresource_name\x18\x01 \x01(\tB0\xe0A\x05\xfaA*\n(googleads.googleapis.com/BiddingStrategy\x12\x14\n\x02id\x18\x10 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x11 \x01(\tH\x02\x88\x01\x01\x12d\n\x06status\x18\x0f \x01(\x0e2O.google.ads.googleads.v21.enums.BiddingStrategyStatusEnum.BiddingStrategyStatusB\x03\xe0A\x03\x12^\n\x04type\x18\x05 \x01(\x0e2K.google.ads.googleads.v21.enums.BiddingStrategyTypeEnum.BiddingStrategyTypeB\x03\xe0A\x03\x12\x1a\n\rcurrency_code\x18\x17 \x01(\tB\x03\xe0A\x05\x12)\n\x17effective_currency_code\x18\x14 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12"\n\x1aaligned_campaign_budget_id\x18\x19 \x01(\x03\x12 \n\x0ecampaign_count\x18\x12 \x01(\x03B\x03\xe0A\x03H\x04\x88\x01\x01\x12,\n\x1anon_removed_campaign_count\x18\x13 \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12D\n\x0cenhanced_cpc\x18\x07 \x01(\x0b2,.google.ads.googleads.v21.common.EnhancedCpcH\x00\x12]\n\x19maximize_conversion_value\x18\x15 \x01(\x0b28.google.ads.googleads.v21.common.MaximizeConversionValueH\x00\x12T\n\x14maximize_conversions\x18\x16 \x01(\x0b24.google.ads.googleads.v21.common.MaximizeConversionsH\x00\x12@\n\ntarget_cpa\x18\t \x01(\x0b2*.google.ads.googleads.v21.common.TargetCpaH\x00\x12Y\n\x17target_impression_share\x180 \x01(\x0b26.google.ads.googleads.v21.common.TargetImpressionShareH\x00\x12B\n\x0btarget_roas\x18\x0b \x01(\x0b2+.google.ads.googleads.v21.common.TargetRoasH\x00\x12D\n\x0ctarget_spend\x18\x0c \x01(\x0b2,.google.ads.googleads.v21.common.TargetSpendH\x00:n\xeaAk\n(googleads.googleapis.com/BiddingStrategy\x12?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}B\x08\n\x06schemeB\x05\n\x03_idB\x07\n\x05_nameB\x1a\n\x18_effective_currency_codeB\x11\n\x0f_campaign_countB\x1d\n\x1b_non_removed_campaign_countB\x86\x02\n&com.google.ads.googleads.v21.resourcesB\x14BiddingStrategyProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.bidding_strategy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x14BiddingStrategyProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['resource_name']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA*\n(googleads.googleapis.com/BiddingStrategy'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['id']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['status']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['type']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['currency_code']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x05'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['effective_currency_code']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['effective_currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['campaign_count']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['campaign_count']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY'].fields_by_name['non_removed_campaign_count']._loaded_options = None
    _globals['_BIDDINGSTRATEGY'].fields_by_name['non_removed_campaign_count']._serialized_options = b'\xe0A\x03'
    _globals['_BIDDINGSTRATEGY']._loaded_options = None
    _globals['_BIDDINGSTRATEGY']._serialized_options = b'\xeaAk\n(googleads.googleapis.com/BiddingStrategy\x12?customers/{customer_id}/biddingStrategies/{bidding_strategy_id}'
    _globals['_BIDDINGSTRATEGY']._serialized_start = 327
    _globals['_BIDDINGSTRATEGY']._serialized_end = 1605