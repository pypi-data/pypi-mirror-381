"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/ad_group_criterion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_criteria__pb2
from ......google.ads.googleads.v21.common import custom_parameter_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_custom__parameter__pb2
from ......google.ads.googleads.v21.enums import ad_group_criterion_approval_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_ad__group__criterion__approval__status__pb2
from ......google.ads.googleads.v21.enums import ad_group_criterion_primary_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_ad__group__criterion__primary__status__pb2
from ......google.ads.googleads.v21.enums import ad_group_criterion_primary_status_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_ad__group__criterion__primary__status__reason__pb2
from ......google.ads.googleads.v21.enums import ad_group_criterion_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_ad__group__criterion__status__pb2
from ......google.ads.googleads.v21.enums import bidding_source_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_bidding__source__pb2
from ......google.ads.googleads.v21.enums import criterion_system_serving_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_criterion__system__serving__status__pb2
from ......google.ads.googleads.v21.enums import criterion_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_criterion__type__pb2
from ......google.ads.googleads.v21.enums import quality_score_bucket_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_quality__score__bucket__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/ads/googleads/v21/resources/ad_group_criterion.proto\x12"google.ads.googleads.v21.resources\x1a.google/ads/googleads/v21/common/criteria.proto\x1a6google/ads/googleads/v21/common/custom_parameter.proto\x1aGgoogle/ads/googleads/v21/enums/ad_group_criterion_approval_status.proto\x1aFgoogle/ads/googleads/v21/enums/ad_group_criterion_primary_status.proto\x1aMgoogle/ads/googleads/v21/enums/ad_group_criterion_primary_status_reason.proto\x1a>google/ads/googleads/v21/enums/ad_group_criterion_status.proto\x1a3google/ads/googleads/v21/enums/bidding_source.proto\x1aDgoogle/ads/googleads/v21/enums/criterion_system_serving_status.proto\x1a3google/ads/googleads/v21/enums/criterion_type.proto\x1a9google/ads/googleads/v21/enums/quality_score_bucket.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xad,\n\x10AdGroupCriterion\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterion\x12\x1e\n\x0ccriterion_id\x188 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18M \x01(\tB\x03\xe0A\x03\x12a\n\x06status\x18\x03 \x01(\x0e2Q.google.ads.googleads.v21.enums.AdGroupCriterionStatusEnum.AdGroupCriterionStatus\x12[\n\x0cquality_info\x18\x04 \x01(\x0b2@.google.ads.googleads.v21.resources.AdGroupCriterion.QualityInfoB\x03\xe0A\x03\x12?\n\x08ad_group\x189 \x01(\tB(\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroupH\x02\x88\x01\x01\x12R\n\x04type\x18\x19 \x01(\x0e2?.google.ads.googleads.v21.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0A\x03\x12\x1a\n\x08negative\x18: \x01(\x08B\x03\xe0A\x05H\x03\x88\x01\x01\x12\x81\x01\n\x15system_serving_status\x184 \x01(\x0e2].google.ads.googleads.v21.enums.CriterionSystemServingStatusEnum.CriterionSystemServingStatusB\x03\xe0A\x03\x12\x7f\n\x0fapproval_status\x185 \x01(\x0e2a.google.ads.googleads.v21.enums.AdGroupCriterionApprovalStatusEnum.AdGroupCriterionApprovalStatusB\x03\xe0A\x03\x12 \n\x13disapproval_reasons\x18; \x03(\tB\x03\xe0A\x03\x12F\n\x06labels\x18< \x03(\tB6\xe0A\x03\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel\x12\x19\n\x0cbid_modifier\x18= \x01(\x01H\x04\x88\x01\x01\x12\x1b\n\x0ecpc_bid_micros\x18> \x01(\x03H\x05\x88\x01\x01\x12\x1b\n\x0ecpm_bid_micros\x18? \x01(\x03H\x06\x88\x01\x01\x12\x1b\n\x0ecpv_bid_micros\x18@ \x01(\x03H\x07\x88\x01\x01\x12#\n\x16percent_cpc_bid_micros\x18A \x01(\x03H\x08\x88\x01\x01\x12*\n\x18effective_cpc_bid_micros\x18B \x01(\x03B\x03\xe0A\x03H\t\x88\x01\x01\x12*\n\x18effective_cpm_bid_micros\x18C \x01(\x03B\x03\xe0A\x03H\n\x88\x01\x01\x12*\n\x18effective_cpv_bid_micros\x18D \x01(\x03B\x03\xe0A\x03H\x0b\x88\x01\x01\x122\n effective_percent_cpc_bid_micros\x18E \x01(\x03B\x03\xe0A\x03H\x0c\x88\x01\x01\x12f\n\x18effective_cpc_bid_source\x18\x15 \x01(\x0e2?.google.ads.googleads.v21.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12f\n\x18effective_cpm_bid_source\x18\x16 \x01(\x0e2?.google.ads.googleads.v21.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12f\n\x18effective_cpv_bid_source\x18\x17 \x01(\x0e2?.google.ads.googleads.v21.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12n\n effective_percent_cpc_bid_source\x18# \x01(\x0e2?.google.ads.googleads.v21.enums.BiddingSourceEnum.BiddingSourceB\x03\xe0A\x03\x12g\n\x12position_estimates\x18\n \x01(\x0b2F.google.ads.googleads.v21.resources.AdGroupCriterion.PositionEstimatesB\x03\xe0A\x03\x12\x12\n\nfinal_urls\x18F \x03(\t\x12\x19\n\x11final_mobile_urls\x18G \x03(\t\x12\x1d\n\x10final_url_suffix\x18H \x01(\tH\r\x88\x01\x01\x12"\n\x15tracking_url_template\x18I \x01(\tH\x0e\x88\x01\x01\x12O\n\x15url_custom_parameters\x18\x0e \x03(\x0b20.google.ads.googleads.v21.common.CustomParameter\x12\x81\x01\n\x0eprimary_status\x18U \x01(\x0e2_.google.ads.googleads.v21.enums.AdGroupCriterionPrimaryStatusEnum.AdGroupCriterionPrimaryStatusB\x03\xe0A\x03H\x0f\x88\x01\x01\x12\x90\x01\n\x16primary_status_reasons\x18V \x03(\x0e2k.google.ads.googleads.v21.enums.AdGroupCriterionPrimaryStatusReasonEnum.AdGroupCriterionPrimaryStatusReasonB\x03\xe0A\x03\x12D\n\x07keyword\x18\x1b \x01(\x0b2,.google.ads.googleads.v21.common.KeywordInfoB\x03\xe0A\x05H\x00\x12H\n\tplacement\x18\x1c \x01(\x0b2..google.ads.googleads.v21.common.PlacementInfoB\x03\xe0A\x05H\x00\x12Z\n\x13mobile_app_category\x18\x1d \x01(\x0b26.google.ads.googleads.v21.common.MobileAppCategoryInfoB\x03\xe0A\x05H\x00\x12Y\n\x12mobile_application\x18\x1e \x01(\x0b26.google.ads.googleads.v21.common.MobileApplicationInfoB\x03\xe0A\x05H\x00\x12O\n\rlisting_group\x18  \x01(\x0b21.google.ads.googleads.v21.common.ListingGroupInfoB\x03\xe0A\x05H\x00\x12G\n\tage_range\x18$ \x01(\x0b2-.google.ads.googleads.v21.common.AgeRangeInfoB\x03\xe0A\x05H\x00\x12B\n\x06gender\x18% \x01(\x0b2+.google.ads.googleads.v21.common.GenderInfoB\x03\xe0A\x05H\x00\x12M\n\x0cincome_range\x18& \x01(\x0b20.google.ads.googleads.v21.common.IncomeRangeInfoB\x03\xe0A\x05H\x00\x12S\n\x0fparental_status\x18\' \x01(\x0b23.google.ads.googleads.v21.common.ParentalStatusInfoB\x03\xe0A\x05H\x00\x12G\n\tuser_list\x18* \x01(\x0b2-.google.ads.googleads.v21.common.UserListInfoB\x03\xe0A\x05H\x00\x12O\n\ryoutube_video\x18( \x01(\x0b21.google.ads.googleads.v21.common.YouTubeVideoInfoB\x03\xe0A\x05H\x00\x12S\n\x0fyoutube_channel\x18) \x01(\x0b23.google.ads.googleads.v21.common.YouTubeChannelInfoB\x03\xe0A\x05H\x00\x12@\n\x05topic\x18+ \x01(\x0b2*.google.ads.googleads.v21.common.TopicInfoB\x03\xe0A\x05H\x00\x12O\n\ruser_interest\x18- \x01(\x0b21.google.ads.googleads.v21.common.UserInterestInfoB\x03\xe0A\x05H\x00\x12D\n\x07webpage\x18. \x01(\x0b2,.google.ads.googleads.v21.common.WebpageInfoB\x03\xe0A\x05H\x00\x12V\n\x11app_payment_model\x18/ \x01(\x0b24.google.ads.googleads.v21.common.AppPaymentModelInfoB\x03\xe0A\x05H\x00\x12S\n\x0fcustom_affinity\x180 \x01(\x0b23.google.ads.googleads.v21.common.CustomAffinityInfoB\x03\xe0A\x05H\x00\x12O\n\rcustom_intent\x181 \x01(\x0b21.google.ads.googleads.v21.common.CustomIntentInfoB\x03\xe0A\x05H\x00\x12S\n\x0fcustom_audience\x18J \x01(\x0b23.google.ads.googleads.v21.common.CustomAudienceInfoB\x03\xe0A\x05H\x00\x12W\n\x11combined_audience\x18K \x01(\x0b25.google.ads.googleads.v21.common.CombinedAudienceInfoB\x03\xe0A\x05H\x00\x12F\n\x08audience\x18O \x01(\x0b2-.google.ads.googleads.v21.common.AudienceInfoB\x03\xe0A\x05H\x00\x12F\n\x08location\x18R \x01(\x0b2-.google.ads.googleads.v21.common.LocationInfoB\x03\xe0A\x05H\x00\x12F\n\x08language\x18S \x01(\x0b2-.google.ads.googleads.v21.common.LanguageInfoB\x03\xe0A\x05H\x00\x12I\n\nlife_event\x18T \x01(\x0b2..google.ads.googleads.v21.common.LifeEventInfoB\x03\xe0A\x05H\x00\x12M\n\x0cvideo_lineup\x18X \x01(\x0b20.google.ads.googleads.v21.common.VideoLineupInfoB\x03\xe0A\x05H\x00\x12]\n\x14extended_demographic\x18Z \x01(\x0b28.google.ads.googleads.v21.common.ExtendedDemographicInfoB\x03\xe0A\x05H\x00\x12I\n\nbrand_list\x18Y \x01(\x0b2..google.ads.googleads.v21.common.BrandListInfoB\x03\xe0A\x05H\x00\x1a\x90\x03\n\x0bQualityInfo\x12\x1f\n\rquality_score\x18\x05 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01\x12n\n\x16creative_quality_score\x18\x02 \x01(\x0e2I.google.ads.googleads.v21.enums.QualityScoreBucketEnum.QualityScoreBucketB\x03\xe0A\x03\x12p\n\x18post_click_quality_score\x18\x03 \x01(\x0e2I.google.ads.googleads.v21.enums.QualityScoreBucketEnum.QualityScoreBucketB\x03\xe0A\x03\x12l\n\x14search_predicted_ctr\x18\x04 \x01(\x0e2I.google.ads.googleads.v21.enums.QualityScoreBucketEnum.QualityScoreBucketB\x03\xe0A\x03B\x10\n\x0e_quality_score\x1a\xbc\x03\n\x11PositionEstimates\x12\'\n\x15first_page_cpc_micros\x18\x06 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12+\n\x19first_position_cpc_micros\x18\x07 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12(\n\x16top_of_page_cpc_micros\x18\x08 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12<\n*estimated_add_clicks_at_first_position_cpc\x18\t \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01\x12:\n(estimated_add_cost_at_first_position_cpc\x18\n \x01(\x03B\x03\xe0A\x03H\x04\x88\x01\x01B\x18\n\x16_first_page_cpc_microsB\x1c\n\x1a_first_position_cpc_microsB\x19\n\x17_top_of_page_cpc_microsB-\n+_estimated_add_clicks_at_first_position_cpcB+\n)_estimated_add_cost_at_first_position_cpc:t\xeaAq\n)googleads.googleapis.com/AdGroupCriterion\x12Dcustomers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}B\x0b\n\tcriterionB\x0f\n\r_criterion_idB\x0b\n\t_ad_groupB\x0b\n\t_negativeB\x0f\n\r_bid_modifierB\x11\n\x0f_cpc_bid_microsB\x11\n\x0f_cpm_bid_microsB\x11\n\x0f_cpv_bid_microsB\x19\n\x17_percent_cpc_bid_microsB\x1b\n\x19_effective_cpc_bid_microsB\x1b\n\x19_effective_cpm_bid_microsB\x1b\n\x19_effective_cpv_bid_microsB#\n!_effective_percent_cpc_bid_microsB\x13\n\x11_final_url_suffixB\x18\n\x16_tracking_url_templateB\x11\n\x0f_primary_statusB\x87\x02\n&com.google.ads.googleads.v21.resourcesB\x15AdGroupCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.ad_group_criterion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x15AdGroupCriterionProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['quality_score']._loaded_options = None
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['quality_score']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['creative_quality_score']._loaded_options = None
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['creative_quality_score']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['post_click_quality_score']._loaded_options = None
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['post_click_quality_score']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['search_predicted_ctr']._loaded_options = None
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['search_predicted_ctr']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['first_page_cpc_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['first_page_cpc_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['first_position_cpc_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['first_position_cpc_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['top_of_page_cpc_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['top_of_page_cpc_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['estimated_add_clicks_at_first_position_cpc']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['estimated_add_clicks_at_first_position_cpc']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['estimated_add_cost_at_first_position_cpc']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['estimated_add_cost_at_first_position_cpc']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)googleads.googleapis.com/AdGroupCriterion'
    _globals['_ADGROUPCRITERION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['display_name']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['quality_info']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['quality_info']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA"\n googleads.googleapis.com/AdGroup'
    _globals['_ADGROUPCRITERION'].fields_by_name['type']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['negative']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['negative']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['system_serving_status']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['system_serving_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['approval_status']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['approval_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['disapproval_reasons']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['disapproval_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['labels']._serialized_options = b'\xe0A\x03\xfaA0\n.googleads.googleapis.com/AdGroupCriterionLabel'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpm_bid_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpm_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpv_bid_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpv_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_percent_cpc_bid_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_percent_cpc_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_source']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpm_bid_source']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpm_bid_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpv_bid_source']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpv_bid_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_percent_cpc_bid_source']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_percent_cpc_bid_source']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['position_estimates']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['position_estimates']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['primary_status']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['primary_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['primary_status_reasons']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['primary_status_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['keyword']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['keyword']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['placement']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['placement']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['mobile_app_category']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['mobile_app_category']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['mobile_application']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['mobile_application']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['listing_group']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['listing_group']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['age_range']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['age_range']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['gender']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['gender']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['income_range']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['income_range']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['parental_status']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['parental_status']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['user_list']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['user_list']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['youtube_video']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['youtube_video']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['youtube_channel']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['youtube_channel']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['topic']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['topic']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['user_interest']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['user_interest']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['webpage']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['webpage']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['app_payment_model']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['app_payment_model']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_affinity']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_affinity']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_intent']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_intent']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_audience']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['custom_audience']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['combined_audience']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['combined_audience']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['audience']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['audience']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['location']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['language']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['language']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['life_event']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['life_event']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['video_lineup']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['video_lineup']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['extended_demographic']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['extended_demographic']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['brand_list']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['brand_list']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION']._loaded_options = None
    _globals['_ADGROUPCRITERION']._serialized_options = b'\xeaAq\n)googleads.googleapis.com/AdGroupCriterion\x12Dcustomers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}'
    _globals['_ADGROUPCRITERION']._serialized_start = 787
    _globals['_ADGROUPCRITERION']._serialized_end = 6464
    _globals['_ADGROUPCRITERION_QUALITYINFO']._serialized_start = 5152
    _globals['_ADGROUPCRITERION_QUALITYINFO']._serialized_end = 5552
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES']._serialized_start = 5555
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES']._serialized_end = 5999