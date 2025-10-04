"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/nas_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import custom_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_custom__job__pb2
from .....google.cloud.aiplatform.v1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1 import study_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_study__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/aiplatform/v1/nas_job.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a+google/cloud/aiplatform/v1/custom_job.proto\x1a0google/cloud/aiplatform/v1/encryption_spec.proto\x1a*google/cloud/aiplatform/v1/job_state.proto\x1a&google/cloud/aiplatform/v1/study.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xf5\x06\n\x06NasJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x0cnas_job_spec\x18\x04 \x01(\x0b2&.google.cloud.aiplatform.v1.NasJobSpecB\x03\xe0A\x02\x12E\n\x0enas_job_output\x18\x05 \x01(\x0b2(.google.cloud.aiplatform.v1.NasJobOutputB\x03\xe0A\x03\x128\n\x05state\x18\x06 \x01(\x0e2$.google.cloud.aiplatform.v1.JobStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12&\n\x05error\x18\x0b \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12>\n\x06labels\x18\x0c \x03(\x0b2..google.cloud.aiplatform.v1.NasJob.LabelsEntry\x12C\n\x0fencryption_spec\x18\r \x01(\x0b2*.google.cloud.aiplatform.v1.EncryptionSpec\x12/\n enable_restricted_image_training\x18\x0e \x01(\x08B\x05\x18\x01\xe0A\x01\x12\x1a\n\rsatisfies_pzs\x18\x0f \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x10 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:`\xeaA]\n aiplatform.googleapis.com/NasJob\x129projects/{project}/locations/{location}/nasJobs/{nas_job}"\xbd\x02\n\x0eNasTrialDetail\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\nparameters\x18\x02 \x01(\t\x12:\n\x0csearch_trial\x18\x03 \x01(\x0b2$.google.cloud.aiplatform.v1.NasTrial\x129\n\x0btrain_trial\x18\x04 \x01(\x0b2$.google.cloud.aiplatform.v1.NasTrial:\x8c\x01\xeaA\x88\x01\n(aiplatform.googleapis.com/NasTrialDetail\x12\\projects/{project}/locations/{location}/nasJobs/{nas_job}/nasTrialDetails/{nas_trial_detail}"\xa5\n\n\nNasJobSpec\x12d\n\x1amulti_trial_algorithm_spec\x18\x02 \x01(\x0b2>.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpecH\x00\x12\x19\n\x11resume_nas_job_id\x18\x03 \x01(\t\x12\x19\n\x11search_space_spec\x18\x01 \x01(\t\x1a\xe4\x08\n\x17MultiTrialAlgorithmSpec\x12q\n\x15multi_trial_algorithm\x18\x01 \x01(\x0e2R.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpec.MultiTrialAlgorithm\x12Y\n\x06metric\x18\x02 \x01(\x0b2I.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec\x12n\n\x11search_trial_spec\x18\x03 \x01(\x0b2N.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpec.SearchTrialSpecB\x03\xe0A\x02\x12g\n\x10train_trial_spec\x18\x04 \x01(\x0b2M.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpec.TrainTrialSpec\x1a\xce\x01\n\nMetricSpec\x12\x16\n\tmetric_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12e\n\x04goal\x18\x02 \x01(\x0e2R.google.cloud.aiplatform.v1.NasJobSpec.MultiTrialAlgorithmSpec.MetricSpec.GoalTypeB\x03\xe0A\x02"A\n\x08GoalType\x12\x19\n\x15GOAL_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08MAXIMIZE\x10\x01\x12\x0c\n\x08MINIMIZE\x10\x02\x1a\xc5\x01\n\x0fSearchTrialSpec\x12M\n\x15search_trial_job_spec\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1.CustomJobSpecB\x03\xe0A\x02\x12\x1c\n\x0fmax_trial_count\x18\x02 \x01(\x05B\x03\xe0A\x02\x12%\n\x18max_parallel_trial_count\x18\x03 \x01(\x05B\x03\xe0A\x02\x12\x1e\n\x16max_failed_trial_count\x18\x04 \x01(\x05\x1a\x9d\x01\n\x0eTrainTrialSpec\x12L\n\x14train_trial_job_spec\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1.CustomJobSpecB\x03\xe0A\x02\x12%\n\x18max_parallel_trial_count\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x16\n\tfrequency\x18\x03 \x01(\x05B\x03\xe0A\x02"i\n\x13MultiTrialAlgorithm\x12%\n!MULTI_TRIAL_ALGORITHM_UNSPECIFIED\x10\x00\x12\x1a\n\x16REINFORCEMENT_LEARNING\x10\x01\x12\x0f\n\x0bGRID_SEARCH\x10\x02B\x14\n\x12nas_algorithm_spec"\x98\x02\n\x0cNasJobOutput\x12c\n\x16multi_trial_job_output\x18\x01 \x01(\x0b2<.google.cloud.aiplatform.v1.NasJobOutput.MultiTrialJobOutputB\x03\xe0A\x03H\x00\x1a\x98\x01\n\x13MultiTrialJobOutput\x12@\n\rsearch_trials\x18\x01 \x03(\x0b2$.google.cloud.aiplatform.v1.NasTrialB\x03\xe0A\x03\x12?\n\x0ctrain_trials\x18\x02 \x03(\x0b2$.google.cloud.aiplatform.v1.NasTrialB\x03\xe0A\x03B\x08\n\x06output"\xf4\x02\n\x08NasTrial\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12>\n\x05state\x18\x02 \x01(\x0e2*.google.cloud.aiplatform.v1.NasTrial.StateB\x03\xe0A\x03\x12G\n\x11final_measurement\x18\x03 \x01(\x0b2\'.google.cloud.aiplatform.v1.MeasurementB\x03\xe0A\x03\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"f\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tREQUESTED\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08STOPPING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\x0e\n\nINFEASIBLE\x10\x05B\xc9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x0bNasJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.nas_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x0bNasJobProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_NASJOB_LABELSENTRY']._loaded_options = None
    _globals['_NASJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_NASJOB'].fields_by_name['name']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOB'].fields_by_name['nas_job_spec']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['nas_job_spec']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOB'].fields_by_name['nas_job_output']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['nas_job_output']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['state']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['error']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['enable_restricted_image_training']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['enable_restricted_image_training']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_NASJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_NASJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB']._loaded_options = None
    _globals['_NASJOB']._serialized_options = b'\xeaA]\n aiplatform.googleapis.com/NasJob\x129projects/{project}/locations/{location}/nasJobs/{nas_job}'
    _globals['_NASTRIALDETAIL'].fields_by_name['name']._loaded_options = None
    _globals['_NASTRIALDETAIL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIALDETAIL']._loaded_options = None
    _globals['_NASTRIALDETAIL']._serialized_options = b'\xeaA\x88\x01\n(aiplatform.googleapis.com/NasTrialDetail\x12\\projects/{project}/locations/{location}/nasJobs/{nas_job}/nasTrialDetails/{nas_trial_detail}'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC'].fields_by_name['metric_id']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC'].fields_by_name['metric_id']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC'].fields_by_name['goal']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC'].fields_by_name['goal']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['search_trial_job_spec']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['search_trial_job_spec']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['max_trial_count']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['max_trial_count']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['max_parallel_trial_count']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC'].fields_by_name['max_parallel_trial_count']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['train_trial_job_spec']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['train_trial_job_spec']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['max_parallel_trial_count']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['max_parallel_trial_count']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['frequency']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC'].fields_by_name['frequency']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC'].fields_by_name['search_trial_spec']._loaded_options = None
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC'].fields_by_name['search_trial_spec']._serialized_options = b'\xe0A\x02'
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT'].fields_by_name['search_trials']._loaded_options = None
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT'].fields_by_name['search_trials']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT'].fields_by_name['train_trials']._loaded_options = None
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT'].fields_by_name['train_trials']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOBOUTPUT'].fields_by_name['multi_trial_job_output']._loaded_options = None
    _globals['_NASJOBOUTPUT'].fields_by_name['multi_trial_job_output']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIAL'].fields_by_name['id']._loaded_options = None
    _globals['_NASTRIAL'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIAL'].fields_by_name['state']._loaded_options = None
    _globals['_NASTRIAL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIAL'].fields_by_name['final_measurement']._loaded_options = None
    _globals['_NASTRIAL'].fields_by_name['final_measurement']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIAL'].fields_by_name['start_time']._loaded_options = None
    _globals['_NASTRIAL'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASTRIAL'].fields_by_name['end_time']._loaded_options = None
    _globals['_NASTRIAL'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_NASJOB']._serialized_start = 370
    _globals['_NASJOB']._serialized_end = 1255
    _globals['_NASJOB_LABELSENTRY']._serialized_start = 1112
    _globals['_NASJOB_LABELSENTRY']._serialized_end = 1157
    _globals['_NASTRIALDETAIL']._serialized_start = 1258
    _globals['_NASTRIALDETAIL']._serialized_end = 1575
    _globals['_NASJOBSPEC']._serialized_start = 1578
    _globals['_NASJOBSPEC']._serialized_end = 2895
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC']._serialized_start = 1749
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC']._serialized_end = 2873
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC']._serialized_start = 2200
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC']._serialized_end = 2406
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC_GOALTYPE']._serialized_start = 2341
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_METRICSPEC_GOALTYPE']._serialized_end = 2406
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC']._serialized_start = 2409
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_SEARCHTRIALSPEC']._serialized_end = 2606
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC']._serialized_start = 2609
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_TRAINTRIALSPEC']._serialized_end = 2766
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_MULTITRIALALGORITHM']._serialized_start = 2768
    _globals['_NASJOBSPEC_MULTITRIALALGORITHMSPEC_MULTITRIALALGORITHM']._serialized_end = 2873
    _globals['_NASJOBOUTPUT']._serialized_start = 2898
    _globals['_NASJOBOUTPUT']._serialized_end = 3178
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT']._serialized_start = 3016
    _globals['_NASJOBOUTPUT_MULTITRIALJOBOUTPUT']._serialized_end = 3168
    _globals['_NASTRIAL']._serialized_start = 3181
    _globals['_NASTRIAL']._serialized_end = 3553
    _globals['_NASTRIAL_STATE']._serialized_start = 3451
    _globals['_NASTRIAL_STATE']._serialized_end = 3553