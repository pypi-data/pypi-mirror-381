"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/common/criteria.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import age_range_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_age__range__type__pb2
from ......google.ads.googleads.v21.enums import app_payment_model_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_app__payment__model__type__pb2
from ......google.ads.googleads.v21.enums import brand_request_rejection_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_brand__request__rejection__reason__pb2
from ......google.ads.googleads.v21.enums import brand_state_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_brand__state__pb2
from ......google.ads.googleads.v21.enums import content_label_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_content__label__type__pb2
from ......google.ads.googleads.v21.enums import day_of_week_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_day__of__week__pb2
from ......google.ads.googleads.v21.enums import device_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_device__pb2
from ......google.ads.googleads.v21.enums import gender_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_gender__type__pb2
from ......google.ads.googleads.v21.enums import hotel_date_selection_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_hotel__date__selection__type__pb2
from ......google.ads.googleads.v21.enums import income_range_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_income__range__type__pb2
from ......google.ads.googleads.v21.enums import interaction_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_interaction__type__pb2
from ......google.ads.googleads.v21.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_keyword__match__type__pb2
from ......google.ads.googleads.v21.enums import listing_group_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_listing__group__type__pb2
from ......google.ads.googleads.v21.enums import location_group_radius_units_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_location__group__radius__units__pb2
from ......google.ads.googleads.v21.enums import minute_of_hour_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_minute__of__hour__pb2
from ......google.ads.googleads.v21.enums import parental_status_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_parental__status__type__pb2
from ......google.ads.googleads.v21.enums import product_category_level_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__category__level__pb2
from ......google.ads.googleads.v21.enums import product_channel_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__channel__pb2
from ......google.ads.googleads.v21.enums import product_channel_exclusivity_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__channel__exclusivity__pb2
from ......google.ads.googleads.v21.enums import product_condition_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__condition__pb2
from ......google.ads.googleads.v21.enums import product_custom_attribute_index_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__custom__attribute__index__pb2
from ......google.ads.googleads.v21.enums import product_type_level_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_product__type__level__pb2
from ......google.ads.googleads.v21.enums import proximity_radius_units_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_proximity__radius__units__pb2
from ......google.ads.googleads.v21.enums import webpage_condition_operand_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_webpage__condition__operand__pb2
from ......google.ads.googleads.v21.enums import webpage_condition_operator_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_webpage__condition__operator__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/googleads/v21/common/criteria.proto\x12\x1fgoogle.ads.googleads.v21.common\x1a3google/ads/googleads/v21/enums/age_range_type.proto\x1a;google/ads/googleads/v21/enums/app_payment_model_type.proto\x1aCgoogle/ads/googleads/v21/enums/brand_request_rejection_reason.proto\x1a0google/ads/googleads/v21/enums/brand_state.proto\x1a7google/ads/googleads/v21/enums/content_label_type.proto\x1a0google/ads/googleads/v21/enums/day_of_week.proto\x1a+google/ads/googleads/v21/enums/device.proto\x1a0google/ads/googleads/v21/enums/gender_type.proto\x1a>google/ads/googleads/v21/enums/hotel_date_selection_type.proto\x1a6google/ads/googleads/v21/enums/income_range_type.proto\x1a5google/ads/googleads/v21/enums/interaction_type.proto\x1a7google/ads/googleads/v21/enums/keyword_match_type.proto\x1a7google/ads/googleads/v21/enums/listing_group_type.proto\x1a@google/ads/googleads/v21/enums/location_group_radius_units.proto\x1a3google/ads/googleads/v21/enums/minute_of_hour.proto\x1a9google/ads/googleads/v21/enums/parental_status_type.proto\x1a;google/ads/googleads/v21/enums/product_category_level.proto\x1a4google/ads/googleads/v21/enums/product_channel.proto\x1a@google/ads/googleads/v21/enums/product_channel_exclusivity.proto\x1a6google/ads/googleads/v21/enums/product_condition.proto\x1aCgoogle/ads/googleads/v21/enums/product_custom_attribute_index.proto\x1a7google/ads/googleads/v21/enums/product_type_level.proto\x1a;google/ads/googleads/v21/enums/proximity_radius_units.proto\x1a>google/ads/googleads/v21/enums/webpage_condition_operand.proto\x1a?google/ads/googleads/v21/enums/webpage_condition_operator.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x84\x01\n\x0bKeywordInfo\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x12Y\n\nmatch_type\x18\x02 \x01(\x0e2E.google.ads.googleads.v21.enums.KeywordMatchTypeEnum.KeywordMatchTypeB\x07\n\x05_text")\n\rPlacementInfo\x12\x10\n\x03url\x18\x02 \x01(\tH\x00\x88\x01\x01B\x06\n\x04_url"A\n\x17NegativeKeywordListInfo\x12\x17\n\nshared_set\x18\x01 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_shared_set"\x9c\x01\n\x15MobileAppCategoryInfo\x12b\n\x1cmobile_app_category_constant\x18\x02 \x01(\tB7\xfaA4\n2googleads.googleapis.com/MobileAppCategoryConstantH\x00\x88\x01\x01B\x1f\n\x1d_mobile_app_category_constant"S\n\x15MobileApplicationInfo\x12\x13\n\x06app_id\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x11\n\x04name\x18\x05 \x01(\tH\x01\x88\x01\x01B\t\n\x07_app_idB\x07\n\x05_name"H\n\x0cLocationInfo\x12 \n\x13geo_target_constant\x18\x02 \x01(\tH\x00\x88\x01\x01B\x16\n\x14_geo_target_constant"M\n\nDeviceInfo\x12?\n\x04type\x18\x01 \x01(\x0e21.google.ads.googleads.v21.enums.DeviceEnum.Device"\xcb\x02\n\x10ListingGroupInfo\x12S\n\x04type\x18\x01 \x01(\x0e2E.google.ads.googleads.v21.enums.ListingGroupTypeEnum.ListingGroupType\x12I\n\ncase_value\x18\x02 \x01(\x0b25.google.ads.googleads.v21.common.ListingDimensionInfo\x12&\n\x19parent_ad_group_criterion\x18\x04 \x01(\tH\x00\x88\x01\x01\x12H\n\x04path\x18\x05 \x01(\x0b25.google.ads.googleads.v21.common.ListingDimensionPathH\x01\x88\x01\x01B\x1c\n\x1a_parent_ad_group_criterionB\x07\n\x05_path"a\n\x14ListingDimensionPath\x12I\n\ndimensions\x18\x01 \x03(\x0b25.google.ads.googleads.v21.common.ListingDimensionInfo"]\n\x10ListingScopeInfo\x12I\n\ndimensions\x18\x02 \x03(\x0b25.google.ads.googleads.v21.common.ListingDimensionInfo"\xf2\x0e\n\x14ListingDimensionInfo\x12@\n\x08hotel_id\x18\x02 \x01(\x0b2,.google.ads.googleads.v21.common.HotelIdInfoH\x00\x12F\n\x0bhotel_class\x18\x03 \x01(\x0b2/.google.ads.googleads.v21.common.HotelClassInfoH\x00\x12W\n\x14hotel_country_region\x18\x04 \x01(\x0b27.google.ads.googleads.v21.common.HotelCountryRegionInfoH\x00\x12F\n\x0bhotel_state\x18\x05 \x01(\x0b2/.google.ads.googleads.v21.common.HotelStateInfoH\x00\x12D\n\nhotel_city\x18\x06 \x01(\x0b2..google.ads.googleads.v21.common.HotelCityInfoH\x00\x12P\n\x10product_category\x18\x18 \x01(\x0b24.google.ads.googleads.v21.common.ProductCategoryInfoH\x00\x12J\n\rproduct_brand\x18\x0f \x01(\x0b21.google.ads.googleads.v21.common.ProductBrandInfoH\x00\x12N\n\x0fproduct_channel\x18\x08 \x01(\x0b23.google.ads.googleads.v21.common.ProductChannelInfoH\x00\x12e\n\x1bproduct_channel_exclusivity\x18\t \x01(\x0b2>.google.ads.googleads.v21.common.ProductChannelExclusivityInfoH\x00\x12R\n\x11product_condition\x18\n \x01(\x0b25.google.ads.googleads.v21.common.ProductConditionInfoH\x00\x12_\n\x18product_custom_attribute\x18\x10 \x01(\x0b2;.google.ads.googleads.v21.common.ProductCustomAttributeInfoH\x00\x12M\n\x0fproduct_item_id\x18\x0b \x01(\x0b22.google.ads.googleads.v21.common.ProductItemIdInfoH\x00\x12H\n\x0cproduct_type\x18\x0c \x01(\x0b20.google.ads.googleads.v21.common.ProductTypeInfoH\x00\x12P\n\x10product_grouping\x18\x11 \x01(\x0b24.google.ads.googleads.v21.common.ProductGroupingInfoH\x00\x12L\n\x0eproduct_labels\x18\x12 \x01(\x0b22.google.ads.googleads.v21.common.ProductLabelsInfoH\x00\x12_\n\x18product_legacy_condition\x18\x13 \x01(\x0b2;.google.ads.googleads.v21.common.ProductLegacyConditionInfoH\x00\x12Q\n\x11product_type_full\x18\x14 \x01(\x0b24.google.ads.googleads.v21.common.ProductTypeFullInfoH\x00\x12F\n\x0bactivity_id\x18\x15 \x01(\x0b2/.google.ads.googleads.v21.common.ActivityIdInfoH\x00\x12N\n\x0factivity_rating\x18\x16 \x01(\x0b23.google.ads.googleads.v21.common.ActivityRatingInfoH\x00\x12P\n\x10activity_country\x18\x17 \x01(\x0b24.google.ads.googleads.v21.common.ActivityCountryInfoH\x00\x12L\n\x0eactivity_state\x18\x19 \x01(\x0b22.google.ads.googleads.v21.common.ActivityStateInfoH\x00\x12J\n\ractivity_city\x18\x1a \x01(\x0b21.google.ads.googleads.v21.common.ActivityCityInfoH\x00\x12a\n\x19unknown_listing_dimension\x18\x0e \x01(\x0b2<.google.ads.googleads.v21.common.UnknownListingDimensionInfoH\x00B\x0b\n\tdimension"+\n\x0bHotelIdInfo\x12\x12\n\x05value\x18\x02 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value".\n\x0eHotelClassInfo\x12\x12\n\x05value\x18\x02 \x01(\x03H\x00\x88\x01\x01B\x08\n\x06_value"\\\n\x16HotelCountryRegionInfo\x12%\n\x18country_region_criterion\x18\x02 \x01(\tH\x00\x88\x01\x01B\x1b\n\x19_country_region_criterion"B\n\x0eHotelStateInfo\x12\x1c\n\x0fstate_criterion\x18\x02 \x01(\tH\x00\x88\x01\x01B\x12\n\x10_state_criterion"?\n\rHotelCityInfo\x12\x1b\n\x0ecity_criterion\x18\x02 \x01(\tH\x00\x88\x01\x01B\x11\n\x0f_city_criterion"\x9d\x01\n\x13ProductCategoryInfo\x12\x18\n\x0bcategory_id\x18\x01 \x01(\x03H\x00\x88\x01\x01\x12\\\n\x05level\x18\x02 \x01(\x0e2M.google.ads.googleads.v21.enums.ProductCategoryLevelEnum.ProductCategoryLevelB\x0e\n\x0c_category_id"0\n\x10ProductBrandInfo\x12\x12\n\x05value\x18\x02 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"h\n\x12ProductChannelInfo\x12R\n\x07channel\x18\x01 \x01(\x0e2A.google.ads.googleads.v21.enums.ProductChannelEnum.ProductChannel"\x95\x01\n\x1dProductChannelExclusivityInfo\x12t\n\x13channel_exclusivity\x18\x01 \x01(\x0e2W.google.ads.googleads.v21.enums.ProductChannelExclusivityEnum.ProductChannelExclusivity"p\n\x14ProductConditionInfo\x12X\n\tcondition\x18\x01 \x01(\x0e2E.google.ads.googleads.v21.enums.ProductConditionEnum.ProductCondition"\xa6\x01\n\x1aProductCustomAttributeInfo\x12\x12\n\x05value\x18\x03 \x01(\tH\x00\x88\x01\x01\x12j\n\x05index\x18\x02 \x01(\x0e2[.google.ads.googleads.v21.enums.ProductCustomAttributeIndexEnum.ProductCustomAttributeIndexB\x08\n\x06_value"1\n\x11ProductItemIdInfo\x12\x12\n\x05value\x18\x02 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"\x85\x01\n\x0fProductTypeInfo\x12\x12\n\x05value\x18\x03 \x01(\tH\x00\x88\x01\x01\x12T\n\x05level\x18\x02 \x01(\x0e2E.google.ads.googleads.v21.enums.ProductTypeLevelEnum.ProductTypeLevelB\x08\n\x06_value"3\n\x13ProductGroupingInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"1\n\x11ProductLabelsInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value":\n\x1aProductLegacyConditionInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"3\n\x13ProductTypeFullInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"\x1d\n\x1bUnknownListingDimensionInfo"}\n\x1aHotelDateSelectionTypeInfo\x12_\n\x04type\x18\x01 \x01(\x0e2Q.google.ads.googleads.v21.enums.HotelDateSelectionTypeEnum.HotelDateSelectionType"g\n\x1dHotelAdvanceBookingWindowInfo\x12\x15\n\x08min_days\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12\x15\n\x08max_days\x18\x04 \x01(\x03H\x01\x88\x01\x01B\x0b\n\t_min_daysB\x0b\n\t_max_days"g\n\x15HotelLengthOfStayInfo\x12\x17\n\nmin_nights\x18\x03 \x01(\x03H\x00\x88\x01\x01\x12\x17\n\nmax_nights\x18\x04 \x01(\x03H\x01\x88\x01\x01B\r\n\x0b_min_nightsB\r\n\x0b_max_nights"A\n\x19HotelCheckInDateRangeInfo\x12\x12\n\nstart_date\x18\x01 \x01(\t\x12\x10\n\x08end_date\x18\x02 \x01(\t"c\n\x13HotelCheckInDayInfo\x12L\n\x0bday_of_week\x18\x01 \x01(\x0e27.google.ads.googleads.v21.enums.DayOfWeekEnum.DayOfWeek".\n\x0eActivityIdInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"2\n\x12ActivityRatingInfo\x12\x12\n\x05value\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x08\n\x06_value"3\n\x13ActivityCountryInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"1\n\x11ActivityStateInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"0\n\x10ActivityCityInfo\x12\x12\n\x05value\x18\x01 \x01(\tH\x00\x88\x01\x01B\x08\n\x06_value"h\n\x13InteractionTypeInfo\x12Q\n\x04type\x18\x01 \x01(\x0e2C.google.ads.googleads.v21.enums.InteractionTypeEnum.InteractionType"\xd2\x02\n\x0eAdScheduleInfo\x12S\n\x0cstart_minute\x18\x01 \x01(\x0e2=.google.ads.googleads.v21.enums.MinuteOfHourEnum.MinuteOfHour\x12Q\n\nend_minute\x18\x02 \x01(\x0e2=.google.ads.googleads.v21.enums.MinuteOfHourEnum.MinuteOfHour\x12\x17\n\nstart_hour\x18\x06 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08end_hour\x18\x07 \x01(\x05H\x01\x88\x01\x01\x12L\n\x0bday_of_week\x18\x05 \x01(\x0e27.google.ads.googleads.v21.enums.DayOfWeekEnum.DayOfWeekB\r\n\x0b_start_hourB\x0b\n\t_end_hour"[\n\x0cAgeRangeInfo\x12K\n\x04type\x18\x01 \x01(\x0e2=.google.ads.googleads.v21.enums.AgeRangeTypeEnum.AgeRangeType"U\n\nGenderInfo\x12G\n\x04type\x18\x01 \x01(\x0e29.google.ads.googleads.v21.enums.GenderTypeEnum.GenderType"d\n\x0fIncomeRangeInfo\x12Q\n\x04type\x18\x01 \x01(\x0e2C.google.ads.googleads.v21.enums.IncomeRangeTypeEnum.IncomeRangeType"m\n\x12ParentalStatusInfo\x12W\n\x04type\x18\x01 \x01(\x0e2I.google.ads.googleads.v21.enums.ParentalStatusTypeEnum.ParentalStatusType"6\n\x10YouTubeVideoInfo\x12\x15\n\x08video_id\x18\x02 \x01(\tH\x00\x88\x01\x01B\x0b\n\t_video_id"<\n\x12YouTubeChannelInfo\x12\x17\n\nchannel_id\x18\x02 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_channel_id"4\n\x0cUserListInfo\x12\x16\n\tuser_list\x18\x02 \x01(\tH\x00\x88\x01\x01B\x0c\n\n_user_list"\x95\x02\n\rProximityInfo\x12@\n\tgeo_point\x18\x01 \x01(\x0b2-.google.ads.googleads.v21.common.GeoPointInfo\x12\x13\n\x06radius\x18\x05 \x01(\x01H\x00\x88\x01\x01\x12c\n\x0cradius_units\x18\x03 \x01(\x0e2M.google.ads.googleads.v21.enums.ProximityRadiusUnitsEnum.ProximityRadiusUnits\x12=\n\x07address\x18\x04 \x01(\x0b2,.google.ads.googleads.v21.common.AddressInfoB\t\n\x07_radius"\x9c\x01\n\x0cGeoPointInfo\x12\'\n\x1alongitude_in_micro_degrees\x18\x03 \x01(\x05H\x00\x88\x01\x01\x12&\n\x19latitude_in_micro_degrees\x18\x04 \x01(\x05H\x01\x88\x01\x01B\x1d\n\x1b_longitude_in_micro_degreesB\x1c\n\x1a_latitude_in_micro_degrees"\xc7\x02\n\x0bAddressInfo\x12\x18\n\x0bpostal_code\x18\x08 \x01(\tH\x00\x88\x01\x01\x12\x1a\n\rprovince_code\x18\t \x01(\tH\x01\x88\x01\x01\x12\x19\n\x0ccountry_code\x18\n \x01(\tH\x02\x88\x01\x01\x12\x1a\n\rprovince_name\x18\x0b \x01(\tH\x03\x88\x01\x01\x12\x1b\n\x0estreet_address\x18\x0c \x01(\tH\x04\x88\x01\x01\x12\x1c\n\x0fstreet_address2\x18\r \x01(\tH\x05\x88\x01\x01\x12\x16\n\tcity_name\x18\x0e \x01(\tH\x06\x88\x01\x01B\x0e\n\x0c_postal_codeB\x10\n\x0e_province_codeB\x0f\n\r_country_codeB\x10\n\x0e_province_nameB\x11\n\x0f_street_addressB\x12\n\x10_street_address2B\x0c\n\n_city_name"v\n\tTopicInfo\x12H\n\x0etopic_constant\x18\x03 \x01(\tB+\xfaA(\n&googleads.googleapis.com/TopicConstantH\x00\x88\x01\x01\x12\x0c\n\x04path\x18\x04 \x03(\tB\x11\n\x0f_topic_constant"D\n\x0cLanguageInfo\x12\x1e\n\x11language_constant\x18\x02 \x01(\tH\x00\x88\x01\x01B\x14\n\x12_language_constant"5\n\x0bIpBlockInfo\x12\x17\n\nip_address\x18\x02 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_ip_address"g\n\x10ContentLabelInfo\x12S\n\x04type\x18\x01 \x01(\x0e2E.google.ads.googleads.v21.enums.ContentLabelTypeEnum.ContentLabelType"p\n\x0bCarrierInfo\x12L\n\x10carrier_constant\x18\x02 \x01(\tB-\xfaA*\n(googleads.googleapis.com/CarrierConstantH\x00\x88\x01\x01B\x13\n\x11_carrier_constant"R\n\x10UserInterestInfo\x12#\n\x16user_interest_category\x18\x02 \x01(\tH\x00\x88\x01\x01B\x19\n\x17_user_interest_category"\xe9\x01\n\x0bWebpageInfo\x12\x1b\n\x0ecriterion_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12I\n\nconditions\x18\x02 \x03(\x0b25.google.ads.googleads.v21.common.WebpageConditionInfo\x12\x1b\n\x13coverage_percentage\x18\x04 \x01(\x01\x12B\n\x06sample\x18\x05 \x01(\x0b22.google.ads.googleads.v21.common.WebpageSampleInfoB\x11\n\x0f_criterion_name"\x89\x02\n\x14WebpageConditionInfo\x12d\n\x07operand\x18\x01 \x01(\x0e2S.google.ads.googleads.v21.enums.WebpageConditionOperandEnum.WebpageConditionOperand\x12g\n\x08operator\x18\x02 \x01(\x0e2U.google.ads.googleads.v21.enums.WebpageConditionOperatorEnum.WebpageConditionOperator\x12\x15\n\x08argument\x18\x04 \x01(\tH\x00\x88\x01\x01B\x0b\n\t_argument"9\n\x0fWebpageListInfo\x12\x17\n\nshared_set\x18\x01 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_shared_set"(\n\x11WebpageSampleInfo\x12\x13\n\x0bsample_urls\x18\x01 \x03(\t"\xb0\x01\n\x1aOperatingSystemVersionInfo\x12l\n!operating_system_version_constant\x18\x02 \x01(\tB<\xfaA9\n7googleads.googleapis.com/OperatingSystemVersionConstantH\x00\x88\x01\x01B$\n"_operating_system_version_constant"p\n\x13AppPaymentModelInfo\x12Y\n\x04type\x18\x01 \x01(\x0e2K.google.ads.googleads.v21.enums.AppPaymentModelTypeEnum.AppPaymentModelType"\x86\x01\n\x10MobileDeviceInfo\x12W\n\x16mobile_device_constant\x18\x02 \x01(\tB2\xfaA/\n-googleads.googleapis.com/MobileDeviceConstantH\x00\x88\x01\x01B\x19\n\x17_mobile_device_constant"F\n\x12CustomAffinityInfo\x12\x1c\n\x0fcustom_affinity\x18\x02 \x01(\tH\x00\x88\x01\x01B\x12\n\x10_custom_affinity"@\n\x10CustomIntentInfo\x12\x1a\n\rcustom_intent\x18\x02 \x01(\tH\x00\x88\x01\x01B\x10\n\x0e_custom_intent"\xdd\x02\n\x11LocationGroupInfo\x12\x1c\n\x14geo_target_constants\x18\x06 \x03(\t\x12\x13\n\x06radius\x18\x07 \x01(\x03H\x00\x88\x01\x01\x12k\n\x0cradius_units\x18\x04 \x01(\x0e2U.google.ads.googleads.v21.enums.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits\x12\x16\n\x0efeed_item_sets\x18\x08 \x03(\t\x125\n(enable_customer_level_location_asset_set\x18\t \x01(\x08H\x01\x88\x01\x01\x12!\n\x19location_group_asset_sets\x18\n \x03(\tB\t\n\x07_radiusB+\n)_enable_customer_level_location_asset_set"-\n\x12CustomAudienceInfo\x12\x17\n\x0fcustom_audience\x18\x01 \x01(\t"a\n\x14CombinedAudienceInfo\x12I\n\x11combined_audience\x18\x01 \x01(\tB.\xfaA+\n)googleads.googleapis.com/CombinedAudience" \n\x0cAudienceInfo\x12\x10\n\x08audience\x18\x01 \x01(\t"\x9c\x01\n\x10KeywordThemeInfo\x12T\n\x16keyword_theme_constant\x18\x01 \x01(\tB2\xfaA/\n-googleads.googleapis.com/KeywordThemeConstantH\x00\x12!\n\x17free_form_keyword_theme\x18\x02 \x01(\tH\x00B\x0f\n\rkeyword_theme"(\n\x12LocalServiceIdInfo\x12\x12\n\nservice_id\x18\x01 \x01(\t"\x1f\n\x0fSearchThemeInfo\x12\x0c\n\x04text\x18\x01 \x01(\t"\x87\x03\n\tBrandInfo\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x16\n\tentity_id\x18\x01 \x01(\tH\x01\x88\x01\x01\x12\x1d\n\x0bprimary_url\x18\x03 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\x7f\n\x10rejection_reason\x18\x04 \x01(\x0e2[.google.ads.googleads.v21.enums.BrandRequestRejectionReasonEnum.BrandRequestRejectionReasonB\x03\xe0A\x03H\x03\x88\x01\x01\x12S\n\x06status\x18\x05 \x01(\x0e29.google.ads.googleads.v21.enums.BrandStateEnum.BrandStateB\x03\xe0A\x03H\x04\x88\x01\x01B\x0f\n\r_display_nameB\x0c\n\n_entity_idB\x0e\n\x0c_primary_urlB\x13\n\x11_rejection_reasonB\t\n\x07_status"7\n\rBrandListInfo\x12\x17\n\nshared_set\x18\x01 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_shared_set"=\n\rLifeEventInfo\x12\x1a\n\rlife_event_id\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x10\n\x0e_life_event_id"[\n\x17ExtendedDemographicInfo\x12$\n\x17extended_demographic_id\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x1a\n\x18_extended_demographic_id"C\n\x0fVideoLineupInfo\x12\x1c\n\x0fvideo_lineup_id\x18\x01 \x01(\x03H\x00\x88\x01\x01B\x12\n\x10_video_lineup_id";\n\x11PlacementListInfo\x12\x17\n\nshared_set\x18\x01 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_shared_setB\xed\x01\n#com.google.ads.googleads.v21.commonB\rCriteriaProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.common.criteria_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v21.commonB\rCriteriaProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v21/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V21.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V21\\Common\xea\x02#Google::Ads::GoogleAds::V21::Common'
    _globals['_MOBILEAPPCATEGORYINFO'].fields_by_name['mobile_app_category_constant']._loaded_options = None
    _globals['_MOBILEAPPCATEGORYINFO'].fields_by_name['mobile_app_category_constant']._serialized_options = b'\xfaA4\n2googleads.googleapis.com/MobileAppCategoryConstant'
    _globals['_TOPICINFO'].fields_by_name['topic_constant']._loaded_options = None
    _globals['_TOPICINFO'].fields_by_name['topic_constant']._serialized_options = b'\xfaA(\n&googleads.googleapis.com/TopicConstant'
    _globals['_CARRIERINFO'].fields_by_name['carrier_constant']._loaded_options = None
    _globals['_CARRIERINFO'].fields_by_name['carrier_constant']._serialized_options = b'\xfaA*\n(googleads.googleapis.com/CarrierConstant'
    _globals['_OPERATINGSYSTEMVERSIONINFO'].fields_by_name['operating_system_version_constant']._loaded_options = None
    _globals['_OPERATINGSYSTEMVERSIONINFO'].fields_by_name['operating_system_version_constant']._serialized_options = b'\xfaA9\n7googleads.googleapis.com/OperatingSystemVersionConstant'
    _globals['_MOBILEDEVICEINFO'].fields_by_name['mobile_device_constant']._loaded_options = None
    _globals['_MOBILEDEVICEINFO'].fields_by_name['mobile_device_constant']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/MobileDeviceConstant'
    _globals['_COMBINEDAUDIENCEINFO'].fields_by_name['combined_audience']._loaded_options = None
    _globals['_COMBINEDAUDIENCEINFO'].fields_by_name['combined_audience']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/CombinedAudience'
    _globals['_KEYWORDTHEMEINFO'].fields_by_name['keyword_theme_constant']._loaded_options = None
    _globals['_KEYWORDTHEMEINFO'].fields_by_name['keyword_theme_constant']._serialized_options = b'\xfaA/\n-googleads.googleapis.com/KeywordThemeConstant'
    _globals['_BRANDINFO'].fields_by_name['display_name']._loaded_options = None
    _globals['_BRANDINFO'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_BRANDINFO'].fields_by_name['primary_url']._loaded_options = None
    _globals['_BRANDINFO'].fields_by_name['primary_url']._serialized_options = b'\xe0A\x03'
    _globals['_BRANDINFO'].fields_by_name['rejection_reason']._loaded_options = None
    _globals['_BRANDINFO'].fields_by_name['rejection_reason']._serialized_options = b'\xe0A\x03'
    _globals['_BRANDINFO'].fields_by_name['status']._loaded_options = None
    _globals['_BRANDINFO'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_KEYWORDINFO']._serialized_start = 1599
    _globals['_KEYWORDINFO']._serialized_end = 1731
    _globals['_PLACEMENTINFO']._serialized_start = 1733
    _globals['_PLACEMENTINFO']._serialized_end = 1774
    _globals['_NEGATIVEKEYWORDLISTINFO']._serialized_start = 1776
    _globals['_NEGATIVEKEYWORDLISTINFO']._serialized_end = 1841
    _globals['_MOBILEAPPCATEGORYINFO']._serialized_start = 1844
    _globals['_MOBILEAPPCATEGORYINFO']._serialized_end = 2000
    _globals['_MOBILEAPPLICATIONINFO']._serialized_start = 2002
    _globals['_MOBILEAPPLICATIONINFO']._serialized_end = 2085
    _globals['_LOCATIONINFO']._serialized_start = 2087
    _globals['_LOCATIONINFO']._serialized_end = 2159
    _globals['_DEVICEINFO']._serialized_start = 2161
    _globals['_DEVICEINFO']._serialized_end = 2238
    _globals['_LISTINGGROUPINFO']._serialized_start = 2241
    _globals['_LISTINGGROUPINFO']._serialized_end = 2572
    _globals['_LISTINGDIMENSIONPATH']._serialized_start = 2574
    _globals['_LISTINGDIMENSIONPATH']._serialized_end = 2671
    _globals['_LISTINGSCOPEINFO']._serialized_start = 2673
    _globals['_LISTINGSCOPEINFO']._serialized_end = 2766
    _globals['_LISTINGDIMENSIONINFO']._serialized_start = 2769
    _globals['_LISTINGDIMENSIONINFO']._serialized_end = 4675
    _globals['_HOTELIDINFO']._serialized_start = 4677
    _globals['_HOTELIDINFO']._serialized_end = 4720
    _globals['_HOTELCLASSINFO']._serialized_start = 4722
    _globals['_HOTELCLASSINFO']._serialized_end = 4768
    _globals['_HOTELCOUNTRYREGIONINFO']._serialized_start = 4770
    _globals['_HOTELCOUNTRYREGIONINFO']._serialized_end = 4862
    _globals['_HOTELSTATEINFO']._serialized_start = 4864
    _globals['_HOTELSTATEINFO']._serialized_end = 4930
    _globals['_HOTELCITYINFO']._serialized_start = 4932
    _globals['_HOTELCITYINFO']._serialized_end = 4995
    _globals['_PRODUCTCATEGORYINFO']._serialized_start = 4998
    _globals['_PRODUCTCATEGORYINFO']._serialized_end = 5155
    _globals['_PRODUCTBRANDINFO']._serialized_start = 5157
    _globals['_PRODUCTBRANDINFO']._serialized_end = 5205
    _globals['_PRODUCTCHANNELINFO']._serialized_start = 5207
    _globals['_PRODUCTCHANNELINFO']._serialized_end = 5311
    _globals['_PRODUCTCHANNELEXCLUSIVITYINFO']._serialized_start = 5314
    _globals['_PRODUCTCHANNELEXCLUSIVITYINFO']._serialized_end = 5463
    _globals['_PRODUCTCONDITIONINFO']._serialized_start = 5465
    _globals['_PRODUCTCONDITIONINFO']._serialized_end = 5577
    _globals['_PRODUCTCUSTOMATTRIBUTEINFO']._serialized_start = 5580
    _globals['_PRODUCTCUSTOMATTRIBUTEINFO']._serialized_end = 5746
    _globals['_PRODUCTITEMIDINFO']._serialized_start = 5748
    _globals['_PRODUCTITEMIDINFO']._serialized_end = 5797
    _globals['_PRODUCTTYPEINFO']._serialized_start = 5800
    _globals['_PRODUCTTYPEINFO']._serialized_end = 5933
    _globals['_PRODUCTGROUPINGINFO']._serialized_start = 5935
    _globals['_PRODUCTGROUPINGINFO']._serialized_end = 5986
    _globals['_PRODUCTLABELSINFO']._serialized_start = 5988
    _globals['_PRODUCTLABELSINFO']._serialized_end = 6037
    _globals['_PRODUCTLEGACYCONDITIONINFO']._serialized_start = 6039
    _globals['_PRODUCTLEGACYCONDITIONINFO']._serialized_end = 6097
    _globals['_PRODUCTTYPEFULLINFO']._serialized_start = 6099
    _globals['_PRODUCTTYPEFULLINFO']._serialized_end = 6150
    _globals['_UNKNOWNLISTINGDIMENSIONINFO']._serialized_start = 6152
    _globals['_UNKNOWNLISTINGDIMENSIONINFO']._serialized_end = 6181
    _globals['_HOTELDATESELECTIONTYPEINFO']._serialized_start = 6183
    _globals['_HOTELDATESELECTIONTYPEINFO']._serialized_end = 6308
    _globals['_HOTELADVANCEBOOKINGWINDOWINFO']._serialized_start = 6310
    _globals['_HOTELADVANCEBOOKINGWINDOWINFO']._serialized_end = 6413
    _globals['_HOTELLENGTHOFSTAYINFO']._serialized_start = 6415
    _globals['_HOTELLENGTHOFSTAYINFO']._serialized_end = 6518
    _globals['_HOTELCHECKINDATERANGEINFO']._serialized_start = 6520
    _globals['_HOTELCHECKINDATERANGEINFO']._serialized_end = 6585
    _globals['_HOTELCHECKINDAYINFO']._serialized_start = 6587
    _globals['_HOTELCHECKINDAYINFO']._serialized_end = 6686
    _globals['_ACTIVITYIDINFO']._serialized_start = 6688
    _globals['_ACTIVITYIDINFO']._serialized_end = 6734
    _globals['_ACTIVITYRATINGINFO']._serialized_start = 6736
    _globals['_ACTIVITYRATINGINFO']._serialized_end = 6786
    _globals['_ACTIVITYCOUNTRYINFO']._serialized_start = 6788
    _globals['_ACTIVITYCOUNTRYINFO']._serialized_end = 6839
    _globals['_ACTIVITYSTATEINFO']._serialized_start = 6841
    _globals['_ACTIVITYSTATEINFO']._serialized_end = 6890
    _globals['_ACTIVITYCITYINFO']._serialized_start = 6892
    _globals['_ACTIVITYCITYINFO']._serialized_end = 6940
    _globals['_INTERACTIONTYPEINFO']._serialized_start = 6942
    _globals['_INTERACTIONTYPEINFO']._serialized_end = 7046
    _globals['_ADSCHEDULEINFO']._serialized_start = 7049
    _globals['_ADSCHEDULEINFO']._serialized_end = 7387
    _globals['_AGERANGEINFO']._serialized_start = 7389
    _globals['_AGERANGEINFO']._serialized_end = 7480
    _globals['_GENDERINFO']._serialized_start = 7482
    _globals['_GENDERINFO']._serialized_end = 7567
    _globals['_INCOMERANGEINFO']._serialized_start = 7569
    _globals['_INCOMERANGEINFO']._serialized_end = 7669
    _globals['_PARENTALSTATUSINFO']._serialized_start = 7671
    _globals['_PARENTALSTATUSINFO']._serialized_end = 7780
    _globals['_YOUTUBEVIDEOINFO']._serialized_start = 7782
    _globals['_YOUTUBEVIDEOINFO']._serialized_end = 7836
    _globals['_YOUTUBECHANNELINFO']._serialized_start = 7838
    _globals['_YOUTUBECHANNELINFO']._serialized_end = 7898
    _globals['_USERLISTINFO']._serialized_start = 7900
    _globals['_USERLISTINFO']._serialized_end = 7952
    _globals['_PROXIMITYINFO']._serialized_start = 7955
    _globals['_PROXIMITYINFO']._serialized_end = 8232
    _globals['_GEOPOINTINFO']._serialized_start = 8235
    _globals['_GEOPOINTINFO']._serialized_end = 8391
    _globals['_ADDRESSINFO']._serialized_start = 8394
    _globals['_ADDRESSINFO']._serialized_end = 8721
    _globals['_TOPICINFO']._serialized_start = 8723
    _globals['_TOPICINFO']._serialized_end = 8841
    _globals['_LANGUAGEINFO']._serialized_start = 8843
    _globals['_LANGUAGEINFO']._serialized_end = 8911
    _globals['_IPBLOCKINFO']._serialized_start = 8913
    _globals['_IPBLOCKINFO']._serialized_end = 8966
    _globals['_CONTENTLABELINFO']._serialized_start = 8968
    _globals['_CONTENTLABELINFO']._serialized_end = 9071
    _globals['_CARRIERINFO']._serialized_start = 9073
    _globals['_CARRIERINFO']._serialized_end = 9185
    _globals['_USERINTERESTINFO']._serialized_start = 9187
    _globals['_USERINTERESTINFO']._serialized_end = 9269
    _globals['_WEBPAGEINFO']._serialized_start = 9272
    _globals['_WEBPAGEINFO']._serialized_end = 9505
    _globals['_WEBPAGECONDITIONINFO']._serialized_start = 9508
    _globals['_WEBPAGECONDITIONINFO']._serialized_end = 9773
    _globals['_WEBPAGELISTINFO']._serialized_start = 9775
    _globals['_WEBPAGELISTINFO']._serialized_end = 9832
    _globals['_WEBPAGESAMPLEINFO']._serialized_start = 9834
    _globals['_WEBPAGESAMPLEINFO']._serialized_end = 9874
    _globals['_OPERATINGSYSTEMVERSIONINFO']._serialized_start = 9877
    _globals['_OPERATINGSYSTEMVERSIONINFO']._serialized_end = 10053
    _globals['_APPPAYMENTMODELINFO']._serialized_start = 10055
    _globals['_APPPAYMENTMODELINFO']._serialized_end = 10167
    _globals['_MOBILEDEVICEINFO']._serialized_start = 10170
    _globals['_MOBILEDEVICEINFO']._serialized_end = 10304
    _globals['_CUSTOMAFFINITYINFO']._serialized_start = 10306
    _globals['_CUSTOMAFFINITYINFO']._serialized_end = 10376
    _globals['_CUSTOMINTENTINFO']._serialized_start = 10378
    _globals['_CUSTOMINTENTINFO']._serialized_end = 10442
    _globals['_LOCATIONGROUPINFO']._serialized_start = 10445
    _globals['_LOCATIONGROUPINFO']._serialized_end = 10794
    _globals['_CUSTOMAUDIENCEINFO']._serialized_start = 10796
    _globals['_CUSTOMAUDIENCEINFO']._serialized_end = 10841
    _globals['_COMBINEDAUDIENCEINFO']._serialized_start = 10843
    _globals['_COMBINEDAUDIENCEINFO']._serialized_end = 10940
    _globals['_AUDIENCEINFO']._serialized_start = 10942
    _globals['_AUDIENCEINFO']._serialized_end = 10974
    _globals['_KEYWORDTHEMEINFO']._serialized_start = 10977
    _globals['_KEYWORDTHEMEINFO']._serialized_end = 11133
    _globals['_LOCALSERVICEIDINFO']._serialized_start = 11135
    _globals['_LOCALSERVICEIDINFO']._serialized_end = 11175
    _globals['_SEARCHTHEMEINFO']._serialized_start = 11177
    _globals['_SEARCHTHEMEINFO']._serialized_end = 11208
    _globals['_BRANDINFO']._serialized_start = 11211
    _globals['_BRANDINFO']._serialized_end = 11602
    _globals['_BRANDLISTINFO']._serialized_start = 11604
    _globals['_BRANDLISTINFO']._serialized_end = 11659
    _globals['_LIFEEVENTINFO']._serialized_start = 11661
    _globals['_LIFEEVENTINFO']._serialized_end = 11722
    _globals['_EXTENDEDDEMOGRAPHICINFO']._serialized_start = 11724
    _globals['_EXTENDEDDEMOGRAPHICINFO']._serialized_end = 11815
    _globals['_VIDEOLINEUPINFO']._serialized_start = 11817
    _globals['_VIDEOLINEUPINFO']._serialized_end = 11884
    _globals['_PLACEMENTLISTINFO']._serialized_start = 11886
    _globals['_PLACEMENTLISTINFO']._serialized_end = 11945