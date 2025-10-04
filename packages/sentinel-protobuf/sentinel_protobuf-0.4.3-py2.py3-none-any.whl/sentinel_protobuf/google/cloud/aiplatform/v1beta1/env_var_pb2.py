"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/env_var.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/env_var.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto"/\n\x06EnvVar\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02"1\n\tSecretRef\x12\x13\n\x06secret\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x0f\n\x07version\x18\x02 \x01(\t"f\n\x0cSecretEnvVar\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12C\n\nsecret_ref\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.SecretRefB\x03\xe0A\x02B\xe2\x01\n#com.google.cloud.aiplatform.v1beta1B\x0bEnvVarProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.env_var_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0bEnvVarProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_ENVVAR'].fields_by_name['name']._loaded_options = None
    _globals['_ENVVAR'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ENVVAR'].fields_by_name['value']._loaded_options = None
    _globals['_ENVVAR'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_SECRETREF'].fields_by_name['secret']._loaded_options = None
    _globals['_SECRETREF'].fields_by_name['secret']._serialized_options = b'\xe0A\x02'
    _globals['_SECRETENVVAR'].fields_by_name['name']._loaded_options = None
    _globals['_SECRETENVVAR'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SECRETENVVAR'].fields_by_name['secret_ref']._loaded_options = None
    _globals['_SECRETENVVAR'].fields_by_name['secret_ref']._serialized_options = b'\xe0A\x02'
    _globals['_ENVVAR']._serialized_start = 115
    _globals['_ENVVAR']._serialized_end = 162
    _globals['_SECRETREF']._serialized_start = 164
    _globals['_SECRETREF']._serialized_end = 213
    _globals['_SECRETENVVAR']._serialized_start = 215
    _globals['_SECRETENVVAR']._serialized_end = 317