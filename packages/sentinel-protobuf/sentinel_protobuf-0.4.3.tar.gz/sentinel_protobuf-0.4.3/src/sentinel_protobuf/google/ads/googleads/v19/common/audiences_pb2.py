"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/common/audiences.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import gender_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_gender__type__pb2
from ......google.ads.googleads.v19.enums import income_range_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_income__range__type__pb2
from ......google.ads.googleads.v19.enums import parental_status_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_parental__status__type__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/ads/googleads/v19/common/audiences.proto\x12\x1fgoogle.ads.googleads.v19.common\x1a0google/ads/googleads/v19/enums/gender_type.proto\x1a6google/ads/googleads/v19/enums/income_range_type.proto\x1a9google/ads/googleads/v19/enums/parental_status_type.proto\x1a\x19google/api/resource.proto"\xa6\x03\n\x11AudienceDimension\x12<\n\x03age\x18\x01 \x01(\x0b2-.google.ads.googleads.v19.common.AgeDimensionH\x00\x12B\n\x06gender\x18\x02 \x01(\x0b20.google.ads.googleads.v19.common.GenderDimensionH\x00\x12U\n\x10household_income\x18\x03 \x01(\x0b29.google.ads.googleads.v19.common.HouseholdIncomeDimensionH\x00\x12S\n\x0fparental_status\x18\x04 \x01(\x0b28.google.ads.googleads.v19.common.ParentalStatusDimensionH\x00\x12V\n\x11audience_segments\x18\x05 \x01(\x0b29.google.ads.googleads.v19.common.AudienceSegmentDimensionH\x00B\x0b\n\tdimension"c\n\x1aAudienceExclusionDimension\x12E\n\nexclusions\x18\x01 \x03(\x0b21.google.ads.googleads.v19.common.ExclusionSegment"d\n\x10ExclusionSegment\x12E\n\tuser_list\x18\x01 \x01(\x0b20.google.ads.googleads.v19.common.UserListSegmentH\x00B\t\n\x07segment"\x8b\x01\n\x0cAgeDimension\x12?\n\nage_ranges\x18\x01 \x03(\x0b2+.google.ads.googleads.v19.common.AgeSegment\x12!\n\x14include_undetermined\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_include_undetermined"P\n\nAgeSegment\x12\x14\n\x07min_age\x18\x01 \x01(\x05H\x00\x88\x01\x01\x12\x14\n\x07max_age\x18\x02 \x01(\x05H\x01\x88\x01\x01B\n\n\x08_min_ageB\n\n\x08_max_age"\x99\x01\n\x0fGenderDimension\x12J\n\x07genders\x18\x01 \x03(\x0e29.google.ads.googleads.v19.enums.GenderTypeEnum.GenderType\x12!\n\x14include_undetermined\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_include_undetermined"\xb2\x01\n\x18HouseholdIncomeDimension\x12Z\n\rincome_ranges\x18\x01 \x03(\x0e2C.google.ads.googleads.v19.enums.IncomeRangeTypeEnum.IncomeRangeType\x12!\n\x14include_undetermined\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_include_undetermined"\xbb\x01\n\x17ParentalStatusDimension\x12d\n\x11parental_statuses\x18\x01 \x03(\x0e2I.google.ads.googleads.v19.enums.ParentalStatusTypeEnum.ParentalStatusType\x12!\n\x14include_undetermined\x18\x02 \x01(\x08H\x00\x88\x01\x01B\x17\n\x15_include_undetermined"^\n\x18AudienceSegmentDimension\x12B\n\x08segments\x18\x01 \x03(\x0b20.google.ads.googleads.v19.common.AudienceSegment"\xab\x03\n\x0fAudienceSegment\x12E\n\tuser_list\x18\x01 \x01(\x0b20.google.ads.googleads.v19.common.UserListSegmentH\x00\x12M\n\ruser_interest\x18\x02 \x01(\x0b24.google.ads.googleads.v19.common.UserInterestSegmentH\x00\x12G\n\nlife_event\x18\x03 \x01(\x0b21.google.ads.googleads.v19.common.LifeEventSegmentH\x00\x12[\n\x14detailed_demographic\x18\x04 \x01(\x0b2;.google.ads.googleads.v19.common.DetailedDemographicSegmentH\x00\x12Q\n\x0fcustom_audience\x18\x05 \x01(\x0b26.google.ads.googleads.v19.common.CustomAudienceSegmentH\x00B\t\n\x07segment"7\n\x0fUserListSegment\x12\x16\n\tuser_list\x18\x01 \x01(\tH\x00\x88\x01\x01B\x0c\n\n_user_list"U\n\x13UserInterestSegment\x12#\n\x16user_interest_category\x18\x01 \x01(\tH\x00\x88\x01\x01B\x19\n\x17_user_interest_category"c\n\x10LifeEventSegment\x12@\n\nlife_event\x18\x01 \x01(\tB\'\xfaA$\n"googleads.googleapis.com/LifeEventH\x00\x88\x01\x01B\r\n\x0b_life_event"\x8b\x01\n\x1aDetailedDemographicSegment\x12T\n\x14detailed_demographic\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/DetailedDemographicH\x00\x88\x01\x01B\x17\n\x15_detailed_demographic"I\n\x15CustomAudienceSegment\x12\x1c\n\x0fcustom_audience\x18\x01 \x01(\tH\x00\x88\x01\x01B\x12\n\x10_custom_audienceB\xee\x01\n#com.google.ads.googleads.v19.commonB\x0eAudiencesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Commonb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.common.audiences_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.ads.googleads.v19.commonB\x0eAudiencesProtoP\x01ZEgoogle.golang.org/genproto/googleapis/ads/googleads/v19/common;common\xa2\x02\x03GAA\xaa\x02\x1fGoogle.Ads.GoogleAds.V19.Common\xca\x02\x1fGoogle\\Ads\\GoogleAds\\V19\\Common\xea\x02#Google::Ads::GoogleAds::V19::Common'
    _globals['_LIFEEVENTSEGMENT'].fields_by_name['life_event']._loaded_options = None
    _globals['_LIFEEVENTSEGMENT'].fields_by_name['life_event']._serialized_options = b'\xfaA$\n"googleads.googleapis.com/LifeEvent'
    _globals['_DETAILEDDEMOGRAPHICSEGMENT'].fields_by_name['detailed_demographic']._loaded_options = None
    _globals['_DETAILEDDEMOGRAPHICSEGMENT'].fields_by_name['detailed_demographic']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/DetailedDemographic'
    _globals['_AUDIENCEDIMENSION']._serialized_start = 277
    _globals['_AUDIENCEDIMENSION']._serialized_end = 699
    _globals['_AUDIENCEEXCLUSIONDIMENSION']._serialized_start = 701
    _globals['_AUDIENCEEXCLUSIONDIMENSION']._serialized_end = 800
    _globals['_EXCLUSIONSEGMENT']._serialized_start = 802
    _globals['_EXCLUSIONSEGMENT']._serialized_end = 902
    _globals['_AGEDIMENSION']._serialized_start = 905
    _globals['_AGEDIMENSION']._serialized_end = 1044
    _globals['_AGESEGMENT']._serialized_start = 1046
    _globals['_AGESEGMENT']._serialized_end = 1126
    _globals['_GENDERDIMENSION']._serialized_start = 1129
    _globals['_GENDERDIMENSION']._serialized_end = 1282
    _globals['_HOUSEHOLDINCOMEDIMENSION']._serialized_start = 1285
    _globals['_HOUSEHOLDINCOMEDIMENSION']._serialized_end = 1463
    _globals['_PARENTALSTATUSDIMENSION']._serialized_start = 1466
    _globals['_PARENTALSTATUSDIMENSION']._serialized_end = 1653
    _globals['_AUDIENCESEGMENTDIMENSION']._serialized_start = 1655
    _globals['_AUDIENCESEGMENTDIMENSION']._serialized_end = 1749
    _globals['_AUDIENCESEGMENT']._serialized_start = 1752
    _globals['_AUDIENCESEGMENT']._serialized_end = 2179
    _globals['_USERLISTSEGMENT']._serialized_start = 2181
    _globals['_USERLISTSEGMENT']._serialized_end = 2236
    _globals['_USERINTERESTSEGMENT']._serialized_start = 2238
    _globals['_USERINTERESTSEGMENT']._serialized_end = 2323
    _globals['_LIFEEVENTSEGMENT']._serialized_start = 2325
    _globals['_LIFEEVENTSEGMENT']._serialized_end = 2424
    _globals['_DETAILEDDEMOGRAPHICSEGMENT']._serialized_start = 2427
    _globals['_DETAILEDDEMOGRAPHICSEGMENT']._serialized_end = 2566
    _globals['_CUSTOMAUDIENCESEGMENT']._serialized_start = 2568
    _globals['_CUSTOMAUDIENCESEGMENT']._serialized_end = 2641