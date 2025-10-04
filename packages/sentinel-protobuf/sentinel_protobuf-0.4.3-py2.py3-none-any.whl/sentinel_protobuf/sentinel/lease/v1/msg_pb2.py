"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/lease/v1/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.lease.v1 import params_pb2 as sentinel_dot_lease_dot_v1_dot_params__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsentinel/lease/v1/msg.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/lease/v1/params.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1fsentinel/types/v1/renewal.proto"5\n\x12MsgEndLeaseRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID"y\n\x14MsgRenewLeaseRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05hours\x18\x03 \x01(\x03\x121\n\tmax_price\x18\x04 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00"\xc0\x01\n\x14MsgStartLeaseRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\r\n\x05hours\x18\x03 \x01(\x03\x121\n\tmax_price\x18\x04 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12C\n\x14renewal_price_policy\x18\x05 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"}\n\x15MsgUpdateLeaseRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12C\n\x14renewal_price_policy\x18\x03 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy"V\n\x16MsgUpdateParamsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12/\n\x06params\x18\x02 \x01(\x0b2\x19.sentinel.lease.v1.ParamsB\x04\xc8\xde\x1f\x00"\x15\n\x13MsgEndLeaseResponse"\x17\n\x15MsgRenewLeaseResponse"+\n\x15MsgStartLeaseResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x18\n\x16MsgUpdateLeaseResponse"\x19\n\x17MsgUpdateParamsResponse2\x83\x04\n\nMsgService\x12\\\n\x0bMsgEndLease\x12%.sentinel.lease.v1.MsgEndLeaseRequest\x1a&.sentinel.lease.v1.MsgEndLeaseResponse\x12b\n\rMsgRenewLease\x12\'.sentinel.lease.v1.MsgRenewLeaseRequest\x1a(.sentinel.lease.v1.MsgRenewLeaseResponse\x12b\n\rMsgStartLease\x12\'.sentinel.lease.v1.MsgStartLeaseRequest\x1a(.sentinel.lease.v1.MsgStartLeaseResponse\x12e\n\x0eMsgUpdateLease\x12(.sentinel.lease.v1.MsgUpdateLeaseRequest\x1a).sentinel.lease.v1.MsgUpdateLeaseResponse\x12h\n\x0fMsgUpdateParams\x12).sentinel.lease.v1.MsgUpdateParamsRequest\x1a*.sentinel.lease.v1.MsgUpdateParamsResponseBGZ=github.com/sentinel-official/sentinelhub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/sentinel-official/sentinelhub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGENDLEASEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGENDLEASEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGRENEWLEASEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGRENEWLEASEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGRENEWLEASEREQUEST'].fields_by_name['max_price']._loaded_options = None
    _globals['_MSGRENEWLEASEREQUEST'].fields_by_name['max_price']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGSTARTLEASEREQUEST'].fields_by_name['max_price']._loaded_options = None
    _globals['_MSGSTARTLEASEREQUEST'].fields_by_name['max_price']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGUPDATELEASEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATELEASEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGSTARTLEASERESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTLEASERESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGENDLEASEREQUEST']._serialized_start = 168
    _globals['_MSGENDLEASEREQUEST']._serialized_end = 221
    _globals['_MSGRENEWLEASEREQUEST']._serialized_start = 223
    _globals['_MSGRENEWLEASEREQUEST']._serialized_end = 344
    _globals['_MSGSTARTLEASEREQUEST']._serialized_start = 347
    _globals['_MSGSTARTLEASEREQUEST']._serialized_end = 539
    _globals['_MSGUPDATELEASEREQUEST']._serialized_start = 541
    _globals['_MSGUPDATELEASEREQUEST']._serialized_end = 666
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 668
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 754
    _globals['_MSGENDLEASERESPONSE']._serialized_start = 756
    _globals['_MSGENDLEASERESPONSE']._serialized_end = 777
    _globals['_MSGRENEWLEASERESPONSE']._serialized_start = 779
    _globals['_MSGRENEWLEASERESPONSE']._serialized_end = 802
    _globals['_MSGSTARTLEASERESPONSE']._serialized_start = 804
    _globals['_MSGSTARTLEASERESPONSE']._serialized_end = 847
    _globals['_MSGUPDATELEASERESPONSE']._serialized_start = 849
    _globals['_MSGUPDATELEASERESPONSE']._serialized_end = 873
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 875
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 900
    _globals['_MSGSERVICE']._serialized_start = 903
    _globals['_MSGSERVICE']._serialized_end = 1418