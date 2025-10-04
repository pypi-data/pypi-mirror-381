"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/training_pipeline.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__pb2
from .....google.cloud.aiplatform.v1beta1 import pipeline_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_pipeline__state__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/aiplatform/v1beta1/training_pipeline.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a+google/cloud/aiplatform/v1beta1/model.proto\x1a4google/cloud/aiplatform/v1beta1/pipeline_state.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa7\x08\n\x10TrainingPipeline\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\x11input_data_config\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1beta1.InputDataConfig\x12%\n\x18training_task_definition\x18\x04 \x01(\tB\x03\xe0A\x02\x129\n\x14training_task_inputs\x18\x05 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x02\x12;\n\x16training_task_metadata\x18\x06 \x01(\x0b2\x16.google.protobuf.ValueB\x03\xe0A\x03\x12?\n\x0fmodel_to_upload\x18\x07 \x01(\x0b2&.google.cloud.aiplatform.v1beta1.Model\x12\x15\n\x08model_id\x18\x16 \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cparent_model\x18\x15 \x01(\tB\x03\xe0A\x01\x12B\n\x05state\x18\t \x01(\x0e2..google.cloud.aiplatform.v1beta1.PipelineStateB\x03\xe0A\x03\x12&\n\x05error\x18\n \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x06labels\x18\x0f \x03(\x0b2=.google.cloud.aiplatform.v1beta1.TrainingPipeline.LabelsEntry\x12H\n\x0fencryption_spec\x18\x12 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:~\xeaA{\n*aiplatform.googleapis.com/TrainingPipeline\x12Mprojects/{project}/locations/{location}/trainingPipelines/{training_pipeline}"\xd2\x05\n\x0fInputDataConfig\x12H\n\x0efraction_split\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.FractionSplitH\x00\x12D\n\x0cfilter_split\x18\x03 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.FilterSplitH\x00\x12L\n\x10predefined_split\x18\x04 \x01(\x0b20.google.cloud.aiplatform.v1beta1.PredefinedSplitH\x00\x12J\n\x0ftimestamp_split\x18\x05 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.TimestampSplitH\x00\x12L\n\x10stratified_split\x18\x0c \x01(\x0b20.google.cloud.aiplatform.v1beta1.StratifiedSplitH\x00\x12J\n\x0fgcs_destination\x18\x08 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestinationH\x01\x12T\n\x14bigquery_destination\x18\n \x01(\x0b24.google.cloud.aiplatform.v1beta1.BigQueryDestinationH\x01\x12\x17\n\ndataset_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\x12annotations_filter\x18\x06 \x01(\t\x12\x1d\n\x15annotation_schema_uri\x18\t \x01(\t\x12\x16\n\x0esaved_query_id\x18\x07 \x01(\t\x12!\n\x19persist_ml_use_assignment\x18\x0b \x01(\x08B\x07\n\x05splitB\r\n\x0bdestination"^\n\rFractionSplit\x12\x19\n\x11training_fraction\x18\x01 \x01(\x01\x12\x1b\n\x13validation_fraction\x18\x02 \x01(\x01\x12\x15\n\rtest_fraction\x18\x03 \x01(\x01"e\n\x0bFilterSplit\x12\x1c\n\x0ftraining_filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11validation_filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0btest_filter\x18\x03 \x01(\tB\x03\xe0A\x02"#\n\x0fPredefinedSplit\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02"q\n\x0eTimestampSplit\x12\x19\n\x11training_fraction\x18\x01 \x01(\x01\x12\x1b\n\x13validation_fraction\x18\x02 \x01(\x01\x12\x15\n\rtest_fraction\x18\x03 \x01(\x01\x12\x10\n\x03key\x18\x04 \x01(\tB\x03\xe0A\x02"r\n\x0fStratifiedSplit\x12\x19\n\x11training_fraction\x18\x01 \x01(\x01\x12\x1b\n\x13validation_fraction\x18\x02 \x01(\x01\x12\x15\n\rtest_fraction\x18\x03 \x01(\x01\x12\x10\n\x03key\x18\x04 \x01(\tB\x03\xe0A\x02B\xec\x01\n#com.google.cloud.aiplatform.v1beta1B\x15TrainingPipelineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.training_pipeline_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x15TrainingPipelineProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_TRAININGPIPELINE_LABELSENTRY']._loaded_options = None
    _globals['_TRAININGPIPELINE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TRAININGPIPELINE'].fields_by_name['name']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_definition']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_definition']._serialized_options = b'\xe0A\x02'
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_inputs']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_inputs']._serialized_options = b'\xe0A\x02'
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_metadata']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['training_task_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['model_id']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['model_id']._serialized_options = b'\xe0A\x01'
    _globals['_TRAININGPIPELINE'].fields_by_name['parent_model']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['parent_model']._serialized_options = b'\xe0A\x01'
    _globals['_TRAININGPIPELINE'].fields_by_name['state']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['error']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['start_time']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['end_time']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_TRAININGPIPELINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TRAININGPIPELINE']._loaded_options = None
    _globals['_TRAININGPIPELINE']._serialized_options = b'\xeaA{\n*aiplatform.googleapis.com/TrainingPipeline\x12Mprojects/{project}/locations/{location}/trainingPipelines/{training_pipeline}'
    _globals['_INPUTDATACONFIG'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_INPUTDATACONFIG'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_FILTERSPLIT'].fields_by_name['training_filter']._loaded_options = None
    _globals['_FILTERSPLIT'].fields_by_name['training_filter']._serialized_options = b'\xe0A\x02'
    _globals['_FILTERSPLIT'].fields_by_name['validation_filter']._loaded_options = None
    _globals['_FILTERSPLIT'].fields_by_name['validation_filter']._serialized_options = b'\xe0A\x02'
    _globals['_FILTERSPLIT'].fields_by_name['test_filter']._loaded_options = None
    _globals['_FILTERSPLIT'].fields_by_name['test_filter']._serialized_options = b'\xe0A\x02'
    _globals['_PREDEFINEDSPLIT'].fields_by_name['key']._loaded_options = None
    _globals['_PREDEFINEDSPLIT'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_TIMESTAMPSPLIT'].fields_by_name['key']._loaded_options = None
    _globals['_TIMESTAMPSPLIT'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_STRATIFIEDSPLIT'].fields_by_name['key']._loaded_options = None
    _globals['_STRATIFIEDSPLIT'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_TRAININGPIPELINE']._serialized_start = 437
    _globals['_TRAININGPIPELINE']._serialized_end = 1500
    _globals['_TRAININGPIPELINE_LABELSENTRY']._serialized_start = 1327
    _globals['_TRAININGPIPELINE_LABELSENTRY']._serialized_end = 1372
    _globals['_INPUTDATACONFIG']._serialized_start = 1503
    _globals['_INPUTDATACONFIG']._serialized_end = 2225
    _globals['_FRACTIONSPLIT']._serialized_start = 2227
    _globals['_FRACTIONSPLIT']._serialized_end = 2321
    _globals['_FILTERSPLIT']._serialized_start = 2323
    _globals['_FILTERSPLIT']._serialized_end = 2424
    _globals['_PREDEFINEDSPLIT']._serialized_start = 2426
    _globals['_PREDEFINEDSPLIT']._serialized_end = 2461
    _globals['_TIMESTAMPSPLIT']._serialized_start = 2463
    _globals['_TIMESTAMPSPLIT']._serialized_end = 2576
    _globals['_STRATIFIEDSPLIT']._serialized_start = 2578
    _globals['_STRATIFIEDSPLIT']._serialized_end = 2692