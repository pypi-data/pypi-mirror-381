"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/smart_campaign_suggest_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import ad_type_infos_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_ad__type__infos__pb2
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.resources import keyword_theme_constant_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_keyword__theme__constant__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v19/services/smart_campaign_suggest_service.proto\x12!google.ads.googleads.v19.services\x1a3google/ads/googleads/v19/common/ad_type_infos.proto\x1a.google/ads/googleads/v19/common/criteria.proto\x1a?google/ads/googleads/v19/resources/keyword_theme_constant.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf6\x01\n(SuggestSmartCampaignBudgetOptionsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12=\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/CampaignH\x00\x12^\n\x0fsuggestion_info\x18\x03 \x01(\x0b2>.google.ads.googleads.v19.services.SmartCampaignSuggestionInfoB\x03\xe0A\x02H\x00B\x11\n\x0fsuggestion_data"\xe5\x05\n\x1bSmartCampaignSuggestionInfo\x12\x16\n\tfinal_url\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rlanguage_code\x18\x03 \x01(\tB\x03\xe0A\x01\x12J\n\x0cad_schedules\x18\x06 \x03(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfoB\x03\xe0A\x01\x12N\n\x0ekeyword_themes\x18\x07 \x03(\x0b21.google.ads.googleads.v19.common.KeywordThemeInfoB\x03\xe0A\x01\x12o\n\x10business_context\x18\x08 \x01(\x0b2N.google.ads.googleads.v19.services.SmartCampaignSuggestionInfo.BusinessContextB\x03\xe0A\x01H\x00\x12(\n\x19business_profile_location\x18\t \x01(\tB\x03\xe0A\x01H\x00\x12i\n\rlocation_list\x18\x04 \x01(\x0b2K.google.ads.googleads.v19.services.SmartCampaignSuggestionInfo.LocationListB\x03\xe0A\x01H\x01\x12H\n\tproximity\x18\x05 \x01(\x0b2..google.ads.googleads.v19.common.ProximityInfoB\x03\xe0A\x01H\x01\x1aU\n\x0cLocationList\x12E\n\tlocations\x18\x01 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x1a-\n\x0fBusinessContext\x12\x1a\n\rbusiness_name\x18\x01 \x01(\tB\x03\xe0A\x01B\x12\n\x10business_settingB\x0c\n\ngeo_target"\xff\x04\n)SuggestSmartCampaignBudgetOptionsResponse\x12p\n\x03low\x18\x01 \x01(\x0b2Y.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsResponse.BudgetOptionB\x03\xe0A\x01H\x00\x88\x01\x01\x12x\n\x0brecommended\x18\x02 \x01(\x0b2Y.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsResponse.BudgetOptionB\x03\xe0A\x01H\x01\x88\x01\x01\x12q\n\x04high\x18\x03 \x01(\x0b2Y.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsResponse.BudgetOptionB\x03\xe0A\x01H\x02\x88\x01\x01\x1a=\n\x07Metrics\x12\x18\n\x10min_daily_clicks\x18\x01 \x01(\x03\x12\x18\n\x10max_daily_clicks\x18\x02 \x01(\x03\x1a\x92\x01\n\x0cBudgetOption\x12\x1b\n\x13daily_amount_micros\x18\x01 \x01(\x03\x12e\n\x07metrics\x18\x02 \x01(\x0b2T.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsResponse.MetricsB\x06\n\x04_lowB\x0e\n\x0c_recommendedB\x07\n\x05_high"\x97\x01\n\x1dSuggestSmartCampaignAdRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\\\n\x0fsuggestion_info\x18\x02 \x01(\x0b2>.google.ads.googleads.v19.services.SmartCampaignSuggestionInfoB\x03\xe0A\x02"l\n\x1eSuggestSmartCampaignAdResponse\x12J\n\x07ad_info\x18\x01 \x01(\x0b24.google.ads.googleads.v19.common.SmartCampaignAdInfoB\x03\xe0A\x01"\x95\x01\n\x1bSuggestKeywordThemesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\\\n\x0fsuggestion_info\x18\x02 \x01(\x0b2>.google.ads.googleads.v19.services.SmartCampaignSuggestionInfoB\x03\xe0A\x02"\xa5\x02\n\x1cSuggestKeywordThemesResponse\x12d\n\x0ekeyword_themes\x18\x02 \x03(\x0b2L.google.ads.googleads.v19.services.SuggestKeywordThemesResponse.KeywordTheme\x1a\x9e\x01\n\x0cKeywordTheme\x12Z\n\x16keyword_theme_constant\x18\x01 \x01(\x0b28.google.ads.googleads.v19.resources.KeywordThemeConstantH\x00\x12!\n\x17free_form_keyword_theme\x18\x02 \x01(\tH\x00B\x0f\n\rkeyword_theme2\xea\x06\n\x1bSmartCampaignSuggestService\x12\x8b\x02\n!SuggestSmartCampaignBudgetOptions\x12K.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsRequest\x1aL.google.ads.googleads.v19.services.SuggestSmartCampaignBudgetOptionsResponse"K\x82\xd3\xe4\x93\x02E"@/v19/customers/{customer_id=*}:suggestSmartCampaignBudgetOptions:\x01*\x12\xfd\x01\n\x16SuggestSmartCampaignAd\x12@.google.ads.googleads.v19.services.SuggestSmartCampaignAdRequest\x1aA.google.ads.googleads.v19.services.SuggestSmartCampaignAdResponse"^\xdaA\x1bcustomer_id,suggestion_info\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}:suggestSmartCampaignAd:\x01*\x12\xf5\x01\n\x14SuggestKeywordThemes\x12>.google.ads.googleads.v19.services.SuggestKeywordThemesRequest\x1a?.google.ads.googleads.v19.services.SuggestKeywordThemesResponse"\\\xdaA\x1bcustomer_id,suggestion_info\x82\xd3\xe4\x93\x028"3/v19/customers/{customer_id=*}:suggestKeywordThemes:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v19.servicesB SmartCampaignSuggestServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.smart_campaign_suggest_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB SmartCampaignSuggestServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['campaign']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['campaign']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['suggestion_info']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST'].fields_by_name['suggestion_info']._serialized_options = b'\xe0A\x02'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_LOCATIONLIST'].fields_by_name['locations']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_LOCATIONLIST'].fields_by_name['locations']._serialized_options = b'\xe0A\x02'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_BUSINESSCONTEXT'].fields_by_name['business_name']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_BUSINESSCONTEXT'].fields_by_name['business_name']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['final_url']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['final_url']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['language_code']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['ad_schedules']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['ad_schedules']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['keyword_themes']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['keyword_themes']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['business_context']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['business_context']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['business_profile_location']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['business_profile_location']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['location_list']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['location_list']._serialized_options = b'\xe0A\x01'
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['proximity']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO'].fields_by_name['proximity']._serialized_options = b'\xe0A\x01'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['low']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['low']._serialized_options = b'\xe0A\x01'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['recommended']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['recommended']._serialized_options = b'\xe0A\x01'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['high']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE'].fields_by_name['high']._serialized_options = b'\xe0A\x01'
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST'].fields_by_name['suggestion_info']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST'].fields_by_name['suggestion_info']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTSMARTCAMPAIGNADRESPONSE'].fields_by_name['ad_info']._loaded_options = None
    _globals['_SUGGESTSMARTCAMPAIGNADRESPONSE'].fields_by_name['ad_info']._serialized_options = b'\xe0A\x01'
    _globals['_SUGGESTKEYWORDTHEMESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_SUGGESTKEYWORDTHEMESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_SUGGESTKEYWORDTHEMESREQUEST'].fields_by_name['suggestion_info']._loaded_options = None
    _globals['_SUGGESTKEYWORDTHEMESREQUEST'].fields_by_name['suggestion_info']._serialized_options = b'\xe0A\x02'
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestSmartCampaignBudgetOptions']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestSmartCampaignBudgetOptions']._serialized_options = b'\x82\xd3\xe4\x93\x02E"@/v19/customers/{customer_id=*}:suggestSmartCampaignBudgetOptions:\x01*'
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestSmartCampaignAd']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestSmartCampaignAd']._serialized_options = b'\xdaA\x1bcustomer_id,suggestion_info\x82\xd3\xe4\x93\x02:"5/v19/customers/{customer_id=*}:suggestSmartCampaignAd:\x01*'
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestKeywordThemes']._loaded_options = None
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE'].methods_by_name['SuggestKeywordThemes']._serialized_options = b'\xdaA\x1bcustomer_id,suggestion_info\x82\xd3\xe4\x93\x028"3/v19/customers/{customer_id=*}:suggestKeywordThemes:\x01*'
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST']._serialized_start = 391
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSREQUEST']._serialized_end = 637
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO']._serialized_start = 640
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO']._serialized_end = 1381
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_LOCATIONLIST']._serialized_start = 1215
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_LOCATIONLIST']._serialized_end = 1300
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_BUSINESSCONTEXT']._serialized_start = 1302
    _globals['_SMARTCAMPAIGNSUGGESTIONINFO_BUSINESSCONTEXT']._serialized_end = 1347
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE']._serialized_start = 1384
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE']._serialized_end = 2023
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE_METRICS']._serialized_start = 1780
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE_METRICS']._serialized_end = 1841
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE_BUDGETOPTION']._serialized_start = 1844
    _globals['_SUGGESTSMARTCAMPAIGNBUDGETOPTIONSRESPONSE_BUDGETOPTION']._serialized_end = 1990
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST']._serialized_start = 2026
    _globals['_SUGGESTSMARTCAMPAIGNADREQUEST']._serialized_end = 2177
    _globals['_SUGGESTSMARTCAMPAIGNADRESPONSE']._serialized_start = 2179
    _globals['_SUGGESTSMARTCAMPAIGNADRESPONSE']._serialized_end = 2287
    _globals['_SUGGESTKEYWORDTHEMESREQUEST']._serialized_start = 2290
    _globals['_SUGGESTKEYWORDTHEMESREQUEST']._serialized_end = 2439
    _globals['_SUGGESTKEYWORDTHEMESRESPONSE']._serialized_start = 2442
    _globals['_SUGGESTKEYWORDTHEMESRESPONSE']._serialized_end = 2735
    _globals['_SUGGESTKEYWORDTHEMESRESPONSE_KEYWORDTHEME']._serialized_start = 2577
    _globals['_SUGGESTKEYWORDTHEMESRESPONSE_KEYWORDTHEME']._serialized_end = 2735
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE']._serialized_start = 2738
    _globals['_SMARTCAMPAIGNSUGGESTSERVICE']._serialized_end = 3612