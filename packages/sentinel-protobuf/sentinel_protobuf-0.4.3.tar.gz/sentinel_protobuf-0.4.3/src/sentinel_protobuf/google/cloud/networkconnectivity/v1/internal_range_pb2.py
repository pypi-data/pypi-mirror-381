"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networkconnectivity/v1/internal_range.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.networkconnectivity.v1 import common_pb2 as google_dot_cloud_dot_networkconnectivity_dot_v1_dot_common__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/networkconnectivity/v1/internal_range.proto\x12#google.cloud.networkconnectivity.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/networkconnectivity/v1/common.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8c\r\n\rInternalRange\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12/\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12N\n\x06labels\x18\x04 \x03(\x0b2>.google.cloud.networkconnectivity.v1.InternalRange.LabelsEntry\x12\x18\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x1a\n\rip_cidr_range\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x14\n\x07network\x18\x07 \x01(\tB\x03\xe0A\x05\x12L\n\x05usage\x18\x08 \x01(\x0e28.google.cloud.networkconnectivity.v1.InternalRange.UsageB\x03\xe0A\x01\x12P\n\x07peering\x18\t \x01(\x0e2:.google.cloud.networkconnectivity.v1.InternalRange.PeeringB\x03\xe0A\x01\x12\x1a\n\rprefix_length\x18\n \x01(\x05B\x03\xe0A\x01\x12\x1e\n\x11target_cidr_range\x18\x0b \x03(\tB\x03\xe0A\x01\x12\x12\n\x05users\x18\x0c \x03(\tB\x03\xe0A\x03\x12Q\n\x08overlaps\x18\r \x03(\x0e2:.google.cloud.networkconnectivity.v1.InternalRange.OverlapB\x03\xe0A\x01\x12T\n\tmigration\x18\x0e \x01(\x0b2<.google.cloud.networkconnectivity.v1.InternalRange.MigrationB\x03\xe0A\x01\x12\x16\n\timmutable\x18\x0f \x01(\x08B\x03\xe0A\x01\x12e\n\x12allocation_options\x18\x10 \x01(\x0b2D.google.cloud.networkconnectivity.v1.InternalRange.AllocationOptionsB\x03\xe0A\x01\x12 \n\x13exclude_cidr_ranges\x18\x11 \x03(\tB\x03\xe0A\x01\x1a5\n\tMigration\x12\x13\n\x06source\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x13\n\x06target\x18\x02 \x01(\tB\x03\xe0A\x05\x1a\xad\x01\n\x11AllocationOptions\x12g\n\x13allocation_strategy\x18\x01 \x01(\x0e2E.google.cloud.networkconnectivity.v1.InternalRange.AllocationStrategyB\x03\xe0A\x01\x12/\n"first_available_ranges_lookup_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"S\n\x05Usage\x12\x15\n\x11USAGE_UNSPECIFIED\x10\x00\x12\x0b\n\x07FOR_VPC\x10\x01\x12\x13\n\x0fEXTERNAL_TO_VPC\x10\x02\x12\x11\n\rFOR_MIGRATION\x10\x03"N\n\x07Peering\x12\x17\n\x13PEERING_UNSPECIFIED\x10\x00\x12\x0c\n\x08FOR_SELF\x10\x01\x12\x0c\n\x08FOR_PEER\x10\x02\x12\x0e\n\nNOT_SHARED\x10\x03"^\n\x07Overlap\x12\x17\n\x13OVERLAP_UNSPECIFIED\x10\x00\x12\x17\n\x13OVERLAP_ROUTE_RANGE\x10\x01\x12!\n\x1dOVERLAP_EXISTING_SUBNET_RANGE\x10\x02"\x94\x01\n\x12AllocationStrategy\x12#\n\x1fALLOCATION_STRATEGY_UNSPECIFIED\x10\x00\x12\n\n\x06RANDOM\x10\x01\x12\x13\n\x0fFIRST_AVAILABLE\x10\x02\x12\x1c\n\x18RANDOM_FIRST_N_AVAILABLE\x10\x03\x12\x1a\n\x16FIRST_SMALLEST_FITTING\x10\x04:~\xeaA{\n0networkconnectivity.googleapis.com/InternalRange\x12Gprojects/{project}/locations/{location}/internalRanges/{internal_range}"\x9f\x01\n\x19ListInternalRangesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x97\x01\n\x1aListInternalRangesResponse\x12K\n\x0finternal_ranges\x18\x01 \x03(\x0b22.google.cloud.networkconnectivity.v1.InternalRange\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"a\n\x17GetInternalRangeRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0networkconnectivity.googleapis.com/InternalRange"\xf0\x01\n\x1aCreateInternalRangeRequest\x12H\n\x06parent\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\x120networkconnectivity.googleapis.com/InternalRange\x12\x1e\n\x11internal_range_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12O\n\x0einternal_range\x18\x03 \x01(\x0b22.google.cloud.networkconnectivity.v1.InternalRangeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xbc\x01\n\x1aUpdateInternalRangeRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12O\n\x0einternal_range\x18\x02 \x01(\x0b22.google.cloud.networkconnectivity.v1.InternalRangeB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"}\n\x1aDeleteInternalRangeRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0networkconnectivity.googleapis.com/InternalRange\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x012\xa7\n\n\x14InternalRangeService\x12\xda\x01\n\x12ListInternalRanges\x12>.google.cloud.networkconnectivity.v1.ListInternalRangesRequest\x1a?.google.cloud.networkconnectivity.v1.ListInternalRangesResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/internalRanges\x12\xc7\x01\n\x10GetInternalRange\x12<.google.cloud.networkconnectivity.v1.GetInternalRangeRequest\x1a2.google.cloud.networkconnectivity.v1.InternalRange"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/internalRanges/*}\x12\x91\x02\n\x13CreateInternalRange\x12?.google.cloud.networkconnectivity.v1.CreateInternalRangeRequest\x1a\x1d.google.longrunning.Operation"\x99\x01\xcaA"\n\rInternalRange\x12\x11OperationMetadata\xdaA\'parent,internal_range,internal_range_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/internalRanges:\x0einternal_range\x12\x93\x02\n\x13UpdateInternalRange\x12?.google.cloud.networkconnectivity.v1.UpdateInternalRangeRequest\x1a\x1d.google.longrunning.Operation"\x9b\x01\xcaA"\n\rInternalRange\x12\x11OperationMetadata\xdaA\x1ainternal_range,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{internal_range.name=projects/*/locations/*/internalRanges/*}:\x0einternal_range\x12\xe5\x01\n\x13DeleteInternalRange\x12?.google.cloud.networkconnectivity.v1.DeleteInternalRangeRequest\x1a\x1d.google.longrunning.Operation"n\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/internalRanges/*}\x1aV\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8f\x02\n\'com.google.cloud.networkconnectivity.v1B\x12InternalRangeProtoP\x01ZYcloud.google.com/go/networkconnectivity/apiv1/networkconnectivitypb;networkconnectivitypb\xaa\x02#Google.Cloud.NetworkConnectivity.V1\xca\x02#Google\\Cloud\\NetworkConnectivity\\V1\xea\x02&Google::Cloud::NetworkConnectivity::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networkconnectivity.v1.internal_range_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.networkconnectivity.v1B\x12InternalRangeProtoP\x01ZYcloud.google.com/go/networkconnectivity/apiv1/networkconnectivitypb;networkconnectivitypb\xaa\x02#Google.Cloud.NetworkConnectivity.V1\xca\x02#Google\\Cloud\\NetworkConnectivity\\V1\xea\x02&Google::Cloud::NetworkConnectivity::V1"
    _globals['_INTERNALRANGE_MIGRATION'].fields_by_name['source']._loaded_options = None
    _globals['_INTERNALRANGE_MIGRATION'].fields_by_name['source']._serialized_options = b'\xe0A\x05'
    _globals['_INTERNALRANGE_MIGRATION'].fields_by_name['target']._loaded_options = None
    _globals['_INTERNALRANGE_MIGRATION'].fields_by_name['target']._serialized_options = b'\xe0A\x05'
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS'].fields_by_name['allocation_strategy']._loaded_options = None
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS'].fields_by_name['allocation_strategy']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS'].fields_by_name['first_available_ranges_lookup_size']._loaded_options = None
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS'].fields_by_name['first_available_ranges_lookup_size']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE_LABELSENTRY']._loaded_options = None
    _globals['_INTERNALRANGE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_INTERNALRANGE'].fields_by_name['name']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_INTERNALRANGE'].fields_by_name['description']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['ip_cidr_range']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['ip_cidr_range']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['network']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['network']._serialized_options = b'\xe0A\x05'
    _globals['_INTERNALRANGE'].fields_by_name['usage']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['usage']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['peering']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['peering']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['prefix_length']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['prefix_length']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['target_cidr_range']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['target_cidr_range']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['users']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['users']._serialized_options = b'\xe0A\x03'
    _globals['_INTERNALRANGE'].fields_by_name['overlaps']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['overlaps']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['migration']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['migration']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['immutable']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['immutable']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['allocation_options']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['allocation_options']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE'].fields_by_name['exclude_cidr_ranges']._loaded_options = None
    _globals['_INTERNALRANGE'].fields_by_name['exclude_cidr_ranges']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGE']._loaded_options = None
    _globals['_INTERNALRANGE']._serialized_options = b'\xeaA{\n0networkconnectivity.googleapis.com/InternalRange\x12Gprojects/{project}/locations/{location}/internalRanges/{internal_range}'
    _globals['_LISTINTERNALRANGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTINTERNALRANGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_GETINTERNALRANGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETINTERNALRANGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0networkconnectivity.googleapis.com/InternalRange'
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA2\x120networkconnectivity.googleapis.com/InternalRange'
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['internal_range_id']._loaded_options = None
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['internal_range_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['internal_range']._loaded_options = None
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['internal_range']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEINTERNALRANGEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['internal_range']._loaded_options = None
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['internal_range']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEINTERNALRANGEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEINTERNALRANGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEINTERNALRANGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0networkconnectivity.googleapis.com/InternalRange'
    _globals['_DELETEINTERNALRANGEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEINTERNALRANGEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_INTERNALRANGESERVICE']._loaded_options = None
    _globals['_INTERNALRANGESERVICE']._serialized_options = b'\xcaA"networkconnectivity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_INTERNALRANGESERVICE'].methods_by_name['ListInternalRanges']._loaded_options = None
    _globals['_INTERNALRANGESERVICE'].methods_by_name['ListInternalRanges']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1/{parent=projects/*/locations/*}/internalRanges'
    _globals['_INTERNALRANGESERVICE'].methods_by_name['GetInternalRange']._loaded_options = None
    _globals['_INTERNALRANGESERVICE'].methods_by_name['GetInternalRange']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1/{name=projects/*/locations/*/internalRanges/*}'
    _globals['_INTERNALRANGESERVICE'].methods_by_name['CreateInternalRange']._loaded_options = None
    _globals['_INTERNALRANGESERVICE'].methods_by_name['CreateInternalRange']._serialized_options = b'\xcaA"\n\rInternalRange\x12\x11OperationMetadata\xdaA\'parent,internal_range,internal_range_id\x82\xd3\xe4\x93\x02D"2/v1/{parent=projects/*/locations/*}/internalRanges:\x0einternal_range'
    _globals['_INTERNALRANGESERVICE'].methods_by_name['UpdateInternalRange']._loaded_options = None
    _globals['_INTERNALRANGESERVICE'].methods_by_name['UpdateInternalRange']._serialized_options = b'\xcaA"\n\rInternalRange\x12\x11OperationMetadata\xdaA\x1ainternal_range,update_mask\x82\xd3\xe4\x93\x02S2A/v1/{internal_range.name=projects/*/locations/*/internalRanges/*}:\x0einternal_range'
    _globals['_INTERNALRANGESERVICE'].methods_by_name['DeleteInternalRange']._loaded_options = None
    _globals['_INTERNALRANGESERVICE'].methods_by_name['DeleteInternalRange']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1/{name=projects/*/locations/*/internalRanges/*}'
    _globals['_INTERNALRANGE']._serialized_start = 396
    _globals['_INTERNALRANGE']._serialized_end = 2072
    _globals['_INTERNALRANGE_MIGRATION']._serialized_start = 1256
    _globals['_INTERNALRANGE_MIGRATION']._serialized_end = 1309
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS']._serialized_start = 1312
    _globals['_INTERNALRANGE_ALLOCATIONOPTIONS']._serialized_end = 1485
    _globals['_INTERNALRANGE_LABELSENTRY']._serialized_start = 1487
    _globals['_INTERNALRANGE_LABELSENTRY']._serialized_end = 1532
    _globals['_INTERNALRANGE_USAGE']._serialized_start = 1534
    _globals['_INTERNALRANGE_USAGE']._serialized_end = 1617
    _globals['_INTERNALRANGE_PEERING']._serialized_start = 1619
    _globals['_INTERNALRANGE_PEERING']._serialized_end = 1697
    _globals['_INTERNALRANGE_OVERLAP']._serialized_start = 1699
    _globals['_INTERNALRANGE_OVERLAP']._serialized_end = 1793
    _globals['_INTERNALRANGE_ALLOCATIONSTRATEGY']._serialized_start = 1796
    _globals['_INTERNALRANGE_ALLOCATIONSTRATEGY']._serialized_end = 1944
    _globals['_LISTINTERNALRANGESREQUEST']._serialized_start = 2075
    _globals['_LISTINTERNALRANGESREQUEST']._serialized_end = 2234
    _globals['_LISTINTERNALRANGESRESPONSE']._serialized_start = 2237
    _globals['_LISTINTERNALRANGESRESPONSE']._serialized_end = 2388
    _globals['_GETINTERNALRANGEREQUEST']._serialized_start = 2390
    _globals['_GETINTERNALRANGEREQUEST']._serialized_end = 2487
    _globals['_CREATEINTERNALRANGEREQUEST']._serialized_start = 2490
    _globals['_CREATEINTERNALRANGEREQUEST']._serialized_end = 2730
    _globals['_UPDATEINTERNALRANGEREQUEST']._serialized_start = 2733
    _globals['_UPDATEINTERNALRANGEREQUEST']._serialized_end = 2921
    _globals['_DELETEINTERNALRANGEREQUEST']._serialized_start = 2923
    _globals['_DELETEINTERNALRANGEREQUEST']._serialized_end = 3048
    _globals['_INTERNALRANGESERVICE']._serialized_start = 3051
    _globals['_INTERNALRANGESERVICE']._serialized_end = 4370