"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/job_state.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/aiplatform/v1/job_state.proto\x12\x1agoogle.cloud.aiplatform.v1*\xb3\x02\n\x08JobState\x12\x19\n\x15JOB_STATE_UNSPECIFIED\x10\x00\x12\x14\n\x10JOB_STATE_QUEUED\x10\x01\x12\x15\n\x11JOB_STATE_PENDING\x10\x02\x12\x15\n\x11JOB_STATE_RUNNING\x10\x03\x12\x17\n\x13JOB_STATE_SUCCEEDED\x10\x04\x12\x14\n\x10JOB_STATE_FAILED\x10\x05\x12\x18\n\x14JOB_STATE_CANCELLING\x10\x06\x12\x17\n\x13JOB_STATE_CANCELLED\x10\x07\x12\x14\n\x10JOB_STATE_PAUSED\x10\x08\x12\x15\n\x11JOB_STATE_EXPIRED\x10\t\x12\x16\n\x12JOB_STATE_UPDATING\x10\n\x12!\n\x1dJOB_STATE_PARTIALLY_SUCCEEDED\x10\x0bB\xcb\x01\n\x1ecom.google.cloud.aiplatform.v1B\rJobStateProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.job_state_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\rJobStateProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_JOBSTATE']._serialized_start = 75
    _globals['_JOBSTATE']._serialized_end = 382