"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/audience_insights_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import audience_insights_attribute_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_audience__insights__attribute__pb2
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.common import dates_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_dates__pb2
from ......google.ads.googleads.v19.enums import audience_insights_dimension_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_audience__insights__dimension__pb2
from ......google.ads.googleads.v19.enums import audience_insights_marketing_objective_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_audience__insights__marketing__objective__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/services/audience_insights_service.proto\x12!google.ads.googleads.v19.services\x1aAgoogle/ads/googleads/v19/common/audience_insights_attribute.proto\x1a.google/ads/googleads/v19/common/criteria.proto\x1a+google/ads/googleads/v19/common/dates.proto\x1a@google/ads/googleads/v19/enums/audience_insights_dimension.proto\x1aJgoogle/ads/googleads/v19/enums/audience_insights_marketing_objective.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\x94\x02\n#GenerateInsightsFinderReportRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\x11baseline_audience\x18\x02 \x01(\x0b28.google.ads.googleads.v19.services.BasicInsightsAudienceB\x03\xe0A\x02\x12X\n\x11specific_audience\x18\x03 \x01(\x0b28.google.ads.googleads.v19.services.BasicInsightsAudienceB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x04 \x01(\t"@\n$GenerateInsightsFinderReportResponse\x12\x18\n\x10saved_report_url\x18\x01 \x01(\t"\x89\x03\n*GenerateAudienceCompositionInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x08audience\x18\x02 \x01(\x0b23.google.ads.googleads.v19.services.InsightsAudienceB\x03\xe0A\x02\x12N\n\x11baseline_audience\x18\x06 \x01(\x0b23.google.ads.googleads.v19.services.InsightsAudience\x12\x12\n\ndata_month\x18\x03 \x01(\t\x12p\n\ndimensions\x18\x04 \x03(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x05 \x01(\t"~\n+GenerateAudienceCompositionInsightsResponse\x12O\n\x08sections\x18\x01 \x03(\x0b2=.google.ads.googleads.v19.services.AudienceCompositionSection"\xbb\x02\n)GenerateSuggestedTargetingInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x05 \x01(\tB\x03\xe0A\x01\x12\\\n\x13audience_definition\x18\x06 \x01(\x0b2=.google.ads.googleads.v19.services.InsightsAudienceDefinitionH\x00\x12^\n\x14audience_description\x18\x07 \x01(\x0b2>.google.ads.googleads.v19.services.InsightsAudienceDescriptionH\x00B\x10\n\x0eaudience_input"\x80\x01\n*GenerateSuggestedTargetingInsightsResponse\x12R\n\x0bsuggestions\x18\x01 \x03(\x0b2=.google.ads.googleads.v19.services.TargetingSuggestionMetrics"\xdf\x03\n\x1aTargetingSuggestionMetrics\x12U\n\tlocations\x18\t \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12A\n\nage_ranges\x18\x02 \x03(\x0b2-.google.ads.googleads.v19.common.AgeRangeInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v19.common.GenderInfo\x12L\n\x0fparental_status\x18\x08 \x01(\x0b23.google.ads.googleads.v19.common.ParentalStatusInfo\x12Z\n\x0euser_interests\x18\n \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12\x10\n\x08coverage\x18\x05 \x01(\x01\x12\r\n\x05index\x18\x06 \x01(\x01\x12\x1f\n\x17potential_youtube_reach\x18\x07 \x01(\x03"\x8d\x03\n%ListAudienceInsightsAttributesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12p\n\ndimensions\x18\x02 \x03(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x17\n\nquery_text\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x04 \x01(\t\x12O\n\x18location_country_filters\x18\x05 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfo\x12M\n\x16youtube_reach_location\x18\x06 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfo"\x80\x01\n&ListAudienceInsightsAttributesResponse\x12V\n\nattributes\x18\x02 \x03(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata""\n ListInsightsEligibleDatesRequest"~\n!ListInsightsEligibleDatesResponse\x12\x13\n\x0bdata_months\x18\x01 \x03(\t\x12D\n\x10last_thirty_days\x18\x02 \x01(\x0b2*.google.ads.googleads.v19.common.DateRange"\xff\x02\n&GenerateAudienceOverlapInsightsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\x10country_location\x18\x02 \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12Z\n\x11primary_attribute\x18\x06 \x01(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x02\x12p\n\ndimensions\x18\x04 \x03(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimensionB\x03\xe0A\x02\x12\x1f\n\x17customer_insights_group\x18\x05 \x01(\t"\xe7\x01\n\'GenerateAudienceOverlapInsightsResponse\x12f\n\x1aprimary_attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12T\n\x11dimension_results\x18\x02 \x03(\x0b29.google.ads.googleads.v19.services.DimensionOverlapResult"\xcb\x01\n\x16DimensionOverlapResult\x12j\n\tdimension\x18\x01 \x01(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension\x12E\n\x05items\x18\x02 \x03(\x0b26.google.ads.googleads.v19.services.AudienceOverlapItem"\xa3\x01\n\x13AudienceOverlapItem\x12^\n\x12attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12,\n$potential_youtube_reach_intersection\x18\x02 \x01(\x03"\xbd\x01\n)GenerateTargetingSuggestionMetricsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\taudiences\x18\x02 \x03(\x0b28.google.ads.googleads.v19.services.BasicInsightsAudienceB\x03\xe0A\x02\x12$\n\x17customer_insights_group\x18\x03 \x01(\tB\x03\xe0A\x01"\x80\x01\n*GenerateTargetingSuggestionMetricsResponse\x12R\n\x0bsuggestions\x18\x01 \x03(\x0b2=.google.ads.googleads.v19.services.TargetingSuggestionMetrics"\xc6\x03\n\x15BasicInsightsAudience\x12L\n\x10country_location\x18\x01 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12L\n\x15sub_country_locations\x18\x02 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v19.common.GenderInfo\x12A\n\nage_ranges\x18\x04 \x03(\x0b2-.google.ads.googleads.v19.common.AgeRangeInfo\x12I\n\x0euser_interests\x18\x05 \x03(\x0b21.google.ads.googleads.v19.common.UserInterestInfo\x12F\n\x06topics\x18\x07 \x03(\x0b26.google.ads.googleads.v19.common.AudienceInsightsTopic"\xd6\x01\n\x1aInsightsAudienceDefinition\x12J\n\x08audience\x18\x01 \x01(\x0b23.google.ads.googleads.v19.services.InsightsAudienceB\x03\xe0A\x02\x12S\n\x11baseline_audience\x18\x02 \x01(\x0b23.google.ads.googleads.v19.services.InsightsAudienceB\x03\xe0A\x01\x12\x17\n\ndata_month\x18\x03 \x01(\tB\x03\xe0A\x01"\x9d\x02\n\x1bInsightsAudienceDescription\x12M\n\x11country_locations\x18\x01 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12!\n\x14audience_description\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x8b\x01\n\x13marketing_objective\x18\x03 \x01(\x0e2i.google.ads.googleads.v19.enums.AudienceInsightsMarketingObjectiveEnum.AudienceInsightsMarketingObjectiveB\x03\xe0A\x01"\x87\x05\n\x10InsightsAudience\x12M\n\x11country_locations\x18\x01 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x02\x12L\n\x15sub_country_locations\x18\x02 \x03(\x0b2-.google.ads.googleads.v19.common.LocationInfo\x12;\n\x06gender\x18\x03 \x01(\x0b2+.google.ads.googleads.v19.common.GenderInfo\x12A\n\nage_ranges\x18\x04 \x03(\x0b2-.google.ads.googleads.v19.common.AgeRangeInfo\x12L\n\x0fparental_status\x18\x05 \x01(\x0b23.google.ads.googleads.v19.common.ParentalStatusInfo\x12G\n\rincome_ranges\x18\x06 \x03(\x0b20.google.ads.googleads.v19.common.IncomeRangeInfo\x12W\n\x0fdynamic_lineups\x18\t \x03(\x0b2>.google.ads.googleads.v19.common.AudienceInsightsDynamicLineup\x12f\n\x1btopic_audience_combinations\x18\x08 \x03(\x0b2A.google.ads.googleads.v19.services.InsightsAudienceAttributeGroup"u\n\x1eInsightsAudienceAttributeGroup\x12S\n\nattributes\x18\x02 \x03(\x0b2:.google.ads.googleads.v19.common.AudienceInsightsAttributeB\x03\xe0A\x02"\xc7\x02\n\x1aAudienceCompositionSection\x12j\n\tdimension\x18\x01 \x01(\x0e2W.google.ads.googleads.v19.enums.AudienceInsightsDimensionEnum.AudienceInsightsDimension\x12W\n\x0etop_attributes\x18\x03 \x03(\x0b2?.google.ads.googleads.v19.services.AudienceCompositionAttribute\x12d\n\x14clustered_attributes\x18\x04 \x03(\x0b2F.google.ads.googleads.v19.services.AudienceCompositionAttributeCluster"\xf0\x01\n#AudienceCompositionAttributeCluster\x12\x1c\n\x14cluster_display_name\x18\x01 \x01(\t\x12V\n\x0fcluster_metrics\x18\x03 \x01(\x0b2=.google.ads.googleads.v19.services.AudienceCompositionMetrics\x12S\n\nattributes\x18\x04 \x03(\x0b2?.google.ads.googleads.v19.services.AudienceCompositionAttribute"s\n\x1aAudienceCompositionMetrics\x12\x1f\n\x17baseline_audience_share\x18\x01 \x01(\x01\x12\x16\n\x0eaudience_share\x18\x02 \x01(\x01\x12\r\n\x05index\x18\x03 \x01(\x01\x12\r\n\x05score\x18\x04 \x01(\x01"\xce\x01\n\x1cAudienceCompositionAttribute\x12^\n\x12attribute_metadata\x18\x03 \x01(\x0b2B.google.ads.googleads.v19.common.AudienceInsightsAttributeMetadata\x12N\n\x07metrics\x18\x02 \x01(\x0b2=.google.ads.googleads.v19.services.AudienceCompositionMetrics2\xd0\x10\n\x17AudienceInsightsService\x12\xa9\x02\n\x1cGenerateInsightsFinderReport\x12F.google.ads.googleads.v19.services.GenerateInsightsFinderReportRequest\x1aG.google.ads.googleads.v19.services.GenerateInsightsFinderReportResponse"x\xdaA/customer_id,baseline_audience,specific_audience\x82\xd3\xe4\x93\x02@";/v19/customers/{customer_id=*}:generateInsightsFinderReport:\x01*\x12\xa5\x02\n\x1eListAudienceInsightsAttributes\x12H.google.ads.googleads.v19.services.ListAudienceInsightsAttributesRequest\x1aI.google.ads.googleads.v19.services.ListAudienceInsightsAttributesResponse"n\xdaA!customer_id,dimensions,query_text\x82\xd3\xe4\x93\x02D"?/v19/customers/{customer_id=*}:searchAudienceInsightsAttributes:\x01*\x12\xe2\x01\n\x19ListInsightsEligibleDates\x12C.google.ads.googleads.v19.services.ListInsightsEligibleDatesRequest\x1aD.google.ads.googleads.v19.services.ListInsightsEligibleDatesResponse":\x82\xd3\xe4\x93\x024"//v19/audienceInsights:listInsightsEligibleDates:\x01*\x12\xb5\x02\n#GenerateAudienceCompositionInsights\x12M.google.ads.googleads.v19.services.GenerateAudienceCompositionInsightsRequest\x1aN.google.ads.googleads.v19.services.GenerateAudienceCompositionInsightsResponse"o\xdaA\x1fcustomer_id,audience,dimensions\x82\xd3\xe4\x93\x02G"B/v19/customers/{customer_id=*}:generateAudienceCompositionInsights:\x01*\x12\x8f\x02\n"GenerateSuggestedTargetingInsights\x12L.google.ads.googleads.v19.services.GenerateSuggestedTargetingInsightsRequest\x1aM.google.ads.googleads.v19.services.GenerateSuggestedTargetingInsightsResponse"L\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}:generateSuggestedTargetingInsights:\x01*\x12\xc0\x02\n\x1fGenerateAudienceOverlapInsights\x12I.google.ads.googleads.v19.services.GenerateAudienceOverlapInsightsRequest\x1aJ.google.ads.googleads.v19.services.GenerateAudienceOverlapInsightsResponse"\x85\x01\xdaA9customer_id,country_location,primary_attribute,dimensions\x82\xd3\xe4\x93\x02C">/v19/customers/{customer_id=*}:generateAudienceOverlapInsights:\x01*\x12\xa7\x02\n"GenerateTargetingSuggestionMetrics\x12L.google.ads.googleads.v19.services.GenerateTargetingSuggestionMetricsRequest\x1aM.google.ads.googleads.v19.services.GenerateTargetingSuggestionMetricsResponse"d\xdaA\x15customer_id,audiences\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}:generateTargetingSuggestionMetrics:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x88\x02\n%com.google.ads.googleads.v19.servicesB\x1cAudienceInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.audience_insights_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1cAudienceInsightsServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['baseline_audience']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['baseline_audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['specific_audience']._loaded_options = None
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST'].fields_by_name['specific_audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['query_text']._loaded_options = None
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST'].fields_by_name['query_text']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['country_location']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['country_location']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['primary_attribute']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['primary_attribute']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['dimensions']._loaded_options = None
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['audiences']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['audiences']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_insights_group']._loaded_options = None
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST'].fields_by_name['customer_insights_group']._serialized_options = b'\xe0A\x01'
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
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateInsightsFinderReport']._serialized_options = b'\xdaA/customer_id,baseline_audience,specific_audience\x82\xd3\xe4\x93\x02@";/v19/customers/{customer_id=*}:generateInsightsFinderReport:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListAudienceInsightsAttributes']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListAudienceInsightsAttributes']._serialized_options = b'\xdaA!customer_id,dimensions,query_text\x82\xd3\xe4\x93\x02D"?/v19/customers/{customer_id=*}:searchAudienceInsightsAttributes:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListInsightsEligibleDates']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['ListInsightsEligibleDates']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v19/audienceInsights:listInsightsEligibleDates:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceCompositionInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceCompositionInsights']._serialized_options = b'\xdaA\x1fcustomer_id,audience,dimensions\x82\xd3\xe4\x93\x02G"B/v19/customers/{customer_id=*}:generateAudienceCompositionInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateSuggestedTargetingInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateSuggestedTargetingInsights']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}:generateSuggestedTargetingInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceOverlapInsights']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateAudienceOverlapInsights']._serialized_options = b'\xdaA9customer_id,country_location,primary_attribute,dimensions\x82\xd3\xe4\x93\x02C">/v19/customers/{customer_id=*}:generateAudienceOverlapInsights:\x01*'
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateTargetingSuggestionMetrics']._loaded_options = None
    _globals['_AUDIENCEINSIGHTSSERVICE'].methods_by_name['GenerateTargetingSuggestionMetrics']._serialized_options = b'\xdaA\x15customer_id,audiences\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}:generateTargetingSuggestionMetrics:\x01*'
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST']._serialized_start = 495
    _globals['_GENERATEINSIGHTSFINDERREPORTREQUEST']._serialized_end = 771
    _globals['_GENERATEINSIGHTSFINDERREPORTRESPONSE']._serialized_start = 773
    _globals['_GENERATEINSIGHTSFINDERREPORTRESPONSE']._serialized_end = 837
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST']._serialized_start = 840
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSREQUEST']._serialized_end = 1233
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSRESPONSE']._serialized_start = 1235
    _globals['_GENERATEAUDIENCECOMPOSITIONINSIGHTSRESPONSE']._serialized_end = 1361
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST']._serialized_start = 1364
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSREQUEST']._serialized_end = 1679
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSRESPONSE']._serialized_start = 1682
    _globals['_GENERATESUGGESTEDTARGETINGINSIGHTSRESPONSE']._serialized_end = 1810
    _globals['_TARGETINGSUGGESTIONMETRICS']._serialized_start = 1813
    _globals['_TARGETINGSUGGESTIONMETRICS']._serialized_end = 2292
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST']._serialized_start = 2295
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESREQUEST']._serialized_end = 2692
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESRESPONSE']._serialized_start = 2695
    _globals['_LISTAUDIENCEINSIGHTSATTRIBUTESRESPONSE']._serialized_end = 2823
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST']._serialized_start = 2825
    _globals['_LISTINSIGHTSELIGIBLEDATESREQUEST']._serialized_end = 2859
    _globals['_LISTINSIGHTSELIGIBLEDATESRESPONSE']._serialized_start = 2861
    _globals['_LISTINSIGHTSELIGIBLEDATESRESPONSE']._serialized_end = 2987
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST']._serialized_start = 2990
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSREQUEST']._serialized_end = 3373
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSRESPONSE']._serialized_start = 3376
    _globals['_GENERATEAUDIENCEOVERLAPINSIGHTSRESPONSE']._serialized_end = 3607
    _globals['_DIMENSIONOVERLAPRESULT']._serialized_start = 3610
    _globals['_DIMENSIONOVERLAPRESULT']._serialized_end = 3813
    _globals['_AUDIENCEOVERLAPITEM']._serialized_start = 3816
    _globals['_AUDIENCEOVERLAPITEM']._serialized_end = 3979
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST']._serialized_start = 3982
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSREQUEST']._serialized_end = 4171
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSRESPONSE']._serialized_start = 4174
    _globals['_GENERATETARGETINGSUGGESTIONMETRICSRESPONSE']._serialized_end = 4302
    _globals['_BASICINSIGHTSAUDIENCE']._serialized_start = 4305
    _globals['_BASICINSIGHTSAUDIENCE']._serialized_end = 4759
    _globals['_INSIGHTSAUDIENCEDEFINITION']._serialized_start = 4762
    _globals['_INSIGHTSAUDIENCEDEFINITION']._serialized_end = 4976
    _globals['_INSIGHTSAUDIENCEDESCRIPTION']._serialized_start = 4979
    _globals['_INSIGHTSAUDIENCEDESCRIPTION']._serialized_end = 5264
    _globals['_INSIGHTSAUDIENCE']._serialized_start = 5267
    _globals['_INSIGHTSAUDIENCE']._serialized_end = 5914
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP']._serialized_start = 5916
    _globals['_INSIGHTSAUDIENCEATTRIBUTEGROUP']._serialized_end = 6033
    _globals['_AUDIENCECOMPOSITIONSECTION']._serialized_start = 6036
    _globals['_AUDIENCECOMPOSITIONSECTION']._serialized_end = 6363
    _globals['_AUDIENCECOMPOSITIONATTRIBUTECLUSTER']._serialized_start = 6366
    _globals['_AUDIENCECOMPOSITIONATTRIBUTECLUSTER']._serialized_end = 6606
    _globals['_AUDIENCECOMPOSITIONMETRICS']._serialized_start = 6608
    _globals['_AUDIENCECOMPOSITIONMETRICS']._serialized_end = 6723
    _globals['_AUDIENCECOMPOSITIONATTRIBUTE']._serialized_start = 6726
    _globals['_AUDIENCECOMPOSITIONATTRIBUTE']._serialized_end = 6932
    _globals['_AUDIENCEINSIGHTSSERVICE']._serialized_start = 6935
    _globals['_AUDIENCEINSIGHTSSERVICE']._serialized_end = 9063