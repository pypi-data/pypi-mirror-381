"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/reach_plan_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import additional_application_info_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_additional__application__info__pb2
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.common import dates_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_dates__pb2
from ......google.ads.googleads.v21.enums import frequency_cap_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_frequency__cap__time__unit__pb2
from ......google.ads.googleads.v21.enums import reach_plan_age_range_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_reach__plan__age__range__pb2
from ......google.ads.googleads.v21.enums import reach_plan_conversion_rate_model_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_reach__plan__conversion__rate__model__pb2
from ......google.ads.googleads.v21.enums import reach_plan_network_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_reach__plan__network__pb2
from ......google.ads.googleads.v21.enums import reach_plan_plannable_user_list_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_reach__plan__plannable__user__list__status__pb2
from ......google.ads.googleads.v21.enums import reach_plan_surface_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_reach__plan__surface__pb2
from ......google.ads.googleads.v21.enums import target_frequency_time_unit_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_target__frequency__time__unit__pb2
from ......google.ads.googleads.v21.enums import user_interest_taxonomy_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__interest__taxonomy__type__pb2
from ......google.ads.googleads.v21.enums import user_list_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_user__list__type__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v21/services/reach_plan_service.proto\x12!google.ads.googleads.v21.services\x1aAgoogle/ads/googleads/v21/common/additional_application_info.proto\x1a.google/ads/googleads/v21/common/criteria.proto\x1a+google/ads/googleads/v21/common/dates.proto\x1a<google/ads/googleads/v21/enums/frequency_cap_time_unit.proto\x1a9google/ads/googleads/v21/enums/reach_plan_age_range.proto\x1aEgoogle/ads/googleads/v21/enums/reach_plan_conversion_rate_model.proto\x1a7google/ads/googleads/v21/enums/reach_plan_network.proto\x1aJgoogle/ads/googleads/v21/enums/reach_plan_plannable_user_list_status.proto\x1a7google/ads/googleads/v21/enums/reach_plan_surface.proto\x1a?google/ads/googleads/v21/enums/target_frequency_time_unit.proto\x1a@google/ads/googleads/v21/enums/user_interest_taxonomy_type.proto\x1a3google/ads/googleads/v21/enums/user_list_type.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xd7\x01\n\x1eGenerateConversionRatesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14customer_reach_group\x18\x02 \x01(\tH\x00\x88\x01\x01\x12_\n\x16reach_application_info\x18\x03 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01B\x17\n\x15_customer_reach_group"\x83\x01\n\x1fGenerateConversionRatesResponse\x12`\n\x1bconversion_rate_suggestions\x18\x01 \x03(\x0b2;.google.ads.googleads.v21.services.ConversionRateSuggestion"\xd1\x01\n\x18ConversionRateSuggestion\x12|\n\x15conversion_rate_model\x18\x01 \x01(\x0e2].google.ads.googleads.v21.enums.ReachPlanConversionRateModelEnum.ReachPlanConversionRateModel\x12\x1e\n\x16plannable_product_code\x18\x02 \x01(\t\x12\x17\n\x0fconversion_rate\x18\x03 \x01(\x01"\x80\x01\n\x1dListPlannableLocationsRequest\x12_\n\x16reach_application_info\x18\x01 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"s\n\x1eListPlannableLocationsResponse\x12Q\n\x13plannable_locations\x18\x01 \x03(\x0b24.google.ads.googleads.v21.services.PlannableLocation"\xd7\x01\n\x11PlannableLocation\x12\x0f\n\x02id\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x05 \x01(\tH\x01\x88\x01\x01\x12\x1e\n\x11parent_country_id\x18\x06 \x01(\x03H\x02\x88\x01\x01\x12\x19\n\x0ccountry_code\x18\x07 \x01(\tH\x03\x88\x01\x01\x12\x1a\n\rlocation_type\x18\x08 \x01(\tH\x04\x88\x01\x01B\x05\n\x03_idB\x07\n\x05_nameB\x14\n\x12_parent_country_idB\x0f\n\r_country_codeB\x10\n\x0e_location_type"\xa3\x01\n\x1cListPlannableProductsRequest\x12"\n\x15plannable_location_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12_\n\x16reach_application_info\x18\x03 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01"m\n\x1dListPlannableProductsResponse\x12L\n\x10product_metadata\x18\x01 \x03(\x0b22.google.ads.googleads.v21.services.ProductMetadata"\xc5\x01\n\x0fProductMetadata\x12#\n\x16plannable_product_code\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x16plannable_product_name\x18\x03 \x01(\t\x12R\n\x13plannable_targeting\x18\x02 \x01(\x0b25.google.ads.googleads.v21.services.PlannableTargetingB\x19\n\x17_plannable_product_code"\xd6\x01\n\x1dListPlannableUserListsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x14customer_reach_group\x18\x02 \x01(\tH\x00\x88\x01\x01\x12_\n\x16reach_application_info\x18\x03 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01B\x17\n\x15_customer_reach_group"t\n\x1eListPlannableUserListsResponse\x12R\n\x14plannable_user_lists\x18\x01 \x03(\x0b24.google.ads.googleads.v21.services.PlannableUserList"\xc8\x02\n\x11PlannableUserList\x12E\n\x0euser_list_info\x18\x01 \x01(\x0b2-.google.ads.googleads.v21.common.UserListInfo\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12U\n\x0euser_list_type\x18\x03 \x01(\x0e2=.google.ads.googleads.v21.enums.UserListTypeEnum.UserListType\x12\x7f\n\x10plannable_status\x18\x04 \x01(\x0e2e.google.ads.googleads.v21.enums.ReachPlanPlannableUserListStatusEnum.ReachPlanPlannableUserListStatus"\xfa\x03\n\x12PlannableTargeting\x12[\n\nage_ranges\x18\x01 \x03(\x0e2G.google.ads.googleads.v21.enums.ReachPlanAgeRangeEnum.ReachPlanAgeRange\x12<\n\x07genders\x18\x02 \x03(\x0b2+.google.ads.googleads.v21.common.GenderInfo\x12<\n\x07devices\x18\x03 \x03(\x0b2+.google.ads.googleads.v21.common.DeviceInfo\x12W\n\x08networks\x18\x04 \x03(\x0e2E.google.ads.googleads.v21.enums.ReachPlanNetworkEnum.ReachPlanNetwork\x12V\n\x16youtube_select_lineups\x18\x05 \x03(\x0b26.google.ads.googleads.v21.services.YouTubeSelectLineUp\x12Z\n\x11surface_targeting\x18\x06 \x01(\x0b2?.google.ads.googleads.v21.services.SurfaceTargetingCombinations"\xf1\x02\n!ListPlannableUserInterestsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x80\x01\n\x1cuser_interest_taxonomy_types\x18\x02 \x03(\x0e2U.google.ads.googleads.v21.enums.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyTypeB\x03\xe0A\x01\x12\x17\n\nname_query\x18\x03 \x01(\tH\x00\x88\x01\x01\x12\x17\n\npath_query\x18\x04 \x01(\tH\x01\x88\x01\x01\x12_\n\x16reach_application_info\x18\x05 \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01B\r\n\x0b_name_queryB\r\n\x0b_path_query"\x80\x01\n"ListPlannableUserInterestsResponse\x12Z\n\x18plannable_user_interests\x18\x01 \x03(\x0b28.google.ads.googleads.v21.services.PlannableUserInterest"\x94\x02\n\x15PlannableUserInterest\x12H\n\ruser_interest\x18\x01 \x01(\x0b21.google.ads.googleads.v21.common.UserInterestInfo\x12q\n\x12user_interest_type\x18\x02 \x01(\x0e2U.google.ads.googleads.v21.enums.UserInterestTaxonomyTypeEnum.UserInterestTaxonomyType\x12"\n\x1auser_interest_display_name\x18\x03 \x01(\t\x12\x1a\n\x12user_interest_path\x18\x04 \x01(\t"\x9d\x07\n\x1cGenerateReachForecastRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rcurrency_code\x18\t \x01(\tH\x00\x88\x01\x01\x12S\n\x11campaign_duration\x18\x03 \x01(\x0b23.google.ads.googleads.v21.services.CampaignDurationB\x03\xe0A\x02\x12!\n\x14cookie_frequency_cap\x18\n \x01(\x05H\x01\x88\x01\x01\x12U\n\x1ccookie_frequency_cap_setting\x18\x08 \x01(\x0b2/.google.ads.googleads.v21.services.FrequencyCap\x12$\n\x17min_effective_frequency\x18\x0b \x01(\x05H\x02\x88\x01\x01\x12b\n\x19effective_frequency_limit\x18\x0c \x01(\x0b2:.google.ads.googleads.v21.services.EffectiveFrequencyLimitH\x03\x88\x01\x01\x12?\n\ttargeting\x18\x06 \x01(\x0b2,.google.ads.googleads.v21.services.Targeting\x12P\n\x10planned_products\x18\x07 \x03(\x0b21.google.ads.googleads.v21.services.PlannedProductB\x03\xe0A\x02\x12Y\n\x17forecast_metric_options\x18\r \x01(\x0b28.google.ads.googleads.v21.services.ForecastMetricOptions\x12!\n\x14customer_reach_group\x18\x0e \x01(\tH\x04\x88\x01\x01\x12_\n\x16reach_application_info\x18\x0f \x01(\x0b2:.google.ads.googleads.v21.common.AdditionalApplicationInfoB\x03\xe0A\x01B\x10\n\x0e_currency_codeB\x17\n\x15_cookie_frequency_capB\x1a\n\x18_min_effective_frequencyB\x1c\n\x1a_effective_frequency_limitB\x17\n\x15_customer_reach_group"F\n\x17EffectiveFrequencyLimit\x12+\n#effective_frequency_breakdown_limit\x18\x01 \x01(\x05"\x8f\x01\n\x0cFrequencyCap\x12\x18\n\x0bimpressions\x18\x03 \x01(\x05B\x03\xe0A\x02\x12e\n\ttime_unit\x18\x02 \x01(\x0e2M.google.ads.googleads.v21.enums.FrequencyCapTimeUnitEnum.FrequencyCapTimeUnitB\x03\xe0A\x02"\xeb\x03\n\tTargeting\x12"\n\x15plannable_location_id\x18\x06 \x01(\tH\x00\x88\x01\x01\x12\x1e\n\x16plannable_location_ids\x18\x08 \x03(\t\x12Z\n\tage_range\x18\x02 \x01(\x0e2G.google.ads.googleads.v21.enums.ReachPlanAgeRangeEnum.ReachPlanAgeRange\x12<\n\x07genders\x18\x03 \x03(\x0b2+.google.ads.googleads.v21.common.GenderInfo\x12<\n\x07devices\x18\x04 \x03(\x0b2+.google.ads.googleads.v21.common.DeviceInfo\x12V\n\x07network\x18\x05 \x01(\x0e2E.google.ads.googleads.v21.enums.ReachPlanNetworkEnum.ReachPlanNetwork\x12P\n\x12audience_targeting\x18\x07 \x01(\x0b24.google.ads.googleads.v21.services.AudienceTargetingB\x18\n\x16_plannable_location_id"\x86\x01\n\x10CampaignDuration\x12\x1d\n\x10duration_in_days\x18\x02 \x01(\x05H\x00\x88\x01\x01\x12>\n\ndate_range\x18\x03 \x01(\x0b2*.google.ads.googleads.v21.common.DateRangeB\x13\n\x11_duration_in_days"\x9b\x02\n\x0ePlannedProduct\x12(\n\x16plannable_product_code\x18\x03 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x1f\n\rbudget_micros\x18\x04 \x01(\x03B\x03\xe0A\x02H\x01\x88\x01\x01\x12\x1c\n\x0fconversion_rate\x18\x06 \x01(\x01H\x02\x88\x01\x01\x12_\n\x1aadvanced_product_targeting\x18\x05 \x01(\x0b2;.google.ads.googleads.v21.services.AdvancedProductTargetingB\x19\n\x17_plannable_product_codeB\x10\n\x0e_budget_microsB\x12\n\x10_conversion_rate"\xc3\x01\n\x1dGenerateReachForecastResponse\x12^\n\x1aon_target_audience_metrics\x18\x01 \x01(\x0b2:.google.ads.googleads.v21.services.OnTargetAudienceMetrics\x12B\n\x0breach_curve\x18\x02 \x01(\x0b2-.google.ads.googleads.v21.services.ReachCurve"W\n\nReachCurve\x12I\n\x0freach_forecasts\x18\x01 \x03(\x0b20.google.ads.googleads.v21.services.ReachForecast"\xcc\x01\n\rReachForecast\x12\x13\n\x0bcost_micros\x18\x05 \x01(\x03\x12=\n\x08forecast\x18\x02 \x01(\x0b2+.google.ads.googleads.v21.services.Forecast\x12g\n\x1fplanned_product_reach_forecasts\x18\x04 \x03(\x0b2>.google.ads.googleads.v21.services.PlannedProductReachForecast"\xce\x05\n\x08Forecast\x12\x1c\n\x0fon_target_reach\x18\x05 \x01(\x03H\x00\x88\x01\x01\x12\x18\n\x0btotal_reach\x18\x06 \x01(\x03H\x01\x88\x01\x01\x12"\n\x15on_target_impressions\x18\x07 \x01(\x03H\x02\x88\x01\x01\x12\x1e\n\x11total_impressions\x18\x08 \x01(\x03H\x03\x88\x01\x01\x12!\n\x14viewable_impressions\x18\t \x01(\x03H\x04\x88\x01\x01\x12f\n\x1eeffective_frequency_breakdowns\x18\n \x03(\x0b2>.google.ads.googleads.v21.services.EffectiveFrequencyBreakdown\x12#\n\x16on_target_coview_reach\x18\x0b \x01(\x03H\x05\x88\x01\x01\x12\x1f\n\x12total_coview_reach\x18\x0c \x01(\x03H\x06\x88\x01\x01\x12)\n\x1con_target_coview_impressions\x18\r \x01(\x03H\x07\x88\x01\x01\x12%\n\x18total_coview_impressions\x18\x0e \x01(\x03H\x08\x88\x01\x01\x12\x12\n\x05views\x18\x0f \x01(\x03H\t\x88\x01\x01\x12\x18\n\x0bconversions\x18\x10 \x01(\x01H\n\x88\x01\x01B\x12\n\x10_on_target_reachB\x0e\n\x0c_total_reachB\x18\n\x16_on_target_impressionsB\x14\n\x12_total_impressionsB\x17\n\x15_viewable_impressionsB\x19\n\x17_on_target_coview_reachB\x15\n\x13_total_coview_reachB\x1f\n\x1d_on_target_coview_impressionsB\x1b\n\x19_total_coview_impressionsB\x08\n\x06_viewsB\x0e\n\x0c_conversions"\xaf\x01\n\x1bPlannedProductReachForecast\x12\x1e\n\x16plannable_product_code\x18\x01 \x01(\t\x12\x13\n\x0bcost_micros\x18\x02 \x01(\x03\x12[\n\x18planned_product_forecast\x18\x03 \x01(\x0b29.google.ads.googleads.v21.services.PlannedProductForecast"\xc2\x04\n\x16PlannedProductForecast\x12\x17\n\x0fon_target_reach\x18\x01 \x01(\x03\x12\x13\n\x0btotal_reach\x18\x02 \x01(\x03\x12\x1d\n\x15on_target_impressions\x18\x03 \x01(\x03\x12\x19\n\x11total_impressions\x18\x04 \x01(\x03\x12!\n\x14viewable_impressions\x18\x05 \x01(\x03H\x00\x88\x01\x01\x12#\n\x16on_target_coview_reach\x18\x06 \x01(\x03H\x01\x88\x01\x01\x12\x1f\n\x12total_coview_reach\x18\x07 \x01(\x03H\x02\x88\x01\x01\x12)\n\x1con_target_coview_impressions\x18\x08 \x01(\x03H\x03\x88\x01\x01\x12%\n\x18total_coview_impressions\x18\t \x01(\x03H\x04\x88\x01\x01\x12\x1e\n\x11average_frequency\x18\n \x01(\x01H\x05\x88\x01\x01\x12\x12\n\x05views\x18\x0b \x01(\x03H\x06\x88\x01\x01\x12\x18\n\x0bconversions\x18\x0c \x01(\x01H\x07\x88\x01\x01B\x17\n\x15_viewable_impressionsB\x19\n\x17_on_target_coview_reachB\x15\n\x13_total_coview_reachB\x1f\n\x1d_on_target_coview_impressionsB\x1b\n\x19_total_coview_impressionsB\x14\n\x12_average_frequencyB\x08\n\x06_viewsB\x0e\n\x0c_conversions"\x93\x01\n\x17OnTargetAudienceMetrics\x12"\n\x15youtube_audience_size\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12!\n\x14census_audience_size\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x18\n\x16_youtube_audience_sizeB\x17\n\x15_census_audience_size"\xfc\x01\n\x1bEffectiveFrequencyBreakdown\x12\x1b\n\x13effective_frequency\x18\x01 \x01(\x05\x12\x17\n\x0fon_target_reach\x18\x02 \x01(\x03\x12\x13\n\x0btotal_reach\x18\x03 \x01(\x03\x12#\n\x16effective_coview_reach\x18\x04 \x01(\x03H\x00\x88\x01\x01\x12-\n on_target_effective_coview_reach\x18\x05 \x01(\x03H\x01\x88\x01\x01B\x19\n\x17_effective_coview_reachB#\n!_on_target_effective_coview_reach"/\n\x15ForecastMetricOptions\x12\x16\n\x0einclude_coview\x18\x01 \x01(\x08"\xa0\x01\n\x11AudienceTargeting\x12H\n\ruser_interest\x18\x01 \x03(\x0b21.google.ads.googleads.v21.common.UserInterestInfo\x12A\n\nuser_lists\x18\x02 \x03(\x0b2-.google.ads.googleads.v21.common.UserListInfo"\xc5\x02\n\x18AdvancedProductTargeting\x12W\n\x1asurface_targeting_settings\x18\x02 \x01(\x0b23.google.ads.googleads.v21.services.SurfaceTargeting\x12]\n\x19target_frequency_settings\x18\x03 \x01(\x0b2:.google.ads.googleads.v21.services.TargetFrequencySettings\x12[\n\x17youtube_select_settings\x18\x01 \x01(\x0b28.google.ads.googleads.v21.services.YouTubeSelectSettingsH\x00B\x14\n\x12advanced_targeting"*\n\x15YouTubeSelectSettings\x12\x11\n\tlineup_id\x18\x01 \x01(\x03"=\n\x13YouTubeSelectLineUp\x12\x11\n\tlineup_id\x18\x01 \x01(\x03\x12\x13\n\x0blineup_name\x18\x02 \x01(\t"\xcd\x01\n\x1cSurfaceTargetingCombinations\x12N\n\x11default_targeting\x18\x01 \x01(\x0b23.google.ads.googleads.v21.services.SurfaceTargeting\x12]\n available_targeting_combinations\x18\x02 \x03(\x0b23.google.ads.googleads.v21.services.SurfaceTargeting"k\n\x10SurfaceTargeting\x12W\n\x08surfaces\x18\x01 \x03(\x0e2E.google.ads.googleads.v21.enums.ReachPlanSurfaceEnum.ReachPlanSurface"\xa5\x01\n\x17TargetFrequencySettings\x12k\n\ttime_unit\x18\x01 \x01(\x0e2S.google.ads.googleads.v21.enums.TargetFrequencyTimeUnitEnum.TargetFrequencyTimeUnitB\x03\xe0A\x02\x12\x1d\n\x10target_frequency\x18\x02 \x01(\x05B\x03\xe0A\x022\xa2\x0b\n\x10ReachPlanService\x12\xd7\x01\n\x17GenerateConversionRates\x12A.google.ads.googleads.v21.services.GenerateConversionRatesRequest\x1aB.google.ads.googleads.v21.services.GenerateConversionRatesResponse"5\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02!"\x1c/v21:generateConversionRates:\x01*\x12\xc5\x01\n\x16ListPlannableLocations\x12@.google.ads.googleads.v21.services.ListPlannableLocationsRequest\x1aA.google.ads.googleads.v21.services.ListPlannableLocationsResponse"&\x82\xd3\xe4\x93\x02 "\x1b/v21:listPlannableLocations:\x01*\x12\xd9\x01\n\x15ListPlannableProducts\x12?.google.ads.googleads.v21.services.ListPlannableProductsRequest\x1a@.google.ads.googleads.v21.services.ListPlannableProductsResponse"=\xdaA\x15plannable_location_id\x82\xd3\xe4\x93\x02\x1f"\x1a/v21:listPlannableProducts:\x01*\x12\x8c\x02\n\x15GenerateReachForecast\x12?.google.ads.googleads.v21.services.GenerateReachForecastRequest\x1a@.google.ads.googleads.v21.services.GenerateReachForecastResponse"p\xdaA.customer_id,campaign_duration,planned_products\x82\xd3\xe4\x93\x029"4/v21/customers/{customer_id=*}:generateReachForecast:\x01*\x12\xd3\x01\n\x16ListPlannableUserLists\x12@.google.ads.googleads.v21.services.ListPlannableUserListsRequest\x1aA.google.ads.googleads.v21.services.ListPlannableUserListsResponse"4\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02 "\x1b/v21:listPlannableUserLists:\x01*\x12\xe3\x01\n\x1aListPlannableUserInterests\x12D.google.ads.googleads.v21.services.ListPlannableUserInterestsRequest\x1aE.google.ads.googleads.v21.services.ListPlannableUserInterestsResponse"8\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02$"\x1f/v21:listPlannableUserInterests:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x81\x02\n%com.google.ads.googleads.v21.servicesB\x15ReachPlanServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.reach_plan_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x15ReachPlanServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_GENERATECONVERSIONRATESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATECONVERSIONRATESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATECONVERSIONRATESREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_GENERATECONVERSIONRATESREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLANNABLELOCATIONSREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_LISTPLANNABLELOCATIONSREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLANNABLEPRODUCTSREQUEST'].fields_by_name['plannable_location_id']._loaded_options = None
    _globals['_LISTPLANNABLEPRODUCTSREQUEST'].fields_by_name['plannable_location_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPLANNABLEPRODUCTSREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_LISTPLANNABLEPRODUCTSREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLANNABLEUSERLISTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTPLANNABLEUSERLISTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPLANNABLEUSERLISTSREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_LISTPLANNABLEUSERLISTSREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['user_interest_taxonomy_types']._loaded_options = None
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['user_interest_taxonomy_types']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['campaign_duration']._loaded_options = None
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['campaign_duration']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['planned_products']._loaded_options = None
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['planned_products']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['reach_application_info']._loaded_options = None
    _globals['_GENERATEREACHFORECASTREQUEST'].fields_by_name['reach_application_info']._serialized_options = b'\xe0A\x01'
    _globals['_FREQUENCYCAP'].fields_by_name['impressions']._loaded_options = None
    _globals['_FREQUENCYCAP'].fields_by_name['impressions']._serialized_options = b'\xe0A\x02'
    _globals['_FREQUENCYCAP'].fields_by_name['time_unit']._loaded_options = None
    _globals['_FREQUENCYCAP'].fields_by_name['time_unit']._serialized_options = b'\xe0A\x02'
    _globals['_PLANNEDPRODUCT'].fields_by_name['plannable_product_code']._loaded_options = None
    _globals['_PLANNEDPRODUCT'].fields_by_name['plannable_product_code']._serialized_options = b'\xe0A\x02'
    _globals['_PLANNEDPRODUCT'].fields_by_name['budget_micros']._loaded_options = None
    _globals['_PLANNEDPRODUCT'].fields_by_name['budget_micros']._serialized_options = b'\xe0A\x02'
    _globals['_TARGETFREQUENCYSETTINGS'].fields_by_name['time_unit']._loaded_options = None
    _globals['_TARGETFREQUENCYSETTINGS'].fields_by_name['time_unit']._serialized_options = b'\xe0A\x02'
    _globals['_TARGETFREQUENCYSETTINGS'].fields_by_name['target_frequency']._loaded_options = None
    _globals['_TARGETFREQUENCYSETTINGS'].fields_by_name['target_frequency']._serialized_options = b'\xe0A\x02'
    _globals['_REACHPLANSERVICE']._loaded_options = None
    _globals['_REACHPLANSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_REACHPLANSERVICE'].methods_by_name['GenerateConversionRates']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['GenerateConversionRates']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02!"\x1c/v21:generateConversionRates:\x01*'
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableLocations']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableLocations']._serialized_options = b'\x82\xd3\xe4\x93\x02 "\x1b/v21:listPlannableLocations:\x01*'
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableProducts']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableProducts']._serialized_options = b'\xdaA\x15plannable_location_id\x82\xd3\xe4\x93\x02\x1f"\x1a/v21:listPlannableProducts:\x01*'
    _globals['_REACHPLANSERVICE'].methods_by_name['GenerateReachForecast']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['GenerateReachForecast']._serialized_options = b'\xdaA.customer_id,campaign_duration,planned_products\x82\xd3\xe4\x93\x029"4/v21/customers/{customer_id=*}:generateReachForecast:\x01*'
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableUserLists']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableUserLists']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02 "\x1b/v21:listPlannableUserLists:\x01*'
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableUserInterests']._loaded_options = None
    _globals['_REACHPLANSERVICE'].methods_by_name['ListPlannableUserInterests']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x02$"\x1f/v21:listPlannableUserInterests:\x01*'
    _globals['_GENERATECONVERSIONRATESREQUEST']._serialized_start = 912
    _globals['_GENERATECONVERSIONRATESREQUEST']._serialized_end = 1127
    _globals['_GENERATECONVERSIONRATESRESPONSE']._serialized_start = 1130
    _globals['_GENERATECONVERSIONRATESRESPONSE']._serialized_end = 1261
    _globals['_CONVERSIONRATESUGGESTION']._serialized_start = 1264
    _globals['_CONVERSIONRATESUGGESTION']._serialized_end = 1473
    _globals['_LISTPLANNABLELOCATIONSREQUEST']._serialized_start = 1476
    _globals['_LISTPLANNABLELOCATIONSREQUEST']._serialized_end = 1604
    _globals['_LISTPLANNABLELOCATIONSRESPONSE']._serialized_start = 1606
    _globals['_LISTPLANNABLELOCATIONSRESPONSE']._serialized_end = 1721
    _globals['_PLANNABLELOCATION']._serialized_start = 1724
    _globals['_PLANNABLELOCATION']._serialized_end = 1939
    _globals['_LISTPLANNABLEPRODUCTSREQUEST']._serialized_start = 1942
    _globals['_LISTPLANNABLEPRODUCTSREQUEST']._serialized_end = 2105
    _globals['_LISTPLANNABLEPRODUCTSRESPONSE']._serialized_start = 2107
    _globals['_LISTPLANNABLEPRODUCTSRESPONSE']._serialized_end = 2216
    _globals['_PRODUCTMETADATA']._serialized_start = 2219
    _globals['_PRODUCTMETADATA']._serialized_end = 2416
    _globals['_LISTPLANNABLEUSERLISTSREQUEST']._serialized_start = 2419
    _globals['_LISTPLANNABLEUSERLISTSREQUEST']._serialized_end = 2633
    _globals['_LISTPLANNABLEUSERLISTSRESPONSE']._serialized_start = 2635
    _globals['_LISTPLANNABLEUSERLISTSRESPONSE']._serialized_end = 2751
    _globals['_PLANNABLEUSERLIST']._serialized_start = 2754
    _globals['_PLANNABLEUSERLIST']._serialized_end = 3082
    _globals['_PLANNABLETARGETING']._serialized_start = 3085
    _globals['_PLANNABLETARGETING']._serialized_end = 3591
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST']._serialized_start = 3594
    _globals['_LISTPLANNABLEUSERINTERESTSREQUEST']._serialized_end = 3963
    _globals['_LISTPLANNABLEUSERINTERESTSRESPONSE']._serialized_start = 3966
    _globals['_LISTPLANNABLEUSERINTERESTSRESPONSE']._serialized_end = 4094
    _globals['_PLANNABLEUSERINTEREST']._serialized_start = 4097
    _globals['_PLANNABLEUSERINTEREST']._serialized_end = 4373
    _globals['_GENERATEREACHFORECASTREQUEST']._serialized_start = 4376
    _globals['_GENERATEREACHFORECASTREQUEST']._serialized_end = 5301
    _globals['_EFFECTIVEFREQUENCYLIMIT']._serialized_start = 5303
    _globals['_EFFECTIVEFREQUENCYLIMIT']._serialized_end = 5373
    _globals['_FREQUENCYCAP']._serialized_start = 5376
    _globals['_FREQUENCYCAP']._serialized_end = 5519
    _globals['_TARGETING']._serialized_start = 5522
    _globals['_TARGETING']._serialized_end = 6013
    _globals['_CAMPAIGNDURATION']._serialized_start = 6016
    _globals['_CAMPAIGNDURATION']._serialized_end = 6150
    _globals['_PLANNEDPRODUCT']._serialized_start = 6153
    _globals['_PLANNEDPRODUCT']._serialized_end = 6436
    _globals['_GENERATEREACHFORECASTRESPONSE']._serialized_start = 6439
    _globals['_GENERATEREACHFORECASTRESPONSE']._serialized_end = 6634
    _globals['_REACHCURVE']._serialized_start = 6636
    _globals['_REACHCURVE']._serialized_end = 6723
    _globals['_REACHFORECAST']._serialized_start = 6726
    _globals['_REACHFORECAST']._serialized_end = 6930
    _globals['_FORECAST']._serialized_start = 6933
    _globals['_FORECAST']._serialized_end = 7651
    _globals['_PLANNEDPRODUCTREACHFORECAST']._serialized_start = 7654
    _globals['_PLANNEDPRODUCTREACHFORECAST']._serialized_end = 7829
    _globals['_PLANNEDPRODUCTFORECAST']._serialized_start = 7832
    _globals['_PLANNEDPRODUCTFORECAST']._serialized_end = 8410
    _globals['_ONTARGETAUDIENCEMETRICS']._serialized_start = 8413
    _globals['_ONTARGETAUDIENCEMETRICS']._serialized_end = 8560
    _globals['_EFFECTIVEFREQUENCYBREAKDOWN']._serialized_start = 8563
    _globals['_EFFECTIVEFREQUENCYBREAKDOWN']._serialized_end = 8815
    _globals['_FORECASTMETRICOPTIONS']._serialized_start = 8817
    _globals['_FORECASTMETRICOPTIONS']._serialized_end = 8864
    _globals['_AUDIENCETARGETING']._serialized_start = 8867
    _globals['_AUDIENCETARGETING']._serialized_end = 9027
    _globals['_ADVANCEDPRODUCTTARGETING']._serialized_start = 9030
    _globals['_ADVANCEDPRODUCTTARGETING']._serialized_end = 9355
    _globals['_YOUTUBESELECTSETTINGS']._serialized_start = 9357
    _globals['_YOUTUBESELECTSETTINGS']._serialized_end = 9399
    _globals['_YOUTUBESELECTLINEUP']._serialized_start = 9401
    _globals['_YOUTUBESELECTLINEUP']._serialized_end = 9462
    _globals['_SURFACETARGETINGCOMBINATIONS']._serialized_start = 9465
    _globals['_SURFACETARGETINGCOMBINATIONS']._serialized_end = 9670
    _globals['_SURFACETARGETING']._serialized_start = 9672
    _globals['_SURFACETARGETING']._serialized_end = 9779
    _globals['_TARGETFREQUENCYSETTINGS']._serialized_start = 9782
    _globals['_TARGETFREQUENCYSETTINGS']._serialized_end = 9947
    _globals['_REACHPLANSERVICE']._serialized_start = 9950
    _globals['_REACHPLANSERVICE']._serialized_end = 11392