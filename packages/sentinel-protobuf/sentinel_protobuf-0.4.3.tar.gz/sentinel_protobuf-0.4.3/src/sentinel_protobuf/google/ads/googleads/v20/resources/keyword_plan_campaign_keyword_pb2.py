"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/keyword_plan_campaign_keyword.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import keyword_match_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_keyword__match__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v20/resources/keyword_plan_campaign_keyword.proto\x12"google.ads.googleads.v20.resources\x1a7google/ads/googleads/v20/enums/keyword_match_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb2\x04\n\x1aKeywordPlanCampaignKeyword\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x05\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeyword\x12U\n\x15keyword_plan_campaign\x18\x08 \x01(\tB1\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaignH\x00\x88\x01\x01\x12\x14\n\x02id\x18\t \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04text\x18\n \x01(\tH\x02\x88\x01\x01\x12Y\n\nmatch_type\x18\x05 \x01(\x0e2E.google.ads.googleads.v20.enums.KeywordMatchTypeEnum.KeywordMatchType\x12\x1a\n\x08negative\x18\x0b \x01(\x08B\x03\xe0A\x05H\x03\x88\x01\x01:\x91\x01\xeaA\x8d\x01\n3googleads.googleapis.com/KeywordPlanCampaignKeyword\x12Vcustomers/{customer_id}/keywordPlanCampaignKeywords/{keyword_plan_campaign_keyword_id}B\x18\n\x16_keyword_plan_campaignB\x05\n\x03_idB\x07\n\x05_textB\x0b\n\t_negativeB\x91\x02\n&com.google.ads.googleads.v20.resourcesB\x1fKeywordPlanCampaignKeywordProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.keyword_plan_campaign_keyword_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1fKeywordPlanCampaignKeywordProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA5\n3googleads.googleapis.com/KeywordPlanCampaignKeyword'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['keyword_plan_campaign']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['keyword_plan_campaign']._serialized_options = b'\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['id']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['negative']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD'].fields_by_name['negative']._serialized_options = b'\xe0A\x05'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD']._serialized_options = b'\xeaA\x8d\x01\n3googleads.googleapis.com/KeywordPlanCampaignKeyword\x12Vcustomers/{customer_id}/keywordPlanCampaignKeywords/{keyword_plan_campaign_keyword_id}'
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD']._serialized_start = 228
    _globals['_KEYWORDPLANCAMPAIGNKEYWORD']._serialized_end = 790