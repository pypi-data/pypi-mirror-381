"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/oracle/v1/asset.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/oracle/v1/asset.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto"\x9b\x01\n\x05Asset\x12\r\n\x05denom\x18\x01 \x01(\t\x12\x10\n\x08decimals\x18\x02 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x03 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x04 \x01(\t\x12,\n\x05price\x18\x05 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x12\x0e\n\x06height\x18\x06 \x01(\x03BHZ>github.com/sentinel-official/sentinelhub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.asset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/sentinel-official/sentinelhub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_ASSET'].fields_by_name['price']._loaded_options = None
    _globals['_ASSET'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_ASSET']._serialized_start = 77
    _globals['_ASSET']._serialized_end = 232