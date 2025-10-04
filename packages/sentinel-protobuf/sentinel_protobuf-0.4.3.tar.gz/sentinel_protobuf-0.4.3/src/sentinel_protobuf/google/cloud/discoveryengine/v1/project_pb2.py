"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/project.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/discoveryengine/v1/project.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x05\n\x07Project\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x19provision_completion_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12]\n\x11service_terms_map\x18\x04 \x03(\x0b2=.google.cloud.discoveryengine.v1.Project.ServiceTermsMapEntryB\x03\xe0A\x03\x1a\xb5\x02\n\x0cServiceTerms\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\x12J\n\x05state\x18\x04 \x01(\x0e2;.google.cloud.discoveryengine.v1.Project.ServiceTerms.State\x12/\n\x0baccept_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x120\n\x0cdecline_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp"Y\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x12\n\x0eTERMS_ACCEPTED\x10\x01\x12\x11\n\rTERMS_PENDING\x10\x02\x12\x12\n\x0eTERMS_DECLINED\x10\x03\x1am\n\x14ServiceTermsMapEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12D\n\x05value\x18\x02 \x01(\x0b25.google.cloud.discoveryengine.v1.Project.ServiceTerms:\x028\x01:?\xeaA<\n&discoveryengine.googleapis.com/Project\x12\x12projects/{project}B\xff\x01\n#com.google.cloud.discoveryengine.v1B\x0cProjectProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0cProjectProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_PROJECT_SERVICETERMSMAPENTRY']._loaded_options = None
    _globals['_PROJECT_SERVICETERMSMAPENTRY']._serialized_options = b'8\x01'
    _globals['_PROJECT'].fields_by_name['name']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['create_time']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['provision_completion_time']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['provision_completion_time']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['service_terms_map']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['service_terms_map']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT']._loaded_options = None
    _globals['_PROJECT']._serialized_options = b'\xeaA<\n&discoveryengine.googleapis.com/Project\x12\x12projects/{project}'
    _globals['_PROJECT']._serialized_start = 176
    _globals['_PROJECT']._serialized_end = 909
    _globals['_PROJECT_SERVICETERMS']._serialized_start = 424
    _globals['_PROJECT_SERVICETERMS']._serialized_end = 733
    _globals['_PROJECT_SERVICETERMS_STATE']._serialized_start = 644
    _globals['_PROJECT_SERVICETERMS_STATE']._serialized_end = 733
    _globals['_PROJECT_SERVICETERMSMAPENTRY']._serialized_start = 735
    _globals['_PROJECT_SERVICETERMSMAPENTRY']._serialized_end = 844