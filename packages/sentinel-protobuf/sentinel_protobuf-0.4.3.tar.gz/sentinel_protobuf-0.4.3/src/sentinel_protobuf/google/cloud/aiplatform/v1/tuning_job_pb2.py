"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/tuning_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_content__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_job__state__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/aiplatform/v1/tuning_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1/content.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1/job_state.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xc7\x08\n\tTuningJob\x12\x14\n\nbase_model\x18\x04 \x01(\tH\x00\x12R\n\x16supervised_tuning_spec\x18\x05 \x01(\x0b20.google.cloud.aiplatform.v1.SupervisedTuningSpecH\x01\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x03\x12%\n\x18tuned_model_display_name\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x128\n\x05state\x18\x06 \x01(\x0e2$.google.cloud.aiplatform.v1.JobStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12&\n\x05error\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12F\n\x06labels\x18\x0c \x03(\x0b21.google.cloud.aiplatform.v1.TuningJob.LabelsEntryB\x03\xe0A\x01\x12=\n\nexperiment\x18\r \x01(\tB)\xe0A\x03\xfaA#\n!aiplatform.googleapis.com/Context\x12@\n\x0btuned_model\x18\x0e \x01(\x0b2&.google.cloud.aiplatform.v1.TunedModelB\x03\xe0A\x03\x12K\n\x11tuning_data_stats\x18\x0f \x01(\x0b2+.google.cloud.aiplatform.v1.TuningDataStatsB\x03\xe0A\x03\x12C\n\x0fencryption_spec\x18\x10 \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12\x17\n\x0fservice_account\x18\x16 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x80\x01\xeaA}\n#aiplatform.googleapis.com/TuningJob\x12?projects/{project}/locations/{location}/tuningJobs/{tuning_job}*\ntuningJobs2\ttuningJobB\x0e\n\x0csource_modelB\r\n\x0btuning_spec"\xce\x01\n\nTunedModel\x126\n\x05model\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model\x12<\n\x08endpoint\x18\x02 \x01(\tB*\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12J\n\x0bcheckpoints\x18\x03 \x03(\x0b20.google.cloud.aiplatform.v1.TunedModelCheckpointB\x03\xe0A\x03"\xf2\x02\n#SupervisedTuningDatasetDistribution\x12\x10\n\x03sum\x18\x01 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cbillable_sum\x18\t \x01(\x03B\x03\xe0A\x03\x12\x10\n\x03min\x18\x02 \x01(\x01B\x03\xe0A\x03\x12\x10\n\x03max\x18\x03 \x01(\x01B\x03\xe0A\x03\x12\x11\n\x04mean\x18\x04 \x01(\x01B\x03\xe0A\x03\x12\x13\n\x06median\x18\x05 \x01(\x01B\x03\xe0A\x03\x12\x0f\n\x02p5\x18\x06 \x01(\x01B\x03\xe0A\x03\x12\x10\n\x03p95\x18\x07 \x01(\x01B\x03\xe0A\x03\x12c\n\x07buckets\x18\x08 \x03(\x0b2M.google.cloud.aiplatform.v1.SupervisedTuningDatasetDistribution.DatasetBucketB\x03\xe0A\x03\x1aJ\n\rDatasetBucket\x12\x12\n\x05count\x18\x01 \x01(\x01B\x03\xe0A\x03\x12\x11\n\x04left\x18\x02 \x01(\x01B\x03\xe0A\x03\x12\x12\n\x05right\x18\x03 \x01(\x01B\x03\xe0A\x03"\xfc\x05\n\x19SupervisedTuningDataStats\x12)\n\x1ctuning_dataset_example_count\x18\x01 \x01(\x03B\x03\xe0A\x03\x12)\n\x1ctotal_tuning_character_count\x18\x02 \x01(\x03B\x03\xe0A\x03\x12-\n\x1etotal_billable_character_count\x18\x03 \x01(\x03B\x05\x18\x01\xe0A\x03\x12\'\n\x1atotal_billable_token_count\x18\t \x01(\x03B\x03\xe0A\x03\x12\x1e\n\x11tuning_step_count\x18\x04 \x01(\x03B\x03\xe0A\x03\x12k\n\x1duser_input_token_distribution\x18\x05 \x01(\x0b2?.google.cloud.aiplatform.v1.SupervisedTuningDatasetDistributionB\x03\xe0A\x03\x12l\n\x1euser_output_token_distribution\x18\x06 \x01(\x0b2?.google.cloud.aiplatform.v1.SupervisedTuningDatasetDistributionB\x03\xe0A\x03\x12s\n%user_message_per_example_distribution\x18\x07 \x01(\x0b2?.google.cloud.aiplatform.v1.SupervisedTuningDatasetDistributionB\x03\xe0A\x03\x12G\n\x15user_dataset_examples\x18\x08 \x03(\x0b2#.google.cloud.aiplatform.v1.ContentB\x03\xe0A\x03\x12*\n\x1dtotal_truncated_example_count\x18\n \x01(\x03B\x03\xe0A\x03\x12&\n\x19truncated_example_indices\x18\x0b \x03(\x03B\x03\xe0A\x03\x12$\n\x17dropped_example_reasons\x18\x0c \x03(\tB\x03\xe0A\x03"\x85\x01\n\x0fTuningDataStats\x12]\n\x1csupervised_tuning_data_stats\x18\x01 \x01(\x0b25.google.cloud.aiplatform.v1.SupervisedTuningDataStatsH\x00B\x13\n\x11tuning_data_stats"\xfa\x02\n\x19SupervisedHyperParameters\x12\x18\n\x0bepoch_count\x18\x01 \x01(\x03B\x03\xe0A\x01\x12%\n\x18learning_rate_multiplier\x18\x02 \x01(\x01B\x03\xe0A\x01\x12\\\n\x0cadapter_size\x18\x03 \x01(\x0e2A.google.cloud.aiplatform.v1.SupervisedHyperParameters.AdapterSizeB\x03\xe0A\x01"\xbd\x01\n\x0bAdapterSize\x12\x1c\n\x18ADAPTER_SIZE_UNSPECIFIED\x10\x00\x12\x14\n\x10ADAPTER_SIZE_ONE\x10\x01\x12\x14\n\x10ADAPTER_SIZE_TWO\x10\x06\x12\x15\n\x11ADAPTER_SIZE_FOUR\x10\x02\x12\x16\n\x12ADAPTER_SIZE_EIGHT\x10\x03\x12\x18\n\x14ADAPTER_SIZE_SIXTEEN\x10\x04\x12\x1b\n\x17ADAPTER_SIZE_THIRTY_TWO\x10\x05"\xde\x01\n\x14SupervisedTuningSpec\x12!\n\x14training_dataset_uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12#\n\x16validation_dataset_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12T\n\x10hyper_parameters\x18\x03 \x01(\x0b25.google.cloud.aiplatform.v1.SupervisedHyperParametersB\x03\xe0A\x01\x12(\n\x1bexport_last_checkpoint_only\x18\x06 \x01(\x08B\x03\xe0A\x01"\xe3\x01\n\rTunedModelRef\x12;\n\x0btuned_model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/ModelH\x00\x12>\n\ntuning_job\x18\x02 \x01(\tB(\xfaA%\n#aiplatform.googleapis.com/TuningJobH\x00\x12B\n\x0cpipeline_job\x18\x03 \x01(\tB*\xfaA\'\n%aiplatform.googleapis.com/PipelineJobH\x00B\x11\n\x0ftuned_model_ref"\\\n\x14TunedModelCheckpoint\x12\x15\n\rcheckpoint_id\x18\x01 \x01(\t\x12\r\n\x05epoch\x18\x02 \x01(\x03\x12\x0c\n\x04step\x18\x03 \x01(\x03\x12\x10\n\x08endpoint\x18\x04 \x01(\tB\xcc\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0eTuningJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.tuning_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0eTuningJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_TUNINGJOB_LABELSENTRY']._loaded_options = None
    _globals['_TUNINGJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_TUNINGJOB'].fields_by_name['name']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['tuned_model_display_name']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['tuned_model_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_TUNINGJOB'].fields_by_name['description']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TUNINGJOB'].fields_by_name['state']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['error']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['labels']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_TUNINGJOB'].fields_by_name['experiment']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['experiment']._serialized_options = b'\xe0A\x03\xfaA#\n!aiplatform.googleapis.com/Context'
    _globals['_TUNINGJOB'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['tuned_model']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB'].fields_by_name['tuning_data_stats']._loaded_options = None
    _globals['_TUNINGJOB'].fields_by_name['tuning_data_stats']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGJOB']._loaded_options = None
    _globals['_TUNINGJOB']._serialized_options = b'\xeaA}\n#aiplatform.googleapis.com/TuningJob\x12?projects/{project}/locations/{location}/tuningJobs/{tuning_job}*\ntuningJobs2\ttuningJob'
    _globals['_TUNEDMODEL'].fields_by_name['model']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['model']._serialized_options = b'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_TUNEDMODEL'].fields_by_name['endpoint']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_TUNEDMODEL'].fields_by_name['checkpoints']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['checkpoints']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['left']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['left']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['right']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET'].fields_by_name['right']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['sum']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['sum']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['billable_sum']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['billable_sum']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['min']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['min']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['max']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['max']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['mean']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['mean']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['median']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['median']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['p5']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['p5']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['p95']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['p95']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['buckets']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION'].fields_by_name['buckets']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['tuning_dataset_example_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['tuning_dataset_example_count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_tuning_character_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_tuning_character_count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_billable_character_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_billable_character_count']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_billable_token_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_billable_token_count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['tuning_step_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['tuning_step_count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_input_token_distribution']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_input_token_distribution']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_output_token_distribution']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_output_token_distribution']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_message_per_example_distribution']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_message_per_example_distribution']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_dataset_examples']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['user_dataset_examples']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_truncated_example_count']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['total_truncated_example_count']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['truncated_example_indices']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['truncated_example_indices']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['dropped_example_reasons']._loaded_options = None
    _globals['_SUPERVISEDTUNINGDATASTATS'].fields_by_name['dropped_example_reasons']._serialized_options = b'\xe0A\x03'
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['epoch_count']._loaded_options = None
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['epoch_count']._serialized_options = b'\xe0A\x01'
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['learning_rate_multiplier']._loaded_options = None
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['learning_rate_multiplier']._serialized_options = b'\xe0A\x01'
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['adapter_size']._loaded_options = None
    _globals['_SUPERVISEDHYPERPARAMETERS'].fields_by_name['adapter_size']._serialized_options = b'\xe0A\x01'
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['training_dataset_uri']._loaded_options = None
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['training_dataset_uri']._serialized_options = b'\xe0A\x02'
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['validation_dataset_uri']._loaded_options = None
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['validation_dataset_uri']._serialized_options = b'\xe0A\x01'
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['hyper_parameters']._loaded_options = None
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['hyper_parameters']._serialized_options = b'\xe0A\x01'
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['export_last_checkpoint_only']._loaded_options = None
    _globals['_SUPERVISEDTUNINGSPEC'].fields_by_name['export_last_checkpoint_only']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODELREF'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_TUNEDMODELREF'].fields_by_name['tuned_model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_TUNEDMODELREF'].fields_by_name['tuning_job']._loaded_options = None
    _globals['_TUNEDMODELREF'].fields_by_name['tuning_job']._serialized_options = b'\xfaA%\n#aiplatform.googleapis.com/TuningJob'
    _globals['_TUNEDMODELREF'].fields_by_name['pipeline_job']._loaded_options = None
    _globals['_TUNEDMODELREF'].fields_by_name['pipeline_job']._serialized_options = b"\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_TUNINGJOB']._serialized_start = 330
    _globals['_TUNINGJOB']._serialized_end = 1425
    _globals['_TUNINGJOB_LABELSENTRY']._serialized_start = 1218
    _globals['_TUNINGJOB_LABELSENTRY']._serialized_end = 1263
    _globals['_TUNEDMODEL']._serialized_start = 1428
    _globals['_TUNEDMODEL']._serialized_end = 1634
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION']._serialized_start = 1637
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION']._serialized_end = 2007
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET']._serialized_start = 1933
    _globals['_SUPERVISEDTUNINGDATASETDISTRIBUTION_DATASETBUCKET']._serialized_end = 2007
    _globals['_SUPERVISEDTUNINGDATASTATS']._serialized_start = 2010
    _globals['_SUPERVISEDTUNINGDATASTATS']._serialized_end = 2774
    _globals['_TUNINGDATASTATS']._serialized_start = 2777
    _globals['_TUNINGDATASTATS']._serialized_end = 2910
    _globals['_SUPERVISEDHYPERPARAMETERS']._serialized_start = 2913
    _globals['_SUPERVISEDHYPERPARAMETERS']._serialized_end = 3291
    _globals['_SUPERVISEDHYPERPARAMETERS_ADAPTERSIZE']._serialized_start = 3102
    _globals['_SUPERVISEDHYPERPARAMETERS_ADAPTERSIZE']._serialized_end = 3291
    _globals['_SUPERVISEDTUNINGSPEC']._serialized_start = 3294
    _globals['_SUPERVISEDTUNINGSPEC']._serialized_end = 3516
    _globals['_TUNEDMODELREF']._serialized_start = 3519
    _globals['_TUNEDMODELREF']._serialized_end = 3746
    _globals['_TUNEDMODELCHECKPOINT']._serialized_start = 3748
    _globals['_TUNEDMODELCHECKPOINT']._serialized_end = 3840