"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/blockchainnodeengine/v1/blockchainnodeengine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/blockchainnodeengine/v1/blockchainnodeengine.proto\x12$google.cloud.blockchainnodeengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa3\x1a\n\x0eBlockchainNode\x12`\n\x10ethereum_details\x18\x07 \x01(\x0b2D.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetailsH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x06labels\x18\x04 \x03(\x0b2@.google.cloud.blockchainnodeengine.v1.BlockchainNode.LabelsEntry\x12f\n\x0fblockchain_type\x18\x05 \x01(\x0e2C.google.cloud.blockchainnodeengine.v1.BlockchainNode.BlockchainTypeB\x03\xe0A\x05H\x01\x88\x01\x01\x12a\n\x0fconnection_info\x18\x06 \x01(\x0b2C.google.cloud.blockchainnodeengine.v1.BlockchainNode.ConnectionInfoB\x03\xe0A\x03\x12N\n\x05state\x18\x08 \x01(\x0e2:.google.cloud.blockchainnodeengine.v1.BlockchainNode.StateB\x03\xe0A\x03\x12.\n\x1fprivate_service_connect_enabled\x18\x0c \x01(\x08B\x05\x18\x01\xe0A\x01\x1a\xf9\x01\n\x0eConnectionInfo\x12l\n\rendpoint_info\x18\x02 \x01(\x0b2P.google.cloud.blockchainnodeengine.v1.BlockchainNode.ConnectionInfo.EndpointInfoB\x03\xe0A\x03\x12\x1f\n\x12service_attachment\x18\x03 \x01(\tB\x03\xe0A\x03\x1aX\n\x0cEndpointInfo\x12"\n\x15json_rpc_api_endpoint\x18\x01 \x01(\tB\x03\xe0A\x03\x12$\n\x17websockets_api_endpoint\x18\x02 \x01(\tB\x03\xe0A\x03\x1a\xe2\x0f\n\x0fEthereumDetails\x12h\n\x0cgeth_details\x18\x08 \x01(\x0b2P.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.GethDetailsH\x00\x12g\n\x07network\x18\x01 \x01(\x0e2L.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.NetworkB\x03\xe0A\x05H\x01\x88\x01\x01\x12j\n\tnode_type\x18\x02 \x01(\x0e2M.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.NodeTypeB\x03\xe0A\x05H\x02\x88\x01\x01\x12x\n\x10execution_client\x18\x03 \x01(\x0e2T.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.ExecutionClientB\x03\xe0A\x05H\x03\x88\x01\x01\x12x\n\x10consensus_client\x18\x04 \x01(\x0e2T.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.ConsensusClientB\x03\xe0A\x05H\x04\x88\x01\x01\x12"\n\x10api_enable_admin\x18\x05 \x01(\x08B\x03\xe0A\x05H\x05\x88\x01\x01\x12"\n\x10api_enable_debug\x18\x06 \x01(\x08B\x03\xe0A\x05H\x06\x88\x01\x01\x12~\n\x14additional_endpoints\x18\x07 \x01(\x0b2V.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.EthereumEndpointsB\x03\xe0A\x03H\x07\x88\x01\x01\x12s\n\x10validator_config\x18\n \x01(\x0b2T.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.ValidatorConfigH\x08\x88\x01\x01\x1a\x96\x02\n\x0bGethDetails\x12\x91\x01\n\x17garbage_collection_mode\x18\x01 \x01(\x0e2f.google.cloud.blockchainnodeengine.v1.BlockchainNode.EthereumDetails.GethDetails.GarbageCollectionModeB\x03\xe0A\x05H\x00\x88\x01\x01"W\n\x15GarbageCollectionMode\x12\'\n#GARBAGE_COLLECTION_MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04FULL\x10\x01\x12\x0b\n\x07ARCHIVE\x10\x02B\x1a\n\x18_garbage_collection_mode\x1a\xa9\x01\n\x11EthereumEndpoints\x12 \n\x13beacon_api_endpoint\x18\x01 \x01(\tB\x03\xe0A\x03\x123\n&beacon_prometheus_metrics_api_endpoint\x18\x02 \x01(\tB\x03\xe0A\x03\x12=\n0execution_client_prometheus_metrics_api_endpoint\x18\x03 \x01(\tB\x03\xe0A\x03\x1a\x8e\x01\n\x0fValidatorConfig\x12\x16\n\x0emev_relay_urls\x18\x01 \x03(\t\x12\'\n\x18managed_validator_client\x18\x02 \x01(\x08B\x05\x18\x01\xe0A\x05\x12!\n\x14beacon_fee_recipient\x18\x03 \x01(\tH\x00\x88\x01\x01B\x17\n\x15_beacon_fee_recipient"x\n\x07Network\x12\x17\n\x13NETWORK_UNSPECIFIED\x10\x00\x12\x0b\n\x07MAINNET\x10\x01\x12\x1d\n\x15TESTNET_GOERLI_PRATER\x10\x02\x1a\x02\x08\x01\x12\x13\n\x0fTESTNET_SEPOLIA\x10\x03\x12\x13\n\x0fTESTNET_HOLESKY\x10\x04"G\n\x08NodeType\x12\x19\n\x15NODE_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05LIGHT\x10\x01\x12\x08\n\x04FULL\x10\x02\x12\x0b\n\x07ARCHIVE\x10\x03"I\n\x0fExecutionClient\x12 \n\x1cEXECUTION_CLIENT_UNSPECIFIED\x10\x00\x12\x08\n\x04GETH\x10\x01\x12\n\n\x06ERIGON\x10\x02"C\n\x0fConsensusClient\x12 \n\x1cCONSENSUS_CLIENT_UNSPECIFIED\x10\x00\x12\x0e\n\nLIGHTHOUSE\x10\x01B\x1a\n\x18execution_client_detailsB\n\n\x08_networkB\x0c\n\n_node_typeB\x13\n\x11_execution_clientB\x13\n\x11_consensus_clientB\x13\n\x11_api_enable_adminB\x13\n\x11_api_enable_debugB\x17\n\x15_additional_endpointsB\x13\n\x11_validator_config\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"?\n\x0eBlockchainType\x12\x1f\n\x1bBLOCKCHAIN_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ETHEREUM\x10\x01"\x8d\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\x0c\n\x08DELETING\x10\x02\x12\x0b\n\x07RUNNING\x10\x04\x12\t\n\x05ERROR\x10\x05\x12\x0c\n\x08UPDATING\x10\x06\x12\r\n\tREPAIRING\x10\x07\x12\x0f\n\x0bRECONCILING\x10\x08\x12\x0b\n\x07SYNCING\x10\t:\x82\x01\xeaA\x7f\n2blockchainnodeengine.googleapis.com/BlockchainNode\x12Iprojects/{project}/locations/{location}/blockchainNodes/{blockchain_node}B\x19\n\x17blockchain_type_detailsB\x12\n\x10_blockchain_type"\xb1\x01\n\x1aListBlockchainNodesRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122blockchainnodeengine.googleapis.com/BlockchainNode\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x9b\x01\n\x1bListBlockchainNodesResponse\x12N\n\x10blockchain_nodes\x18\x01 \x03(\x0b24.google.cloud.blockchainnodeengine.v1.BlockchainNode\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"d\n\x18GetBlockchainNodeRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2blockchainnodeengine.googleapis.com/BlockchainNode"\xf7\x01\n\x1bCreateBlockchainNodeRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122blockchainnodeengine.googleapis.com/BlockchainNode\x12\x1f\n\x12blockchain_node_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x0fblockchain_node\x18\x03 \x01(\x0b24.google.cloud.blockchainnodeengine.v1.BlockchainNodeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xc0\x01\n\x1bUpdateBlockchainNodeRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12R\n\x0fblockchain_node\x18\x02 \x01(\x0b24.google.cloud.blockchainnodeengine.v1.BlockchainNodeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x80\x01\n\x1bDeleteBlockchainNodeRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2blockchainnodeengine.googleapis.com/BlockchainNode\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xc8\n\n\x14BlockchainNodeEngine\x12\xe0\x01\n\x13ListBlockchainNodes\x12@.google.cloud.blockchainnodeengine.v1.ListBlockchainNodesRequest\x1aA.google.cloud.blockchainnodeengine.v1.ListBlockchainNodesResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/blockchainNodes\x12\xcd\x01\n\x11GetBlockchainNode\x12>.google.cloud.blockchainnodeengine.v1.GetBlockchainNodeRequest\x1a4.google.cloud.blockchainnodeengine.v1.BlockchainNode"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/blockchainNodes/*}\x12\x99\x02\n\x14CreateBlockchainNode\x12A.google.cloud.blockchainnodeengine.v1.CreateBlockchainNodeRequest\x1a\x1d.google.longrunning.Operation"\x9e\x01\xcaA#\n\x0eBlockchainNode\x12\x11OperationMetadata\xdaA)parent,blockchain_node,blockchain_node_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/blockchainNodes:\x0fblockchain_node\x12\x9b\x02\n\x14UpdateBlockchainNode\x12A.google.cloud.blockchainnodeengine.v1.UpdateBlockchainNodeRequest\x1a\x1d.google.longrunning.Operation"\xa0\x01\xcaA#\n\x0eBlockchainNode\x12\x11OperationMetadata\xdaA\x1bblockchain_node,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{blockchain_node.name=projects/*/locations/*/blockchainNodes/*}:\x0fblockchain_node\x12\xe9\x01\n\x14DeleteBlockchainNode\x12A.google.cloud.blockchainnodeengine.v1.DeleteBlockchainNodeRequest\x1a\x1d.google.longrunning.Operation"o\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/blockchainNodes/*}\x1aW\xcaA#blockchainnodeengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n(com.google.cloud.blockchainnodeengine.v1B\x19BlockchainnodeengineProtoP\x01Z\\cloud.google.com/go/blockchainnodeengine/apiv1/blockchainnodeenginepb;blockchainnodeenginepb\xaa\x02$Google.Cloud.BlockchainNodeEngine.V1\xca\x02$Google\\Cloud\\BlockchainNodeEngine\\V1\xea\x02\'Google::Cloud::BlockchainNodeEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.blockchainnodeengine.v1.blockchainnodeengine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.blockchainnodeengine.v1B\x19BlockchainnodeengineProtoP\x01Z\\cloud.google.com/go/blockchainnodeengine/apiv1/blockchainnodeenginepb;blockchainnodeenginepb\xaa\x02$Google.Cloud.BlockchainNodeEngine.V1\xca\x02$Google\\Cloud\\BlockchainNodeEngine\\V1\xea\x02'Google::Cloud::BlockchainNodeEngine::V1"
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO'].fields_by_name['json_rpc_api_endpoint']._loaded_options = None
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO'].fields_by_name['json_rpc_api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO'].fields_by_name['websockets_api_endpoint']._loaded_options = None
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO'].fields_by_name['websockets_api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO'].fields_by_name['endpoint_info']._loaded_options = None
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO'].fields_by_name['endpoint_info']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO'].fields_by_name['service_attachment']._loaded_options = None
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO'].fields_by_name['service_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS'].fields_by_name['garbage_collection_mode']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS'].fields_by_name['garbage_collection_mode']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['beacon_api_endpoint']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['beacon_api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['beacon_prometheus_metrics_api_endpoint']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['beacon_prometheus_metrics_api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['execution_client_prometheus_metrics_api_endpoint']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS'].fields_by_name['execution_client_prometheus_metrics_api_endpoint']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_VALIDATORCONFIG'].fields_by_name['managed_validator_client']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_VALIDATORCONFIG'].fields_by_name['managed_validator_client']._serialized_options = b'\x18\x01\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NETWORK'].values_by_name['TESTNET_GOERLI_PRATER']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NETWORK'].values_by_name['TESTNET_GOERLI_PRATER']._serialized_options = b'\x08\x01'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['network']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['network']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['node_type']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['node_type']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['execution_client']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['execution_client']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['consensus_client']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['consensus_client']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['api_enable_admin']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['api_enable_admin']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['api_enable_debug']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['api_enable_debug']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['additional_endpoints']._loaded_options = None
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS'].fields_by_name['additional_endpoints']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE_LABELSENTRY']._loaded_options = None
    _globals['_BLOCKCHAINNODE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BLOCKCHAINNODE'].fields_by_name['name']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE'].fields_by_name['create_time']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE'].fields_by_name['update_time']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE'].fields_by_name['blockchain_type']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['blockchain_type']._serialized_options = b'\xe0A\x05'
    _globals['_BLOCKCHAINNODE'].fields_by_name['connection_info']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['connection_info']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE'].fields_by_name['state']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODE'].fields_by_name['private_service_connect_enabled']._loaded_options = None
    _globals['_BLOCKCHAINNODE'].fields_by_name['private_service_connect_enabled']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_BLOCKCHAINNODE']._loaded_options = None
    _globals['_BLOCKCHAINNODE']._serialized_options = b'\xeaA\x7f\n2blockchainnodeengine.googleapis.com/BlockchainNode\x12Iprojects/{project}/locations/{location}/blockchainNodes/{blockchain_node}'
    _globals['_LISTBLOCKCHAINNODESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBLOCKCHAINNODESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122blockchainnodeengine.googleapis.com/BlockchainNode'
    _globals['_GETBLOCKCHAINNODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBLOCKCHAINNODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2blockchainnodeengine.googleapis.com/BlockchainNode'
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122blockchainnodeengine.googleapis.com/BlockchainNode'
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node_id']._loaded_options = None
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node']._loaded_options = None
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node']._loaded_options = None
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['blockchain_node']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEBLOCKCHAINNODEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBLOCKCHAINNODEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2blockchainnodeengine.googleapis.com/BlockchainNode'
    _globals['_DELETEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEBLOCKCHAINNODEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_BLOCKCHAINNODEENGINE']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE']._serialized_options = b'\xcaA#blockchainnodeengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['ListBlockchainNodes']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['ListBlockchainNodes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1/{parent=projects/*/locations/*}/blockchainNodes'
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['GetBlockchainNode']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['GetBlockchainNode']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/blockchainNodes/*}'
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['CreateBlockchainNode']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['CreateBlockchainNode']._serialized_options = b'\xcaA#\n\x0eBlockchainNode\x12\x11OperationMetadata\xdaA)parent,blockchain_node,blockchain_node_id\x82\xd3\xe4\x93\x02F"3/v1/{parent=projects/*/locations/*}/blockchainNodes:\x0fblockchain_node'
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['UpdateBlockchainNode']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['UpdateBlockchainNode']._serialized_options = b'\xcaA#\n\x0eBlockchainNode\x12\x11OperationMetadata\xdaA\x1bblockchain_node,update_mask\x82\xd3\xe4\x93\x02V2C/v1/{blockchain_node.name=projects/*/locations/*/blockchainNodes/*}:\x0fblockchain_node'
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['DeleteBlockchainNode']._loaded_options = None
    _globals['_BLOCKCHAINNODEENGINE'].methods_by_name['DeleteBlockchainNode']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/blockchainNodes/*}'
    _globals['_BLOCKCHAINNODE']._serialized_start = 354
    _globals['_BLOCKCHAINNODE']._serialized_end = 3717
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO']._serialized_start = 1011
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO']._serialized_end = 1260
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO']._serialized_start = 1172
    _globals['_BLOCKCHAINNODE_CONNECTIONINFO_ENDPOINTINFO']._serialized_end = 1260
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS']._serialized_start = 1263
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS']._serialized_end = 3281
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS']._serialized_start = 2163
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS']._serialized_end = 2441
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS_GARBAGECOLLECTIONMODE']._serialized_start = 2326
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_GETHDETAILS_GARBAGECOLLECTIONMODE']._serialized_end = 2413
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS']._serialized_start = 2444
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_ETHEREUMENDPOINTS']._serialized_end = 2613
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_VALIDATORCONFIG']._serialized_start = 2616
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_VALIDATORCONFIG']._serialized_end = 2758
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NETWORK']._serialized_start = 2760
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NETWORK']._serialized_end = 2880
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NODETYPE']._serialized_start = 2882
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_NODETYPE']._serialized_end = 2953
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_EXECUTIONCLIENT']._serialized_start = 2955
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_EXECUTIONCLIENT']._serialized_end = 3028
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_CONSENSUSCLIENT']._serialized_start = 3030
    _globals['_BLOCKCHAINNODE_ETHEREUMDETAILS_CONSENSUSCLIENT']._serialized_end = 3097
    _globals['_BLOCKCHAINNODE_LABELSENTRY']._serialized_start = 3283
    _globals['_BLOCKCHAINNODE_LABELSENTRY']._serialized_end = 3328
    _globals['_BLOCKCHAINNODE_BLOCKCHAINTYPE']._serialized_start = 3330
    _globals['_BLOCKCHAINNODE_BLOCKCHAINTYPE']._serialized_end = 3393
    _globals['_BLOCKCHAINNODE_STATE']._serialized_start = 3396
    _globals['_BLOCKCHAINNODE_STATE']._serialized_end = 3537
    _globals['_LISTBLOCKCHAINNODESREQUEST']._serialized_start = 3720
    _globals['_LISTBLOCKCHAINNODESREQUEST']._serialized_end = 3897
    _globals['_LISTBLOCKCHAINNODESRESPONSE']._serialized_start = 3900
    _globals['_LISTBLOCKCHAINNODESRESPONSE']._serialized_end = 4055
    _globals['_GETBLOCKCHAINNODEREQUEST']._serialized_start = 4057
    _globals['_GETBLOCKCHAINNODEREQUEST']._serialized_end = 4157
    _globals['_CREATEBLOCKCHAINNODEREQUEST']._serialized_start = 4160
    _globals['_CREATEBLOCKCHAINNODEREQUEST']._serialized_end = 4407
    _globals['_UPDATEBLOCKCHAINNODEREQUEST']._serialized_start = 4410
    _globals['_UPDATEBLOCKCHAINNODEREQUEST']._serialized_end = 4602
    _globals['_DELETEBLOCKCHAINNODEREQUEST']._serialized_start = 4605
    _globals['_DELETEBLOCKCHAINNODEREQUEST']._serialized_end = 4733
    _globals['_OPERATIONMETADATA']._serialized_start = 4736
    _globals['_OPERATIONMETADATA']._serialized_end = 4992
    _globals['_BLOCKCHAINNODEENGINE']._serialized_start = 4995
    _globals['_BLOCKCHAINNODEENGINE']._serialized_end = 6347