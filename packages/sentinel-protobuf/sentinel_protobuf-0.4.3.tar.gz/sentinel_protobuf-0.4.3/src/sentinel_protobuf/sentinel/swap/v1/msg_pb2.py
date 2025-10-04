"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/swap/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/swap/v1/msg.proto\x12\x10sentinel.swap.v1\x1a\x14gogoproto/gogo.proto"o\n\x0eMsgSwapRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x0f\n\x07tx_hash\x18\x02 \x01(\x0c\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12-\n\x06amount\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int"\x11\n\x0fMsgSwapResponse2\\\n\nMsgService\x12N\n\x07MsgSwap\x12 .sentinel.swap.v1.MsgSwapRequest\x1a!.sentinel.swap.v1.MsgSwapResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.swap.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/swap/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGSWAPREQUEST'].fields_by_name['amount']._loaded_options = None
    _globals['_MSGSWAPREQUEST'].fields_by_name['amount']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGSWAPREQUEST']._serialized_start = 70
    _globals['_MSGSWAPREQUEST']._serialized_end = 181
    _globals['_MSGSWAPRESPONSE']._serialized_start = 183
    _globals['_MSGSWAPRESPONSE']._serialized_end = 200
    _globals['_MSGSERVICE']._serialized_start = 202
    _globals['_MSGSERVICE']._serialized_end = 294