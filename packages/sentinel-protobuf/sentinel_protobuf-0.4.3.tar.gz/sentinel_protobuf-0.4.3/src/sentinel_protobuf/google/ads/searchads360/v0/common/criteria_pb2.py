"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/common/criteria.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import age_range_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_age__range__type__pb2
from ......google.ads.searchads360.v0.enums import day_of_week_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_day__of__week__pb2
from ......google.ads.searchads360.v0.enums import device_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_device__pb2
from ......google.ads.searchads360.v0.enums import gender_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_gender__type__pb2
from ......google.ads.searchads360.v0.enums import keyword_match_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_keyword__match__type__pb2
from ......google.ads.searchads360.v0.enums import listing_group_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_listing__group__type__pb2
from ......google.ads.searchads360.v0.enums import location_group_radius_units_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_location__group__radius__units__pb2
from ......google.ads.searchads360.v0.enums import minute_of_hour_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_minute__of__hour__pb2
from ......google.ads.searchads360.v0.enums import webpage_condition_operand_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_webpage__condition__operand__pb2
from ......google.ads.searchads360.v0.enums import webpage_condition_operator_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_webpage__condition__operator__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/ads/searchads360/v0/common/criteria.proto\x12!google.ads.searchads360.v0.common\x1a5google/ads/searchads360/v0/enums/age_range_type.proto\x1a2google/ads/searchads360/v0/enums/day_of_week.proto\x1a-google/ads/searchads360/v0/enums/device.proto\x1a2google/ads/searchads360/v0/enums/gender_type.proto\x1a9google/ads/searchads360/v0/enums/keyword_match_type.proto\x1a9google/ads/searchads360/v0/enums/listing_group_type.proto\x1aBgoogle/ads/searchads360/v0/enums/location_group_radius_units.proto\x1a5google/ads/searchads360/v0/enums/minute_of_hour.proto\x1a@google/ads/searchads360/v0/enums/webpage_condition_operand.proto\x1aAgoogle/ads/searchads360/v0/enums/webpage_condition_operator.proto"\x86\x01\n\x0bKeywordInfo\x12\x11\n\x04text\x18\x03 \x01(\tH\x00\x88\x01\x01\x12[\n\nmatch_type\x18\x02 \x01(\x0e2G.google.ads.searchads360.v0.enums.KeywordMatchTypeEnum.KeywordMatchTypeB\x07\n\x05_text"H\n\x0cLocationInfo\x12 \n\x13geo_target_constant\x18\x02 \x01(\tH\x00\x88\x01\x01B\x16\n\x14_geo_target_constant"O\n\nDeviceInfo\x12A\n\x04type\x18\x01 \x01(\x0e23.google.ads.searchads360.v0.enums.DeviceEnum.Device"i\n\x10ListingGroupInfo\x12U\n\x04type\x18\x01 \x01(\x0e2G.google.ads.searchads360.v0.enums.ListingGroupTypeEnum.ListingGroupType"\xd8\x02\n\x0eAdScheduleInfo\x12U\n\x0cstart_minute\x18\x01 \x01(\x0e2?.google.ads.searchads360.v0.enums.MinuteOfHourEnum.MinuteOfHour\x12S\n\nend_minute\x18\x02 \x01(\x0e2?.google.ads.searchads360.v0.enums.MinuteOfHourEnum.MinuteOfHour\x12\x17\n\nstart_hour\x18\x06 \x01(\x05H\x00\x88\x01\x01\x12\x15\n\x08end_hour\x18\x07 \x01(\x05H\x01\x88\x01\x01\x12N\n\x0bday_of_week\x18\x05 \x01(\x0e29.google.ads.searchads360.v0.enums.DayOfWeekEnum.DayOfWeekB\r\n\x0b_start_hourB\x0b\n\t_end_hour"]\n\x0cAgeRangeInfo\x12M\n\x04type\x18\x01 \x01(\x0e2?.google.ads.searchads360.v0.enums.AgeRangeTypeEnum.AgeRangeType"W\n\nGenderInfo\x12I\n\x04type\x18\x01 \x01(\x0e2;.google.ads.searchads360.v0.enums.GenderTypeEnum.GenderType"4\n\x0cUserListInfo\x12\x16\n\tuser_list\x18\x02 \x01(\tH\x00\x88\x01\x01B\x0c\n\n_user_list"D\n\x0cLanguageInfo\x12\x1e\n\x11language_constant\x18\x02 \x01(\tH\x00\x88\x01\x01B\x14\n\x12_language_constant"\xa7\x01\n\x0bWebpageInfo\x12\x1b\n\x0ecriterion_name\x18\x03 \x01(\tH\x00\x88\x01\x01\x12K\n\nconditions\x18\x02 \x03(\x0b27.google.ads.searchads360.v0.common.WebpageConditionInfo\x12\x1b\n\x13coverage_percentage\x18\x04 \x01(\x01B\x11\n\x0f_criterion_name"\x8d\x02\n\x14WebpageConditionInfo\x12f\n\x07operand\x18\x01 \x01(\x0e2U.google.ads.searchads360.v0.enums.WebpageConditionOperandEnum.WebpageConditionOperand\x12i\n\x08operator\x18\x02 \x01(\x0e2W.google.ads.searchads360.v0.enums.WebpageConditionOperatorEnum.WebpageConditionOperator\x12\x15\n\x08argument\x18\x04 \x01(\tH\x00\x88\x01\x01B\x0b\n\t_argument"\xd8\x01\n\x11LocationGroupInfo\x12\x1c\n\x14geo_target_constants\x18\x06 \x03(\t\x12\x13\n\x06radius\x18\x07 \x01(\x03H\x00\x88\x01\x01\x12m\n\x0cradius_units\x18\x04 \x01(\x0e2W.google.ads.searchads360.v0.enums.LocationGroupRadiusUnitsEnum.LocationGroupRadiusUnits\x12\x16\n\x0efeed_item_sets\x18\x08 \x03(\tB\t\n\x07_radius" \n\x0cAudienceInfo\x12\x10\n\x08audience\x18\x01 \x01(\tB\xfb\x01\n%com.google.ads.searchads360.v0.commonB\rCriteriaProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.common.criteria_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.searchads360.v0.commonB\rCriteriaProtoP\x01ZGgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/common;common\xa2\x02\x07GASA360\xaa\x02!Google.Ads.SearchAds360.V0.Common\xca\x02!Google\\Ads\\SearchAds360\\V0\\Common\xea\x02%Google::Ads::SearchAds360::V0::Common'
    _globals['_KEYWORDINFO']._serialized_start = 668
    _globals['_KEYWORDINFO']._serialized_end = 802
    _globals['_LOCATIONINFO']._serialized_start = 804
    _globals['_LOCATIONINFO']._serialized_end = 876
    _globals['_DEVICEINFO']._serialized_start = 878
    _globals['_DEVICEINFO']._serialized_end = 957
    _globals['_LISTINGGROUPINFO']._serialized_start = 959
    _globals['_LISTINGGROUPINFO']._serialized_end = 1064
    _globals['_ADSCHEDULEINFO']._serialized_start = 1067
    _globals['_ADSCHEDULEINFO']._serialized_end = 1411
    _globals['_AGERANGEINFO']._serialized_start = 1413
    _globals['_AGERANGEINFO']._serialized_end = 1506
    _globals['_GENDERINFO']._serialized_start = 1508
    _globals['_GENDERINFO']._serialized_end = 1595
    _globals['_USERLISTINFO']._serialized_start = 1597
    _globals['_USERLISTINFO']._serialized_end = 1649
    _globals['_LANGUAGEINFO']._serialized_start = 1651
    _globals['_LANGUAGEINFO']._serialized_end = 1719
    _globals['_WEBPAGEINFO']._serialized_start = 1722
    _globals['_WEBPAGEINFO']._serialized_end = 1889
    _globals['_WEBPAGECONDITIONINFO']._serialized_start = 1892
    _globals['_WEBPAGECONDITIONINFO']._serialized_end = 2161
    _globals['_LOCATIONGROUPINFO']._serialized_start = 2164
    _globals['_LOCATIONGROUPINFO']._serialized_end = 2380
    _globals['_AUDIENCEINFO']._serialized_start = 2382
    _globals['_AUDIENCEINFO']._serialized_end = 2414