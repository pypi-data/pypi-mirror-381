"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/subscription/v2/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"sentinel/subscription/v2/msg.proto\x12\x18sentinel.subscription.v2\x1a\x14gogoproto/gogo.proto"t\n\x12MsgAllocateRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07address\x18\x03 \x01(\t\x12,\n\x05bytes\x18\x04 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int"3\n\x10MsgCancelRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x15\n\x13MsgAllocateResponse"\x13\n\x11MsgCancelResponse2\xde\x01\n\nMsgService\x12j\n\x0bMsgAllocate\x12,.sentinel.subscription.v2.MsgAllocateRequest\x1a-.sentinel.subscription.v2.MsgAllocateResponse\x12d\n\tMsgCancel\x12*.sentinel.subscription.v2.MsgCancelRequest\x1a+.sentinel.subscription.v2.MsgCancelResponseBNZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v2.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGALLOCATEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGALLOCATEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGALLOCATEREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGALLOCATEREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGCANCELREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGCANCELREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGALLOCATEREQUEST']._serialized_start = 86
    _globals['_MSGALLOCATEREQUEST']._serialized_end = 202
    _globals['_MSGCANCELREQUEST']._serialized_start = 204
    _globals['_MSGCANCELREQUEST']._serialized_end = 255
    _globals['_MSGALLOCATERESPONSE']._serialized_start = 257
    _globals['_MSGALLOCATERESPONSE']._serialized_end = 278
    _globals['_MSGCANCELRESPONSE']._serialized_start = 280
    _globals['_MSGCANCELRESPONSE']._serialized_end = 299
    _globals['_MSGSERVICE']._serialized_start = 302
    _globals['_MSGSERVICE']._serialized_end = 524