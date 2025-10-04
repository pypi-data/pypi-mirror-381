"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/dataflow/v1beta3/metrics.proto')
_sym_db = _symbol_database.Default()
from ....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ....google.api import client_pb2 as google_dot_api_dot_client__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/dataflow/v1beta3/metrics.proto\x12\x17google.dataflow.v1beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x01\n\x14MetricStructuredName\x12\x0e\n\x06origin\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12K\n\x07context\x18\x03 \x03(\x0b2:.google.dataflow.v1beta3.MetricStructuredName.ContextEntry\x1a.\n\x0cContextEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xe6\x03\n\x0cMetricUpdate\x12;\n\x04name\x18\x01 \x01(\x0b2-.google.dataflow.v1beta3.MetricStructuredName\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x12\n\ncumulative\x18\x03 \x01(\x08\x12&\n\x06scalar\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08mean_sum\x18\x05 \x01(\x0b2\x16.google.protobuf.Value\x12*\n\nmean_count\x18\x06 \x01(\x0b2\x16.google.protobuf.Value\x12#\n\x03set\x18\x07 \x01(\x0b2\x16.google.protobuf.Value\x12$\n\x04trie\x18\r \x01(\x0b2\x16.google.protobuf.Value\x12,\n\x0cdistribution\x18\x0b \x01(\x0b2\x16.google.protobuf.Value\x12%\n\x05gauge\x18\x0c \x01(\x0b2\x16.google.protobuf.Value\x12(\n\x08internal\x18\x08 \x01(\x0b2\x16.google.protobuf.Value\x12/\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.Timestamp"|\n\x14GetJobMetricsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x10\n\x08location\x18\x04 \x01(\t"u\n\nJobMetrics\x12/\n\x0bmetric_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x07metrics\x18\x02 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate"|\n\x1dGetJobExecutionDetailsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"\xb8\x01\n\x12ProgressTimeseries\x12\x18\n\x10current_progress\x18\x01 \x01(\x01\x12F\n\x0bdata_points\x18\x02 \x03(\x0b21.google.dataflow.v1beta3.ProgressTimeseries.Point\x1a@\n\x05Point\x12(\n\x04time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01"\xee\x02\n\rStragglerInfo\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12B\n\x06causes\x18\x02 \x03(\x0b22.google.dataflow.v1beta3.StragglerInfo.CausesEntry\x1a{\n\x16StragglerDebuggingInfo\x12?\n\x07hot_key\x18\x01 \x01(\x0b2,.google.dataflow.v1beta3.HotKeyDebuggingInfoH\x00B \n\x1estraggler_debugging_info_value\x1al\n\x0bCausesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12L\n\x05value\x18\x02 \x01(\x0b2=.google.dataflow.v1beta3.StragglerInfo.StragglerDebuggingInfo:\x028\x01"\xfb\x01\n\x16StreamingStragglerInfo\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x13\n\x0bworker_name\x18\x03 \x01(\t\x125\n\x12data_watermark_lag\x18\x04 \x01(\x0b2\x19.google.protobuf.Duration\x127\n\x14system_watermark_lag\x18\x05 \x01(\x0b2\x19.google.protobuf.Duration"\xb0\x01\n\tStraggler\x12A\n\x0fbatch_straggler\x18\x01 \x01(\x0b2&.google.dataflow.v1beta3.StragglerInfoH\x00\x12N\n\x13streaming_straggler\x18\x02 \x01(\x0b2/.google.dataflow.v1beta3.StreamingStragglerInfoH\x00B\x10\n\x0estraggler_info"\xc6\x02\n\x13HotKeyDebuggingInfo\x12\\\n\x11detected_hot_keys\x18\x01 \x03(\x0b2A.google.dataflow.v1beta3.HotKeyDebuggingInfo.DetectedHotKeysEntry\x1a`\n\nHotKeyInfo\x12.\n\x0bhot_key_age\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x12\x0b\n\x03key\x18\x02 \x01(\t\x12\x15\n\rkey_truncated\x18\x03 \x01(\x08\x1ao\n\x14DetectedHotKeysEntry\x12\x0b\n\x03key\x18\x01 \x01(\x04\x12F\n\x05value\x18\x02 \x01(\x0b27.google.dataflow.v1beta3.HotKeyDebuggingInfo.HotKeyInfo:\x028\x01"\x8f\x02\n\x10StragglerSummary\x12\x1d\n\x15total_straggler_count\x18\x01 \x01(\x03\x12a\n\x15straggler_cause_count\x18\x02 \x03(\x0b2B.google.dataflow.v1beta3.StragglerSummary.StragglerCauseCountEntry\x12=\n\x11recent_stragglers\x18\x03 \x03(\x0b2".google.dataflow.v1beta3.Straggler\x1a:\n\x18StragglerCauseCountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x028\x01"\xf3\x02\n\x0cStageSummary\x12\x10\n\x08stage_id\x18\x01 \x01(\t\x126\n\x05state\x18\x02 \x01(\x0e2\'.google.dataflow.v1beta3.ExecutionState\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12=\n\x08progress\x18\x05 \x01(\x0b2+.google.dataflow.v1beta3.ProgressTimeseries\x126\n\x07metrics\x18\x06 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate\x12D\n\x11straggler_summary\x18\x07 \x01(\x0b2).google.dataflow.v1beta3.StragglerSummary"e\n\x13JobExecutionDetails\x125\n\x06stages\x18\x01 \x03(\x0b2%.google.dataflow.v1beta3.StageSummary\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xee\x01\n\x1fGetStageExecutionDetailsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x12\x10\n\x08location\x18\x03 \x01(\t\x12\x10\n\x08stage_id\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05\x12\x12\n\npage_token\x18\x06 \x01(\t\x12.\n\nstart_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x83\x03\n\x0fWorkItemDetails\x12\x0f\n\x07task_id\x18\x01 \x01(\t\x12\x12\n\nattempt_id\x18\x02 \x01(\t\x12.\n\nstart_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x126\n\x05state\x18\x05 \x01(\x0e2\'.google.dataflow.v1beta3.ExecutionState\x12=\n\x08progress\x18\x06 \x01(\x0b2+.google.dataflow.v1beta3.ProgressTimeseries\x126\n\x07metrics\x18\x07 \x03(\x0b2%.google.dataflow.v1beta3.MetricUpdate\x12>\n\x0estraggler_info\x18\x08 \x01(\x0b2&.google.dataflow.v1beta3.StragglerInfo"b\n\rWorkerDetails\x12\x13\n\x0bworker_name\x18\x01 \x01(\t\x12<\n\nwork_items\x18\x02 \x03(\x0b2(.google.dataflow.v1beta3.WorkItemDetails"i\n\x15StageExecutionDetails\x127\n\x07workers\x18\x01 \x03(\x0b2&.google.dataflow.v1beta3.WorkerDetails\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\xc5\x01\n\x0eExecutionState\x12\x1b\n\x17EXECUTION_STATE_UNKNOWN\x10\x00\x12\x1f\n\x1bEXECUTION_STATE_NOT_STARTED\x10\x01\x12\x1b\n\x17EXECUTION_STATE_RUNNING\x10\x02\x12\x1d\n\x19EXECUTION_STATE_SUCCEEDED\x10\x03\x12\x1a\n\x16EXECUTION_STATE_FAILED\x10\x04\x12\x1d\n\x19EXECUTION_STATE_CANCELLED\x10\x052\xbd\x06\n\x0eMetricsV1Beta3\x12\xe9\x01\n\rGetJobMetrics\x12-.google.dataflow.v1beta3.GetJobMetricsRequest\x1a#.google.dataflow.v1beta3.JobMetrics"\x83\x01\x82\xd3\xe4\x93\x02}\x12F/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/metricsZ3\x121/v1b3/projects/{project_id}/jobs/{job_id}/metrics\x12\xd7\x01\n\x16GetJobExecutionDetails\x126.google.dataflow.v1beta3.GetJobExecutionDetailsRequest\x1a,.google.dataflow.v1beta3.JobExecutionDetails"W\x82\xd3\xe4\x93\x02Q\x12O/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/executionDetails\x12\xef\x01\n\x18GetStageExecutionDetails\x128.google.dataflow.v1beta3.GetStageExecutionDetailsRequest\x1a..google.dataflow.v1beta3.StageExecutionDetails"i\x82\xd3\xe4\x93\x02c\x12a/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/stages/{stage_id}/executionDetails\x1as\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/computeB\xcf\x01\n\x1bcom.google.dataflow.v1beta3B\x0cMetricsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.dataflow.v1beta3.metrics_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.dataflow.v1beta3B\x0cMetricsProtoP\x01Z=cloud.google.com/go/dataflow/apiv1beta3/dataflowpb;dataflowpb\xaa\x02\x1dGoogle.Cloud.Dataflow.V1Beta3\xca\x02\x1dGoogle\\Cloud\\Dataflow\\V1beta3\xea\x02 Google::Cloud::Dataflow::V1beta3'
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._loaded_options = None
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_options = b'8\x01'
    _globals['_STRAGGLERINFO_CAUSESENTRY']._loaded_options = None
    _globals['_STRAGGLERINFO_CAUSESENTRY']._serialized_options = b'8\x01'
    _globals['_HOTKEYDEBUGGINGINFO_DETECTEDHOTKEYSENTRY']._loaded_options = None
    _globals['_HOTKEYDEBUGGINGINFO_DETECTEDHOTKEYSENTRY']._serialized_options = b'8\x01'
    _globals['_STRAGGLERSUMMARY_STRAGGLERCAUSECOUNTENTRY']._loaded_options = None
    _globals['_STRAGGLERSUMMARY_STRAGGLERCAUSECOUNTENTRY']._serialized_options = b'8\x01'
    _globals['_METRICSV1BETA3']._loaded_options = None
    _globals['_METRICSV1BETA3']._serialized_options = b'\xcaA\x17dataflow.googleapis.com\xd2AVhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/compute'
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobMetrics']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobMetrics']._serialized_options = b'\x82\xd3\xe4\x93\x02}\x12F/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/metricsZ3\x121/v1b3/projects/{project_id}/jobs/{job_id}/metrics'
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobExecutionDetails']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetJobExecutionDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02Q\x12O/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/executionDetails'
    _globals['_METRICSV1BETA3'].methods_by_name['GetStageExecutionDetails']._loaded_options = None
    _globals['_METRICSV1BETA3'].methods_by_name['GetStageExecutionDetails']._serialized_options = b'\x82\xd3\xe4\x93\x02c\x12a/v1b3/projects/{project_id}/locations/{location}/jobs/{job_id}/stages/{stage_id}/executionDetails'
    _globals['_EXECUTIONSTATE']._serialized_start = 4164
    _globals['_EXECUTIONSTATE']._serialized_end = 4361
    _globals['_METRICSTRUCTUREDNAME']._serialized_start = 217
    _globals['_METRICSTRUCTUREDNAME']._serialized_end = 394
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_start = 348
    _globals['_METRICSTRUCTUREDNAME_CONTEXTENTRY']._serialized_end = 394
    _globals['_METRICUPDATE']._serialized_start = 397
    _globals['_METRICUPDATE']._serialized_end = 883
    _globals['_GETJOBMETRICSREQUEST']._serialized_start = 885
    _globals['_GETJOBMETRICSREQUEST']._serialized_end = 1009
    _globals['_JOBMETRICS']._serialized_start = 1011
    _globals['_JOBMETRICS']._serialized_end = 1128
    _globals['_GETJOBEXECUTIONDETAILSREQUEST']._serialized_start = 1130
    _globals['_GETJOBEXECUTIONDETAILSREQUEST']._serialized_end = 1254
    _globals['_PROGRESSTIMESERIES']._serialized_start = 1257
    _globals['_PROGRESSTIMESERIES']._serialized_end = 1441
    _globals['_PROGRESSTIMESERIES_POINT']._serialized_start = 1377
    _globals['_PROGRESSTIMESERIES_POINT']._serialized_end = 1441
    _globals['_STRAGGLERINFO']._serialized_start = 1444
    _globals['_STRAGGLERINFO']._serialized_end = 1810
    _globals['_STRAGGLERINFO_STRAGGLERDEBUGGINGINFO']._serialized_start = 1577
    _globals['_STRAGGLERINFO_STRAGGLERDEBUGGINGINFO']._serialized_end = 1700
    _globals['_STRAGGLERINFO_CAUSESENTRY']._serialized_start = 1702
    _globals['_STRAGGLERINFO_CAUSESENTRY']._serialized_end = 1810
    _globals['_STREAMINGSTRAGGLERINFO']._serialized_start = 1813
    _globals['_STREAMINGSTRAGGLERINFO']._serialized_end = 2064
    _globals['_STRAGGLER']._serialized_start = 2067
    _globals['_STRAGGLER']._serialized_end = 2243
    _globals['_HOTKEYDEBUGGINGINFO']._serialized_start = 2246
    _globals['_HOTKEYDEBUGGINGINFO']._serialized_end = 2572
    _globals['_HOTKEYDEBUGGINGINFO_HOTKEYINFO']._serialized_start = 2363
    _globals['_HOTKEYDEBUGGINGINFO_HOTKEYINFO']._serialized_end = 2459
    _globals['_HOTKEYDEBUGGINGINFO_DETECTEDHOTKEYSENTRY']._serialized_start = 2461
    _globals['_HOTKEYDEBUGGINGINFO_DETECTEDHOTKEYSENTRY']._serialized_end = 2572
    _globals['_STRAGGLERSUMMARY']._serialized_start = 2575
    _globals['_STRAGGLERSUMMARY']._serialized_end = 2846
    _globals['_STRAGGLERSUMMARY_STRAGGLERCAUSECOUNTENTRY']._serialized_start = 2788
    _globals['_STRAGGLERSUMMARY_STRAGGLERCAUSECOUNTENTRY']._serialized_end = 2846
    _globals['_STAGESUMMARY']._serialized_start = 2849
    _globals['_STAGESUMMARY']._serialized_end = 3220
    _globals['_JOBEXECUTIONDETAILS']._serialized_start = 3222
    _globals['_JOBEXECUTIONDETAILS']._serialized_end = 3323
    _globals['_GETSTAGEEXECUTIONDETAILSREQUEST']._serialized_start = 3326
    _globals['_GETSTAGEEXECUTIONDETAILSREQUEST']._serialized_end = 3564
    _globals['_WORKITEMDETAILS']._serialized_start = 3567
    _globals['_WORKITEMDETAILS']._serialized_end = 3954
    _globals['_WORKERDETAILS']._serialized_start = 3956
    _globals['_WORKERDETAILS']._serialized_end = 4054
    _globals['_STAGEEXECUTIONDETAILS']._serialized_start = 4056
    _globals['_STAGEEXECUTIONDETAILS']._serialized_end = 4161
    _globals['_METRICSV1BETA3']._serialized_start = 4364
    _globals['_METRICSV1BETA3']._serialized_end = 5193