"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/securitycenter/v1/event_threat_detection_custom_module_validation_errors.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n[google/cloud/securitycenter/v1/event_threat_detection_custom_module_validation_errors.proto\x12\x1egoogle.cloud.securitycenter.v1"k\n\x1cCustomModuleValidationErrors\x12K\n\x06errors\x18\x01 \x03(\x0b2;.google.cloud.securitycenter.v1.CustomModuleValidationError"\xd2\x01\n\x1bCustomModuleValidationError\x12\x13\n\x0bdescription\x18\x01 \x01(\t\x12\x12\n\nfield_path\x18\x02 \x01(\t\x12<\n\x05start\x18\x03 \x01(\x0b2(.google.cloud.securitycenter.v1.PositionH\x00\x88\x01\x01\x12:\n\x03end\x18\x04 \x01(\x0b2(.google.cloud.securitycenter.v1.PositionH\x01\x88\x01\x01B\x08\n\x06_startB\x06\n\x04_end"6\n\x08Position\x12\x13\n\x0bline_number\x18\x01 \x01(\x05\x12\x15\n\rcolumn_number\x18\x02 \x01(\x05B\x8f\x02\n"com.google.cloud.securitycenter.v1B5EventThreatDetectionCustomModuleValidationErrorsProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.securitycenter.v1.event_threat_detection_custom_module_validation_errors_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.securitycenter.v1B5EventThreatDetectionCustomModuleValidationErrorsProtoP\x01ZJcloud.google.com/go/securitycenter/apiv1/securitycenterpb;securitycenterpb\xaa\x02\x1eGoogle.Cloud.SecurityCenter.V1\xca\x02\x1eGoogle\\Cloud\\SecurityCenter\\V1\xea\x02!Google::Cloud::SecurityCenter::V1'
    _globals['_CUSTOMMODULEVALIDATIONERRORS']._serialized_start = 127
    _globals['_CUSTOMMODULEVALIDATIONERRORS']._serialized_end = 234
    _globals['_CUSTOMMODULEVALIDATIONERROR']._serialized_start = 237
    _globals['_CUSTOMMODULEVALIDATIONERROR']._serialized_end = 447
    _globals['_POSITION']._serialized_start = 449
    _globals['_POSITION']._serialized_end = 503