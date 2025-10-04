"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/keyword_plan_campaign_keyword_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.resources import keyword_plan_campaign_keyword_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_keyword__plan__campaign__keyword__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/ads/googleads/v19/services/keyword_plan_campaign_keyword_service.proto\x12!google.ads.googleads.v19.services\x1aFgoogle/ads/googleads/v19/resources/keyword_plan_campaign_keyword.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xd5\x01\n(MutateKeywordPlanCampaignKeywordsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12_\n\noperations\x18\x02 \x03(\x0b2F.google.ads.googleads.v19.services.KeywordPlanCampaignKeywordOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xd3\x02\n#KeywordPlanCampaignKeywordOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12P\n\x06create\x18\x01 \x01(\x0b2>.google.ads.googleads.v19.resources.KeywordPlanCampaignKeywordH\x00\x12P\n\x06update\x18\x02 \x01(\x0b2>.google.ads.googleads.v19.resources.KeywordPlanCampaignKeywordH\x00\x12J\n\x06remove\x18\x03 \x01(\tB8\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeywordH\x00B\x0b\n\toperation"\xba\x01\n)MutateKeywordPlanCampaignKeywordsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12Z\n\x07results\x18\x02 \x03(\x0b2I.google.ads.googleads.v19.services.MutateKeywordPlanCampaignKeywordResult"y\n&MutateKeywordPlanCampaignKeywordResult\x12O\n\rresource_name\x18\x01 \x01(\tB8\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeyword2\x92\x03\n!KeywordPlanCampaignKeywordService\x12\xa5\x02\n!MutateKeywordPlanCampaignKeywords\x12K.google.ads.googleads.v19.services.MutateKeywordPlanCampaignKeywordsRequest\x1aL.google.ads.googleads.v19.services.MutateKeywordPlanCampaignKeywordsResponse"e\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}/keywordPlanCampaignKeywords:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x92\x02\n%com.google.ads.googleads.v19.servicesB&KeywordPlanCampaignKeywordServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.keyword_plan_campaign_keyword_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB&KeywordPlanCampaignKeywordServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeyword'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeyword'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE'].methods_by_name['MutateKeywordPlanCampaignKeywords']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE'].methods_by_name['MutateKeywordPlanCampaignKeywords']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02F"A/v19/customers/{customer_id=*}/keywordPlanCampaignKeywords:mutate:\x01*'
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST']._serialized_start = 363
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSREQUEST']._serialized_end = 576
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDOPERATION']._serialized_start = 579
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDOPERATION']._serialized_end = 918
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSRESPONSE']._serialized_start = 921
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDSRESPONSE']._serialized_end = 1107
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDRESULT']._serialized_start = 1109
    _globals['_MUTATEKEYWORDPLANCAMPAIGNKEYWORDRESULT']._serialized_end = 1230
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE']._serialized_start = 1233
    _globals['_KEYWORDPLANCAMPAIGNKEYWORDSERVICE']._serialized_end = 1635