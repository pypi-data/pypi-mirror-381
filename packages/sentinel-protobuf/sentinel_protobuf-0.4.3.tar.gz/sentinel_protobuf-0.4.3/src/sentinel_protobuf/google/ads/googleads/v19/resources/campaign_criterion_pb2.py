"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/campaign_criterion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v19.enums import campaign_criterion_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_campaign__criterion__status__pb2
from ......google.ads.googleads.v19.enums import criterion_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_criterion__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v19/resources/campaign_criterion.proto\x12"google.ads.googleads.v19.resources\x1a.google/ads/googleads/v19/common/criteria.proto\x1a>google/ads/googleads/v19/enums/campaign_criterion_status.proto\x1a3google/ads/googleads/v19/enums/criterion_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe5\x18\n\x11CampaignCriterion\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x05\xfaA,\n*googleads.googleapis.com/CampaignCriterion\x12@\n\x08campaign\x18% \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18& \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18+ \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cbid_modifier\x18\' \x01(\x02H\x03\x88\x01\x01\x12\x1a\n\x08negative\x18( \x01(\x08B\x03\xe0A\x05H\x04\x88\x01\x01\x12R\n\x04type\x18\x06 \x01(\x0e2?.google.ads.googleads.v19.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0A\x03\x12c\n\x06status\x18# \x01(\x0e2S.google.ads.googleads.v19.enums.CampaignCriterionStatusEnum.CampaignCriterionStatus\x12D\n\x07keyword\x18\x08 \x01(\x0b2,.google.ads.googleads.v19.common.KeywordInfoB\x03\xe0A\x05H\x00\x12H\n\tplacement\x18\t \x01(\x0b2..google.ads.googleads.v19.common.PlacementInfoB\x03\xe0A\x05H\x00\x12Z\n\x13mobile_app_category\x18\n \x01(\x0b26.google.ads.googleads.v19.common.MobileAppCategoryInfoB\x03\xe0A\x05H\x00\x12Y\n\x12mobile_application\x18\x0b \x01(\x0b26.google.ads.googleads.v19.common.MobileApplicationInfoB\x03\xe0A\x05H\x00\x12F\n\x08location\x18\x0c \x01(\x0b2-.google.ads.googleads.v19.common.LocationInfoB\x03\xe0A\x05H\x00\x12B\n\x06device\x18\r \x01(\x0b2+.google.ads.googleads.v19.common.DeviceInfoB\x03\xe0A\x05H\x00\x12K\n\x0bad_schedule\x18\x0f \x01(\x0b2/.google.ads.googleads.v19.common.AdScheduleInfoB\x03\xe0A\x05H\x00\x12G\n\tage_range\x18\x10 \x01(\x0b2-.google.ads.googleads.v19.common.AgeRangeInfoB\x03\xe0A\x05H\x00\x12B\n\x06gender\x18\x11 \x01(\x0b2+.google.ads.googleads.v19.common.GenderInfoB\x03\xe0A\x05H\x00\x12M\n\x0cincome_range\x18\x12 \x01(\x0b20.google.ads.googleads.v19.common.IncomeRangeInfoB\x03\xe0A\x05H\x00\x12S\n\x0fparental_status\x18\x13 \x01(\x0b23.google.ads.googleads.v19.common.ParentalStatusInfoB\x03\xe0A\x05H\x00\x12G\n\tuser_list\x18\x16 \x01(\x0b2-.google.ads.googleads.v19.common.UserListInfoB\x03\xe0A\x05H\x00\x12O\n\ryoutube_video\x18\x14 \x01(\x0b21.google.ads.googleads.v19.common.YouTubeVideoInfoB\x03\xe0A\x05H\x00\x12S\n\x0fyoutube_channel\x18\x15 \x01(\x0b23.google.ads.googleads.v19.common.YouTubeChannelInfoB\x03\xe0A\x05H\x00\x12H\n\tproximity\x18\x17 \x01(\x0b2..google.ads.googleads.v19.common.ProximityInfoB\x03\xe0A\x05H\x00\x12@\n\x05topic\x18\x18 \x01(\x0b2*.google.ads.googleads.v19.common.TopicInfoB\x03\xe0A\x05H\x00\x12O\n\rlisting_scope\x18\x19 \x01(\x0b21.google.ads.googleads.v19.common.ListingScopeInfoB\x03\xe0A\x05H\x00\x12F\n\x08language\x18\x1a \x01(\x0b2-.google.ads.googleads.v19.common.LanguageInfoB\x03\xe0A\x05H\x00\x12E\n\x08ip_block\x18\x1b \x01(\x0b2,.google.ads.googleads.v19.common.IpBlockInfoB\x03\xe0A\x05H\x00\x12O\n\rcontent_label\x18\x1c \x01(\x0b21.google.ads.googleads.v19.common.ContentLabelInfoB\x03\xe0A\x05H\x00\x12D\n\x07carrier\x18\x1d \x01(\x0b2,.google.ads.googleads.v19.common.CarrierInfoB\x03\xe0A\x05H\x00\x12O\n\ruser_interest\x18\x1e \x01(\x0b21.google.ads.googleads.v19.common.UserInterestInfoB\x03\xe0A\x05H\x00\x12D\n\x07webpage\x18\x1f \x01(\x0b2,.google.ads.googleads.v19.common.WebpageInfoB\x03\xe0A\x05H\x00\x12d\n\x18operating_system_version\x18  \x01(\x0b2;.google.ads.googleads.v19.common.OperatingSystemVersionInfoB\x03\xe0A\x05H\x00\x12O\n\rmobile_device\x18! \x01(\x0b21.google.ads.googleads.v19.common.MobileDeviceInfoB\x03\xe0A\x05H\x00\x12Q\n\x0elocation_group\x18" \x01(\x0b22.google.ads.googleads.v19.common.LocationGroupInfoB\x03\xe0A\x05H\x00\x12S\n\x0fcustom_affinity\x18$ \x01(\x0b23.google.ads.googleads.v19.common.CustomAffinityInfoB\x03\xe0A\x05H\x00\x12S\n\x0fcustom_audience\x18) \x01(\x0b23.google.ads.googleads.v19.common.CustomAudienceInfoB\x03\xe0A\x05H\x00\x12W\n\x11combined_audience\x18* \x01(\x0b25.google.ads.googleads.v19.common.CombinedAudienceInfoB\x03\xe0A\x05H\x00\x12O\n\rkeyword_theme\x18- \x01(\x0b21.google.ads.googleads.v19.common.KeywordThemeInfoB\x03\xe0A\x05H\x00\x12T\n\x10local_service_id\x18. \x01(\x0b23.google.ads.googleads.v19.common.LocalServiceIdInfoB\x03\xe0A\x05H\x00\x12I\n\nbrand_list\x18/ \x01(\x0b2..google.ads.googleads.v19.common.BrandListInfoB\x03\xe0A\x05H\x00:v\xeaAs\n*googleads.googleapis.com/CampaignCriterion\x12Ecustomers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}B\x0b\n\tcriterionB\x0b\n\t_campaignB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x0b\n\t_negativeB\x88\x02\n&com.google.ads.googleads.v19.resourcesB\x16CampaignCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.campaign_criterion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x16CampaignCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA,\n*googleads.googleapis.com/CampaignCriterion'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['negative']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['negative']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['type']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['placement']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['placement']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_app_category']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_app_category']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_application']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_application']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['device']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['device']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['ad_schedule']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['ad_schedule']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['age_range']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['age_range']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['gender']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['gender']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['income_range']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['income_range']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['parental_status']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['parental_status']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_list']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_list']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['youtube_video']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['youtube_video']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['youtube_channel']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['youtube_channel']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['proximity']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['proximity']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['topic']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['topic']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['listing_scope']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['listing_scope']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['language']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['language']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['ip_block']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['ip_block']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['content_label']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['content_label']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['carrier']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['carrier']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_interest']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_interest']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['webpage']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['webpage']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['operating_system_version']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['operating_system_version']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_device']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['mobile_device']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location_group']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location_group']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['custom_affinity']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['custom_affinity']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['custom_audience']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['custom_audience']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['combined_audience']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['combined_audience']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword_theme']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword_theme']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['local_service_id']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['local_service_id']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['brand_list']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['brand_list']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION']._loaded_options = None
    _globals['_CAMPAIGNCRITERION']._serialized_options = b'\xeaAs\n*googleads.googleapis.com/CampaignCriterion\x12Ecustomers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}'
    _globals['_CAMPAIGNCRITERION']._serialized_start = 325
    _globals['_CAMPAIGNCRITERION']._serialized_end = 3498