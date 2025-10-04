"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta3/permission_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ai.generativelanguage.v1beta3 import permission_pb2 as google_dot_ai_dot_generativelanguage_dot_v1beta3_dot_permission__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ai/generativelanguage/v1beta3/permission_service.proto\x12$google.ai.generativelanguage.v1beta3\x1a5google/ai/generativelanguage/v1beta3/permission.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xaa\x01\n\x17CreatePermissionRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,generativelanguage.googleapis.com/Permission\x12I\n\npermission\x18\x02 \x01(\x0b20.google.ai.generativelanguage.v1beta3.PermissionB\x03\xe0A\x02"Z\n\x14GetPermissionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission"d\n\x16ListPermissionsRequest\x12\x19\n\x06parent\x18\x01 \x01(\tB\t\xe0A\x02\xfaA\x03\n\x01*\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"y\n\x17ListPermissionsResponse\x12E\n\x0bpermissions\x18\x01 \x03(\x0b20.google.ai.generativelanguage.v1beta3.Permission\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9a\x01\n\x17UpdatePermissionRequest\x12I\n\npermission\x18\x01 \x01(\x0b20.google.ai.generativelanguage.v1beta3.PermissionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"]\n\x17DeletePermissionRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/Permission"z\n\x18TransferOwnershipRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel\x12\x1a\n\remail_address\x18\x02 \x01(\tB\x03\xe0A\x02"\x1b\n\x19TransferOwnershipResponse2\x85\n\n\x11PermissionService\x12\xd8\x01\n\x10CreatePermission\x12=.google.ai.generativelanguage.v1beta3.CreatePermissionRequest\x1a0.google.ai.generativelanguage.v1beta3.Permission"S\xdaA\x11parent,permission\x82\xd3\xe4\x93\x029"+/v1beta3/{parent=tunedModels/*}/permissions:\npermission\x12\xb9\x01\n\rGetPermission\x12:.google.ai.generativelanguage.v1beta3.GetPermissionRequest\x1a0.google.ai.generativelanguage.v1beta3.Permission":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1beta3/{name=tunedModels/*/permissions/*}\x12\xcc\x01\n\x0fListPermissions\x12<.google.ai.generativelanguage.v1beta3.ListPermissionsRequest\x1a=.google.ai.generativelanguage.v1beta3.ListPermissionsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1beta3/{parent=tunedModels/*}/permissions\x12\xe8\x01\n\x10UpdatePermission\x12=.google.ai.generativelanguage.v1beta3.UpdatePermissionRequest\x1a0.google.ai.generativelanguage.v1beta3.Permission"c\xdaA\x16permission,update_mask\x82\xd3\xe4\x93\x02D26/v1beta3/{permission.name=tunedModels/*/permissions/*}:\npermission\x12\xa5\x01\n\x10DeletePermission\x12=.google.ai.generativelanguage.v1beta3.DeletePermissionRequest\x1a\x16.google.protobuf.Empty":\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1beta3/{name=tunedModels/*/permissions/*}\x12\xd0\x01\n\x11TransferOwnership\x12>.google.ai.generativelanguage.v1beta3.TransferOwnershipRequest\x1a?.google.ai.generativelanguage.v1beta3.TransferOwnershipResponse":\x82\xd3\xe4\x93\x024"//v1beta3/{name=tunedModels/*}:transferOwnership:\x01*\x1a$\xcaA!generativelanguage.googleapis.comB\xa4\x01\n(com.google.ai.generativelanguage.v1beta3B\x16PermissionServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta3/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta3.permission_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ai.generativelanguage.v1beta3B\x16PermissionServiceProtoP\x01Z^cloud.google.com/go/ai/generativelanguage/apiv1beta3/generativelanguagepb;generativelanguagepb'
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
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,generativelanguage.googleapis.com/TunedModel'
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['email_address']._loaded_options = None
    _globals['_TRANSFEROWNERSHIPREQUEST'].fields_by_name['email_address']._serialized_options = b'\xe0A\x02'
    _globals['_PERMISSIONSERVICE']._loaded_options = None
    _globals['_PERMISSIONSERVICE']._serialized_options = b'\xcaA!generativelanguage.googleapis.com'
    _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['CreatePermission']._serialized_options = b'\xdaA\x11parent,permission\x82\xd3\xe4\x93\x029"+/v1beta3/{parent=tunedModels/*}/permissions:\npermission'
    _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['GetPermission']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/v1beta3/{name=tunedModels/*/permissions/*}'
    _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['ListPermissions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1beta3/{parent=tunedModels/*}/permissions'
    _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['UpdatePermission']._serialized_options = b'\xdaA\x16permission,update_mask\x82\xd3\xe4\x93\x02D26/v1beta3/{permission.name=tunedModels/*/permissions/*}:\npermission'
    _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['DeletePermission']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-*+/v1beta3/{name=tunedModels/*/permissions/*}'
    _globals['_PERMISSIONSERVICE'].methods_by_name['TransferOwnership']._loaded_options = None
    _globals['_PERMISSIONSERVICE'].methods_by_name['TransferOwnership']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v1beta3/{name=tunedModels/*}:transferOwnership:\x01*'
    _globals['_CREATEPERMISSIONREQUEST']._serialized_start = 337
    _globals['_CREATEPERMISSIONREQUEST']._serialized_end = 507
    _globals['_GETPERMISSIONREQUEST']._serialized_start = 509
    _globals['_GETPERMISSIONREQUEST']._serialized_end = 599
    _globals['_LISTPERMISSIONSREQUEST']._serialized_start = 601
    _globals['_LISTPERMISSIONSREQUEST']._serialized_end = 701
    _globals['_LISTPERMISSIONSRESPONSE']._serialized_start = 703
    _globals['_LISTPERMISSIONSRESPONSE']._serialized_end = 824
    _globals['_UPDATEPERMISSIONREQUEST']._serialized_start = 827
    _globals['_UPDATEPERMISSIONREQUEST']._serialized_end = 981
    _globals['_DELETEPERMISSIONREQUEST']._serialized_start = 983
    _globals['_DELETEPERMISSIONREQUEST']._serialized_end = 1076
    _globals['_TRANSFEROWNERSHIPREQUEST']._serialized_start = 1078
    _globals['_TRANSFEROWNERSHIPREQUEST']._serialized_end = 1200
    _globals['_TRANSFEROWNERSHIPRESPONSE']._serialized_start = 1202
    _globals['_TRANSFEROWNERSHIPRESPONSE']._serialized_end = 1229
    _globals['_PERMISSIONSERVICE']._serialized_start = 1232
    _globals['_PERMISSIONSERVICE']._serialized_end = 2517