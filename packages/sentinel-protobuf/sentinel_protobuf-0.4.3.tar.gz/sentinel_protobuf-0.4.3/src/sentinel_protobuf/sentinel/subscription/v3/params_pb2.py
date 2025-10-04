"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/subscription/v3/params.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v3/params.proto\x12\x18sentinel.subscription.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto"\x9a\x01\n\x06Params\x12\x17\n\x0fmax_allocations\x18\x01 \x01(\x03\x12:\n\rstaking_share\x18\x02 \x01(\tB#\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec\x12;\n\x0estatus_timeout\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01BNZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.params_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_PARAMS'].fields_by_name['staking_share']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['staking_share']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x1bcosmossdk.io/math.LegacyDec'
    _globals['_PARAMS'].fields_by_name['status_timeout']._loaded_options = None
    _globals['_PARAMS'].fields_by_name['status_timeout']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_PARAMS']._serialized_start = 122
    _globals['_PARAMS']._serialized_end = 276