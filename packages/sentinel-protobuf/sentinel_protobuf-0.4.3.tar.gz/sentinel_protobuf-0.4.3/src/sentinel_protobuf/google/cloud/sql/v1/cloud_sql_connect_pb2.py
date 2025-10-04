"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1/cloud_sql_connect.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.sql.v1 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1_dot_cloud__sql__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/sql/v1/cloud_sql_connect.proto\x12\x13google.cloud.sql.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a-google/cloud/sql/v1/cloud_sql_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"r\n\x19GetConnectSettingsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x122\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"\xe3\x03\n\x0fConnectSettings\x12\x0c\n\x04kind\x18\x01 \x01(\t\x124\n\x0eserver_ca_cert\x18\x02 \x01(\x0b2\x1c.google.cloud.sql.v1.SslCert\x124\n\x0cip_addresses\x18\x03 \x03(\x0b2\x1e.google.cloud.sql.v1.IpMapping\x12\x0e\n\x06region\x18\x04 \x01(\t\x12A\n\x10database_version\x18\x1f \x01(\x0e2\'.google.cloud.sql.v1.SqlDatabaseVersion\x129\n\x0cbackend_type\x18  \x01(\x0e2#.google.cloud.sql.v1.SqlBackendType\x12\x13\n\x0bpsc_enabled\x18! \x01(\x08\x12\x10\n\x08dns_name\x18" \x01(\t\x12C\n\x0eserver_ca_mode\x18# \x01(\x0e2+.google.cloud.sql.v1.ConnectSettings.CaMode"\\\n\x06CaMode\x12\x17\n\x13CA_MODE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aGOOGLE_MANAGED_INTERNAL_CA\x10\x01\x12\x19\n\x15GOOGLE_MANAGED_CAS_CA\x10\x02"\xf6\x01\n\x1cGenerateEphemeralCertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x1e\n\npublic_key\x18\x03 \x01(\tR\npublic_key\x12\'\n\x0caccess_token\x18\x04 \x01(\tB\x03\xe0A\x01R\x0caccess_token\x122\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x126\n\x0evalid_duration\x18\x0c \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"U\n\x1dGenerateEphemeralCertResponse\x124\n\x0eephemeral_cert\x18\x01 \x01(\x0b2\x1c.google.cloud.sql.v1.SslCert2\x92\x04\n\x11SqlConnectService\x12\xaf\x01\n\x12GetConnectSettings\x12..google.cloud.sql.v1.GetConnectSettingsRequest\x1a$.google.cloud.sql.v1.ConnectSettings"C\x82\xd3\xe4\x93\x02=\x12;/v1/projects/{project}/instances/{instance}/connectSettings\x12\xcc\x01\n\x15GenerateEphemeralCert\x121.google.cloud.sql.v1.GenerateEphemeralCertRequest\x1a2.google.cloud.sql.v1.GenerateEphemeralCertResponse"L\x82\xd3\xe4\x93\x02F"A/v1/projects/{project}/instances/{instance}:generateEphemeralCert:\x01*\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminB\\\n\x17com.google.cloud.sql.v1B\x14CloudSqlConnectProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1.cloud_sql_connect_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.cloud.sql.v1B\x14CloudSqlConnectProtoP\x01Z)cloud.google.com/go/sql/apiv1/sqlpb;sqlpb'
    _globals['_GETCONNECTSETTINGSREQUEST'].fields_by_name['read_time']._loaded_options = None
    _globals['_GETCONNECTSETTINGSREQUEST'].fields_by_name['read_time']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['access_token']._loaded_options = None
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['access_token']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['read_time']._loaded_options = None
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['read_time']._serialized_options = b'\xe0A\x01'
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['valid_duration']._loaded_options = None
    _globals['_GENERATEEPHEMERALCERTREQUEST'].fields_by_name['valid_duration']._serialized_options = b'\xe0A\x01'
    _globals['_SQLCONNECTSERVICE']._loaded_options = None
    _globals['_SQLCONNECTSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GetConnectSettings']._loaded_options = None
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GetConnectSettings']._serialized_options = b'\x82\xd3\xe4\x93\x02=\x12;/v1/projects/{project}/instances/{instance}/connectSettings'
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GenerateEphemeralCert']._loaded_options = None
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GenerateEphemeralCert']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v1/projects/{project}/instances/{instance}:generateEphemeralCert:\x01*'
    _globals['_GETCONNECTSETTINGSREQUEST']._serialized_start = 268
    _globals['_GETCONNECTSETTINGSREQUEST']._serialized_end = 382
    _globals['_CONNECTSETTINGS']._serialized_start = 385
    _globals['_CONNECTSETTINGS']._serialized_end = 868
    _globals['_CONNECTSETTINGS_CAMODE']._serialized_start = 776
    _globals['_CONNECTSETTINGS_CAMODE']._serialized_end = 868
    _globals['_GENERATEEPHEMERALCERTREQUEST']._serialized_start = 871
    _globals['_GENERATEEPHEMERALCERTREQUEST']._serialized_end = 1117
    _globals['_GENERATEEPHEMERALCERTRESPONSE']._serialized_start = 1119
    _globals['_GENERATEEPHEMERALCERTRESPONSE']._serialized_end = 1204
    _globals['_SQLCONNECTSERVICE']._serialized_start = 1207
    _globals['_SQLCONNECTSERVICE']._serialized_end = 1737