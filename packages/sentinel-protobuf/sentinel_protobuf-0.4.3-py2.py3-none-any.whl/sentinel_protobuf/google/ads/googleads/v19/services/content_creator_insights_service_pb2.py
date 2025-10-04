"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/content_creator_insights_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import audience_insights_attribute_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_audience__insights__attribute__pb2
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.enums import insights_trend_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_insights__trend__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/ads/googleads/v19/services/content_creator_insights_service.proto\x12!google.ads.googleads.v19.services\x1aAgoogle/ads/googleads/v19/common/audience_insights_attribute.proto\x1a.google/ads/googleads/v19/common/criteria.proto\x1a3google/ads/googleads/v19/enums/insights_trend.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xc6\x07\n\x1eGenerateCreatorInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x02 \x01(\tB\x03\xe0A\x02\x12M\n\x11country_locations\x18\x06 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12o\n\x11search_attributes\x18\x03 \x01(\x0b2R.google.ads.googleads.v19.services.GenerateCreatorInsightsRequest.SearchAttributesH\x00\x12e\n\x0csearch_brand\x18\x05 \x01(\x0b2M.google.ads.googleads.v19.services.GenerateCreatorInsightsRequest.SearchBrandH\x00\x12l\n\x0fsearch_channels\x18\x04 \x01(\x0b2Q.google.ads.googleads.v19.services.GenerateCreatorInsightsRequest.YouTubeChannelsH\x00\x1a\xcd\x01\n\x10SearchAttributes\x12\\\n\x13audience_attributes\x18\x01 \x03(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x01\x12[\n\x12creator_attributes\x18\x02 \x03(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x01\x1a\x8b\x01\n\x0bSearchBrand\x12W\n\x0ebrand_entities\x18\x01 \x03(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x01\x12#\n\x16include_related_topics\x18\x02 \x01(\x08B\x03\xe0A\x01\x1ae\n\x0fYouTubeChannels\x12R\n\x10youtube_channels\x18\x01 \x03(\x0b23.google.ads.googleads.v19.common.YouTubeChannelInfoB\x03\xe0A\x01B\n\n\x08criteria"v\n\x1fGenerateCreatorInsightsResponse\x12S\n\x10creator_insights\x18\x01 \x03(\x0b29.google.ads.googleads.v19.services.YouTubeCreatorInsights"\xd3\x02\n\x1fGenerateTrendingInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\x10country_location\x18\x03 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12L\n\x0fsearch_audience\x18\x04 \x01(\x0b21.google.ads.googleads.v19.services.SearchAudienceH\x00\x12H\n\rsearch_topics\x18\x05 \x01(\x0b2/.google.ads.googleads.v19.services.SearchTopicsH\x00B\n\n\x08criteria"k\n GenerateTrendingInsightsResponse\x12G\n\x0etrend_insights\x18\x01 \x03(\x0b2/.google.ads.googleads.v19.services.TrendInsight"\x83\x01\n\x16YouTubeCreatorInsights\x12\x14\n\x0ccreator_name\x18\x01 \x01(\t\x12S\n\x10creator_channels\x18\x02 \x03(\x0b29.google.ads.googleads.v19.services.YouTubeChannelInsights"v\n\x0eYouTubeMetrics\x12\x18\n\x10subscriber_count\x18\x01 \x01(\x03\x12\x13\n\x0bviews_count\x18\x02 \x01(\x03\x12\x13\n\x0bvideo_count\x18\x03 \x01(\x03\x12 \n\x18is_active_shorts_creator\x18\x04 \x01(\x08"\xb1\x04\n\x16YouTubeChannelInsights\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12L\n\x0fyoutube_channel\x18\x02 \x01(\x0b23.google.ads.googleads.v19.common.YouTubeChannelInfo\x12\x13\n\x0bchannel_url\x18\t \x01(\t\x12\x1b\n\x13channel_description\x18\n \x01(\t\x12J\n\x0fchannel_metrics\x18\x03 \x01(\x0b21.google.ads.googleads.v19.services.YouTubeMetrics\x12g\n\x1bchannel_audience_attributes\x18\x07 \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12^\n\x12channel_attributes\x18\x05 \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12V\n\ntop_videos\x18\x08 \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12\x14\n\x0cchannel_type\x18\x06 \x01(\t"n\n\x0eSearchAudience\x12\\\n\x13audience_attributes\x18\x01 \x03(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x02"^\n\x0cSearchTopics\x12N\n\x08entities\x18\x01 \x03(\x0b27.google.ads.googleads.v19.common.AudienceInsightsEntityB\x03\xe0A\x02"\x8a\x02\n\x0cTrendInsight\x12[\n\x0ftrend_attribute\x18\x01 \x01(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12M\n\rtrend_metrics\x18\x02 \x01(\x0b26.google.ads.googleads.v19.services.TrendInsightMetrics\x12N\n\x05trend\x18\x03 \x01(\x0e2?.google.ads.googleads.v19.enums.InsightsTrendEnum.InsightsTrend"*\n\x13TrendInsightMetrics\x12\x13\n\x0bviews_count\x18\x01 \x01(\x032\xb6\x04\n\x1dContentCreatorInsightsService\x12\xe3\x01\n\x17GenerateCreatorInsights\x12A.google.ads.googleads.v19.services.GenerateCreatorInsightsRequest\x1aB.google.ads.googleads.v19.services.GenerateCreatorInsightsResponse"A\x82\xd3\xe4\x93\x02;"6/v19/customers/{customer_id=*}:generateCreatorInsights:\x01*\x12\xe7\x01\n\x18GenerateTrendingInsights\x12B.google.ads.googleads.v19.services.GenerateTrendingInsightsRequest\x1aC.google.ads.googleads.v19.services.GenerateTrendingInsightsResponse"B\x82\xd3\xe4\x93\x02<"7/v19/customers/{customer_id=*}:generateTrendingInsights:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8e\x02\n%com.google.ads.googleads.v19.servicesB"ContentCreatorInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.content_creator_insights_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB"ContentCreatorInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES'].fields_by_name['audience_attributes']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES'].fields_by_name['audience_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES'].fields_by_name['creator_attributes']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES'].fields_by_name['creator_attributes']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND'].fields_by_name['brand_entities']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND'].fields_by_name['brand_entities']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND'].fields_by_name['include_related_topics']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND'].fields_by_name['include_related_topics']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREATORINSIGHTSREQUEST_YOUTUBECHANNELS'].fields_by_name['youtube_channels']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST_YOUTUBECHANNELS'].fields_by_name['youtube_channels']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['country_locations']._loaded_options = None
    _globals['_GENERATECREATORINSIGHTSREQUEST'].fields_by_name['country_locations']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['country_location']._loaded_options = None
    _globals['_GENERATETRENDINGINSIGHTSREQUEST'].fields_by_name['country_location']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHAUDIENCE'].fields_by_name['audience_attributes']._loaded_options = None
    _globals['_SEARCHAUDIENCE'].fields_by_name['audience_attributes']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHTOPICS'].fields_by_name['entities']._loaded_options = None
    _globals['_SEARCHTOPICS'].fields_by_name['entities']._serialized_options = b'\xe0A\x02'
    _globals['_CONTENTCREATORINSIGHTSSERVICE']._loaded_options = None
    _globals['_CONTENTCREATORINSIGHTSSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CONTENTCREATORINSIGHTSSERVICE'].methods_by_name['GenerateCreatorInsights']._loaded_options = None
    _globals['_CONTENTCREATORINSIGHTSSERVICE'].methods_by_name['GenerateCreatorInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02;"6/v19/customers/{customer_id=*}:generateCreatorInsights:\x01*'
    _globals['_CONTENTCREATORINSIGHTSSERVICE'].methods_by_name['GenerateTrendingInsights']._loaded_options = None
    _globals['_CONTENTCREATORINSIGHTSSERVICE'].methods_by_name['GenerateTrendingInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02<"7/v19/customers/{customer_id=*}:generateTrendingInsights:\x01*'
    _globals['_GENERATECREATORINSIGHTSREQUEST']._serialized_start = 368
    _globals['_GENERATECREATORINSIGHTSREQUEST']._serialized_end = 1334
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES']._serialized_start = 872
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHATTRIBUTES']._serialized_end = 1077
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND']._serialized_start = 1080
    _globals['_GENERATECREATORINSIGHTSREQUEST_SEARCHBRAND']._serialized_end = 1219
    _globals['_GENERATECREATORINSIGHTSREQUEST_YOUTUBECHANNELS']._serialized_start = 1221
    _globals['_GENERATECREATORINSIGHTSREQUEST_YOUTUBECHANNELS']._serialized_end = 1322
    _globals['_GENERATECREATORINSIGHTSRESPONSE']._serialized_start = 1336
    _globals['_GENERATECREATORINSIGHTSRESPONSE']._serialized_end = 1454
    _globals['_GENERATETRENDINGINSIGHTSREQUEST']._serialized_start = 1457
    _globals['_GENERATETRENDINGINSIGHTSREQUEST']._serialized_end = 1796
    _globals['_GENERATETRENDINGINSIGHTSRESPONSE']._serialized_start = 1798
    _globals['_GENERATETRENDINGINSIGHTSRESPONSE']._serialized_end = 1905
    _globals['_YOUTUBECREATORINSIGHTS']._serialized_start = 1908
    _globals['_YOUTUBECREATORINSIGHTS']._serialized_end = 2039
    _globals['_YOUTUBEMETRICS']._serialized_start = 2041
    _globals['_YOUTUBEMETRICS']._serialized_end = 2159
    _globals['_YOUTUBECHANNELINSIGHTS']._serialized_start = 2162
    _globals['_YOUTUBECHANNELINSIGHTS']._serialized_end = 2723
    _globals['_SEARCHAUDIENCE']._serialized_start = 2725
    _globals['_SEARCHAUDIENCE']._serialized_end = 2835
    _globals['_SEARCHTOPICS']._serialized_start = 2837
    _globals['_SEARCHTOPICS']._serialized_end = 2931
    _globals['_TRENDINSIGHT']._serialized_start = 2934
    _globals['_TRENDINSIGHT']._serialized_end = 3200
    _globals['_TRENDINSIGHTMETRICS']._serialized_start = 3202
    _globals['_TRENDINSIGHTMETRICS']._serialized_end = 3244
    _globals['_CONTENTCREATORINSIGHTSSERVICE']._serialized_start = 3247
    _globals['_CONTENTCREATORINSIGHTSSERVICE']._serialized_end = 3813