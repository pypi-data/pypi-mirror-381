"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/provider/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/provider/v1/msg.proto\x12\x14sentinel.provider.v1\x1a\x14gogoproto/gogo.proto"g\n\x12MsgRegisterRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"e\n\x10MsgUpdateRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"\x15\n\x13MsgRegisterResponse"\x13\n\x11MsgUpdateResponse2\xce\x01\n\nMsgService\x12b\n\x0bMsgRegister\x12(.sentinel.provider.v1.MsgRegisterRequest\x1a).sentinel.provider.v1.MsgRegisterResponse\x12\\\n\tMsgUpdate\x12&.sentinel.provider.v1.MsgUpdateRequest\x1a\'.sentinel.provider.v1.MsgUpdateResponseBJZ@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGREGISTERREQUEST']._serialized_start = 78
    _globals['_MSGREGISTERREQUEST']._serialized_end = 181
    _globals['_MSGUPDATEREQUEST']._serialized_start = 183
    _globals['_MSGUPDATEREQUEST']._serialized_end = 284
    _globals['_MSGREGISTERRESPONSE']._serialized_start = 286
    _globals['_MSGREGISTERRESPONSE']._serialized_end = 307
    _globals['_MSGUPDATERESPONSE']._serialized_start = 309
    _globals['_MSGUPDATERESPONSE']._serialized_end = 328
    _globals['_MSGSERVICE']._serialized_start = 331
    _globals['_MSGSERVICE']._serialized_end = 537