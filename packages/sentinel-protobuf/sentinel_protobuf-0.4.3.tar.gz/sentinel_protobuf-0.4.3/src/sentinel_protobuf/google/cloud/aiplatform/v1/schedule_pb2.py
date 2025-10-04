"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/schedule.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import notebook_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_notebook__service__pb2
from .....google.cloud.aiplatform.v1 import pipeline_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_pipeline__service__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/aiplatform/v1/schedule.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/aiplatform/v1/notebook_service.proto\x1a1google/cloud/aiplatform/v1/pipeline_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xf5\t\n\x08Schedule\x12\x0e\n\x04cron\x18\n \x01(\tH\x00\x12[\n\x1bcreate_pipeline_job_request\x18\x0e \x01(\x0b24.google.cloud.aiplatform.v1.CreatePipelineJobRequestH\x01\x12n\n%create_notebook_execution_job_request\x18\x14 \x01(\x0b2=.google.cloud.aiplatform.v1.CreateNotebookExecutionJobRequestH\x01\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x123\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x121\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01\x12\x1a\n\rmax_run_count\x18\x10 \x01(\x03B\x03\xe0A\x01\x12\x1e\n\x11started_run_count\x18\x11 \x01(\x03B\x03\xe0A\x03\x12>\n\x05state\x18\x05 \x01(\x0e2*.google.cloud.aiplatform.v1.Schedule.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x13 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rnext_run_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x128\n\x0flast_pause_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x129\n\x10last_resume_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12%\n\x18max_concurrent_run_count\x18\x0b \x01(\x03B\x03\xe0A\x02\x12\x1b\n\x0eallow_queueing\x18\x0c \x01(\x08B\x03\xe0A\x01\x12\x15\n\x08catch_up\x18\r \x01(\x08B\x03\xe0A\x03\x12Z\n\x1blast_scheduled_run_response\x18\x12 \x01(\x0b20.google.cloud.aiplatform.v1.Schedule.RunResponseB\x03\xe0A\x03\x1a[\n\x0bRunResponse\x126\n\x12scheduled_run_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x14\n\x0crun_response\x18\x02 \x01(\t"E\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\n\n\x06PAUSED\x10\x02\x12\r\n\tCOMPLETED\x10\x03:e\xeaAb\n"aiplatform.googleapis.com/Schedule\x12<projects/{project}/locations/{location}/schedules/{schedule}B\x14\n\x12time_specificationB\t\n\x07requestB\xcb\x01\n\x1ecom.google.cloud.aiplatform.v1B\rScheduleProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.schedule_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\rScheduleProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_SCHEDULE'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SCHEDULE'].fields_by_name['display_name']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEDULE'].fields_by_name['start_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULE'].fields_by_name['end_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULE'].fields_by_name['max_run_count']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['max_run_count']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULE'].fields_by_name['started_run_count']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['started_run_count']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['state']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['create_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['update_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['next_run_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['next_run_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['last_pause_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['last_pause_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['last_resume_time']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['last_resume_time']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['max_concurrent_run_count']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['max_concurrent_run_count']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEDULE'].fields_by_name['allow_queueing']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['allow_queueing']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEDULE'].fields_by_name['catch_up']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['catch_up']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE'].fields_by_name['last_scheduled_run_response']._loaded_options = None
    _globals['_SCHEDULE'].fields_by_name['last_scheduled_run_response']._serialized_options = b'\xe0A\x03'
    _globals['_SCHEDULE']._loaded_options = None
    _globals['_SCHEDULE']._serialized_options = b'\xeaAb\n"aiplatform.googleapis.com/Schedule\x12<projects/{project}/locations/{location}/schedules/{schedule}'
    _globals['_SCHEDULE']._serialized_start = 269
    _globals['_SCHEDULE']._serialized_end = 1538
    _globals['_SCHEDULE_RUNRESPONSE']._serialized_start = 1240
    _globals['_SCHEDULE_RUNRESPONSE']._serialized_end = 1331
    _globals['_SCHEDULE_STATE']._serialized_start = 1333
    _globals['_SCHEDULE_STATE']._serialized_end = 1402