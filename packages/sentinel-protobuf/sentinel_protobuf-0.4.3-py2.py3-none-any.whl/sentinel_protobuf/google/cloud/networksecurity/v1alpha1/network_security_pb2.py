"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networksecurity/v1alpha1/network_security.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.networksecurity.v1alpha1 import client_tls_policy_pb2 as google_dot_cloud_dot_networksecurity_dot_v1alpha1_dot_client__tls__policy__pb2
from .....google.cloud.networksecurity.v1alpha1 import common_pb2 as google_dot_cloud_dot_networksecurity_dot_v1alpha1_dot_common__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networksecurity/v1alpha1/network_security.proto\x12%google.cloud.networksecurity.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a=google/cloud/networksecurity/v1alpha1/client_tls_policy.proto\x1a2google/cloud/networksecurity/v1alpha1/common.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto2\xfd\x0b\n\x0fNetworkSecurity\x12\xf0\x01\n\x15ListClientTlsPolicies\x12C.google.cloud.networksecurity.v1alpha1.ListClientTlsPoliciesRequest\x1aD.google.cloud.networksecurity.v1alpha1.ListClientTlsPoliciesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*}/clientTlsPolicies\x12\xda\x01\n\x12GetClientTlsPolicy\x12@.google.cloud.networksecurity.v1alpha1.GetClientTlsPolicyRequest\x1a6.google.cloud.networksecurity.v1alpha1.ClientTlsPolicy"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clientTlsPolicies/*}\x12\xd1\x02\n\x15CreateClientTlsPolicy\x12C.google.cloud.networksecurity.v1alpha1.CreateClientTlsPolicyRequest\x1a\x1d.google.longrunning.Operation"\xd3\x01\xcaAJ\n\x0fClientTlsPolicy\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA-parent,client_tls_policy,client_tls_policy_id\x82\xd3\xe4\x93\x02P";/v1alpha1/{parent=projects/*/locations/*}/clientTlsPolicies:\x11client_tls_policy\x12\xd3\x02\n\x15UpdateClientTlsPolicy\x12C.google.cloud.networksecurity.v1alpha1.UpdateClientTlsPolicyRequest\x1a\x1d.google.longrunning.Operation"\xd5\x01\xcaAJ\n\x0fClientTlsPolicy\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA\x1dclient_tls_policy,update_mask\x82\xd3\xe4\x93\x02b2M/v1alpha1/{client_tls_policy.name=projects/*/locations/*/clientTlsPolicies/*}:\x11client_tls_policy\x12\x9b\x02\n\x15DeleteClientTlsPolicy\x12C.google.cloud.networksecurity.v1alpha1.DeleteClientTlsPolicyRequest\x1a\x1d.google.longrunning.Operation"\x9d\x01\xcaAP\n\x15google.protobuf.Empty\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clientTlsPolicies/*}\x1aR\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfd\x01\n)com.google.cloud.networksecurity.v1alpha1P\x01ZScloud.google.com/go/networksecurity/apiv1alpha1/networksecuritypb;networksecuritypb\xaa\x02%Google.Cloud.NetworkSecurity.V1Alpha1\xca\x02%Google\\Cloud\\NetworkSecurity\\V1alpha1\xea\x02(Google::Cloud::NetworkSecurity::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1alpha1.network_security_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.networksecurity.v1alpha1P\x01ZScloud.google.com/go/networksecurity/apiv1alpha1/networksecuritypb;networksecuritypb\xaa\x02%Google.Cloud.NetworkSecurity.V1Alpha1\xca\x02%Google\\Cloud\\NetworkSecurity\\V1alpha1\xea\x02(Google::Cloud::NetworkSecurity::V1alpha1'
    _globals['_NETWORKSECURITY']._loaded_options = None
    _globals['_NETWORKSECURITY']._serialized_options = b'\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_NETWORKSECURITY'].methods_by_name['ListClientTlsPolicies']._loaded_options = None
    _globals['_NETWORKSECURITY'].methods_by_name['ListClientTlsPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{parent=projects/*/locations/*}/clientTlsPolicies'
    _globals['_NETWORKSECURITY'].methods_by_name['GetClientTlsPolicy']._loaded_options = None
    _globals['_NETWORKSECURITY'].methods_by_name['GetClientTlsPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha1/{name=projects/*/locations/*/clientTlsPolicies/*}'
    _globals['_NETWORKSECURITY'].methods_by_name['CreateClientTlsPolicy']._loaded_options = None
    _globals['_NETWORKSECURITY'].methods_by_name['CreateClientTlsPolicy']._serialized_options = b'\xcaAJ\n\x0fClientTlsPolicy\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA-parent,client_tls_policy,client_tls_policy_id\x82\xd3\xe4\x93\x02P";/v1alpha1/{parent=projects/*/locations/*}/clientTlsPolicies:\x11client_tls_policy'
    _globals['_NETWORKSECURITY'].methods_by_name['UpdateClientTlsPolicy']._loaded_options = None
    _globals['_NETWORKSECURITY'].methods_by_name['UpdateClientTlsPolicy']._serialized_options = b'\xcaAJ\n\x0fClientTlsPolicy\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA\x1dclient_tls_policy,update_mask\x82\xd3\xe4\x93\x02b2M/v1alpha1/{client_tls_policy.name=projects/*/locations/*/clientTlsPolicies/*}:\x11client_tls_policy'
    _globals['_NETWORKSECURITY'].methods_by_name['DeleteClientTlsPolicy']._loaded_options = None
    _globals['_NETWORKSECURITY'].methods_by_name['DeleteClientTlsPolicy']._serialized_options = b'\xcaAP\n\x15google.protobuf.Empty\x127google.cloud.networksecurity.v1alpha1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha1/{name=projects/*/locations/*/clientTlsPolicies/*}'
    _globals['_NETWORKSECURITY']._serialized_start = 340
    _globals['_NETWORKSECURITY']._serialized_end = 1873