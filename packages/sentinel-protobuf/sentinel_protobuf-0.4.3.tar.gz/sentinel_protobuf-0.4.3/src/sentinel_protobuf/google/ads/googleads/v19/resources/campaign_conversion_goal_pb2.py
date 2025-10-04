"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/campaign_conversion_goal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import conversion_action_category_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_conversion__action__category__pb2
from ......google.ads.googleads.v19.enums import conversion_origin_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_conversion__origin__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/ads/googleads/v19/resources/campaign_conversion_goal.proto\x12"google.ads.googleads.v19.resources\x1a?google/ads/googleads/v19/enums/conversion_action_category.proto\x1a6google/ads/googleads/v19/enums/conversion_origin.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x82\x04\n\x16CampaignConversionGoal\x12N\n\rresource_name\x18\x01 \x01(\tB7\xe0A\x05\xfaA1\n/googleads.googleapis.com/CampaignConversionGoal\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign\x12g\n\x08category\x18\x03 \x01(\x0e2U.google.ads.googleads.v19.enums.ConversionActionCategoryEnum.ConversionActionCategory\x12U\n\x06origin\x18\x04 \x01(\x0e2E.google.ads.googleads.v19.enums.ConversionOriginEnum.ConversionOrigin\x12\x10\n\x08biddable\x18\x05 \x01(\x08:\x88\x01\xeaA\x84\x01\n/googleads.googleapis.com/CampaignConversionGoal\x12Qcustomers/{customer_id}/campaignConversionGoals/{campaign_id}~{category}~{source}B\x8d\x02\n&com.google.ads.googleads.v19.resourcesB\x1bCampaignConversionGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.campaign_conversion_goal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1bCampaignConversionGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CAMPAIGNCONVERSIONGOAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNCONVERSIONGOAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA1\n/googleads.googleapis.com/CampaignConversionGoal'
    _globals['_CAMPAIGNCONVERSIONGOAL'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNCONVERSIONGOAL'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNCONVERSIONGOAL']._loaded_options = None
    _globals['_CAMPAIGNCONVERSIONGOAL']._serialized_options = b'\xeaA\x84\x01\n/googleads.googleapis.com/CampaignConversionGoal\x12Qcustomers/{customer_id}/campaignConversionGoals/{campaign_id}~{category}~{source}'
    _globals['_CAMPAIGNCONVERSIONGOAL']._serialized_start = 287
    _globals['_CAMPAIGNCONVERSIONGOAL']._serialized_end = 801