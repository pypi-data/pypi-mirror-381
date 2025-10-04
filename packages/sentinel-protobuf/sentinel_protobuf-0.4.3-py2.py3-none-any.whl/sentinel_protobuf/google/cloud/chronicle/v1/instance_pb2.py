"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/chronicle/v1/instance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/chronicle/v1/instance.proto\x12\x19google.cloud.chronicle.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x98\x01\n\x08Instance\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08:y\xeaAv\n!chronicle.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance"M\n\x12GetInstanceRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!chronicle.googleapis.com/Instance2\x81\x02\n\x0fInstanceService\x12\x9f\x01\n\x0bGetInstance\x12-.google.cloud.chronicle.v1.GetInstanceRequest\x1a#.google.cloud.chronicle.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x1aL\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc4\x01\n\x1dcom.google.cloud.chronicle.v1B\rInstanceProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.chronicle.v1.instance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.chronicle.v1B\rInstanceProtoP\x01Z;cloud.google.com/go/chronicle/apiv1/chroniclepb;chroniclepb\xaa\x02\x19Google.Cloud.Chronicle.V1\xca\x02\x19Google\\Cloud\\Chronicle\\V1\xea\x02\x1cGoogle::Cloud::Chronicle::V1'
    _globals['_INSTANCE'].fields_by_name['name']._loaded_options = None
    _globals['_INSTANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INSTANCE']._loaded_options = None
    _globals['_INSTANCE']._serialized_options = b'\xeaAv\n!chronicle.googleapis.com/Instance\x12<projects/{project}/locations/{location}/instances/{instance}*\tinstances2\x08instance'
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!chronicle.googleapis.com/Instance'
    _globals['_INSTANCESERVICE']._loaded_options = None
    _globals['_INSTANCESERVICE']._serialized_options = b'\xcaA\x18chronicle.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INSTANCESERVICE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_INSTANCESERVICE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_INSTANCE']._serialized_start = 187
    _globals['_INSTANCE']._serialized_end = 339
    _globals['_GETINSTANCEREQUEST']._serialized_start = 341
    _globals['_GETINSTANCEREQUEST']._serialized_end = 418
    _globals['_INSTANCESERVICE']._serialized_start = 421
    _globals['_INSTANCESERVICE']._serialized_end = 678