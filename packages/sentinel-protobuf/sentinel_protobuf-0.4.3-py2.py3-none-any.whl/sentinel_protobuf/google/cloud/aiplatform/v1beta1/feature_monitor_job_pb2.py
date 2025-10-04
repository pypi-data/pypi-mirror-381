"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature_monitor_job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitor_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitor__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1beta1/feature_monitor_job.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/feature_monitor.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xd8\t\n\x11FeatureMonitorJob\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12-\n\x0cfinal_status\x18\x03 \x01(\x0b2\x12.google.rpc.StatusB\x03\xe0A\x03\x12W\n\x0bjob_summary\x18\x04 \x01(\x0b2=.google.cloud.aiplatform.v1beta1.FeatureMonitorJob.JobSummaryB\x03\xe0A\x03\x12S\n\x06labels\x18\x05 \x03(\x0b2>.google.cloud.aiplatform.v1beta1.FeatureMonitorJob.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12.\n!drift_base_feature_monitor_job_id\x18\x07 \x01(\x03B\x03\xe0A\x03\x12A\n\x18drift_base_snapshot_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12^\n\x18feature_selection_config\x18\t \x01(\x0b27.google.cloud.aiplatform.v1beta1.FeatureSelectionConfigB\x03\xe0A\x03\x12f\n\x0ctrigger_type\x18\n \x01(\x0e2K.google.cloud.aiplatform.v1beta1.FeatureMonitorJob.FeatureMonitorJobTriggerB\x03\xe0A\x03\x1a\x8b\x01\n\nJobSummary\x12\x1a\n\rtotal_slot_ms\x18\x01 \x01(\x03B\x03\xe0A\x03\x12a\n\x1bfeature_stats_and_anomalies\x18\x02 \x03(\x0b27.google.cloud.aiplatform.v1beta1.FeatureStatsAndAnomalyB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9c\x01\n\x18FeatureMonitorJobTrigger\x12+\n\'FEATURE_MONITOR_JOB_TRIGGER_UNSPECIFIED\x10\x00\x12(\n$FEATURE_MONITOR_JOB_TRIGGER_PERIODIC\x10\x01\x12)\n%FEATURE_MONITOR_JOB_TRIGGER_ON_DEMAND\x10\x02:\xeb\x01\xeaA\xe7\x01\n+aiplatform.googleapis.com/FeatureMonitorJob\x12\x90\x01projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}*\x12featureMonitorJobs2\x11featureMonitorJobB\xed\x01\n#com.google.cloud.aiplatform.v1beta1B\x16FeatureMonitorJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_monitor_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x16FeatureMonitorJobProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATUREMONITORJOB_JOBSUMMARY'].fields_by_name['total_slot_ms']._loaded_options = None
    _globals['_FEATUREMONITORJOB_JOBSUMMARY'].fields_by_name['total_slot_ms']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB_JOBSUMMARY'].fields_by_name['feature_stats_and_anomalies']._loaded_options = None
    _globals['_FEATUREMONITORJOB_JOBSUMMARY'].fields_by_name['feature_stats_and_anomalies']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB_LABELSENTRY']._loaded_options = None
    _globals['_FEATUREMONITORJOB_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREMONITORJOB'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREMONITORJOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['final_status']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['final_status']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['job_summary']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['job_summary']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITORJOB'].fields_by_name['description']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITORJOB'].fields_by_name['drift_base_feature_monitor_job_id']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['drift_base_feature_monitor_job_id']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['drift_base_snapshot_time']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['drift_base_snapshot_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['feature_selection_config']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['feature_selection_config']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB'].fields_by_name['trigger_type']._loaded_options = None
    _globals['_FEATUREMONITORJOB'].fields_by_name['trigger_type']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITORJOB']._loaded_options = None
    _globals['_FEATUREMONITORJOB']._serialized_options = b'\xeaA\xe7\x01\n+aiplatform.googleapis.com/FeatureMonitorJob\x12\x90\x01projects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}/featureMonitorJobs/{feature_monitor_job}*\x12featureMonitorJobs2\x11featureMonitorJob'
    _globals['_FEATUREMONITORJOB']._serialized_start = 268
    _globals['_FEATUREMONITORJOB']._serialized_end = 1508
    _globals['_FEATUREMONITORJOB_JOBSUMMARY']._serialized_start = 925
    _globals['_FEATUREMONITORJOB_JOBSUMMARY']._serialized_end = 1064
    _globals['_FEATUREMONITORJOB_LABELSENTRY']._serialized_start = 1066
    _globals['_FEATUREMONITORJOB_LABELSENTRY']._serialized_end = 1111
    _globals['_FEATUREMONITORJOB_FEATUREMONITORJOBTRIGGER']._serialized_start = 1114
    _globals['_FEATUREMONITORJOB_FEATUREMONITORJOBTRIGGER']._serialized_end = 1270