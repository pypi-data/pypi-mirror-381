"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataproc/v1/node_groups.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataproc.v1 import clusters_pb2 as google_dot_cloud_dot_dataproc_dot_v1_dot_clusters__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/cloud/dataproc/v1/node_groups.proto\x12\x18google.cloud.dataproc.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/dataproc/v1/clusters.proto\x1a#google/longrunning/operations.proto\x1a\x1egoogle/protobuf/duration.proto"\xc6\x01\n\x16CreateNodeGroupRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dataproc.googleapis.com/NodeGroup\x12<\n\nnode_group\x18\x02 \x01(\x0b2#.google.cloud.dataproc.v1.NodeGroupB\x03\xe0A\x02\x12\x1a\n\rnode_group_id\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x9e\x01\n\x16ResizeNodeGroupRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04size\x18\x02 \x01(\x05B\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01\x12E\n\x1dgraceful_decommission_timeout\x18\x04 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"N\n\x13GetNodeGroupRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dataproc.googleapis.com/NodeGroup2\xa7\x06\n\x13NodeGroupController\x12\x95\x02\n\x0fCreateNodeGroup\x120.google.cloud.dataproc.v1.CreateNodeGroupRequest\x1a\x1d.google.longrunning.Operation"\xb0\x01\xcaA@\n\tNodeGroup\x123google.cloud.dataproc.v1.NodeGroupOperationMetadata\xdaA\x1fparent,node_group,node_group_id\x82\xd3\xe4\x93\x02E"7/v1/{parent=projects/*/regions/*/clusters/*}/nodeGroups:\nnode_group\x12\xfd\x01\n\x0fResizeNodeGroup\x120.google.cloud.dataproc.v1.ResizeNodeGroupRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA@\n\tNodeGroup\x123google.cloud.dataproc.v1.NodeGroupOperationMetadata\xdaA\tname,size\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/regions/*/clusters/*/nodeGroups/*}:resize:\x01*\x12\xaa\x01\n\x0cGetNodeGroup\x12-.google.cloud.dataproc.v1.GetNodeGroupRequest\x1a#.google.cloud.dataproc.v1.NodeGroup"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/regions/*/clusters/*/nodeGroups/*}\x1aK\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd0\x01\n\x1ccom.google.cloud.dataproc.v1B\x0fNodeGroupsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb\xeaA_\n%dataproc.googleapis.com/ClusterRegion\x126projects/{project}/regions/{region}/clusters/{cluster}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataproc.v1.node_groups_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataproc.v1B\x0fNodeGroupsProtoP\x01Z;cloud.google.com/go/dataproc/v2/apiv1/dataprocpb;dataprocpb\xeaA_\n%dataproc.googleapis.com/ClusterRegion\x126projects/{project}/regions/{region}/clusters/{cluster}'
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dataproc.googleapis.com/NodeGroup'
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['node_group']._loaded_options = None
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['node_group']._serialized_options = b'\xe0A\x02'
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['node_group_id']._loaded_options = None
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['node_group_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATENODEGROUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['size']._loaded_options = None
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['graceful_decommission_timeout']._loaded_options = None
    _globals['_RESIZENODEGROUPREQUEST'].fields_by_name['graceful_decommission_timeout']._serialized_options = b'\xe0A\x01'
    _globals['_GETNODEGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETNODEGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dataproc.googleapis.com/NodeGroup'
    _globals['_NODEGROUPCONTROLLER']._loaded_options = None
    _globals['_NODEGROUPCONTROLLER']._serialized_options = b'\xcaA\x17dataproc.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['CreateNodeGroup']._loaded_options = None
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['CreateNodeGroup']._serialized_options = b'\xcaA@\n\tNodeGroup\x123google.cloud.dataproc.v1.NodeGroupOperationMetadata\xdaA\x1fparent,node_group,node_group_id\x82\xd3\xe4\x93\x02E"7/v1/{parent=projects/*/regions/*/clusters/*}/nodeGroups:\nnode_group'
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['ResizeNodeGroup']._loaded_options = None
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['ResizeNodeGroup']._serialized_options = b'\xcaA@\n\tNodeGroup\x123google.cloud.dataproc.v1.NodeGroupOperationMetadata\xdaA\tname,size\x82\xd3\xe4\x93\x02C">/v1/{name=projects/*/regions/*/clusters/*/nodeGroups/*}:resize:\x01*'
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['GetNodeGroup']._loaded_options = None
    _globals['_NODEGROUPCONTROLLER'].methods_by_name['GetNodeGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/regions/*/clusters/*/nodeGroups/*}'
    _globals['_CREATENODEGROUPREQUEST']._serialized_start = 298
    _globals['_CREATENODEGROUPREQUEST']._serialized_end = 496
    _globals['_RESIZENODEGROUPREQUEST']._serialized_start = 499
    _globals['_RESIZENODEGROUPREQUEST']._serialized_end = 657
    _globals['_GETNODEGROUPREQUEST']._serialized_start = 659
    _globals['_GETNODEGROUPREQUEST']._serialized_end = 737
    _globals['_NODEGROUPCONTROLLER']._serialized_start = 740
    _globals['_NODEGROUPCONTROLLER']._serialized_end = 1547