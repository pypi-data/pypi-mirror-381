"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/notebook_idle_shutdown_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/aiplatform/v1beta1/notebook_idle_shutdown_config.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1egoogle/protobuf/duration.proto"r\n\x1aNotebookIdleShutdownConfig\x124\n\x0cidle_timeout\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x12\x1e\n\x16idle_shutdown_disabled\x18\x02 \x01(\x08B\xf6\x01\n#com.google.cloud.aiplatform.v1beta1B\x1fNotebookIdleShutdownConfigProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.notebook_idle_shutdown_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1fNotebookIdleShutdownConfigProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_NOTEBOOKIDLESHUTDOWNCONFIG'].fields_by_name['idle_timeout']._loaded_options = None
    _globals['_NOTEBOOKIDLESHUTDOWNCONFIG'].fields_by_name['idle_timeout']._serialized_options = b'\xe0A\x02'
    _globals['_NOTEBOOKIDLESHUTDOWNCONFIG']._serialized_start = 169
    _globals['_NOTEBOOKIDLESHUTDOWNCONFIG']._serialized_end = 283