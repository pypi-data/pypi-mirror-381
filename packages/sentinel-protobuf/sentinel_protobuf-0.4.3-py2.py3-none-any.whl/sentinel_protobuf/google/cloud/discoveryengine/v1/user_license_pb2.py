"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/user_license.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/discoveryengine/v1/user_license.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbb\x04\n\x0bUserLicense\x12\x1e\n\x0euser_principal\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x02\x12\x19\n\x0cuser_profile\x18\x03 \x01(\tB\x03\xe0A\x01\x12j\n\x18license_assignment_state\x18\x04 \x01(\x0e2C.google.cloud.discoveryengine.v1.UserLicense.LicenseAssignmentStateB\x03\xe0A\x03\x12L\n\x0elicense_config\x18\x05 \x01(\tB4\xe0A\x01\xfaA.\n,discoveryengine.googleapis.com/LicenseConfig\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x0flast_login_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x90\x01\n\x16LicenseAssignmentState\x12(\n$LICENSE_ASSIGNMENT_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08ASSIGNED\x10\x01\x12\x0e\n\nUNASSIGNED\x10\x02\x12\x0e\n\nNO_LICENSE\x10\x03\x12\x1e\n\x1aNO_LICENSE_ATTEMPTED_LOGIN\x10\x04B\x83\x02\n#com.google.cloud.discoveryengine.v1B\x10UserLicenseProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.user_license_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x10UserLicenseProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_USERLICENSE'].fields_by_name['user_principal']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['user_principal']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_USERLICENSE'].fields_by_name['user_profile']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['user_profile']._serialized_options = b'\xe0A\x01'
    _globals['_USERLICENSE'].fields_by_name['license_assignment_state']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['license_assignment_state']._serialized_options = b'\xe0A\x03'
    _globals['_USERLICENSE'].fields_by_name['license_config']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['license_config']._serialized_options = b'\xe0A\x01\xfaA.\n,discoveryengine.googleapis.com/LicenseConfig'
    _globals['_USERLICENSE'].fields_by_name['create_time']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERLICENSE'].fields_by_name['update_time']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERLICENSE'].fields_by_name['last_login_time']._loaded_options = None
    _globals['_USERLICENSE'].fields_by_name['last_login_time']._serialized_options = b'\xe0A\x03'
    _globals['_USERLICENSE']._serialized_start = 181
    _globals['_USERLICENSE']._serialized_end = 752
    _globals['_USERLICENSE_LICENSEASSIGNMENTSTATE']._serialized_start = 608
    _globals['_USERLICENSE_LICENSEASSIGNMENTSTATE']._serialized_end = 752