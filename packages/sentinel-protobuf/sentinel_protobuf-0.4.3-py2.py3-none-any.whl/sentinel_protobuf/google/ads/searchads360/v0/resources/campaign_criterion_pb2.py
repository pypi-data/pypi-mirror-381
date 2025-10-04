"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/campaign_criterion.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.common import criteria_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_common_dot_criteria__pb2
from ......google.ads.searchads360.v0.enums import campaign_criterion_status_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_campaign__criterion__status__pb2
from ......google.ads.searchads360.v0.enums import criterion_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_criterion__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/searchads360/v0/resources/campaign_criterion.proto\x12$google.ads.searchads360.v0.resources\x1a0google/ads/searchads360/v0/common/criteria.proto\x1a@google/ads/searchads360/v0/enums/campaign_criterion_status.proto\x1a5google/ads/searchads360/v0/enums/criterion_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x83\n\n\x11CampaignCriterion\x12L\n\rresource_name\x18\x01 \x01(\tB5\xe0A\x05\xfaA/\n-searchads360.googleapis.com/CampaignCriterion\x12\x1e\n\x0ccriterion_id\x18& \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x19\n\x0cdisplay_name\x18+ \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cbid_modifier\x18\' \x01(\x02H\x02\x88\x01\x01\x12\x1a\n\x08negative\x18( \x01(\x08B\x03\xe0A\x05H\x03\x88\x01\x01\x12T\n\x04type\x18\x06 \x01(\x0e2A.google.ads.searchads360.v0.enums.CriterionTypeEnum.CriterionTypeB\x03\xe0A\x03\x12e\n\x06status\x18# \x01(\x0e2U.google.ads.searchads360.v0.enums.CampaignCriterionStatusEnum.CampaignCriterionStatus\x12\x1f\n\x12last_modified_time\x18, \x01(\tB\x03\xe0A\x03\x12F\n\x07keyword\x18\x08 \x01(\x0b2..google.ads.searchads360.v0.common.KeywordInfoB\x03\xe0A\x05H\x00\x12H\n\x08location\x18\x0c \x01(\x0b2/.google.ads.searchads360.v0.common.LocationInfoB\x03\xe0A\x05H\x00\x12D\n\x06device\x18\r \x01(\x0b2-.google.ads.searchads360.v0.common.DeviceInfoB\x03\xe0A\x05H\x00\x12I\n\tage_range\x18\x10 \x01(\x0b2/.google.ads.searchads360.v0.common.AgeRangeInfoB\x03\xe0A\x05H\x00\x12D\n\x06gender\x18\x11 \x01(\x0b2-.google.ads.searchads360.v0.common.GenderInfoB\x03\xe0A\x05H\x00\x12I\n\tuser_list\x18\x16 \x01(\x0b2/.google.ads.searchads360.v0.common.UserListInfoB\x03\xe0A\x05H\x00\x12H\n\x08language\x18\x1a \x01(\x0b2/.google.ads.searchads360.v0.common.LanguageInfoB\x03\xe0A\x05H\x00\x12F\n\x07webpage\x18\x1f \x01(\x0b2..google.ads.searchads360.v0.common.WebpageInfoB\x03\xe0A\x05H\x00\x12S\n\x0elocation_group\x18" \x01(\x0b24.google.ads.searchads360.v0.common.LocationGroupInfoB\x03\xe0A\x05H\x00:y\xeaAv\n-searchads360.googleapis.com/CampaignCriterion\x12Ecustomers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}B\x0b\n\tcriterionB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x0b\n\t_negativeB\x96\x02\n(com.google.ads.searchads360.v0.resourcesB\x16CampaignCriterionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.campaign_criterion_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x16CampaignCriterionProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA/\n-searchads360.googleapis.com/CampaignCriterion'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['negative']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['negative']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['type']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['keyword']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['device']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['device']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['age_range']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['age_range']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['gender']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['gender']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_list']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['user_list']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['language']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['language']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['webpage']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['webpage']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location_group']._loaded_options = None
    _globals['_CAMPAIGNCRITERION'].fields_by_name['location_group']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNCRITERION']._loaded_options = None
    _globals['_CAMPAIGNCRITERION']._serialized_options = b'\xeaAv\n-searchads360.googleapis.com/CampaignCriterion\x12Ecustomers/{customer_id}/campaignCriteria/{campaign_id}~{criterion_id}'
    _globals['_CAMPAIGNCRITERION']._serialized_start = 335
    _globals['_CAMPAIGNCRITERION']._serialized_end = 1618