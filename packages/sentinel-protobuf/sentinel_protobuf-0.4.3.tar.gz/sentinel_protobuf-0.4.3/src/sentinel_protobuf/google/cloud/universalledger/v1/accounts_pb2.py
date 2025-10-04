"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/accounts.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/universalledger/v1/accounts.proto\x12\x1fgoogle.cloud.universalledger.v1*g\n\rAccountStatus\x12\x1e\n\x1aACCOUNT_STATUS_UNSPECIFIED\x10\x00\x12\x19\n\x15ACCOUNT_STATUS_ACTIVE\x10\x01\x12\x1b\n\x17ACCOUNT_STATUS_INACTIVE\x10\x02*y\n\x04Role\x12\x14\n\x10ROLE_UNSPECIFIED\x10\x00\x12\x0e\n\nROLE_PAYER\x10\x05\x12\x11\n\rROLE_RECEIVER\x10\x06\x12\x19\n\x15ROLE_CONTRACT_CREATOR\x10\x07\x12\x1d\n\x19ROLE_CONTRACT_PARTICIPANT\x10\x08*Z\n\x12ContractPermission\x12#\n\x1fCONTRACT_PERMISSION_UNSPECIFIED\x10\x00\x12\x1f\n\x1bCONTRACT_PERMISSION_STORAGE\x10\x01B\xee\x01\n#com.google.cloud.universalledger.v1B\rAccountsProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.accounts_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\rAccountsProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_ACCOUNTSTATUS']._serialized_start = 83
    _globals['_ACCOUNTSTATUS']._serialized_end = 186
    _globals['_ROLE']._serialized_start = 188
    _globals['_ROLE']._serialized_end = 309
    _globals['_CONTRACTPERMISSION']._serialized_start = 311
    _globals['_CONTRACTPERMISSION']._serialized_end = 401