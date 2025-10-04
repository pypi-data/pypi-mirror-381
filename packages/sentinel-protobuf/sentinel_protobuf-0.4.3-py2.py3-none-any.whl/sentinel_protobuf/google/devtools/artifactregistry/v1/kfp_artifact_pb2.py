"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/devtools/artifactregistry/v1/kfp_artifact.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/devtools/artifactregistry/v1/kfp_artifact.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xc4\x01\n\x0bKfpArtifact\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x07version\x18\x02 \x01(\t:\x90\x01\xeaA\x8c\x01\n+artifactregistry.googleapis.com/KfpArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/kfpArtifacts/{kfp_artifact}B\xfb\x01\n\'com.google.devtools.artifactregistry.v1B\x10KfpArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.kfp_artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\x10KfpArtifactProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_KFPARTIFACT'].fields_by_name['name']._loaded_options = None
    _globals['_KFPARTIFACT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_KFPARTIFACT']._loaded_options = None
    _globals['_KFPARTIFACT']._serialized_options = b'\xeaA\x8c\x01\n+artifactregistry.googleapis.com/KfpArtifact\x12]projects/{project}/locations/{location}/repositories/{repository}/kfpArtifacts/{kfp_artifact}'
    _globals['_KFPARTIFACT']._serialized_start = 156
    _globals['_KFPARTIFACT']._serialized_end = 352