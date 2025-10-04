"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/networksecurity/v1/address_group.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/networksecurity/v1/address_group.proto\x12\x1fgoogle.cloud.networksecurity.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbd\x06\n\x0cAddressGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12N\n\x06labels\x18\x05 \x03(\x0b29.google.cloud.networksecurity.v1.AddressGroup.LabelsEntryB\x03\xe0A\x01\x12E\n\x04type\x18\x06 \x01(\x0e22.google.cloud.networksecurity.v1.AddressGroup.TypeB\x03\xe0A\x02\x12\x12\n\x05items\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x15\n\x08capacity\x18\x08 \x01(\x05B\x03\xe0A\x02\x12\x16\n\tself_link\x18\t \x01(\tB\x03\xe0A\x03\x12K\n\x07purpose\x18\n \x03(\x0e25.google.cloud.networksecurity.v1.AddressGroup.PurposeB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"0\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04IPV4\x10\x01\x12\x08\n\x04IPV6\x10\x02"@\n\x07Purpose\x12\x17\n\x13PURPOSE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DEFAULT\x10\x01\x12\x0f\n\x0bCLOUD_ARMOR\x10\x02:\xc9\x01\xeaA\xc5\x01\n+networksecurity.googleapis.com/AddressGroup\x12Eprojects/{project}/locations/{location}/addressGroups/{address_group}\x12Oorganizations/{organization}/locations/{location}/addressGroups/{address_group}"\xa1\x01\n\x18ListAddressGroupsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12#\n\x16return_partial_success\x18\x04 \x01(\x08B\x03\xe0A\x01"\x90\x01\n\x19ListAddressGroupsResponse\x12E\n\x0eaddress_groups\x18\x01 \x03(\x0b2-.google.cloud.networksecurity.v1.AddressGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"[\n\x16GetAddressGroupRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup"\xe3\x01\n\x19CreateAddressGroupRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+networksecurity.googleapis.com/AddressGroup\x12\x1d\n\x10address_group_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12I\n\raddress_group\x18\x03 \x01(\x0b2-.google.cloud.networksecurity.v1.AddressGroupB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xb5\x01\n\x19UpdateAddressGroupRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12I\n\raddress_group\x18\x02 \x01(\x0b2-.google.cloud.networksecurity.v1.AddressGroupB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"w\n\x19DeleteAddressGroupRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x96\x01\n\x1bAddAddressGroupItemsRequest\x12J\n\raddress_group\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12\x12\n\x05items\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x99\x01\n\x1eRemoveAddressGroupItemsRequest\x12J\n\raddress_group\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12\x12\n\x05items\x18\x02 \x03(\tB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xd7\x01\n\x1dCloneAddressGroupItemsRequest\x12J\n\raddress_group\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12Q\n\x14source_address_group\x18\x02 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x96\x01\n!ListAddressGroupReferencesRequest\x12J\n\raddress_group\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x9c\x02\n"ListAddressGroupReferencesResponse\x12{\n\x18address_group_references\x18\x01 \x03(\x0b2Y.google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse.AddressGroupReference\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x1a`\n\x15AddressGroupReference\x12\x17\n\x0ffirewall_policy\x18\x01 \x01(\t\x12\x17\n\x0fsecurity_policy\x18\x04 \x01(\t\x12\x15\n\rrule_priority\x18\x02 \x01(\x052\xda\x13\n\x13AddressGroupService\x12\xce\x01\n\x11ListAddressGroups\x129.google.cloud.networksecurity.v1.ListAddressGroupsRequest\x1a:.google.cloud.networksecurity.v1.ListAddressGroupsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/addressGroups\x12\xbb\x01\n\x0fGetAddressGroup\x127.google.cloud.networksecurity.v1.GetAddressGroupRequest\x1a-.google.cloud.networksecurity.v1.AddressGroup"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/addressGroups/*}\x12\xa6\x02\n\x12CreateAddressGroup\x12:.google.cloud.networksecurity.v1.CreateAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA%parent,address_group,address_group_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/addressGroups:\raddress_group\x12\xa8\x02\n\x12UpdateAddressGroup\x12:.google.cloud.networksecurity.v1.UpdateAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\xb6\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x19address_group,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{address_group.name=projects/*/locations/*/addressGroups/*}:\raddress_group\x12\x9e\x02\n\x14AddAddressGroupItems\x12<.google.cloud.networksecurity.v1.AddAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xa8\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02H"C/v1/{address_group=projects/*/locations/*/addressGroups/*}:addItems:\x01*\x12\xa7\x02\n\x17RemoveAddressGroupItems\x12?.google.cloud.networksecurity.v1.RemoveAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02K"F/v1/{address_group=projects/*/locations/*/addressGroups/*}:removeItems:\x01*\x12\xb3\x02\n\x16CloneAddressGroupItems\x12>.google.cloud.networksecurity.v1.CloneAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA"address_group,source_address_group\x82\xd3\xe4\x93\x02J"E/v1/{address_group=projects/*/locations/*/addressGroups/*}:cloneItems:\x01*\x12\xff\x01\n\x12DeleteAddressGroup\x12:.google.cloud.networksecurity.v1.DeleteAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaAJ\n\x15google.protobuf.Empty\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/addressGroups/*}\x12\x88\x02\n\x1aListAddressGroupReferences\x12B.google.cloud.networksecurity.v1.ListAddressGroupReferencesRequest\x1aC.google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse"a\xdaA\raddress_group\x82\xd3\xe4\x93\x02K\x12I/v1/{address_group=projects/*/locations/*/addressGroups/*}:listReferences\x1aR\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform2\x93\x14\n\x1fOrganizationAddressGroupService\x12\xd3\x01\n\x11ListAddressGroups\x129.google.cloud.networksecurity.v1.ListAddressGroupsRequest\x1a:.google.cloud.networksecurity.v1.ListAddressGroupsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=organizations/*/locations/*}/addressGroups\x12\xc0\x01\n\x0fGetAddressGroup\x127.google.cloud.networksecurity.v1.GetAddressGroupRequest\x1a-.google.cloud.networksecurity.v1.AddressGroup"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=organizations/*/locations/*/addressGroups/*}\x12\xab\x02\n\x12CreateAddressGroup\x12:.google.cloud.networksecurity.v1.CreateAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\xb9\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA%parent,address_group,address_group_id\x82\xd3\xe4\x93\x02G"6/v1/{parent=organizations/*/locations/*}/addressGroups:\raddress_group\x12\xad\x02\n\x12UpdateAddressGroup\x12:.google.cloud.networksecurity.v1.UpdateAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\xbb\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x19address_group,update_mask\x82\xd3\xe4\x93\x02U2D/v1/{address_group.name=organizations/*/locations/*/addressGroups/*}:\raddress_group\x12\xa3\x02\n\x14AddAddressGroupItems\x12<.google.cloud.networksecurity.v1.AddAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02M"H/v1/{address_group=organizations/*/locations/*/addressGroups/*}:addItems:\x01*\x12\xac\x02\n\x17RemoveAddressGroupItems\x12?.google.cloud.networksecurity.v1.RemoveAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xb0\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02P"K/v1/{address_group=organizations/*/locations/*/addressGroups/*}:removeItems:\x01*\x12\xb8\x02\n\x16CloneAddressGroupItems\x12>.google.cloud.networksecurity.v1.CloneAddressGroupItemsRequest\x1a\x1d.google.longrunning.Operation"\xbe\x01\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA"address_group,source_address_group\x82\xd3\xe4\x93\x02O"J/v1/{address_group=organizations/*/locations/*/addressGroups/*}:cloneItems:\x01*\x12\x84\x02\n\x12DeleteAddressGroup\x12:.google.cloud.networksecurity.v1.DeleteAddressGroupRequest\x1a\x1d.google.longrunning.Operation"\x92\x01\xcaAJ\n\x15google.protobuf.Empty\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=organizations/*/locations/*/addressGroups/*}\x12\x8d\x02\n\x1aListAddressGroupReferences\x12B.google.cloud.networksecurity.v1.ListAddressGroupReferencesRequest\x1aC.google.cloud.networksecurity.v1.ListAddressGroupReferencesResponse"f\xdaA\raddress_group\x82\xd3\xe4\x93\x02P\x12N/v1/{address_group=organizations/*/locations/*/addressGroups/*}:listReferences\x1aR\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdd\x02\n#com.google.cloud.networksecurity.v1B\x11AddressGroupProtoP\x01ZMcloud.google.com/go/networksecurity/apiv1/networksecuritypb;networksecuritypb\xaa\x02\x1fGoogle.Cloud.NetworkSecurity.V1\xca\x02\x1fGoogle\\Cloud\\NetworkSecurity\\V1\xea\x02"Google::Cloud::NetworkSecurity::V1\xeaAh\n3networksecurity.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.networksecurity.v1.address_group_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.networksecurity.v1B\x11AddressGroupProtoP\x01ZMcloud.google.com/go/networksecurity/apiv1/networksecuritypb;networksecuritypb\xaa\x02\x1fGoogle.Cloud.NetworkSecurity.V1\xca\x02\x1fGoogle\\Cloud\\NetworkSecurity\\V1\xea\x02"Google::Cloud::NetworkSecurity::V1\xeaAh\n3networksecurity.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}'
    _globals['_ADDRESSGROUP_LABELSENTRY']._loaded_options = None
    _globals['_ADDRESSGROUP_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ADDRESSGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSGROUP'].fields_by_name['description']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ADDRESSGROUP'].fields_by_name['create_time']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADDRESSGROUP'].fields_by_name['update_time']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADDRESSGROUP'].fields_by_name['labels']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ADDRESSGROUP'].fields_by_name['type']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSGROUP'].fields_by_name['items']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['items']._serialized_options = b'\xe0A\x01'
    _globals['_ADDRESSGROUP'].fields_by_name['capacity']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['capacity']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSGROUP'].fields_by_name['self_link']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_ADDRESSGROUP'].fields_by_name['purpose']._loaded_options = None
    _globals['_ADDRESSGROUP'].fields_by_name['purpose']._serialized_options = b'\xe0A\x01'
    _globals['_ADDRESSGROUP']._loaded_options = None
    _globals['_ADDRESSGROUP']._serialized_options = b'\xeaA\xc5\x01\n+networksecurity.googleapis.com/AddressGroup\x12Eprojects/{project}/locations/{location}/addressGroups/{address_group}\x12Oorganizations/{organization}/locations/{location}/addressGroups/{address_group}'
    _globals['_LISTADDRESSGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTADDRESSGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTADDRESSGROUPSREQUEST'].fields_by_name['return_partial_success']._loaded_options = None
    _globals['_LISTADDRESSGROUPSREQUEST'].fields_by_name['return_partial_success']._serialized_options = b'\xe0A\x01'
    _globals['_GETADDRESSGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETADDRESSGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+networksecurity.googleapis.com/AddressGroup'
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['address_group_id']._loaded_options = None
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['address_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEADDRESSGROUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEADDRESSGROUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEADDRESSGROUPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEADDRESSGROUPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_DELETEADDRESSGROUPREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEADDRESSGROUPREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['items']._loaded_options = None
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['items']._serialized_options = b'\xe0A\x02'
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_ADDADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['items']._loaded_options = None
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['items']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['source_address_group']._loaded_options = None
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['source_address_group']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CLONEADDRESSGROUPITEMSREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTADDRESSGROUPREFERENCESREQUEST'].fields_by_name['address_group']._loaded_options = None
    _globals['_LISTADDRESSGROUPREFERENCESREQUEST'].fields_by_name['address_group']._serialized_options = b'\xe0A\x02\xfaA-\n+networksecurity.googleapis.com/AddressGroup'
    _globals['_ADDRESSGROUPSERVICE']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE']._serialized_options = b'\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroups']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1/{parent=projects/*/locations/*}/addressGroups'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['GetAddressGroup']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['GetAddressGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1/{name=projects/*/locations/*/addressGroups/*}'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['CreateAddressGroup']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['CreateAddressGroup']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA%parent,address_group,address_group_id\x82\xd3\xe4\x93\x02B"1/v1/{parent=projects/*/locations/*}/addressGroups:\raddress_group'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['UpdateAddressGroup']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['UpdateAddressGroup']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x19address_group,update_mask\x82\xd3\xe4\x93\x02P2?/v1/{address_group.name=projects/*/locations/*/addressGroups/*}:\raddress_group'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['AddAddressGroupItems']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['AddAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02H"C/v1/{address_group=projects/*/locations/*/addressGroups/*}:addItems:\x01*'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['RemoveAddressGroupItems']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['RemoveAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02K"F/v1/{address_group=projects/*/locations/*/addressGroups/*}:removeItems:\x01*'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['CloneAddressGroupItems']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['CloneAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA"address_group,source_address_group\x82\xd3\xe4\x93\x02J"E/v1/{address_group=projects/*/locations/*/addressGroups/*}:cloneItems:\x01*'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['DeleteAddressGroup']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['DeleteAddressGroup']._serialized_options = b'\xcaAJ\n\x15google.protobuf.Empty\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1/{name=projects/*/locations/*/addressGroups/*}'
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroupReferences']._loaded_options = None
    _globals['_ADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroupReferences']._serialized_options = b'\xdaA\raddress_group\x82\xd3\xe4\x93\x02K\x12I/v1/{address_group=projects/*/locations/*/addressGroups/*}:listReferences'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE']._serialized_options = b'\xcaA\x1enetworksecurity.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroups']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=organizations/*/locations/*}/addressGroups'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['GetAddressGroup']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['GetAddressGroup']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=organizations/*/locations/*/addressGroups/*}'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['CreateAddressGroup']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['CreateAddressGroup']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA%parent,address_group,address_group_id\x82\xd3\xe4\x93\x02G"6/v1/{parent=organizations/*/locations/*}/addressGroups:\raddress_group'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['UpdateAddressGroup']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['UpdateAddressGroup']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x19address_group,update_mask\x82\xd3\xe4\x93\x02U2D/v1/{address_group.name=organizations/*/locations/*/addressGroups/*}:\raddress_group'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['AddAddressGroupItems']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['AddAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02M"H/v1/{address_group=organizations/*/locations/*/addressGroups/*}:addItems:\x01*'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['RemoveAddressGroupItems']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['RemoveAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x13address_group,items\x82\xd3\xe4\x93\x02P"K/v1/{address_group=organizations/*/locations/*/addressGroups/*}:removeItems:\x01*'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['CloneAddressGroupItems']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['CloneAddressGroupItems']._serialized_options = b'\xcaAA\n\x0cAddressGroup\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA"address_group,source_address_group\x82\xd3\xe4\x93\x02O"J/v1/{address_group=organizations/*/locations/*/addressGroups/*}:cloneItems:\x01*'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['DeleteAddressGroup']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['DeleteAddressGroup']._serialized_options = b'\xcaAJ\n\x15google.protobuf.Empty\x121google.cloud.networksecurity.v1.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=organizations/*/locations/*/addressGroups/*}'
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroupReferences']._loaded_options = None
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE'].methods_by_name['ListAddressGroupReferences']._serialized_options = b'\xdaA\raddress_group\x82\xd3\xe4\x93\x02P\x12N/v1/{address_group=organizations/*/locations/*/addressGroups/*}:listReferences'
    _globals['_ADDRESSGROUP']._serialized_start = 308
    _globals['_ADDRESSGROUP']._serialized_end = 1137
    _globals['_ADDRESSGROUP_LABELSENTRY']._serialized_start = 772
    _globals['_ADDRESSGROUP_LABELSENTRY']._serialized_end = 817
    _globals['_ADDRESSGROUP_TYPE']._serialized_start = 819
    _globals['_ADDRESSGROUP_TYPE']._serialized_end = 867
    _globals['_ADDRESSGROUP_PURPOSE']._serialized_start = 869
    _globals['_ADDRESSGROUP_PURPOSE']._serialized_end = 933
    _globals['_LISTADDRESSGROUPSREQUEST']._serialized_start = 1140
    _globals['_LISTADDRESSGROUPSREQUEST']._serialized_end = 1301
    _globals['_LISTADDRESSGROUPSRESPONSE']._serialized_start = 1304
    _globals['_LISTADDRESSGROUPSRESPONSE']._serialized_end = 1448
    _globals['_GETADDRESSGROUPREQUEST']._serialized_start = 1450
    _globals['_GETADDRESSGROUPREQUEST']._serialized_end = 1541
    _globals['_CREATEADDRESSGROUPREQUEST']._serialized_start = 1544
    _globals['_CREATEADDRESSGROUPREQUEST']._serialized_end = 1771
    _globals['_UPDATEADDRESSGROUPREQUEST']._serialized_start = 1774
    _globals['_UPDATEADDRESSGROUPREQUEST']._serialized_end = 1955
    _globals['_DELETEADDRESSGROUPREQUEST']._serialized_start = 1957
    _globals['_DELETEADDRESSGROUPREQUEST']._serialized_end = 2076
    _globals['_ADDADDRESSGROUPITEMSREQUEST']._serialized_start = 2079
    _globals['_ADDADDRESSGROUPITEMSREQUEST']._serialized_end = 2229
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST']._serialized_start = 2232
    _globals['_REMOVEADDRESSGROUPITEMSREQUEST']._serialized_end = 2385
    _globals['_CLONEADDRESSGROUPITEMSREQUEST']._serialized_start = 2388
    _globals['_CLONEADDRESSGROUPITEMSREQUEST']._serialized_end = 2603
    _globals['_LISTADDRESSGROUPREFERENCESREQUEST']._serialized_start = 2606
    _globals['_LISTADDRESSGROUPREFERENCESREQUEST']._serialized_end = 2756
    _globals['_LISTADDRESSGROUPREFERENCESRESPONSE']._serialized_start = 2759
    _globals['_LISTADDRESSGROUPREFERENCESRESPONSE']._serialized_end = 3043
    _globals['_LISTADDRESSGROUPREFERENCESRESPONSE_ADDRESSGROUPREFERENCE']._serialized_start = 2947
    _globals['_LISTADDRESSGROUPREFERENCESRESPONSE_ADDRESSGROUPREFERENCE']._serialized_end = 3043
    _globals['_ADDRESSGROUPSERVICE']._serialized_start = 3046
    _globals['_ADDRESSGROUPSERVICE']._serialized_end = 5568
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE']._serialized_start = 5571
    _globals['_ORGANIZATIONADDRESSGROUPSERVICE']._serialized_end = 8150