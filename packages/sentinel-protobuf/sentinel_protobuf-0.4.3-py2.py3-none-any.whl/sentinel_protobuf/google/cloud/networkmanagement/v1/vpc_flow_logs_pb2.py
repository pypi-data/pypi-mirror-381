"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkmanagement/v1/vpc_flow_logs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkmanagement.v1 import reachability_pb2 as google_dot_cloud_dot_networkmanagement_dot_v1_dot_reachability__pb2
from .....google.cloud.networkmanagement.v1 import vpc_flow_logs_config_pb2 as google_dot_cloud_dot_networkmanagement_dot_v1_dot_vpc__flow__logs__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/networkmanagement/v1/vpc_flow_logs.proto\x12!google.cloud.networkmanagement.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/networkmanagement/v1/reachability.proto\x1a<google/cloud/networkmanagement/v1/vpc_flow_logs_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc8\x01\n\x1dListVpcFlowLogsConfigsRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122networkmanagement.googleapis.com/VpcFlowLogsConfig\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xa3\x01\n\x1eListVpcFlowLogsConfigsResponse\x12S\n\x15vpc_flow_logs_configs\x18\x01 \x03(\x0b24.google.cloud.networkmanagement.v1.VpcFlowLogsConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"g\n\x1bGetVpcFlowLogsConfigRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig"\xa2\x02\n\x1eCreateVpcFlowLogsConfigRequest\x12J\n\x06parent\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\x122networkmanagement.googleapis.com/VpcFlowLogsConfig\x12[\n\x17vpc_flow_logs_config_id\x18\x02 \x01(\tB:\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig\x12W\n\x14vpc_flow_logs_config\x18\x03 \x01(\x0b24.google.cloud.networkmanagement.v1.VpcFlowLogsConfigB\x03\xe0A\x02"\xaf\x01\n\x1eUpdateVpcFlowLogsConfigRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12W\n\x14vpc_flow_logs_config\x18\x02 \x01(\x0b24.google.cloud.networkmanagement.v1.VpcFlowLogsConfigB\x03\xe0A\x02"j\n\x1eDeleteVpcFlowLogsConfigRequest\x12H\n\x04name\x18\x01 \x01(\tB:\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig2\xec\x0b\n\x12VpcFlowLogsService\x12\xe6\x01\n\x16ListVpcFlowLogsConfigs\x12@.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsRequest\x1aA.google.cloud.networkmanagement.v1.ListVpcFlowLogsConfigsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs\x12\xd3\x01\n\x14GetVpcFlowLogsConfig\x12>.google.cloud.networkmanagement.v1.GetVpcFlowLogsConfigRequest\x1a4.google.cloud.networkmanagement.v1.VpcFlowLogsConfig"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}\x12\xd3\x02\n\x17CreateVpcFlowLogsConfig\x12A.google.cloud.networkmanagement.v1.CreateVpcFlowLogsConfigRequest\x1a\x1d.google.longrunning.Operation"\xd5\x01\xcaAH\n\x11VpcFlowLogsConfig\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA3parent,vpc_flow_logs_config,vpc_flow_logs_config_id\x82\xd3\xe4\x93\x02N"6/v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:\x14vpc_flow_logs_config\x12\xd5\x02\n\x17UpdateVpcFlowLogsConfig\x12A.google.cloud.networkmanagement.v1.UpdateVpcFlowLogsConfigRequest\x1a\x1d.google.longrunning.Operation"\xd7\x01\xcaAH\n\x11VpcFlowLogsConfig\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA vpc_flow_logs_config,update_mask\x82\xd3\xe4\x93\x02c2K/v1/{vpc_flow_logs_config.name=projects/*/locations/*/vpcFlowLogsConfigs/*}:\x14vpc_flow_logs_config\x12\x92\x02\n\x17DeleteVpcFlowLogsConfig\x12A.google.cloud.networkmanagement.v1.DeleteVpcFlowLogsConfigRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaAL\n\x15google.protobuf.Empty\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}\x1aT\xcaA networkmanagement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xff\x01\n%com.google.cloud.networkmanagement.v1B\x10VpcFlowLogsProtoP\x01ZScloud.google.com/go/networkmanagement/apiv1/networkmanagementpb;networkmanagementpb\xaa\x02!Google.Cloud.NetworkManagement.V1\xca\x02!Google\\Cloud\\NetworkManagement\\V1\xea\x02$Google::Cloud::NetworkManagement::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkmanagement.v1.vpc_flow_logs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.networkmanagement.v1B\x10VpcFlowLogsProtoP\x01ZScloud.google.com/go/networkmanagement/apiv1/networkmanagementpb;networkmanagementpb\xaa\x02!Google.Cloud.NetworkManagement.V1\xca\x02!Google\\Cloud\\NetworkManagement\\V1\xea\x02$Google::Cloud::NetworkManagement::V1'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122networkmanagement.googleapis.com/VpcFlowLogsConfig'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig'
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA4\x122networkmanagement.googleapis.com/VpcFlowLogsConfig'
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config_id']._loaded_options = None
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config_id']._serialized_options = b'\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig'
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config']._loaded_options = None
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config']._loaded_options = None
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['vpc_flow_logs_config']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEVPCFLOWLOGSCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA4\n2networkmanagement.googleapis.com/VpcFlowLogsConfig'
    _globals['_VPCFLOWLOGSSERVICE']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE']._serialized_options = b'\xcaA networkmanagement.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['ListVpcFlowLogsConfigs']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['ListVpcFlowLogsConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs'
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['GetVpcFlowLogsConfig']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['GetVpcFlowLogsConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}'
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['CreateVpcFlowLogsConfig']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['CreateVpcFlowLogsConfig']._serialized_options = b'\xcaAH\n\x11VpcFlowLogsConfig\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA3parent,vpc_flow_logs_config,vpc_flow_logs_config_id\x82\xd3\xe4\x93\x02N"6/v1/{parent=projects/*/locations/*}/vpcFlowLogsConfigs:\x14vpc_flow_logs_config'
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['UpdateVpcFlowLogsConfig']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['UpdateVpcFlowLogsConfig']._serialized_options = b'\xcaAH\n\x11VpcFlowLogsConfig\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA vpc_flow_logs_config,update_mask\x82\xd3\xe4\x93\x02c2K/v1/{vpc_flow_logs_config.name=projects/*/locations/*/vpcFlowLogsConfigs/*}:\x14vpc_flow_logs_config'
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['DeleteVpcFlowLogsConfig']._loaded_options = None
    _globals['_VPCFLOWLOGSSERVICE'].methods_by_name['DeleteVpcFlowLogsConfig']._serialized_options = b'\xcaAL\n\x15google.protobuf.Empty\x123google.cloud.networkmanagement.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=projects/*/locations/*/vpcFlowLogsConfigs/*}'
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST']._serialized_start = 424
    _globals['_LISTVPCFLOWLOGSCONFIGSREQUEST']._serialized_end = 624
    _globals['_LISTVPCFLOWLOGSCONFIGSRESPONSE']._serialized_start = 627
    _globals['_LISTVPCFLOWLOGSCONFIGSRESPONSE']._serialized_end = 790
    _globals['_GETVPCFLOWLOGSCONFIGREQUEST']._serialized_start = 792
    _globals['_GETVPCFLOWLOGSCONFIGREQUEST']._serialized_end = 895
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST']._serialized_start = 898
    _globals['_CREATEVPCFLOWLOGSCONFIGREQUEST']._serialized_end = 1188
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST']._serialized_start = 1191
    _globals['_UPDATEVPCFLOWLOGSCONFIGREQUEST']._serialized_end = 1366
    _globals['_DELETEVPCFLOWLOGSCONFIGREQUEST']._serialized_start = 1368
    _globals['_DELETEVPCFLOWLOGSCONFIGREQUEST']._serialized_end = 1474
    _globals['_VPCFLOWLOGSSERVICE']._serialized_start = 1477
    _globals['_VPCFLOWLOGSSERVICE']._serialized_end = 2993