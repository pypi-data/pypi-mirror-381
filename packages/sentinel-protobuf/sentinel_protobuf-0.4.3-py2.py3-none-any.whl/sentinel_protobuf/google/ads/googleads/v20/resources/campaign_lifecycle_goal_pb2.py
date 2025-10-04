"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/campaign_lifecycle_goal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import lifecycle_goals_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_lifecycle__goals__pb2
from ......google.ads.googleads.v20.enums import customer_acquisition_optimization_mode_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_customer__acquisition__optimization__mode__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v20/resources/campaign_lifecycle_goal.proto\x12"google.ads.googleads.v20.resources\x1a5google/ads/googleads/v20/common/lifecycle_goals.proto\x1aKgoogle/ads/googleads/v20/enums/customer_acquisition_optimization_mode.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8c\x03\n\x15CampaignLifecycleGoal\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/CampaignLifecycleGoal\x12;\n\x08campaign\x18\x02 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign\x12t\n"customer_acquisition_goal_settings\x18\x03 \x01(\x0b2C.google.ads.googleads.v20.resources.CustomerAcquisitionGoalSettingsB\x03\xe0A\x03:q\xeaAn\n.googleads.googleapis.com/CampaignLifecycleGoal\x12<customers/{customer_id}/campaignLifecycleGoals/{campaign_id}"\x89\x02\n\x1fCustomerAcquisitionGoalSettings\x12\x8b\x01\n\x11optimization_mode\x18\x01 \x01(\x0e2k.google.ads.googleads.v20.enums.CustomerAcquisitionOptimizationModeEnum.CustomerAcquisitionOptimizationModeB\x03\xe0A\x03\x12X\n\x0evalue_settings\x18\x02 \x01(\x0b2;.google.ads.googleads.v20.common.LifecycleGoalValueSettingsB\x03\xe0A\x03B\x8c\x02\n&com.google.ads.googleads.v20.resourcesB\x1aCampaignLifecycleGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.campaign_lifecycle_goal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1aCampaignLifecycleGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/CampaignLifecycleGoal'
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['customer_acquisition_goal_settings']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOAL'].fields_by_name['customer_acquisition_goal_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNLIFECYCLEGOAL']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOAL']._serialized_options = b'\xeaAn\n.googleads.googleapis.com/CampaignLifecycleGoal\x12<customers/{customer_id}/campaignLifecycleGoals/{campaign_id}'
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS'].fields_by_name['optimization_mode']._loaded_options = None
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS'].fields_by_name['optimization_mode']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS'].fields_by_name['value_settings']._loaded_options = None
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS'].fields_by_name['value_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNLIFECYCLEGOAL']._serialized_start = 297
    _globals['_CAMPAIGNLIFECYCLEGOAL']._serialized_end = 693
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS']._serialized_start = 696
    _globals['_CUSTOMERACQUISITIONGOALSETTINGS']._serialized_end = 961