"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_flags.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/sql/v1/cloud_sql_flags.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto\x1a\x1egoogle/protobuf/wrappers.proto"/\n\x13SqlFlagsListRequest\x12\x18\n\x10database_version\x18\x01 \x01(\t"K\n\x11FlagsListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12(\n\x05items\x18\x02 \x03(\x0b2\x19.google.cloud.sql.v1.Flag"\x8d\x03\n\x04Flag\x12\x0c\n\x04name\x18\x01 \x01(\t\x12.\n\x04type\x18\x02 \x01(\x0e2 .google.cloud.sql.v1.SqlFlagType\x12;\n\napplies_to\x18\x03 \x03(\x0e2\'.google.cloud.sql.v1.SqlDatabaseVersion\x12\x1d\n\x15allowed_string_values\x18\x04 \x03(\t\x12.\n\tmin_value\x18\x05 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12.\n\tmax_value\x18\x06 \x01(\x0b2\x1b.google.protobuf.Int64Value\x124\n\x10requires_restart\x18\x07 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x0c\n\x04kind\x18\x08 \x01(\t\x12+\n\x07in_beta\x18\t \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x1a\n\x12allowed_int_values\x18\n \x03(\x03*\x97\x01\n\x0bSqlFlagType\x12\x1d\n\x19SQL_FLAG_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07BOOLEAN\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x0b\n\x07INTEGER\x10\x03\x12\x08\n\x04NONE\x10\x04\x12\x19\n\x15MYSQL_TIMEZONE_OFFSET\x10\x05\x12\t\n\x05FLOAT\x10\x06\x12\x13\n\x0fREPEATED_STRING\x10\x072\xfc\x01\n\x0fSqlFlagsService\x12k\n\x04List\x12(.google.cloud.sql.v1.SqlFlagsListRequest\x1a&.google.cloud.sql.v1.FlagsListResponse"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/flags\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBZ\n\x17com.google.cloud.sql.v1B\x12CloudSqlFlagsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_flags_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x12CloudSqlFlagsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_SQLFLAGSSERVICE']._loaded_options = None
    _globals['_SQLFLAGSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLFLAGSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLFLAGSSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/flags'
    _globals['_SQLFLAGTYPE']._serialized_start = 727
    _globals['_SQLFLAGTYPE']._serialized_end = 878
    _globals['_SQLFLAGSLISTREQUEST']._serialized_start = 200
    _globals['_SQLFLAGSLISTREQUEST']._serialized_end = 247
    _globals['_FLAGSLISTRESPONSE']._serialized_start = 249
    _globals['_FLAGSLISTRESPONSE']._serialized_end = 324
    _globals['_FLAG']._serialized_start = 327
    _globals['_FLAG']._serialized_end = 724
    _globals['_SQLFLAGSSERVICE']._serialized_start = 881
    _globals['_SQLFLAGSSERVICE']._serialized_end = 1133