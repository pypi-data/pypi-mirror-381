"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/assuredworkloads/v1beta1/assuredworkloads_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.assuredworkloads.v1beta1 import assuredworkloads_pb2 as google_dot_cloud_dot_assuredworkloads_dot_v1beta1_dot_assuredworkloads__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/assuredworkloads/v1beta1/assuredworkloads_service.proto\x12%google.cloud.assuredworkloads.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a<google/cloud/assuredworkloads/v1beta1/assuredworkloads.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto2\x90\x0b\n\x17AssuredWorkloadsService\x12\xf9\x01\n\x0eCreateWorkload\x12<.google.cloud.assuredworkloads.v1beta1.CreateWorkloadRequest\x1a\x1d.google.longrunning.Operation"\x89\x01\xcaA+\n\x08Workload\x12\x1fCreateWorkloadOperationMetadata\xdaA\x0fparent,workload\x82\xd3\xe4\x93\x02C"7/v1beta1/{parent=organizations/*/locations/*}/workloads:\x08workload\x12\x98\x01\n\x0eUpdateWorkload\x12<.google.cloud.assuredworkloads.v1beta1.UpdateWorkloadRequest\x1a/.google.cloud.assuredworkloads.v1beta1.Workload"\x17\xdaA\x14workload,update_mask\x12\x88\x02\n\x18RestrictAllowedResources\x12F.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesRequest\x1aG.google.cloud.assuredworkloads.v1beta1.RestrictAllowedResourcesResponse"[\x82\xd3\xe4\x93\x02U"P/v1beta1/{name=organizations/*/locations/*/workloads/*}:restrictAllowedResources:\x01*\x12\xae\x01\n\x0eDeleteWorkload\x12<.google.cloud.assuredworkloads.v1beta1.DeleteWorkloadRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=organizations/*/locations/*/workloads/*}\x12\x82\x01\n\x0bGetWorkload\x129.google.cloud.assuredworkloads.v1beta1.GetWorkloadRequest\x1a/.google.cloud.assuredworkloads.v1beta1.Workload"\x07\xdaA\x04name\x12\xaf\x01\n\x13AnalyzeWorkloadMove\x12A.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveRequest\x1aB.google.cloud.assuredworkloads.v1beta1.AnalyzeWorkloadMoveResponse"\x11\xdaA\x0eproject,target\x12\x95\x01\n\rListWorkloads\x12;.google.cloud.assuredworkloads.v1beta1.ListWorkloadsRequest\x1a<.google.cloud.assuredworkloads.v1beta1.ListWorkloadsResponse"\t\xdaA\x06parent\x1aS\xcaA\x1fassuredworkloads.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n)com.google.cloud.assuredworkloads.v1beta1B\x1cAssuredworkloadsServiceProtoP\x01ZUcloud.google.com/go/assuredworkloads/apiv1beta1/assuredworkloadspb;assuredworkloadspb\xaa\x02%Google.Cloud.AssuredWorkloads.V1Beta1\xca\x02%Google\\Cloud\\AssuredWorkloads\\V1beta1\xea\x02(Google::Cloud::AssuredWorkloads::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.assuredworkloads.v1beta1.assuredworkloads_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.assuredworkloads.v1beta1B\x1cAssuredworkloadsServiceProtoP\x01ZUcloud.google.com/go/assuredworkloads/apiv1beta1/assuredworkloadspb;assuredworkloadspb\xaa\x02%Google.Cloud.AssuredWorkloads.V1Beta1\xca\x02%Google\\Cloud\\AssuredWorkloads\\V1beta1\xea\x02(Google::Cloud::AssuredWorkloads::V1beta1'
    _globals['_ASSUREDWORKLOADSSERVICE']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE']._serialized_options = b'\xcaA\x1fassuredworkloads.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['CreateWorkload']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['CreateWorkload']._serialized_options = b'\xcaA+\n\x08Workload\x12\x1fCreateWorkloadOperationMetadata\xdaA\x0fparent,workload\x82\xd3\xe4\x93\x02C"7/v1beta1/{parent=organizations/*/locations/*}/workloads:\x08workload'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['UpdateWorkload']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['UpdateWorkload']._serialized_options = b'\xdaA\x14workload,update_mask'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['RestrictAllowedResources']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['RestrictAllowedResources']._serialized_options = b'\x82\xd3\xe4\x93\x02U"P/v1beta1/{name=organizations/*/locations/*/workloads/*}:restrictAllowedResources:\x01*'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['DeleteWorkload']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['DeleteWorkload']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v1beta1/{name=organizations/*/locations/*/workloads/*}'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['GetWorkload']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['GetWorkload']._serialized_options = b'\xdaA\x04name'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['AnalyzeWorkloadMove']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['AnalyzeWorkloadMove']._serialized_options = b'\xdaA\x0eproject,target'
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['ListWorkloads']._loaded_options = None
    _globals['_ASSUREDWORKLOADSSERVICE'].methods_by_name['ListWorkloads']._serialized_options = b'\xdaA\x06parent'
    _globals['_ASSUREDWORKLOADSSERVICE']._serialized_start = 295
    _globals['_ASSUREDWORKLOADSSERVICE']._serialized_end = 1719