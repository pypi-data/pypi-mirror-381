"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/session/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n sentinel/session/v3/events.proto\x12\x13sentinel.session.v3\x1a\x14gogoproto/gogo.proto"X\n\x08EventEnd\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"\xa2\x01\n\x12EventUpdateDetails\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x16\n\x0edownload_bytes\x18\x04 \x01(\t\x12\x14\n\x0cupload_bytes\x18\x05 \x01(\t\x12\x10\n\x08duration\x18\x06 \x01(\t"q\n\x11EventUpdateStatus\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\tBIZ?github.com/sentinel-official/sentinelhub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.session.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z?github.com/sentinel-official/sentinelhub/v12/x/session/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTEND'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTEND'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTEND']._serialized_start = 79
    _globals['_EVENTEND']._serialized_end = 167
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 170
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 332
    _globals['_EVENTUPDATESTATUS']._serialized_start = 334
    _globals['_EVENTUPDATESTATUS']._serialized_end = 447