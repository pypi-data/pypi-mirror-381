"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/model_evaluation.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_explanation__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/aiplatform/v1/model_evaluation.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/aiplatform/v1/explanation.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xeb\x05\n\x0fModelEvaluation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\n \x01(\t\x12\x1a\n\x12metrics_schema_uri\x18\x02 \x01(\t\x12\'\n\x07metrics\x18\x03 \x01(\x0b2\x16.google.protobuf.Value\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x10slice_dimensions\x18\x05 \x03(\t\x12\x1c\n\x14data_item_schema_uri\x18\x06 \x01(\t\x12\x1d\n\x15annotation_schema_uri\x18\x07 \x01(\t\x12G\n\x11model_explanation\x18\x08 \x01(\x0b2,.google.cloud.aiplatform.v1.ModelExplanation\x12e\n\x11explanation_specs\x18\t \x03(\x0b2J.google.cloud.aiplatform.v1.ModelEvaluation.ModelEvaluationExplanationSpec\x12(\n\x08metadata\x18\x0b \x01(\x0b2\x16.google.protobuf.Value\x1a\x81\x01\n\x1eModelEvaluationExplanationSpec\x12\x18\n\x10explanation_type\x18\x01 \x01(\t\x12E\n\x10explanation_spec\x18\x02 \x01(\x0b2+.google.cloud.aiplatform.v1.ExplanationSpec:\x7f\xeaA|\n)aiplatform.googleapis.com/ModelEvaluation\x12Oprojects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}B\xd2\x01\n\x1ecom.google.cloud.aiplatform.v1B\x14ModelEvaluationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.model_evaluation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x14ModelEvaluationProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_MODELEVALUATION'].fields_by_name['name']._loaded_options = None
    _globals['_MODELEVALUATION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELEVALUATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATION']._loaded_options = None
    _globals['_MODELEVALUATION']._serialized_options = b'\xeaA|\n)aiplatform.googleapis.com/ModelEvaluation\x12Oprojects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}'
    _globals['_MODELEVALUATION']._serialized_start = 251
    _globals['_MODELEVALUATION']._serialized_end = 998
    _globals['_MODELEVALUATION_MODELEVALUATIONEXPLANATIONSPEC']._serialized_start = 740
    _globals['_MODELEVALUATION_MODELEVALUATIONEXPLANATIONSPEC']._serialized_end = 869