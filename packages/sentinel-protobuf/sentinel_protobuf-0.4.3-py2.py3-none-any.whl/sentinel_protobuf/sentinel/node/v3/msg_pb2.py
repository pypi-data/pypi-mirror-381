"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/node/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.node.v3 import params_pb2 as sentinel_dot_node_dot_v3_dot_params__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/node/v3/msg.proto\x12\x10sentinel.node.v3\x1a\x14gogoproto/gogo.proto\x1a\x1dsentinel/node/v3/params.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1esentinel/types/v1/status.proto"\xab\x01\n\x16MsgRegisterNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x127\n\x0fgigabyte_prices\x18\x02 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x125\n\rhourly_prices\x18\x03 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cremote_addrs\x18\x04 \x03(\t"\xb0\x01\n\x1bMsgUpdateNodeDetailsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x127\n\x0fgigabyte_prices\x18\x02 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x125\n\rhourly_prices\x18\x03 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\x14\n\x0cremote_addrs\x18\x04 \x03(\t"T\n\x1aMsgUpdateNodeStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"\x90\x01\n\x16MsgStartSessionRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x11\n\tgigabytes\x18\x03 \x01(\x03\x12\r\n\x05hours\x18\x04 \x01(\x03\x121\n\tmax_price\x18\x05 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00"U\n\x16MsgUpdateParamsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12.\n\x06params\x18\x02 \x01(\x0b2\x18.sentinel.node.v3.ParamsB\x04\xc8\xde\x1f\x00"\x19\n\x17MsgRegisterNodeResponse"\x1e\n\x1cMsgUpdateNodeDetailsResponse"\x1d\n\x1bMsgUpdateNodeStatusResponse"-\n\x17MsgStartSessionResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x19\n\x17MsgUpdateParamsResponse2\xaf\x04\n\nMsgService\x12f\n\x0fMsgRegisterNode\x12(.sentinel.node.v3.MsgRegisterNodeRequest\x1a).sentinel.node.v3.MsgRegisterNodeResponse\x12u\n\x14MsgUpdateNodeDetails\x12-.sentinel.node.v3.MsgUpdateNodeDetailsRequest\x1a..sentinel.node.v3.MsgUpdateNodeDetailsResponse\x12r\n\x13MsgUpdateNodeStatus\x12,.sentinel.node.v3.MsgUpdateNodeStatusRequest\x1a-.sentinel.node.v3.MsgUpdateNodeStatusResponse\x12f\n\x0fMsgStartSession\x12(.sentinel.node.v3.MsgStartSessionRequest\x1a).sentinel.node.v3.MsgStartSessionResponse\x12f\n\x0fMsgUpdateParams\x12(.sentinel.node.v3.MsgUpdateParamsRequest\x1a).sentinel.node.v3.MsgUpdateParamsResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGREGISTERNODEREQUEST'].fields_by_name['gigabyte_prices']._loaded_options = None
    _globals['_MSGREGISTERNODEREQUEST'].fields_by_name['gigabyte_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGREGISTERNODEREQUEST'].fields_by_name['hourly_prices']._loaded_options = None
    _globals['_MSGREGISTERNODEREQUEST'].fields_by_name['hourly_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUPDATENODEDETAILSREQUEST'].fields_by_name['gigabyte_prices']._loaded_options = None
    _globals['_MSGUPDATENODEDETAILSREQUEST'].fields_by_name['gigabyte_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUPDATENODEDETAILSREQUEST'].fields_by_name['hourly_prices']._loaded_options = None
    _globals['_MSGUPDATENODEDETAILSREQUEST'].fields_by_name['hourly_prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['max_price']._loaded_options = None
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['max_price']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGREGISTERNODEREQUEST']._serialized_start = 165
    _globals['_MSGREGISTERNODEREQUEST']._serialized_end = 336
    _globals['_MSGUPDATENODEDETAILSREQUEST']._serialized_start = 339
    _globals['_MSGUPDATENODEDETAILSREQUEST']._serialized_end = 515
    _globals['_MSGUPDATENODESTATUSREQUEST']._serialized_start = 517
    _globals['_MSGUPDATENODESTATUSREQUEST']._serialized_end = 601
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_start = 604
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_end = 748
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 750
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 835
    _globals['_MSGREGISTERNODERESPONSE']._serialized_start = 837
    _globals['_MSGREGISTERNODERESPONSE']._serialized_end = 862
    _globals['_MSGUPDATENODEDETAILSRESPONSE']._serialized_start = 864
    _globals['_MSGUPDATENODEDETAILSRESPONSE']._serialized_end = 894
    _globals['_MSGUPDATENODESTATUSRESPONSE']._serialized_start = 896
    _globals['_MSGUPDATENODESTATUSRESPONSE']._serialized_end = 925
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_start = 927
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_end = 972
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 974
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 999
    _globals['_MSGSERVICE']._serialized_start = 1002
    _globals['_MSGSERVICE']._serialized_end = 1561