"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/audience_insights_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import additional_application_info_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_additional__application__info__pb2
from ......google.ads.googleads.v21.common import audience_insights_attribute_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_audience__insights__attribute__pb2
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.common import dates_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_dates__pb2
from ......google.ads.googleads.v21.enums import audience_insights_dimension_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_audience__insights__dimension__pb2
from ......google.ads.googleads.v21.enums import audience_insights_marketing_objective_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_audience__insights__marketing__objective__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v21/services/audience_insights_service.proto\x12!google.ads.googleads.v21.services\x1aAgoogle/ads/googleads/v21/common/additional_application_info.proto\x1aAgoogle/ads/googleads/v21/common/audience_insights_attribute.proto\x1a.google/ads/googleads/v21/common/criteria.proto\x1a+google/ads/googleads/v21/common/dates.proto\x1a@google/ads/googleads/v21/enums/audience_insights_dimension.proto\x1aJgoogle/ads/googleads/v21/enums/audience_insights_marketing_objective.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xf8\x02\n#GenerateInsightsFinderReportRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\x11baseline_audience\x18\x02 \x01(\x0b28.google.ads.googleads.v21.services.BasicInsightsAudienceB\x03\xe0A\x02\x12X\n\x11specific_audience\x18\x03 \x01(\x0b28.google.ads.googleads.v21.services.BasicInsightsAudienceB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x04 \x01(\t\x12b\n\x19insights_application_info\x18\x05 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"@\n$GenerateInsightsFinderReportResponse\x12\x18\n\x10saved_report_url\x18\x01 \x01(\t"\xed\x03\n*GenerateAudienceCompositionInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x08audience\x18\x02 \x01(\x0b23.google.ads.googleads.v21.services.InsightsAudienceB\x03\xe0A\x02\x12N\n\x11baseline_audience\x18\x06 \x01(\x0b23.google.ads.googleads.v21.services.InsightsAudience\x12\x12\n\ndata_month\x18\x03 \x01(\t\x12p\n\ndimensions\x18\x04 \x03(\x0e2W.google.ads.googleads.v21.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x05 \x01(\t\x12b\n\x19insights_application_info\x18\x07 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"~\n+GenerateAudienceCompositionInsightsResponse\x12O\n\x08sections\x18\x01 \x03(\x0b2=.google.ads.googleads.v21.services.AudienceCompositionSection"\x9f\x03\n)GenerateSuggestedTargetingInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x05 \x01(\tB\x03\xe0A\x01\x12b\n\x19insights_application_info\x18\x08 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01\x12\\\n\x13audience_definition\x18\x06 \x01(\x0b2=.google.ads.googleads.v21.services.InsightsAudienceDefinitionH\x00\x12^\n\x14audience_description\x18\x07 \x01(\x0b2>.google.ads.googleads.v21.services.InsightsAudienceDescriptionH\x00B\x10\n\x0eaudience_input"\x80\x01\n*GenerateSuggestedTargetingInsightsResponse\x12R\n\x0bsuggestions\x18\x01 \x03(\x0b2=.google.ads.googleads.v21.services.TargetingSuggestionMetrics"\xe4\x03\n\x1aTargetingSuggestionMetrics\x12U\n\tlocations\x18\t \x03(\x0b2B.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadata\x12A\n\nage_ranges\x18\x02 \x03(\x0b2-.google.ads.googleads.v21.common.AgeRangeInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v21.common.GenderInfo\x12L\n\x0fparental_status\x18\x08 \x01(\x0b23.google.ads.googleads.v21.common.ParentalStatusInfo\x12_\n\x0euser_interests\x18\x0b \x03(\x0b2G.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadataGroup\x12\x10\n\x08coverage\x18\x05 \x01(\x01\x12\r\n\x05index\x18\x06 \x01(\x01\x12\x1f\n\x17potential_youtube_reach\x18\x07 \x01(\x03"\xf1\x03\n%ListAudienceInsightsAttributesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12p\n\ndimensions\x18\x02 \x03(\x0e2W.google.ads.googleads.v21.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x17\n\nquery_text\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x04 \x01(\t\x12b\n\x19insights_application_info\x18\x07 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01\x12O\n\x18location_country_filters\x18\x05 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfo\x12M\n\x16youtube_reach_location\x18\x06 \x01(\x0b2-.google.ads.googleads.v21.common.LocationInfo"\x80\x01\n&ListAudienceInsightsAttributesResponse\x12V\n\nattributes\x18\x02 \x03(\x0b2B.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadata"\x86\x01\n ListInsightsEligibleDatesRequest\x12b\n\x19insights_application_info\x18\x01 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"~\n!ListInsightsEligibleDatesResponse\x12\x13\n\x0bdata_months\x18\x01 \x03(\t\x12D\n\x10last_thirty_days\x18\x02 \x01(\x0b2*.google.ads.googleads.v21.common.DateRange"\xe3\x03\n&GenerateAudienceOverlapInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x10country_location\x18\x02 \x01(\x0b2-.google.ads.googleads.v21.common.LocationInfoB\x03\xe0A\x02\x12Z\n\x11primary_attribute\x18\x06 \x01(\x0b2:.google.ads.googleads.v21.common.AudienceInsightsAttributeB\x03\xe0A\x02\x12p\n\ndimensions\x18\x04 \x03(\x0e2W.google.ads.googleads.v21.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x05 \x01(\t\x12b\n\x19insights_application_info\x18\x07 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"\xe7\x01\n\'GenerateAudienceOverlapInsightsResponse\x12f\n\x1aprimary_attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadata\x12T\n\x11dimension_results\x18\x02 \x03(\x0b29.google.ads.googleads.v21.services.DimensionOverlapResult"\xcb\x01\n\x16DimensionOverlapResult\x12j\n\tdimension\x18\x01 \x01(\x0e2W.google.ads.googleads.v21.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension\x12E\n\x05items\x18\x02 \x03(\x0b26.google.ads.googleads.v21.services.AudienceOverlapItem"\xa3\x01\n\x13AudienceOverlapItem\x12^\n\x12attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadata\x12,\n$potential_youtube_reach_intersection\x18\x02 \x01(\x03"\x9c\x02\n)GenerateTargetingSuggestionMetricsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\taudiences\x18\x05 \x03(\x0b23.google.ads.googleads.v21.services.InsightsAudienceB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x03 \x01(\tB\x03\xe0A\x01\x12b\n\x19insights_application_info\x18\x04 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"\x80\x01\n*GenerateTargetingSuggestionMetricsResponse\x12R\n\x0bsuggestions\x18\x01 \x03(\x0b2=.google.ads.googleads.v21.services.TargetingSuggestionMetrics"\xc6\x03\n\x15BasicInsightsAudience\x12L\n\x10country_location\x18\x01 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfoB\x03\xe0A\x02\x12L\n\x15sub_country_locations\x18\x02 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v21.common.GenderInfo\x12A\n\nage_ranges\x18\x04 \x03(\x0b2-.google.ads.googleads.v21.common.AgeRangeInfo\x12I\n\x0euser_interests\x18\x05 \x03(\x0b21.google.ads.googleads.v21.common.UserInterestInfo\x12F\n\x06topics\x18\x07 \x03(\x0b26.google.ads.googleads.v21.common.AudienceInsightsTopic"\xd6\x01\n\x1aInsightsAudienceDefinition\x12J\n\x08audience\x18\x01 \x01(\x0b23.google.ads.googleads.v21.services.InsightsAudienceB\x03\xe0A\x02\x12S\n\x11baseline_audience\x18\x02 \x01(\x0b23.google.ads.googleads.v21.services.InsightsAudienceB\x03\xe0A\x01\x12\x17\n\ndata_month\x18\x03 \x01(\tB\x03\xe0A\x01"\x9d\x02\n\x1bInsightsAudienceDescription\x12M\n\x11country_locations\x18\x01 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfoB\x03\xe0A\x02\x12!\n\x14audience_description\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x8b\x01\n\x13marketing_objective\x18\x03 \x01(\x0e2i.google.ads.googleads.v21.enums.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjectiveB\x03\xe0A\x01"\xba\x05\n\x10InsightsAudience\x12M\n\x11country_locations\x18\x01 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfoB\x03\xe0A\x02\x12L\n\x15sub_country_locations\x18\x02 \x03(\x0b2-.google.ads.googleads.v21.common.LocationInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v21.common.GenderInfo\x12A\n\nage_ranges\x18\x04 \x03(\x0b2-.google.ads.googleads.v21.common.AgeRangeInfo\x12L\n\x0fparental_status\x18\x05 \x01(\x0b23.google.ads.googleads.v21.common.ParentalStatusInfo\x12G\n\rincome_ranges\x18\x06 \x03(\x0b20.google.ads.googleads.v21.common.IncomeRangeInfo\x12H\n\x07lineups\x18\n \x03(\x0b27.google.ads.googleads.v21.common.AudienceInsightsLineup\x12@\n\tuser_list\x18\x0b \x01(\x0b2-.google.ads.googleads.v21.common.UserListInfo\x12f\n\x1btopic_audience_combinations\x18\x08 \x03(\x0b2A.google.ads.googleads.v21.services.InsightsAudienceAttributeGroup"u\n\x1eInsightsAudienceAttributeGroup\x12S\n\nattributes\x18\x02 \x03(\x0b2:.google.ads.googleads.v21.common.AudienceInsightsAttributeB\x03\xe0A\x02"\xc7\x02\n\x1aAudienceCompositionSection\x12j\n\tdimension\x18\x01 \x01(\x0e2W.google.ads.googleads.v21.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension\x12W\n\x0etop_attributes\x18\x03 \x03(\x0b2?.google.ads.googleads.v21.services.AudienceCompositionAttribute\x12d\n\x14clustered_attributes\x18\x04 \x03(\x0b2F.google.ads.googleads.v21.services.AudienceCompositionAttributeCluster"\xf0\x01\n#AudienceCompositionAttributeCluster\x12\x1c\n\x14cluster_display_name\x18\x01 \x01(\t\x12V\n\x0fcluster_metrics\x18\x03 \x01(\x0b2=.google.ads.googleads.v21.services.AudienceCompositionMetrics\x12S\n\nattributes\x18\x04 \x03(\x0b2?.google.ads.googleads.v21.services.AudienceCompositionAttribute"s\n\x1aAudienceCompositionMetrics\x12\x1f\n\x17baseline_audience_share\x18\x01 \x01(\x01\x12\x16\n\x0eaudience_share\x18\x02 \x01(\x01\x12\r\n\x05index\x18\x03 \x01(\x01\x12\r\n\x05score\x18\x04 \x01(\x01"\xce\x01\n\x1cAudienceCompositionAttribute\x12^\n\x12attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v21.common.AudienceInsightsAttributeMetadata\x12N\n\x07metrics\x18\x02 \x01(\x0b2=.google.ads.googleads.v21.services.AudienceCompositionMetrics2\xd0\x10\n\x17AudienceInsightsService\x12\xa9\x02\n\x1cGenerateInsightsFinderReport\x12F.google.ads.googleads.v21.services.GenerateInsightsFinderReportRequest\x1aG.google.ads.googleads.v21.services.GenerateInsightsFinderReportResponse"x\xdaA/customer_id,baseline_audience,specific_audience\x82\xd3\xe4\x93\x02@";/v21/customers/{customer_id=*}:generateInsightsFinderReport:\x01*\x12\xa5\x02\n\x1eListAudienceInsightsAttributes\x12H.google.ads.googleads.v21.services.ListAudienceInsightsAttributesRequest\x1aI.google.ads.googleads.v21.services.ListAudienceInsightsAttributesResponse"n\xdaA!customer_id,dimensions,query_text\x82\xd3\xe4\x93\x02D"?/v21/customers/{customer_id=*}:searchAudienceInsightsAttributes:\x01*\x12\xe2\x01\n\x19ListInsightsEligibleDates\x12C.google.ads.googleads.v21.services.ListInsightsEligibleDatesRequest\x1aD.google.ads.googleads.v21.services.ListInsightsEligibleDatesResponse":\x82\xd3\xe4\x93\x024"//v21/audienceInsights:listInsightsEligibleDates:\x01*\x12\xb5\x02\n#GenerateAudienceCompositionInsights\x12M.google.ads.googleads.v21.services.GenerateAudienceCompositionInsightsRequest\x1aN.google.ads.googleads.v21.services.GenerateAudienceCompositionInsightsResponse"o\xdaA\x1fcustomer_id,audience,dimensions\x82\xd3\xe4\x93\x02G"B/v21/customers/{customer_id=*}:generateAudienceCompositionInsights:\x01*\x12\x8f\x02\n"GenerateSuggestedTargetingInsights\x12L.google.ads.googleads.v21.services.GenerateSuggestedTargetingInsightsRequest\x1aM.google.ads.googleads.v21.services.GenerateSuggestedTargetingInsightsResponse"L\x82\xd3\xe4\x93\x02F"A/v21/customers/{customer_id=*}:generateSuggestedTargetingInsights:\x01*\x12\xc0\x02\n\x1fGenerateAudienceOverlapInsights\x12I.google.ads.googleads.v21.services.GenerateAudienceOverlapInsightsRequest\x1aJ.google.ads.googleads.v21.services.GenerateAudienceOverlapInsightsResponse"\x85\x01\xdaA9customer_id,country_location,primary_attribute,dimensions\x82\xd3\xe4\x93\x02C">/v21/customers/{customer_id=*}:generateAudienceOverlapInsights:\x01*\x12\xa7\x02\n"GenerateTargetingSuggestionMetrics\x12L.google.ads.googleads.v21.services.GenerateTargetingSuggestionMetricsRequest\x1aM.google.ads.googleads.v21.services.GenerateTargetingSuggestionMetricsResponse"d\xdaA\x15customer_id,audiences\x82\xd3\xe4\x93\x02F"A/v21/customers/{customer_id=*}:generateTargetingSuggestionMetrics:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x88\x02\n%com.google.ads.googleads.v21.servicesB\x1cAudienceInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.audience_insights_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1cAudienceInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['baseline_audience']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['baseline_audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['specific_audience']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['specific_audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['query_text']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['query_text']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['country_location']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['country_location']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['primary_attribute']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['primary_attribute']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['audiences']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['audiences']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['insights_application_info']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['insights_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_BASICINSIGHTSAUDIENCE'].fields_by_name['country_location']._loaded_options = None
    _globals['_BASICINSIGHTSAUDIENCE'].fields_by_name['country_location']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['audience']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['audience']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['baseline_audience']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['baseline_audience']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['data_month']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDEFINITION'].fields_by_name['data_month']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['country_locations']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['country_locations']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['audience_description']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['audience_description']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['marketing_objective']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEDESCRIPTION'].fields_by_name['marketing_objective']._serialized_options = b'\xe0A\x01'
    _globals['_INSIGHTSAUDIENCE'].fields_by_name['country_locations']._loaded_options = None
    _globals['_INSIGHTSAUDIENCE'].fields_by_name['country_locations']._serialized_options = b'\xe0A\x02'
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP'].fields_by_name['attributes']._loaded_options = None
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP'].fields_by_name['attributes']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEINSIGHTSSERVICE']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateInsightsFinderReport']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateInsightsFinderReport']._serialized_options = b'\xdaA/customer_id,baseline_audience,specific_audience\x82\xd3\xe4\x93\x02@";/v21/customers/{customer_id=*}:generateInsightsFinderReport:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListAudienceInsightsAttributes']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListAudienceInsightsAttributes']._serialized_options = b'\xdaA!customer_id,dimensions,query_text\x82\xd3\xe4\x93\x02D"?/v21/customers/{customer_id=*}:searchAudienceInsightsAttributes:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListInsightsEligibleDates']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListInsightsEligibleDates']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v21/audienceInsights:listInsightsEligibleDates:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceCompositionInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceCompositionInsights']._serialized_options = b'\xdaA\x1fcustomer_id,audience,dimensions\x82\xd3\xe4\x93\x02G"B/v21/customers/{customer_id=*}:generateAudienceCompositionInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateSuggestedTargetingInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateSuggestedTargetingInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v21/customers/{customer_id=*}:generateSuggestedTargetingInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceOverlapInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceOverlapInsights']._serialized_options = b'\xdaA9customer_id,country_location,primary_attribute,dimensions\x82\xd3\xe4\x93\x02C">/v21/customers/{customer_id=*}:generateAudienceOverlapInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateTargetingSuggestionMetrics']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateTargetingSuggestionMetrics']._serialized_options = b'\xdaA\x15customer_id,audiences\x82\xd3\xe4\x93\x02F"A/v21/customers/{customer_id=*}:generateTargetingSuggestionMetrics:\x01*'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST']._serialized_start = 562
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST']._serialized_end = 938
    _globals['_GENERATEINSIGHTSFINDERREPORTRESPONSE']._serialized_start = 940
    _globals['_GENERATEINSIGHTSFINDERREPORTRESPONSE']._serialized_end = 1004
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST']._serialized_start = 1007
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST']._serialized_end = 1500
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSRESPONSE']._serialized_start = 1502
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSRESPONSE']._serialized_end = 1628
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST']._serialized_start = 1631
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST']._serialized_end = 2046
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSRESPONSE']._serialized_start = 2049
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSRESPONSE']._serialized_end = 2177
    _globals['_TARGETINGSUGGESTIONMETRICS']._serialized_start = 2180
    _globals['_TARGETINGSUGGESTIONMETRICS']._serialized_end = 2664
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST']._serialized_start = 2667
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST']._serialized_end = 3164
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESRESPONSE']._serialized_start = 3167
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESRESPONSE']._serialized_end = 3295
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST']._serialized_start = 3298
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST']._serialized_end = 3432
    _globals['_LISTINSIGHTSELIGIBLEDATESRESPONSE']._serialized_start = 3434
    _globals['_LISTINSIGHTSELIGIBLEDATESRESPONSE']._serialized_end = 3560
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST']._serialized_start = 3563
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST']._serialized_end = 4046
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSRESPONSE']._serialized_start = 4049
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSRESPONSE']._serialized_end = 4280
    _globals['_DIMENSIONOVERLAPRESULT']._serialized_start = 4283
    _globals['_DIMENSIONOVERLAPRESULT']._serialized_end = 4486
    _globals['_AUDIENCEOVERLAPITEM']._serialized_start = 4489
    _globals['_AUDIENCEOVERLAPITEM']._serialized_end = 4652
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST']._serialized_start = 4655
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST']._serialized_end = 4939
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSRESPONSE']._serialized_start = 4942
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSRESPONSE']._serialized_end = 5070
    _globals['_BASICINSIGHTSAUDIENCE']._serialized_start = 5073
    _globals['_BASICINSIGHTSAUDIENCE']._serialized_end = 5527
    _globals['_INSIGHTSAUDIENCEDEFINITION']._serialized_start = 5530
    _globals['_INSIGHTSAUDIENCEDEFINITION']._serialized_end = 5744
    _globals['_INSIGHTSAUDIENCEDESCRIPTION']._serialized_start = 5747
    _globals['_INSIGHTSAUDIENCEDESCRIPTION']._serialized_end = 6032
    _globals['_INSIGHTSAUDIENCE']._serialized_start = 6035
    _globals['_INSIGHTSAUDIENCE']._serialized_end = 6733
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP']._serialized_start = 6735
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP']._serialized_end = 6852
    _globals['_AUDIENCECOMPOSITIONSECTION']._serialized_start = 6855
    _globals['_AUDIENCECOMPOSITIONSECTION']._serialized_end = 7182
    _globals['_AUDIENCECOMPOSITIONATTRIBUTECLUSTER']._serialized_start = 7185
    _globals['_AUDIENCECOMPOSITIONATTRIBUTECLUSTER']._serialized_end = 7425
    _globals['_AUDIENCECOMPOSITIONMETRICS']._serialized_start = 7427
    _globals['_AUDIENCECOMPOSITIONMETRICS']._serialized_end = 7542
    _globals['_AUDIENCECOMPOSITIONATTRIBUTE']._serialized_start = 7545
    _globals['_AUDIENCECOMPOSITIONATTRIBUTE']._serialized_end = 7751
    _globals['_AUDIENCEINSIGHTSSERVICE']._serialized_start = 7754
    _globals['_AUDIENCEINSIGHTSSERVICE']._serialized_end = 9882