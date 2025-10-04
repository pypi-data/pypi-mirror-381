"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/deposit/v2/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/deposit/v2/events.proto\x12\x13sentinel.deposit.v2\x1a\x14gogoproto/gogo.proto".\n\x08EventAdd\x12\x13\n\x0bacc_address\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t"3\n\rEventSubtract\x12\x13\n\x0bacc_address\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\tBIZ?github.com/sentinel-official/sentinelhub/v12/x/deposit/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.deposit.v2.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/sentinel-official/sentinelhub/v12/x/deposit/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTADD']._serialized_start = 79
    _globals['_EVENTADD']._serialized_end = 125
    _globals['_EVENTSUBTRACT']._serialized_start = 127
    _globals['_EVENTSUBTRACT']._serialized_end = 178