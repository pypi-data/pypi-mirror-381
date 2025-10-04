"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/campaign_budget.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import budget_delivery_method_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_budget__delivery__method__pb2
from ......google.ads.googleads.v21.enums import budget_period_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_budget__period__pb2
from ......google.ads.googleads.v21.enums import budget_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_budget__status__pb2
from ......google.ads.googleads.v21.enums import budget_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_budget__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v21/resources/campaign_budget.proto\x12"google.ads.googleads.v21.resources\x1a;google/ads/googleads/v21/enums/budget_delivery_method.proto\x1a2google/ads/googleads/v21/enums/budget_period.proto\x1a2google/ads/googleads/v21/enums/budget_status.proto\x1a0google/ads/googleads/v21/enums/budget_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf3\x0b\n\x0eCampaignBudget\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x05\xfaA)\n\'googleads.googleapis.com/CampaignBudget\x12\x14\n\x02id\x18\x13 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x14 \x01(\tH\x01\x88\x01\x01\x12\x1a\n\ramount_micros\x18\x15 \x01(\x03H\x02\x88\x01\x01\x12 \n\x13total_amount_micros\x18\x16 \x01(\x03H\x03\x88\x01\x01\x12R\n\x06status\x18\x06 \x01(\x0e2=.google.ads.googleads.v21.enums.BudgetStatusEnum.BudgetStatusB\x03\xe0A\x03\x12f\n\x0fdelivery_method\x18\x07 \x01(\x0e2M.google.ads.googleads.v21.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod\x12\x1e\n\x11explicitly_shared\x18\x17 \x01(\x08H\x04\x88\x01\x01\x12!\n\x0freference_count\x18\x18 \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12(\n\x16has_recommended_budget\x18\x19 \x01(\x08B\x03\xe0A\x03H\x06\x88\x01\x01\x122\n recommended_budget_amount_micros\x18\x1a \x01(\x03B\x03\xe0A\x03H\x07\x88\x01\x01\x12R\n\x06period\x18\r \x01(\x0e2=.google.ads.googleads.v21.enums.BudgetPeriodEnum.BudgetPeriodB\x03\xe0A\x05\x12C\n1recommended_budget_estimated_change_weekly_clicks\x18\x1b \x01(\x03B\x03\xe0A\x03H\x08\x88\x01\x01\x12H\n6recommended_budget_estimated_change_weekly_cost_micros\x18\x1c \x01(\x03B\x03\xe0A\x03H\t\x88\x01\x01\x12I\n7recommended_budget_estimated_change_weekly_interactions\x18\x1d \x01(\x03B\x03\xe0A\x03H\n\x88\x01\x01\x12B\n0recommended_budget_estimated_change_weekly_views\x18\x1e \x01(\x03B\x03\xe0A\x03H\x0b\x88\x01\x01\x12L\n\x04type\x18\x12 \x01(\x0e29.google.ads.googleads.v21.enums.BudgetTypeEnum.BudgetTypeB\x03\xe0A\x05\x12#\n\x1baligned_bidding_strategy_id\x18\x1f \x01(\x03:j\xeaAg\n\'googleads.googleapis.com/CampaignBudget\x12<customers/{customer_id}/campaignBudgets/{campaign_budget_id}B\x05\n\x03_idB\x07\n\x05_nameB\x10\n\x0e_amount_microsB\x16\n\x14_total_amount_microsB\x14\n\x12_explicitly_sharedB\x12\n\x10_reference_countB\x19\n\x17_has_recommended_budgetB#\n!_recommended_budget_amount_microsB4\n2_recommended_budget_estimated_change_weekly_clicksB9\n7_recommended_budget_estimated_change_weekly_cost_microsB:\n8_recommended_budget_estimated_change_weekly_interactionsB3\n1_recommended_budget_estimated_change_weekly_viewsB\x85\x02\n&com.google.ads.googleads.v21.resourcesB\x13CampaignBudgetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.campaign_budget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x13CampaignBudgetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x05\xfaA)\n'googleads.googleapis.com/CampaignBudget"
    _globals['_CAMPAIGNBUDGET'].fields_by_name['id']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['status']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['reference_count']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['reference_count']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['has_recommended_budget']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['has_recommended_budget']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_amount_micros']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_amount_micros']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['period']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['period']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_clicks']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_clicks']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_cost_micros']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_cost_micros']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_interactions']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_interactions']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_views']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['recommended_budget_estimated_change_weekly_views']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['type']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNBUDGET']._loaded_options = None
    _globals['_CAMPAIGNBUDGET']._serialized_options = b"\xeaAg\n'googleads.googleapis.com/CampaignBudget\x12<customers/{customer_id}/campaignBudgets/{campaign_budget_id}"
    _globals['_CAMPAIGNBUDGET']._serialized_start = 372
    _globals['_CAMPAIGNBUDGET']._serialized_end = 1895