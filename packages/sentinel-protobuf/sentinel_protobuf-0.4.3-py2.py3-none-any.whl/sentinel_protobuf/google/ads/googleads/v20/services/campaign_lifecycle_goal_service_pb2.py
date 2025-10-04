"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/campaign_lifecycle_goal_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import campaign_lifecycle_goal_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_campaign__lifecycle__goal__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nGgoogle/ads/googleads/v20/services/campaign_lifecycle_goal_service.proto\x12!google.ads.googleads.v20.services\x1a@google/ads/googleads/v20/resources/campaign_lifecycle_goal.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xb9\x01\n&ConfigureCampaignLifecycleGoalsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\toperation\x18\x02 \x01(\x0b2A.google.ads.googleads.v20.services.CampaignLifecycleGoalOperationB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"\xfd\x01\n\x1eCampaignLifecycleGoalOperation\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12K\n\x06create\x18\x01 \x01(\x0b29.google.ads.googleads.v20.resources.CampaignLifecycleGoalH\x00\x12K\n\x06update\x18\x03 \x01(\x0b29.google.ads.googleads.v20.resources.CampaignLifecycleGoalH\x00B\x0b\n\toperation"\x83\x01\n\'ConfigureCampaignLifecycleGoalsResponse\x12X\n\x06result\x18\x01 \x01(\x0b2H.google.ads.googleads.v20.services.ConfigureCampaignLifecycleGoalsResult"s\n%ConfigureCampaignLifecycleGoalsResult\x12J\n\rresource_name\x18\x01 \x01(\tB3\xfaA0\n.googleads.googleapis.com/CampaignLifecycleGoal2\x99\x03\n\x1cCampaignLifecycleGoalService\x12\xb1\x02\n\x1fConfigureCampaignLifecycleGoals\x12I.google.ads.googleads.v20.services.ConfigureCampaignLifecycleGoalsRequest\x1aJ.google.ads.googleads.v20.services.ConfigureCampaignLifecycleGoalsResponse"w\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02Y"T/v20/customers/{customer_id=*}/campaignLifecycleGoal:configureCampaignLifecycleGoals:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8d\x02\n%com.google.ads.googleads.v20.servicesB!CampaignLifecycleGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.campaign_lifecycle_goal_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB!CampaignLifecycleGoalServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_CAMPAIGNLIFECYCLEGOALOPERATION'].fields_by_name['update_mask']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOALOPERATION'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA0\n.googleads.googleapis.com/CampaignLifecycleGoal'
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE'].methods_by_name['ConfigureCampaignLifecycleGoals']._loaded_options = None
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE'].methods_by_name['ConfigureCampaignLifecycleGoals']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x02Y"T/v20/customers/{customer_id=*}/campaignLifecycleGoal:configureCampaignLifecycleGoals:\x01*'
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST']._serialized_start = 326
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSREQUEST']._serialized_end = 511
    _globals['_CAMPAIGNLIFECYCLEGOALOPERATION']._serialized_start = 514
    _globals['_CAMPAIGNLIFECYCLEGOALOPERATION']._serialized_end = 767
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESPONSE']._serialized_start = 770
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESPONSE']._serialized_end = 901
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESULT']._serialized_start = 903
    _globals['_CONFIGURECAMPAIGNLIFECYCLEGOALSRESULT']._serialized_end = 1018
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE']._serialized_start = 1021
    _globals['_CAMPAIGNLIFECYCLEGOALSERVICE']._serialized_end = 1430