"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/subscription/v3/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v3/events.proto\x12\x18sentinel.subscription.v3\x1a\x14gogoproto/gogo.proto"\x80\x01\n\rEventAllocate\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x15\n\rgranted_bytes\x18\x03 \x01(\t\x12\x16\n\x0eutilised_bytes\x18\x04 \x01(\t"{\n\x0bEventCreate\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t"\x8f\x01\n\x12EventCreateSession\x12!\n\nsession_id\x18\x01 \x01(\x04B\r\xe2\xde\x1f\tSessionID\x12+\n\x0fsubscription_id\x18\x04 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x14\n\x0cnode_address\x18\x03 \x01(\t"i\n\x08EventEnd\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t"\xa8\x01\n\x08EventPay\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x14\n\x0cprov_address\x18\x04 \x01(\t\x12\x0f\n\x07payment\x18\x05 \x01(\t\x12\x16\n\x0estaking_reward\x18\x06 \x01(\t"z\n\nEventRenew\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\r\n\x05price\x18\x04 \x01(\t"\x91\x01\n\x12EventUpdateDetails\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x1c\n\x14renewal_price_policy\x18\x04 \x01(\t"\x82\x01\n\x11EventUpdateStatus\x12+\n\x0fsubscription_id\x18\x01 \x01(\x04B\x12\xe2\xde\x1f\x0eSubscriptionID\x12\x1b\n\x07plan_id\x18\x02 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12\x13\n\x0bacc_address\x18\x03 \x01(\t\x12\x0e\n\x06status\x18\x04 \x01(\tBNZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTALLOCATE'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTALLOCATE'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTCREATE'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTCREATE'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTCREATE'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTCREATESESSION'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTCREATESESSION'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID'
    _globals['_EVENTCREATESESSION'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTCREATESESSION'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTEND'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTEND'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTEND'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTEND'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTPAY'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTPAY'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTPAY'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTRENEW'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTRENEW'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTRENEW'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTRENEW'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATEDETAILS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_EVENTALLOCATE']._serialized_start = 90
    _globals['_EVENTALLOCATE']._serialized_end = 218
    _globals['_EVENTCREATE']._serialized_start = 220
    _globals['_EVENTCREATE']._serialized_end = 343
    _globals['_EVENTCREATESESSION']._serialized_start = 346
    _globals['_EVENTCREATESESSION']._serialized_end = 489
    _globals['_EVENTEND']._serialized_start = 491
    _globals['_EVENTEND']._serialized_end = 596
    _globals['_EVENTPAY']._serialized_start = 599
    _globals['_EVENTPAY']._serialized_end = 767
    _globals['_EVENTRENEW']._serialized_start = 769
    _globals['_EVENTRENEW']._serialized_end = 891
    _globals['_EVENTUPDATEDETAILS']._serialized_start = 894
    _globals['_EVENTUPDATEDETAILS']._serialized_end = 1039
    _globals['_EVENTUPDATESTATUS']._serialized_start = 1042
    _globals['_EVENTUPDATESTATUS']._serialized_end = 1172