"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_ssl_certs.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/sql/v1/cloud_sql_ssl_certs.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto"W\n\x18SqlSslCertsDeleteRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x18\n\x10sha1_fingerprint\x18\x03 \x01(\t"T\n\x15SqlSslCertsGetRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x18\n\x10sha1_fingerprint\x18\x03 \x01(\t"w\n\x18SqlSslCertsInsertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x128\n\x04body\x18d \x01(\x0b2*.google.cloud.sql.v1.SslCertsInsertRequest";\n\x16SqlSslCertsListRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t",\n\x15SslCertsInsertRequest\x12\x13\n\x0bcommon_name\x18\x01 \x01(\t"\xc8\x01\n\x16SslCertsInsertResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x121\n\toperation\x18\x02 \x01(\x0b2\x1e.google.cloud.sql.v1.Operation\x124\n\x0eserver_ca_cert\x18\x03 \x01(\x0b2\x1c.google.cloud.sql.v1.SslCert\x127\n\x0bclient_cert\x18\x04 \x01(\x0b2".google.cloud.sql.v1.SslCertDetail"Q\n\x14SslCertsListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12+\n\x05items\x18\x02 \x03(\x0b2\x1c.google.cloud.sql.v1.SslCert2\xaa\x06\n\x12SqlSslCertsService\x12\xa8\x01\n\x06Delete\x12-.google.cloud.sql.v1.SqlSslCertsDeleteRequest\x1a\x1e.google.cloud.sql.v1.Operation"O\x82\xd3\xe4\x93\x02I*G/v1/projects/{project}/instances/{instance}/sslCerts/{sha1_fingerprint}\x12\xa0\x01\n\x03Get\x12*.google.cloud.sql.v1.SqlSslCertsGetRequest\x1a\x1c.google.cloud.sql.v1.SslCert"O\x82\xd3\xe4\x93\x02I\x12G/v1/projects/{project}/instances/{instance}/sslCerts/{sha1_fingerprint}\x12\xa8\x01\n\x06Insert\x12-.google.cloud.sql.v1.SqlSslCertsInsertRequest\x1a+.google.cloud.sql.v1.SslCertsInsertResponse"B\x82\xd3\xe4\x93\x02<"4/v1/projects/{project}/instances/{instance}/sslCerts:\x04body\x12\x9c\x01\n\x04List\x12+.google.cloud.sql.v1.SqlSslCertsListRequest\x1a).google.cloud.sql.v1.SslCertsListResponse"<\x82\xd3\xe4\x93\x026\x124/v1/projects/{project}/instances/{instance}/sslCerts\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminB]\n\x17com.google.cloud.sql.v1B\x15CloudSqlSslCertsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_ssl_certs_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x15CloudSqlSslCertsProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_SQLSSLCERTSSERVICE']._loaded_options = None
    _globals['_SQLSSLCERTSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Delete']._loaded_options = None
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Delete']._serialized_options = b'\x82\xd3\xe4\x93\x02I*G/v1/projects/{project}/instances/{instance}/sslCerts/{sha1_fingerprint}'
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Get']._loaded_options = None
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Get']._serialized_options = b'\x82\xd3\xe4\x93\x02I\x12G/v1/projects/{project}/instances/{instance}/sslCerts/{sha1_fingerprint}'
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Insert']._loaded_options = None
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['Insert']._serialized_options = b'\x82\xd3\xe4\x93\x02<"4/v1/projects/{project}/instances/{instance}/sslCerts:\x04body'
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLSSLCERTSSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/v1/projects/{project}/instances/{instance}/sslCerts'
    _globals['_SQLSSLCERTSDELETEREQUEST']._serialized_start = 172
    _globals['_SQLSSLCERTSDELETEREQUEST']._serialized_end = 259
    _globals['_SQLSSLCERTSGETREQUEST']._serialized_start = 261
    _globals['_SQLSSLCERTSGETREQUEST']._serialized_end = 345
    _globals['_SQLSSLCERTSINSERTREQUEST']._serialized_start = 347
    _globals['_SQLSSLCERTSINSERTREQUEST']._serialized_end = 466
    _globals['_SQLSSLCERTSLISTREQUEST']._serialized_start = 468
    _globals['_SQLSSLCERTSLISTREQUEST']._serialized_end = 527
    _globals['_SSLCERTSINSERTREQUEST']._serialized_start = 529
    _globals['_SSLCERTSINSERTREQUEST']._serialized_end = 573
    _globals['_SSLCERTSINSERTRESPONSE']._serialized_start = 576
    _globals['_SSLCERTSINSERTRESPONSE']._serialized_end = 776
    _globals['_SSLCERTSLISTRESPONSE']._serialized_start = 778
    _globals['_SSLCERTSLISTRESPONSE']._serialized_end = 859
    _globals['_SQLSSLCERTSSERVICE']._serialized_start = 862
    _globals['_SQLSSLCERTSSERVICE']._serialized_end = 1672