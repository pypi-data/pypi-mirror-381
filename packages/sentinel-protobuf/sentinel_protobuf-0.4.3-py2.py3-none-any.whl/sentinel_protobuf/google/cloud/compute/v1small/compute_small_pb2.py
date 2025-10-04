"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/compute/v1small/compute_small.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud import extended_operations_pb2 as google_dot_cloud_dot_extended__operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/compute/v1small/compute_small.proto\x12\x1cgoogle.cloud.compute.v1small\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/extended_operations.proto"\xfe\x08\n\x07Address\x12\x18\n\x07address\x18\xf4\xb7\xde\xdc\x01 \x01(\tH\x00\x88\x01\x01\x12\x1c\n\x0caddress_type\x18\xa5\x89\x84~ \x01(\tH\x01\x88\x01\x01\x12"\n\x12creation_timestamp\x18\xb6\x8f\xc7\x0e \x01(\tH\x02\x88\x01\x01\x12\x1c\n\x0bdescription\x18\xfc\x87\xd6\xc9\x01 \x01(\tH\x03\x88\x01\x01\x12\x10\n\x02id\x18\x9b\x1a \x01(\x04H\x04\x88\x01\x01\x12\x1b\n\nip_version\x18\xc0\xf3\xd2\x8c\x01 \x01(\tH\x05\x88\x01\x01\x12\x14\n\x04kind\x18\x94\xf7\xc8\x01 \x01(\tH\x06\x88\x01\x01\x12\x14\n\x04name\x18\x8b\xf5\xcd\x01 \x01(\tH\x07\x88\x01\x01\x12\x17\n\x07network\x18\xae\xb4\x85o \x01(\tH\x08\x88\x01\x01\x12\x1d\n\x0cnetwork_tier\x18\xd3\xba\xdb\xf6\x01 \x01(\tH\t\x88\x01\x01\x12\x1e\n\rprefix_length\x18\xb3\xba\xa3\xd8\x01 \x01(\x05H\n\x88\x01\x01\x12\x18\n\x07purpose\x18\x9e\xfa\xef\x96\x01 \x01(\tH\x0b\x88\x01\x01\x12\x16\n\x06region\x18\xf4\xcd\xa0B \x01(\tH\x0c\x88\x01\x01\x12\x1a\n\tself_link\x18\x8d\x92\xc5\xd9\x01 \x01(\tH\r\x88\x01\x01\x12\x16\n\x06status\x18\xf2\x9f\xb7V \x01(\tH\x0e\x88\x01\x01\x12\x1b\n\nsubnetwork\x18\xee\xa7\xe4\x92\x01 \x01(\tH\x0f\x88\x01\x01\x12\x10\n\x05users\x18\x88\x9c\x9a5 \x03(\t"e\n\x0bAddressType\x12\x1a\n\x16UNDEFINED_ADDRESS_TYPE\x10\x00\x12\x0f\n\x08EXTERNAL\x10\xcb\xa7\xfd\x10\x12\x10\n\x08INTERNAL\x10\xbd\xed\x96\x85\x01\x12\x17\n\x10UNSPECIFIED_TYPE\x10\xe2\xee\xdb\x19"[\n\tIpVersion\x12\x18\n\x14UNDEFINED_IP_VERSION\x10\x00\x12\x0b\n\x04IPV4\x10\x85\xcc\x89\x01\x12\x0b\n\x04IPV6\x10\x87\xcc\x89\x01\x12\x1a\n\x13UNSPECIFIED_VERSION\x10\x90\xcf\xb5\n"L\n\x0bNetworkTier\x12\x1a\n\x16UNDEFINED_NETWORK_TIER\x10\x00\x12\x0f\n\x07PREMIUM\x10\xb7\xb4\xc1\xbe\x01\x12\x10\n\x08STANDARD\x10\xbd\x9d\x8c\xe7\x01"q\n\x07Purpose\x12\x15\n\x11UNDEFINED_PURPOSE\x10\x00\x12\x14\n\x0cDNS_RESOLVER\x10\xfc\xdc\x83\xe3\x01\x12\x13\n\x0cGCE_ENDPOINT\x10\xab\xc4\xf5m\x12\x0f\n\x08NAT_AUTO\x10\xad\xb4\x85N\x12\x13\n\x0bVPC_PEERING\x10\xaa\xf3\x8e\xbf\x01"R\n\x06Status\x12\x14\n\x10UNDEFINED_STATUS\x10\x00\x12\r\n\x06IN_USE\x10\xcd\xce\xa5\x08\x12\x10\n\x08RESERVED\x10\xa8\xf6\x8d\xce\x01\x12\x11\n\tRESERVING\x10\xd9\xf4\xaf\xf5\x01B\n\n\x08_addressB\x0f\n\r_address_typeB\x15\n\x13_creation_timestampB\x0e\n\x0c_descriptionB\x05\n\x03_idB\r\n\x0b_ip_versionB\x07\n\x05_kindB\x07\n\x05_nameB\n\n\x08_networkB\x0f\n\r_network_tierB\x10\n\x0e_prefix_lengthB\n\n\x08_purposeB\t\n\x07_regionB\x0c\n\n_self_linkB\t\n\x07_statusB\r\n\x0b_subnetwork"\xad\x03\n\x15AddressAggregatedList\x12\x10\n\x02id\x18\x9b\x1a \x01(\tH\x00\x88\x01\x01\x12P\n\x05items\x18\xc0\xcf\xf7/ \x03(\x0b2>.google.cloud.compute.v1small.AddressAggregatedList.ItemsEntry\x12\x14\n\x04kind\x18\x94\xf7\xc8\x01 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x0fnext_page_token\x18\x95\xba\x86& \x01(\tH\x02\x88\x01\x01\x12\x1a\n\tself_link\x18\x8d\x92\xc5\xd9\x01 \x01(\tH\x03\x88\x01\x01\x12>\n\x07warning\x18\x9c\xdf\x96\x18 \x01(\x0b2%.google.cloud.compute.v1small.WarningH\x04\x88\x01\x01\x1a_\n\nItemsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12@\n\x05value\x18\x02 \x01(\x0b21.google.cloud.compute.v1small.AddressesScopedList:\x028\x01B\x05\n\x03_idB\x07\n\x05_kindB\x12\n\x10_next_page_tokenB\x0c\n\n_self_linkB\n\n\x08_warning"\xa9\x02\n\x0bAddressList\x12\x10\n\x02id\x18\x9b\x1a \x01(\tH\x00\x88\x01\x01\x127\n\x05items\x18\xc0\xcf\xf7/ \x03(\x0b2%.google.cloud.compute.v1small.Address\x12\x14\n\x04kind\x18\x94\xf7\xc8\x01 \x01(\tH\x01\x88\x01\x01\x12\x1f\n\x0fnext_page_token\x18\x95\xba\x86& \x01(\tH\x02\x88\x01\x01\x12\x1a\n\tself_link\x18\x8d\x92\xc5\xd9\x01 \x01(\tH\x03\x88\x01\x01\x12>\n\x07warning\x18\x9c\xdf\x96\x18 \x01(\x0b2%.google.cloud.compute.v1small.WarningH\x04\x88\x01\x01B\x05\n\x03_idB\x07\n\x05_kindB\x12\n\x10_next_page_tokenB\x0c\n\n_self_linkB\n\n\x08_warning"\x9f\x01\n\x13AddressesScopedList\x12<\n\taddresses\x18\xa2\xf7\x81\xa1\x01 \x03(\x0b2%.google.cloud.compute.v1small.Address\x12>\n\x07warning\x18\x9c\xdf\x96\x18 \x01(\x0b2%.google.cloud.compute.v1small.WarningH\x00\x88\x01\x01B\n\n\x08_warning"\x98\x02\n\x1eAggregatedListAddressesRequest\x12\x17\n\x06filter\x18\xf8\x96\xa3\xa0\x01 \x01(\tH\x00\x88\x01\x01\x12#\n\x12include_all_scopes\x18\xf4\xe1\xcc\xba\x01 \x01(\x08H\x01\x88\x01\x01\x12\x1b\n\x0bmax_results\x18\x9b\xc8\x8b\x1a \x01(\rH\x02\x88\x01\x01\x12\x18\n\x08order_by\x18\xe8\xfd\xc7L \x01(\tH\x03\x88\x01\x01\x12\x1a\n\npage_token\x18\xc9\xb0\xc4\t \x01(\tH\x04\x88\x01\x01\x12\x17\n\x07project\x18\x99\x96\xc1l \x01(\tB\x03\xe0A\x02B\t\n\x07_filterB\x15\n\x13_include_all_scopesB\x0e\n\x0c_max_resultsB\x0b\n\t_order_byB\r\n\x0b_page_token"C\n\x04Data\x12\x12\n\x03key\x18\xdf\xbc\x06 \x01(\tH\x00\x88\x01\x01\x12\x15\n\x05value\x18\xf1\xa2\xb25 \x01(\tH\x01\x88\x01\x01B\x06\n\x04_keyB\x08\n\x06_value"\x9f\x01\n\x14DeleteAddressRequest\x12\x18\n\x07address\x18\xf4\xb7\xde\xdc\x01 \x01(\tB\x03\xe0A\x02\x12!\n\x07project\x18\x99\x96\xc1l \x01(\tB\r\xe0A\x02\xf2G\x07project\x12\x1f\n\x06region\x18\xf4\xcd\xa0B \x01(\tB\x0c\xe0A\x02\xf2G\x06region\x12\x1a\n\nrequest_id\x18\xcb\x81\xd9\x11 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_request_id"A\n\x05Error\x128\n\x06errors\x18\xeb\xde\xd5\x96\x01 \x03(\x0b2$.google.cloud.compute.v1small.Errors"u\n\x06Errors\x12\x14\n\x04code\x18\xed\xdb\xba\x01 \x01(\tH\x00\x88\x01\x01\x12\x19\n\x08location\x18\xb5\xbf\xbe\x8a\x01 \x01(\tH\x01\x88\x01\x01\x12\x18\n\x07message\x18\x87\x80\xac\xc7\x01 \x01(\tH\x02\x88\x01\x01B\x07\n\x05_codeB\x0b\n\t_locationB\n\n\x08_message"n\n\x19GetRegionOperationRequest\x12 \n\toperation\x18\xe7\xaa\xeb\x18 \x01(\tB\n\xe0A\x02\xfaG\x04name\x12\x17\n\x07project\x18\x99\x96\xc1l \x01(\tB\x03\xe0A\x02\x12\x16\n\x06region\x18\xf4\xcd\xa0B \x01(\tB\x03\xe0A\x02"\xcf\x01\n\x14InsertAddressRequest\x12H\n\x10address_resource\x18\xf9\x97\xde\xe6\x01 \x01(\x0b2%.google.cloud.compute.v1small.AddressB\x03\xe0A\x02\x12!\n\x07project\x18\x99\x96\xc1l \x01(\tB\r\xe0A\x02\xf2G\x07project\x12\x1f\n\x06region\x18\xf4\xcd\xa0B \x01(\tB\x0c\xe0A\x02\xf2G\x06region\x12\x1a\n\nrequest_id\x18\xcb\x81\xd9\x11 \x01(\tH\x00\x88\x01\x01B\r\n\x0b_request_id"\xdd\x01\n\x14ListAddressesRequest\x12\x17\n\x06filter\x18\xf8\x96\xa3\xa0\x01 \x01(\tH\x00\x88\x01\x01\x12\x1b\n\x0bmax_results\x18\x9b\xc8\x8b\x1a \x01(\rH\x01\x88\x01\x01\x12\x18\n\x08order_by\x18\xe8\xfd\xc7L \x01(\tB\x03\xe0A\x02\x12\x1a\n\npage_token\x18\xc9\xb0\xc4\t \x01(\tH\x02\x88\x01\x01\x12\x17\n\x07project\x18\x99\x96\xc1l \x01(\tB\x03\xe0A\x02\x12\x16\n\x06region\x18\xf4\xcd\xa0B \x01(\tB\x03\xe0A\x02B\t\n\x07_filterB\x0e\n\x0c_max_resultsB\r\n\x0b_page_token"\xaf\t\n\tOperation\x12$\n\x13client_operation_id\x18\xe7\x8d\xde\x8d\x01 \x01(\tH\x00\x88\x01\x01\x12"\n\x12creation_timestamp\x18\xb6\x8f\xc7\x0e \x01(\tH\x01\x88\x01\x01\x12\x1c\n\x0bdescription\x18\xfc\x87\xd6\xc9\x01 \x01(\tH\x02\x88\x01\x01\x12\x18\n\x08end_time\x18\xb1\xa7\xe76 \x01(\tH\x03\x88\x01\x01\x12:\n\x05error\x18\x88\xa4\x93. \x01(\x0b2#.google.cloud.compute.v1small.ErrorH\x04\x88\x01\x01\x12\'\n\x12http_error_message\x18\xd9\xfa\xc8` \x01(\tB\x03\xe8G\x04H\x05\x88\x01\x01\x12,\n\x16http_error_status_code\x18\xec\x84\xf8\x94\x01 \x01(\x05B\x03\xe8G\x03H\x06\x88\x01\x01\x12\x10\n\x02id\x18\x9b\x1a \x01(\x04H\x07\x88\x01\x01\x12\x1c\n\x0binsert_time\x18\x93\xa9\xe8\xce\x01 \x01(\tH\x08\x88\x01\x01\x12\x14\n\x04kind\x18\x94\xf7\xc8\x01 \x01(\tH\t\x88\x01\x01\x12\x19\n\x04name\x18\x8b\xf5\xcd\x01 \x01(\tB\x03\xe8G\x01H\n\x88\x01\x01\x12\x1e\n\x0eoperation_type\x18\x92\xf6\xdaT \x01(\tH\x0b\x88\x01\x01\x12\x18\n\x08progress\x18\xad\x84\xd3" \x01(\x05H\x0c\x88\x01\x01\x12\x16\n\x06region\x18\xf4\xcd\xa0B \x01(\tH\r\x88\x01\x01\x12\x1a\n\tself_link\x18\x8d\x92\xc5\xd9\x01 \x01(\tH\x0e\x88\x01\x01\x12\x1a\n\nstart_time\x18\x8a\xe9\xee\x11 \x01(\tH\x0f\x88\x01\x01\x12K\n\x06status\x18\xf2\x9f\xb7V \x01(\x0e2..google.cloud.compute.v1small.Operation.StatusB\x03\xe8G\x02H\x10\x88\x01\x01\x12\x1f\n\x0estatus_message\x18\xba\xc9\xe9\x8d\x01 \x01(\tH\x11\x88\x01\x01\x12\x19\n\ttarget_id\x18\x89\x95\x8d{ \x01(\x04H\x12\x88\x01\x01\x12\x1b\n\x0btarget_link\x18\xe8\x93\xf1\x1d \x01(\tH\x13\x88\x01\x01\x12\x14\n\x04user\x18\xcb\xd7\xdb\x01 \x01(\tH\x14\x88\x01\x01\x12<\n\x08warnings\x18\xd7\x88\xc1\xed\x01 \x03(\x0b2&.google.cloud.compute.v1small.Warnings\x12\x14\n\x04zone\x18\xac\xc7\xe4\x01 \x01(\tH\x15\x88\x01\x01"K\n\x06Status\x12\x14\n\x10UNDEFINED_STATUS\x10\x00\x12\x0b\n\x04DONE\x10\x82\xb7\x80\x01\x12\x0e\n\x07PENDING\x10\xf7\xaa\xf0\x10\x12\x0e\n\x07RUNNING\x10\x9f\xc3\xea9B\x16\n\x14_client_operation_idB\x15\n\x13_creation_timestampB\x0e\n\x0c_descriptionB\x0b\n\t_end_timeB\x08\n\x06_errorB\x15\n\x13_http_error_messageB\x19\n\x17_http_error_status_codeB\x05\n\x03_idB\x0e\n\x0c_insert_timeB\x07\n\x05_kindB\x07\n\x05_nameB\x11\n\x0f_operation_typeB\x0b\n\t_progressB\t\n\x07_regionB\x0c\n\n_self_linkB\r\n\x0b_start_timeB\t\n\x07_statusB\x11\n\x0f_status_messageB\x0c\n\n_target_idB\x0e\n\x0c_target_linkB\x07\n\x05_userB\x07\n\x05_zone"h\n\x1aWaitRegionOperationRequest\x12\x19\n\toperation\x18\xe7\xaa\xeb\x18 \x01(\tB\x03\xe0A\x02\x12\x17\n\x07project\x18\x99\x96\xc1l \x01(\tB\x03\xe0A\x02\x12\x16\n\x06region\x18\xf4\xcd\xa0B \x01(\tB\x03\xe0A\x02"\x9f\x07\n\x07Warning\x12\x14\n\x04code\x18\xed\xdb\xba\x01 \x01(\tH\x00\x88\x01\x01\x123\n\x04data\x18\xaa\xdf\xbb\x01 \x03(\x0b2".google.cloud.compute.v1small.Data\x12\x18\n\x07message\x18\x87\x80\xac\xc7\x01 \x01(\tH\x01\x88\x01\x01"\x99\x06\n\x04Code\x12\x12\n\x0eUNDEFINED_CODE\x10\x00\x12\x15\n\x0eCLEANUP_FAILED\x10\xd8\x8c\xd6G\x12 \n\x18DEPRECATED_RESOURCE_USED\x10\xc2\xdf\xeb\xba\x01\x12\x1c\n\x14DEPRECATED_TYPE_USED\x10\x96\xa4\x9e\xa5\x01\x12(\n DISK_SIZE_LARGER_THAN_IMAGE_SIZE\x10\x97\x81\x95\xb0\x01\x12\x1e\n\x16EXPERIMENTAL_TYPE_USED\x10\x8b\x8e\xc1\xd7\x01\x12\x1b\n\x14EXTERNAL_API_WARNING\x10\xc3\xbf\xdaS\x12\x1d\n\x15FIELD_VALUE_OVERRIDEN\x10\xaf\xb6\x99\x9d\x01\x12#\n\x1bINJECTED_KERNELS_DEPRECATED\x10\x8b\xd9\x82\xc7\x01\x12\x1f\n\x17MISSING_TYPE_DEPENDENCY\x10\xf7\xf8\xa2\xa4\x01\x12%\n\x1dNEXT_HOP_ADDRESS_NOT_ASSIGNED\x10\x87\xa5\xfa\x9a\x01\x12"\n\x1aNEXT_HOP_CANNOT_IP_FORWARD\x10\xe7\xea\xe7\xb6\x01\x12#\n\x1bNEXT_HOP_INSTANCE_NOT_FOUND\x10\xce\xcc\xaf\xdd\x01\x12\'\n NEXT_HOP_INSTANCE_NOT_ON_NETWORK\x10\xc2\xe8\x9dt\x12\x1c\n\x14NEXT_HOP_NOT_RUNNING\x10\xb1\xcf\xf0\xc6\x01\x12\x19\n\x12NOT_CRITICAL_ERROR\x10\xd4\xa8\xb72\x12\x19\n\x12NO_RESULTS_ON_PAGE\x10\x88\xa6\xa9\x0e\x12\x1d\n\x16REQUIRED_TOS_AGREEMENT\x10\x83\xce\xe4\x01\x121\n)RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING\x10\xc1\xf4\xed\xec\x01\x12\x1b\n\x14RESOURCE_NOT_DELETED\x10\xbc\xb7\xb2P\x12!\n\x19SCHEMA_VALIDATION_IGNORED\x10\xca\xd4\x9f\x83\x01\x12(\n!SINGLE_INSTANCE_PROPERTY_TEMPLATE\x10\xd1\x89\xf8\x7f\x12\x1d\n\x15UNDECLARED_PROPERTIES\x10\x9f\x86\x9b\xba\x01\x12\x12\n\x0bUNREACHABLE\x10\xb4\xbd\xad\x06B\x07\n\x05_codeB\n\n\x08_message"\xa0\x07\n\x08Warnings\x12\x14\n\x04code\x18\xed\xdb\xba\x01 \x01(\tH\x00\x88\x01\x01\x123\n\x04data\x18\xaa\xdf\xbb\x01 \x03(\x0b2".google.cloud.compute.v1small.Data\x12\x18\n\x07message\x18\x87\x80\xac\xc7\x01 \x01(\tH\x01\x88\x01\x01"\x99\x06\n\x04Code\x12\x12\n\x0eUNDEFINED_CODE\x10\x00\x12\x15\n\x0eCLEANUP_FAILED\x10\xd8\x8c\xd6G\x12 \n\x18DEPRECATED_RESOURCE_USED\x10\xc2\xdf\xeb\xba\x01\x12\x1c\n\x14DEPRECATED_TYPE_USED\x10\x96\xa4\x9e\xa5\x01\x12(\n DISK_SIZE_LARGER_THAN_IMAGE_SIZE\x10\x97\x81\x95\xb0\x01\x12\x1e\n\x16EXPERIMENTAL_TYPE_USED\x10\x8b\x8e\xc1\xd7\x01\x12\x1b\n\x14EXTERNAL_API_WARNING\x10\xc3\xbf\xdaS\x12\x1d\n\x15FIELD_VALUE_OVERRIDEN\x10\xaf\xb6\x99\x9d\x01\x12#\n\x1bINJECTED_KERNELS_DEPRECATED\x10\x8b\xd9\x82\xc7\x01\x12\x1f\n\x17MISSING_TYPE_DEPENDENCY\x10\xf7\xf8\xa2\xa4\x01\x12%\n\x1dNEXT_HOP_ADDRESS_NOT_ASSIGNED\x10\x87\xa5\xfa\x9a\x01\x12"\n\x1aNEXT_HOP_CANNOT_IP_FORWARD\x10\xe7\xea\xe7\xb6\x01\x12#\n\x1bNEXT_HOP_INSTANCE_NOT_FOUND\x10\xce\xcc\xaf\xdd\x01\x12\'\n NEXT_HOP_INSTANCE_NOT_ON_NETWORK\x10\xc2\xe8\x9dt\x12\x1c\n\x14NEXT_HOP_NOT_RUNNING\x10\xb1\xcf\xf0\xc6\x01\x12\x19\n\x12NOT_CRITICAL_ERROR\x10\xd4\xa8\xb72\x12\x19\n\x12NO_RESULTS_ON_PAGE\x10\x88\xa6\xa9\x0e\x12\x1d\n\x16REQUIRED_TOS_AGREEMENT\x10\x83\xce\xe4\x01\x121\n)RESOURCE_IN_USE_BY_OTHER_RESOURCE_WARNING\x10\xc1\xf4\xed\xec\x01\x12\x1b\n\x14RESOURCE_NOT_DELETED\x10\xbc\xb7\xb2P\x12!\n\x19SCHEMA_VALIDATION_IGNORED\x10\xca\xd4\x9f\x83\x01\x12(\n!SINGLE_INSTANCE_PROPERTY_TEMPLATE\x10\xd1\x89\xf8\x7f\x12\x1d\n\x15UNDECLARED_PROPERTIES\x10\x9f\x86\x9b\xba\x01\x12\x12\n\x0bUNREACHABLE\x10\xb4\xbd\xad\x06B\x07\n\x05_codeB\n\n\x08_message2\xe5\x07\n\tAddresses\x12\xca\x01\n\x0eAggregatedList\x12<.google.cloud.compute.v1small.AggregatedListAddressesRequest\x1a3.google.cloud.compute.v1small.AddressAggregatedList"E\xdaA\x07project\x82\xd3\xe4\x93\x025\x123/compute/v1/projects/{project}/aggregated/addresses\x12\xde\x01\n\x06Delete\x122.google.cloud.compute.v1small.DeleteAddressRequest\x1a\'.google.cloud.compute.v1small.Operation"w\xdaA\x16project,region,address\x8aN\x10RegionOperations\x82\xd3\xe4\x93\x02E*C/compute/v1/projects/{project}/regions/{region}/addresses/{address}\x12\xf0\x01\n\x06Insert\x122.google.cloud.compute.v1small.InsertAddressRequest\x1a\'.google.cloud.compute.v1small.Operation"\x88\x01\xdaA\x1fproject,region,address_resource\x8aN\x10RegionOperations\x82\xd3\xe4\x93\x02M"9/compute/v1/projects/{project}/regions/{region}/addresses:\x10address_resource\x12\xc2\x01\n\x04List\x122.google.cloud.compute.v1small.ListAddressesRequest\x1a).google.cloud.compute.v1small.AddressList"[\xdaA\x17project,region,order_by\x82\xd3\xe4\x93\x02;\x129/compute/v1/projects/{project}/regions/{region}/addresses\x1ar\xcaA\x16compute.googleapis.com\xd2AVhttps://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/cloud-platform2\xf6\x04\n\x10RegionOperations\x12\xd5\x01\n\x03Get\x127.google.cloud.compute.v1small.GetRegionOperationRequest\x1a\'.google.cloud.compute.v1small.Operation"l\xdaA\x18project,region,operation\x90N\x01\x82\xd3\xe4\x93\x02H\x12F/compute/v1/projects/{project}/regions/{region}/operations/{operation}\x12\xe2\x01\n\x04Wait\x128.google.cloud.compute.v1small.WaitRegionOperationRequest\x1a\'.google.cloud.compute.v1small.Operation"w\xdaA\x18project,region,operation\x82\xd3\xe4\x93\x02V"T/compute/v1/projects/projects/{project}/regions/{region}/operations/{operation}/wait\x1a\xa4\x01\xcaA\x16compute.googleapis.com\xd2A\x87\x01https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/cloud-platformB\xc9\x01\n com.google.cloud.compute.v1smallP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/compute/v1small;compute\xaa\x02\x1cGoogle.Cloud.Compute.V1Small\xca\x02\x1cGoogle\\Cloud\\Compute\\V1small\xea\x02\x1fGoogle::Cloud::Compute::V1smallb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.compute.v1small.compute_small_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.cloud.compute.v1smallP\x01ZCgoogle.golang.org/genproto/googleapis/cloud/compute/v1small;compute\xaa\x02\x1cGoogle.Cloud.Compute.V1Small\xca\x02\x1cGoogle\\Cloud\\Compute\\V1small\xea\x02\x1fGoogle::Cloud::Compute::V1small'
    _globals['_ADDRESSAGGREGATEDLIST_ITEMSENTRY']._loaded_options = None
    _globals['_ADDRESSAGGREGATEDLIST_ITEMSENTRY']._serialized_options = b'8\x01'
    _globals['_AGGREGATEDLISTADDRESSESREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_AGGREGATEDLISTADDRESSESREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['address']._loaded_options = None
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['address']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02\xf2G\x07project'
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_DELETEADDRESSREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02\xf2G\x06region'
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02\xfaG\x04name'
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_GETREGIONOPERATIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['address_resource']._loaded_options = None
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['address_resource']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02\xf2G\x07project'
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_INSERTADDRESSREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02\xf2G\x06region'
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x02'
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_LISTADDRESSESREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_OPERATION'].fields_by_name['http_error_message']._loaded_options = None
    _globals['_OPERATION'].fields_by_name['http_error_message']._serialized_options = b'\xe8G\x04'
    _globals['_OPERATION'].fields_by_name['http_error_status_code']._loaded_options = None
    _globals['_OPERATION'].fields_by_name['http_error_status_code']._serialized_options = b'\xe8G\x03'
    _globals['_OPERATION'].fields_by_name['name']._loaded_options = None
    _globals['_OPERATION'].fields_by_name['name']._serialized_options = b'\xe8G\x01'
    _globals['_OPERATION'].fields_by_name['status']._loaded_options = None
    _globals['_OPERATION'].fields_by_name['status']._serialized_options = b'\xe8G\x02'
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['region']._loaded_options = None
    _globals['_WAITREGIONOPERATIONREQUEST'].fields_by_name['region']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSES']._loaded_options = None
    _globals['_ADDRESSES']._serialized_options = b'\xcaA\x16compute.googleapis.com\xd2AVhttps://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/cloud-platform'
    _globals['_ADDRESSES'].methods_by_name['AggregatedList']._loaded_options = None
    _globals['_ADDRESSES'].methods_by_name['AggregatedList']._serialized_options = b'\xdaA\x07project\x82\xd3\xe4\x93\x025\x123/compute/v1/projects/{project}/aggregated/addresses'
    _globals['_ADDRESSES'].methods_by_name['Delete']._loaded_options = None
    _globals['_ADDRESSES'].methods_by_name['Delete']._serialized_options = b'\xdaA\x16project,region,address\x8aN\x10RegionOperations\x82\xd3\xe4\x93\x02E*C/compute/v1/projects/{project}/regions/{region}/addresses/{address}'
    _globals['_ADDRESSES'].methods_by_name['Insert']._loaded_options = None
    _globals['_ADDRESSES'].methods_by_name['Insert']._serialized_options = b'\xdaA\x1fproject,region,address_resource\x8aN\x10RegionOperations\x82\xd3\xe4\x93\x02M"9/compute/v1/projects/{project}/regions/{region}/addresses:\x10address_resource'
    _globals['_ADDRESSES'].methods_by_name['List']._loaded_options = None
    _globals['_ADDRESSES'].methods_by_name['List']._serialized_options = b'\xdaA\x17project,region,order_by\x82\xd3\xe4\x93\x02;\x129/compute/v1/projects/{project}/regions/{region}/addresses'
    _globals['_REGIONOPERATIONS']._loaded_options = None
    _globals['_REGIONOPERATIONS']._serialized_options = b'\xcaA\x16compute.googleapis.com\xd2A\x87\x01https://www.googleapis.com/auth/compute.readonly,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/cloud-platform'
    _globals['_REGIONOPERATIONS'].methods_by_name['Get']._loaded_options = None
    _globals['_REGIONOPERATIONS'].methods_by_name['Get']._serialized_options = b'\xdaA\x18project,region,operation\x90N\x01\x82\xd3\xe4\x93\x02H\x12F/compute/v1/projects/{project}/regions/{region}/operations/{operation}'
    _globals['_REGIONOPERATIONS'].methods_by_name['Wait']._loaded_options = None
    _globals['_REGIONOPERATIONS'].methods_by_name['Wait']._serialized_options = b'\xdaA\x18project,region,operation\x82\xd3\xe4\x93\x02V"T/compute/v1/projects/projects/{project}/regions/{region}/operations/{operation}/wait'
    _globals['_ADDRESS']._serialized_start = 238
    _globals['_ADDRESS']._serialized_end = 1388
    _globals['_ADDRESS_ADDRESSTYPE']._serialized_start = 699
    _globals['_ADDRESS_ADDRESSTYPE']._serialized_end = 800
    _globals['_ADDRESS_IPVERSION']._serialized_start = 802
    _globals['_ADDRESS_IPVERSION']._serialized_end = 893
    _globals['_ADDRESS_NETWORKTIER']._serialized_start = 895
    _globals['_ADDRESS_NETWORKTIER']._serialized_end = 971
    _globals['_ADDRESS_PURPOSE']._serialized_start = 973
    _globals['_ADDRESS_PURPOSE']._serialized_end = 1086
    _globals['_ADDRESS_STATUS']._serialized_start = 1088
    _globals['_ADDRESS_STATUS']._serialized_end = 1170
    _globals['_ADDRESSAGGREGATEDLIST']._serialized_start = 1391
    _globals['_ADDRESSAGGREGATEDLIST']._serialized_end = 1820
    _globals['_ADDRESSAGGREGATEDLIST_ITEMSENTRY']._serialized_start = 1663
    _globals['_ADDRESSAGGREGATEDLIST_ITEMSENTRY']._serialized_end = 1758
    _globals['_ADDRESSLIST']._serialized_start = 1823
    _globals['_ADDRESSLIST']._serialized_end = 2120
    _globals['_ADDRESSESSCOPEDLIST']._serialized_start = 2123
    _globals['_ADDRESSESSCOPEDLIST']._serialized_end = 2282
    _globals['_AGGREGATEDLISTADDRESSESREQUEST']._serialized_start = 2285
    _globals['_AGGREGATEDLISTADDRESSESREQUEST']._serialized_end = 2565
    _globals['_DATA']._serialized_start = 2567
    _globals['_DATA']._serialized_end = 2634
    _globals['_DELETEADDRESSREQUEST']._serialized_start = 2637
    _globals['_DELETEADDRESSREQUEST']._serialized_end = 2796
    _globals['_ERROR']._serialized_start = 2798
    _globals['_ERROR']._serialized_end = 2863
    _globals['_ERRORS']._serialized_start = 2865
    _globals['_ERRORS']._serialized_end = 2982
    _globals['_GETREGIONOPERATIONREQUEST']._serialized_start = 2984
    _globals['_GETREGIONOPERATIONREQUEST']._serialized_end = 3094
    _globals['_INSERTADDRESSREQUEST']._serialized_start = 3097
    _globals['_INSERTADDRESSREQUEST']._serialized_end = 3304
    _globals['_LISTADDRESSESREQUEST']._serialized_start = 3307
    _globals['_LISTADDRESSESREQUEST']._serialized_end = 3528
    _globals['_OPERATION']._serialized_start = 3531
    _globals['_OPERATION']._serialized_end = 4730
    _globals['_OPERATION_STATUS']._serialized_start = 4328
    _globals['_OPERATION_STATUS']._serialized_end = 4403
    _globals['_WAITREGIONOPERATIONREQUEST']._serialized_start = 4732
    _globals['_WAITREGIONOPERATIONREQUEST']._serialized_end = 4836
    _globals['_WARNING']._serialized_start = 4839
    _globals['_WARNING']._serialized_end = 5766
    _globals['_WARNING_CODE']._serialized_start = 4952
    _globals['_WARNING_CODE']._serialized_end = 5745
    _globals['_WARNINGS']._serialized_start = 5769
    _globals['_WARNINGS']._serialized_end = 6697
    _globals['_WARNINGS_CODE']._serialized_start = 4952
    _globals['_WARNINGS_CODE']._serialized_end = 5745
    _globals['_ADDRESSES']._serialized_start = 6700
    _globals['_ADDRESSES']._serialized_end = 7697
    _globals['_REGIONOPERATIONS']._serialized_start = 7700
    _globals['_REGIONOPERATIONS']._serialized_end = 8330