"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1beta4/cloud_sql_connect.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.sql.v1beta4 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1beta4_dot_cloud__sql__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/sql/v1beta4/cloud_sql_connect.proto\x12\x18google.cloud.sql.v1beta4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/cloud/sql/v1beta4/cloud_sql_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"r\n\x19GetConnectSettingsRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x122\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01"\xd4\x02\n\x0fConnectSettings\x12\x0c\n\x04kind\x18\x01 \x01(\t\x129\n\x0eserver_ca_cert\x18\x02 \x01(\x0b2!.google.cloud.sql.v1beta4.SslCert\x129\n\x0cip_addresses\x18\x03 \x03(\x0b2#.google.cloud.sql.v1beta4.IpMapping\x12\x0e\n\x06region\x18\x04 \x01(\t\x12F\n\x10database_version\x18\x1f \x01(\x0e2,.google.cloud.sql.v1beta4.SqlDatabaseVersion\x12>\n\x0cbackend_type\x18  \x01(\x0e2(.google.cloud.sql.v1beta4.SqlBackendType\x12\x13\n\x0bpsc_enabled\x18! \x01(\x08\x12\x10\n\x08dns_name\x18" \x01(\t"\xdc\x01\n\x1cGenerateEphemeralCertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x12\n\npublic_key\x18\x03 \x01(\t\x12\x19\n\x0caccess_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x126\n\x0evalid_duration\x18\x0c \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01"Z\n\x1dGenerateEphemeralCertResponse\x129\n\x0eephemeral_cert\x18\x01 \x01(\x0b2!.google.cloud.sql.v1beta4.SslCert2\xb8\x04\n\x11SqlConnectService\x12\xc2\x01\n\x12GetConnectSettings\x123.google.cloud.sql.v1beta4.GetConnectSettingsRequest\x1a).google.cloud.sql.v1beta4.ConnectSettings"L\x82\xd3\xe4\x93\x02F\x12D/sql/v1beta4/projects/{project}/instances/{instance}/connectSettings\x12\xdf\x01\n\x15GenerateEphemeralCert\x126.google.cloud.sql.v1beta4.GenerateEphemeralCertRequest\x1a7.google.cloud.sql.v1beta4.GenerateEphemeralCertResponse"U\x82\xd3\xe4\x93\x02O"J/sql/v1beta4/projects/{project}/instances/{instance}:generateEphemeralCert:\x01*\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBf\n\x1ccom.google.cloud.sql.v1beta4B\x14CloudSqlConnectProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1beta4.cloud_sql_connect_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.sql.v1beta4B\x14CloudSqlConnectProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpb'
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
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GetConnectSettings']._serialized_options = b'\x82\xd3\xe4\x93\x02F\x12D/sql/v1beta4/projects/{project}/instances/{instance}/connectSettings'
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GenerateEphemeralCert']._loaded_options = None
    _globals['_SQLCONNECTSERVICE'].methods_by_name['GenerateEphemeralCert']._serialized_options = b'\x82\xd3\xe4\x93\x02O"J/sql/v1beta4/projects/{project}/instances/{instance}:generateEphemeralCert:\x01*'
    _globals['_GETCONNECTSETTINGSREQUEST']._serialized_start = 283
    _globals['_GETCONNECTSETTINGSREQUEST']._serialized_end = 397
    _globals['_CONNECTSETTINGS']._serialized_start = 400
    _globals['_CONNECTSETTINGS']._serialized_end = 740
    _globals['_GENERATEEPHEMERALCERTREQUEST']._serialized_start = 743
    _globals['_GENERATEEPHEMERALCERTREQUEST']._serialized_end = 963
    _globals['_GENERATEEPHEMERALCERTRESPONSE']._serialized_start = 965
    _globals['_GENERATEEPHEMERALCERTRESPONSE']._serialized_end = 1055
    _globals['_SQLCONNECTSERVICE']._serialized_start = 1058
    _globals['_SQLCONNECTSERVICE']._serialized_end = 1626