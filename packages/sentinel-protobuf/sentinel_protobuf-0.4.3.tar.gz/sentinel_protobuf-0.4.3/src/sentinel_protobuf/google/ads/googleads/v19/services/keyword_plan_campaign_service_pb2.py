"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/keyword_plan_campaign_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import keyword_plan_campaign_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_keyword__plan__campaign__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v19/services/keyword_plan_campaign_service.proto\x12!google.ads.googleads.v19.services\x1a>google/ads/googleads/v19/resources/keyword_plan_campaign.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xc7\x01\n!MutateKeywordPlanCampaignsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12X\n\noperations\x18\x02 \x03(\x0b2?.google.ads.googleads.v19.services.KeywordPlanCampaignOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xb7\x02\n\x1cKeywordPlanCampaignOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12I\n\x06create\x18\x01 \x01(\x0b27.google.ads.googleads.v19.resources.KeywordPlanCampaignH\x00\x12I\n\x06update\x18\x02 \x01(\x0b27.google.ads.googleads.v19.resources.KeywordPlanCampaignH\x00\x12C\n\x06remove\x18\x03 \x01(\tB1\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaignH\x00B\x0b\n\toperation"\xac\x01\n"MutateKeywordPlanCampaignsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12S\n\x07results\x18\x02 \x03(\x0b2B.google.ads.googleads.v19.services.MutateKeywordPlanCampaignResult"k\n\x1fMutateKeywordPlanCampaignResult\x12H\n\rresource_name\x18\x01 \x01(\tB1\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign2\xef\x02\n\x1aKeywordPlanCampaignService\x12\x89\x02\n\x1aMutateKeywordPlanCampaigns\x12D.google.ads.googleads.v19.services.MutateKeywordPlanCampaignsRequest\x1aE.google.ads.googleads.v19.services.MutateKeywordPlanCampaignsResponse"^\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/keywordPlanCampaigns:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8b\x02\n%com.google.ads.googleads.v19.servicesB\x1fKeywordPlanCampaignServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.keyword_plan_campaign_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1fKeywordPlanCampaignServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_KEYWORDPLANCAMPAIGNOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign'
    _globals['_KEYWORDPLANCAMPAIGNSERVICE']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_KEYWORDPLANCAMPAIGNSERVICE'].methods_by_name['MutateKeywordPlanCampaigns']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNSERVICE'].methods_by_name['MutateKeywordPlanCampaigns']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02?":/v19/customers/{customer_id=*}/keywordPlanCampaigns:mutate:\x01*'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST']._serialized_start = 347
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSREQUEST']._serialized_end = 546
    _globals['_KEYWORDPLANCAMPAIGNOPERATION']._serialized_start = 549
    _globals['_KEYWORDPLANCAMPAIGNOPERATION']._serialized_end = 860
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSRESPONSE']._serialized_start = 863
    _globals['_MUTATEKEYWORDPLANCAMPAIGNSRESPONSE']._serialized_end = 1035
    _globals['_MUTATEKEYWORDPLANCAMPAIGNRESULT']._serialized_start = 1037
    _globals['_MUTATEKEYWORDPLANCAMPAIGNRESULT']._serialized_end = 1144
    _globals['_KEYWORDPLANCAMPAIGNSERVICE']._serialized_start = 1147
    _globals['_KEYWORDPLANCAMPAIGNSERVICE']._serialized_end = 1514