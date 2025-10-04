"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/integrations/v1alpha/cloud_logging_details.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/integrations/v1alpha/cloud_logging_details.proto\x12!google.cloud.integrations.v1alpha\x1a\x1fgoogle/api/field_behavior.proto"\xca\x02\n\x13CloudLoggingDetails\x12u\n\x16cloud_logging_severity\x18\x01 \x01(\x0e2K.google.cloud.integrations.v1alpha.CloudLoggingDetails.CloudLoggingSeverityB\x03\xe0A\x01H\x00\x88\x01\x01\x12&\n\x14enable_cloud_logging\x18\x02 \x01(\x08B\x03\xe0A\x01H\x01\x88\x01\x01"`\n\x14CloudLoggingSeverity\x12&\n"CLOUD_LOGGING_SEVERITY_UNSPECIFIED\x10\x00\x12\x08\n\x04INFO\x10\x02\x12\t\n\x05ERROR\x10\x03\x12\x0b\n\x07WARNING\x10\x04B\x19\n\x17_cloud_logging_severityB\x17\n\x15_enable_cloud_loggingB\xb2\x01\n%com.google.cloud.integrations.v1alphaB\x18CloudLoggingDetailsProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.integrations.v1alpha.cloud_logging_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.integrations.v1alphaB\x18CloudLoggingDetailsProtoP\x01ZIcloud.google.com/go/integrations/apiv1alpha/integrationspb;integrationspb\xaa\x02!Google.Cloud.Integrations.V1Alpha'
    _globals['_CLOUDLOGGINGDETAILS'].fields_by_name['cloud_logging_severity']._loaded_options = None
    _globals['_CLOUDLOGGINGDETAILS'].fields_by_name['cloud_logging_severity']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOGGINGDETAILS'].fields_by_name['enable_cloud_logging']._loaded_options = None
    _globals['_CLOUDLOGGINGDETAILS'].fields_by_name['enable_cloud_logging']._serialized_options = b'\xe0A\x01'
    _globals['_CLOUDLOGGINGDETAILS']._serialized_start = 134
    _globals['_CLOUDLOGGINGDETAILS']._serialized_end = 464
    _globals['_CLOUDLOGGINGDETAILS_CLOUDLOGGINGSEVERITY']._serialized_start = 316
    _globals['_CLOUDLOGGINGDETAILS_CLOUDLOGGINGSEVERITY']._serialized_end = 412