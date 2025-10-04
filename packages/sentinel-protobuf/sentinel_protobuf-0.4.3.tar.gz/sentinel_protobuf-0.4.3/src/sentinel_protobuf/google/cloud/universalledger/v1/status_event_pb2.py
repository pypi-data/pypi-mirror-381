"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/universalledger/v1/status_event.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/universalledger/v1/status_event.proto\x12\x1fgoogle.cloud.universalledger.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xd2\x01\n\x0bStatusEvent\x123\n\nevent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\nevent_type\x18\x02 \x01(\x0e2*.google.cloud.universalledger.v1.EventTypeB\x03\xe0A\x03\x12I\n\revent_details\x18\x03 \x01(\x0b2-.google.cloud.universalledger.v1.EventDetailsB\x03\xe0A\x03"t\n\x0cEventDetails\x12S\n\x11execution_details\x18\x01 \x01(\x0b21.google.cloud.universalledger.v1.ExecutionDetailsB\x03\xe0A\x03H\x00B\x0f\n\revent_details")\n\x10ExecutionDetails\x12\x15\n\x08round_id\x18\x01 \x01(\x03B\x03\xe0A\x03*\xd4\x01\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13EVENT_TYPE_RECEIVED\x10\x01\x12\x1a\n\x16EVENT_TYPE_BROADCASTED\x10\x02\x12\x16\n\x12EVENT_TYPE_ORDERED\x10\x03\x12 \n\x1cEVENT_TYPE_EXECUTION_STARTED\x10\x04\x12"\n\x1eEVENT_TYPE_EXECUTION_COMPLETED\x10\x05\x12\x18\n\x14EVENT_TYPE_FINALIZED\x10\x06B\xf1\x01\n#com.google.cloud.universalledger.v1B\x10StatusEventProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.universalledger.v1.status_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.universalledger.v1B\x10StatusEventProtoP\x01ZMcloud.google.com/go/universalledger/apiv1/universalledgerpb;universalledgerpb\xaa\x02\x1fGoogle.Cloud.UniversalLedger.V1\xca\x02\x1fGoogle\\Cloud\\UniversalLedger\\V1\xea\x02"Google::Cloud::UniversalLedger::V1'
    _globals['_STATUSEVENT'].fields_by_name['event_time']._loaded_options = None
    _globals['_STATUSEVENT'].fields_by_name['event_time']._serialized_options = b'\xe0A\x03'
    _globals['_STATUSEVENT'].fields_by_name['event_type']._loaded_options = None
    _globals['_STATUSEVENT'].fields_by_name['event_type']._serialized_options = b'\xe0A\x03'
    _globals['_STATUSEVENT'].fields_by_name['event_details']._loaded_options = None
    _globals['_STATUSEVENT'].fields_by_name['event_details']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTDETAILS'].fields_by_name['execution_details']._loaded_options = None
    _globals['_EVENTDETAILS'].fields_by_name['execution_details']._serialized_options = b'\xe0A\x03'
    _globals['_EXECUTIONDETAILS'].fields_by_name['round_id']._loaded_options = None
    _globals['_EXECUTIONDETAILS'].fields_by_name['round_id']._serialized_options = b'\xe0A\x03'
    _globals['_EVENTTYPE']._serialized_start = 528
    _globals['_EVENTTYPE']._serialized_end = 740
    _globals['_STATUSEVENT']._serialized_start = 154
    _globals['_STATUSEVENT']._serialized_end = 364
    _globals['_EVENTDETAILS']._serialized_start = 366
    _globals['_EVENTDETAILS']._serialized_end = 482
    _globals['_EXECUTIONDETAILS']._serialized_start = 484
    _globals['_EXECUTIONDETAILS']._serialized_end = 525