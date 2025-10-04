"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/gkemulticloud/v1/common_resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/gkemulticloud/v1/common_resources.proto\x12\x1dgoogle.cloud.gkemulticloud.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"r\n\x03Jwk\x12\x0b\n\x03kty\x18\x01 \x01(\t\x12\x0b\n\x03alg\x18\x02 \x01(\t\x12\x0b\n\x03use\x18\x03 \x01(\t\x12\x0b\n\x03kid\x18\x04 \x01(\t\x12\t\n\x01n\x18\x05 \x01(\t\x12\t\n\x01e\x18\x06 \x01(\t\x12\t\n\x01x\x18\x07 \x01(\t\x12\t\n\x01y\x18\x08 \x01(\t\x12\x0b\n\x03crv\x18\t \x01(\t"^\n\x16WorkloadIdentityConfig\x12\x12\n\nissuer_uri\x18\x01 \x01(\t\x12\x15\n\rworkload_pool\x18\x02 \x01(\t\x12\x19\n\x11identity_provider\x18\x03 \x01(\t"3\n\x11MaxPodsConstraint\x12\x1e\n\x11max_pods_per_node\x18\x01 \x01(\x03B\x03\xe0A\x02"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rstatus_detail\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cerror_detail\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x07 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03"\xd2\x01\n\tNodeTaint\x12\x10\n\x03key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02\x12D\n\x06effect\x18\x03 \x01(\x0e2/.google.cloud.gkemulticloud.v1.NodeTaint.EffectB\x03\xe0A\x02"Y\n\x06Effect\x12\x16\n\x12EFFECT_UNSPECIFIED\x10\x00\x12\x0f\n\x0bNO_SCHEDULE\x10\x01\x12\x16\n\x12PREFER_NO_SCHEDULE\x10\x02\x12\x0e\n\nNO_EXECUTE\x10\x03"\xae\x02\n\x11NodeKubeletConfig\x123\n&insecure_kubelet_readonly_port_enabled\x18\x01 \x01(\x08B\x03\xe0A\x01\x12$\n\x12cpu_manager_policy\x18\x02 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1f\n\rcpu_cfs_quota\x18\x03 \x01(\x08B\x03\xe0A\x01H\x01\x88\x01\x01\x12&\n\x14cpu_cfs_quota_period\x18\x04 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12 \n\x0epod_pids_limit\x18\x05 \x01(\x03B\x03\xe0A\x01H\x03\x88\x01\x01B\x15\n\x13_cpu_manager_policyB\x10\n\x0e_cpu_cfs_quotaB\x17\n\x15_cpu_cfs_quota_periodB\x11\n\x0f_pod_pids_limit"6\n\x05Fleet\x12\x14\n\x07project\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\nmembership\x18\x02 \x01(\tB\x03\xe0A\x03"`\n\rLoggingConfig\x12O\n\x10component_config\x18\x01 \x01(\x0b25.google.cloud.gkemulticloud.v1.LoggingComponentConfig"\xc2\x01\n\x16LoggingComponentConfig\x12Z\n\x11enable_components\x18\x01 \x03(\x0e2?.google.cloud.gkemulticloud.v1.LoggingComponentConfig.Component"L\n\tComponent\x12\x19\n\x15COMPONENT_UNSPECIFIED\x10\x00\x12\x15\n\x11SYSTEM_COMPONENTS\x10\x01\x12\r\n\tWORKLOADS\x10\x02"\xc4\x01\n\x10MonitoringConfig\x12Y\n\x19managed_prometheus_config\x18\x02 \x01(\x0b26.google.cloud.gkemulticloud.v1.ManagedPrometheusConfig\x12U\n\x17cloud_monitoring_config\x18\x04 \x01(\x0b24.google.cloud.gkemulticloud.v1.CloudMonitoringConfig"*\n\x17ManagedPrometheusConfig\x12\x0f\n\x07enabled\x18\x01 \x01(\x08"9\n\x15CloudMonitoringConfig\x12\x14\n\x07enabled\x18\x01 \x01(\x08H\x00\x88\x01\x01B\n\n\x08_enabled"\xd8\x01\n\x13BinaryAuthorization\x12Z\n\x0fevaluation_mode\x18\x01 \x01(\x0e2A.google.cloud.gkemulticloud.v1.BinaryAuthorization.EvaluationMode"e\n\x0eEvaluationMode\x12\x1f\n\x1bEVALUATION_MODE_UNSPECIFIED\x10\x00\x12\x0c\n\x08DISABLED\x10\x01\x12$\n PROJECT_SINGLETON_POLICY_ENFORCE\x10\x02"\xee\x01\n\x15SecurityPostureConfig\x12b\n\x12vulnerability_mode\x18\x01 \x01(\x0e2F.google.cloud.gkemulticloud.v1.SecurityPostureConfig.VulnerabilityMode"q\n\x11VulnerabilityMode\x12"\n\x1eVULNERABILITY_MODE_UNSPECIFIED\x10\x00\x12\x1a\n\x16VULNERABILITY_DISABLED\x10\x01\x12\x1c\n\x18VULNERABILITY_ENTERPRISE\x10\x02B\xe7\x01\n!com.google.cloud.gkemulticloud.v1B\x14CommonResourcesProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.gkemulticloud.v1.common_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.gkemulticloud.v1B\x14CommonResourcesProtoP\x01ZGcloud.google.com/go/gkemulticloud/apiv1/gkemulticloudpb;gkemulticloudpb\xaa\x02\x1dGoogle.Cloud.GkeMultiCloud.V1\xca\x02\x1dGoogle\\Cloud\\GkeMultiCloud\\V1\xea\x02 Google::Cloud::GkeMultiCloud::V1'
    _globals['_MAXPODSCONSTRAINT'].fields_by_name['max_pods_per_node']._loaded_options = None
    _globals['_MAXPODSCONSTRAINT'].fields_by_name['max_pods_per_node']._serialized_options = b'\xe0A\x02'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_detail']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['error_detail']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['error_detail']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_NODETAINT'].fields_by_name['key']._loaded_options = None
    _globals['_NODETAINT'].fields_by_name['key']._serialized_options = b'\xe0A\x02'
    _globals['_NODETAINT'].fields_by_name['value']._loaded_options = None
    _globals['_NODETAINT'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_NODETAINT'].fields_by_name['effect']._loaded_options = None
    _globals['_NODETAINT'].fields_by_name['effect']._serialized_options = b'\xe0A\x02'
    _globals['_NODEKUBELETCONFIG'].fields_by_name['insecure_kubelet_readonly_port_enabled']._loaded_options = None
    _globals['_NODEKUBELETCONFIG'].fields_by_name['insecure_kubelet_readonly_port_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_manager_policy']._loaded_options = None
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_manager_policy']._serialized_options = b'\xe0A\x01'
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_cfs_quota']._loaded_options = None
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_cfs_quota']._serialized_options = b'\xe0A\x01'
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_cfs_quota_period']._loaded_options = None
    _globals['_NODEKUBELETCONFIG'].fields_by_name['cpu_cfs_quota_period']._serialized_options = b'\xe0A\x01'
    _globals['_NODEKUBELETCONFIG'].fields_by_name['pod_pids_limit']._loaded_options = None
    _globals['_NODEKUBELETCONFIG'].fields_by_name['pod_pids_limit']._serialized_options = b'\xe0A\x01'
    _globals['_FLEET'].fields_by_name['project']._loaded_options = None
    _globals['_FLEET'].fields_by_name['project']._serialized_options = b'\xe0A\x02'
    _globals['_FLEET'].fields_by_name['membership']._loaded_options = None
    _globals['_FLEET'].fields_by_name['membership']._serialized_options = b'\xe0A\x03'
    _globals['_JWK']._serialized_start = 153
    _globals['_JWK']._serialized_end = 267
    _globals['_WORKLOADIDENTITYCONFIG']._serialized_start = 269
    _globals['_WORKLOADIDENTITYCONFIG']._serialized_end = 363
    _globals['_MAXPODSCONSTRAINT']._serialized_start = 365
    _globals['_MAXPODSCONSTRAINT']._serialized_end = 416
    _globals['_OPERATIONMETADATA']._serialized_start = 419
    _globals['_OPERATIONMETADATA']._serialized_end = 675
    _globals['_NODETAINT']._serialized_start = 678
    _globals['_NODETAINT']._serialized_end = 888
    _globals['_NODETAINT_EFFECT']._serialized_start = 799
    _globals['_NODETAINT_EFFECT']._serialized_end = 888
    _globals['_NODEKUBELETCONFIG']._serialized_start = 891
    _globals['_NODEKUBELETCONFIG']._serialized_end = 1193
    _globals['_FLEET']._serialized_start = 1195
    _globals['_FLEET']._serialized_end = 1249
    _globals['_LOGGINGCONFIG']._serialized_start = 1251
    _globals['_LOGGINGCONFIG']._serialized_end = 1347
    _globals['_LOGGINGCOMPONENTCONFIG']._serialized_start = 1350
    _globals['_LOGGINGCOMPONENTCONFIG']._serialized_end = 1544
    _globals['_LOGGINGCOMPONENTCONFIG_COMPONENT']._serialized_start = 1468
    _globals['_LOGGINGCOMPONENTCONFIG_COMPONENT']._serialized_end = 1544
    _globals['_MONITORINGCONFIG']._serialized_start = 1547
    _globals['_MONITORINGCONFIG']._serialized_end = 1743
    _globals['_MANAGEDPROMETHEUSCONFIG']._serialized_start = 1745
    _globals['_MANAGEDPROMETHEUSCONFIG']._serialized_end = 1787
    _globals['_CLOUDMONITORINGCONFIG']._serialized_start = 1789
    _globals['_CLOUDMONITORINGCONFIG']._serialized_end = 1846
    _globals['_BINARYAUTHORIZATION']._serialized_start = 1849
    _globals['_BINARYAUTHORIZATION']._serialized_end = 2065
    _globals['_BINARYAUTHORIZATION_EVALUATIONMODE']._serialized_start = 1964
    _globals['_BINARYAUTHORIZATION_EVALUATIONMODE']._serialized_end = 2065
    _globals['_SECURITYPOSTURECONFIG']._serialized_start = 2068
    _globals['_SECURITYPOSTURECONFIG']._serialized_end = 2306
    _globals['_SECURITYPOSTURECONFIG_VULNERABILITYMODE']._serialized_start = 2193
    _globals['_SECURITYPOSTURECONFIG_VULNERABILITYMODE']._serialized_end = 2306