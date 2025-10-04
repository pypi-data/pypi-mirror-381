"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/api/servicecontrol/v1/check_error.proto')
_sym_db = _symbol_database.Default()
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/api/servicecontrol/v1/check_error.proto\x12\x1cgoogle.api.servicecontrol.v1\x1a\x17google/rpc/status.proto"\xae\x05\n\nCheckError\x12;\n\x04code\x18\x01 \x01(\x0e2-.google.api.servicecontrol.v1.CheckError.Code\x12\x0f\n\x07subject\x18\x04 \x01(\t\x12\x0e\n\x06detail\x18\x02 \x01(\t\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status"\x9d\x04\n\x04Code\x12\x1a\n\x16ERROR_CODE_UNSPECIFIED\x10\x00\x12\r\n\tNOT_FOUND\x10\x05\x12\x15\n\x11PERMISSION_DENIED\x10\x07\x12\x16\n\x12RESOURCE_EXHAUSTED\x10\x08\x12\x19\n\x15SERVICE_NOT_ACTIVATED\x10h\x12\x14\n\x10BILLING_DISABLED\x10k\x12\x13\n\x0fPROJECT_DELETED\x10l\x12\x13\n\x0fPROJECT_INVALID\x10r\x12\x14\n\x10CONSUMER_INVALID\x10}\x12\x16\n\x12IP_ADDRESS_BLOCKED\x10m\x12\x13\n\x0fREFERER_BLOCKED\x10n\x12\x16\n\x12CLIENT_APP_BLOCKED\x10o\x12\x16\n\x12API_TARGET_BLOCKED\x10z\x12\x13\n\x0fAPI_KEY_INVALID\x10i\x12\x13\n\x0fAPI_KEY_EXPIRED\x10p\x12\x15\n\x11API_KEY_NOT_FOUND\x10q\x12\x16\n\x12INVALID_CREDENTIAL\x10{\x12!\n\x1cNAMESPACE_LOOKUP_UNAVAILABLE\x10\xac\x02\x12\x1f\n\x1aSERVICE_STATUS_UNAVAILABLE\x10\xad\x02\x12\x1f\n\x1aBILLING_STATUS_UNAVAILABLE\x10\xae\x02\x12/\n*CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE\x10\xb1\x02B\xea\x01\n com.google.api.servicecontrol.v1B\x0fCheckErrorProtoP\x01ZJcloud.google.com/go/servicecontrol/apiv1/servicecontrolpb;servicecontrolpb\xf8\x01\x01\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.api.servicecontrol.v1.check_error_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.api.servicecontrol.v1B\x0fCheckErrorProtoP\x01ZJcloud.google.com/go/servicecontrol/apiv1/servicecontrolpb;servicecontrolpb\xf8\x01\x01\xaa\x02\x1eGoogle.Cloud.ServiceControl.V1\xca\x02\x1eGoogle\\Cloud\\ServiceControl\\V1\xea\x02!Google::Cloud::ServiceControl::V1'
    _globals['_CHECKERROR']._serialized_start = 106
    _globals['_CHECKERROR']._serialized_end = 792
    _globals['_CHECKERROR_CODE']._serialized_start = 251
    _globals['_CHECKERROR_CODE']._serialized_end = 792