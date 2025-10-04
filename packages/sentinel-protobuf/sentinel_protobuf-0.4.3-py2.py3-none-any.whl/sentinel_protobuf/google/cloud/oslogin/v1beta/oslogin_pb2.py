"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/oslogin/v1beta/oslogin.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.oslogin.common import common_pb2 as google_dot_cloud_dot_oslogin_dot_common_dot_common__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/oslogin/v1beta/oslogin.proto\x12\x1bgoogle.cloud.oslogin.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/oslogin/common/common.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xdd\x02\n\x0cLoginProfile\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12A\n\x0eposix_accounts\x18\x02 \x03(\x0b2).google.cloud.oslogin.common.PosixAccount\x12U\n\x0fssh_public_keys\x18\x03 \x03(\x0b2<.google.cloud.oslogin.v1beta.LoginProfile.SshPublicKeysEntry\x12?\n\rsecurity_keys\x18\x05 \x03(\x0b2(.google.cloud.oslogin.v1beta.SecurityKey\x1a_\n\x12SshPublicKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x128\n\x05value\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKey:\x028\x01"\xa0\x01\n\x19CreateSshPublicKeyRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x02"V\n\x19DeletePosixAccountRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/PosixAccount"V\n\x19DeleteSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey"\xaf\x01\n\x16GetLoginProfileRequest\x121\n\x04name\x18\x01 \x01(\tB#\xe0A\x02\xfaA\x1d\n\x1boslogin.googleapis.com/User\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x11\n\tsystem_id\x18\x03 \x01(\t\x12;\n\x04view\x18\x04 \x01(\x0e2-.google.cloud.oslogin.v1beta.LoginProfileView"S\n\x16GetSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey"\x84\x02\n\x19ImportSshPublicKeyRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xfaA%\x12#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x02\x12\x12\n\nproject_id\x18\x03 \x01(\t\x12;\n\x04view\x18\x04 \x01(\x0e2-.google.cloud.oslogin.v1beta.LoginProfileView\x12\x14\n\x07regions\x18\x05 \x03(\tB\x03\xe0A\x01"o\n\x1aImportSshPublicKeyResponse\x12@\n\rlogin_profile\x18\x01 \x01(\x0b2).google.cloud.oslogin.v1beta.LoginProfile\x12\x0f\n\x07details\x18\x02 \x01(\t"\xcf\x01\n\x19UpdateSshPublicKeyRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey\x12F\n\x0essh_public_key\x18\x02 \x01(\x0b2).google.cloud.oslogin.common.SshPublicKeyB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x86\x02\n\x0bSecurityKey\x12\x12\n\npublic_key\x18\x01 \x01(\t\x12\x13\n\x0bprivate_key\x18\x02 \x01(\t\x12O\n\x14universal_two_factor\x18\x03 \x01(\x0b2/.google.cloud.oslogin.v1beta.UniversalTwoFactorH\x00\x12:\n\tweb_authn\x18\x04 \x01(\x0b2%.google.cloud.oslogin.v1beta.WebAuthnH\x00\x12\x1c\n\x0fdevice_nickname\x18\x05 \x01(\tH\x01\x88\x01\x01B\x0f\n\rprotocol_typeB\x12\n\x10_device_nickname"$\n\x12UniversalTwoFactor\x12\x0e\n\x06app_id\x18\x01 \x01(\t"\x19\n\x08WebAuthn\x12\r\n\x05rp_id\x18\x01 \x01(\t"A\n\x17SignSshPublicKeyRequest\x12\x16\n\x0essh_public_key\x18\x01 \x01(\t\x12\x0e\n\x06parent\x18\x02 \x01(\t"9\n\x18SignSshPublicKeyResponse\x12\x1d\n\x15signed_ssh_public_key\x18\x01 \x01(\t*S\n\x10LoginProfileView\x12"\n\x1eLOGIN_PROFILE_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x10\n\x0cSECURITY_KEY\x10\x022\xf2\x0e\n\x0eOsLoginService\x12\xcf\x01\n\x12CreateSshPublicKey\x126.google.cloud.oslogin.v1beta.CreateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"V\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x028"&/v1beta/{parent=users/*}/sshPublicKeys:\x0essh_public_key\x12\x96\x01\n\x12DeletePosixAccount\x126.google.cloud.oslogin.v1beta.DeletePosixAccountRequest\x1a\x16.google.protobuf.Empty"0\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v1beta/{name=users/*/projects/*}\x12\x9b\x01\n\x12DeleteSshPublicKey\x126.google.cloud.oslogin.v1beta.DeleteSshPublicKeyRequest\x1a\x16.google.protobuf.Empty"5\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/v1beta/{name=users/*/sshPublicKeys/*}\x12\xa5\x01\n\x0fGetLoginProfile\x123.google.cloud.oslogin.v1beta.GetLoginProfileRequest\x1a).google.cloud.oslogin.v1beta.LoginProfile"2\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1beta/{name=users/*}/loginProfile\x12\xa8\x01\n\x0fGetSshPublicKey\x123.google.cloud.oslogin.v1beta.GetSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"5\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1beta/{name=users/*/sshPublicKeys/*}\x12\x85\x02\n\x12ImportSshPublicKey\x126.google.cloud.oslogin.v1beta.ImportSshPublicKeyRequest\x1a7.google.cloud.oslogin.v1beta.ImportSshPublicKeyResponse"~\xdaA\x15parent,ssh_public_key\xdaA parent,ssh_public_key,project_id\x82\xd3\xe4\x93\x02="+/v1beta/{parent=users/*}:importSshPublicKey:\x0essh_public_key\x12\xef\x01\n\x12UpdateSshPublicKey\x126.google.cloud.oslogin.v1beta.UpdateSshPublicKeyRequest\x1a).google.cloud.oslogin.common.SshPublicKey"v\xdaA\x13name,ssh_public_key\xdaA\x1fname,ssh_public_key,update_mask\x82\xd3\xe4\x93\x0282&/v1beta/{name=users/*/sshPublicKeys/*}:\x0essh_public_key\x12\xa9\x02\n\x10SignSshPublicKey\x124.google.cloud.oslogin.v1beta.SignSshPublicKeyRequest\x1a5.google.cloud.oslogin.v1beta.SignSshPublicKeyResponse"\xa7\x01\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x02\x88\x01"</v1beta/{parent=users/*/projects/*/zones/*}:signSshPublicKey:\x01*ZE"@/v1beta/{parent=users/*/projects/*/locations/*}:signSshPublicKey:\x01*\x1a\xdd\x01\xcaA\x16oslogin.googleapis.com\xd2A\xc0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonlyB\xc9\x01\n\x1fcom.google.cloud.oslogin.v1betaB\x0cOsLoginProtoP\x01Z9cloud.google.com/go/oslogin/apiv1beta/osloginpb;osloginpb\xaa\x02\x1bGoogle.Cloud.OsLogin.V1Beta\xca\x02\x1bGoogle\\Cloud\\OsLogin\\V1beta\xea\x02\x1eGoogle::Cloud::OsLogin::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oslogin.v1beta.oslogin_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.oslogin.v1betaB\x0cOsLoginProtoP\x01Z9cloud.google.com/go/oslogin/apiv1beta/osloginpb;osloginpb\xaa\x02\x1bGoogle.Cloud.OsLogin.V1Beta\xca\x02\x1bGoogle\\Cloud\\OsLogin\\V1beta\xea\x02\x1eGoogle::Cloud::OsLogin::V1beta'
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._loaded_options = None
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_options = b'8\x01'
    _globals['_LOGINPROFILE'].fields_by_name['name']._loaded_options = None
    _globals['_LOGINPROFILE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#oslogin.googleapis.com/SshPublicKey'
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_CREATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPOSIXACCOUNTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPOSIXACCOUNTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/PosixAccount'
    _globals['_DELETESSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_GETLOGINPROFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETLOGINPROFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1d\n\x1boslogin.googleapis.com/User'
    _globals['_GETSSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xfaA%\x12#oslogin.googleapis.com/SshPublicKey'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['regions']._loaded_options = None
    _globals['_IMPORTSSHPUBLICKEYREQUEST'].fields_by_name['regions']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#oslogin.googleapis.com/SshPublicKey'
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._loaded_options = None
    _globals['_UPDATESSHPUBLICKEYREQUEST'].fields_by_name['ssh_public_key']._serialized_options = b'\xe0A\x02'
    _globals['_OSLOGINSERVICE']._loaded_options = None
    _globals['_OSLOGINSERVICE']._serialized_options = b'\xcaA\x16oslogin.googleapis.com\xd2A\xc0\x01https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/compute,https://www.googleapis.com/auth/compute.readonly'
    _globals['_OSLOGINSERVICE'].methods_by_name['CreateSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['CreateSshPublicKey']._serialized_options = b'\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x028"&/v1beta/{parent=users/*}/sshPublicKeys:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeletePosixAccount']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02#*!/v1beta/{name=users/*/projects/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['DeleteSshPublicKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(*&/v1beta/{name=users/*/sshPublicKeys/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetLoginProfile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02%\x12#/v1beta/{name=users/*}/loginProfile'
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['GetSshPublicKey']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02(\x12&/v1beta/{name=users/*/sshPublicKeys/*}'
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['ImportSshPublicKey']._serialized_options = b'\xdaA\x15parent,ssh_public_key\xdaA parent,ssh_public_key,project_id\x82\xd3\xe4\x93\x02="+/v1beta/{parent=users/*}:importSshPublicKey:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['UpdateSshPublicKey']._serialized_options = b'\xdaA\x13name,ssh_public_key\xdaA\x1fname,ssh_public_key,update_mask\x82\xd3\xe4\x93\x0282&/v1beta/{name=users/*/sshPublicKeys/*}:\x0essh_public_key'
    _globals['_OSLOGINSERVICE'].methods_by_name['SignSshPublicKey']._loaded_options = None
    _globals['_OSLOGINSERVICE'].methods_by_name['SignSshPublicKey']._serialized_options = b'\xdaA\x15parent,ssh_public_key\x82\xd3\xe4\x93\x02\x88\x01"</v1beta/{parent=users/*/projects/*/zones/*}:signSshPublicKey:\x01*ZE"@/v1beta/{parent=users/*/projects/*/locations/*}:signSshPublicKey:\x01*'
    _globals['_LOGINPROFILEVIEW']._serialized_start = 2290
    _globals['_LOGINPROFILEVIEW']._serialized_end = 2373
    _globals['_LOGINPROFILE']._serialized_start = 295
    _globals['_LOGINPROFILE']._serialized_end = 644
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_start = 549
    _globals['_LOGINPROFILE_SSHPUBLICKEYSENTRY']._serialized_end = 644
    _globals['_CREATESSHPUBLICKEYREQUEST']._serialized_start = 647
    _globals['_CREATESSHPUBLICKEYREQUEST']._serialized_end = 807
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_start = 809
    _globals['_DELETEPOSIXACCOUNTREQUEST']._serialized_end = 895
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_start = 897
    _globals['_DELETESSHPUBLICKEYREQUEST']._serialized_end = 983
    _globals['_GETLOGINPROFILEREQUEST']._serialized_start = 986
    _globals['_GETLOGINPROFILEREQUEST']._serialized_end = 1161
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_start = 1163
    _globals['_GETSSHPUBLICKEYREQUEST']._serialized_end = 1246
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_start = 1249
    _globals['_IMPORTSSHPUBLICKEYREQUEST']._serialized_end = 1509
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_start = 1511
    _globals['_IMPORTSSHPUBLICKEYRESPONSE']._serialized_end = 1622
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_start = 1625
    _globals['_UPDATESSHPUBLICKEYREQUEST']._serialized_end = 1832
    _globals['_SECURITYKEY']._serialized_start = 1835
    _globals['_SECURITYKEY']._serialized_end = 2097
    _globals['_UNIVERSALTWOFACTOR']._serialized_start = 2099
    _globals['_UNIVERSALTWOFACTOR']._serialized_end = 2135
    _globals['_WEBAUTHN']._serialized_start = 2137
    _globals['_WEBAUTHN']._serialized_end = 2162
    _globals['_SIGNSSHPUBLICKEYREQUEST']._serialized_start = 2164
    _globals['_SIGNSSHPUBLICKEYREQUEST']._serialized_end = 2229
    _globals['_SIGNSSHPUBLICKEYRESPONSE']._serialized_start = 2231
    _globals['_SIGNSSHPUBLICKEYRESPONSE']._serialized_end = 2288
    _globals['_OSLOGINSERVICE']._serialized_start = 2376
    _globals['_OSLOGINSERVICE']._serialized_end = 4282