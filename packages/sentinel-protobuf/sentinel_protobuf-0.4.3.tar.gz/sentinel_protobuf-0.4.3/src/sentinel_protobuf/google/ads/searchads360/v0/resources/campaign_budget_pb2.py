"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/campaign_budget.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import budget_delivery_method_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_budget__delivery__method__pb2
from ......google.ads.searchads360.v0.enums import budget_period_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_budget__period__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/searchads360/v0/resources/campaign_budget.proto\x12$google.ads.searchads360.v0.resources\x1a=google/ads/searchads360/v0/enums/budget_delivery_method.proto\x1a4google/ads/searchads360/v0/enums/budget_period.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xaf\x03\n\x0eCampaignBudget\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x05\xfaA,\n*searchads360.googleapis.com/CampaignBudget\x12\x1a\n\ramount_micros\x18\x15 \x01(\x03H\x00\x88\x01\x01\x12h\n\x0fdelivery_method\x18\x07 \x01(\x0e2O.google.ads.searchads360.v0.enums.BudgetDeliveryMethodEnum.BudgetDeliveryMethod\x12T\n\x06period\x18\r \x01(\x0e2?.google.ads.searchads360.v0.enums.BudgetPeriodEnum.BudgetPeriodB\x03\xe0A\x05:d\xeaAa\n*searchads360.googleapis.com/CampaignBudget\x123customers/{customer_id}/campaignBudgets/{budget_id}B\x10\n\x0e_amount_microsB\x93\x02\n(com.google.ads.searchads360.v0.resourcesB\x13CampaignBudgetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.campaign_budget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x13CampaignBudgetProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA,\n*searchads360.googleapis.com/CampaignBudget'
    _globals['_CAMPAIGNBUDGET'].fields_by_name['period']._loaded_options = None
    _globals['_CAMPAIGNBUDGET'].fields_by_name['period']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNBUDGET']._loaded_options = None
    _globals['_CAMPAIGNBUDGET']._serialized_options = b'\xeaAa\n*searchads360.googleapis.com/CampaignBudget\x123customers/{customer_id}/campaignBudgets/{budget_id}'
    _globals['_CAMPAIGNBUDGET']._serialized_start = 278
    _globals['_CAMPAIGNBUDGET']._serialized_end = 709