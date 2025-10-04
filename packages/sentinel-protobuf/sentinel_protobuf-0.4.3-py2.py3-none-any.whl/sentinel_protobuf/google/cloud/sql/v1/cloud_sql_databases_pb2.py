"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_databases.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/sql/v1/cloud_sql_databases.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto"P\n\x19SqlDatabasesDeleteRequest\x12\x10\n\x08database\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t"M\n\x16SqlDatabasesGetRequest\x12\x10\n\x08database\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t"k\n\x19SqlDatabasesInsertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12+\n\x04body\x18d \x01(\x0b2\x1d.google.cloud.sql.v1.Database"<\n\x17SqlDatabasesListRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t"}\n\x19SqlDatabasesUpdateRequest\x12\x10\n\x08database\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12+\n\x04body\x18d \x01(\x0b2\x1d.google.cloud.sql.v1.Database"S\n\x15DatabasesListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12,\n\x05items\x18\x02 \x03(\x0b2\x1d.google.cloud.sql.v1.Database2\xed\x08\n\x13SqlDatabasesService\x12\xa2\x01\n\x06Delete\x12..google.cloud.sql.v1.SqlDatabasesDeleteRequest\x1a\x1e.google.cloud.sql.v1.Operation"H\x82\xd3\xe4\x93\x02B*@/v1/projects/{project}/instances/{instance}/databases/{database}\x12\x9b\x01\n\x03Get\x12+.google.cloud.sql.v1.SqlDatabasesGetRequest\x1a\x1d.google.cloud.sql.v1.Database"H\x82\xd3\xe4\x93\x02B\x12@/v1/projects/{project}/instances/{instance}/databases/{database}\x12\x9d\x01\n\x06Insert\x12..google.cloud.sql.v1.SqlDatabasesInsertRequest\x1a\x1e.google.cloud.sql.v1.Operation"C\x82\xd3\xe4\x93\x02="5/v1/projects/{project}/instances/{instance}/databases:\x04body\x12\x9f\x01\n\x04List\x12,.google.cloud.sql.v1.SqlDatabasesListRequest\x1a*.google.cloud.sql.v1.DatabasesListResponse"=\x82\xd3\xe4\x93\x027\x125/v1/projects/{project}/instances/{instance}/databases\x12\xa7\x01\n\x05Patch\x12..google.cloud.sql.v1.SqlDatabasesUpdateRequest\x1a\x1e.google.cloud.sql.v1.Operation"N\x82\xd3\xe4\x93\x02H2@/v1/projects/{project}/instances/{instance}/databases/{database}:\x04body\x12\xa8\x01\n\x06Update\x12..google.cloud.sql.v1.SqlDatabasesUpdateRequest\x1a\x1e.google.cloud.sql.v1.Operation"N\x82\xd3\xe4\x93\x02H\x1a@/v1/projects/{project}/instances/{instance}/databases/{database}:\x04body\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminB^\n\x17com.google.cloud.sql.v1B\x16CloudSqlDatabasesProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_databases_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x16CloudSqlDatabasesProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_SQLDATABASESSERVICE']._loaded_options = None
    _globals['_SQLDATABASESSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Delete']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Delete']._serialized_options = b'\x82\xd3\xe4\x93\x02B*@/v1/projects/{project}/instances/{instance}/databases/{database}'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Get']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Get']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x12@/v1/projects/{project}/instances/{instance}/databases/{database}'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Insert']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Insert']._serialized_options = b'\x82\xd3\xe4\x93\x02="5/v1/projects/{project}/instances/{instance}/databases:\x04body'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x027\x125/v1/projects/{project}/instances/{instance}/databases'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Patch']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Patch']._serialized_options = b'\x82\xd3\xe4\x93\x02H2@/v1/projects/{project}/instances/{instance}/databases/{database}:\x04body'
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Update']._loaded_options = None
    _globals['_SQLDATABASESSERVICE'].methods_by_name['Update']._serialized_options = b'\x82\xd3\xe4\x93\x02H\x1a@/v1/projects/{project}/instances/{instance}/databases/{database}:\x04body'
    _globals['_SQLDATABASESDELETEREQUEST']._serialized_start = 172
    _globals['_SQLDATABASESDELETEREQUEST']._serialized_end = 252
    _globals['_SQLDATABASESGETREQUEST']._serialized_start = 254
    _globals['_SQLDATABASESGETREQUEST']._serialized_end = 331
    _globals['_SQLDATABASESINSERTREQUEST']._serialized_start = 333
    _globals['_SQLDATABASESINSERTREQUEST']._serialized_end = 440
    _globals['_SQLDATABASESLISTREQUEST']._serialized_start = 442
    _globals['_SQLDATABASESLISTREQUEST']._serialized_end = 502
    _globals['_SQLDATABASESUPDATEREQUEST']._serialized_start = 504
    _globals['_SQLDATABASESUPDATEREQUEST']._serialized_end = 629
    _globals['_DATABASESLISTRESPONSE']._serialized_start = 631
    _globals['_DATABASESLISTRESPONSE']._serialized_end = 714
    _globals['_SQLDATABASESSERVICE']._serialized_start = 717
    _globals['_SQLDATABASESSERVICE']._serialized_end = 1850