"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkemulticloud/v1/attached_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkemulticloud.v1 import attached_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_attached__resources__pb2
from .....google.cloud.gkemulticloud.v1 import common_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_common__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/gkemulticloud/v1/attached_service.proto\x12\x1dgoogle.cloud.gkemulticloud.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/gkemulticloud/v1/attached_resources.proto\x1a4google/cloud/gkemulticloud/v1/common_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x85\x02\n-GenerateAttachedClusterInstallManifestRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster\x12 \n\x13attached_cluster_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10platform_version\x18\x03 \x01(\tB\x03\xe0A\x02\x12M\n\x0cproxy_config\x18\x04 \x01(\x0b22.google.cloud.gkemulticloud.v1.AttachedProxyConfigB\x03\xe0A\x01"B\n.GenerateAttachedClusterInstallManifestResponse\x12\x10\n\x08manifest\x18\x01 \x01(\t"\xec\x01\n\x1cCreateAttachedClusterRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster\x12M\n\x10attached_cluster\x18\x02 \x01(\x0b2..google.cloud.gkemulticloud.v1.AttachedClusterB\x03\xe0A\x02\x12 \n\x13attached_cluster_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xa3\x02\n\x1cImportAttachedClusterRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x1d\n\x10fleet_membership\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x1d\n\x10platform_version\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdistribution\x18\x05 \x01(\tB\x03\xe0A\x02\x12M\n\x0cproxy_config\x18\x06 \x01(\x0b22.google.cloud.gkemulticloud.v1.AttachedProxyConfigB\x03\xe0A\x01"\xba\x01\n\x1cUpdateAttachedClusterRequest\x12M\n\x10attached_cluster\x18\x01 \x01(\x0b2..google.cloud.gkemulticloud.v1.AttachedClusterB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"_\n\x19GetAttachedClusterRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster"\x8a\x01\n\x1bListAttachedClustersRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x82\x01\n\x1cListAttachedClustersResponse\x12I\n\x11attached_clusters\x18\x01 \x03(\x0b2..google.cloud.gkemulticloud.v1.AttachedCluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb5\x01\n\x1cDeleteAttachedClusterRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\x12\x15\n\rignore_errors\x18\x05 \x01(\x08\x12\x0c\n\x04etag\x18\x04 \x01(\t"i\n\x1eGetAttachedServerConfigRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1gkemulticloud.googleapis.com/AttachedServerConfig"\xca\x02\n(GenerateAttachedClusterAgentTokenRequest\x12N\n\x10attached_cluster\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster\x12\x1a\n\rsubject_token\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12subject_token_type\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x17\n\ngrant_type\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08audience\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05scope\x18\x08 \x01(\tB\x03\xe0A\x01\x12!\n\x14requested_token_type\x18\t \x01(\tB\x03\xe0A\x01\x12\x14\n\x07options\x18\n \x01(\tB\x03\xe0A\x01"i\n)GenerateAttachedClusterAgentTokenResponse\x12\x14\n\x0caccess_token\x18\x01 \x01(\t\x12\x12\n\nexpires_in\x18\x02 \x01(\x05\x12\x12\n\ntoken_type\x18\x03 \x01(\t2\xdd\x12\n\x10AttachedClusters\x12\x99\x02\n\x15CreateAttachedCluster\x12;.google.cloud.gkemulticloud.v1.CreateAttachedClusterRequest\x1a\x1d.google.longrunning.Operation"\xa3\x01\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA+parent,attached_cluster,attached_cluster_id\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/attachedClusters:\x10attached_cluster\x12\x9b\x02\n\x15UpdateAttachedCluster\x12;.google.cloud.gkemulticloud.v1.UpdateAttachedClusterRequest\x1a\x1d.google.longrunning.Operation"\xa5\x01\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA\x1cattached_cluster,update_mask\x82\xd3\xe4\x93\x02Y2E/v1/{attached_cluster.name=projects/*/locations/*/attachedClusters/*}:\x10attached_cluster\x12\xfd\x01\n\x15ImportAttachedCluster\x12;.google.cloud.gkemulticloud.v1.ImportAttachedClusterRequest\x1a\x1d.google.longrunning.Operation"\x87\x01\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA\x17parent,fleet_membership\x82\xd3\xe4\x93\x02@";/v1/{parent=projects/*/locations/*}/attachedClusters:import:\x01*\x12\xc3\x01\n\x12GetAttachedCluster\x128.google.cloud.gkemulticloud.v1.GetAttachedClusterRequest\x1a..google.cloud.gkemulticloud.v1.AttachedCluster"C\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/attachedClusters/*}\x12\xd6\x01\n\x14ListAttachedClusters\x12:.google.cloud.gkemulticloud.v1.ListAttachedClustersRequest\x1a;.google.cloud.gkemulticloud.v1.ListAttachedClustersResponse"E\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/attachedClusters\x12\xe5\x01\n\x15DeleteAttachedCluster\x12;.google.cloud.gkemulticloud.v1.DeleteAttachedClusterRequest\x1a\x1d.google.longrunning.Operation"p\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/attachedClusters/*}\x12\xd4\x01\n\x17GetAttachedServerConfig\x12=.google.cloud.gkemulticloud.v1.GetAttachedServerConfigRequest\x1a3.google.cloud.gkemulticloud.v1.AttachedServerConfig"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/attachedServerConfig}\x12\xb6\x02\n&GenerateAttachedClusterInstallManifest\x12L.google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestRequest\x1aM.google.cloud.gkemulticloud.v1.GenerateAttachedClusterInstallManifestResponse"o\xdaA\x1aparent,attached_cluster_id\x82\xd3\xe4\x93\x02L\x12J/v1/{parent=projects/*/locations/*}:generateAttachedClusterInstallManifest\x12\xa5\x02\n!GenerateAttachedClusterAgentToken\x12G.google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenRequest\x1aH.google.cloud.gkemulticloud.v1.GenerateAttachedClusterAgentTokenResponse"m\x82\xd3\xe4\x93\x02g"b/v1/{attached_cluster=projects/*/locations/*/attachedClusters/*}:generateAttachedClusterAgentToken:\x01*\x1aP\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe7\x01\n!com.google.cloud.gkemulticloud.v1B\x14AttachedServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkemulticloud.v1.attached_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.gkemulticloud.v1B\x14AttachedServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1'
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['attached_cluster_id']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['attached_cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['platform_version']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['platform_version']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['proxy_config']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST'].fields_by_name['proxy_config']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster']._loaded_options = None
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster_id']._loaded_options = None
    _globals['_CREATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['fleet_membership']._loaded_options = None
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['fleet_membership']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['platform_version']._loaded_options = None
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['platform_version']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['distribution']._loaded_options = None
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['distribution']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['proxy_config']._loaded_options = None
    _globals['_IMPORTATTACHEDCLUSTERREQUEST'].fields_by_name['proxy_config']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster']._loaded_options = None
    _globals['_UPDATEATTACHEDCLUSTERREQUEST'].fields_by_name['attached_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEATTACHEDCLUSTERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEATTACHEDCLUSTERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETATTACHEDCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTACHEDCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_LISTATTACHEDCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTATTACHEDCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_DELETEATTACHEDCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEATTACHEDCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_GETATTACHEDSERVERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTACHEDSERVERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1gkemulticloud.googleapis.com/AttachedServerConfig'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['attached_cluster']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['attached_cluster']._serialized_options = b'\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AttachedCluster'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._loaded_options = None
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_ATTACHEDCLUSTERS']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS']._serialized_options = b'\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['CreateAttachedCluster']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['CreateAttachedCluster']._serialized_options = b'\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA+parent,attached_cluster,attached_cluster_id\x82\xd3\xe4\x93\x02H"4/v1/{parent=projects/*/locations/*}/attachedClusters:\x10attached_cluster'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['UpdateAttachedCluster']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['UpdateAttachedCluster']._serialized_options = b'\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA\x1cattached_cluster,update_mask\x82\xd3\xe4\x93\x02Y2E/v1/{attached_cluster.name=projects/*/locations/*/attachedClusters/*}:\x10attached_cluster'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['ImportAttachedCluster']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['ImportAttachedCluster']._serialized_options = b'\xcaA$\n\x0fAttachedCluster\x12\x11OperationMetadata\xdaA\x17parent,fleet_membership\x82\xd3\xe4\x93\x02@";/v1/{parent=projects/*/locations/*}/attachedClusters:import:\x01*'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GetAttachedCluster']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GetAttachedCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x026\x124/v1/{name=projects/*/locations/*/attachedClusters/*}'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['ListAttachedClusters']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['ListAttachedClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x026\x124/v1/{parent=projects/*/locations/*}/attachedClusters'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['DeleteAttachedCluster']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['DeleteAttachedCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026*4/v1/{name=projects/*/locations/*/attachedClusters/*}'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GetAttachedServerConfig']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GetAttachedServerConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/attachedServerConfig}'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GenerateAttachedClusterInstallManifest']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GenerateAttachedClusterInstallManifest']._serialized_options = b'\xdaA\x1aparent,attached_cluster_id\x82\xd3\xe4\x93\x02L\x12J/v1/{parent=projects/*/locations/*}:generateAttachedClusterInstallManifest'
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GenerateAttachedClusterAgentToken']._loaded_options = None
    _globals['_ATTACHEDCLUSTERS'].methods_by_name['GenerateAttachedClusterAgentToken']._serialized_options = b'\x82\xd3\xe4\x93\x02g"b/v1/{attached_cluster=projects/*/locations/*/attachedClusters/*}:generateAttachedClusterAgentToken:\x01*'
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST']._serialized_start = 413
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTREQUEST']._serialized_end = 674
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTRESPONSE']._serialized_start = 676
    _globals['_GENERATEATTACHEDCLUSTERINSTALLMANIFESTRESPONSE']._serialized_end = 742
    _globals['_CREATEATTACHEDCLUSTERREQUEST']._serialized_start = 745
    _globals['_CREATEATTACHEDCLUSTERREQUEST']._serialized_end = 981
    _globals['_IMPORTATTACHEDCLUSTERREQUEST']._serialized_start = 984
    _globals['_IMPORTATTACHEDCLUSTERREQUEST']._serialized_end = 1275
    _globals['_UPDATEATTACHEDCLUSTERREQUEST']._serialized_start = 1278
    _globals['_UPDATEATTACHEDCLUSTERREQUEST']._serialized_end = 1464
    _globals['_GETATTACHEDCLUSTERREQUEST']._serialized_start = 1466
    _globals['_GETATTACHEDCLUSTERREQUEST']._serialized_end = 1561
    _globals['_LISTATTACHEDCLUSTERSREQUEST']._serialized_start = 1564
    _globals['_LISTATTACHEDCLUSTERSREQUEST']._serialized_end = 1702
    _globals['_LISTATTACHEDCLUSTERSRESPONSE']._serialized_start = 1705
    _globals['_LISTATTACHEDCLUSTERSRESPONSE']._serialized_end = 1835
    _globals['_DELETEATTACHEDCLUSTERREQUEST']._serialized_start = 1838
    _globals['_DELETEATTACHEDCLUSTERREQUEST']._serialized_end = 2019
    _globals['_GETATTACHEDSERVERCONFIGREQUEST']._serialized_start = 2021
    _globals['_GETATTACHEDSERVERCONFIGREQUEST']._serialized_end = 2126
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST']._serialized_start = 2129
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENREQUEST']._serialized_end = 2459
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENRESPONSE']._serialized_start = 2461
    _globals['_GENERATEATTACHEDCLUSTERAGENTTOKENRESPONSE']._serialized_end = 2566
    _globals['_ATTACHEDCLUSTERS']._serialized_start = 2569
    _globals['_ATTACHEDCLUSTERS']._serialized_end = 4966