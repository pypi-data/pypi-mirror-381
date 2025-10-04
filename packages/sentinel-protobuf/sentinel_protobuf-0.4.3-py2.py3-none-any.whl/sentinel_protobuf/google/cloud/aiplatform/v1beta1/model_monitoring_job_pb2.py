"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_monitoring_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import job_state_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_job__state__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/model_monitoring_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/job_state.proto\x1a;google/cloud/aiplatform/v1beta1/model_monitoring_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto\x1a\x1agoogle/type/interval.proto"\xc1\x05\n\x12ModelMonitoringJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12S\n\x15model_monitoring_spec\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.ModelMonitoringSpec\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12=\n\x05state\x18\x06 \x01(\x0e2).google.cloud.aiplatform.v1beta1.JobStateB\x03\xe0A\x03\x12<\n\x08schedule\x18\x07 \x01(\tB*\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Schedule\x12e\n\x14job_execution_detail\x18\x08 \x01(\x0b2B.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetailB\x03\xe0A\x03\x126\n\rschedule_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xa4\x01\xeaA\xa0\x01\n,aiplatform.googleapis.com/ModelMonitoringJob\x12pprojects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}"\xb4\x04\n!ModelMonitoringJobExecutionDetail\x12n\n\x11baseline_datasets\x18\x01 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset\x12l\n\x0ftarget_datasets\x18\x02 \x03(\x0b2S.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ProcessedDataset\x12q\n\x10objective_status\x18\x03 \x03(\x0b2W.google.cloud.aiplatform.v1beta1.ModelMonitoringJobExecutionDetail.ObjectiveStatusEntry\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status\x1aO\n\x10ProcessedDataset\x12\x10\n\x08location\x18\x01 \x01(\t\x12)\n\ntime_range\x18\x02 \x01(\x0b2\x15.google.type.Interval\x1aJ\n\x14ObjectiveStatusEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b2\x12.google.rpc.Status:\x028\x01B\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x17ModelMonitoringJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitoring_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x17ModelMonitoringJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELMONITORINGJOB'].fields_by_name['name']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB'].fields_by_name['state']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB'].fields_by_name['schedule']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['schedule']._serialized_options = b'\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Schedule'
    _globals['_MODELMONITORINGJOB'].fields_by_name['job_execution_detail']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['job_execution_detail']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB'].fields_by_name['schedule_time']._loaded_options = None
    _globals['_MODELMONITORINGJOB'].fields_by_name['schedule_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITORINGJOB']._loaded_options = None
    _globals['_MODELMONITORINGJOB']._serialized_options = b'\xeaA\xa0\x01\n,aiplatform.googleapis.com/ModelMonitoringJob\x12pprojects/{project}/locations/{location}/modelMonitors/{model_monitor}/modelMonitoringJobs/{model_monitoring_job}'
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_OBJECTIVESTATUSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_OBJECTIVESTATUSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGJOB']._serialized_start = 352
    _globals['_MODELMONITORINGJOB']._serialized_end = 1057
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL']._serialized_start = 1060
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL']._serialized_end = 1624
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_PROCESSEDDATASET']._serialized_start = 1469
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_PROCESSEDDATASET']._serialized_end = 1548
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_OBJECTIVESTATUSENTRY']._serialized_start = 1550
    _globals['_MODELMONITORINGJOBEXECUTIONDETAIL_OBJECTIVESTATUSENTRY']._serialized_end = 1624