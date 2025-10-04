"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/session.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import answer_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_answer__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/discoveryengine/v1/session.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/answer.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc0\x08\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x07 \x01(\tB\x03\xe0A\x01\x12=\n\x05state\x18\x02 \x01(\x0e2..google.cloud.discoveryengine.v1.Session.State\x12\x16\n\x0euser_pseudo_id\x18\x03 \x01(\t\x12<\n\x05turns\x18\x04 \x03(\x0b2-.google.cloud.discoveryengine.v1.Session.Turn\x123\n\nstart_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x16\n\tis_pinned\x18\x08 \x01(\x08B\x03\xe0A\x01\x1a\xd7\x02\n\x04Turn\x12:\n\x05query\x18\x01 \x01(\x0b2&.google.cloud.discoveryengine.v1.QueryB\x03\xe0A\x01\x12=\n\x06answer\x18\x02 \x01(\tB-\xe0A\x01\xfaA\'\n%discoveryengine.googleapis.com/Answer\x12E\n\x0fdetailed_answer\x18\x07 \x01(\x0b2\'.google.cloud.discoveryengine.v1.AnswerB\x03\xe0A\x03\x12Y\n\x0cquery_config\x18\x10 \x03(\x0b2>.google.cloud.discoveryengine.v1.Session.Turn.QueryConfigEntryB\x03\xe0A\x01\x1a2\n\x10QueryConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"/\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0f\n\x0bIN_PROGRESS\x10\x01:\xe6\x02\xeaA\xe2\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}*\x08sessions2\x07session"9\n\x05Query\x12\x0e\n\x04text\x18\x02 \x01(\tH\x00\x12\x15\n\x08query_id\x18\x01 \x01(\tB\x03\xe0A\x03B\t\n\x07contentB\xff\x01\n#com.google.cloud.discoveryengine.v1B\x0cSessionProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0cSessionProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._loaded_options = None
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_options = b'8\x01'
    _globals['_SESSION_TURN'].fields_by_name['query']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['query']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION_TURN'].fields_by_name['answer']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['answer']._serialized_options = b"\xe0A\x01\xfaA'\n%discoveryengine.googleapis.com/Answer"
    _globals['_SESSION_TURN'].fields_by_name['detailed_answer']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['detailed_answer']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION_TURN'].fields_by_name['query_config']._loaded_options = None
    _globals['_SESSION_TURN'].fields_by_name['query_config']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SESSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['start_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['end_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['is_pinned']._loaded_options = None
    _globals['_SESSION'].fields_by_name['is_pinned']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\xe2\x02\n&discoveryengine.googleapis.com/Session\x12Rprojects/{project}/locations/{location}/dataStores/{data_store}/sessions/{session}\x12kprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/sessions/{session}\x12dprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/sessions/{session}*\x08sessions2\x07session'
    _globals['_QUERY'].fields_by_name['query_id']._loaded_options = None
    _globals['_QUERY'].fields_by_name['query_id']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION']._serialized_start = 222
    _globals['_SESSION']._serialized_end = 1310
    _globals['_SESSION_TURN']._serialized_start = 557
    _globals['_SESSION_TURN']._serialized_end = 900
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_start = 850
    _globals['_SESSION_TURN_QUERYCONFIGENTRY']._serialized_end = 900
    _globals['_SESSION_STATE']._serialized_start = 902
    _globals['_SESSION_STATE']._serialized_end = 949
    _globals['_QUERY']._serialized_start = 1312
    _globals['_QUERY']._serialized_end = 1369