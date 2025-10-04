"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/campaign_draft.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import campaign_draft_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_campaign__draft__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/resources/campaign_draft.proto\x12"google.ads.googleads.v19.resources\x1a:google/ads/googleads/v19/enums/campaign_draft_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xae\x05\n\rCampaignDraft\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x05\xfaA(\n&googleads.googleapis.com/CampaignDraft\x12\x1a\n\x08draft_id\x18\t \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12E\n\rbase_campaign\x18\n \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/CampaignH\x01\x88\x01\x01\x12\x11\n\x04name\x18\x0b \x01(\tH\x02\x88\x01\x01\x12F\n\x0edraft_campaign\x18\x0c \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CampaignH\x03\x88\x01\x01\x12`\n\x06status\x18\x06 \x01(\x0e2K.google.ads.googleads.v19.enums.CampaignDraftStatusEnum.CampaignDraftStatusB\x03\xe0A\x03\x12(\n\x16has_experiment_running\x18\r \x01(\x08B\x03\xe0A\x03H\x04\x88\x01\x01\x12(\n\x16long_running_operation\x18\x0e \x01(\tB\x03\xe0A\x03H\x05\x88\x01\x01:q\xeaAn\n&googleads.googleapis.com/CampaignDraft\x12Dcustomers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}B\x0b\n\t_draft_idB\x10\n\x0e_base_campaignB\x07\n\x05_nameB\x11\n\x0f_draft_campaignB\x19\n\x17_has_experiment_runningB\x19\n\x17_long_running_operationB\x84\x02\n&com.google.ads.googleads.v19.resourcesB\x12CampaignDraftProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.campaign_draft_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x12CampaignDraftProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA(\n&googleads.googleapis.com/CampaignDraft'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['draft_id']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['draft_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['base_campaign']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['base_campaign']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['draft_campaign']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['draft_campaign']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['status']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['has_experiment_running']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['has_experiment_running']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNDRAFT'].fields_by_name['long_running_operation']._loaded_options = None
    _globals['_CAMPAIGNDRAFT'].fields_by_name['long_running_operation']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNDRAFT']._loaded_options = None
    _globals['_CAMPAIGNDRAFT']._serialized_options = b'\xeaAn\n&googleads.googleapis.com/CampaignDraft\x12Dcustomers/{customer_id}/campaignDrafts/{base_campaign_id}~{draft_id}'
    _globals['_CAMPAIGNDRAFT']._serialized_start = 216
    _globals['_CAMPAIGNDRAFT']._serialized_end = 902