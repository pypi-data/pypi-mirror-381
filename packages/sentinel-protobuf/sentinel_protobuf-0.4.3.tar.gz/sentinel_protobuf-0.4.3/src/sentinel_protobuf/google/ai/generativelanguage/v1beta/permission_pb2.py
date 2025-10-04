"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/permission.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ai/generativelanguage/v1beta/permission.proto\x12#google.ai.generativelanguage.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xde\x04\n\nPermission\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12^\n\x0cgrantee_type\x18\x02 \x01(\x0e2;.google.ai.generativelanguage.v1beta.Permission.GranteeTypeB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12"\n\remail_address\x18\x03 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12L\n\x04role\x18\x04 \x01(\x0e24.google.ai.generativelanguage.v1beta.Permission.RoleB\x03\xe0A\x02H\x02\x88\x01\x01"N\n\x0bGranteeType\x12\x1c\n\x18GRANTEE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04USER\x10\x01\x12\t\n\x05GROUP\x10\x02\x12\x0c\n\x08EVERYONE\x10\x03"?\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\t\n\x05OWNER\x10\x01\x12\n\n\x06WRITER\x10\x02\x12\n\n\x06READER\x10\x03:\xaa\x01\xeaA\xa6\x01\n,generativelanguage.googleapis.com/Permission\x122tunedModels/{tuned_model}/permissions/{permission}\x12)corpora/{corpus}/permissions/{permission}*\x0bpermissions2\npermissionB\x0f\n\r_grantee_typeB\x10\n\x0e_email_addressB\x07\n\x05_roleB\x9b\x01\n\'com.google.ai.generativelanguage.v1betaB\x0fPermissionProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.permission_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x0fPermissionProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_PERMISSION'].fields_by_name['name']._loaded_options = None
    _globals['_PERMISSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_PERMISSION'].fields_by_name['grantee_type']._loaded_options = None
    _globals['_PERMISSION'].fields_by_name['grantee_type']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PERMISSION'].fields_by_name['email_address']._loaded_options = None
    _globals['_PERMISSION'].fields_by_name['email_address']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_PERMISSION'].fields_by_name['role']._loaded_options = None
    _globals['_PERMISSION'].fields_by_name['role']._serialized_options = b'\xe0A\x02'
    _globals['_PERMISSION']._loaded_options = None
    _globals['_PERMISSION']._serialized_options = b'\xeaA\xa6\x01\n,generativelanguage.googleapis.com/Permission\x122tunedModels/{tuned_model}/permissions/{permission}\x12)corpora/{corpus}/permissions/{permission}*\x0bpermissions2\npermission'
    _globals['_PERMISSION']._serialized_start = 154
    _globals['_PERMISSION']._serialized_end = 760
    _globals['_PERMISSION_GRANTEETYPE']._serialized_start = 400
    _globals['_PERMISSION_GRANTEETYPE']._serialized_end = 478
    _globals['_PERMISSION_ROLE']._serialized_start = 480
    _globals['_PERMISSION_ROLE']._serialized_end = 543