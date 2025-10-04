"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/sql/v1beta4/cloud_sql_users.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.sql.v1beta4 import cloud_sql_resources_pb2 as google_dot_cloud_dot_sql_dot_v1beta4_dot_cloud__sql__resources__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/sql/v1beta4/cloud_sql_users.proto\x12\x18google.cloud.sql.v1beta4\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a2google/cloud/sql/v1beta4/cloud_sql_resources.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"V\n\x15SqlUsersDeleteRequest\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t"S\n\x12SqlUsersGetRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0c\n\x04host\x18\x04 \x01(\t"h\n\x15SqlUsersInsertRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12,\n\x04body\x18d \x01(\x0b2\x1e.google.cloud.sql.v1beta4.User"8\n\x13SqlUsersListRequest\x12\x10\n\x08instance\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t"\x89\x01\n\x15SqlUsersUpdateRequest\x12\x11\n\x04host\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x10\n\x08instance\x18\x02 \x01(\t\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12,\n\x04body\x18d \x01(\x0b2\x1e.google.cloud.sql.v1beta4.User"\x8b\x02\n\x1cUserPasswordValidationPolicy\x12\x1f\n\x17allowed_failed_attempts\x18\x01 \x01(\x05\x12?\n\x1cpassword_expiration_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12$\n\x1cenable_failed_attempts_check\x18\x03 \x01(\x08\x12=\n\x06status\x18\x04 \x01(\x0b2(.google.cloud.sql.v1beta4.PasswordStatusB\x03\xe0A\x03\x12$\n\x1cenable_password_verification\x18\x05 \x01(\x08"^\n\x0ePasswordStatus\x12\x0e\n\x06locked\x18\x01 \x01(\x08\x12<\n\x18password_expiration_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"\xf1\x05\n\x04User\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x10\n\x08password\x18\x02 \x01(\t\x12\x0c\n\x04etag\x18\x03 \x01(\t\x12\x0c\n\x04name\x18\x04 \x01(\t\x12\x11\n\x04host\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x10\n\x08instance\x18\x06 \x01(\t\x12\x0f\n\x07project\x18\x07 \x01(\t\x128\n\x04type\x18\x08 \x01(\x0e2*.google.cloud.sql.v1beta4.User.SqlUserType\x12P\n\x16sqlserver_user_details\x18\t \x01(\x0b2..google.cloud.sql.v1beta4.SqlServerUserDetailsH\x00\x12O\n\x0fpassword_policy\x18\x0c \x01(\x0b26.google.cloud.sql.v1beta4.UserPasswordValidationPolicy\x12P\n\x12dual_password_type\x18\r \x01(\x0e2/.google.cloud.sql.v1beta4.User.DualPasswordTypeH\x01\x88\x01\x01"\xa2\x01\n\x0bSqlUserType\x12\x0c\n\x08BUILT_IN\x10\x00\x12\x12\n\x0eCLOUD_IAM_USER\x10\x01\x12\x1d\n\x19CLOUD_IAM_SERVICE_ACCOUNT\x10\x02\x12\x13\n\x0fCLOUD_IAM_GROUP\x10\x03\x12\x18\n\x14CLOUD_IAM_GROUP_USER\x10\x04\x12#\n\x1fCLOUD_IAM_GROUP_SERVICE_ACCOUNT\x10\x05"|\n\x10DualPasswordType\x12"\n\x1eDUAL_PASSWORD_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17NO_MODIFY_DUAL_PASSWORD\x10\x01\x12\x14\n\x10NO_DUAL_PASSWORD\x10\x02\x12\x11\n\rDUAL_PASSWORD\x10\x03B\x0e\n\x0cuser_detailsB\x15\n\x13_dual_password_type">\n\x14SqlServerUserDetails\x12\x10\n\x08disabled\x18\x01 \x01(\x08\x12\x14\n\x0cserver_roles\x18\x02 \x03(\t"m\n\x11UsersListResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12-\n\x05items\x18\x02 \x03(\x0b2\x1e.google.cloud.sql.v1beta4.User\x12\x1b\n\x0fnext_page_token\x18\x03 \x01(\tB\x02\x18\x012\xd4\x07\n\x0fSqlUsersService\x12\xa2\x01\n\x06Delete\x12/.google.cloud.sql.v1beta4.SqlUsersDeleteRequest\x1a#.google.cloud.sql.v1beta4.Operation"B\x82\xd3\xe4\x93\x02<*:/sql/v1beta4/projects/{project}/instances/{instance}/users\x12\x9e\x01\n\x03Get\x12,.google.cloud.sql.v1beta4.SqlUsersGetRequest\x1a\x1e.google.cloud.sql.v1beta4.User"I\x82\xd3\xe4\x93\x02C\x12A/sql/v1beta4/projects/{project}/instances/{instance}/users/{name}\x12\xa8\x01\n\x06Insert\x12/.google.cloud.sql.v1beta4.SqlUsersInsertRequest\x1a#.google.cloud.sql.v1beta4.Operation"H\x82\xd3\xe4\x93\x02B":/sql/v1beta4/projects/{project}/instances/{instance}/users:\x04body\x12\xa6\x01\n\x04List\x12-.google.cloud.sql.v1beta4.SqlUsersListRequest\x1a+.google.cloud.sql.v1beta4.UsersListResponse"B\x82\xd3\xe4\x93\x02<\x12:/sql/v1beta4/projects/{project}/instances/{instance}/users\x12\xa8\x01\n\x06Update\x12/.google.cloud.sql.v1beta4.SqlUsersUpdateRequest\x1a#.google.cloud.sql.v1beta4.Operation"H\x82\xd3\xe4\x93\x02B\x1a:/sql/v1beta4/projects/{project}/instances/{instance}/users:\x04body\x1a|\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.adminBd\n\x1ccom.google.cloud.sql.v1beta4B\x12CloudSqlUsersProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.sql.v1beta4.cloud_sql_users_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.sql.v1beta4B\x12CloudSqlUsersProtoP\x01Z.cloud.google.com/go/sql/apiv1beta4/sqlpb;sqlpb'
    _globals['_SQLUSERSUPDATEREQUEST'].fields_by_name['host']._loaded_options = None
    _globals['_SQLUSERSUPDATEREQUEST'].fields_by_name['host']._serialized_options = b'\xe0A\x01'
    _globals['_USERPASSWORDVALIDATIONPOLICY'].fields_by_name['status']._loaded_options = None
    _globals['_USERPASSWORDVALIDATIONPOLICY'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_USER'].fields_by_name['host']._loaded_options = None
    _globals['_USER'].fields_by_name['host']._serialized_options = b'\xe0A\x01'
    _globals['_USERSLISTRESPONSE'].fields_by_name['next_page_token']._loaded_options = None
    _globals['_USERSLISTRESPONSE'].fields_by_name['next_page_token']._serialized_options = b'\x18\x01'
    _globals['_SQLUSERSSERVICE']._loaded_options = None
    _globals['_SQLUSERSSERVICE']._serialized_options = b'\xcaA\x17sqladmin.googleapis.com\xd2A_https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/sqlservice.admin'
    _globals['_SQLUSERSSERVICE'].methods_by_name['Delete']._loaded_options = None
    _globals['_SQLUSERSSERVICE'].methods_by_name['Delete']._serialized_options = b'\x82\xd3\xe4\x93\x02<*:/sql/v1beta4/projects/{project}/instances/{instance}/users'
    _globals['_SQLUSERSSERVICE'].methods_by_name['Get']._loaded_options = None
    _globals['_SQLUSERSSERVICE'].methods_by_name['Get']._serialized_options = b'\x82\xd3\xe4\x93\x02C\x12A/sql/v1beta4/projects/{project}/instances/{instance}/users/{name}'
    _globals['_SQLUSERSSERVICE'].methods_by_name['Insert']._loaded_options = None
    _globals['_SQLUSERSSERVICE'].methods_by_name['Insert']._serialized_options = b'\x82\xd3\xe4\x93\x02B":/sql/v1beta4/projects/{project}/instances/{instance}/users:\x04body'
    _globals['_SQLUSERSSERVICE'].methods_by_name['List']._loaded_options = None
    _globals['_SQLUSERSSERVICE'].methods_by_name['List']._serialized_options = b'\x82\xd3\xe4\x93\x02<\x12:/sql/v1beta4/projects/{project}/instances/{instance}/users'
    _globals['_SQLUSERSSERVICE'].methods_by_name['Update']._loaded_options = None
    _globals['_SQLUSERSSERVICE'].methods_by_name['Update']._serialized_options = b'\x82\xd3\xe4\x93\x02B\x1a:/sql/v1beta4/projects/{project}/instances/{instance}/users:\x04body'
    _globals['_SQLUSERSDELETEREQUEST']._serialized_start = 281
    _globals['_SQLUSERSDELETEREQUEST']._serialized_end = 367
    _globals['_SQLUSERSGETREQUEST']._serialized_start = 369
    _globals['_SQLUSERSGETREQUEST']._serialized_end = 452
    _globals['_SQLUSERSINSERTREQUEST']._serialized_start = 454
    _globals['_SQLUSERSINSERTREQUEST']._serialized_end = 558
    _globals['_SQLUSERSLISTREQUEST']._serialized_start = 560
    _globals['_SQLUSERSLISTREQUEST']._serialized_end = 616
    _globals['_SQLUSERSUPDATEREQUEST']._serialized_start = 619
    _globals['_SQLUSERSUPDATEREQUEST']._serialized_end = 756
    _globals['_USERPASSWORDVALIDATIONPOLICY']._serialized_start = 759
    _globals['_USERPASSWORDVALIDATIONPOLICY']._serialized_end = 1026
    _globals['_PASSWORDSTATUS']._serialized_start = 1028
    _globals['_PASSWORDSTATUS']._serialized_end = 1122
    _globals['_USER']._serialized_start = 1125
    _globals['_USER']._serialized_end = 1878
    _globals['_USER_SQLUSERTYPE']._serialized_start = 1551
    _globals['_USER_SQLUSERTYPE']._serialized_end = 1713
    _globals['_USER_DUALPASSWORDTYPE']._serialized_start = 1715
    _globals['_USER_DUALPASSWORDTYPE']._serialized_end = 1839
    _globals['_SQLSERVERUSERDETAILS']._serialized_start = 1880
    _globals['_SQLSERVERUSERDETAILS']._serialized_end = 1942
    _globals['_USERSLISTRESPONSE']._serialized_start = 1944
    _globals['_USERSLISTRESPONSE']._serialized_end = 2053
    _globals['_SQLUSERSSERVICE']._serialized_start = 2056
    _globals['_SQLUSERSSERVICE']._serialized_end = 3036