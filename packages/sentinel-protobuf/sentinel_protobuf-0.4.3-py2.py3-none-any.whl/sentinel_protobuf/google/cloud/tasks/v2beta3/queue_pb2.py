"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/tasks/v2beta3/queue.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2beta3 import target_pb2 as google_dot_cloud_dot_tasks_dot_v2beta3_dot_target__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/tasks/v2beta3/queue.proto\x12\x1agoogle.cloud.tasks.v2beta3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/tasks/v2beta3/target.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x07\n\x05Queue\x12\x0c\n\x04name\x18\x01 \x01(\t\x12O\n\x15app_engine_http_queue\x18\x03 \x01(\x0b2..google.cloud.tasks.v2beta3.AppEngineHttpQueueH\x00\x12;\n\x0bhttp_target\x18\r \x01(\x0b2&.google.cloud.tasks.v2beta3.HttpTarget\x12;\n\x0brate_limits\x18\x04 \x01(\x0b2&.google.cloud.tasks.v2beta3.RateLimits\x12=\n\x0cretry_config\x18\x05 \x01(\x0b2\'.google.cloud.tasks.v2beta3.RetryConfig\x126\n\x05state\x18\x06 \x01(\x0e2\'.google.cloud.tasks.v2beta3.Queue.State\x12.\n\npurge_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x08task_ttl\x18\x08 \x01(\x0b2\x19.google.protobuf.Duration\x120\n\rtombstone_ttl\x18\t \x01(\x0b2\x19.google.protobuf.Duration\x12X\n\x1astackdriver_logging_config\x18\n \x01(\x0b24.google.cloud.tasks.v2beta3.StackdriverLoggingConfig\x129\n\x04type\x18\x0b \x01(\x0e2&.google.cloud.tasks.v2beta3.Queue.TypeB\x03\xe0A\x05\x12:\n\x05stats\x18\x0c \x01(\x0b2&.google.cloud.tasks.v2beta3.QueueStatsB\x03\xe0A\x03"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\x0c\n\x08DISABLED\x10\x03"0\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04PULL\x10\x01\x12\x08\n\x04PUSH\x10\x02:\\\xeaAY\n\x1fcloudtasks.googleapis.com/Queue\x126projects/{project}/locations/{location}/queues/{queue}B\x0c\n\nqueue_type"j\n\nRateLimits\x12!\n\x19max_dispatches_per_second\x18\x01 \x01(\x01\x12\x16\n\x0emax_burst_size\x18\x02 \x01(\x05\x12!\n\x19max_concurrent_dispatches\x18\x03 \x01(\x05"\xd1\x01\n\x0bRetryConfig\x12\x14\n\x0cmax_attempts\x18\x01 \x01(\x05\x125\n\x12max_retry_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\x0bmin_backoff\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12.\n\x0bmax_backoff\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x12\x15\n\rmax_doublings\x18\x05 \x01(\x05"2\n\x18StackdriverLoggingConfig\x12\x16\n\x0esampling_ratio\x18\x01 \x01(\x01"\xe8\x01\n\nQueueStats\x12\x18\n\x0btasks_count\x18\x01 \x01(\x03B\x03\xe0A\x03\x12F\n\x1doldest_estimated_arrival_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\'\n\x1aexecuted_last_minute_count\x18\x03 \x01(\x03B\x03\xe0A\x03\x12(\n\x1bconcurrent_dispatches_count\x18\x04 \x01(\x03B\x03\xe0A\x03\x12%\n\x18effective_execution_rate\x18\x05 \x01(\x01B\x03\xe0A\x03Bs\n\x1ecom.google.cloud.tasks.v2beta3B\nQueueProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta3/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2beta3.queue_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.tasks.v2beta3B\nQueueProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta3/cloudtaskspb;cloudtaskspb'
    _globals['_QUEUE'].fields_by_name['type']._loaded_options = None
    _globals['_QUEUE'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_QUEUE'].fields_by_name['stats']._loaded_options = None
    _globals['_QUEUE'].fields_by_name['stats']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUE']._loaded_options = None
    _globals['_QUEUE']._serialized_options = b'\xeaAY\n\x1fcloudtasks.googleapis.com/Queue\x126projects/{project}/locations/{location}/queues/{queue}'
    _globals['_QUEUESTATS'].fields_by_name['tasks_count']._loaded_options = None
    _globals['_QUEUESTATS'].fields_by_name['tasks_count']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUESTATS'].fields_by_name['oldest_estimated_arrival_time']._loaded_options = None
    _globals['_QUEUESTATS'].fields_by_name['oldest_estimated_arrival_time']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUESTATS'].fields_by_name['executed_last_minute_count']._loaded_options = None
    _globals['_QUEUESTATS'].fields_by_name['executed_last_minute_count']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUESTATS'].fields_by_name['concurrent_dispatches_count']._loaded_options = None
    _globals['_QUEUESTATS'].fields_by_name['concurrent_dispatches_count']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUESTATS'].fields_by_name['effective_execution_rate']._loaded_options = None
    _globals['_QUEUESTATS'].fields_by_name['effective_execution_rate']._serialized_options = b'\xe0A\x03'
    _globals['_QUEUE']._serialized_start = 237
    _globals['_QUEUE']._serialized_end = 1161
    _globals['_QUEUE_STATE']._serialized_start = 934
    _globals['_QUEUE_STATE']._serialized_end = 1003
    _globals['_QUEUE_TYPE']._serialized_start = 1005
    _globals['_QUEUE_TYPE']._serialized_end = 1053
    _globals['_RATELIMITS']._serialized_start = 1163
    _globals['_RATELIMITS']._serialized_end = 1269
    _globals['_RETRYCONFIG']._serialized_start = 1272
    _globals['_RETRYCONFIG']._serialized_end = 1481
    _globals['_STACKDRIVERLOGGINGCONFIG']._serialized_start = 1483
    _globals['_STACKDRIVERLOGGINGCONFIG']._serialized_end = 1533
    _globals['_QUEUESTATS']._serialized_start = 1536
    _globals['_QUEUESTATS']._serialized_end = 1768