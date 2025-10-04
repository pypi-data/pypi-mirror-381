"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/data_foundry_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_content__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/data_foundry_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1/content.proto"\xdf\x02\n\x1cGenerateSyntheticDataRequest\x12O\n\x10task_description\x18\x03 \x01(\x0b23.google.cloud.aiplatform.v1.TaskDescriptionStrategyH\x00\x12;\n\x08location\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x12\n\x05count\x18\x02 \x01(\x05B\x03\xe0A\x02\x12L\n\x12output_field_specs\x18\x04 \x03(\x0b2+.google.cloud.aiplatform.v1.OutputFieldSpecB\x03\xe0A\x02\x12C\n\x08examples\x18\x05 \x03(\x0b2,.google.cloud.aiplatform.v1.SyntheticExampleB\x03\xe0A\x01B\n\n\x08strategy"d\n\x0eSyntheticField\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x01\x129\n\x07content\x18\x02 \x01(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x02"S\n\x10SyntheticExample\x12?\n\x06fields\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1.SyntheticFieldB\x03\xe0A\x02"\xe7\x01\n\x0fOutputFieldSpec\x12\x17\n\nfield_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08guidance\x18\x02 \x01(\tB\x03\xe0A\x01\x12N\n\nfield_type\x18\x03 \x01(\x0e25.google.cloud.aiplatform.v1.OutputFieldSpec.FieldTypeB\x03\xe0A\x01"T\n\tFieldType\x12\x1a\n\x16FIELD_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07CONTENT\x10\x01\x12\x08\n\x04TEXT\x10\x02\x12\t\n\x05IMAGE\x10\x03\x12\t\n\x05AUDIO\x10\x04"8\n\x17TaskDescriptionStrategy\x12\x1d\n\x10task_description\x18\x01 \x01(\tB\x03\xe0A\x02"i\n\x1dGenerateSyntheticDataResponse\x12H\n\x12synthetic_examples\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1.SyntheticExample2\xba\x02\n\x12DataFoundryService\x12\xd4\x01\n\x15GenerateSyntheticData\x128.google.cloud.aiplatform.v1.GenerateSyntheticDataRequest\x1a9.google.cloud.aiplatform.v1.GenerateSyntheticDataResponse"F\x82\xd3\xe4\x93\x02@";/v1/{location=projects/*/locations/*}:generateSyntheticData:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd5\x01\n\x1ecom.google.cloud.aiplatform.v1B\x17DataFoundryServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.data_foundry_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x17DataFoundryServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['location']._loaded_options = None
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['location']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['count']._loaded_options = None
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['count']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['output_field_specs']._loaded_options = None
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['output_field_specs']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['examples']._loaded_options = None
    _globals['_GENERATESYNTHETICDATAREQUEST'].fields_by_name['examples']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHETICFIELD'].fields_by_name['field_name']._loaded_options = None
    _globals['_SYNTHETICFIELD'].fields_by_name['field_name']._serialized_options = b'\xe0A\x01'
    _globals['_SYNTHETICFIELD'].fields_by_name['content']._loaded_options = None
    _globals['_SYNTHETICFIELD'].fields_by_name['content']._serialized_options = b'\xe0A\x02'
    _globals['_SYNTHETICEXAMPLE'].fields_by_name['fields']._loaded_options = None
    _globals['_SYNTHETICEXAMPLE'].fields_by_name['fields']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['field_name']._loaded_options = None
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['field_name']._serialized_options = b'\xe0A\x02'
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['guidance']._loaded_options = None
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['guidance']._serialized_options = b'\xe0A\x01'
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['field_type']._loaded_options = None
    _globals['_OUTPUTFIELDSPEC'].fields_by_name['field_type']._serialized_options = b'\xe0A\x01'
    _globals['_TASKDESCRIPTIONSTRATEGY'].fields_by_name['task_description']._loaded_options = None
    _globals['_TASKDESCRIPTIONSTRATEGY'].fields_by_name['task_description']._serialized_options = b'\xe0A\x02'
    _globals['_DATAFOUNDRYSERVICE']._loaded_options = None
    _globals['_DATAFOUNDRYSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAFOUNDRYSERVICE'].methods_by_name['GenerateSyntheticData']._loaded_options = None
    _globals['_DATAFOUNDRYSERVICE'].methods_by_name['GenerateSyntheticData']._serialized_options = b'\x82\xd3\xe4\x93\x02@";/v1/{location=projects/*/locations/*}:generateSyntheticData:\x01*'
    _globals['_GENERATESYNTHETICDATAREQUEST']._serialized_start = 243
    _globals['_GENERATESYNTHETICDATAREQUEST']._serialized_end = 594
    _globals['_SYNTHETICFIELD']._serialized_start = 596
    _globals['_SYNTHETICFIELD']._serialized_end = 696
    _globals['_SYNTHETICEXAMPLE']._serialized_start = 698
    _globals['_SYNTHETICEXAMPLE']._serialized_end = 781
    _globals['_OUTPUTFIELDSPEC']._serialized_start = 784
    _globals['_OUTPUTFIELDSPEC']._serialized_end = 1015
    _globals['_OUTPUTFIELDSPEC_FIELDTYPE']._serialized_start = 931
    _globals['_OUTPUTFIELDSPEC_FIELDTYPE']._serialized_end = 1015
    _globals['_TASKDESCRIPTIONSTRATEGY']._serialized_start = 1017
    _globals['_TASKDESCRIPTIONSTRATEGY']._serialized_end = 1073
    _globals['_GENERATESYNTHETICDATARESPONSE']._serialized_start = 1075
    _globals['_GENERATESYNTHETICDATARESPONSE']._serialized_end = 1180
    _globals['_DATAFOUNDRYSERVICE']._serialized_start = 1183
    _globals['_DATAFOUNDRYSERVICE']._serialized_end = 1497