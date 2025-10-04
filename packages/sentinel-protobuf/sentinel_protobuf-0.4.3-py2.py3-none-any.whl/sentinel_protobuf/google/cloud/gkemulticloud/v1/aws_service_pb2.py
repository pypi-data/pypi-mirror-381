"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkemulticloud/v1/aws_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkemulticloud.v1 import aws_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_aws__resources__pb2
from .....google.cloud.gkemulticloud.v1 import common_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_common__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/gkemulticloud/v1/aws_service.proto\x12\x1dgoogle.cloud.gkemulticloud.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/gkemulticloud/v1/aws_resources.proto\x1a4google/cloud/gkemulticloud/v1/common_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd3\x01\n\x17CreateAwsClusterRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'gkemulticloud.googleapis.com/AwsCluster\x12C\n\x0baws_cluster\x18\x02 \x01(\x0b2).google.cloud.gkemulticloud.v1.AwsClusterB\x03\xe0A\x02\x12\x1b\n\x0eaws_cluster_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xab\x01\n\x17UpdateAwsClusterRequest\x12C\n\x0baws_cluster\x18\x01 \x01(\x0b2).google.cloud.gkemulticloud.v1.AwsClusterB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"U\n\x14GetAwsClusterRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster"\x80\x01\n\x16ListAwsClustersRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\x12\'gkemulticloud.googleapis.com/AwsCluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"s\n\x17ListAwsClustersResponse\x12?\n\x0caws_clusters\x18\x01 \x03(\x0b2).google.cloud.gkemulticloud.v1.AwsCluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb0\x01\n\x17DeleteAwsClusterRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\x12\x1a\n\rignore_errors\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x0c\n\x04etag\x18\x04 \x01(\t"\xda\x01\n\x18CreateAwsNodePoolRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AwsNodePool\x12F\n\raws_node_pool\x18\x02 \x01(\x0b2*.google.cloud.gkemulticloud.v1.AwsNodePoolB\x03\xe0A\x02\x12\x1d\n\x10aws_node_pool_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xaf\x01\n\x18UpdateAwsNodePoolRequest\x12F\n\raws_node_pool\x18\x01 \x01(\x0b2*.google.cloud.gkemulticloud.v1.AwsNodePoolB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"|\n RollbackAwsNodePoolUpdateRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool\x12\x18\n\x0brespect_pdb\x18\x02 \x01(\x08B\x03\xe0A\x01"W\n\x15GetAwsNodePoolRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool"\x82\x01\n\x17ListAwsNodePoolsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AwsNodePool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"w\n\x18ListAwsNodePoolsResponse\x12B\n\x0eaws_node_pools\x18\x01 \x03(\x0b2*.google.cloud.gkemulticloud.v1.AwsNodePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb2\x01\n\x18DeleteAwsNodePoolRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\x12\x1a\n\rignore_errors\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x0c\n\x04etag\x18\x04 \x01(\t"a\n\x19GetAwsOpenIdConfigRequest\x12D\n\x0baws_cluster\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster"`\n\x18GetAwsJsonWebKeysRequest\x12D\n\x0baws_cluster\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster"_\n\x19GetAwsServerConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AwsServerConfig"e\n\x1dGenerateAwsAccessTokenRequest\x12D\n\x0baws_cluster\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster"u\n\x1eGenerateAwsAccessTokenResponse\x12\x19\n\x0caccess_token\x18\x01 \x01(\tB\x03\xe0A\x03\x128\n\x0fexpiration_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\xd6\x02\n#GenerateAwsClusterAgentTokenRequest\x12D\n\x0baws_cluster\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'gkemulticloud.googleapis.com/AwsCluster\x12\x1a\n\rsubject_token\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12subject_token_type\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cnode_pool_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x17\n\ngrant_type\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08audience\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05scope\x18\x08 \x01(\tB\x03\xe0A\x01\x12!\n\x14requested_token_type\x18\t \x01(\tB\x03\xe0A\x01\x12\x14\n\x07options\x18\n \x01(\tB\x03\xe0A\x01"d\n$GenerateAwsClusterAgentTokenResponse\x12\x14\n\x0caccess_token\x18\x01 \x01(\t\x12\x12\n\nexpires_in\x18\x02 \x01(\x05\x12\x12\n\ntoken_type\x18\x03 \x01(\t2\xa9\x1d\n\x0bAwsClusters\x12\xf6\x01\n\x10CreateAwsCluster\x126.google.cloud.gkemulticloud.v1.CreateAwsClusterRequest\x1a\x1d.google.longrunning.Operation"\x8a\x01\xcaA\x1f\n\nAwsCluster\x12\x11OperationMetadata\xdaA!parent,aws_cluster,aws_cluster_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/awsClusters:\x0baws_cluster\x12\xf8\x01\n\x10UpdateAwsCluster\x126.google.cloud.gkemulticloud.v1.UpdateAwsClusterRequest\x1a\x1d.google.longrunning.Operation"\x8c\x01\xcaA\x1f\n\nAwsCluster\x12\x11OperationMetadata\xdaA\x17aws_cluster,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{aws_cluster.name=projects/*/locations/*/awsClusters/*}:\x0baws_cluster\x12\xaf\x01\n\rGetAwsCluster\x123.google.cloud.gkemulticloud.v1.GetAwsClusterRequest\x1a).google.cloud.gkemulticloud.v1.AwsCluster">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/awsClusters/*}\x12\xc2\x01\n\x0fListAwsClusters\x125.google.cloud.gkemulticloud.v1.ListAwsClustersRequest\x1a6.google.cloud.gkemulticloud.v1.ListAwsClustersResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/awsClusters\x12\xd6\x01\n\x10DeleteAwsCluster\x126.google.cloud.gkemulticloud.v1.DeleteAwsClusterRequest\x1a\x1d.google.longrunning.Operation"k\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/awsClusters/*}\x12\x87\x02\n\x1cGenerateAwsClusterAgentToken\x12B.google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenRequest\x1aC.google.cloud.gkemulticloud.v1.GenerateAwsClusterAgentTokenResponse"^\x82\xd3\xe4\x93\x02X"S/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}:generateAwsClusterAgentToken:\x01*\x12\xec\x01\n\x16GenerateAwsAccessToken\x12<.google.cloud.gkemulticloud.v1.GenerateAwsAccessTokenRequest\x1a=.google.cloud.gkemulticloud.v1.GenerateAwsAccessTokenResponse"U\x82\xd3\xe4\x93\x02O\x12M/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}:generateAwsAccessToken\x12\x8e\x02\n\x11CreateAwsNodePool\x127.google.cloud.gkemulticloud.v1.CreateAwsNodePoolRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA%parent,aws_node_pool,aws_node_pool_id\x82\xd3\xe4\x93\x02O">/v1/{parent=projects/*/locations/*/awsClusters/*}/awsNodePools:\raws_node_pool\x12\x90\x02\n\x11UpdateAwsNodePool\x127.google.cloud.gkemulticloud.v1.UpdateAwsNodePoolRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA\x19aws_node_pool,update_mask\x82\xd3\xe4\x93\x02]2L/v1/{aws_node_pool.name=projects/*/locations/*/awsClusters/*/awsNodePools/*}:\raws_node_pool\x12\xf9\x01\n\x19RollbackAwsNodePoolUpdate\x12?.google.cloud.gkemulticloud.v1.RollbackAwsNodePoolUpdateRequest\x1a\x1d.google.longrunning.Operation"|\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}:rollback:\x01*\x12\xc1\x01\n\x0eGetAwsNodePool\x124.google.cloud.gkemulticloud.v1.GetAwsNodePoolRequest\x1a*.google.cloud.gkemulticloud.v1.AwsNodePool"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}\x12\xd4\x01\n\x10ListAwsNodePools\x126.google.cloud.gkemulticloud.v1.ListAwsNodePoolsRequest\x1a7.google.cloud.gkemulticloud.v1.ListAwsNodePoolsResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/awsClusters/*}/awsNodePools\x12\xe7\x01\n\x11DeleteAwsNodePool\x127.google.cloud.gkemulticloud.v1.DeleteAwsNodePoolRequest\x1a\x1d.google.longrunning.Operation"z\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}\x12\xdf\x01\n\x12GetAwsOpenIdConfig\x128.google.cloud.gkemulticloud.v1.GetAwsOpenIdConfigRequest\x1a..google.cloud.gkemulticloud.v1.AwsOpenIdConfig"_\x82\xd3\xe4\x93\x02Y\x12W/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}/.well-known/openid-configuration\x12\xc0\x01\n\x11GetAwsJsonWebKeys\x127.google.cloud.gkemulticloud.v1.GetAwsJsonWebKeysRequest\x1a-.google.cloud.gkemulticloud.v1.AwsJsonWebKeys"C\x82\xd3\xe4\x93\x02=\x12;/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}/jwks\x12\xc0\x01\n\x12GetAwsServerConfig\x128.google.cloud.gkemulticloud.v1.GetAwsServerConfigRequest\x1a..google.cloud.gkemulticloud.v1.AwsServerConfig"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/awsServerConfig}\x1aP\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe2\x01\n!com.google.cloud.gkemulticloud.v1B\x0fAwsServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkemulticloud.v1.aws_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.gkemulticloud.v1B\x0fAwsServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1'
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster_id']._loaded_options = None
    _globals['_CREATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_UPDATEAWSCLUSTERREQUEST'].fields_by_name['aws_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAWSCLUSTERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAWSCLUSTERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETAWSCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAWSCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_LISTAWSCLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAWSCLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\x12'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_DELETEAWSCLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAWSCLUSTERREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_DELETEAWSCLUSTERREQUEST'].fields_by_name['ignore_errors']._loaded_options = None
    _globals['_DELETEAWSCLUSTERREQUEST'].fields_by_name['ignore_errors']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AwsNodePool'
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool']._loaded_options = None
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool_id']._loaded_options = None
    _globals['_CREATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool']._loaded_options = None
    _globals['_UPDATEAWSNODEPOOLREQUEST'].fields_by_name['aws_node_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAWSNODEPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAWSNODEPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool'
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST'].fields_by_name['respect_pdb']._loaded_options = None
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST'].fields_by_name['respect_pdb']._serialized_options = b'\xe0A\x01'
    _globals['_GETAWSNODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAWSNODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool'
    _globals['_LISTAWSNODEPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAWSNODEPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AwsNodePool'
    _globals['_DELETEAWSNODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAWSNODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AwsNodePool'
    _globals['_DELETEAWSNODEPOOLREQUEST'].fields_by_name['ignore_errors']._loaded_options = None
    _globals['_DELETEAWSNODEPOOLREQUEST'].fields_by_name['ignore_errors']._serialized_options = b'\xe0A\x01'
    _globals['_GETAWSOPENIDCONFIGREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_GETAWSOPENIDCONFIGREQUEST'].fields_by_name['aws_cluster']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_GETAWSJSONWEBKEYSREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_GETAWSJSONWEBKEYSREQUEST'].fields_by_name['aws_cluster']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_GETAWSSERVERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAWSSERVERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,gkemulticloud.googleapis.com/AwsServerConfig'
    _globals['_GENERATEAWSACCESSTOKENREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_GENERATEAWSACCESSTOKENREQUEST'].fields_by_name['aws_cluster']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_GENERATEAWSACCESSTOKENRESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_GENERATEAWSACCESSTOKENRESPONSE'].fields_by_name['access_token']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEAWSACCESSTOKENRESPONSE'].fields_by_name['expiration_time']._loaded_options = None
    _globals['_GENERATEAWSACCESSTOKENRESPONSE'].fields_by_name['expiration_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['aws_cluster']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['aws_cluster']._serialized_options = b"\xe0A\x02\xfaA)\n'gkemulticloud.googleapis.com/AwsCluster"
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['node_pool_id']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['node_pool_id']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._loaded_options = None
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_AWSCLUSTERS']._loaded_options = None
    _globals['_AWSCLUSTERS']._serialized_options = b'\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AWSCLUSTERS'].methods_by_name['CreateAwsCluster']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['CreateAwsCluster']._serialized_options = b'\xcaA\x1f\n\nAwsCluster\x12\x11OperationMetadata\xdaA!parent,aws_cluster,aws_cluster_id\x82\xd3\xe4\x93\x02>"//v1/{parent=projects/*/locations/*}/awsClusters:\x0baws_cluster'
    _globals['_AWSCLUSTERS'].methods_by_name['UpdateAwsCluster']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['UpdateAwsCluster']._serialized_options = b'\xcaA\x1f\n\nAwsCluster\x12\x11OperationMetadata\xdaA\x17aws_cluster,update_mask\x82\xd3\xe4\x93\x02J2;/v1/{aws_cluster.name=projects/*/locations/*/awsClusters/*}:\x0baws_cluster'
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsCluster']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v1/{name=projects/*/locations/*/awsClusters/*}'
    _globals['_AWSCLUSTERS'].methods_by_name['ListAwsClusters']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['ListAwsClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/awsClusters'
    _globals['_AWSCLUSTERS'].methods_by_name['DeleteAwsCluster']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['DeleteAwsCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/awsClusters/*}'
    _globals['_AWSCLUSTERS'].methods_by_name['GenerateAwsClusterAgentToken']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GenerateAwsClusterAgentToken']._serialized_options = b'\x82\xd3\xe4\x93\x02X"S/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}:generateAwsClusterAgentToken:\x01*'
    _globals['_AWSCLUSTERS'].methods_by_name['GenerateAwsAccessToken']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GenerateAwsAccessToken']._serialized_options = b'\x82\xd3\xe4\x93\x02O\x12M/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}:generateAwsAccessToken'
    _globals['_AWSCLUSTERS'].methods_by_name['CreateAwsNodePool']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['CreateAwsNodePool']._serialized_options = b'\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA%parent,aws_node_pool,aws_node_pool_id\x82\xd3\xe4\x93\x02O">/v1/{parent=projects/*/locations/*/awsClusters/*}/awsNodePools:\raws_node_pool'
    _globals['_AWSCLUSTERS'].methods_by_name['UpdateAwsNodePool']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['UpdateAwsNodePool']._serialized_options = b'\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA\x19aws_node_pool,update_mask\x82\xd3\xe4\x93\x02]2L/v1/{aws_node_pool.name=projects/*/locations/*/awsClusters/*/awsNodePools/*}:\raws_node_pool'
    _globals['_AWSCLUSTERS'].methods_by_name['RollbackAwsNodePoolUpdate']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['RollbackAwsNodePoolUpdate']._serialized_options = b'\xcaA \n\x0bAwsNodePool\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02L"G/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}:rollback:\x01*'
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsNodePool']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsNodePool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}'
    _globals['_AWSCLUSTERS'].methods_by_name['ListAwsNodePools']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['ListAwsNodePools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1/{parent=projects/*/locations/*/awsClusters/*}/awsNodePools'
    _globals['_AWSCLUSTERS'].methods_by_name['DeleteAwsNodePool']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['DeleteAwsNodePool']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1/{name=projects/*/locations/*/awsClusters/*/awsNodePools/*}'
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsOpenIdConfig']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsOpenIdConfig']._serialized_options = b'\x82\xd3\xe4\x93\x02Y\x12W/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}/.well-known/openid-configuration'
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsJsonWebKeys']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsJsonWebKeys']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/v1/{aws_cluster=projects/*/locations/*/awsClusters/*}/jwks'
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsServerConfig']._loaded_options = None
    _globals['_AWSCLUSTERS'].methods_by_name['GetAwsServerConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/awsServerConfig}'
    _globals['_CREATEAWSCLUSTERREQUEST']._serialized_start = 436
    _globals['_CREATEAWSCLUSTERREQUEST']._serialized_end = 647
    _globals['_UPDATEAWSCLUSTERREQUEST']._serialized_start = 650
    _globals['_UPDATEAWSCLUSTERREQUEST']._serialized_end = 821
    _globals['_GETAWSCLUSTERREQUEST']._serialized_start = 823
    _globals['_GETAWSCLUSTERREQUEST']._serialized_end = 908
    _globals['_LISTAWSCLUSTERSREQUEST']._serialized_start = 911
    _globals['_LISTAWSCLUSTERSREQUEST']._serialized_end = 1039
    _globals['_LISTAWSCLUSTERSRESPONSE']._serialized_start = 1041
    _globals['_LISTAWSCLUSTERSRESPONSE']._serialized_end = 1156
    _globals['_DELETEAWSCLUSTERREQUEST']._serialized_start = 1159
    _globals['_DELETEAWSCLUSTERREQUEST']._serialized_end = 1335
    _globals['_CREATEAWSNODEPOOLREQUEST']._serialized_start = 1338
    _globals['_CREATEAWSNODEPOOLREQUEST']._serialized_end = 1556
    _globals['_UPDATEAWSNODEPOOLREQUEST']._serialized_start = 1559
    _globals['_UPDATEAWSNODEPOOLREQUEST']._serialized_end = 1734
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST']._serialized_start = 1736
    _globals['_ROLLBACKAWSNODEPOOLUPDATEREQUEST']._serialized_end = 1860
    _globals['_GETAWSNODEPOOLREQUEST']._serialized_start = 1862
    _globals['_GETAWSNODEPOOLREQUEST']._serialized_end = 1949
    _globals['_LISTAWSNODEPOOLSREQUEST']._serialized_start = 1952
    _globals['_LISTAWSNODEPOOLSREQUEST']._serialized_end = 2082
    _globals['_LISTAWSNODEPOOLSRESPONSE']._serialized_start = 2084
    _globals['_LISTAWSNODEPOOLSRESPONSE']._serialized_end = 2203
    _globals['_DELETEAWSNODEPOOLREQUEST']._serialized_start = 2206
    _globals['_DELETEAWSNODEPOOLREQUEST']._serialized_end = 2384
    _globals['_GETAWSOPENIDCONFIGREQUEST']._serialized_start = 2386
    _globals['_GETAWSOPENIDCONFIGREQUEST']._serialized_end = 2483
    _globals['_GETAWSJSONWEBKEYSREQUEST']._serialized_start = 2485
    _globals['_GETAWSJSONWEBKEYSREQUEST']._serialized_end = 2581
    _globals['_GETAWSSERVERCONFIGREQUEST']._serialized_start = 2583
    _globals['_GETAWSSERVERCONFIGREQUEST']._serialized_end = 2678
    _globals['_GENERATEAWSACCESSTOKENREQUEST']._serialized_start = 2680
    _globals['_GENERATEAWSACCESSTOKENREQUEST']._serialized_end = 2781
    _globals['_GENERATEAWSACCESSTOKENRESPONSE']._serialized_start = 2783
    _globals['_GENERATEAWSACCESSTOKENRESPONSE']._serialized_end = 2900
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST']._serialized_start = 2903
    _globals['_GENERATEAWSCLUSTERAGENTTOKENREQUEST']._serialized_end = 3245
    _globals['_GENERATEAWSCLUSTERAGENTTOKENRESPONSE']._serialized_start = 3247
    _globals['_GENERATEAWSCLUSTERAGENTTOKENRESPONSE']._serialized_end = 3347
    _globals['_AWSCLUSTERS']._serialized_start = 3350
    _globals['_AWSCLUSTERS']._serialized_end = 7103