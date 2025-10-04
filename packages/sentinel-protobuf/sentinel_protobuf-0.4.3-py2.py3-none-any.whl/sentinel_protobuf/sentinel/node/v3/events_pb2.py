"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/node/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/node/v3/events.proto\x12\x10sentinel.node.v3\x1a\x14gogoproto/gogo.proto"i\n\x0bEventCreate\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12\x17\n\x0fgigabyte_prices\x18\x02 \x01(\t\x12\x15\n\rhourly_prices\x18\x03 \x01(\t\x12\x14\n\x0cremote_addrs\x18\x04 \x03(\t"\x81\x01\n\x08EventPay\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\x0f\n\x07payment\x18\x04 \x01(\t\x12\x16\n\x0estaking_reward\x18\x05 \x01(\t"T\n\x0bEventRefund\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"p\n\x12EventUpdateDetails\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12\x17\n\x0fgigabyte_prices\x18\x02 \x01(\t\x12\x15\n\rhourly_prices\x18\x03 \x01(\t\x12\x14\n\x0cremote_addrs\x18\x04 \x03(\t"9\n\x11EventUpdateStatus\x12\x14\n\x0cnode_address\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t"\x9a\x01\n\x12EventCreateSession\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t\x12\x11\n\tmax_bytes\x18\x05 \x01(\t\x12\x14\n\x0cmax_duration\x18\x06 \x01(\tBFZ<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTPAY'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTREFUND'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTCREATESESSION'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTCREATESESSION'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTCREATE']._serialized_start = 73
    _globals['_EVENTCREATE']._serialized_end = 178
    _globals['_EVENTPAY']._serialized_start = 181
    _globals['_EVENTPAY']._serialized_end = 310
    _globals['_EVENTREFUND']._serialized_start = 312
    _globals['_EVENTREFUND']._serialized_end = 396
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 398
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 510
    _globals['_EVENTUPDATESTATUS']._serialized_start = 512
    _globals['_EVENTUPDATESTATUS']._serialized_end = 569
    _globals['_EVENTCREATESESSION']._serialized_start = 572
    _globals['_EVENTCREATESESSION']._serialized_end = 726