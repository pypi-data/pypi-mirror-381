"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_monitoring_spec.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_alert_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__alert__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/aiplatform/v1beta1/model_monitoring_spec.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x19google/api/resource.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a7google/cloud/aiplatform/v1beta1/machine_resources.proto\x1a<google/cloud/aiplatform/v1beta1/model_monitoring_alert.proto\x1a\x1agoogle/type/interval.proto"\x9a\x02\n\x13ModelMonitoringSpec\x12U\n\x0eobjective_spec\x18\x01 \x01(\x0b2=.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec\x12[\n\x11notification_spec\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ModelMonitoringNotificationSpec\x12O\n\x0boutput_spec\x18\x03 \x01(\x0b2:.google.cloud.aiplatform.v1beta1.ModelMonitoringOutputSpec"\xbb\x0e\n\x1cModelMonitoringObjectiveSpec\x12k\n\x11tabular_objective\x18\x01 \x01(\x0b2N.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.TabularObjectiveH\x00\x12J\n\x10explanation_spec\x18\x03 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x12O\n\x10baseline_dataset\x18\x04 \x01(\x0b25.google.cloud.aiplatform.v1beta1.ModelMonitoringInput\x12M\n\x0etarget_dataset\x18\x05 \x01(\x0b25.google.cloud.aiplatform.v1beta1.ModelMonitoringInput\x1a\xc0\x04\n\rDataDriftSpec\x12\x10\n\x08features\x18\x01 \x03(\t\x12\x1f\n\x17categorical_metric_type\x18\x02 \x01(\t\x12\x1b\n\x13numeric_metric_type\x18\x03 \x01(\t\x12k\n#default_categorical_alert_condition\x18\x04 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertCondition\x12g\n\x1fdefault_numeric_alert_condition\x18\x05 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertCondition\x12\x89\x01\n\x18feature_alert_conditions\x18\x06 \x03(\x0b2g.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.DataDriftSpec.FeatureAlertConditionsEntry\x1a}\n\x1bFeatureAlertConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertCondition:\x028\x01\x1a\x88\x04\n\x16FeatureAttributionSpec\x12\x10\n\x08features\x18\x01 \x03(\t\x12_\n\x17default_alert_condition\x18\x02 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertCondition\x12\x92\x01\n\x18feature_alert_conditions\x18\x03 \x03(\x0b2p.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.FeatureAttributionSpec.FeatureAlertConditionsEntry\x12g\n%batch_explanation_dedicated_resources\x18\x04 \x01(\x0b28.google.cloud.aiplatform.v1beta1.BatchDedicatedResources\x1a}\n\x1bFeatureAlertConditionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12M\n\x05value\x18\x02 \x01(\x0b2>.google.cloud.aiplatform.v1beta1.ModelMonitoringAlertCondition:\x028\x01\x1a\xe6\x02\n\x10TabularObjective\x12g\n\x12feature_drift_spec\x18\n \x01(\x0b2K.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.DataDriftSpec\x12q\n\x1cprediction_output_drift_spec\x18\x0b \x01(\x0b2K.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.DataDriftSpec\x12v\n\x18feature_attribution_spec\x18\x0c \x01(\x0b2T.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.FeatureAttributionSpecB\x0b\n\tobjective"h\n\x19ModelMonitoringOutputSpec\x12K\n\x12gcs_base_directory\x18\x01 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestination"\xc7\x0b\n\x14ModelMonitoringInput\x12j\n\x12columnized_dataset\x18\x01 \x01(\x0b2L.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDatasetH\x00\x12n\n\x17batch_prediction_output\x18\x02 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.BatchPredictionOutputH\x00\x12h\n\x14vertex_endpoint_logs\x18\x03 \x01(\x0b2H.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.VertexEndpointLogsH\x00\x12.\n\rtime_interval\x18\x06 \x01(\x0b2\x15.google.type.IntervalH\x01\x12W\n\x0btime_offset\x18\x07 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.TimeOffsetH\x01\x1a\xdd\x05\n\x16ModelMonitoringDataset\x12@\n\x0evertex_dataset\x18\x01 \x01(\tB&\xfaA#\n!aiplatform.googleapis.com/DatasetH\x00\x12{\n\ngcs_source\x18\x02 \x01(\x0b2e.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSourceH\x00\x12\x85\x01\n\x0fbigquery_source\x18\x06 \x01(\x0b2j.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringBigQuerySourceH\x00\x12\x17\n\x0ftimestamp_field\x18\x07 \x01(\t\x1a\xfc\x01\n\x18ModelMonitoringGcsSource\x12\x0f\n\x07gcs_uri\x18\x01 \x01(\t\x12\x80\x01\n\x06format\x18\x02 \x01(\x0e2p.google.cloud.aiplatform.v1beta1.ModelMonitoringInput.ModelMonitoringDataset.ModelMonitoringGcsSource.DataFormat"L\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x07\n\x03CSV\x10\x01\x12\r\n\tTF_RECORD\x10\x02\x12\t\n\x05JSONL\x10\x03\x1aS\n\x1dModelMonitoringBigQuerySource\x12\x13\n\ttable_uri\x18\x01 \x01(\tH\x00\x12\x0f\n\x05query\x18\x02 \x01(\tH\x00B\x0c\n\nconnectionB\x0f\n\rdata_location\x1ah\n\x15BatchPredictionOutput\x12O\n\x14batch_prediction_job\x18\x01 \x01(\tB1\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob\x1aP\n\x12VertexEndpointLogs\x12:\n\tendpoints\x18\x01 \x03(\tB\'\xfaA$\n"aiplatform.googleapis.com/Endpoint\x1a,\n\nTimeOffset\x12\x0e\n\x06offset\x18\x01 \x01(\t\x12\x0e\n\x06window\x18\x02 \x01(\tB\t\n\x07datasetB\x0b\n\ttime_spec"\x85\x03\n\x1fModelMonitoringNotificationSpec\x12b\n\x0cemail_config\x18\x01 \x01(\x0b2L.google.cloud.aiplatform.v1beta1.ModelMonitoringNotificationSpec.EmailConfig\x12\x1c\n\x14enable_cloud_logging\x18\x02 \x01(\x08\x12\x80\x01\n\x1cnotification_channel_configs\x18\x03 \x03(\x0b2Z.google.cloud.aiplatform.v1beta1.ModelMonitoringNotificationSpec.NotificationChannelConfig\x1a"\n\x0bEmailConfig\x12\x13\n\x0buser_emails\x18\x01 \x03(\t\x1a9\n\x19NotificationChannelConfig\x12\x1c\n\x14notification_channel\x18\x01 \x01(\tB\xef\x01\n#com.google.cloud.aiplatform.v1beta1B\x18ModelMonitoringSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitoring_spec_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x18ModelMonitoringSpecProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC_FEATUREALERTCONDITIONSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC_FEATUREALERTCONDITIONSENTRY']._loaded_options = None
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_options = b'8\x01'
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET'].fields_by_name['vertex_dataset']._loaded_options = None
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET'].fields_by_name['vertex_dataset']._serialized_options = b'\xfaA#\n!aiplatform.googleapis.com/Dataset'
    _globals['_MODELMONITORINGINPUT_BATCHPREDICTIONOUTPUT'].fields_by_name['batch_prediction_job']._loaded_options = None
    _globals['_MODELMONITORINGINPUT_BATCHPREDICTIONOUTPUT'].fields_by_name['batch_prediction_job']._serialized_options = b'\xfaA.\n,aiplatform.googleapis.com/BatchPredictionJob'
    _globals['_MODELMONITORINGINPUT_VERTEXENDPOINTLOGS'].fields_by_name['endpoints']._loaded_options = None
    _globals['_MODELMONITORINGINPUT_VERTEXENDPOINTLOGS'].fields_by_name['endpoints']._serialized_options = b'\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_MODELMONITORINGSPEC']._serialized_start = 364
    _globals['_MODELMONITORINGSPEC']._serialized_end = 646
    _globals['_MODELMONITORINGOBJECTIVESPEC']._serialized_start = 649
    _globals['_MODELMONITORINGOBJECTIVESPEC']._serialized_end = 2500
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC']._serialized_start = 1027
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC']._serialized_end = 1603
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_start = 1478
    _globals['_MODELMONITORINGOBJECTIVESPEC_DATADRIFTSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_end = 1603
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC']._serialized_start = 1606
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC']._serialized_end = 2126
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_start = 1478
    _globals['_MODELMONITORINGOBJECTIVESPEC_FEATUREATTRIBUTIONSPEC_FEATUREALERTCONDITIONSENTRY']._serialized_end = 1603
    _globals['_MODELMONITORINGOBJECTIVESPEC_TABULAROBJECTIVE']._serialized_start = 2129
    _globals['_MODELMONITORINGOBJECTIVESPEC_TABULAROBJECTIVE']._serialized_end = 2487
    _globals['_MODELMONITORINGOUTPUTSPEC']._serialized_start = 2502
    _globals['_MODELMONITORINGOUTPUTSPEC']._serialized_end = 2606
    _globals['_MODELMONITORINGINPUT']._serialized_start = 2609
    _globals['_MODELMONITORINGINPUT']._serialized_end = 4088
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET']._serialized_start = 3097
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET']._serialized_end = 3830
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGGCSSOURCE']._serialized_start = 3476
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGGCSSOURCE']._serialized_end = 3728
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGGCSSOURCE_DATAFORMAT']._serialized_start = 3652
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGGCSSOURCE_DATAFORMAT']._serialized_end = 3728
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGBIGQUERYSOURCE']._serialized_start = 3730
    _globals['_MODELMONITORINGINPUT_MODELMONITORINGDATASET_MODELMONITORINGBIGQUERYSOURCE']._serialized_end = 3813
    _globals['_MODELMONITORINGINPUT_BATCHPREDICTIONOUTPUT']._serialized_start = 3832
    _globals['_MODELMONITORINGINPUT_BATCHPREDICTIONOUTPUT']._serialized_end = 3936
    _globals['_MODELMONITORINGINPUT_VERTEXENDPOINTLOGS']._serialized_start = 3938
    _globals['_MODELMONITORINGINPUT_VERTEXENDPOINTLOGS']._serialized_end = 4018
    _globals['_MODELMONITORINGINPUT_TIMEOFFSET']._serialized_start = 4020
    _globals['_MODELMONITORINGINPUT_TIMEOFFSET']._serialized_end = 4064
    _globals['_MODELMONITORINGNOTIFICATIONSPEC']._serialized_start = 4091
    _globals['_MODELMONITORINGNOTIFICATIONSPEC']._serialized_end = 4480
    _globals['_MODELMONITORINGNOTIFICATIONSPEC_EMAILCONFIG']._serialized_start = 4387
    _globals['_MODELMONITORINGNOTIFICATIONSPEC_EMAILCONFIG']._serialized_end = 4421
    _globals['_MODELMONITORINGNOTIFICATIONSPEC_NOTIFICATIONCHANNELCONFIG']._serialized_start = 4423
    _globals['_MODELMONITORINGNOTIFICATIONSPEC_NOTIFICATIONCHANNELCONFIG']._serialized_end = 4480