"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/tasks/v2beta2/task.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2beta2 import target_pb2 as google_dot_cloud_dot_tasks_dot_v2beta2_dot_target__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/tasks/v2beta2/task.proto\x12\x1agoogle.cloud.tasks.v2beta2\x1a\x19google/api/resource.proto\x1a\'google/cloud/tasks/v2beta2/target.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xe9\x04\n\x04Task\x12\x0c\n\x04name\x18\x01 \x01(\t\x12S\n\x17app_engine_http_request\x18\x03 \x01(\x0b20.google.cloud.tasks.v2beta2.AppEngineHttpRequestH\x00\x12?\n\x0cpull_message\x18\x04 \x01(\x0b2\'.google.cloud.tasks.v2beta2.PullMessageH\x00\x12?\n\x0chttp_request\x18\r \x01(\x0b2\'.google.cloud.tasks.v2beta2.HttpRequestH\x00\x121\n\rschedule_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x06status\x18\x07 \x01(\x0b2&.google.cloud.tasks.v2beta2.TaskStatus\x123\n\x04view\x18\x08 \x01(\x0e2%.google.cloud.tasks.v2beta2.Task.View"1\n\x04View\x12\x14\n\x10VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02:h\xeaAe\n\x1ecloudtasks.googleapis.com/Task\x12Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}B\x0e\n\x0cpayload_type"\xdd\x01\n\nTaskStatus\x12\x1e\n\x16attempt_dispatch_count\x18\x01 \x01(\x05\x12\x1e\n\x16attempt_response_count\x18\x02 \x01(\x05\x12G\n\x14first_attempt_status\x18\x03 \x01(\x0b2).google.cloud.tasks.v2beta2.AttemptStatus\x12F\n\x13last_attempt_status\x18\x04 \x01(\x0b2).google.cloud.tasks.v2beta2.AttemptStatus"\xd5\x01\n\rAttemptStatus\x121\n\rschedule_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rdispatch_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x121\n\rresponse_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12+\n\x0fresponse_status\x18\x04 \x01(\x0b2\x12.google.rpc.StatusBr\n\x1ecom.google.cloud.tasks.v2beta2B\tTaskProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta2/cloudtaskspb;cloudtaskspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2beta2.task_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.tasks.v2beta2B\tTaskProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta2/cloudtaskspb;cloudtaskspb'
    _globals['_TASK']._loaded_options = None
    _globals['_TASK']._serialized_options = b'\xeaAe\n\x1ecloudtasks.googleapis.com/Task\x12Cprojects/{project}/locations/{location}/queues/{queue}/tasks/{task}'
    _globals['_TASK']._serialized_start = 196
    _globals['_TASK']._serialized_end = 813
    _globals['_TASK_VIEW']._serialized_start = 642
    _globals['_TASK_VIEW']._serialized_end = 691
    _globals['_TASKSTATUS']._serialized_start = 816
    _globals['_TASKSTATUS']._serialized_end = 1037
    _globals['_ATTEMPTSTATUS']._serialized_start = 1040
    _globals['_ATTEMPTSTATUS']._serialized_end = 1253