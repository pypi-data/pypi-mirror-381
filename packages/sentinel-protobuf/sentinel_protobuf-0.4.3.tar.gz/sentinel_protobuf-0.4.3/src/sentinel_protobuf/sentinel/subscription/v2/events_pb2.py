"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/subscription/v2/events.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%sentinel/subscription/v2/events.proto\x12\x18sentinel.subscription.v2\x1a\x14gogoproto/gogo.proto\x1a\x1esentinel/types/v1/status.proto"\xc2\x01\n\rEventAllocate\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x124\n\rgranted_bytes\x18\x02 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x125\n\x0eutilised_bytes\x18\x03 \x01(\tB\x1d\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int\x12\x1f\n\x02id\x18\x04 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\x88\x01\n\x11EventCreatePayout\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\xe0\x01\n\x11EventPayForPayout\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12#\n\x07payment\x18\x03 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"payment"\x121\n\x0estaking_reward\x18\x04 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"staking_reward"\x12\x1f\n\x02id\x18\x05 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\xe6\x01\n\x0fEventPayForPlan\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12#\n\x07payment\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"payment"\x125\n\x10provider_address\x18\x03 \x01(\tB\x1b\xf2\xde\x1f\x17yaml:"provider_address"\x121\n\x0estaking_reward\x18\x04 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"staking_reward"\x12\x1f\n\x02id\x18\x05 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\xbf\x02\n\x12EventPayForSession\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12-\n\x0cnode_address\x18\x02 \x01(\tB\x17\xf2\xde\x1f\x13yaml:"node_address"\x12#\n\x07payment\x18\x03 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"payment"\x121\n\x0estaking_reward\x18\x04 \x01(\tB\x19\xf2\xde\x1f\x15yaml:"staking_reward"\x126\n\nsession_id\x18\x05 \x01(\x04B"\xe2\xde\x1f\tSessionID\xf2\xde\x1f\x11yaml:"session_id"\x12E\n\x0fsubscription_id\x18\x06 \x01(\x04B,\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id""v\n\x0bEventRefund\x12#\n\x07address\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12!\n\x06amount\x18\x02 \x01(\tB\x11\xf2\xde\x1f\ryaml:"amount"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id""\xc6\x01\n\x11EventUpdateStatus\x12<\n\x06status\x18\x01 \x01(\x0e2\x19.sentinel.types.v1.StatusB\x11\xf2\xde\x1f\ryaml:"status"\x12#\n\x07address\x18\x02 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"address"\x12\x1f\n\x02id\x18\x03 \x01(\x04B\x13\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"\x12-\n\x07plan_id\x18\x04 \x01(\x04B\x1c\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"BNZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v2.events_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v2\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_EVENTALLOCATE'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTALLOCATE'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTALLOCATE'].fields_by_name['granted_bytes']._loaded_options = None
    _globals['_EVENTALLOCATE'].fields_by_name['granted_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_EVENTALLOCATE'].fields_by_name['utilised_bytes']._loaded_options = None
    _globals['_EVENTALLOCATE'].fields_by_name['utilised_bytes']._serialized_options = b'\xc8\xde\x1f\x00\xda\xde\x1f\x15cosmossdk.io/math.Int'
    _globals['_EVENTALLOCATE'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTALLOCATE'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTCREATEPAYOUT'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['payment']._loaded_options = None
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['payment']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"payment"'
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['staking_reward']._loaded_options = None
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['staking_reward']._serialized_options = b'\xf2\xde\x1f\x15yaml:"staking_reward"'
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTPAYFORPAYOUT'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTPAYFORPLAN'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTPAYFORPLAN'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTPAYFORPLAN'].fields_by_name['payment']._loaded_options = None
    _globals['_EVENTPAYFORPLAN'].fields_by_name['payment']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"payment"'
    _globals['_EVENTPAYFORPLAN'].fields_by_name['provider_address']._loaded_options = None
    _globals['_EVENTPAYFORPLAN'].fields_by_name['provider_address']._serialized_options = b'\xf2\xde\x1f\x17yaml:"provider_address"'
    _globals['_EVENTPAYFORPLAN'].fields_by_name['staking_reward']._loaded_options = None
    _globals['_EVENTPAYFORPLAN'].fields_by_name['staking_reward']._serialized_options = b'\xf2\xde\x1f\x15yaml:"staking_reward"'
    _globals['_EVENTPAYFORPLAN'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTPAYFORPLAN'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['node_address']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['node_address']._serialized_options = b'\xf2\xde\x1f\x13yaml:"node_address"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['payment']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['payment']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"payment"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['staking_reward']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['staking_reward']._serialized_options = b'\xf2\xde\x1f\x15yaml:"staking_reward"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['session_id']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['session_id']._serialized_options = b'\xe2\xde\x1f\tSessionID\xf2\xde\x1f\x11yaml:"session_id"'
    _globals['_EVENTPAYFORSESSION'].fields_by_name['subscription_id']._loaded_options = None
    _globals['_EVENTPAYFORSESSION'].fields_by_name['subscription_id']._serialized_options = b'\xe2\xde\x1f\x0eSubscriptionID\xf2\xde\x1f\x16yaml:"subscription_id"'
    _globals['_EVENTREFUND'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTREFUND'].fields_by_name['amount']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['amount']._serialized_options = b'\xf2\xde\x1f\ryaml:"amount"'
    _globals['_EVENTREFUND'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTREFUND'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['status']._serialized_options = b'\xf2\xde\x1f\ryaml:"status"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['address']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"address"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID\xf2\xde\x1f\tyaml:"id"'
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._loaded_options = None
    _globals['_EVENTUPDATESTATUS'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID\xf2\xde\x1f\x0eyaml:"plan_id"'
    _globals['_EVENTALLOCATE']._serialized_start = 122
    _globals['_EVENTALLOCATE']._serialized_end = 316
    _globals['_EVENTCREATEPAYOUT']._serialized_start = 319
    _globals['_EVENTCREATEPAYOUT']._serialized_end = 455
    _globals['_EVENTPAYFORPAYOUT']._serialized_start = 458
    _globals['_EVENTPAYFORPAYOUT']._serialized_end = 682
    _globals['_EVENTPAYFORPLAN']._serialized_start = 685
    _globals['_EVENTPAYFORPLAN']._serialized_end = 915
    _globals['_EVENTPAYFORSESSION']._serialized_start = 918
    _globals['_EVENTPAYFORSESSION']._serialized_end = 1237
    _globals['_EVENTREFUND']._serialized_start = 1239
    _globals['_EVENTREFUND']._serialized_end = 1357
    _globals['_EVENTUPDATESTATUS']._serialized_start = 1360
    _globals['_EVENTUPDATESTATUS']._serialized_end = 1558