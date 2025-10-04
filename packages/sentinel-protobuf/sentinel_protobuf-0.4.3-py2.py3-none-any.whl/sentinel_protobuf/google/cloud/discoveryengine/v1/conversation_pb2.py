"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/conversation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import search_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_search__service__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/discoveryengine/v1/conversation.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/discoveryengine/v1/search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe6\x05\n\x0cConversation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12B\n\x05state\x18\x02 \x01(\x0e23.google.cloud.discoveryengine.v1.Conversation.State\x12\x16\n\x0euser_pseudo_id\x18\x03 \x01(\t\x12F\n\x08messages\x18\x04 \x03(\x0b24.google.cloud.discoveryengine.v1.ConversationMessage\x123\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03">\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01\x12\r\n\tCOMPLETED\x10\x02:\xf6\x02\xeaA\xf2\x02\n+discoveryengine.googleapis.com/Conversation\x12\\projects/{project}/locations/{location}/dataStores/{data_store}/conversations/{conversation}\x12uprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/conversations/{conversation}\x12nprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/conversations/{conversation}"Q\n\x05Reply\x12H\n\x07summary\x18\x03 \x01(\x0b27.google.cloud.discoveryengine.v1.SearchResponse.Summary"I\n\x13ConversationContext\x12\x19\n\x11context_documents\x18\x01 \x03(\t\x12\x17\n\x0factive_document\x18\x02 \x01(\t"a\n\tTextInput\x12\r\n\x05input\x18\x01 \x01(\t\x12E\n\x07context\x18\x02 \x01(\x0b24.google.cloud.discoveryengine.v1.ConversationContext"\xd1\x01\n\x13ConversationMessage\x12@\n\nuser_input\x18\x01 \x01(\x0b2*.google.cloud.discoveryengine.v1.TextInputH\x00\x127\n\x05reply\x18\x02 \x01(\x0b2&.google.cloud.discoveryengine.v1.ReplyH\x00\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\t\n\x07messageB\x84\x02\n#com.google.cloud.discoveryengine.v1B\x11ConversationProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.conversation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x11ConversationProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CONVERSATION'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_CONVERSATION'].fields_by_name['start_time']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATION'].fields_by_name['end_time']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATION']._loaded_options = None
    _globals['_CONVERSATION']._serialized_options = b'\xeaA\xf2\x02\n+discoveryengine.googleapis.com/Conversation\x12\\projects/{project}/locations/{location}/dataStores/{data_store}/conversations/{conversation}\x12uprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/conversations/{conversation}\x12nprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/conversations/{conversation}'
    _globals['_CONVERSATIONMESSAGE'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONVERSATIONMESSAGE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATION']._serialized_start = 235
    _globals['_CONVERSATION']._serialized_end = 977
    _globals['_CONVERSATION_STATE']._serialized_start = 538
    _globals['_CONVERSATION_STATE']._serialized_end = 600
    _globals['_REPLY']._serialized_start = 979
    _globals['_REPLY']._serialized_end = 1060
    _globals['_CONVERSATIONCONTEXT']._serialized_start = 1062
    _globals['_CONVERSATIONCONTEXT']._serialized_end = 1135
    _globals['_TEXTINPUT']._serialized_start = 1137
    _globals['_TEXTINPUT']._serialized_end = 1234
    _globals['_CONVERSATIONMESSAGE']._serialized_start = 1237
    _globals['_CONVERSATIONMESSAGE']._serialized_end = 1446