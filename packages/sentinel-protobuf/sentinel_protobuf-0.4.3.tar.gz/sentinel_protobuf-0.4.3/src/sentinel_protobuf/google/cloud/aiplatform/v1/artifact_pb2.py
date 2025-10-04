"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/artifact.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/aiplatform/v1/artifact.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x05\n\x08Artifact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12\x0b\n\x03uri\x18\x06 \x01(\t\x12\x0c\n\x04etag\x18\t \x01(\t\x12@\n\x06labels\x18\n \x03(\x0b20.google.cloud.aiplatform.v1.Artifact.LabelsEntry\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x05state\x18\r \x01(\x0e2*.google.cloud.aiplatform.v1.Artifact.State\x12\x14\n\x0cschema_title\x18\x0e \x01(\t\x12\x16\n\x0eschema_version\x18\x0f \x01(\t\x12)\n\x08metadata\x18\x10 \x01(\x0b2\x17.google.protobuf.Struct\x12\x13\n\x0bdescription\x18\x11 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"5\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x08\n\x04LIVE\x10\x02:\x86\x01\xeaA\x82\x01\n"aiplatform.googleapis.com/Artifact\x12\\projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}B\xcb\x01\n\x1ecom.google.cloud.aiplatform.v1B\rArtifactProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\rArtifactProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_ARTIFACT_LABELSENTRY']._loaded_options = None
    _globals['_ARTIFACT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ARTIFACT'].fields_by_name['name']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['create_time']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ARTIFACT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ARTIFACT']._loaded_options = None
    _globals['_ARTIFACT']._serialized_options = b'\xeaA\x82\x01\n"aiplatform.googleapis.com/Artifact\x12\\projects/{project}/locations/{location}/metadataStores/{metadata_store}/artifacts/{artifact}'
    _globals['_ARTIFACT']._serialized_start = 197
    _globals['_ARTIFACT']._serialized_end = 857
    _globals['_ARTIFACT_LABELSENTRY']._serialized_start = 620
    _globals['_ARTIFACT_LABELSENTRY']._serialized_end = 665
    _globals['_ARTIFACT_STATE']._serialized_start = 667
    _globals['_ARTIFACT_STATE']._serialized_end = 720