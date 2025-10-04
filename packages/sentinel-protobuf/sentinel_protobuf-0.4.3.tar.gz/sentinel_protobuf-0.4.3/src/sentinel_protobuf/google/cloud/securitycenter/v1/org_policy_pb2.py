"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v1/org_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/securitycenter/v1/org_policy.proto\x12\x1egoogle.cloud.securitycenter.v1\x1a\x19google/api/resource.proto"\xd6\x01\n\tOrgPolicy\x12\x0c\n\x04name\x18\x01 \x01(\t:\xba\x01\xeaA\xb6\x01\n\x1forgpolicy.googleapis.com/Policy\x127organizations/{organization}/policies/{constraint_name}\x12+folders/{folder}/policies/{constraint_name}\x12-projects/{project}/policies/{constraint_name}B\xe8\x01\n"com.google.cloud.securitycenter.v1B\x0eOrgPolicyProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.org_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B\x0eOrgPolicyProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_ORGPOLICY']._loaded_options = None
    _globals['_ORGPOLICY']._serialized_options = b'\xeaA\xb6\x01\n\x1forgpolicy.googleapis.com/Policy\x127organizations/{organization}/policies/{constraint_name}\x12+folders/{folder}/policies/{constraint_name}\x12-projects/{project}/policies/{constraint_name}'
    _globals['_ORGPOLICY']._serialized_start = 111
    _globals['_ORGPOLICY']._serialized_end = 325