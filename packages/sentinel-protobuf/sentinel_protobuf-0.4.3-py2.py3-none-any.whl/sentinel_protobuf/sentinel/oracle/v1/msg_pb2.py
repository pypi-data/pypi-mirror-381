"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/oracle/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.oracle.v1 import params_pb2 as sentinel_dot_oracle_dot_v1_dot_params__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1csentinel/oracle/v1/msg.proto\x12\x12sentinel.oracle.v1\x1a\x14gogoproto/gogo.proto\x1a\x1fsentinel/oracle/v1/params.proto"z\n\x15MsgCreateAssetRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\t"3\n\x15MsgDeleteAssetRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t"z\n\x15MsgUpdateAssetRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\r\n\x05denom\x18\x02 \x01(\t\x12\x10\n\x08decimals\x18\x03 \x01(\x03\x12\x18\n\x10base_asset_denom\x18\x04 \x01(\t\x12\x19\n\x11quote_asset_denom\x18\x05 \x01(\t"W\n\x16MsgUpdateParamsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x120\n\x06params\x18\x02 \x01(\x0b2\x1a.sentinel.oracle.v1.ParamsB\x04\xc8\xde\x1f\x00"\x18\n\x16MsgCreateAssetResponse"\x18\n\x16MsgDeleteAssetResponse"\x18\n\x16MsgUpdateAssetResponse"\x19\n\x17MsgUpdateParamsResponse2\xb3\x03\n\nMsgService\x12g\n\x0eMsgCreateAsset\x12).sentinel.oracle.v1.MsgCreateAssetRequest\x1a*.sentinel.oracle.v1.MsgCreateAssetResponse\x12g\n\x0eMsgDeleteAsset\x12).sentinel.oracle.v1.MsgDeleteAssetRequest\x1a*.sentinel.oracle.v1.MsgDeleteAssetResponse\x12g\n\x0eMsgUpdateAsset\x12).sentinel.oracle.v1.MsgUpdateAssetRequest\x1a*.sentinel.oracle.v1.MsgUpdateAssetResponse\x12j\n\x0fMsgUpdateParams\x12*.sentinel.oracle.v1.MsgUpdateParamsRequest\x1a+.sentinel.oracle.v1.MsgUpdateParamsResponseBHZ>github.com/sentinel-official/sentinelhub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.oracle.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z>github.com/sentinel-official/sentinelhub/v12/x/oracle/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGCREATEASSETREQUEST']._serialized_start = 107
    _globals['_MSGCREATEASSETREQUEST']._serialized_end = 229
    _globals['_MSGDELETEASSETREQUEST']._serialized_start = 231
    _globals['_MSGDELETEASSETREQUEST']._serialized_end = 282
    _globals['_MSGUPDATEASSETREQUEST']._serialized_start = 284
    _globals['_MSGUPDATEASSETREQUEST']._serialized_end = 406
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 408
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 495
    _globals['_MSGCREATEASSETRESPONSE']._serialized_start = 497
    _globals['_MSGCREATEASSETRESPONSE']._serialized_end = 521
    _globals['_MSGDELETEASSETRESPONSE']._serialized_start = 523
    _globals['_MSGDELETEASSETRESPONSE']._serialized_end = 547
    _globals['_MSGUPDATEASSETRESPONSE']._serialized_start = 549
    _globals['_MSGUPDATEASSETRESPONSE']._serialized_end = 573
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 575
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 600
    _globals['_MSGSERVICE']._serialized_start = 603
    _globals['_MSGSERVICE']._serialized_end = 1038