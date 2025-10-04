"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/assistant.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/discoveryengine/v1/assistant.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb9\x01\n\tAssistant\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05:\x98\x01\xeaA\x94\x01\n(discoveryengine.googleapis.com/Assistant\x12hprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}B\x81\x02\n#com.google.cloud.discoveryengine.v1B\x0eAssistantProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.assistant_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0eAssistantProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_ASSISTANT'].fields_by_name['name']._loaded_options = None
    _globals['_ASSISTANT'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_ASSISTANT']._loaded_options = None
    _globals['_ASSISTANT']._serialized_options = b'\xeaA\x94\x01\n(discoveryengine.googleapis.com/Assistant\x12hprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/assistants/{assistant}'
    _globals['_ASSISTANT']._serialized_start = 145
    _globals['_ASSISTANT']._serialized_end = 330