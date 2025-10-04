"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/plan/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1asentinel/plan/v3/msg.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1fsentinel/types/v1/renewal.proto\x1a\x1esentinel/types/v1/status.proto"\xc9\x01\n\x14MsgCreatePlanRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12,\n\x05bytes\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x125\n\x08duration\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x08\xc8\xde\x1f\x00\x98\xdf\x1f\x01\x12.\n\x06prices\x18\x04 \x03(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12\x0f\n\x07private\x18\x05 \x01(\x08"K\n\x12MsgLinkNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"M\n\x14MsgUnlinkNodeRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"O\n\x1bMsgUpdatePlanDetailsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x0f\n\x07private\x18\x03 \x01(\x08"h\n\x1aMsgUpdatePlanStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12)\n\x06status\x18\x03 \x01(\x0e2\x19.sentinel.types.v1.Status"\xa3\x01\n\x16MsgStartSessionRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x12\n\x02id\x18\x02 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\r\n\x05denom\x18\x03 \x01(\t\x12C\n\x14renewal_price_policy\x18\x04 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy\x12\x14\n\x0cnode_address\x18\x05 \x01(\t"+\n\x15MsgCreatePlanResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID"\x15\n\x13MsgLinkNodeResponse"\x17\n\x15MsgUnlinkNodeResponse"\x1e\n\x1cMsgUpdatePlanDetailsResponse"\x1d\n\x1bMsgUpdatePlanStatusResponse"-\n\x17MsgStartSessionResponse\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID2\xff\x04\n\nMsgService\x12`\n\rMsgCreatePlan\x12&.sentinel.plan.v3.MsgCreatePlanRequest\x1a\'.sentinel.plan.v3.MsgCreatePlanResponse\x12Z\n\x0bMsgLinkNode\x12$.sentinel.plan.v3.MsgLinkNodeRequest\x1a%.sentinel.plan.v3.MsgLinkNodeResponse\x12`\n\rMsgUnlinkNode\x12&.sentinel.plan.v3.MsgUnlinkNodeRequest\x1a\'.sentinel.plan.v3.MsgUnlinkNodeResponse\x12u\n\x14MsgUpdatePlanDetails\x12-.sentinel.plan.v3.MsgUpdatePlanDetailsRequest\x1a..sentinel.plan.v3.MsgUpdatePlanDetailsResponse\x12r\n\x13MsgUpdatePlanStatus\x12,.sentinel.plan.v3.MsgUpdatePlanStatusRequest\x1a-.sentinel.plan.v3.MsgUpdatePlanStatusResponse\x12f\n\x0fMsgStartSession\x12(.sentinel.plan.v3.MsgStartSessionRequest\x1a).sentinel.plan.v3.MsgStartSessionResponseBFZ<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['bytes']._loaded_options = None
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['duration']._loaded_options = None
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['duration']._serialized_options = b'\xc8\xde\x1f\x00\x98\xdf\x1f\x01'
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['prices']._loaded_options = None
    _globals['_MSGCREATEPLANREQUEST'].fields_by_name['prices']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGLINKNODEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGLINKNODEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUNLINKNODEREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUNLINKNODEREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATEPLANDETAILSREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATEPLANDETAILSREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGUPDATEPLANSTATUSREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGUPDATEPLANSTATUSREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSESSIONREQUEST'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGCREATEPLANRESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGCREATEPLANRESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._loaded_options = None
    _globals['_MSGSTARTSESSIONRESPONSE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_MSGCREATEPLANREQUEST']._serialized_start = 199
    _globals['_MSGCREATEPLANREQUEST']._serialized_end = 400
    _globals['_MSGLINKNODEREQUEST']._serialized_start = 402
    _globals['_MSGLINKNODEREQUEST']._serialized_end = 477
    _globals['_MSGUNLINKNODEREQUEST']._serialized_start = 479
    _globals['_MSGUNLINKNODEREQUEST']._serialized_end = 556
    _globals['_MSGUPDATEPLANDETAILSREQUEST']._serialized_start = 558
    _globals['_MSGUPDATEPLANDETAILSREQUEST']._serialized_end = 637
    _globals['_MSGUPDATEPLANSTATUSREQUEST']._serialized_start = 639
    _globals['_MSGUPDATEPLANSTATUSREQUEST']._serialized_end = 743
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_start = 746
    _globals['_MSGSTARTSESSIONREQUEST']._serialized_end = 909
    _globals['_MSGCREATEPLANRESPONSE']._serialized_start = 911
    _globals['_MSGCREATEPLANRESPONSE']._serialized_end = 954
    _globals['_MSGLINKNODERESPONSE']._serialized_start = 956
    _globals['_MSGLINKNODERESPONSE']._serialized_end = 977
    _globals['_MSGUNLINKNODERESPONSE']._serialized_start = 979
    _globals['_MSGUNLINKNODERESPONSE']._serialized_end = 1002
    _globals['_MSGUPDATEPLANDETAILSRESPONSE']._serialized_start = 1004
    _globals['_MSGUPDATEPLANDETAILSRESPONSE']._serialized_end = 1034
    _globals['_MSGUPDATEPLANSTATUSRESPONSE']._serialized_start = 1036
    _globals['_MSGUPDATEPLANSTATUSRESPONSE']._serialized_end = 1065
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_start = 1067
    _globals['_MSGSTARTSESSIONRESPONSE']._serialized_end = 1112
    _globals['_MSGSERVICE']._serialized_start = 1115
    _globals['_MSGSERVICE']._serialized_end = 1754