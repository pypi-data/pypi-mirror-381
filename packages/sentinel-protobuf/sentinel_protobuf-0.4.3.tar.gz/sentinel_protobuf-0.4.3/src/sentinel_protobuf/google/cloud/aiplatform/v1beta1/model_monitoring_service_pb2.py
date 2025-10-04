"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_monitoring_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitor_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitor__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_alert_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__alert__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__job__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_stats_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__stats__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/aiplatform/v1beta1/model_monitoring_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/aiplatform/v1beta1/model_monitor.proto\x1a<google/cloud/aiplatform/v1beta1/model_monitoring_alert.proto\x1a:google/cloud/aiplatform/v1beta1/model_monitoring_job.proto\x1a<google/cloud/aiplatform/v1beta1/model_monitoring_stats.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1agoogle/type/interval.proto"\xc0\x01\n\x19CreateModelMonitorRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12I\n\rmodel_monitor\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.ModelMonitorB\x03\xe0A\x02\x12\x1d\n\x10model_monitor_id\x18\x03 \x01(\tB\x03\xe0A\x01"z\n#CreateModelMonitorOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x9c\x01\n\x19UpdateModelMonitorRequest\x12I\n\rmodel_monitor\x18\x01 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.ModelMonitorB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"z\n#UpdateModelMonitorOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"V\n\x16GetModelMonitorRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor"\xbb\x01\n\x18ListModelMonitorsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"{\n\x19ListModelMonitorsResponse\x12E\n\x0emodel_monitors\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.ModelMonitor\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"m\n\x19DeleteModelMonitorRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\xdf\x01\n\x1fCreateModelMonitoringJobRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor\x12V\n\x14model_monitoring_job\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.ModelMonitoringJobB\x03\xe0A\x02\x12$\n\x17model_monitoring_job_id\x18\x03 \x01(\tB\x03\xe0A\x01"b\n\x1cGetModelMonitoringJobRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/ModelMonitoringJob"\xc6\x01\n\x1eListModelMonitoringJobsRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x8e\x01\n\x1fListModelMonitoringJobsResponse\x12R\n\x15model_monitoring_jobs\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1beta1.ModelMonitoringJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"e\n\x1fDeleteModelMonitoringJobRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/ModelMonitoringJob"\x98\x02\n!SearchModelMonitoringStatsRequest\x12E\n\rmodel_monitor\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor\x12W\n\x0cstats_filter\x18\x02 \x01(\x0b2A.google.cloud.aiplatform.v1beta1.SearchModelMonitoringStatsFilter\x12,\n\rtime_interval\x18\x03 \x01(\x0b2\x15.google.type.Interval\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"\x8e\x01\n"SearchModelMonitoringStatsResponse\x12O\n\x10monitoring_stats\x18\x01 \x03(\x0b25.google.cloud.aiplatform.v1beta1.ModelMonitoringStats\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x90\x02\n"SearchModelMonitoringAlertsRequest\x12E\n\rmodel_monitor\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor\x12\x1c\n\x14model_monitoring_job\x18\x02 \x01(\t\x122\n\x13alert_time_interval\x18\x03 \x01(\x0b2\x15.google.type.Interval\x12\x12\n\nstats_name\x18\x04 \x01(\t\x12\x16\n\x0eobjective_type\x18\x05 \x01(\t\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t"\xb3\x01\n#SearchModelMonitoringAlertsResponse\x12V\n\x17model_monitoring_alerts\x18\x01 \x03(\x0b25.google.cloud.aiplatform.v1beta1.ModelMonitoringAlert\x12\x1b\n\x13total_number_alerts\x18\x02 \x01(\x03\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t2\xf6\x16\n\x16ModelMonitoringService\x12\x8c\x02\n\x12CreateModelMonitor\x12:.google.cloud.aiplatform.v1beta1.CreateModelMonitorRequest\x1a\x1d.google.longrunning.Operation"\x9a\x01\xcaA3\n\x0cModelMonitor\x12#CreateModelMonitorOperationMetadata\xdaA\x14parent,model_monitor\x82\xd3\xe4\x93\x02G"6/v1beta1/{parent=projects/*/locations/*}/modelMonitors:\rmodel_monitor\x12\x9f\x02\n\x12UpdateModelMonitor\x12:.google.cloud.aiplatform.v1beta1.UpdateModelMonitorRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA3\n\x0cModelMonitor\x12#UpdateModelMonitorOperationMetadata\xdaA\x19model_monitor,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{model_monitor.name=projects/*/locations/*/modelMonitors/*}:\rmodel_monitor\x12\xc0\x01\n\x0fGetModelMonitor\x127.google.cloud.aiplatform.v1beta1.GetModelMonitorRequest\x1a-.google.cloud.aiplatform.v1beta1.ModelMonitor"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/modelMonitors/*}\x12\xd3\x01\n\x11ListModelMonitors\x129.google.cloud.aiplatform.v1beta1.ListModelMonitorsRequest\x1a:.google.cloud.aiplatform.v1beta1.ListModelMonitorsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/modelMonitors\x12\xe9\x01\n\x12DeleteModelMonitor\x12:.google.cloud.aiplatform.v1beta1.DeleteModelMonitorRequest\x1a\x1d.google.longrunning.Operation"x\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/modelMonitors/*}\x12\x9c\x02\n\x18CreateModelMonitoringJob\x12@.google.cloud.aiplatform.v1beta1.CreateModelMonitoringJobRequest\x1a3.google.cloud.aiplatform.v1beta1.ModelMonitoringJob"\x88\x01\xdaA\x1bparent,model_monitoring_job\x82\xd3\xe4\x93\x02d"L/v1beta1/{parent=projects/*/locations/*/modelMonitors/*}/modelMonitoringJobs:\x14model_monitoring_job\x12\xe8\x01\n\x15GetModelMonitoringJob\x12=.google.cloud.aiplatform.v1beta1.GetModelMonitoringJobRequest\x1a3.google.cloud.aiplatform.v1beta1.ModelMonitoringJob"[\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{name=projects/*/locations/*/modelMonitors/*/modelMonitoringJobs/*}\x12\xfb\x01\n\x17ListModelMonitoringJobs\x12?.google.cloud.aiplatform.v1beta1.ListModelMonitoringJobsRequest\x1a@.google.cloud.aiplatform.v1beta1.ListModelMonitoringJobsResponse"]\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/modelMonitors/*}/modelMonitoringJobs\x12\x8c\x02\n\x18DeleteModelMonitoringJob\x12@.google.cloud.aiplatform.v1beta1.DeleteModelMonitoringJobRequest\x1a\x1d.google.longrunning.Operation"\x8e\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02N*L/v1beta1/{name=projects/*/locations/*/modelMonitors/*/modelMonitoringJobs/*}\x12\x9c\x02\n\x1aSearchModelMonitoringStats\x12B.google.cloud.aiplatform.v1beta1.SearchModelMonitoringStatsRequest\x1aC.google.cloud.aiplatform.v1beta1.SearchModelMonitoringStatsResponse"u\xdaA\rmodel_monitor\x82\xd3\xe4\x93\x02_"Z/v1beta1/{model_monitor=projects/*/locations/*/modelMonitors/*}:searchModelMonitoringStats:\x01*\x12\xa0\x02\n\x1bSearchModelMonitoringAlerts\x12C.google.cloud.aiplatform.v1beta1.SearchModelMonitoringAlertsRequest\x1aD.google.cloud.aiplatform.v1beta1.SearchModelMonitoringAlertsResponse"v\xdaA\rmodel_monitor\x82\xd3\xe4\x93\x02`"[/v1beta1/{model_monitor=projects/*/locations/*/modelMonitors/*}:searchModelMonitoringAlerts:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf2\x01\n#com.google.cloud.aiplatform.v1beta1B\x1bModelMonitoringServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitoring_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1bModelMonitoringServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['model_monitor']._loaded_options = None
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['model_monitor']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['model_monitor_id']._loaded_options = None
    _globals['_CREATEMODELMONITORREQUEST'].fields_by_name['model_monitor_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMODELMONITORREQUEST'].fields_by_name['model_monitor']._loaded_options = None
    _globals['_UPDATEMODELMONITORREQUEST'].fields_by_name['model_monitor']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMODELMONITORREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMODELMONITORREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_GETMODELMONITORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELMONITORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_LISTMODELMONITORSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELMONITORSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEMODELMONITORREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELMONITORREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_DELETEMODELMONITORREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETEMODELMONITORREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['model_monitoring_job']._loaded_options = None
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['model_monitoring_job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['model_monitoring_job_id']._loaded_options = None
    _globals['_CREATEMODELMONITORINGJOBREQUEST'].fields_by_name['model_monitoring_job_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETMODELMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMODELMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/ModelMonitoringJob'
    _globals['_LISTMODELMONITORINGJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMODELMONITORINGJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_DELETEMODELMONITORINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEMODELMONITORINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/ModelMonitoringJob'
    _globals['_SEARCHMODELMONITORINGSTATSREQUEST'].fields_by_name['model_monitor']._loaded_options = None
    _globals['_SEARCHMODELMONITORINGSTATSREQUEST'].fields_by_name['model_monitor']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_SEARCHMODELMONITORINGALERTSREQUEST'].fields_by_name['model_monitor']._loaded_options = None
    _globals['_SEARCHMODELMONITORINGALERTSREQUEST'].fields_by_name['model_monitor']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ModelMonitor'
    _globals['_MODELMONITORINGSERVICE']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['CreateModelMonitor']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['CreateModelMonitor']._serialized_options = b'\xcaA3\n\x0cModelMonitor\x12#CreateModelMonitorOperationMetadata\xdaA\x14parent,model_monitor\x82\xd3\xe4\x93\x02G"6/v1beta1/{parent=projects/*/locations/*}/modelMonitors:\rmodel_monitor'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['UpdateModelMonitor']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['UpdateModelMonitor']._serialized_options = b'\xcaA3\n\x0cModelMonitor\x12#UpdateModelMonitorOperationMetadata\xdaA\x19model_monitor,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{model_monitor.name=projects/*/locations/*/modelMonitors/*}:\rmodel_monitor'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['GetModelMonitor']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['GetModelMonitor']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/modelMonitors/*}'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['ListModelMonitors']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['ListModelMonitors']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/modelMonitors'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['DeleteModelMonitor']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['DeleteModelMonitor']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/modelMonitors/*}'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['CreateModelMonitoringJob']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['CreateModelMonitoringJob']._serialized_options = b'\xdaA\x1bparent,model_monitoring_job\x82\xd3\xe4\x93\x02d"L/v1beta1/{parent=projects/*/locations/*/modelMonitors/*}/modelMonitoringJobs:\x14model_monitoring_job'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['GetModelMonitoringJob']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['GetModelMonitoringJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{name=projects/*/locations/*/modelMonitors/*/modelMonitoringJobs/*}'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['ListModelMonitoringJobs']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['ListModelMonitoringJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/v1beta1/{parent=projects/*/locations/*/modelMonitors/*}/modelMonitoringJobs'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['DeleteModelMonitoringJob']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['DeleteModelMonitoringJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02N*L/v1beta1/{name=projects/*/locations/*/modelMonitors/*/modelMonitoringJobs/*}'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['SearchModelMonitoringStats']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['SearchModelMonitoringStats']._serialized_options = b'\xdaA\rmodel_monitor\x82\xd3\xe4\x93\x02_"Z/v1beta1/{model_monitor=projects/*/locations/*/modelMonitors/*}:searchModelMonitoringStats:\x01*'
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['SearchModelMonitoringAlerts']._loaded_options = None
    _globals['_MODELMONITORINGSERVICE'].methods_by_name['SearchModelMonitoringAlerts']._serialized_options = b'\xdaA\rmodel_monitor\x82\xd3\xe4\x93\x02`"[/v1beta1/{model_monitor=projects/*/locations/*/modelMonitors/*}:searchModelMonitoringAlerts:\x01*'
    _globals['_CREATEMODELMONITORREQUEST']._serialized_start = 629
    _globals['_CREATEMODELMONITORREQUEST']._serialized_end = 821
    _globals['_CREATEMODELMONITOROPERATIONMETADATA']._serialized_start = 823
    _globals['_CREATEMODELMONITOROPERATIONMETADATA']._serialized_end = 945
    _globals['_UPDATEMODELMONITORREQUEST']._serialized_start = 948
    _globals['_UPDATEMODELMONITORREQUEST']._serialized_end = 1104
    _globals['_UPDATEMODELMONITOROPERATIONMETADATA']._serialized_start = 1106
    _globals['_UPDATEMODELMONITOROPERATIONMETADATA']._serialized_end = 1228
    _globals['_GETMODELMONITORREQUEST']._serialized_start = 1230
    _globals['_GETMODELMONITORREQUEST']._serialized_end = 1316
    _globals['_LISTMODELMONITORSREQUEST']._serialized_start = 1319
    _globals['_LISTMODELMONITORSREQUEST']._serialized_end = 1506
    _globals['_LISTMODELMONITORSRESPONSE']._serialized_start = 1508
    _globals['_LISTMODELMONITORSRESPONSE']._serialized_end = 1631
    _globals['_DELETEMODELMONITORREQUEST']._serialized_start = 1633
    _globals['_DELETEMODELMONITORREQUEST']._serialized_end = 1742
    _globals['_CREATEMODELMONITORINGJOBREQUEST']._serialized_start = 1745
    _globals['_CREATEMODELMONITORINGJOBREQUEST']._serialized_end = 1968
    _globals['_GETMODELMONITORINGJOBREQUEST']._serialized_start = 1970
    _globals['_GETMODELMONITORINGJOBREQUEST']._serialized_end = 2068
    _globals['_LISTMODELMONITORINGJOBSREQUEST']._serialized_start = 2071
    _globals['_LISTMODELMONITORINGJOBSREQUEST']._serialized_end = 2269
    _globals['_LISTMODELMONITORINGJOBSRESPONSE']._serialized_start = 2272
    _globals['_LISTMODELMONITORINGJOBSRESPONSE']._serialized_end = 2414
    _globals['_DELETEMODELMONITORINGJOBREQUEST']._serialized_start = 2416
    _globals['_DELETEMODELMONITORINGJOBREQUEST']._serialized_end = 2517
    _globals['_SEARCHMODELMONITORINGSTATSREQUEST']._serialized_start = 2520
    _globals['_SEARCHMODELMONITORINGSTATSREQUEST']._serialized_end = 2800
    _globals['_SEARCHMODELMONITORINGSTATSRESPONSE']._serialized_start = 2803
    _globals['_SEARCHMODELMONITORINGSTATSRESPONSE']._serialized_end = 2945
    _globals['_SEARCHMODELMONITORINGALERTSREQUEST']._serialized_start = 2948
    _globals['_SEARCHMODELMONITORINGALERTSREQUEST']._serialized_end = 3220
    _globals['_SEARCHMODELMONITORINGALERTSRESPONSE']._serialized_start = 3223
    _globals['_SEARCHMODELMONITORINGALERTSRESPONSE']._serialized_end = 3402
    _globals['_MODELMONITORINGSERVICE']._serialized_start = 3405
    _globals['_MODELMONITORINGSERVICE']._serialized_end = 6339