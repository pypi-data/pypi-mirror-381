"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/campaign_budget_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v20.resources import campaign_budget_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_campaign__budget__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/ads/googleads/v20/services/campaign_budget_service.proto\x12!google.ads.googleads.v20.services\x1a:google/ads/googleads/v20/enums/response_content_type.proto\x1a8google/ads/googleads/v20/resources/campaign_budget.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xa9\x02\n\x1cMutateCampaignBudgetsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\noperations\x18\x02 \x03(\x0b2:.google.ads.googleads.v20.services.CampaignBudgetOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v20.enums.ResponseContentTypeEnum.ResponseContentType"\xa3\x02\n\x17CampaignBudgetOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12D\n\x06create\x18\x01 \x01(\x0b22.google.ads.googleads.v20.resources.CampaignBudgetH\x00\x12D\n\x06update\x18\x02 \x01(\x0b22.google.ads.googleads.v20.resources.CampaignBudgetH\x00\x12>\n\x06remove\x18\x03 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/CampaignBudgetH\x00B\x0b\n\toperation"\xa2\x01\n\x1dMutateCampaignBudgetsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12N\n\x07results\x18\x02 \x03(\x0b2=.google.ads.googleads.v20.services.MutateCampaignBudgetResult"\xae\x01\n\x1aMutateCampaignBudgetResult\x12C\n\rresource_name\x18\x01 \x01(\tB,\xfaA)\n\'googleads.googleapis.com/CampaignBudget\x12K\n\x0fcampaign_budget\x18\x02 \x01(\x0b22.google.ads.googleads.v20.resources.CampaignBudget2\xd6\x02\n\x15CampaignBudgetService\x12\xf5\x01\n\x15MutateCampaignBudgets\x12?.google.ads.googleads.v20.services.MutateCampaignBudgetsRequest\x1a@.google.ads.googleads.v20.services.MutateCampaignBudgetsResponse"Y\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v20/customers/{customer_id=*}/campaignBudgets:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x86\x02\n%com.google.ads.googleads.v20.servicesB\x1aCampaignBudgetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.campaign_budget_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x1aCampaignBudgetServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNBUDGETOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_CAMPAIGNBUDGETOPERATION'].fields_by_name['remove']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/CampaignBudget"
    _globals['_MUTATECAMPAIGNBUDGETRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATECAMPAIGNBUDGETRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA)\n'googleads.googleapis.com/CampaignBudget"
    _globals['_CAMPAIGNBUDGETSERVICE']._loaded_options = None
    _globals['_CAMPAIGNBUDGETSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_CAMPAIGNBUDGETSERVICE'].methods_by_name['MutateCampaignBudgets']._loaded_options = None
    _globals['_CAMPAIGNBUDGETSERVICE'].methods_by_name['MutateCampaignBudgets']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02:"5/v20/customers/{customer_id=*}/campaignBudgets:mutate:\x01*'
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST']._serialized_start = 395
    _globals['_MUTATECAMPAIGNBUDGETSREQUEST']._serialized_end = 692
    _globals['_CAMPAIGNBUDGETOPERATION']._serialized_start = 695
    _globals['_CAMPAIGNBUDGETOPERATION']._serialized_end = 986
    _globals['_MUTATECAMPAIGNBUDGETSRESPONSE']._serialized_start = 989
    _globals['_MUTATECAMPAIGNBUDGETSRESPONSE']._serialized_end = 1151
    _globals['_MUTATECAMPAIGNBUDGETRESULT']._serialized_start = 1154
    _globals['_MUTATECAMPAIGNBUDGETRESULT']._serialized_end = 1328
    _globals['_CAMPAIGNBUDGETSERVICE']._serialized_start = 1331
    _globals['_CAMPAIGNBUDGETSERVICE']._serialized_end = 1673