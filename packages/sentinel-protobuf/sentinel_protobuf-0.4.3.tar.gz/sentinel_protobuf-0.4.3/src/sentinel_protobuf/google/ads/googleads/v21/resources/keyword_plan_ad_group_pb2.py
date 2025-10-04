"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/keyword_plan_ad_group.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v21/resources/keyword_plan_ad_group.proto\x12"google.ads.googleads.v21.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb4\x03\n\x12KeywordPlanAdGroup\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/KeywordPlanAdGroup\x12U\n\x15keyword_plan_campaign\x18\x06 \x01(\tB1\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaignH\x00\x88\x01\x01\x12\x14\n\x02id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x08 \x01(\tH\x02\x88\x01\x01\x12\x1b\n\x0ecpc_bid_micros\x18\t \x01(\x03H\x03\x88\x01\x01:x\xeaAu\n+googleads.googleapis.com/KeywordPlanAdGroup\x12Fcustomers/{customer_id}/keywordPlanAdGroups/{keyword_plan_ad_group_id}B\x18\n\x16_keyword_plan_campaignB\x05\n\x03_idB\x07\n\x05_nameB\x11\n\x0f_cpc_bid_microsB\x89\x02\n&com.google.ads.googleads.v21.resourcesB\x17KeywordPlanAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.keyword_plan_ad_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x17KeywordPlanAdGroupProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['resource_name']._loaded_options = None
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/KeywordPlanAdGroup'
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['keyword_plan_campaign']._loaded_options = None
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['keyword_plan_campaign']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign'
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['id']._loaded_options = None
    _globals['_KEYWORDPLANADGROUP'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_KEYWORDPLANADGROUP']._loaded_options = None
    _globals['_KEYWORDPLANADGROUP']._serialized_options = b'\xeaAu\n+googleads.googleapis.com/KeywordPlanAdGroup\x12Fcustomers/{customer_id}/keywordPlanAdGroups/{keyword_plan_ad_group_id}'
    _globals['_KEYWORDPLANADGROUP']._serialized_start = 163
    _globals['_KEYWORDPLANADGROUP']._serialized_end = 599