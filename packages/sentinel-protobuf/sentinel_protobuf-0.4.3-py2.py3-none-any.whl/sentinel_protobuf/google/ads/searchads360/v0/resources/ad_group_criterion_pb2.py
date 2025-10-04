"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/ad_group_criterion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import criteria_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_criteria__pb2
from ......google.ads.searchads360.v0.enums import ad_group_criterion_engine_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__criterion__engine__status__pb2
from ......google.ads.searchads360.v0.enums import ad_group_criterion_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_ad__group__criterion__status__pb2
from ......google.ads.searchads360.v0.enums import criterion_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_criterion__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/searchads360/v0/resources/ad_group_criterion.proto\x12$google.ads.searchads360.v0.resources\x1a0google/ads/searchads360/v0/common/criteria.proto\x1aGgoogle/ads/searchads360/v0/enums/ad_group_criterion_engine_status.proto\x1a@google/ads/searchads360/v0/enums/ad_group_criterion_status.proto\x1a5google/ads/searchads360/v0/enums/criterion_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf8\x10\n\x10AdGroupCriterion\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AdGroupCriterion\x12\x1e\n\x0ccriterion_id\x188 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1a\n\rcreation_time\x18Q \x01(\tB\x03\xe0A\x03\x12c\n\x06status\x18\x03 \x01(\x0e2S.google.ads.searchads360.v0.enums.AdGroupCriterionStatusEnum.AdGroupCriterionStatus\x12]\n\x0cquality_info\x18\x04 \x01(\x0b2B.google.ads.searchads360.v0.resources.AdGroupCriterion.QualityInfoB\x03\xe0A\x03\x12B\n\x08ad_group\x189 \x01(\tB+\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroupH\x02\x88\x01\x01\x12T\n\x04type\x18\x19 \x01(\x0e2A.google.ads.searchads360.v0.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0A\x03\x12\x1a\n\x08negative\x18: \x01(\x08B\x03\xe0A\x05H\x03\x88\x01\x01\x12I\n\x06labels\x18< \x03(\tB9\xe0A\x03\xfaA3\n1searchads360.googleapis.com/AdGroupCriterionLabel\x12\\\n\x10effective_labels\x18W \x03(\tBB\xe0A\x03\xfaA<\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel\x12\x19\n\x0cbid_modifier\x18= \x01(\x01H\x04\x88\x01\x01\x12\x1b\n\x0ecpc_bid_micros\x18> \x01(\x03H\x05\x88\x01\x01\x12*\n\x18effective_cpc_bid_micros\x18B \x01(\x03B\x03\xe0A\x03H\x06\x88\x01\x01\x12i\n\x12position_estimates\x18\n \x01(\x0b2H.google.ads.searchads360.v0.resources.AdGroupCriterion.PositionEstimatesB\x03\xe0A\x03\x12\x12\n\nfinal_urls\x18F \x03(\t\x12\x80\x01\n\rengine_status\x18P \x01(\x0e2_.google.ads.searchads360.v0.enums.AdGroupCriterionEngineStatusEnum.AdGroupCriterionEngineStatusB\x03\xe0A\x03H\x07\x88\x01\x01\x12\x1d\n\x10final_url_suffix\x18H \x01(\tH\x08\x88\x01\x01\x12"\n\x15tracking_url_template\x18I \x01(\tH\t\x88\x01\x01\x12\x16\n\tengine_id\x18L \x01(\tB\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18N \x01(\tB\x03\xe0A\x03\x12F\n\x07keyword\x18\x1b \x01(\x0b2..google.ads.searchads360.v0.common.KeywordInfoB\x03\xe0A\x05H\x00\x12Q\n\rlisting_group\x18  \x01(\x0b23.google.ads.searchads360.v0.common.ListingGroupInfoB\x03\xe0A\x05H\x00\x12I\n\tage_range\x18$ \x01(\x0b2/.google.ads.searchads360.v0.common.AgeRangeInfoB\x03\xe0A\x05H\x00\x12D\n\x06gender\x18% \x01(\x0b2-.google.ads.searchads360.v0.common.GenderInfoB\x03\xe0A\x05H\x00\x12I\n\tuser_list\x18* \x01(\x0b2/.google.ads.searchads360.v0.common.UserListInfoB\x03\xe0A\x05H\x00\x12F\n\x07webpage\x18. \x01(\x0b2..google.ads.searchads360.v0.common.WebpageInfoB\x03\xe0A\x05H\x00\x12H\n\x08location\x18R \x01(\x0b2/.google.ads.searchads360.v0.common.LocationInfoB\x03\xe0A\x05H\x00\x1a@\n\x0bQualityInfo\x12\x1f\n\rquality_score\x18\x05 \x01(\x05B\x03\xe0A\x03H\x00\x88\x01\x01B\x10\n\x0e_quality_score\x1aX\n\x11PositionEstimates\x12(\n\x16top_of_page_cpc_micros\x18\x08 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01B\x19\n\x17_top_of_page_cpc_micros:w\xeaAt\n,searchads360.googleapis.com/AdGroupCriterion\x12Dcustomers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}B\x0b\n\tcriterionB\x0f\n\r_criterion_idB\x0b\n\t_ad_groupB\x0b\n\t_negativeB\x0f\n\r_bid_modifierB\x11\n\x0f_cpc_bid_microsB\x1b\n\x19_effective_cpc_bid_microsB\x10\n\x0e_engine_statusB\x13\n\x11_final_url_suffixB\x18\n\x16_tracking_url_templateB\x95\x02\n(com.google.ads.searchads360.v0.resourcesB\x15AdGroupCriterionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.ad_group_criterion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x15AdGroupCriterionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['quality_score']._loaded_options = None
    _globals['_ADGROUPCRITERION_QUALITYINFO'].fields_by_name['quality_score']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['top_of_page_cpc_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES'].fields_by_name['top_of_page_cpc_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,searchads360.googleapis.com/AdGroupCriterion'
    _globals['_ADGROUPCRITERION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['quality_info']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['quality_info']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['ad_group']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['ad_group']._serialized_options = b'\xe0A\x05\xfaA%\n#searchads360.googleapis.com/AdGroup'
    _globals['_ADGROUPCRITERION'].fields_by_name['type']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['negative']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['negative']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['labels']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['labels']._serialized_options = b'\xe0A\x03\xfaA3\n1searchads360.googleapis.com/AdGroupCriterionLabel'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_labels']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_labels']._serialized_options = b'\xe0A\x03\xfaA<\n:searchads360.googleapis.com/AdGroupCriterionEffectiveLabel'
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_micros']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['effective_cpc_bid_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['position_estimates']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['position_estimates']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['engine_status']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['engine_status']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['engine_id']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERION'].fields_by_name['keyword']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['keyword']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['listing_group']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['listing_group']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['age_range']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['age_range']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['gender']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['gender']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['user_list']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['user_list']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['webpage']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['webpage']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION'].fields_by_name['location']._loaded_options = None
    _globals['_ADGROUPCRITERION'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_ADGROUPCRITERION']._loaded_options = None
    _globals['_ADGROUPCRITERION']._serialized_options = b'\xeaAt\n,searchads360.googleapis.com/AdGroupCriterion\x12Dcustomers/{customer_id}/adGroupCriteria/{ad_group_id}~{criterion_id}'
    _globals['_ADGROUPCRITERION']._serialized_start = 408
    _globals['_ADGROUPCRITERION']._serialized_end = 2576
    _globals['_ADGROUPCRITERION_QUALITYINFO']._serialized_start = 2115
    _globals['_ADGROUPCRITERION_QUALITYINFO']._serialized_end = 2179
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES']._serialized_start = 2181
    _globals['_ADGROUPCRITERION_POSITIONESTIMATES']._serialized_end = 2269