"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/plan/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dsentinel/plan/v3/events.proto\x12\x10sentinel.plan.v3\x1a\x14gogoproto/gogo.proto"\x82\x01\n\x0bEventCreate\x12\x1b\n\x07plan_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\r\n\x05bytes\x18\x03 \x01(\t\x12\x10\n\x08duration\x18\x04 \x01(\t\x12\x0e\n\x06prices\x18\x05 \x01(\t\x12\x0f\n\x07private\x18\x06 \x01(\x08"X\n\rEventLinkNode\x12\x1b\n\x07plan_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"Z\n\x0fEventUnlinkNode\x12\x1b\n\x07plan_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"X\n\x12EventUpdateDetails\x12\x1b\n\x07plan_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x0f\n\x07private\x18\x03 \x01(\x08"V\n\x11EventUpdateStatus\x12\x1b\n\x07plan_id\x18\x01 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\x0e\n\x06status\x18\x03 \x01(\tBFZ<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.plan.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/plan/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTLINKNODE'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTLINKNODE'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTUNLINKNODE'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUNLINKNODE'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTCREATE']._serialized_start = 74
    _globals['_EVENTCREATE']._serialized_end = 204
    _globals['_EVENTLINKNODE']._serialized_start = 206
    _globals['_EVENTLINKNODE']._serialized_end = 294
    _globals['_EVENTUNLINKNODE']._serialized_start = 296
    _globals['_EVENTUNLINKNODE']._serialized_end = 386
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 388
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 476
    _globals['_EVENTUPDATESTATUS']._serialized_start = 478
    _globals['_EVENTUPDATESTATUS']._serialized_end = 564