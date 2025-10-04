"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/devtools/artifactregistry/v1/settings.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/devtools/artifactregistry/v1/settings.proto\x12#google.devtools.artifactregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\x88\x04\n\x0fProjectSettings\x12\x0c\n\x04name\x18\x01 \x01(\t\x12g\n\x18legacy_redirection_state\x18\x02 \x01(\x0e2E.google.devtools.artifactregistry.v1.ProjectSettings.RedirectionState\x12\x14\n\x0cpull_percent\x18\x03 \x01(\x05"\x8d\x02\n\x10RedirectionState\x12!\n\x1dREDIRECTION_STATE_UNSPECIFIED\x10\x00\x12$\n REDIRECTION_FROM_GCR_IO_DISABLED\x10\x01\x12#\n\x1fREDIRECTION_FROM_GCR_IO_ENABLED\x10\x02\x12)\n!REDIRECTION_FROM_GCR_IO_FINALIZED\x10\x03\x1a\x02\x08\x01\x12/\n+REDIRECTION_FROM_GCR_IO_ENABLED_AND_COPYING\x10\x05\x12/\n+REDIRECTION_FROM_GCR_IO_PARTIAL_AND_COPYING\x10\x06:X\xeaAU\n/artifactregistry.googleapis.com/ProjectSettings\x12"projects/{project}/projectSettings"b\n\x19GetProjectSettingsRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/artifactregistry.googleapis.com/ProjectSettings"\x9f\x01\n\x1cUpdateProjectSettingsRequest\x12N\n\x10project_settings\x18\x02 \x01(\x0b24.google.devtools.artifactregistry.v1.ProjectSettings\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\xf8\x01\n\'com.google.devtools.artifactregistry.v1B\rSettingsProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.devtools.artifactregistry.v1.settings_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.devtools.artifactregistry.v1B\rSettingsProtoP\x01ZPcloud.google.com/go/artifactregistry/apiv1/artifactregistrypb;artifactregistrypb\xaa\x02 Google.Cloud.ArtifactRegistry.V1\xca\x02 Google\\Cloud\\ArtifactRegistry\\V1\xea\x02#Google::Cloud::ArtifactRegistry::V1"
    _globals['_PROJECTSETTINGS_REDIRECTIONSTATE'].values_by_name['REDIRECTION_FROM_GCR_IO_FINALIZED']._loaded_options = None
    _globals['_PROJECTSETTINGS_REDIRECTIONSTATE'].values_by_name['REDIRECTION_FROM_GCR_IO_FINALIZED']._serialized_options = b'\x08\x01'
    _globals['_PROJECTSETTINGS']._loaded_options = None
    _globals['_PROJECTSETTINGS']._serialized_options = b'\xeaAU\n/artifactregistry.googleapis.com/ProjectSettings\x12"projects/{project}/projectSettings'
    _globals['_GETPROJECTSETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROJECTSETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/artifactregistry.googleapis.com/ProjectSettings'
    _globals['_PROJECTSETTINGS']._serialized_start = 186
    _globals['_PROJECTSETTINGS']._serialized_end = 706
    _globals['_PROJECTSETTINGS_REDIRECTIONSTATE']._serialized_start = 347
    _globals['_PROJECTSETTINGS_REDIRECTIONSTATE']._serialized_end = 616
    _globals['_GETPROJECTSETTINGSREQUEST']._serialized_start = 708
    _globals['_GETPROJECTSETTINGSREQUEST']._serialized_end = 806
    _globals['_UPDATEPROJECTSETTINGSREQUEST']._serialized_start = 809
    _globals['_UPDATEPROJECTSETTINGSREQUEST']._serialized_end = 968