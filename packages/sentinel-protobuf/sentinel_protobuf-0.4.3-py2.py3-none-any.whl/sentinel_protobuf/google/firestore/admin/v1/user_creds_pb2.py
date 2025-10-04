"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/firestore/admin/v1/user_creds.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*google/firestore/admin/v1/user_creds.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x04\n\tUserCreds\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12>\n\x05state\x18\x04 \x01(\x0e2*.google.firestore.admin.v1.UserCreds.StateB\x03\xe0A\x03\x12\x1c\n\x0fsecure_password\x18\x05 \x01(\tB\x03\xe0A\x03\x12R\n\x11resource_identity\x18\x06 \x01(\x0b25.google.firestore.admin.v1.UserCreds.ResourceIdentityH\x00\x1a*\n\x10ResourceIdentity\x12\x16\n\tprincipal\x18\x01 \x01(\tB\x03\xe0A\x03"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07ENABLED\x10\x01\x12\x0c\n\x08DISABLED\x10\x02:}\xeaAz\n"firestore.googleapis.com/UserCreds\x12>projects/{project}/databases/{database}/userCreds/{user_creds}*\tuserCreds2\tuserCredsB\x13\n\x11UserCredsIdentityB\xdd\x01\n\x1dcom.google.firestore.admin.v1B\x0eUserCredsProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.user_creds_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\x0eUserCredsProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_USERCREDS_RESOURCEIDENTITY'].fields_by_name['principal']._loaded_options = None
    _globals['_USERCREDS_RESOURCEIDENTITY'].fields_by_name['principal']._serialized_options = b'\xe0A\x03'
    _globals['_USERCREDS'].fields_by_name['name']._loaded_options = None
    _globals['_USERCREDS'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_USERCREDS'].fields_by_name['create_time']._loaded_options = None
    _globals['_USERCREDS'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERCREDS'].fields_by_name['update_time']._loaded_options = None
    _globals['_USERCREDS'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERCREDS'].fields_by_name['state']._loaded_options = None
    _globals['_USERCREDS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_USERCREDS'].fields_by_name['secure_password']._loaded_options = None
    _globals['_USERCREDS'].fields_by_name['secure_password']._serialized_options = b'\xe0A\x03'
    _globals['_USERCREDS']._loaded_options = None
    _globals['_USERCREDS']._serialized_options = b'\xeaAz\n"firestore.googleapis.com/UserCreds\x12>projects/{project}/databases/{database}/userCreds/{user_creds}*\tuserCreds2\tuserCreds'
    _globals['_USERCREDS']._serialized_start = 167
    _globals['_USERCREDS']._serialized_end = 734
    _globals['_USERCREDS_RESOURCEIDENTITY']._serialized_start = 485
    _globals['_USERCREDS_RESOURCEIDENTITY']._serialized_end = 527
    _globals['_USERCREDS_STATE']._serialized_start = 529
    _globals['_USERCREDS_STATE']._serialized_end = 586