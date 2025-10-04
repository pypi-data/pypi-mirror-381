"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/actor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/support/v2beta/actor.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1fgoogle/api/field_behavior.proto"d\n\x05Actor\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x11\n\x05email\x18\x02 \x01(\tB\x02\x18\x01\x12\x1b\n\x0egoogle_support\x18\x04 \x01(\x08B\x03\xe0A\x03\x12\x15\n\x08username\x18\x05 \x01(\tB\x03\xe0A\x03B\xc7\x01\n\x1fcom.google.cloud.support.v2betaB\nActorProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.actor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\nActorProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_ACTOR'].fields_by_name['email']._loaded_options = None
    _globals['_ACTOR'].fields_by_name['email']._serialized_options = b'\x18\x01'
    _globals['_ACTOR'].fields_by_name['google_support']._loaded_options = None
    _globals['_ACTOR'].fields_by_name['google_support']._serialized_options = b'\xe0A\x03'
    _globals['_ACTOR'].fields_by_name['username']._loaded_options = None
    _globals['_ACTOR'].fields_by_name['username']._serialized_options = b'\xe0A\x03'
    _globals['_ACTOR']._serialized_start = 105
    _globals['_ACTOR']._serialized_end = 205