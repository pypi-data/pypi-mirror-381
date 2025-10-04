"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_operations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/sql/v1/cloud_sql_operations.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto\x1a\x1bgoogle/protobuf/empty.proto"=\n\x17SqlOperationsGetRequest\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t"f\n\x18SqlOperationsListRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x13\n\x0bmax_results\x18\x02 \x01(\r\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t"n\n\x16OperationsListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12-\n\x05items\x18\x02 \x03(\x0b2\x1e.google.cloud.sql.v1.Operation\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t"@\n\x1aSqlOperationsCancelRequest\x12\x11\n\toperation\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t2\xc3\x04\n\x14SqlOperationsService\x12\x8a\x01\n\x03Get\x12,.google.cloud.sql.v1.SqlOperationsGetRequest\x1a\x1e.google.cloud.sql.v1.Operation"5\x82\xd3\xe4\x93\x02/\x12-/v1/projects/{project}/operations/{operation}\x12\x8d\x01\n\x04List\x12-.google.cloud.sql.v1.SqlOperationsListRequest\x1a+.google.cloud.sql.v1.OperationsListResponse")\x82\xd3\xe4\x93\x02#\x12!/v1/projects/{project}/operations\x12\x8f\x01\n\x06Cancel\x12/.google.cloud.sql.v1.SqlOperationsCancelRequest\x1a\x16.google.protobuf.Empty"<\x82\xd3\xe4\x93\x026"4/v1/projects/{project}/operations/{operation}/cancel\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminB_\n\x17com.google.cloud.sql.v1B\x17CloudSqlOperationsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x17CloudSqlOperationsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_SQLOPERATIONSSERVICE']._loaded_options = None
    _globals['_SQLOPERATIONSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['Get']._loaded_options = None
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['Get']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/v1/projects/{project}/operations/{operation}'
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x02#\x12!/v1/projects/{project}/operations'
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['Cancel']._loaded_options = None
    _globals['_SQLOPERATIONSSERVICE'].methods_by_name['Cancel']._serialized_options = b'\x82\xd3\xe4\x93\x026"4/v1/projects/{project}/operations/{operation}/cancel'
    _globals['_SQLOPERATIONSGETREQUEST']._serialized_start = 235
    _globals['_SQLOPERATIONSGETREQUEST']._serialized_end = 296
    _globals['_SQLOPERATIONSLISTREQUEST']._serialized_start = 298
    _globals['_SQLOPERATIONSLISTREQUEST']._serialized_end = 400
    _globals['_OPERATIONSLISTRESPONSE']._serialized_start = 402
    _globals['_OPERATIONSLISTRESPONSE']._serialized_end = 512
    _globals['_SQLOPERATIONSCANCELREQUEST']._serialized_start = 514
    _globals['_SQLOPERATIONSCANCELREQUEST']._serialized_end = 578
    _globals['_SQLOPERATIONSSERVICE']._serialized_start = 581
    _globals['_SQLOPERATIONSSERVICE']._serialized_end = 1160