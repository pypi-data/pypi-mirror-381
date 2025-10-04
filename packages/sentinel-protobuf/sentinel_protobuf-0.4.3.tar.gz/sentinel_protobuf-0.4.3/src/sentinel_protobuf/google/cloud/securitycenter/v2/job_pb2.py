"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/cloud/securitycenter/v2/job.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1fgoogle/api/field_behavior.proto"w\n\x03Job\x12\x0c\n\x04name\x18\x01 \x01(\t\x12<\n\x05state\x18\x02 \x01(\x0e2(.google.cloud.securitycenter.v2.JobStateB\x03\xe0A\x03\x12\x12\n\nerror_code\x18\x03 \x01(\x05\x12\x10\n\x08location\x18\x04 \x01(\t*Z\n\x08JobState\x12\x19\n\x15JOB_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07RUNNING\x10\x02\x12\r\n\tSUCCEEDED\x10\x03\x12\n\n\x06FAILED\x10\x04B\xe2\x01\n"com.google.cloud.securitycenter.v2B\x08JobProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x08JobProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_JOB'].fields_by_name['state']._loaded_options = None
    _globals['_JOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_JOBSTATE']._serialized_start = 230
    _globals['_JOBSTATE']._serialized_end = 320
    _globals['_JOB']._serialized_start = 109
    _globals['_JOB']._serialized_end = 228