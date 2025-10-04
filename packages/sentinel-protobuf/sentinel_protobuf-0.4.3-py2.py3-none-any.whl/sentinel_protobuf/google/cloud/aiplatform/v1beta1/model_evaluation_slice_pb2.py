"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_evaluation_slice.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/aiplatform/v1beta1/model_evaluation_slice.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto"\xe0\t\n\x14ModelEvaluationSlice\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12O\n\x05slice\x18\x02 \x01(\x0b2;.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.SliceB\x03\xe0A\x03\x12\x1f\n\x12metrics_schema_uri\x18\x03 \x01(\tB\x03\xe0A\x03\x12,\n\x07metrics\x18\x04 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Q\n\x11model_explanation\x18\x06 \x01(\x0b21.google.cloud.aiplatform.v1beta1.ModelExplanationB\x03\xe0A\x03\x1a\xf4\x05\n\x05Slice\x12\x16\n\tdimension\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x03\x12^\n\nslice_spec\x18\x03 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpecB\x03\xe0A\x03\x1a\xde\x04\n\tSliceSpec\x12c\n\x07configs\x18\x01 \x03(\x0b2R.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpec.ConfigsEntry\x1a\x83\x02\n\x0bSliceConfig\x12\\\n\x05value\x18\x01 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpec.ValueH\x00\x12\\\n\x05range\x18\x02 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpec.RangeH\x00\x120\n\nall_values\x18\x03 \x01(\x0b2\x1a.google.protobuf.BoolValueH\x00B\x06\n\x04kind\x1a"\n\x05Range\x12\x0b\n\x03low\x18\x01 \x01(\x02\x12\x0c\n\x04high\x18\x02 \x01(\x02\x1a>\n\x05Value\x12\x16\n\x0cstring_value\x18\x01 \x01(\tH\x00\x12\x15\n\x0bfloat_value\x18\x02 \x01(\x02H\x00B\x06\n\x04kind\x1a\x81\x01\n\x0cConfigsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12`\n\x05value\x18\x02 \x01(\x0b2Q.google.cloud.aiplatform.v1beta1.ModelEvaluationSlice.Slice.SliceSpec.SliceConfig:\x028\x01:\x94\x01\xeaA\x90\x01\n.aiplatform.googleapis.com/ModelEvaluationSlice\x12^projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}B\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19ModelEvaluationSliceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_evaluation_slice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19ModelEvaluationSliceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_CONFIGSENTRY']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_CONFIGSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['dimension']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['dimension']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['value']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['value']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['slice_spec']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE_SLICE'].fields_by_name['slice_spec']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['name']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['slice']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['slice']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['metrics_schema_uri']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['metrics_schema_uri']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['metrics']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['metrics']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['model_explanation']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE'].fields_by_name['model_explanation']._serialized_options = b'\xe0A\x03'
    _globals['_MODELEVALUATIONSLICE']._loaded_options = None
    _globals['_MODELEVALUATIONSLICE']._serialized_options = b'\xeaA\x90\x01\n.aiplatform.googleapis.com/ModelEvaluationSlice\x12^projects/{project}/locations/{location}/models/{model}/evaluations/{evaluation}/slices/{slice}'
    _globals['_MODELEVALUATIONSLICE']._serialized_start = 304
    _globals['_MODELEVALUATIONSLICE']._serialized_end = 1552
    _globals['_MODELEVALUATIONSLICE_SLICE']._serialized_start = 645
    _globals['_MODELEVALUATIONSLICE_SLICE']._serialized_end = 1401
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC']._serialized_start = 795
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC']._serialized_end = 1401
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_SLICECONFIG']._serialized_start = 910
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_SLICECONFIG']._serialized_end = 1169
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_RANGE']._serialized_start = 1171
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_RANGE']._serialized_end = 1205
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_VALUE']._serialized_start = 1207
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_VALUE']._serialized_end = 1269
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_CONFIGSENTRY']._serialized_start = 1272
    _globals['_MODELEVALUATIONSLICE_SLICE_SLICESPEC_CONFIGSENTRY']._serialized_end = 1401