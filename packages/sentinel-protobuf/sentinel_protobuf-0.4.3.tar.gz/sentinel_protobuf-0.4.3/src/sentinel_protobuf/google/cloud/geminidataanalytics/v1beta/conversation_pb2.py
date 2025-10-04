"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/conversation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/geminidataanalytics/v1beta/conversation.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xca\x03\n\x0cConversation\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x01\xe0A\x08\x12\x13\n\x06agents\x18\x02 \x03(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x127\n\x0elast_used_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12V\n\x06labels\x18\t \x03(\x0b2A.google.cloud.geminidataanalytics.v1beta.Conversation.LabelsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x98\x01\xeaA\x94\x01\n/geminidataanalytics.googleapis.com/Conversation\x12Dprojects/{project}/locations/{location}/conversations/{conversation}*\rconversations2\x0cconversation"\xf5\x01\n\x19CreateConversationRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/geminidataanalytics.googleapis.com/Conversation\x12\x1c\n\x0fconversation_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12P\n\x0cconversation\x18\x03 \x01(\x0b25.google.cloud.geminidataanalytics.v1beta.ConversationB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"_\n\x16GetConversationRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation"\xa9\x01\n\x18ListConversationsRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\x12/geminidataanalytics.googleapis.com/Conversation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x19ListConversationsResponse\x12L\n\rconversations\x18\x01 \x03(\x0b25.google.cloud.geminidataanalytics.v1beta.Conversation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\tB\xa2\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x11ConversationProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.conversation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x11ConversationProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_CONVERSATION_LABELSENTRY']._loaded_options = None
    _globals['_CONVERSATION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_CONVERSATION'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['name']._serialized_options = b'\xe0A\x01\xe0A\x08'
    _globals['_CONVERSATION'].fields_by_name['agents']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['agents']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATION'].fields_by_name['last_used_time']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['last_used_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATION'].fields_by_name['labels']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATION']._loaded_options = None
    _globals['_CONVERSATION']._serialized_options = b'\xeaA\x94\x01\n/geminidataanalytics.googleapis.com/Conversation\x12Dprojects/{project}/locations/{location}/conversations/{conversation}*\rconversations2\x0cconversation'
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/geminidataanalytics.googleapis.com/Conversation'
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['conversation_id']._loaded_options = None
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['conversation_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['conversation']._loaded_options = None
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['conversation']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATECONVERSATIONREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GETCONVERSATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONVERSATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\x12/geminidataanalytics.googleapis.com/Conversation'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCONVERSATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATION']._serialized_start = 226
    _globals['_CONVERSATION']._serialized_end = 684
    _globals['_CONVERSATION_LABELSENTRY']._serialized_start = 484
    _globals['_CONVERSATION_LABELSENTRY']._serialized_end = 529
    _globals['_CREATECONVERSATIONREQUEST']._serialized_start = 687
    _globals['_CREATECONVERSATIONREQUEST']._serialized_end = 932
    _globals['_GETCONVERSATIONREQUEST']._serialized_start = 934
    _globals['_GETCONVERSATIONREQUEST']._serialized_end = 1029
    _globals['_LISTCONVERSATIONSREQUEST']._serialized_start = 1032
    _globals['_LISTCONVERSATIONSREQUEST']._serialized_end = 1201
    _globals['_LISTCONVERSATIONSRESPONSE']._serialized_start = 1204
    _globals['_LISTCONVERSATIONSRESPONSE']._serialized_end = 1334