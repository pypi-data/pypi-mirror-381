"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_evaluation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import model_evaluation_slice_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__evaluation__slice__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/model_evaluation.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a<google/cloud/aiplatform/v1beta1/model_evaluation_slice.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8a\x07\n\x0fModelEvaluation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\n \x01(\t\x12\x1a\n\x12metrics_schema_uri\x18\x02 \x01(\t\x12\'\n\x07metrics\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x10slice_dimensions\x18\x05 \x03(\t\x12L\n\x11model_explanation\x18\x08 \x01(\x0b21.google.cloud.aiplatform.v1beta1.ModelExplanation\x12j\n\x11explanation_specs\x18\t \x03(\x0b2O.google.cloud.aiplatform.v1beta1.ModelEvaluation.ModelEvaluationExplanationSpec\x12(\n\x08metadata\x18\x0b \x01(\x0b2\x16.google.protobuf.Value\x12Q\n\x0cbias_configs\x18\x0c \x01(\x0b2;.google.cloud.aiplatform.v1beta1.ModelEvaluation.BiasConfig\x1a\x86\x01\n\x1eModelEvaluationExplanationSpec\x12\x18\n\x10explanation_type\x18\x01 \x01(\t\x12J\n\x10explanation_spec\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x1ax\n\nBiasConfig\x12Z\n\x0bbias_slices\x18\x01 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpec\x12\x0e\n\x06labels\x18\x02 \x03(\t:\x7f\xeaA|\n)aiplatform.googleapis.com/ModelEvaluation\x12Oprojects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}B\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14ModelEvaluationProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14ModelEvaluationProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELEVALUATION'].fields_by_name['name']._loaded_options = None
    _globals['_MODELEVALUATION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELEVALUATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATION']._loaded_options = None
    _globals['_MODELEVALUATION']._serialized_options = b'\xeaA|\n)aiplatform.googleapis.com/ModelEvaluation\x12Oprojects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}'
    _globals['_MODELEVALUATION']._serialized_start = 328
    _globals['_MODELEVALUATION']._serialized_end = 1234
    _globals['_MODELEVALUATION_MODELEVALUATIONEXPLANATIONSPEC']._serialized_start = 849
    _globals['_MODELEVALUATION_MODELEVALUATIONEXPLANATIONSPEC']._serialized_end = 983
    _globals['_MODELEVALUATION_BIASCONFIG']._serialized_start = 985
    _globals['_MODELEVALUATION_BIASCONFIG']._serialized_end = 1105