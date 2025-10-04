"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitor_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitor__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_monitoring_stats_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__monitoring__stats__pb2
from .....google.cloud.aiplatform.v1beta1 import featurestore_monitoring_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_featurestore__monitoring__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/feature.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/feature_monitor.proto\x1a>google/cloud/aiplatform/v1beta1/feature_monitoring_stats.proto\x1a=google/cloud/aiplatform/v1beta1/featurestore_monitoring.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x0c\n\x07Feature\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x13\n\x0bdescription\x18\x02 \x01(\t\x12K\n\nvalue_type\x18\x03 \x01(\x0e22.google.cloud.aiplatform.v1beta1.Feature.ValueTypeB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x06labels\x18\x06 \x03(\x0b24.google.cloud.aiplatform.v1beta1.Feature.LabelsEntryB\x03\xe0A\x01\x12\x0c\n\x04etag\x18\x07 \x01(\t\x12_\n\x11monitoring_config\x18\t \x01(\x0b2=.google.cloud.aiplatform.v1beta1.FeaturestoreMonitoringConfigB\x05\x18\x01\xe0A\x01\x12\x1f\n\x12disable_monitoring\x18\x0c \x01(\x08B\x03\xe0A\x01\x12S\n\x10monitoring_stats\x18\n \x03(\x0b24.google.cloud.aiplatform.v1beta1.FeatureStatsAnomalyB\x03\xe0A\x03\x12h\n\x1amonitoring_stats_anomalies\x18\x0b \x03(\x0b2?.google.cloud.aiplatform.v1beta1.Feature.MonitoringStatsAnomalyB\x03\xe0A\x03\x12_\n\x19feature_stats_and_anomaly\x18\r \x03(\x0b27.google.cloud.aiplatform.v1beta1.FeatureStatsAndAnomalyB\x03\xe0A\x03\x12\x1b\n\x13version_column_name\x18j \x01(\t\x12\x18\n\x10point_of_contact\x18k \x01(\t\x1a\xb1\x02\n\x16MonitoringStatsAnomaly\x12a\n\tobjective\x18\x01 \x01(\x0e2I.google.cloud.aiplatform.v1beta1.Feature.MonitoringStatsAnomaly.ObjectiveB\x03\xe0A\x03\x12X\n\x15feature_stats_anomaly\x18\x02 \x01(\x0b24.google.cloud.aiplatform.v1beta1.FeatureStatsAnomalyB\x03\xe0A\x03"Z\n\tObjective\x12\x19\n\x15OBJECTIVE_UNSPECIFIED\x10\x00\x12\x1b\n\x17IMPORT_FEATURE_ANALYSIS\x10\x01\x12\x15\n\x11SNAPSHOT_ANALYSIS\x10\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xb0\x01\n\tValueType\x12\x1a\n\x16VALUE_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04BOOL\x10\x01\x12\x0e\n\nBOOL_ARRAY\x10\x02\x12\n\n\x06DOUBLE\x10\x03\x12\x10\n\x0cDOUBLE_ARRAY\x10\x04\x12\t\n\x05INT64\x10\t\x12\x0f\n\x0bINT64_ARRAY\x10\n\x12\n\n\x06STRING\x10\x0b\x12\x10\n\x0cSTRING_ARRAY\x10\x0c\x12\t\n\x05BYTES\x10\r\x12\n\n\x06STRUCT\x10\x0e:\x87\x02\xeaA\x83\x02\n!aiplatform.googleapis.com/Feature\x12qprojects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}\x12Xprojects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}*\x08features2\x07featureB\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cFeatureProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cFeatureProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FEATURE_MONITORINGSTATSANOMALY'].fields_by_name['objective']._loaded_options = None
    _globals['_FEATURE_MONITORINGSTATSANOMALY'].fields_by_name['objective']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE_MONITORINGSTATSANOMALY'].fields_by_name['feature_stats_anomaly']._loaded_options = None
    _globals['_FEATURE_MONITORINGSTATSANOMALY'].fields_by_name['feature_stats_anomaly']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE_LABELSENTRY']._loaded_options = None
    _globals['_FEATURE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATURE'].fields_by_name['name']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_FEATURE'].fields_by_name['value_type']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['value_type']._serialized_options = b'\xe0A\x05'
    _globals['_FEATURE'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURE'].fields_by_name['monitoring_config']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['monitoring_config']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_FEATURE'].fields_by_name['disable_monitoring']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['disable_monitoring']._serialized_options = b'\xe0A\x01'
    _globals['_FEATURE'].fields_by_name['monitoring_stats']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['monitoring_stats']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['monitoring_stats_anomalies']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['monitoring_stats_anomalies']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE'].fields_by_name['feature_stats_and_anomaly']._loaded_options = None
    _globals['_FEATURE'].fields_by_name['feature_stats_and_anomaly']._serialized_options = b'\xe0A\x03'
    _globals['_FEATURE']._loaded_options = None
    _globals['_FEATURE']._serialized_options = b'\xeaA\x83\x02\n!aiplatform.googleapis.com/Feature\x12qprojects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}/features/{feature}\x12Xprojects/{project}/locations/{location}/featureGroups/{feature_group}/features/{feature}*\x08features2\x07feature'
    _globals['_FEATURE']._serialized_start = 358
    _globals['_FEATURE']._serialized_end = 1954
    _globals['_FEATURE_MONITORINGSTATSANOMALY']._serialized_start = 1157
    _globals['_FEATURE_MONITORINGSTATSANOMALY']._serialized_end = 1462
    _globals['_FEATURE_MONITORINGSTATSANOMALY_OBJECTIVE']._serialized_start = 1372
    _globals['_FEATURE_MONITORINGSTATSANOMALY_OBJECTIVE']._serialized_end = 1462
    _globals['_FEATURE_LABELSENTRY']._serialized_start = 1464
    _globals['_FEATURE_LABELSENTRY']._serialized_end = 1509
    _globals['_FEATURE_VALUETYPE']._serialized_start = 1512
    _globals['_FEATURE_VALUETYPE']._serialized_end = 1688