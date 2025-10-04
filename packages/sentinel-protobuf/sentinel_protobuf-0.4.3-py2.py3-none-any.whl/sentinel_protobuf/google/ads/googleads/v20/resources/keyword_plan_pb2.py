"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/keyword_plan.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import dates_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_dates__pb2
from ......google.ads.googleads.v20.enums import keyword_plan_forecast_interval_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_keyword__plan__forecast__interval__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ads/googleads/v20/resources/keyword_plan.proto\x12"google.ads.googleads.v20.resources\x1a+google/ads/googleads/v20/common/dates.proto\x1aCgoogle/ads/googleads/v20/enums/keyword_plan_forecast_interval.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc6\x02\n\x0bKeywordPlan\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$googleads.googleapis.com/KeywordPlan\x12\x14\n\x02id\x18\x05 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x06 \x01(\tH\x01\x88\x01\x01\x12V\n\x0fforecast_period\x18\x04 \x01(\x0b2=.google.ads.googleads.v20.resources.KeywordPlanForecastPeriod:a\xeaA^\n$googleads.googleapis.com/KeywordPlan\x126customers/{customer_id}/keywordPlans/{keyword_plan_id}B\x05\n\x03_idB\x07\n\x05_name"\xdf\x01\n\x19KeywordPlanForecastPeriod\x12t\n\rdate_interval\x18\x01 \x01(\x0e2[.google.ads.googleads.v20.enums.KeywordPlanForecastIntervalEnum.KeywordPlanForecastIntervalH\x00\x12@\n\ndate_range\x18\x02 \x01(\x0b2*.google.ads.googleads.v20.common.DateRangeH\x00B\n\n\x08intervalB\x82\x02\n&com.google.ads.googleads.v20.resourcesB\x10KeywordPlanProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.keyword_plan_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x10KeywordPlanProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_KEYWORDPLAN'].fields_by_name['resource_name']._loaded_options = None
    _globals['_KEYWORDPLAN'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$googleads.googleapis.com/KeywordPlan'
    _globals['_KEYWORDPLAN'].fields_by_name['id']._loaded_options = None
    _globals['_KEYWORDPLAN'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_KEYWORDPLAN']._loaded_options = None
    _globals['_KEYWORDPLAN']._serialized_options = b'\xeaA^\n$googleads.googleapis.com/KeywordPlan\x126customers/{customer_id}/keywordPlans/{keyword_plan_id}'
    _globals['_KEYWORDPLAN']._serialized_start = 268
    _globals['_KEYWORDPLAN']._serialized_end = 594
    _globals['_KEYWORDPLANFORECASTPERIOD']._serialized_start = 597
    _globals['_KEYWORDPLANFORECASTPERIOD']._serialized_end = 820