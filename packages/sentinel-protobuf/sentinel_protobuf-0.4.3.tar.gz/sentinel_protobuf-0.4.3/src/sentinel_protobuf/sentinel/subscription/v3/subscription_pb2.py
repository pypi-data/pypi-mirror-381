"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/subscription/v3/subscription.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
from ....sentinel.types.v1 import renewal_pb2 as sentinel_dot_types_dot_v1_dot_renewal__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+sentinel/subscription/v3/subscription.proto\x12\x18sentinel.subscription.v3\x1a\x14gogoproto/gogo.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dsentinel/types/v1/price.proto\x1a\x1fsentinel/types/v1/renewal.proto\x1a\x1esentinel/types/v1/status.proto"\x9f\x03\n\x0cSubscription\x12\x12\n\x02id\x18\x01 \x01(\x04B\x06\xe2\xde\x1f\x02ID\x12\x13\n\x0bacc_address\x18\x02 \x01(\t\x12\x1b\n\x07plan_id\x18\x03 \x01(\x04B\n\xe2\xde\x1f\x06PlanID\x12-\n\x05price\x18\x04 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00\x12C\n\x14renewal_price_policy\x18\x05 \x01(\x0e2%.sentinel.types.v1.RenewalPricePolicy\x12)\n\x06status\x18\x06 \x01(\x0e2\x19.sentinel.types.v1.Status\x129\n\x0binactive_at\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x126\n\x08start_at\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01\x127\n\tstatus_at\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x08\xc8\xde\x1f\x00\x90\xdf\x1f\x01BNZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.subscription.v3.subscription_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'ZDgithub.com/sentinel-official/sentinelhub/v12/x/subscription/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_SUBSCRIPTION'].fields_by_name['id']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['id']._serialized_options = b'\xe2\xde\x1f\x02ID'
    _globals['_SUBSCRIPTION'].fields_by_name['plan_id']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['plan_id']._serialized_options = b'\xe2\xde\x1f\x06PlanID'
    _globals['_SUBSCRIPTION'].fields_by_name['price']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SUBSCRIPTION'].fields_by_name['inactive_at']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['inactive_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_SUBSCRIPTION'].fields_by_name['start_at']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['start_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_SUBSCRIPTION'].fields_by_name['status_at']._loaded_options = None
    _globals['_SUBSCRIPTION'].fields_by_name['status_at']._serialized_options = b'\xc8\xde\x1f\x00\x90\xdf\x1f\x01'
    _globals['_SUBSCRIPTION']._serialized_start = 225
    _globals['_SUBSCRIPTION']._serialized_end = 640