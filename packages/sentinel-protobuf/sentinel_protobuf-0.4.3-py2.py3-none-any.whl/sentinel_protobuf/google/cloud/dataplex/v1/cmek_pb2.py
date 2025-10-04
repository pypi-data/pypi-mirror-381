"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataplex/v1/cmek.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import service_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/dataplex/v1/cmek.proto\x12\x18google.cloud.dataplex.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/dataplex/v1/service.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd0\x06\n\x10EncryptionConfig\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x08\xfaA*\n(dataplex.googleapis.com/EncryptionConfig\x12\x10\n\x03key\x18\x02 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12Y\n\x10encryption_state\x18\x05 \x01(\x0e2:.google.cloud.dataplex.v1.EncryptionConfig.EncryptionStateB\x03\xe0A\x03\x12\x0c\n\x04etag\x18\x06 \x01(\t\x12W\n\x0ffailure_details\x18\x07 \x01(\x0b29.google.cloud.dataplex.v1.EncryptionConfig.FailureDetailsB\x03\xe0A\x03\x1a\xd1\x01\n\x0eFailureDetails\x12\\\n\nerror_code\x18\x01 \x01(\x0e2C.google.cloud.dataplex.v1.EncryptionConfig.FailureDetails.ErrorCodeB\x03\xe0A\x03\x12\x1a\n\rerror_message\x18\x02 \x01(\tB\x03\xe0A\x03"E\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x17\n\x13REQUIRE_USER_ACTION\x10\x02"^\n\x0fEncryptionState\x12 \n\x1cENCRYPTION_STATE_UNSPECIFIED\x10\x00\x12\x0e\n\nENCRYPTING\x10\x01\x12\r\n\tCOMPLETED\x10\x02\x12\n\n\x06FAILED\x10\x03:\x87\x01\xeaA\x83\x01\n(dataplex.googleapis.com/EncryptionConfig\x12Worganizations/{organization}/locations/{location}/encryptionConfigs/{encryption_config}"\xd4\x01\n\x1dCreateEncryptionConfigRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,dataplex.googleapis.com/OrganizationLocation\x12!\n\x14encryption_config_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12J\n\x11encryption_config\x18\x03 \x01(\x0b2*.google.cloud.dataplex.v1.EncryptionConfigB\x03\xe0A\x02"\\\n\x1aGetEncryptionConfigRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dataplex.googleapis.com/EncryptionConfig"\xa1\x01\n\x1dUpdateEncryptionConfigRequest\x12J\n\x11encryption_config\x18\x01 \x01(\x0b2*.google.cloud.dataplex.v1.EncryptionConfigB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"r\n\x1dDeleteEncryptionConfigRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dataplex.googleapis.com/EncryptionConfig\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"\xbd\x01\n\x1cListEncryptionConfigsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\x12(dataplex.googleapis.com/EncryptionConfig\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\xc7\x01\n\x1dListEncryptionConfigsResponse\x12F\n\x12encryption_configs\x18\x01 \x03(\x0b2*.google.cloud.dataplex.v1.EncryptionConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12E\n\x15unreachable_locations\x18\x03 \x03(\tB&\xfaA#\n!locations.googleapis.com/Location2\xaa\n\n\x0bCmekService\x12\xa0\x02\n\x16CreateEncryptionConfig\x127.google.cloud.dataplex.v1.CreateEncryptionConfigRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA%\n\x10EncryptionConfig\x12\x11OperationMetadata\xdaA-parent,encryption_config,encryption_config_id\x82\xd3\xe4\x93\x02O":/v1/{parent=organizations/*/locations/*}/encryptionConfigs:\x11encryption_config\x12\xa2\x02\n\x16UpdateEncryptionConfig\x127.google.cloud.dataplex.v1.UpdateEncryptionConfigRequest\x1a\x1d.google.longrunning.Operation"\xaf\x01\xcaA%\n\x10EncryptionConfig\x12\x11OperationMetadata\xdaA\x1dencryption_config,update_mask\x82\xd3\xe4\x93\x02a2L/v1/{encryption_config.name=organizations/*/locations/*/encryptionConfigs/*}:\x11encryption_config\x12\xe8\x01\n\x16DeleteEncryptionConfig\x127.google.cloud.dataplex.v1.DeleteEncryptionConfigRequest\x1a\x1d.google.longrunning.Operation"v\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=organizations/*/locations/*/encryptionConfigs/*}\x12\xd5\x01\n\x15ListEncryptionConfigs\x126.google.cloud.dataplex.v1.ListEncryptionConfigsRequest\x1a7.google.cloud.dataplex.v1.ListEncryptionConfigsResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=organizations/*/locations/*}/encryptionConfigs\x12\xc2\x01\n\x13GetEncryptionConfig\x124.google.cloud.dataplex.v1.GetEncryptionConfigRequest\x1a*.google.cloud.dataplex.v1.EncryptionConfig"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=organizations/*/locations/*/encryptionConfigs/*}\x1aK\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9d\x02\n\x1ccom.google.cloud.dataplex.v1B\tCmekProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb\xaa\x02\x18Google.Cloud.Dataplex.V1\xca\x02\x18Google\\Cloud\\Dataplex\\V1\xea\x02\x1bGoogle::Cloud::Dataplex::V1\xeaAa\n,dataplex.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.cmek_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\tCmekProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb\xaa\x02\x18Google.Cloud.Dataplex.V1\xca\x02\x18Google\\Cloud\\Dataplex\\V1\xea\x02\x1bGoogle::Cloud::Dataplex::V1\xeaAa\n,dataplex.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}'
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS'].fields_by_name['error_code']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS'].fields_by_name['error_code']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS'].fields_by_name['error_message']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS'].fields_by_name['error_message']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xfaA*\n(dataplex.googleapis.com/EncryptionConfig'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['key']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['key']._serialized_options = b'\xe0A\x01'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['encryption_state']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['encryption_state']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['failure_details']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG'].fields_by_name['failure_details']._serialized_options = b'\xe0A\x03'
    _globals['_ENCRYPTIONCONFIG']._loaded_options = None
    _globals['_ENCRYPTIONCONFIG']._serialized_options = b'\xeaA\x83\x01\n(dataplex.googleapis.com/EncryptionConfig\x12Worganizations/{organization}/locations/{location}/encryptionConfigs/{encryption_config}'
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\n,dataplex.googleapis.com/OrganizationLocation'
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config_id']._loaded_options = None
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_CREATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETENCRYPTIONCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENCRYPTIONCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dataplex.googleapis.com/EncryptionConfig'
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config']._loaded_options = None
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST'].fields_by_name['encryption_config']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEENCRYPTIONCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENCRYPTIONCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dataplex.googleapis.com/EncryptionConfig'
    _globals['_DELETEENCRYPTIONCONFIGREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEENCRYPTIONCONFIGREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\x12(dataplex.googleapis.com/EncryptionConfig'
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENCRYPTIONCONFIGSRESPONSE'].fields_by_name['unreachable_locations']._loaded_options = None
    _globals['_LISTENCRYPTIONCONFIGSRESPONSE'].fields_by_name['unreachable_locations']._serialized_options = b'\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CMEKSERVICE']._loaded_options = None
    _globals['_CMEKSERVICE']._serialized_options = b'\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CMEKSERVICE'].methods_by_name['CreateEncryptionConfig']._loaded_options = None
    _globals['_CMEKSERVICE'].methods_by_name['CreateEncryptionConfig']._serialized_options = b'\xcaA%\n\x10EncryptionConfig\x12\x11OperationMetadata\xdaA-parent,encryption_config,encryption_config_id\x82\xd3\xe4\x93\x02O":/v1/{parent=organizations/*/locations/*}/encryptionConfigs:\x11encryption_config'
    _globals['_CMEKSERVICE'].methods_by_name['UpdateEncryptionConfig']._loaded_options = None
    _globals['_CMEKSERVICE'].methods_by_name['UpdateEncryptionConfig']._serialized_options = b'\xcaA%\n\x10EncryptionConfig\x12\x11OperationMetadata\xdaA\x1dencryption_config,update_mask\x82\xd3\xe4\x93\x02a2L/v1/{encryption_config.name=organizations/*/locations/*/encryptionConfigs/*}:\x11encryption_config'
    _globals['_CMEKSERVICE'].methods_by_name['DeleteEncryptionConfig']._loaded_options = None
    _globals['_CMEKSERVICE'].methods_by_name['DeleteEncryptionConfig']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1/{name=organizations/*/locations/*/encryptionConfigs/*}'
    _globals['_CMEKSERVICE'].methods_by_name['ListEncryptionConfigs']._loaded_options = None
    _globals['_CMEKSERVICE'].methods_by_name['ListEncryptionConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=organizations/*/locations/*}/encryptionConfigs'
    _globals['_CMEKSERVICE'].methods_by_name['GetEncryptionConfig']._loaded_options = None
    _globals['_CMEKSERVICE'].methods_by_name['GetEncryptionConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1/{name=organizations/*/locations/*/encryptionConfigs/*}'
    _globals['_ENCRYPTIONCONFIG']._serialized_start = 354
    _globals['_ENCRYPTIONCONFIG']._serialized_end = 1202
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS']._serialized_start = 759
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS']._serialized_end = 968
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS_ERRORCODE']._serialized_start = 899
    _globals['_ENCRYPTIONCONFIG_FAILUREDETAILS_ERRORCODE']._serialized_end = 968
    _globals['_ENCRYPTIONCONFIG_ENCRYPTIONSTATE']._serialized_start = 970
    _globals['_ENCRYPTIONCONFIG_ENCRYPTIONSTATE']._serialized_end = 1064
    _globals['_CREATEENCRYPTIONCONFIGREQUEST']._serialized_start = 1205
    _globals['_CREATEENCRYPTIONCONFIGREQUEST']._serialized_end = 1417
    _globals['_GETENCRYPTIONCONFIGREQUEST']._serialized_start = 1419
    _globals['_GETENCRYPTIONCONFIGREQUEST']._serialized_end = 1511
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST']._serialized_start = 1514
    _globals['_UPDATEENCRYPTIONCONFIGREQUEST']._serialized_end = 1675
    _globals['_DELETEENCRYPTIONCONFIGREQUEST']._serialized_start = 1677
    _globals['_DELETEENCRYPTIONCONFIGREQUEST']._serialized_end = 1791
    _globals['_LISTENCRYPTIONCONFIGSREQUEST']._serialized_start = 1794
    _globals['_LISTENCRYPTIONCONFIGSREQUEST']._serialized_end = 1983
    _globals['_LISTENCRYPTIONCONFIGSRESPONSE']._serialized_start = 1986
    _globals['_LISTENCRYPTIONCONFIGSRESPONSE']._serialized_end = 2185
    _globals['_CMEKSERVICE']._serialized_start = 2188
    _globals['_CMEKSERVICE']._serialized_end = 3510