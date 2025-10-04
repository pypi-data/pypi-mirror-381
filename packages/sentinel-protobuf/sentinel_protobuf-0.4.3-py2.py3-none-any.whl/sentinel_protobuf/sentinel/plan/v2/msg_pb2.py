"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/plan/v2/msg.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/plan/v2/msg.proto\x12\x10sentinel.plan.v2\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1esentinel/types/v1/status.proto"\xc6\x01\n\x10MsgCreateRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x125\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12\x11\n\tgigabytes\x18\x03 \x01(\x03\x12[\n\x06prices\x18\x04 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins"K\n\x12MsgLinkNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"M\n\x14MsgUnlinkNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"d\n\x16MsgUpdateStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.Status"E\n\x13MsgSubscribeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05denom\x18\x03 \x01(\t"\x13\n\x11MsgCreateResponse"\x15\n\x13MsgLinkNodeResponse"\x17\n\x15MsgUnlinkNodeResponse"\x19\n\x17MsgUpdateStatusResponse"\x16\n\x14MsgSubscribeResponse2\xe7\x03\n\nMsgService\x12T\n\tMsgCreate\x12".sentinel.plan.v2.MsgCreateRequest\x1a#.sentinel.plan.v2.MsgCreateResponse\x12Z\n\x0bMsgLinkNode\x12$.sentinel.plan.v2.MsgLinkNodeRequest\x1a%.sentinel.plan.v2.MsgLinkNodeResponse\x12`\n\rMsgUnlinkNode\x12&.sentinel.plan.v2.MsgUnlinkNodeRequest\x1a\'.sentinel.plan.v2.MsgUnlinkNodeResponse\x12f\n\x0fMsgUpdateStatus\x12(.sentinel.plan.v2.MsgUpdateStatusRequest\x1a).sentinel.plan.v2.MsgUpdateStatusResponse\x12]\n\x0cMsgSubscribe\x12%.sentinel.plan.v2.MsgSubscribeRequest\x1a&.sentinel.plan.v2.MsgSubscribeResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v2.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGCREATEREQUEST'].fields_by_name['duration']._loaded_options = None
    _globals['_MSGCREATEREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_MSGCREATEREQUEST'].fields_by_name['prices']._loaded_options = None
    _globals['_MSGCREATEREQUEST'].fields_by_name['prices']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGLINKNODEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGLINKNODEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUNLINKNODEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUNLINKNODEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATESTATUSREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATESTATUSREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSUBSCRIBEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSUBSCRIBEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGCREATEREQUEST']._serialized_start = 167
    _globals['_MSGCREATEREQUEST']._serialized_end = 365
    _globals['_MSGLINKNODEREQUEST']._serialized_start = 367
    _globals['_MSGLINKNODEREQUEST']._serialized_end = 442
    _globals['_MSGUNLINKNODEREQUEST']._serialized_start = 444
    _globals['_MSGUNLINKNODEREQUEST']._serialized_end = 521
    _globals['_MSGUPDATESTATUSREQUEST']._serialized_start = 523
    _globals['_MSGUPDATESTATUSREQUEST']._serialized_end = 623
    _globals['_MSGSUBSCRIBEREQUEST']._serialized_start = 625
    _globals['_MSGSUBSCRIBEREQUEST']._serialized_end = 694
    _globals['_MSGCREATERESPONSE']._serialized_start = 696
    _globals['_MSGCREATERESPONSE']._serialized_end = 715
    _globals['_MSGLINKNODERESPONSE']._serialized_start = 717
    _globals['_MSGLINKNODERESPONSE']._serialized_end = 738
    _globals['_MSGUNLINKNODERESPONSE']._serialized_start = 740
    _globals['_MSGUNLINKNODERESPONSE']._serialized_end = 763
    _globals['_MSGUPDATESTATUSRESPONSE']._serialized_start = 765
    _globals['_MSGUPDATESTATUSRESPONSE']._serialized_end = 790
    _globals['_MSGSUBSCRIBERESPONSE']._serialized_start = 792
    _globals['_MSGSUBSCRIBERESPONSE']._serialized_end = 814
    _globals['_MSGSERVICE']._serialized_start = 817
    _globals['_MSGSERVICE']._serialized_end = 1304