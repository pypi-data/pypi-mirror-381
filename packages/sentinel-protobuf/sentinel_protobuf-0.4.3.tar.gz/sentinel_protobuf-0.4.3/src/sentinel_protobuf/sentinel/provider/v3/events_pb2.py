"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/provider/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n!sentinel/provider/v3/events.proto\x12\x14sentinel.provider.v3\x1a\x14gogoproto/gogo.proto"i\n\x0bEventCreate\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"p\n\x12EventUpdateDetails\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"9\n\x11EventUpdateStatus\x12\x14\n\x0cprov_address\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\tBJZ@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE']._serialized_start = 81
    _globals['_EVENTCREATE']._serialized_end = 186
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 188
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 300
    _globals['_EVENTUPDATESTATUS']._serialized_start = 302
    _globals['_EVENTUPDATESTATUS']._serialized_end = 359