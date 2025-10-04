"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/node/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....cosmos.base.v1beta1 import coin_pb2 as cosmos_dot_base_dot_v1beta1_dot_coin__pb2
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/node/v1/msg.proto\x12\x10sentinel.node.v1\x1a\x1ecosmos/base/v1beta1/coin.proto\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\xb2\x01\n\x12MsgRegisterRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12Z\n\x05price\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"M\n\x13MsgSetStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"\xb0\x01\n\x10MsgUpdateRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x10\n\x08provider\x18\x02 \x01(\t\x12Z\n\x05price\x18\x03 \x03(\x0b2\x19.cosmos.base.v1beta1.CoinB0\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins\x12!\n\nremote_url\x18\x04 \x01(\tB\r\xe2\xde\x1f\tRemoteURL"\x15\n\x13MsgRegisterResponse"\x16\n\x14MsgSetStatusResponse"\x13\n\x11MsgUpdateResponse2\x9d\x02\n\nMsgService\x12Z\n\x0bMsgRegister\x12$.sentinel.node.v1.MsgRegisterRequest\x1a%.sentinel.node.v1.MsgRegisterResponse\x12]\n\x0cMsgSetStatus\x12%.sentinel.node.v1.MsgSetStatusRequest\x1a&.sentinel.node.v1.MsgSetStatusResponse\x12T\n\tMsgUpdate\x12".sentinel.node.v1.MsgUpdateRequest\x1a#.sentinel.node.v1.MsgUpdateResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/node/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/node/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGREGISTERREQUEST'].fields_by_name['price']._loaded_options = None
    _globals['_MSGREGISTERREQUEST'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGREGISTERREQUEST'].fields_by_name['remote_url']._loaded_options = None
    _globals['_MSGREGISTERREQUEST'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_MSGUPDATEREQUEST'].fields_by_name['price']._loaded_options = None
    _globals['_MSGUPDATEREQUEST'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00\xaa\xdf\x1f(github.com/cosmos/cosmos-sdk/types.Coins'
    _globals['_MSGUPDATEREQUEST'].fields_by_name['remote_url']._loaded_options = None
    _globals['_MSGUPDATEREQUEST'].fields_by_name['remote_url']._serialized_options = b'\xe2\xde\x1f\tRemoteURL'
    _globals['_MSGREGISTERREQUEST']._serialized_start = 135
    _globals['_MSGREGISTERREQUEST']._serialized_end = 313
    _globals['_MSGSETSTATUSREQUEST']._serialized_start = 315
    _globals['_MSGSETSTATUSREQUEST']._serialized_end = 392
    _globals['_MSGUPDATEREQUEST']._serialized_start = 395
    _globals['_MSGUPDATEREQUEST']._serialized_end = 571
    _globals['_MSGREGISTERRESPONSE']._serialized_start = 573
    _globals['_MSGREGISTERRESPONSE']._serialized_end = 594
    _globals['_MSGSETSTATUSRESPONSE']._serialized_start = 596
    _globals['_MSGSETSTATUSRESPONSE']._serialized_end = 618
    _globals['_MSGUPDATERESPONSE']._serialized_start = 620
    _globals['_MSGUPDATERESPONSE']._serialized_end = 639
    _globals['_MSGSERVICE']._serialized_start = 642
    _globals['_MSGSERVICE']._serialized_end = 927