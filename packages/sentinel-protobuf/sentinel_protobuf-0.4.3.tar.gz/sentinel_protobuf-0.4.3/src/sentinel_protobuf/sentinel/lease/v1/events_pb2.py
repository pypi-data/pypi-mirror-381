"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/lease/v1/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/lease/v1/events.proto\x12\x11sentinel.lease.v1\x1a\x14gogoproto/gogo.proto"\x98\x01\n\x0bEventCreate\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x11\n\tmax_hours\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\t\x12\x1c\n\x14renewal_price_policy\x18\x06 \x01(\t"U\n\x08EventEnd\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t"~\n\x08EventPay\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x0f\n\x07payment\x18\x04 \x01(\t\x12\x16\n\x0estaking_reward\x18\x05 \x01(\t"Q\n\x0bEventRefund\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cprov_address\x18\x02 \x01(\t\x12\r\n\x05value\x18\x03 \x01(\t"y\n\nEventRenew\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x11\n\tmax_hours\x18\x04 \x01(\x03\x12\r\n\x05price\x18\x05 \x01(\t"}\n\x12EventUpdateDetails\x12\x1d\n\x08lease_id\x18\x01 \x01(\x04B\x0b\xe2\xde\x1f\x07LeaseID\x12\x14\n\x0cnode_address\x18\x02 \x01(\t\x12\x14\n\x0cprov_address\x18\x03 \x01(\t\x12\x1c\n\x14renewal_price_policy\x18\x04 \x01(\tBGZ=github.com/sentinel-official/sentinelhub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.lease.v1.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z=github.com/sentinel-official/sentinelhub/v12/x/lease/types/v1\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTCREATE'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTEND'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTEND'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTPAY'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTREFUND'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTRENEW'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTRENEW'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['lease_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['lease_id']._serialized_options = b'\xe2\xde\x1f\x07LeaseID'
    _globals['_EVENTCREATE']._serialized_start = 76
    _globals['_EVENTCREATE']._serialized_end = 228
    _globals['_EVENTEND']._serialized_start = 230
    _globals['_EVENTEND']._serialized_end = 315
    _globals['_EVENTPAY']._serialized_start = 317
    _globals['_EVENTPAY']._serialized_end = 443
    _globals['_EVENTREFUND']._serialized_start = 445
    _globals['_EVENTREFUND']._serialized_end = 526
    _globals['_EVENTRENEW']._serialized_start = 528
    _globals['_EVENTRENEW']._serialized_end = 649
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 651
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 776