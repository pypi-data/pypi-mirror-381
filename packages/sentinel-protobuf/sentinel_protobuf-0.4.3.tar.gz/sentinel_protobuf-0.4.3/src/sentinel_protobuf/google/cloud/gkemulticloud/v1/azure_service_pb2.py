"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkemulticloud/v1/azure_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.gkemulticloud.v1 import azure_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_azure__resources__pb2
from .....google.cloud.gkemulticloud.v1 import common_resources_pb2 as google_dot_cloud_dot_gkemulticloud_dot_v1_dot_common__resources__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/gkemulticloud/v1/azure_service.proto\x12\x1dgoogle.cloud.gkemulticloud.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/gkemulticloud/v1/azure_resources.proto\x1a4google/cloud/gkemulticloud/v1/common_resources.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdd\x01\n\x19CreateAzureClusterRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)gkemulticloud.googleapis.com/AzureCluster\x12G\n\razure_cluster\x18\x02 \x01(\x0b2+.google.cloud.gkemulticloud.v1.AzureClusterB\x03\xe0A\x02\x12\x1d\n\x10azure_cluster_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xb1\x01\n\x19UpdateAzureClusterRequest\x12G\n\razure_cluster\x18\x01 \x01(\x0b2+.google.cloud.gkemulticloud.v1.AzureClusterB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"Y\n\x16GetAzureClusterRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster"\x84\x01\n\x18ListAzureClustersRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)gkemulticloud.googleapis.com/AzureCluster\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"y\n\x19ListAzureClustersResponse\x12C\n\x0eazure_clusters\x18\x01 \x03(\x0b2+.google.cloud.gkemulticloud.v1.AzureCluster\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb4\x01\n\x19DeleteAzureClusterRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08\x12\x0c\n\x04etag\x18\x04 \x01(\t\x12\x1a\n\rignore_errors\x18\x05 \x01(\x08B\x03\xe0A\x01"\xe4\x01\n\x1aCreateAzureNodePoolRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*gkemulticloud.googleapis.com/AzureNodePool\x12J\n\x0fazure_node_pool\x18\x02 \x01(\x0b2,.google.cloud.gkemulticloud.v1.AzureNodePoolB\x03\xe0A\x02\x12\x1f\n\x12azure_node_pool_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xb5\x01\n\x1aUpdateAzureNodePoolRequest\x12J\n\x0fazure_node_pool\x18\x01 \x01(\x0b2,.google.cloud.gkemulticloud.v1.AzureNodePoolB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x124\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"[\n\x17GetAzureNodePoolRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*gkemulticloud.googleapis.com/AzureNodePool"\x86\x01\n\x19ListAzureNodePoolsRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*gkemulticloud.googleapis.com/AzureNodePool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"}\n\x1aListAzureNodePoolsResponse\x12F\n\x10azure_node_pools\x18\x01 \x03(\x0b2,.google.cloud.gkemulticloud.v1.AzureNodePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb6\x01\n\x1aDeleteAzureNodePoolRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*gkemulticloud.googleapis.com/AzureNodePool\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08\x12\x15\n\rallow_missing\x18\x03 \x01(\x08\x12\x0c\n\x04etag\x18\x04 \x01(\t\x12\x1a\n\rignore_errors\x18\x05 \x01(\x08B\x03\xe0A\x01"g\n\x1bGetAzureOpenIdConfigRequest\x12H\n\razure_cluster\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster"f\n\x1aGetAzureJsonWebKeysRequest\x12H\n\razure_cluster\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster"c\n\x1bGetAzureServerConfigRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.gkemulticloud.googleapis.com/AzureServerConfig"\xd8\x01\n\x18CreateAzureClientRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AzureClient\x12E\n\x0cazure_client\x18\x02 \x01(\x0b2*.google.cloud.gkemulticloud.v1.AzureClientB\x03\xe0A\x02\x12\x1c\n\x0fazure_client_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"W\n\x15GetAzureClientRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AzureClient"\x82\x01\n\x17ListAzureClientsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AzureClient\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"v\n\x18ListAzureClientsResponse\x12A\n\razure_clients\x18\x01 \x03(\x0b2*.google.cloud.gkemulticloud.v1.AzureClient\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x88\x01\n\x18DeleteAzureClientRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AzureClient\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"k\n\x1fGenerateAzureAccessTokenRequest\x12H\n\razure_cluster\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster"w\n GenerateAzureAccessTokenResponse\x12\x19\n\x0caccess_token\x18\x01 \x01(\tB\x03\xe0A\x03\x128\n\x0fexpiration_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\xdc\x02\n%GenerateAzureClusterAgentTokenRequest\x12H\n\razure_cluster\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster\x12\x1a\n\rsubject_token\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1f\n\x12subject_token_type\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cnode_pool_id\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x17\n\ngrant_type\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08audience\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05scope\x18\x08 \x01(\tB\x03\xe0A\x01\x12!\n\x14requested_token_type\x18\t \x01(\tB\x03\xe0A\x01\x12\x14\n\x07options\x18\n \x01(\tB\x03\xe0A\x01"f\n&GenerateAzureClusterAgentTokenResponse\x12\x14\n\x0caccess_token\x18\x01 \x01(\t\x12\x12\n\nexpires_in\x18\x02 \x01(\x05\x12\x12\n\ntoken_type\x18\x03 \x01(\t2\xcc#\n\rAzureClusters\x12\xfd\x01\n\x11CreateAzureClient\x127.google.cloud.gkemulticloud.v1.CreateAzureClientRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA \n\x0bAzureClient\x12\x11OperationMetadata\xdaA#parent,azure_client,azure_client_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/azureClients:\x0cazure_client\x12\xb3\x01\n\x0eGetAzureClient\x124.google.cloud.gkemulticloud.v1.GetAzureClientRequest\x1a*.google.cloud.gkemulticloud.v1.AzureClient"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/azureClients/*}\x12\xc6\x01\n\x10ListAzureClients\x126.google.cloud.gkemulticloud.v1.ListAzureClientsRequest\x1a7.google.cloud.gkemulticloud.v1.ListAzureClientsResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/azureClients\x12\xd9\x01\n\x11DeleteAzureClient\x127.google.cloud.gkemulticloud.v1.DeleteAzureClientRequest\x1a\x1d.google.longrunning.Operation"l\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/azureClients/*}\x12\x84\x02\n\x12CreateAzureCluster\x128.google.cloud.gkemulticloud.v1.CreateAzureClusterRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA!\n\x0cAzureCluster\x12\x11OperationMetadata\xdaA%parent,azure_cluster,azure_cluster_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/azureClusters:\razure_cluster\x12\x86\x02\n\x12UpdateAzureCluster\x128.google.cloud.gkemulticloud.v1.UpdateAzureClusterRequest\x1a\x1d.google.longrunning.Operation"\x96\x01\xcaA!\n\x0cAzureCluster\x12\x11OperationMetadata\xdaA\x19azure_cluster,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{azure_cluster.name=projects/*/locations/*/azureClusters/*}:\razure_cluster\x12\xb7\x01\n\x0fGetAzureCluster\x125.google.cloud.gkemulticloud.v1.GetAzureClusterRequest\x1a+.google.cloud.gkemulticloud.v1.AzureCluster"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/azureClusters/*}\x12\xca\x01\n\x11ListAzureClusters\x127.google.cloud.gkemulticloud.v1.ListAzureClustersRequest\x1a8.google.cloud.gkemulticloud.v1.ListAzureClustersResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/azureClusters\x12\xdc\x01\n\x12DeleteAzureCluster\x128.google.cloud.gkemulticloud.v1.DeleteAzureClusterRequest\x1a\x1d.google.longrunning.Operation"m\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/azureClusters/*}\x12\x93\x02\n\x1eGenerateAzureClusterAgentToken\x12D.google.cloud.gkemulticloud.v1.GenerateAzureClusterAgentTokenRequest\x1aE.google.cloud.gkemulticloud.v1.GenerateAzureClusterAgentTokenResponse"d\x82\xd3\xe4\x93\x02^"Y/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}:generateAzureClusterAgentToken:\x01*\x12\xf8\x01\n\x18GenerateAzureAccessToken\x12>.google.cloud.gkemulticloud.v1.GenerateAzureAccessTokenRequest\x1a?.google.cloud.gkemulticloud.v1.GenerateAzureAccessTokenResponse"[\x82\xd3\xe4\x93\x02U\x12S/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}:generateAzureAccessToken\x12\x9e\x02\n\x13CreateAzureNodePool\x129.google.cloud.gkemulticloud.v1.CreateAzureNodePoolRequest\x1a\x1d.google.longrunning.Operation"\xac\x01\xcaA"\n\rAzureNodePool\x12\x11OperationMetadata\xdaA)parent,azure_node_pool,azure_node_pool_id\x82\xd3\xe4\x93\x02U"B/v1/{parent=projects/*/locations/*/azureClusters/*}/azureNodePools:\x0fazure_node_pool\x12\xa0\x02\n\x13UpdateAzureNodePool\x129.google.cloud.gkemulticloud.v1.UpdateAzureNodePoolRequest\x1a\x1d.google.longrunning.Operation"\xae\x01\xcaA"\n\rAzureNodePool\x12\x11OperationMetadata\xdaA\x1bazure_node_pool,update_mask\x82\xd3\xe4\x93\x02e2R/v1/{azure_node_pool.name=projects/*/locations/*/azureClusters/*/azureNodePools/*}:\x0fazure_node_pool\x12\xcb\x01\n\x10GetAzureNodePool\x126.google.cloud.gkemulticloud.v1.GetAzureNodePoolRequest\x1a,.google.cloud.gkemulticloud.v1.AzureNodePool"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1/{name=projects/*/locations/*/azureClusters/*/azureNodePools/*}\x12\xde\x01\n\x12ListAzureNodePools\x128.google.cloud.gkemulticloud.v1.ListAzureNodePoolsRequest\x1a9.google.cloud.gkemulticloud.v1.ListAzureNodePoolsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1/{parent=projects/*/locations/*/azureClusters/*}/azureNodePools\x12\xef\x01\n\x13DeleteAzureNodePool\x129.google.cloud.gkemulticloud.v1.DeleteAzureNodePoolRequest\x1a\x1d.google.longrunning.Operation"~\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v1/{name=projects/*/locations/*/azureClusters/*/azureNodePools/*}\x12\xf9\x01\n\x14GetAzureOpenIdConfig\x12:.google.cloud.gkemulticloud.v1.GetAzureOpenIdConfigRequest\x1a0.google.cloud.gkemulticloud.v1.AzureOpenIdConfig"s\xdaA\razure_cluster\x82\xd3\xe4\x93\x02]\x12[/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}/.well-known/openid-configuration\x12\xda\x01\n\x13GetAzureJsonWebKeys\x129.google.cloud.gkemulticloud.v1.GetAzureJsonWebKeysRequest\x1a/.google.cloud.gkemulticloud.v1.AzureJsonWebKeys"W\xdaA\razure_cluster\x82\xd3\xe4\x93\x02A\x12?/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}/jwks\x12\xc8\x01\n\x14GetAzureServerConfig\x12:.google.cloud.gkemulticloud.v1.GetAzureServerConfigRequest\x1a0.google.cloud.gkemulticloud.v1.AzureServerConfig"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/azureServerConfig}\x1aP\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe4\x01\n!com.google.cloud.gkemulticloud.v1B\x11AzureServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkemulticloud.v1.azure_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.gkemulticloud.v1B\x11AzureServiceProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1'
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster_id']._loaded_options = None
    _globals['_CREATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_UPDATEAZURECLUSTERREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAZURECLUSTERREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAZURECLUSTERREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETAZURECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAZURECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_LISTAZURECLUSTERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAZURECLUSTERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_DELETEAZURECLUSTERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAZURECLUSTERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_DELETEAZURECLUSTERREQUEST'].fields_by_name['ignore_errors']._loaded_options = None
    _globals['_DELETEAZURECLUSTERREQUEST'].fields_by_name['ignore_errors']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*gkemulticloud.googleapis.com/AzureNodePool'
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool']._loaded_options = None
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool_id']._loaded_options = None
    _globals['_CREATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool']._loaded_options = None
    _globals['_UPDATEAZURENODEPOOLREQUEST'].fields_by_name['azure_node_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAZURENODEPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEAZURENODEPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETAZURENODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAZURENODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*gkemulticloud.googleapis.com/AzureNodePool'
    _globals['_LISTAZURENODEPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAZURENODEPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*gkemulticloud.googleapis.com/AzureNodePool'
    _globals['_DELETEAZURENODEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAZURENODEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*gkemulticloud.googleapis.com/AzureNodePool'
    _globals['_DELETEAZURENODEPOOLREQUEST'].fields_by_name['ignore_errors']._loaded_options = None
    _globals['_DELETEAZURENODEPOOLREQUEST'].fields_by_name['ignore_errors']._serialized_options = b'\xe0A\x01'
    _globals['_GETAZUREOPENIDCONFIGREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_GETAZUREOPENIDCONFIGREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_GETAZUREJSONWEBKEYSREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_GETAZUREJSONWEBKEYSREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_GETAZURESERVERCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAZURESERVERCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.gkemulticloud.googleapis.com/AzureServerConfig'
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AzureClient'
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['azure_client']._loaded_options = None
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['azure_client']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['azure_client_id']._loaded_options = None
    _globals['_CREATEAZURECLIENTREQUEST'].fields_by_name['azure_client_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETAZURECLIENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAZURECLIENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AzureClient'
    _globals['_LISTAZURECLIENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAZURECLIENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(gkemulticloud.googleapis.com/AzureClient'
    _globals['_DELETEAZURECLIENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAZURECLIENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(gkemulticloud.googleapis.com/AzureClient'
    _globals['_GENERATEAZUREACCESSTOKENREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_GENERATEAZUREACCESSTOKENREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE'].fields_by_name['access_token']._loaded_options = None
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE'].fields_by_name['access_token']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE'].fields_by_name['expiration_time']._loaded_options = None
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE'].fields_by_name['expiration_time']._serialized_options = b'\xe0A\x03'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['azure_cluster']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['azure_cluster']._serialized_options = b'\xe0A\x02\xfaA+\n)gkemulticloud.googleapis.com/AzureCluster'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['subject_token_type']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['node_pool_id']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['node_pool_id']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['grant_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['audience']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['scope']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['requested_token_type']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._loaded_options = None
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_AZURECLUSTERS']._loaded_options = None
    _globals['_AZURECLUSTERS']._serialized_options = b'\xcaA\x1cgkemulticloud.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureClient']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureClient']._serialized_options = b'\xcaA \n\x0bAzureClient\x12\x11OperationMetadata\xdaA#parent,azure_client,azure_client_id\x82\xd3\xe4\x93\x02@"0/v1/{parent=projects/*/locations/*}/azureClients:\x0cazure_client'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureClient']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureClient']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v1/{name=projects/*/locations/*/azureClients/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureClients']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureClients']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v1/{parent=projects/*/locations/*}/azureClients'
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureClient']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureClient']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v1/{name=projects/*/locations/*/azureClients/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureCluster']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureCluster']._serialized_options = b'\xcaA!\n\x0cAzureCluster\x12\x11OperationMetadata\xdaA%parent,azure_cluster,azure_cluster_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/azureClusters:\razure_cluster'
    _globals['_AZURECLUSTERS'].methods_by_name['UpdateAzureCluster']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['UpdateAzureCluster']._serialized_options = b'\xcaA!\n\x0cAzureCluster\x12\x11OperationMetadata\xdaA\x19azure_cluster,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{azure_cluster.name=projects/*/locations/*/azureClusters/*}:\razure_cluster'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureCluster']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureCluster']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/azureClusters/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureClusters']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureClusters']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/azureClusters'
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureCluster']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureCluster']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/azureClusters/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['GenerateAzureClusterAgentToken']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GenerateAzureClusterAgentToken']._serialized_options = b'\x82\xd3\xe4\x93\x02^"Y/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}:generateAzureClusterAgentToken:\x01*'
    _globals['_AZURECLUSTERS'].methods_by_name['GenerateAzureAccessToken']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GenerateAzureAccessToken']._serialized_options = b'\x82\xd3\xe4\x93\x02U\x12S/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}:generateAzureAccessToken'
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureNodePool']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['CreateAzureNodePool']._serialized_options = b'\xcaA"\n\rAzureNodePool\x12\x11OperationMetadata\xdaA)parent,azure_node_pool,azure_node_pool_id\x82\xd3\xe4\x93\x02U"B/v1/{parent=projects/*/locations/*/azureClusters/*}/azureNodePools:\x0fazure_node_pool'
    _globals['_AZURECLUSTERS'].methods_by_name['UpdateAzureNodePool']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['UpdateAzureNodePool']._serialized_options = b'\xcaA"\n\rAzureNodePool\x12\x11OperationMetadata\xdaA\x1bazure_node_pool,update_mask\x82\xd3\xe4\x93\x02e2R/v1/{azure_node_pool.name=projects/*/locations/*/azureClusters/*/azureNodePools/*}:\x0fazure_node_pool'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureNodePool']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureNodePool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1/{name=projects/*/locations/*/azureClusters/*/azureNodePools/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureNodePools']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['ListAzureNodePools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1/{parent=projects/*/locations/*/azureClusters/*}/azureNodePools'
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureNodePool']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['DeleteAzureNodePool']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v1/{name=projects/*/locations/*/azureClusters/*/azureNodePools/*}'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureOpenIdConfig']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureOpenIdConfig']._serialized_options = b'\xdaA\razure_cluster\x82\xd3\xe4\x93\x02]\x12[/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}/.well-known/openid-configuration'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureJsonWebKeys']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureJsonWebKeys']._serialized_options = b'\xdaA\razure_cluster\x82\xd3\xe4\x93\x02A\x12?/v1/{azure_cluster=projects/*/locations/*/azureClusters/*}/jwks'
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureServerConfig']._loaded_options = None
    _globals['_AZURECLUSTERS'].methods_by_name['GetAzureServerConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/azureServerConfig}'
    _globals['_CREATEAZURECLUSTERREQUEST']._serialized_start = 440
    _globals['_CREATEAZURECLUSTERREQUEST']._serialized_end = 661
    _globals['_UPDATEAZURECLUSTERREQUEST']._serialized_start = 664
    _globals['_UPDATEAZURECLUSTERREQUEST']._serialized_end = 841
    _globals['_GETAZURECLUSTERREQUEST']._serialized_start = 843
    _globals['_GETAZURECLUSTERREQUEST']._serialized_end = 932
    _globals['_LISTAZURECLUSTERSREQUEST']._serialized_start = 935
    _globals['_LISTAZURECLUSTERSREQUEST']._serialized_end = 1067
    _globals['_LISTAZURECLUSTERSRESPONSE']._serialized_start = 1069
    _globals['_LISTAZURECLUSTERSRESPONSE']._serialized_end = 1190
    _globals['_DELETEAZURECLUSTERREQUEST']._serialized_start = 1193
    _globals['_DELETEAZURECLUSTERREQUEST']._serialized_end = 1373
    _globals['_CREATEAZURENODEPOOLREQUEST']._serialized_start = 1376
    _globals['_CREATEAZURENODEPOOLREQUEST']._serialized_end = 1604
    _globals['_UPDATEAZURENODEPOOLREQUEST']._serialized_start = 1607
    _globals['_UPDATEAZURENODEPOOLREQUEST']._serialized_end = 1788
    _globals['_GETAZURENODEPOOLREQUEST']._serialized_start = 1790
    _globals['_GETAZURENODEPOOLREQUEST']._serialized_end = 1881
    _globals['_LISTAZURENODEPOOLSREQUEST']._serialized_start = 1884
    _globals['_LISTAZURENODEPOOLSREQUEST']._serialized_end = 2018
    _globals['_LISTAZURENODEPOOLSRESPONSE']._serialized_start = 2020
    _globals['_LISTAZURENODEPOOLSRESPONSE']._serialized_end = 2145
    _globals['_DELETEAZURENODEPOOLREQUEST']._serialized_start = 2148
    _globals['_DELETEAZURENODEPOOLREQUEST']._serialized_end = 2330
    _globals['_GETAZUREOPENIDCONFIGREQUEST']._serialized_start = 2332
    _globals['_GETAZUREOPENIDCONFIGREQUEST']._serialized_end = 2435
    _globals['_GETAZUREJSONWEBKEYSREQUEST']._serialized_start = 2437
    _globals['_GETAZUREJSONWEBKEYSREQUEST']._serialized_end = 2539
    _globals['_GETAZURESERVERCONFIGREQUEST']._serialized_start = 2541
    _globals['_GETAZURESERVERCONFIGREQUEST']._serialized_end = 2640
    _globals['_CREATEAZURECLIENTREQUEST']._serialized_start = 2643
    _globals['_CREATEAZURECLIENTREQUEST']._serialized_end = 2859
    _globals['_GETAZURECLIENTREQUEST']._serialized_start = 2861
    _globals['_GETAZURECLIENTREQUEST']._serialized_end = 2948
    _globals['_LISTAZURECLIENTSREQUEST']._serialized_start = 2951
    _globals['_LISTAZURECLIENTSREQUEST']._serialized_end = 3081
    _globals['_LISTAZURECLIENTSRESPONSE']._serialized_start = 3083
    _globals['_LISTAZURECLIENTSRESPONSE']._serialized_end = 3201
    _globals['_DELETEAZURECLIENTREQUEST']._serialized_start = 3204
    _globals['_DELETEAZURECLIENTREQUEST']._serialized_end = 3340
    _globals['_GENERATEAZUREACCESSTOKENREQUEST']._serialized_start = 3342
    _globals['_GENERATEAZUREACCESSTOKENREQUEST']._serialized_end = 3449
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE']._serialized_start = 3451
    _globals['_GENERATEAZUREACCESSTOKENRESPONSE']._serialized_end = 3570
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST']._serialized_start = 3573
    _globals['_GENERATEAZURECLUSTERAGENTTOKENREQUEST']._serialized_end = 3921
    _globals['_GENERATEAZURECLUSTERAGENTTOKENRESPONSE']._serialized_start = 3923
    _globals['_GENERATEAZURECLUSTERAGENTTOKENRESPONSE']._serialized_end = 4025
    _globals['_AZURECLUSTERS']._serialized_start = 4028
    _globals['_AZURECLUSTERS']._serialized_end = 8584