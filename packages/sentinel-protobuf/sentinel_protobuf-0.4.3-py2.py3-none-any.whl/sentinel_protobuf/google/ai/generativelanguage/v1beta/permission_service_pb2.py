"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/permission_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta import permission_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta_dot_permission__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ai/generativelanguage/v1beta/permission_service.proto\x12#google.ai.generativelanguage.v1beta\x1a4google/ai/generativelanguage/v1beta/permission.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa9\x01\n\x17CreatePermissionRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,generativelanguage.googleapis.com/Permission\x12H\n\npermission\x18\x02 \x01(\x0b2/.google.ai.generativelanguage.v1beta.PermissionB\x03\xe0A\x02"Z\n\x14GetPermissionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission"d\n\x16ListPermissionsRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\n\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"x\n\x17ListPermissionsResponse\x12D\n\x0bpermissions\x18\x01 \x03(\x0b2/.google.ai.generativelanguage.v1beta.Permission\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x99\x01\n\x17UpdatePermissionRequest\x12H\n\npermission\x18\x01 \x01(\x0b2/.google.ai.generativelanguage.v1beta.PermissionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"]\n\x17DeletePermissionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission"z\n\x18TransferOwnershipRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,generativelanguage.googleapis.com/Permission\x12\x1a\n\remail_address\x18\x02 \x01(\tB\x03\xe0A\x02"\x1b\n\x19TransferOwnershipResponse2\xec\x0b\n\x11PermissionService\x12\x8c\x02\n\x10CreatePermission\x12<.google.ai.generativelanguage.v1beta.CreatePermissionRequest\x1a/.google.ai.generativelanguage.v1beta.Permission"\x88\x01\xdaA\x11parent,permission\x82\xd3\xe4\x93\x02n"*/v1beta/{parent=tunedModels/*}/permissions:\npermissionZ4"&/v1beta/{parent=corpora/*}/permissions:\npermission\x12\xe0\x01\n\rGetPermission\x129.google.ai.generativelanguage.v1beta.GetPermissionRequest\x1a/.google.ai.generativelanguage.v1beta.Permission"c\xdaA\x04name\x82\xd3\xe4\x93\x02V\x12*/v1beta/{name=tunedModels/*/permissions/*}Z(\x12&/v1beta/{name=corpora/*/permissions/*}\x12\xf3\x01\n\x0fListPermissions\x12;.google.ai.generativelanguage.v1beta.ListPermissionsRequest\x1a<.google.ai.generativelanguage.v1beta.ListPermissionsResponse"e\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12*/v1beta/{parent=tunedModels/*}/permissionsZ(\x12&/v1beta/{parent=corpora/*}/permissions\x12\xa8\x02\n\x10UpdatePermission\x12<.google.ai.generativelanguage.v1beta.UpdatePermissionRequest\x1a/.google.ai.generativelanguage.v1beta.Permission"\xa4\x01\xdaA\x16permission,update_mask\x82\xd3\xe4\x93\x02\x84\x0125/v1beta/{permission.name=tunedModels/*/permissions/*}:\npermissionZ?21/v1beta/{permission.name=corpora/*/permissions/*}:\npermission\x12\xcd\x01\n\x10DeletePermission\x12<.google.ai.generativelanguage.v1beta.DeletePermissionRequest\x1a\x16.google.protobuf.Empty"c\xdaA\x04name\x82\xd3\xe4\x93\x02V**/v1beta/{name=tunedModels/*/permissions/*}Z(*&/v1beta/{name=corpora/*/permissions/*}\x12\xcd\x01\n\x11TransferOwnership\x12=.google.ai.generativelanguage.v1beta.TransferOwnershipRequest\x1a>.google.ai.generativelanguage.v1beta.TransferOwnershipResponse"9\x82\xd3\xe4\x93\x023"./v1beta/{name=tunedModels/*}:transferOwnership:\x01*\x1a$\xcaA!generativelanguage.googleapis.comB\xa2\x01\n\'com.google.ai.generativelanguage.v1betaB\x16PermissionServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.permission_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x16PermissionServiceProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_CREATEPERMISSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPERMISSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,generativelanguage.googleapis.com/Permission'
    _globals['_CREATEPERMISSIONREQUEST'].fields_by_name['permission']._loaded_options = None
    _globals['_CREATEPERMISSIONREQUEST'].fields_by_name['permission']._serialized_options = b'\xe0A\x02'
    _globals['_GETPERMISSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPERMISSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission'
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x03\n\x01*'
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPERMISSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPERMISSIONREQUEST'].fields_by_name['permission']._loaded_options = None
    _globals['_UPDATEPERMISSIONREQUEST'].fields_by_name['permission']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPERMISSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPERMISSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPERMISSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPERMISSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission'
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\x12,generativelanguage.googleapis.com/Permission'
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['email_address']._loaded_options = None
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['email_address']._serialized_options = b'\xe0A\x02'
    _globals['_PERMISSIONSERVICE']._loaded_options = None
    _globals['_PERMISSIONSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._serialized_options = b'\xdaA\x11parent,permission\x82\xd3\xe4\x93\x02n"*/v1beta/{parent=tunedModels/*}/permissions:\npermissionZ4"&/v1beta/{parent=corpora/*}/permissions:\npermission'
    _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02V\x12*/v1beta/{name=tunedModels/*/permissions/*}Z(\x12&/v1beta/{name=corpora/*/permissions/*}'
    _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02V\x12*/v1beta/{parent=tunedModels/*}/permissionsZ(\x12&/v1beta/{parent=corpora/*}/permissions'
    _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._serialized_options = b'\xdaA\x16permission,update_mask\x82\xd3\xe4\x93\x02\x84\x0125/v1beta/{permission.name=tunedModels/*/permissions/*}:\npermissionZ?21/v1beta/{permission.name=corpora/*/permissions/*}:\npermission'
    _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02V**/v1beta/{name=tunedModels/*/permissions/*}Z(*&/v1beta/{name=corpora/*/permissions/*}'
    _globals['_PERMISSIONSERVICE'].methods_by_name['TransferOwnership']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['TransferOwnership']._serialized_options = b'\x82\xd3\xe4\x93\x023"./v1beta/{name=tunedModels/*}:transferOwnership:\x01*'
    _globals['_CREATEPERMISSIONREQUEST']._serialized_start = 334
    _globals['_CREATEPERMISSIONREQUEST']._serialized_end = 503
    _globals['_GETPERMISSIONREQUEST']._serialized_start = 505
    _globals['_GETPERMISSIONREQUEST']._serialized_end = 595
    _globals['_LISTPERMISSIONSREQUEST']._serialized_start = 597
    _globals['_LISTPERMISSIONSREQUEST']._serialized_end = 697
    _globals['_LISTPERMISSIONSRESPONSE']._serialized_start = 699
    _globals['_LISTPERMISSIONSRESPONSE']._serialized_end = 819
    _globals['_UPDATEPERMISSIONREQUEST']._serialized_start = 822
    _globals['_UPDATEPERMISSIONREQUEST']._serialized_end = 975
    _globals['_DELETEPERMISSIONREQUEST']._serialized_start = 977
    _globals['_DELETEPERMISSIONREQUEST']._serialized_end = 1070
    _globals['_TRANSFEROWNERSHIPREQUEST']._serialized_start = 1072
    _globals['_TRANSFEROWNERSHIPREQUEST']._serialized_end = 1194
    _globals['_TRANSFEROWNERSHIPRESPONSE']._serialized_start = 1196
    _globals['_TRANSFEROWNERSHIPRESPONSE']._serialized_end = 1223
    _globals['_PERMISSIONSERVICE']._serialized_start = 1226
    _globals['_PERMISSIONSERVICE']._serialized_end = 2742