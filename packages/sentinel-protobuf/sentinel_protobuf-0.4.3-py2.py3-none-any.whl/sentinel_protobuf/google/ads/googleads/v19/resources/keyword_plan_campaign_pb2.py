"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/keyword_plan_campaign.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import keyword_plan_network_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_keyword__plan__network__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v19/resources/keyword_plan_campaign.proto\x12"google.ads.googleads.v19.resources\x1a9google/ads/googleads/v19/enums/keyword_plan_network.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa2\x05\n\x13KeywordPlanCampaign\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign\x12D\n\x0ckeyword_plan\x18\t \x01(\tB)\xfaA&\n$googleads.googleapis.com/KeywordPlanH\x00\x88\x01\x01\x12\x14\n\x02id\x18\n \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0b \x01(\tH\x02\x88\x01\x01\x12J\n\x12language_constants\x18\x0c \x03(\tB.\xfaA+\n)googleads.googleapis.com/LanguageConstant\x12g\n\x14keyword_plan_network\x18\x06 \x01(\x0e2I.google.ads.googleads.v19.enums.KeywordPlanNetworkEnum.KeywordPlanNetwork\x12\x1b\n\x0ecpc_bid_micros\x18\r \x01(\x03H\x03\x88\x01\x01\x12M\n\x0bgeo_targets\x18\x08 \x03(\x0b28.google.ads.googleads.v19.resources.KeywordPlanGeoTarget:z\xeaAw\n,googleads.googleapis.com/KeywordPlanCampaign\x12Gcustomers/{customer_id}/keywordPlanCampaigns/{keyword_plan_campaign_id}B\x0f\n\r_keyword_planB\x05\n\x03_idB\x07\n\x05_nameB\x11\n\x0f_cpc_bid_micros"\x81\x01\n\x14KeywordPlanGeoTarget\x12Q\n\x13geo_target_constant\x18\x02 \x01(\tB/\xfaA,\n*googleads.googleapis.com/GeoTargetConstantH\x00\x88\x01\x01B\x16\n\x14_geo_target_constantB\x8a\x02\n&com.google.ads.googleads.v19.resourcesB\x18KeywordPlanCampaignProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.keyword_plan_campaign_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x18KeywordPlanCampaignProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['resource_name']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/KeywordPlanCampaign'
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['keyword_plan']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['keyword_plan']._serialized_options = b'\xfaA&\n$googleads.googleapis.com/KeywordPlan'
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['id']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['language_constants']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGN'].fields_by_name['language_constants']._serialized_options = b'\xfaA+\n)googleads.googleapis.com/LanguageConstant'
    _globals['_KEYWORDPLANCAMPAIGN']._loaded_options = None
    _globals['_KEYWORDPLANCAMPAIGN']._serialized_options = b'\xeaAw\n,googleads.googleapis.com/KeywordPlanCampaign\x12Gcustomers/{customer_id}/keywordPlanCampaigns/{keyword_plan_campaign_id}'
    _globals['_KEYWORDPLANGEOTARGET'].fields_by_name['geo_target_constant']._loaded_options = None
    _globals['_KEYWORDPLANGEOTARGET'].fields_by_name['geo_target_constant']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/GeoTargetConstant'
    _globals['_KEYWORDPLANCAMPAIGN']._serialized_start = 222
    _globals['_KEYWORDPLANCAMPAIGN']._serialized_end = 896
    _globals['_KEYWORDPLANGEOTARGET']._serialized_start = 899
    _globals['_KEYWORDPLANGEOTARGET']._serialized_end = 1028