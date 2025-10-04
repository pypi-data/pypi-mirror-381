"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/hyperparameter_tuning_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import custom_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_custom__job__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import study_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_study__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/aiplatform/v1beta1/hyperparameter_tuning_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/aiplatform/v1beta1/custom_job.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a+google/cloud/aiplatform/v1beta1/study.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xd1\x08\n\x17HyperparameterTuningJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12C\n\nstudy_spec\x18\x04 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.StudySpecB\x03\xe0A\x02\x12\x1c\n\x0fmax_trial_count\x18\x05 \x01(\x05B\x03\xe0A\x02\x12!\n\x14parallel_trial_count\x18\x06 \x01(\x05B\x03\xe0A\x02\x12\x1e\n\x16max_failed_trial_count\x18\x07 \x01(\x05\x12K\n\x0etrial_job_spec\x18\x08 \x01(\x0b2..google.cloud.aiplatform.v1beta1.CustomJobSpecB\x03\xe0A\x02\x12;\n\x06trials\x18\t \x03(\x0b2&.google.cloud.aiplatform.v1beta1.TrialB\x03\xe0A\x03\x12=\n\x05state\x18\n \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x0e \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12&\n\x05error\x18\x0f \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12T\n\x06labels\x18\x10 \x03(\x0b2D.google.cloud.aiplatform.v1beta1.HyperparameterTuningJob.LabelsEntry\x12H\n\x0fencryption_spec\x18\x11 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x12\x1a\n\rsatisfies_pzs\x18\x13 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x14 \x01(\x08B\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x95\x01\xeaA\x91\x01\n1aiplatform.googleapis.com/HyperparameterTuningJob\x12\\projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}B\xf3\x01\n#com.google.cloud.aiplatform.v1beta1B\x1cHyperparameterTuningJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.hyperparameter_tuning_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1cHyperparameterTuningJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_HYPERPARAMETERTUNINGJOB_LABELSENTRY']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['name']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['display_name']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['study_spec']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['study_spec']._serialized_options = b'\xe0A\x02'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['max_trial_count']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['max_trial_count']._serialized_options = b'\xe0A\x02'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['parallel_trial_count']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['parallel_trial_count']._serialized_options = b'\xe0A\x02'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['trial_job_spec']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['trial_job_spec']._serialized_options = b'\xe0A\x02'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['trials']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['trials']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['state']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['start_time']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['end_time']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['error']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['error']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_HYPERPARAMETERTUNINGJOB']._loaded_options = None
    _globals['_HYPERPARAMETERTUNINGJOB']._serialized_options = b'\xeaA\x91\x01\n1aiplatform.googleapis.com/HyperparameterTuningJob\x12\\projects/{project}/locations/{location}/hyperparameterTuningJobs/{hyperparameter_tuning_job}'
    _globals['_HYPERPARAMETERTUNINGJOB']._serialized_start = 418
    _globals['_HYPERPARAMETERTUNINGJOB']._serialized_end = 1523
    _globals['_HYPERPARAMETERTUNINGJOB_LABELSENTRY']._serialized_start = 1326
    _globals['_HYPERPARAMETERTUNINGJOB_LABELSENTRY']._serialized_end = 1371