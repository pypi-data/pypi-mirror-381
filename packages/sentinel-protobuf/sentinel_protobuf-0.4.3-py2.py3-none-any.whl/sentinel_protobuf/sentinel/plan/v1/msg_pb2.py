"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/plan/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/plan/v1/msg.proto\x12\x10sentinel.plan.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1esentinel/types/v1/status.proto"\xee\x01\n\rMsgAddRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12Z\n\x05price\x18\x02 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x125\n\x08validity\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12=\n\x05bytes\x18\x04 \x01(\tB.\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int"=\n\x11MsgAddNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0f\n\x07address\x18\x03 \x01(\t"@\n\x14MsgRemoveNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12\x0f\n\x07address\x18\x03 \x01(\t"Y\n\x13MsgSetStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x04\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.Status"\x10\n\x0eMsgAddResponse"\x14\n\x12MsgAddNodeResponse"\x17\n\x15MsgRemoveNodeResponse"\x16\n\x14MsgSetStatusResponse2\xf3\x02\n\nMsgService\x12K\n\x06MsgAdd\x12\x1f.sentinel.plan.v1.MsgAddRequest\x1a .sentinel.plan.v1.MsgAddResponse\x12W\n\nMsgAddNode\x12#.sentinel.plan.v1.MsgAddNodeRequest\x1a$.sentinel.plan.v1.MsgAddNodeResponse\x12`\n\rMsgRemoveNode\x12&.sentinel.plan.v1.MsgRemoveNodeRequest\x1a\'.sentinel.plan.v1.MsgRemoveNodeResponse\x12]\n\x0cMsgSetStatus\x12%.sentinel.plan.v1.MsgSetStatusRequest\x1a&.sentinel.plan.v1.MsgSetStatusResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGADDREQUEST'].fields_by_name['price']._loaded_options = None
    _globals['_MSGADDREQUEST'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGADDREQUEST'].fields_by_name['validity']._loaded_options = None
    _globals['_MSGADDREQUEST'].fields_by_name['validity']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_MSGADDREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGADDREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f&github.com/cosmos/cosmos-sdk/types.Int'
    _globals['_MSGADDREQUEST']._serialized_start = 167
    _globals['_MSGADDREQUEST']._serialized_end = 405
    _globals['_MSGADDNODEREQUEST']._serialized_start = 407
    _globals['_MSGADDNODEREQUEST']._serialized_end = 468
    _globals['_MSGREMOVENODEREQUEST']._serialized_start = 470
    _globals['_MSGREMOVENODEREQUEST']._serialized_end = 534
    _globals['_MSGSETSTATUSREQUEST']._serialized_start = 536
    _globals['_MSGSETSTATUSREQUEST']._serialized_end = 625
    _globals['_MSGADDRESPONSE']._serialized_start = 627
    _globals['_MSGADDRESPONSE']._serialized_end = 643
    _globals['_MSGADDNODERESPONSE']._serialized_start = 645
    _globals['_MSGADDNODERESPONSE']._serialized_end = 665
    _globals['_MSGREMOVENODERESPONSE']._serialized_start = 667
    _globals['_MSGREMOVENODERESPONSE']._serialized_end = 690
    _globals['_MSGSETSTATUSRESPONSE']._serialized_start = 692
    _globals['_MSGSETSTATUSRESPONSE']._serialized_end = 714
    _globals['_MSGSERVICE']._serialized_start = 717
    _globals['_MSGSERVICE']._serialized_end = 1088