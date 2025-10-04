"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1beta4/cloud_sql_tiers.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/sql/v1beta4/cloud_sql_tiers.proto\x12\x18google.cloud.sql.v1beta4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto"&\n\x13SqlTiersListRequest\x12\x0f\n\x07project\x18\x01 \x01(\t"P\n\x11TiersListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12-\n\x05items\x18\x02 \x03(\x0b2\x1e.google.cloud.sql.v1beta4.Tier"S\n\x04Tier\x12\x0c\n\x04tier\x18\x01 \x01(\t\x12\x0b\n\x03RAM\x18\x02 \x01(\x03\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12\x12\n\nDisk_Quota\x18\x04 \x01(\x03\x12\x0e\n\x06region\x18\x05 \x03(\t2\xa3\x02\n\x0fSqlTiersService\x12\x91\x01\n\x04List\x12-.google.cloud.sql.v1beta4.SqlTiersListRequest\x1a+.google.cloud.sql.v1beta4.TiersListResponse"-\x82\xd3\xe4\x93\x02\'\x12%/sql/v1beta4/projects/{project}/tiers\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBd\n\x1ccom.google.cloud.sql.v1beta4B\x12CloudSqlTiersProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1beta4.cloud_sql_tiers_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.sql.v1beta4B\x12CloudSqlTiersProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpb'
    _globals['_SQLTIERSSERVICE']._loaded_options = None
    _globals['_SQLTIERSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLTIERSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLTIERSSERVICE'].methods_by_name['List']._serialized_options = b"\x82\xd3\xe4\x93\x02'\x12%/sql/v1beta4/projects/{project}/tiers"
    _globals['_SQLTIERSLISTREQUEST']._serialized_start = 131
    _globals['_SQLTIERSLISTREQUEST']._serialized_end = 169
    _globals['_TIERSLISTRESPONSE']._serialized_start = 171
    _globals['_TIERSLISTRESPONSE']._serialized_end = 251
    _globals['_TIER']._serialized_start = 253
    _globals['_TIER']._serialized_end = 336
    _globals['_SQLTIERSSERVICE']._serialized_start = 339
    _globals['_SQLTIERSSERVICE']._serialized_end = 630