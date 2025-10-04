"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/keyword_plan_idea_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.common import dates_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_dates__pb2
from ......google.ads.googleads.v19.common import keyword_plan_common_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_keyword__plan__common__pb2
from ......google.ads.googleads.v19.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_keyword__match__type__pb2
from ......google.ads.googleads.v19.enums import keyword_plan_keyword_annotation_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_keyword__plan__keyword__annotation__pb2
from ......google.ads.googleads.v19.enums import keyword_plan_network_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_keyword__plan__network__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/services/keyword_plan_idea_service.proto\x12!google.ads.googleads.v19.services\x1a.google/ads/googleads/v19/common/criteria.proto\x1a+google/ads/googleads/v19/common/dates.proto\x1a9google/ads/googleads/v19/common/keyword_plan_common.proto\x1a7google/ads/googleads/v19/enums/keyword_match_type.proto\x1aDgoogle/ads/googleads/v19/enums/keyword_plan_keyword_annotation.proto\x1a9google/ads/googleads/v19/enums/keyword_plan_network.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xff\x06\n\x1bGenerateKeywordIdeasRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x15\n\x08language\x18\x0e \x01(\tH\x01\x88\x01\x01\x12\x1c\n\x14geo_target_constants\x18\x0f \x03(\t\x12\x1e\n\x16include_adult_keywords\x18\n \x01(\x08\x12\x12\n\npage_token\x18\x0c \x01(\t\x12\x11\n\tpage_size\x18\r \x01(\x05\x12g\n\x14keyword_plan_network\x18\t \x01(\x0e2I.google.ads.googleads.v19.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork\x12y\n\x12keyword_annotation\x18\x11 \x03(\x0e2].google.ads.googleads.v19.enums.KeywordPlanKeywordAnnotationEnum.KeywordPlanKeywordAnnotation\x12W\n\x11aggregate_metrics\x18\x10 \x01(\x0b2<.google.ads.googleads.v19.common.KeywordPlanAggregateMetrics\x12]\n\x1ahistorical_metrics_options\x18\x12 \x01(\x0b29.google.ads.googleads.v19.common.HistoricalMetricsOptions\x12T\n\x14keyword_and_url_seed\x18\x02 \x01(\x0b24.google.ads.googleads.v19.services.KeywordAndUrlSeedH\x00\x12F\n\x0ckeyword_seed\x18\x03 \x01(\x0b2..google.ads.googleads.v19.services.KeywordSeedH\x00\x12>\n\x08url_seed\x18\x05 \x01(\x0b2*.google.ads.googleads.v19.services.UrlSeedH\x00\x12@\n\tsite_seed\x18\x0b \x01(\x0b2+.google.ads.googleads.v19.services.SiteSeedH\x00B\x06\n\x04seedB\x0b\n\t_language"?\n\x11KeywordAndUrlSeed\x12\x10\n\x03url\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x10\n\x08keywords\x18\x04 \x03(\tB\x06\n\x04_url"\x1f\n\x0bKeywordSeed\x12\x10\n\x08keywords\x18\x02 \x03(\t"&\n\x08SiteSeed\x12\x11\n\x04site\x18\x02 \x01(\tH\x00\x88\x01\x01B\x07\n\x05_site"#\n\x07UrlSeed\x12\x10\n\x03url\x18\x02 \x01(\tH\x00\x88\x01\x01B\x06\n\x04_url"\xff\x01\n\x1bGenerateKeywordIdeaResponse\x12M\n\x07results\x18\x01 \x03(\x0b2<.google.ads.googleads.v19.services.GenerateKeywordIdeaResult\x12d\n\x18aggregate_metric_results\x18\x04 \x01(\x0b2B.google.ads.googleads.v19.common.KeywordPlanAggregateMetricResults\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x03"\xfe\x01\n\x19GenerateKeywordIdeaResult\x12\x11\n\x04text\x18\x05 \x01(\tH\x00\x88\x01\x01\x12[\n\x14keyword_idea_metrics\x18\x03 \x01(\x0b2=.google.ads.googleads.v19.common.KeywordPlanHistoricalMetrics\x12P\n\x13keyword_annotations\x18\x06 \x01(\x0b23.google.ads.googleads.v19.common.KeywordAnnotations\x12\x16\n\x0eclose_variants\x18\x07 \x03(\tB\x07\n\x05_text"\xd3\x03\n\'GenerateKeywordHistoricalMetricsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x10\n\x08keywords\x18\x02 \x03(\t\x12\x15\n\x08language\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x16include_adult_keywords\x18\x05 \x01(\x08\x12\x1c\n\x14geo_target_constants\x18\x06 \x03(\t\x12g\n\x14keyword_plan_network\x18\x07 \x01(\x0e2I.google.ads.googleads.v19.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork\x12W\n\x11aggregate_metrics\x18\x08 \x01(\x0b2<.google.ads.googleads.v19.common.KeywordPlanAggregateMetrics\x12]\n\x1ahistorical_metrics_options\x18\x03 \x01(\x0b29.google.ads.googleads.v19.common.HistoricalMetricsOptionsB\x0b\n\t_language"\xec\x01\n(GenerateKeywordHistoricalMetricsResponse\x12Z\n\x07results\x18\x01 \x03(\x0b2I.google.ads.googleads.v19.services.GenerateKeywordHistoricalMetricsResult\x12d\n\x18aggregate_metric_results\x18\x02 \x01(\x0b2B.google.ads.googleads.v19.common.KeywordPlanAggregateMetricResults"\xb4\x01\n&GenerateKeywordHistoricalMetricsResult\x12\x11\n\x04text\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x16\n\x0eclose_variants\x18\x03 \x03(\t\x12V\n\x0fkeyword_metrics\x18\x02 \x01(\x0b2=.google.ads.googleads.v19.common.KeywordPlanHistoricalMetricsB\x07\n\x05_text"g\n\x1cGenerateAdGroupThemesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08keywords\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x16\n\tad_groups\x18\x03 \x03(\tB\x03\xe0A\x02"\xd2\x01\n\x1dGenerateAdGroupThemesResponse\x12a\n\x1cad_group_keyword_suggestions\x18\x01 \x03(\x0b2;.google.ads.googleads.v19.services.AdGroupKeywordSuggestion\x12N\n\x12unusable_ad_groups\x18\x02 \x03(\x0b22.google.ads.googleads.v19.services.UnusableAdGroup"\xed\x01\n\x18AdGroupKeywordSuggestion\x12\x14\n\x0ckeyword_text\x18\x01 \x01(\t\x12\x1e\n\x16suggested_keyword_text\x18\x02 \x01(\t\x12c\n\x14suggested_match_type\x18\x03 \x01(\x0e2E.google.ads.googleads.v19.enums.KeywordMatchTypeEnum.KeywordMatchType\x12\x1a\n\x12suggested_ad_group\x18\x04 \x01(\t\x12\x1a\n\x12suggested_campaign\x18\x05 \x01(\t"5\n\x0fUnusableAdGroup\x12\x10\n\x08ad_group\x18\x01 \x01(\t\x12\x10\n\x08campaign\x18\x02 \x01(\t"\xfd\x01\n%GenerateKeywordForecastMetricsRequest\x12\x13\n\x0bcustomer_id\x18\x01 \x01(\t\x12\x1a\n\rcurrency_code\x18\x02 \x01(\tH\x00\x88\x01\x01\x12C\n\x0fforecast_period\x18\x03 \x01(\x0b2*.google.ads.googleads.v19.common.DateRange\x12L\n\x08campaign\x18\x04 \x01(\x0b25.google.ads.googleads.v19.services.CampaignToForecastB\x03\xe0A\x02B\x10\n\x0e_currency_code"\x98\x07\n\x12CampaignToForecast\x12\x1a\n\x12language_constants\x18\x01 \x03(\t\x12N\n\rgeo_modifiers\x18\x02 \x03(\x0b27.google.ads.googleads.v19.services.CriterionBidModifier\x12l\n\x14keyword_plan_network\x18\x03 \x01(\x0e2I.google.ads.googleads.v19.enums.KeywordPlanNetworkEnum.KeywordPlanNetworkB\x03\xe0A\x02\x12G\n\x11negative_keywords\x18\x04 \x03(\x0b2,.google.ads.googleads.v19.common.KeywordInfo\x12l\n\x10bidding_strategy\x18\x05 \x01(\x0b2M.google.ads.googleads.v19.services.CampaignToForecast.CampaignBiddingStrategyB\x03\xe0A\x02\x12\x1c\n\x0fconversion_rate\x18\x06 \x01(\x01H\x00\x88\x01\x01\x12E\n\tad_groups\x18\x07 \x03(\x0b22.google.ads.googleads.v19.services.ForecastAdGroup\x1a\xf7\x02\n\x17CampaignBiddingStrategy\x12b\n\x1bmanual_cpc_bidding_strategy\x18\x01 \x01(\x0b2;.google.ads.googleads.v19.services.ManualCpcBiddingStrategyH\x00\x12l\n maximize_clicks_bidding_strategy\x18\x02 \x01(\x0b2@.google.ads.googleads.v19.services.MaximizeClicksBiddingStrategyH\x00\x12v\n%maximize_conversions_bidding_strategy\x18\x03 \x01(\x0b2E.google.ads.googleads.v19.services.MaximizeConversionsBiddingStrategyH\x00B\x12\n\x10bidding_strategyB\x12\n\x10_conversion_rate"\xe6\x01\n\x0fForecastAdGroup\x12\x1f\n\x12max_cpc_bid_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12R\n\x11biddable_keywords\x18\x02 \x03(\x0b22.google.ads.googleads.v19.services.BiddableKeywordB\x03\xe0A\x02\x12G\n\x11negative_keywords\x18\x03 \x03(\x0b2,.google.ads.googleads.v19.common.KeywordInfoB\x15\n\x13_max_cpc_bid_micros"\x8d\x01\n\x0fBiddableKeyword\x12B\n\x07keyword\x18\x01 \x01(\x0b2,.google.ads.googleads.v19.common.KeywordInfoB\x03\xe0A\x02\x12\x1f\n\x12max_cpc_bid_micros\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x15\n\x13_max_cpc_bid_micros"_\n\x14CriterionBidModifier\x12\x1b\n\x13geo_target_constant\x18\x01 \x01(\t\x12\x19\n\x0cbid_modifier\x18\x02 \x01(\x01H\x00\x88\x01\x01B\x0f\n\r_bid_modifier"u\n\x18ManualCpcBiddingStrategy\x12 \n\x13daily_budget_micros\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\x1f\n\x12max_cpc_bid_micros\x18\x02 \x01(\x03B\x03\xe0A\x02B\x16\n\x14_daily_budget_micros"\x8f\x01\n\x1dMaximizeClicksBiddingStrategy\x12&\n\x19daily_target_spend_micros\x18\x01 \x01(\x03B\x03\xe0A\x02\x12\'\n\x1amax_cpc_bid_ceiling_micros\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x1d\n\x1b_max_cpc_bid_ceiling_micros"L\n"MaximizeConversionsBiddingStrategy\x12&\n\x19daily_target_spend_micros\x18\x01 \x01(\x03B\x03\xe0A\x02"\xa9\x01\n&GenerateKeywordForecastMetricsResponse\x12a\n\x19campaign_forecast_metrics\x18\x01 \x01(\x0b29.google.ads.googleads.v19.services.KeywordForecastMetricsH\x00\x88\x01\x01B\x1c\n\x1a_campaign_forecast_metrics"\x90\x03\n\x16KeywordForecastMetrics\x12\x18\n\x0bimpressions\x18\x01 \x01(\x01H\x00\x88\x01\x01\x12\x1f\n\x12click_through_rate\x18\x02 \x01(\x01H\x01\x88\x01\x01\x12\x1f\n\x12average_cpc_micros\x18\x03 \x01(\x03H\x02\x88\x01\x01\x12\x13\n\x06clicks\x18\x04 \x01(\x01H\x03\x88\x01\x01\x12\x18\n\x0bcost_micros\x18\x05 \x01(\x03H\x04\x88\x01\x01\x12\x18\n\x0bconversions\x18\x06 \x01(\x01H\x05\x88\x01\x01\x12\x1c\n\x0fconversion_rate\x18\x07 \x01(\x01H\x06\x88\x01\x01\x12\x1f\n\x12average_cpa_micros\x18\x08 \x01(\x03H\x07\x88\x01\x01B\x0e\n\x0c_impressionsB\x15\n\x13_click_through_rateB\x15\n\x13_average_cpc_microsB\t\n\x07_clicksB\x0e\n\x0c_cost_microsB\x0e\n\x0c_conversionsB\x12\n\x10_conversion_rateB\x15\n\x13_average_cpa_micros2\xce\x08\n\x16KeywordPlanIdeaService\x12\xd6\x01\n\x14GenerateKeywordIdeas\x12>.google.ads.googleads.v19.services.GenerateKeywordIdeasRequest\x1a>.google.ads.googleads.v19.services.GenerateKeywordIdeaResponse">\x82\xd3\xe4\x93\x028"3/v19/customers/{customer_id=*}:generateKeywordIdeas:\x01*\x12\x87\x02\n GenerateKeywordHistoricalMetrics\x12J.google.ads.googleads.v19.services.GenerateKeywordHistoricalMetricsRequest\x1aK.google.ads.googleads.v19.services.GenerateKeywordHistoricalMetricsResponse"J\x82\xd3\xe4\x93\x02D"?/v19/customers/{customer_id=*}:generateKeywordHistoricalMetrics:\x01*\x12\xfc\x01\n\x15GenerateAdGroupThemes\x12?.google.ads.googleads.v19.services.GenerateAdGroupThemesRequest\x1a@.google.ads.googleads.v19.services.GenerateAdGroupThemesResponse"`\xdaA\x1ecustomer_id,keywords,ad_groups\x82\xd3\xe4\x93\x029"4/v19/customers/{customer_id=*}:generateAdGroupThemes:\x01*\x12\x8a\x02\n\x1eGenerateKeywordForecastMetrics\x12H.google.ads.googleads.v19.services.GenerateKeywordForecastMetricsRequest\x1aI.google.ads.googleads.v19.services.GenerateKeywordForecastMetricsResponse"S\xdaA\x08campaign\x82\xd3\xe4\x93\x02B"=/v19/customers/{customer_id=*}:generateKeywordForecastMetrics:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x87\x02\n%com.google.ads.googleads.v19.servicesB\x1bKeywordPlanIdeaServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.keyword_plan_idea_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1bKeywordPlanIdeaServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['keywords']._loaded_options = None
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['keywords']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['ad_groups']._loaded_options = None
    _globals['_GENERATEADGROUPTHEMESREQUEST'].fields_by_name['ad_groups']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEKEYWORDFORECASTMETRICSREQUEST'].fields_by_name['campaign']._loaded_options = None
    _globals['_GENERATEKEYWORDFORECASTMETRICSREQUEST'].fields_by_name['campaign']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNTOFORECAST'].fields_by_name['keyword_plan_network']._loaded_options = None
    _globals['_CAMPAIGNTOFORECAST'].fields_by_name['keyword_plan_network']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNTOFORECAST'].fields_by_name['bidding_strategy']._loaded_options = None
    _globals['_CAMPAIGNTOFORECAST'].fields_by_name['bidding_strategy']._serialized_options = b'\xe0A\x02'
    _globals['_FORECASTADGROUP'].fields_by_name['biddable_keywords']._loaded_options = None
    _globals['_FORECASTADGROUP'].fields_by_name['biddable_keywords']._serialized_options = b'\xe0A\x02'
    _globals['_BIDDABLEKEYWORD'].fields_by_name['keyword']._loaded_options = None
    _globals['_BIDDABLEKEYWORD'].fields_by_name['keyword']._serialized_options = b'\xe0A\x02'
    _globals['_MANUALCPCBIDDINGSTRATEGY'].fields_by_name['max_cpc_bid_micros']._loaded_options = None
    _globals['_MANUALCPCBIDDINGSTRATEGY'].fields_by_name['max_cpc_bid_micros']._serialized_options = b'\xe0A\x02'
    _globals['_MAXIMIZECLICKSBIDDINGSTRATEGY'].fields_by_name['daily_target_spend_micros']._loaded_options = None
    _globals['_MAXIMIZECLICKSBIDDINGSTRATEGY'].fields_by_name['daily_target_spend_micros']._serialized_options = b'\xe0A\x02'
    _globals['_MAXIMIZECONVERSIONSBIDDINGSTRATEGY'].fields_by_name['daily_target_spend_micros']._loaded_options = None
    _globals['_MAXIMIZECONVERSIONSBIDDINGSTRATEGY'].fields_by_name['daily_target_spend_micros']._serialized_options = b'\xe0A\x02'
    _globals['_KEYWORDPLANIDEASERVICE']._loaded_options = None
    _globals['_KEYWORDPLANIDEASERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordIdeas']._loaded_options = None
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordIdeas']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/v19/customers/{customer_id=*}:generateKeywordIdeas:\x01*'
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordHistoricalMetrics']._loaded_options = None
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordHistoricalMetrics']._serialized_options = b'\x82\xd3\xe4\x93\x02D"?/v19/customers/{customer_id=*}:generateKeywordHistoricalMetrics:\x01*'
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateAdGroupThemes']._loaded_options = None
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateAdGroupThemes']._serialized_options = b'\xdaA\x1ecustomer_id,keywords,ad_groups\x82\xd3\xe4\x93\x029"4/v19/customers/{customer_id=*}:generateAdGroupThemes:\x01*'
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordForecastMetrics']._loaded_options = None
    _globals['_KEYWORDPLANIDEASERVICE'].methods_by_name['GenerateKeywordForecastMetrics']._serialized_options = b'\xdaA\x08campaign\x82\xd3\xe4\x93\x02B"=/v19/customers/{customer_id=*}:generateKeywordForecastMetrics:\x01*'
    _globals['_GENERATEKEYWORDIDEASREQUEST']._serialized_start = 531
    _globals['_GENERATEKEYWORDIDEASREQUEST']._serialized_end = 1426
    _globals['_KEYWORDANDURLSEED']._serialized_start = 1428
    _globals['_KEYWORDANDURLSEED']._serialized_end = 1491
    _globals['_KEYWORDSEED']._serialized_start = 1493
    _globals['_KEYWORDSEED']._serialized_end = 1524
    _globals['_SITESEED']._serialized_start = 1526
    _globals['_SITESEED']._serialized_end = 1564
    _globals['_URLSEED']._serialized_start = 1566
    _globals['_URLSEED']._serialized_end = 1601
    _globals['_GENERATEKEYWORDIDEARESPONSE']._serialized_start = 1604
    _globals['_GENERATEKEYWORDIDEARESPONSE']._serialized_end = 1859
    _globals['_GENERATEKEYWORDIDEARESULT']._serialized_start = 1862
    _globals['_GENERATEKEYWORDIDEARESULT']._serialized_end = 2116
    _globals['_GENERATEKEYWORDHISTORICALMETRICSREQUEST']._serialized_start = 2119
    _globals['_GENERATEKEYWORDHISTORICALMETRICSREQUEST']._serialized_end = 2586
    _globals['_GENERATEKEYWORDHISTORICALMETRICSRESPONSE']._serialized_start = 2589
    _globals['_GENERATEKEYWORDHISTORICALMETRICSRESPONSE']._serialized_end = 2825
    _globals['_GENERATEKEYWORDHISTORICALMETRICSRESULT']._serialized_start = 2828
    _globals['_GENERATEKEYWORDHISTORICALMETRICSRESULT']._serialized_end = 3008
    _globals['_GENERATEADGROUPTHEMESREQUEST']._serialized_start = 3010
    _globals['_GENERATEADGROUPTHEMESREQUEST']._serialized_end = 3113
    _globals['_GENERATEADGROUPTHEMESRESPONSE']._serialized_start = 3116
    _globals['_GENERATEADGROUPTHEMESRESPONSE']._serialized_end = 3326
    _globals['_ADGROUPKEYWORDSUGGESTION']._serialized_start = 3329
    _globals['_ADGROUPKEYWORDSUGGESTION']._serialized_end = 3566
    _globals['_UNUSABLEADGROUP']._serialized_start = 3568
    _globals['_UNUSABLEADGROUP']._serialized_end = 3621
    _globals['_GENERATEKEYWORDFORECASTMETRICSREQUEST']._serialized_start = 3624
    _globals['_GENERATEKEYWORDFORECASTMETRICSREQUEST']._serialized_end = 3877
    _globals['_CAMPAIGNTOFORECAST']._serialized_start = 3880
    _globals['_CAMPAIGNTOFORECAST']._serialized_end = 4800
    _globals['_CAMPAIGNTOFORECAST_CAMPAIGNBIDDINGSTRATEGY']._serialized_start = 4405
    _globals['_CAMPAIGNTOFORECAST_CAMPAIGNBIDDINGSTRATEGY']._serialized_end = 4780
    _globals['_FORECASTADGROUP']._serialized_start = 4803
    _globals['_FORECASTADGROUP']._serialized_end = 5033
    _globals['_BIDDABLEKEYWORD']._serialized_start = 5036
    _globals['_BIDDABLEKEYWORD']._serialized_end = 5177
    _globals['_CRITERIONBIDMODIFIER']._serialized_start = 5179
    _globals['_CRITERIONBIDMODIFIER']._serialized_end = 5274
    _globals['_MANUALCPCBIDDINGSTRATEGY']._serialized_start = 5276
    _globals['_MANUALCPCBIDDINGSTRATEGY']._serialized_end = 5393
    _globals['_MAXIMIZECLICKSBIDDINGSTRATEGY']._serialized_start = 5396
    _globals['_MAXIMIZECLICKSBIDDINGSTRATEGY']._serialized_end = 5539
    _globals['_MAXIMIZECONVERSIONSBIDDINGSTRATEGY']._serialized_start = 5541
    _globals['_MAXIMIZECONVERSIONSBIDDINGSTRATEGY']._serialized_end = 5617
    _globals['_GENERATEKEYWORDFORECASTMETRICSRESPONSE']._serialized_start = 5620
    _globals['_GENERATEKEYWORDFORECASTMETRICSRESPONSE']._serialized_end = 5789
    _globals['_KEYWORDFORECASTMETRICS']._serialized_start = 5792
    _globals['_KEYWORDFORECASTMETRICS']._serialized_end = 6192
    _globals['_KEYWORDPLANIDEASERVICE']._serialized_start = 6195
    _globals['_KEYWORDPLANIDEASERVICE']._serialized_end = 7297