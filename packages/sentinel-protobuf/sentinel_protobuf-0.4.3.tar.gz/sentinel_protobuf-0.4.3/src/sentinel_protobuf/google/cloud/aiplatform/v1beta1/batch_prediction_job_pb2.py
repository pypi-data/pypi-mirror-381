"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/batch_prediction_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import completion_stats_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_completion__stats__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import manual_batch_tuning_parameters_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_manual__batch__tuning__parameters__pb2
from .....google.cloud.aiplatform.v1beta1 import model_deployment_monitoring_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__deployment__monitoring__job__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__pb2
from .....google.cloud.aiplatform.v1beta1 import unmanaged_container_model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_unmanaged__container__model__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/batch_prediction_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/aiplatform/v1beta1/completion_stats.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1aDgoogle/cloud/aiplatform/v1beta1/manual_batch_tuning_parameters.proto\x1aEgoogle/cloud/aiplatform/v1beta1/model_deployment_monitoring_job.proto\x1a6google/cloud/aiplatform/v1beta1/model_monitoring.proto\x1a?google/cloud/aiplatform/v1beta1/unmanaged_container_model.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xc5\x16\n\x12BatchPredictionJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x123\n\x05model\x18\x03 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x1d\n\x10model_version_id\x18\x1e \x01(\tB\x03\xe0A\x03\x12[\n\x19unmanaged_container_model\x18\x1c \x01(\x0b28.google.cloud.aiplatform.v1beta1.UnmanagedContainerModel\x12Z\n\x0cinput_config\x18\x04 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.BatchPredictionJob.InputConfigB\x03\xe0A\x02\x12[\n\x0finstance_config\x18\x1b \x01(\x0b2B.google.cloud.aiplatform.v1beta1.BatchPredictionJob.InstanceConfig\x120\n\x10model_parameters\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12\\\n\routput_config\x18\x06 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.BatchPredictionJob.OutputConfigB\x03\xe0A\x02\x12U\n\x13dedicated_resources\x18\x07 \x01(\x0b28.google.cloud.aiplatform.v1beta1.BatchDedicatedResources\x12\x17\n\x0fservice_account\x18\x1d \x01(\t\x12i\n\x1emanual_batch_tuning_parameters\x18\x08 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.ManualBatchTuningParametersB\x03\xe0A\x05\x12\x1c\n\x14generate_explanation\x18\x17 \x01(\x08\x12J\n\x10explanation_spec\x18\x19 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x12X\n\x0boutput_info\x18\t \x01(\x0b2>.google.cloud.aiplatform.v1beta1.BatchPredictionJob.OutputInfoB\x03\xe0A\x03\x12=\n\x05state\x18\n \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x12&\n\x05error\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x121\n\x10partial_failures\x18\x0c \x03(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12S\n\x12resources_consumed\x18\r \x01(\x0b22.google.cloud.aiplatform.v1beta1.ResourcesConsumedB\x03\xe0A\x03\x12O\n\x10completion_stats\x18\x0e \x01(\x0b20.google.cloud.aiplatform.v1beta1.CompletionStatsB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x11 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x12 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x06labels\x18\x13 \x03(\x0b2?.google.cloud.aiplatform.v1beta1.BatchPredictionJob.LabelsEntry\x12H\n\x0fencryption_spec\x18\x18 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12W\n\x17model_monitoring_config\x18\x1a \x01(\x0b26.google.cloud.aiplatform.v1beta1.ModelMonitoringConfig\x12h\n model_monitoring_stats_anomalies\x18\x1f \x03(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringStatsAnomalies\x128\n\x17model_monitoring_status\x18  \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12!\n\x19disable_container_logging\x18" \x01(\x08\x12\x1a\n\rsatisfies_pzs\x18$ \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18% \x01(\x08B\x03\xe0A\x03\x1a\xc4\x01\n\x0bInputConfig\x12@\n\ngcs_source\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.GcsSourceH\x00\x12J\n\x0fbigquery_source\x18\x03 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.BigQuerySourceH\x00\x12\x1d\n\x10instances_format\x18\x01 \x01(\tB\x03\xe0A\x02B\x08\n\x06source\x1al\n\x0eInstanceConfig\x12\x15\n\rinstance_type\x18\x01 \x01(\t\x12\x11\n\tkey_field\x18\x02 \x01(\t\x12\x17\n\x0fincluded_fields\x18\x03 \x03(\t\x12\x17\n\x0fexcluded_fields\x18\x04 \x03(\t\x1a\xe0\x01\n\x0cOutputConfig\x12J\n\x0fgcs_destination\x18\x02 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestinationH\x00\x12T\n\x14bigquery_destination\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.BigQueryDestinationH\x00\x12\x1f\n\x12predictions_format\x18\x01 \x01(\tB\x03\xe0A\x02B\r\n\x0bdestination\x1a\x90\x01\n\nOutputInfo\x12#\n\x14gcs_output_directory\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x12&\n\x17bigquery_output_dataset\x18\x02 \x01(\tB\x03\xe0A\x03H\x00\x12"\n\x15bigquery_output_table\x18\x04 \x01(\tB\x03\xe0A\x03B\x11\n\x0foutput_location\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x86\x01\xeaA\x82\x01\n,aiplatform.googleapis.com/BatchPredictionJob\x12Rprojects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}B\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x17BatchPredictionJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.batch_prediction_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x17BatchPredictionJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_BATCHPREDICTIONJOB_INPUTCONFIG'].fields_by_name['instances_format']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_INPUTCONFIG'].fields_by_name['instances_format']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTIONJOB_OUTPUTCONFIG'].fields_by_name['predictions_format']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_OUTPUTCONFIG'].fields_by_name['predictions_format']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['gcs_output_directory']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['gcs_output_directory']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['bigquery_output_dataset']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['bigquery_output_dataset']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['bigquery_output_table']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO'].fields_by_name['bigquery_output_table']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB_LABELSENTRY']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['name']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model_version_id']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model_version_id']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['input_config']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['output_config']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['output_config']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['manual_batch_tuning_parameters']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['manual_batch_tuning_parameters']._serialized_options = b'\xe0A\x05'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['output_info']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['output_info']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['state']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['error']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['partial_failures']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['partial_failures']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['resources_consumed']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['resources_consumed']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['completion_stats']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['completion_stats']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model_monitoring_status']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['model_monitoring_status']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHPREDICTIONJOB']._loaded_options = None
    _globals['_BATCHPREDICTIONJOB']._serialized_options = b'\xeaA\x82\x01\n,aiplatform.googleapis.com/BatchPredictionJob\x12Rprojects/{project}/locations/{location}/batchPredictionJobs/{batch_prediction_job}'
    _globals['_BATCHPREDICTIONJOB']._serialized_start = 816
    _globals['_BATCHPREDICTIONJOB']._serialized_end = 3701
    _globals['_BATCHPREDICTIONJOB_INPUTCONFIG']._serialized_start = 2837
    _globals['_BATCHPREDICTIONJOB_INPUTCONFIG']._serialized_end = 3033
    _globals['_BATCHPREDICTIONJOB_INSTANCECONFIG']._serialized_start = 3035
    _globals['_BATCHPREDICTIONJOB_INSTANCECONFIG']._serialized_end = 3143
    _globals['_BATCHPREDICTIONJOB_OUTPUTCONFIG']._serialized_start = 3146
    _globals['_BATCHPREDICTIONJOB_OUTPUTCONFIG']._serialized_end = 3370
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO']._serialized_start = 3373
    _globals['_BATCHPREDICTIONJOB_OUTPUTINFO']._serialized_end = 3517
    _globals['_BATCHPREDICTIONJOB_LABELSENTRY']._serialized_start = 3519
    _globals['_BATCHPREDICTIONJOB_LABELSENTRY']._serialized_end = 3564