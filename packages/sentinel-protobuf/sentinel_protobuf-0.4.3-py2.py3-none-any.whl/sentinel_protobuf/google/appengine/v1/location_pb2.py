"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/appengine/v1/location.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/appengine/v1/location.proto\x12\x13google.appengine.v1\x1a\x1fgoogle/api/field_behavior.proto"\x85\x01\n\x10LocationMetadata\x12&\n\x1estandard_environment_available\x18\x02 \x01(\x08\x12&\n\x1eflexible_environment_available\x18\x04 \x01(\x08\x12!\n\x14search_api_available\x18\x06 \x01(\x08B\x03\xe0A\x03B\xbe\x01\n\x17com.google.appengine.v1B\rLocationProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.appengine.v1.location_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.appengine.v1B\rLocationProtoP\x01Z;cloud.google.com/go/appengine/apiv1/appenginepb;appenginepb\xaa\x02\x19Google.Cloud.AppEngine.V1\xca\x02\x19Google\\Cloud\\AppEngine\\V1\xea\x02\x1cGoogle::Cloud::AppEngine::V1'
    _globals['_LOCATIONMETADATA'].fields_by_name['search_api_available']._loaded_options = None
    _globals['_LOCATIONMETADATA'].fields_by_name['search_api_available']._serialized_options = b'\xe0A\x03'
    _globals['_LOCATIONMETADATA']._serialized_start = 93
    _globals['_LOCATIONMETADATA']._serialized_end = 226