"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/local_services_lead_conversation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import local_services_conversation_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__conversation__type__pb2
from ......google.ads.googleads.v21.enums import local_services_participant_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__participant__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nIgoogle/ads/googleads/v21/resources/local_services_lead_conversation.proto\x12"google.ads.googleads.v21.resources\x1aEgoogle/ads/googleads/v21/enums/local_services_conversation_type.proto\x1aDgoogle/ads/googleads/v21/enums/local_services_participant_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xce\x06\n\x1dLocalServicesLeadConversation\x12U\n\rresource_name\x18\x01 \x01(\tB>\xe0A\x03\xfaA8\n6googleads.googleapis.com/LocalServicesLeadConversation\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12y\n\x14conversation_channel\x18\x03 \x01(\x0e2V.google.ads.googleads.v21.enums.LocalServicesLeadConversationTypeEnum.ConversationTypeB\x03\xe0A\x03\x12o\n\x10participant_type\x18\x04 \x01(\x0e2P.google.ads.googleads.v21.enums.LocalServicesParticipantTypeEnum.ParticipantTypeB\x03\xe0A\x03\x12@\n\x04lead\x18\x05 \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/LocalServicesLead\x12\x1c\n\x0fevent_date_time\x18\x06 \x01(\tB\x03\xe0A\x03\x12Z\n\x12phone_call_details\x18\x07 \x01(\x0b24.google.ads.googleads.v21.resources.PhoneCallDetailsB\x03\xe0A\x03H\x00\x88\x01\x01\x12U\n\x0fmessage_details\x18\x08 \x01(\x0b22.google.ads.googleads.v21.resources.MessageDetailsB\x03\xe0A\x03H\x01\x88\x01\x01:\x9a\x01\xeaA\x96\x01\n6googleads.googleapis.com/LocalServicesLeadConversation\x12\\customers/{customer_id}/localServicesLeadConversations/{local_services_lead_conversation_id}B\x15\n\x13_phone_call_detailsB\x12\n\x10_message_details"V\n\x10PhoneCallDetails\x12!\n\x14call_duration_millis\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12call_recording_url\x18\x02 \x01(\tB\x03\xe0A\x03"A\n\x0eMessageDetails\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x1c\n\x0fattachment_urls\x18\x02 \x03(\tB\x03\xe0A\x03B\x94\x02\n&com.google.ads.googleads.v21.resourcesB"LocalServicesLeadConversationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.local_services_lead_conversation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB"LocalServicesLeadConversationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA8\n6googleads.googleapis.com/LocalServicesLeadConversation'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['id']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['conversation_channel']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['conversation_channel']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['participant_type']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['participant_type']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['lead']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['lead']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/LocalServicesLead'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['event_date_time']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['event_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['phone_call_details']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['phone_call_details']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['message_details']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION'].fields_by_name['message_details']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION']._loaded_options = None
    _globals['_LOCALSERVICESLEADCONVERSATION']._serialized_options = b'\xeaA\x96\x01\n6googleads.googleapis.com/LocalServicesLeadConversation\x12\\customers/{customer_id}/localServicesLeadConversations/{local_services_lead_conversation_id}'
    _globals['_PHONECALLDETAILS'].fields_by_name['call_duration_millis']._loaded_options = None
    _globals['_PHONECALLDETAILS'].fields_by_name['call_duration_millis']._serialized_options = b'\xe0A\x03'
    _globals['_PHONECALLDETAILS'].fields_by_name['call_recording_url']._loaded_options = None
    _globals['_PHONECALLDETAILS'].fields_by_name['call_recording_url']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEDETAILS'].fields_by_name['text']._loaded_options = None
    _globals['_MESSAGEDETAILS'].fields_by_name['text']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGEDETAILS'].fields_by_name['attachment_urls']._loaded_options = None
    _globals['_MESSAGEDETAILS'].fields_by_name['attachment_urls']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEADCONVERSATION']._serialized_start = 315
    _globals['_LOCALSERVICESLEADCONVERSATION']._serialized_end = 1161
    _globals['_PHONECALLDETAILS']._serialized_start = 1163
    _globals['_PHONECALLDETAILS']._serialized_end = 1249
    _globals['_MESSAGEDETAILS']._serialized_start = 1251
    _globals['_MESSAGEDETAILS']._serialized_end = 1316