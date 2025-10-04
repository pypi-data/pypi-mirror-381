"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkmanagement/v1/vpc_flow_logs_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/networkmanagement/v1/vpc_flow_logs_config.proto\x12!google.cloud.networkmanagement.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\r\n\x11VpcFlowLogsConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1d\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12S\n\x05state\x18\x03 \x01(\x0e2:.google.cloud.networkmanagement.v1.VpcFlowLogsConfig.StateB\x03\xe0A\x01H\x02\x88\x01\x01\x12p\n\x14aggregation_interval\x18\x04 \x01(\x0e2H.google.cloud.networkmanagement.v1.VpcFlowLogsConfig.AggregationIntervalB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1f\n\rflow_sampling\x18\x05 \x01(\x02B\x03\xe0A\x01H\x04\x88\x01\x01\x12Y\n\x08metadata\x18\x06 \x01(\x0e2=.google.cloud.networkmanagement.v1.VpcFlowLogsConfig.MetadataB\x03\xe0A\x01H\x05\x88\x01\x01\x12\x1c\n\x0fmetadata_fields\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x1d\n\x0bfilter_expr\x18\x08 \x01(\tB\x03\xe0A\x01H\x06\x88\x01\x01\x12q\n\x15target_resource_state\x18\x0c \x01(\x0e2H.google.cloud.networkmanagement.v1.VpcFlowLogsConfig.TargetResourceStateB\x03\xe0A\x03H\x07\x88\x01\x01\x12!\n\x17interconnect_attachment\x18f \x01(\tH\x00\x12\x14\n\nvpn_tunnel\x18g \x01(\tH\x00\x12U\n\x06labels\x18\x0b \x03(\x0b2@.google.cloud.networkmanagement.v1.VpcFlowLogsConfig.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02"\xb6\x01\n\x13AggregationInterval\x12$\n AGGREGATION_INTERVAL_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERVAL_5_SEC\x10\x01\x12\x13\n\x0fINTERVAL_30_SEC\x10\x02\x12\x12\n\x0eINTERVAL_1_MIN\x10\x03\x12\x12\n\x0eINTERVAL_5_MIN\x10\x04\x12\x13\n\x0fINTERVAL_10_MIN\x10\x05\x12\x13\n\x0fINTERVAL_15_MIN\x10\x06"m\n\x08Metadata\x12\x18\n\x14METADATA_UNSPECIFIED\x10\x00\x12\x18\n\x14INCLUDE_ALL_METADATA\x10\x01\x12\x18\n\x14EXCLUDE_ALL_METADATA\x10\x02\x12\x13\n\x0fCUSTOM_METADATA\x10\x03"|\n\x13TargetResourceState\x12%\n!TARGET_RESOURCE_STATE_UNSPECIFIED\x10\x00\x12\x1a\n\x16TARGET_RESOURCE_EXISTS\x10\x01\x12"\n\x1eTARGET_RESOURCE_DOES_NOT_EXIST\x10\x02:\xb2\x01\xeaA\xae\x01\n2networkmanagement.googleapis.com/VpcFlowLogsConfig\x12Qprojects/{project}/locations/{location}/vpcFlowLogsConfigs/{vpc_flow_logs_config}*\x12vpcFlowLogsConfigs2\x11vpcFlowLogsConfigB\x11\n\x0ftarget_resourceB\x0e\n\x0c_descriptionB\x08\n\x06_stateB\x17\n\x15_aggregation_intervalB\x10\n\x0e_flow_samplingB\x0b\n\t_metadataB\x0e\n\x0c_filter_exprB\x18\n\x16_target_resource_stateB\x85\x02\n%com.google.cloud.networkmanagement.v1B\x16VpcFlowLogsConfigProtoP\x01ZScloud.google.com/go/networkmanagement/apiv1/networkmanagementpb;networkmanagementpb\xaa\x02!Google.Cloud.NetworkManagement.V1\xca\x02!Google\\Cloud\\NetworkManagement\\V1\xea\x02$Google::Cloud::NetworkManagement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkmanagement.v1.vpc_flow_logs_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.networkmanagement.v1B\x16VpcFlowLogsConfigProtoP\x01ZScloud.google.com/go/networkmanagement/apiv1/networkmanagementpb;networkmanagementpb\xaa\x02!Google.Cloud.NetworkManagement.V1\xca\x02!Google\\Cloud\\NetworkManagement\\V1\xea\x02$Google::Cloud::NetworkManagement::V1'
    _globals['_VPCFLOWLOGSCONFIG_LABELSENTRY']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['description']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['aggregation_interval']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['aggregation_interval']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['flow_sampling']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['flow_sampling']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['metadata']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['metadata']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['metadata_fields']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['metadata_fields']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['filter_expr']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['filter_expr']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['target_resource_state']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['target_resource_state']._serialized_options = b'\xe0A\x03'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['labels']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_VPCFLOWLOGSCONFIG']._loaded_options = None
    _globals['_VPCFLOWLOGSCONFIG']._serialized_options = b'\xeaA\xae\x01\n2networkmanagement.googleapis.com/VpcFlowLogsConfig\x12Qprojects/{project}/locations/{location}/vpcFlowLogsConfigs/{vpc_flow_logs_config}*\x12vpcFlowLogsConfigs2\x11vpcFlowLogsConfig'
    _globals['_VPCFLOWLOGSCONFIG']._serialized_start = 193
    _globals['_VPCFLOWLOGSCONFIG']._serialized_end = 1865
    _globals['_VPCFLOWLOGSCONFIG_LABELSENTRY']._serialized_start = 1015
    _globals['_VPCFLOWLOGSCONFIG_LABELSENTRY']._serialized_end = 1060
    _globals['_VPCFLOWLOGSCONFIG_STATE']._serialized_start = 1062
    _globals['_VPCFLOWLOGSCONFIG_STATE']._serialized_end = 1119
    _globals['_VPCFLOWLOGSCONFIG_AGGREGATIONINTERVAL']._serialized_start = 1122
    _globals['_VPCFLOWLOGSCONFIG_AGGREGATIONINTERVAL']._serialized_end = 1304
    _globals['_VPCFLOWLOGSCONFIG_METADATA']._serialized_start = 1306
    _globals['_VPCFLOWLOGSCONFIG_METADATA']._serialized_end = 1415
    _globals['_VPCFLOWLOGSCONFIG_TARGETRESOURCESTATE']._serialized_start = 1417
    _globals['_VPCFLOWLOGSCONFIG_TARGETRESOURCESTATE']._serialized_end = 1541