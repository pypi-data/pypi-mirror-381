"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v2/data_retention_deletion_event.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/securitycenter/v2/data_retention_deletion_event.proto\x12\x1egoogle.cloud.securitycenter.v2\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xcf\x02\n\x1aDataRetentionDeletionEvent\x128\n\x14event_detection_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x19\n\x11data_object_count\x18\x03 \x01(\x03\x128\n\x15max_retention_allowed\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12X\n\nevent_type\x18\x05 \x01(\x0e2D.google.cloud.securitycenter.v2.DataRetentionDeletionEvent.EventType"H\n\tEventType\x12\x1a\n\x16EVENT_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bEVENT_TYPE_MAX_TTL_EXCEEDED\x10\x01B\xf9\x01\n"com.google.cloud.securitycenter.v2B\x1fDataRetentionDeletionEventProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v2.data_retention_deletion_event_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v2B\x1fDataRetentionDeletionEventProtoP\x01ZJcloud.google.com/go/securitycenter/apiv2/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V2\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V2\xea\x02!Google::Cloud::SecurityCenter::V2'
    _globals['_DATARETENTIONDELETIONEVENT']._serialized_start = 168
    _globals['_DATARETENTIONDELETIONEVENT']._serialized_end = 503
    _globals['_DATARETENTIONDELETIONEVENT_EVENTTYPE']._serialized_start = 431
    _globals['_DATARETENTIONDELETIONEVENT_EVENTTYPE']._serialized_end = 503