"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/unmanaged_container_model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1beta1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/aiplatform/v1beta1/unmanaged_container_model.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a+google/cloud/aiplatform/v1beta1/model.proto"\xcd\x01\n\x17UnmanagedContainerModel\x12\x14\n\x0cartifact_uri\x18\x01 \x01(\t\x12J\n\x10predict_schemata\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1beta1.PredictSchemata\x12P\n\x0econtainer_spec\x18\x03 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ModelContainerSpecB\x03\xe0A\x04B\xf3\x01\n#com.google.cloud.aiplatform.v1beta1B\x1cUnmanagedContainerModelProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.unmanaged_container_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1cUnmanagedContainerModelProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_UNMANAGEDCONTAINERMODEL'].fields_by_name['container_spec']._loaded_options = None
    _globals['_UNMANAGEDCONTAINERMODEL'].fields_by_name['container_spec']._serialized_options = b'\xe0A\x04'
    _globals['_UNMANAGEDCONTAINERMODEL']._serialized_start = 179
    _globals['_UNMANAGEDCONTAINERMODEL']._serialized_end = 384