"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature_monitor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1beta1/feature_monitor.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/interval.proto"\xa7\x05\n\x0eFeatureMonitor\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01\x12P\n\x06labels\x18\x05 \x03(\x0b2;.google.cloud.aiplatform.v1beta1.FeatureMonitor.LabelsEntryB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12M\n\x0fschedule_config\x18\x07 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.ScheduleConfigB\x03\xe0A\x02\x12^\n\x18feature_selection_config\x18\x08 \x01(\x0b27.google.cloud.aiplatform.v1beta1.FeatureSelectionConfigB\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xb8\x01\xeaA\xb4\x01\n(aiplatform.googleapis.com/FeatureMonitor\x12gprojects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}*\x0ffeatureMonitors2\x0efeatureMonitor"\x1e\n\x0eScheduleConfig\x12\x0c\n\x04cron\x18\x01 \x01(\t"\xc5\x01\n\x16FeatureSelectionConfig\x12c\n\x0ffeature_configs\x18\x01 \x03(\x0b2E.google.cloud.aiplatform.v1beta1.FeatureSelectionConfig.FeatureConfigB\x03\xe0A\x01\x1aF\n\rFeatureConfig\x12\x17\n\nfeature_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0fdrift_threshold\x18\x02 \x01(\x01B\x03\xe0A\x01"\xa2\x02\n\x16FeatureStatsAndAnomaly\x12\x12\n\nfeature_id\x18\x01 \x01(\t\x12-\n\rfeature_stats\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x12\x1e\n\x16distribution_deviation\x18\x03 \x01(\x01\x12!\n\x19drift_detection_threshold\x18\x04 \x01(\x01\x12\x16\n\x0edrift_detected\x18\x05 \x01(\x08\x12.\n\nstats_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1e\n\x16feature_monitor_job_id\x18\x07 \x01(\x03\x12\x1a\n\x12feature_monitor_id\x18\x08 \x01(\t"\x8f\x01\n\x1aFeatureStatsAndAnomalySpec\x12$\n\x12latest_stats_count\x18\x01 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01\x124\n\x10stats_time_range\x18\x02 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x01B\x15\n\x13_latest_stats_countB\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13FeatureMonitorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_monitor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13FeatureMonitorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATUREMONITOR_LABELSENTRY']._loaded_options = None
    _globals['_FEATUREMONITOR_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREMONITOR'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREMONITOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREMONITOR'].fields_by_name['etag']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITOR'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITOR'].fields_by_name['description']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITOR'].fields_by_name['schedule_config']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['schedule_config']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREMONITOR'].fields_by_name['feature_selection_config']._loaded_options = None
    _globals['_FEATUREMONITOR'].fields_by_name['feature_selection_config']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREMONITOR']._loaded_options = None
    _globals['_FEATUREMONITOR']._serialized_options = b'\xeaA\xb4\x01\n(aiplatform.googleapis.com/FeatureMonitor\x12gprojects/{project}/locations/{location}/featureGroups/{feature_group}/featureMonitors/{feature_monitor}*\x0ffeatureMonitors2\x0efeatureMonitor'
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG'].fields_by_name['feature_id']._loaded_options = None
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG'].fields_by_name['feature_id']._serialized_options = b'\xe0A\x02'
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG'].fields_by_name['drift_threshold']._loaded_options = None
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG'].fields_by_name['drift_threshold']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESELECTIONCONFIG'].fields_by_name['feature_configs']._loaded_options = None
    _globals['_FEATURESELECTIONCONFIG'].fields_by_name['feature_configs']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTATSANDANOMALYSPEC'].fields_by_name['latest_stats_count']._loaded_options = None
    _globals['_FEATURESTATSANDANOMALYSPEC'].fields_by_name['latest_stats_count']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURESTATSANDANOMALYSPEC'].fields_by_name['stats_time_range']._loaded_options = None
    _globals['_FEATURESTATSANDANOMALYSPEC'].fields_by_name['stats_time_range']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREMONITOR']._serialized_start = 242
    _globals['_FEATUREMONITOR']._serialized_end = 921
    _globals['_FEATUREMONITOR_LABELSENTRY']._serialized_start = 689
    _globals['_FEATUREMONITOR_LABELSENTRY']._serialized_end = 734
    _globals['_SCHEDULECONFIG']._serialized_start = 923
    _globals['_SCHEDULECONFIG']._serialized_end = 953
    _globals['_FEATURESELECTIONCONFIG']._serialized_start = 956
    _globals['_FEATURESELECTIONCONFIG']._serialized_end = 1153
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG']._serialized_start = 1083
    _globals['_FEATURESELECTIONCONFIG_FEATURECONFIG']._serialized_end = 1153
    _globals['_FEATURESTATSANDANOMALY']._serialized_start = 1156
    _globals['_FEATURESTATSANDANOMALY']._serialized_end = 1446
    _globals['_FEATURESTATSANDANOMALYSPEC']._serialized_start = 1449
    _globals['_FEATURESTATSANDANOMALYSPEC']._serialized_end = 1592