"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/campaign_bid_modifier.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import criteria_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_criteria__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/ads/googleads/v20/resources/campaign_bid_modifier.proto\x12"google.ads.googleads.v20.resources\x1a.google/ads/googleads/v20/common/criteria.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xf0\x03\n\x13CampaignBidModifier\x12K\n\rresource_name\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,googleads.googleapis.com/CampaignBidModifier\x12@\n\x08campaign\x18\x06 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x19\n\x0cbid_modifier\x18\x08 \x01(\x01H\x03\x88\x01\x01\x12U\n\x10interaction_type\x18\x05 \x01(\x0b24.google.ads.googleads.v20.common.InteractionTypeInfoB\x03\xe0A\x05H\x00:|\xeaAy\n,googleads.googleapis.com/CampaignBidModifier\x12Icustomers/{customer_id}/campaignBidModifiers/{campaign_id}~{criterion_id}B\x0b\n\tcriterionB\x0b\n\t_campaignB\x0f\n\r_criterion_idB\x0f\n\r_bid_modifierB\x8a\x02\n&com.google.ads.googleads.v20.resourcesB\x18CampaignBidModifierProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.campaign_bid_modifier_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x18CampaignBidModifierProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA.\n,googleads.googleapis.com/CampaignBidModifier'
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['interaction_type']._loaded_options = None
    _globals['_CAMPAIGNBIDMODIFIER'].fields_by_name['interaction_type']._serialized_options = b'\xe0A\x05'
    _globals['_CAMPAIGNBIDMODIFIER']._loaded_options = None
    _globals['_CAMPAIGNBIDMODIFIER']._serialized_options = b'\xeaAy\n,googleads.googleapis.com/CampaignBidModifier\x12Icustomers/{customer_id}/campaignBidModifiers/{campaign_id}~{criterion_id}'
    _globals['_CAMPAIGNBIDMODIFIER']._serialized_start = 211
    _globals['_CAMPAIGNBIDMODIFIER']._serialized_end = 707