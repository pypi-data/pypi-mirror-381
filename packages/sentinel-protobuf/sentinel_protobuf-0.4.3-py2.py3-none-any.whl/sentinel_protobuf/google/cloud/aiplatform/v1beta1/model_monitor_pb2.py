"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/model_monitor.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import encryption_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_encryption__spec__pb2
from .....google.cloud.aiplatform.v1beta1 import explanation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_explanation__pb2
from .....google.cloud.aiplatform.v1beta1 import model_monitoring_spec_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_model__monitoring__spec__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/aiplatform/v1beta1/model_monitor.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1beta1/encryption_spec.proto\x1a1google/cloud/aiplatform/v1beta1/explanation.proto\x1a;google/cloud/aiplatform/v1beta1/model_monitoring_spec.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\n\n\x0cModelMonitor\x12k\n\x11tabular_objective\x18\x0b \x01(\x0b2N.google.cloud.aiplatform.v1beta1.ModelMonitoringObjectiveSpec.TabularObjectiveH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12d\n\x17model_monitoring_target\x18\x03 \x01(\x0b2C.google.cloud.aiplatform.v1beta1.ModelMonitor.ModelMonitoringTarget\x12O\n\x10training_dataset\x18\n \x01(\x0b25.google.cloud.aiplatform.v1beta1.ModelMonitoringInput\x12[\n\x11notification_spec\x18\x0c \x01(\x0b2@.google.cloud.aiplatform.v1beta1.ModelMonitoringNotificationSpec\x12O\n\x0boutput_spec\x18\r \x01(\x0b2:.google.cloud.aiplatform.v1beta1.ModelMonitoringOutputSpec\x12J\n\x10explanation_spec\x18\x10 \x01(\x0b20.google.cloud.aiplatform.v1beta1.ExplanationSpec\x12W\n\x17model_monitoring_schema\x18\t \x01(\x0b26.google.cloud.aiplatform.v1beta1.ModelMonitoringSchema\x12H\n\x0fencryption_spec\x18\x05 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.EncryptionSpec\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x11 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x12 \x01(\x08B\x03\xe0A\x03\x1a\xf4\x01\n\x15ModelMonitoringTarget\x12m\n\x0cvertex_model\x18\x01 \x01(\x0b2U.google.cloud.aiplatform.v1beta1.ModelMonitor.ModelMonitoringTarget.VertexModelSourceH\x00\x1ab\n\x11VertexModelSource\x123\n\x05model\x18\x01 \x01(\tB$\xfaA!\n\x1faiplatform.googleapis.com/Model\x12\x18\n\x10model_version_id\x18\x02 \x01(\tB\x08\n\x06source:r\xeaAo\n&aiplatform.googleapis.com/ModelMonitor\x12Eprojects/{project}/locations/{location}/modelMonitors/{model_monitor}B\x13\n\x11default_objective"\xf5\x02\n\x15ModelMonitoringSchema\x12Z\n\x0efeature_fields\x18\x01 \x03(\x0b2B.google.cloud.aiplatform.v1beta1.ModelMonitoringSchema.FieldSchema\x12]\n\x11prediction_fields\x18\x02 \x03(\x0b2B.google.cloud.aiplatform.v1beta1.ModelMonitoringSchema.FieldSchema\x12_\n\x13ground_truth_fields\x18\x03 \x03(\x0b2B.google.cloud.aiplatform.v1beta1.ModelMonitoringSchema.FieldSchema\x1a@\n\x0bFieldSchema\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tdata_type\x18\x02 \x01(\t\x12\x10\n\x08repeated\x18\x03 \x01(\x08B\xe8\x01\n#com.google.cloud.aiplatform.v1beta1B\x11ModelMonitorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.model_monitor_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x11ModelMonitorProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_MODELMONITOR_MODELMONITORINGTARGET_VERTEXMODELSOURCE'].fields_by_name['model']._loaded_options = None
    _globals['_MODELMONITOR_MODELMONITORINGTARGET_VERTEXMODELSOURCE'].fields_by_name['model']._serialized_options = b'\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_MODELMONITOR'].fields_by_name['name']._loaded_options = None
    _globals['_MODELMONITOR'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_MODELMONITOR'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODELMONITOR'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITOR'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODELMONITOR'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITOR'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_MODELMONITOR'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITOR'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_MODELMONITOR'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_MODELMONITOR']._loaded_options = None
    _globals['_MODELMONITOR']._serialized_options = b'\xeaAo\n&aiplatform.googleapis.com/ModelMonitor\x12Eprojects/{project}/locations/{location}/modelMonitors/{model_monitor}'
    _globals['_MODELMONITOR']._serialized_start = 349
    _globals['_MODELMONITOR']._serialized_end = 1657
    _globals['_MODELMONITOR_MODELMONITORINGTARGET']._serialized_start = 1276
    _globals['_MODELMONITOR_MODELMONITORINGTARGET']._serialized_end = 1520
    _globals['_MODELMONITOR_MODELMONITORINGTARGET_VERTEXMODELSOURCE']._serialized_start = 1412
    _globals['_MODELMONITOR_MODELMONITORINGTARGET_VERTEXMODELSOURCE']._serialized_end = 1510
    _globals['_MODELMONITORINGSCHEMA']._serialized_start = 1660
    _globals['_MODELMONITORINGSCHEMA']._serialized_end = 2033
    _globals['_MODELMONITORINGSCHEMA_FIELDSCHEMA']._serialized_start = 1969
    _globals['_MODELMONITORINGSCHEMA_FIELDSCHEMA']._serialized_end = 2033