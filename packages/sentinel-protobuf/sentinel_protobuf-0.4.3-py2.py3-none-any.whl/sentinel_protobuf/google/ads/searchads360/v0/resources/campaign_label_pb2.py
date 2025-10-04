"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/campaign_label.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/searchads360/v0/resources/campaign_label.proto\x12$google.ads.searchads360.v0.resources\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa1\x03\n\rCampaignLabel\x12H\n\rresource_name\x18\x01 \x01(\tB1\xe0A\x05\xfaA+\n)searchads360.googleapis.com/CampaignLabel\x12C\n\x08campaign\x18\x04 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/CampaignH\x00\x88\x01\x01\x12=\n\x05label\x18\x05 \x01(\tB)\xe0A\x05\xfaA#\n!searchads360.googleapis.com/LabelH\x01\x88\x01\x01\x12#\n\x11owner_customer_id\x18\x06 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01:p\xeaAm\n)searchads360.googleapis.com/CampaignLabel\x12@customers/{customer_id}/campaignLabels/{campaign_id}~{entity_id}B\x0b\n\t_campaignB\x08\n\x06_labelB\x14\n\x12_owner_customer_idB\x92\x02\n(com.google.ads.searchads360.v0.resourcesB\x12CampaignLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.campaign_label_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\x12CampaignLabelProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_CAMPAIGNLABEL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNLABEL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA+\n)searchads360.googleapis.com/CampaignLabel'
    _globals['_CAMPAIGNLABEL'].fields_by_name['campaign']._loaded_options = None
    _globals['_CAMPAIGNLABEL'].fields_by_name['campaign']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/Campaign'
    _globals['_CAMPAIGNLABEL'].fields_by_name['label']._loaded_options = None
    _globals['_CAMPAIGNLABEL'].fields_by_name['label']._serialized_options = b'\xe0A\x05\xfaA#\n!searchads360.googleapis.com/Label'
    _globals['_CAMPAIGNLABEL'].fields_by_name['owner_customer_id']._loaded_options = None
    _globals['_CAMPAIGNLABEL'].fields_by_name['owner_customer_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNLABEL']._loaded_options = None
    _globals['_CAMPAIGNLABEL']._serialized_options = b'\xeaAm\n)searchads360.googleapis.com/CampaignLabel\x12@customers/{customer_id}/campaignLabels/{campaign_id}~{entity_id}'
    _globals['_CAMPAIGNLABEL']._serialized_start = 160
    _globals['_CAMPAIGNLABEL']._serialized_end = 577