"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/campaign_shared_set.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import campaign_shared_set_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_campaign__shared__set__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v20/resources/campaign_shared_set.proto\x12"google.ads.googleads.v20.resources\x1a?google/ads/googleads/v20/enums/campaign_shared_set_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe6\x03\n\x11CampaignSharedSet\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x05\xfaA,\n*googleads.googleapis.com/CampaignSharedSet\x12@\n\x08campaign\x18\x05 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CampaignH\x00\x88\x01\x01\x12C\n\nshared_set\x18\x06 \x01(\tB*\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSetH\x01\x88\x01\x01\x12h\n\x06status\x18\x02 \x01(\x0e2S.google.ads.googleads.v20.enums.CampaignSharedSetStatusEnum.CampaignSharedSetStatusB\x03\xe0A\x03:y\xeaAv\n*googleads.googleapis.com/CampaignSharedSet\x12Hcustomers/{customer_id}/campaignSharedSets/{campaign_id}~{shared_set_id}B\x0b\n\t_campaignB\r\n\x0b_shared_setB\x88\x02\n&com.google.ads.googleads.v20.resourcesB\x16CampaignSharedSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.campaign_shared_set_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x16CampaignSharedSetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA,\n*googleads.googleapis.com/CampaignSharedSet'
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['shared_set']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['shared_set']._serialized_options = b'\xe0A\x05\xfaA$\n"googleads.googleapis.com/SharedSet'
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['status']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSHAREDSET']._loaded_options = None
    _globals['_CAMPAIGNSHAREDSET']._serialized_options = b'\xeaAv\n*googleads.googleapis.com/CampaignSharedSet\x12Hcustomers/{customer_id}/campaignSharedSets/{campaign_id}~{shared_set_id}'
    _globals['_CAMPAIGNSHAREDSET']._serialized_start = 226
    _globals['_CAMPAIGNSHAREDSET']._serialized_end = 712