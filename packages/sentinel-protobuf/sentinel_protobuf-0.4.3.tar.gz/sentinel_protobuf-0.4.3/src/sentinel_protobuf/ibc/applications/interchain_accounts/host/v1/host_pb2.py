"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'ibc/applications/interchain_accounts/host/v1/host.proto')
_sym_db = _symbol_database.Default()
from ......gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7ibc/applications/interchain_accounts/host/v1/host.proto\x12,ibc.applications.interchain_accounts.host.v1\x1a\x14gogoproto/gogo.proto"j\n\x06Params\x12-\n\x0chost_enabled\x18\x01 \x01(\x08B\x17\xf2\xde\x1f\x13yaml:"host_enabled"\x121\n\x0eallow_messages\x18\x02 \x03(\tB\x19\xf2\xde\x1f\x15yaml:"allow_messages""*\n\x0cQueryRequest\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x0c\n\x04data\x18\x02 \x01(\x0cBLZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.interchain_accounts.host.v1.host_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZJgithub.com/cosmos/ibc-go/v7/modules/apps/27-interchain-accounts/host/types'
    _globals['_PARAMS'].fields_by_name['host_enabled']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['host_enabled']._serialized_options = b'\xf2\xde\x1f\x13yaml:"host_enabled"'
    _globals['_PARAMS'].fields_by_name['allow_messages']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['allow_messages']._serialized_options = b'\xf2\xde\x1f\x15yaml:"allow_messages"'
    _globals['_PARAMS']._serialized_start = 127
    _globals['_PARAMS']._serialized_end = 233
    _globals['_QUERYREQUEST']._serialized_start = 235
    _globals['_QUERYREQUEST']._serialized_end = 277