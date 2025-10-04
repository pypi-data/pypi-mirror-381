"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/alloydb/v1alpha/csql_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.alloydb.v1alpha import csql_resources_pb2 as google_dot_cloud_dot_alloydb_dot_v1alpha_dot_csql__resources__pb2
from .....google.cloud.alloydb.v1alpha import resources_pb2 as google_dot_cloud_dot_alloydb_dot_v1alpha_dot_resources__pb2
from .....google.cloud.alloydb.v1alpha import service_pb2 as google_dot_cloud_dot_alloydb_dot_v1alpha_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/alloydb/v1alpha/csql_service.proto\x12\x1cgoogle.cloud.alloydb.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/alloydb/v1alpha/csql_resources.proto\x1a,google/cloud/alloydb/v1alpha/resources.proto\x1a*google/cloud/alloydb/v1alpha/service.proto\x1a#google/longrunning/operations.proto"\x91\x02\n\x1aRestoreFromCloudSQLRequest\x12[\n\x1acloudsql_backup_run_source\x18e \x01(\x0b25.google.cloud.alloydb.v1alpha.CloudSQLBackupRunSourceH\x00\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1ealloydb.googleapis.com/Cluster\x12\x17\n\ncluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x07cluster\x18\x03 \x01(\x0b2%.google.cloud.alloydb.v1alpha.ClusterB\x03\xe0A\x02B\x08\n\x06source2\xd5\x02\n\x10AlloyDBCSQLAdmin\x12\xf4\x01\n\x13RestoreFromCloudSQL\x128.google.cloud.alloydb.v1alpha.RestoreFromCloudSQLRequest\x1a\x1d.google.longrunning.Operation"\x83\x01\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x11parent,cluster_id\x82\xd3\xe4\x93\x02J"E/v1alpha/{parent=projects/*/locations/*}/clusters:restoreFromCloudSQL:\x01*\x1aJ\xcaA\x16alloydb.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd2\x01\n com.google.cloud.alloydb.v1alphaB\x10CSQLServiceProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.alloydb.v1alpha.csql_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.alloydb.v1alphaB\x10CSQLServiceProtoP\x01Z:cloud.google.com/go/alloydb/apiv1alpha/alloydbpb;alloydbpb\xaa\x02\x1cGoogle.Cloud.AlloyDb.V1Alpha\xca\x02\x1cGoogle\\Cloud\\AlloyDb\\V1alpha\xea\x02\x1fGoogle::Cloud::AlloyDB::V1alpha'
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1ealloydb.googleapis.com/Cluster'
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['cluster_id']._loaded_options = None
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['cluster']._loaded_options = None
    _globals['_RESTOREFROMCLOUDSQLREQUEST'].fields_by_name['cluster']._serialized_options = b'\xe0A\x02'
    _globals['_ALLOYDBCSQLADMIN']._loaded_options = None
    _globals['_ALLOYDBCSQLADMIN']._serialized_options = b'\xcaA\x16alloydb.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ALLOYDBCSQLADMIN'].methods_by_name['RestoreFromCloudSQL']._loaded_options = None
    _globals['_ALLOYDBCSQLADMIN'].methods_by_name['RestoreFromCloudSQL']._serialized_options = b'\xcaA\x1c\n\x07Cluster\x12\x11OperationMetadata\xdaA\x11parent,cluster_id\x82\xd3\xe4\x93\x02J"E/v1alpha/{parent=projects/*/locations/*}/clusters:restoreFromCloudSQL:\x01*'
    _globals['_RESTOREFROMCLOUDSQLREQUEST']._serialized_start = 375
    _globals['_RESTOREFROMCLOUDSQLREQUEST']._serialized_end = 648
    _globals['_ALLOYDBCSQLADMIN']._serialized_start = 651
    _globals['_ALLOYDBCSQLADMIN']._serialized_end = 992