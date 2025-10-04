"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/project.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)google/cloud/retail/v2alpha/project.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto"\xfd\x05\n\rLoggingConfig\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12a\n\x1bdefault_log_generation_rule\x18\x02 \x01(\x0b2<.google.cloud.retail.v2alpha.LoggingConfig.LogGenerationRule\x12i\n\x1cservice_log_generation_rules\x18\x04 \x03(\x0b2C.google.cloud.retail.v2alpha.LoggingConfig.ServiceLogGenerationRule\x1a\x9f\x01\n\x11LogGenerationRule\x12N\n\rlogging_level\x18\x01 \x01(\x0e27.google.cloud.retail.v2alpha.LoggingConfig.LoggingLevel\x12!\n\x14info_log_sample_rate\x18\x02 \x01(\x02H\x00\x88\x01\x01B\x17\n\x15_info_log_sample_rate\x1a\x90\x01\n\x18ServiceLogGenerationRule\x12\x19\n\x0cservice_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12Y\n\x13log_generation_rule\x18\x03 \x01(\x0b2<.google.cloud.retail.v2alpha.LoggingConfig.LogGenerationRule"\x86\x01\n\x0cLoggingLevel\x12\x1d\n\x19LOGGING_LEVEL_UNSPECIFIED\x10\x00\x12\x14\n\x10LOGGING_DISABLED\x10\x01\x12\x18\n\x14LOG_ERRORS_AND_ABOVE\x10\x02\x12\x1a\n\x16LOG_WARNINGS_AND_ABOVE\x10\x03\x12\x0b\n\x07LOG_ALL\x10\x04:J\xeaAG\n#retail.googleapis.com/LoggingConfig\x12 projects/{project}/loggingConfig"\xb4\x01\n\x07Project\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12J\n\x12enrolled_solutions\x18\x02 \x03(\x0e2).google.cloud.retail.v2alpha.SolutionTypeB\x03\xe0A\x03:J\xeaAG\n#retail.googleapis.com/RetailProject\x12 projects/{project}/retailProject"\xfb\x03\n\x0bAlertConfig\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12L\n\x0ealert_policies\x18\x02 \x03(\x0b24.google.cloud.retail.v2alpha.AlertConfig.AlertPolicy\x1a\xbf\x02\n\x0bAlertPolicy\x12\x13\n\x0balert_group\x18\x01 \x01(\t\x12X\n\renroll_status\x18\x02 \x01(\x0e2A.google.cloud.retail.v2alpha.AlertConfig.AlertPolicy.EnrollStatus\x12R\n\nrecipients\x18\x03 \x03(\x0b2>.google.cloud.retail.v2alpha.AlertConfig.AlertPolicy.Recipient\x1a"\n\tRecipient\x12\x15\n\remail_address\x18\x01 \x01(\t"I\n\x0cEnrollStatus\x12\x1d\n\x19ENROLL_STATUS_UNSPECIFIED\x10\x00\x12\x0c\n\x08ENROLLED\x10\x01\x12\x0c\n\x08DECLINED\x10\x02:F\xeaAC\n!retail.googleapis.com/AlertConfig\x12\x1eprojects/{project}/alertConfigB\xd0\x01\n\x1fcom.google.cloud.retail.v2alphaB\x0cProjectProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.project_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\x0cProjectProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_LOGGINGCONFIG_SERVICELOGGENERATIONRULE'].fields_by_name['service_name']._loaded_options = None
    _globals['_LOGGINGCONFIG_SERVICELOGGENERATIONRULE'].fields_by_name['service_name']._serialized_options = b'\xe0A\x02'
    _globals['_LOGGINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_LOGGINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_LOGGINGCONFIG']._loaded_options = None
    _globals['_LOGGINGCONFIG']._serialized_options = b'\xeaAG\n#retail.googleapis.com/LoggingConfig\x12 projects/{project}/loggingConfig'
    _globals['_PROJECT'].fields_by_name['name']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT'].fields_by_name['enrolled_solutions']._loaded_options = None
    _globals['_PROJECT'].fields_by_name['enrolled_solutions']._serialized_options = b'\xe0A\x03'
    _globals['_PROJECT']._loaded_options = None
    _globals['_PROJECT']._serialized_options = b'\xeaAG\n#retail.googleapis.com/RetailProject\x12 projects/{project}/retailProject'
    _globals['_ALERTCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_ALERTCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_ALERTCONFIG']._loaded_options = None
    _globals['_ALERTCONFIG']._serialized_options = b'\xeaAC\n!retail.googleapis.com/AlertConfig\x12\x1eprojects/{project}/alertConfig'
    _globals['_LOGGINGCONFIG']._serialized_start = 177
    _globals['_LOGGINGCONFIG']._serialized_end = 942
    _globals['_LOGGINGCONFIG_LOGGENERATIONRULE']._serialized_start = 423
    _globals['_LOGGINGCONFIG_LOGGENERATIONRULE']._serialized_end = 582
    _globals['_LOGGINGCONFIG_SERVICELOGGENERATIONRULE']._serialized_start = 585
    _globals['_LOGGINGCONFIG_SERVICELOGGENERATIONRULE']._serialized_end = 729
    _globals['_LOGGINGCONFIG_LOGGINGLEVEL']._serialized_start = 732
    _globals['_LOGGINGCONFIG_LOGGINGLEVEL']._serialized_end = 866
    _globals['_PROJECT']._serialized_start = 945
    _globals['_PROJECT']._serialized_end = 1125
    _globals['_ALERTCONFIG']._serialized_start = 1128
    _globals['_ALERTCONFIG']._serialized_end = 1635
    _globals['_ALERTCONFIG_ALERTPOLICY']._serialized_start = 1244
    _globals['_ALERTCONFIG_ALERTPOLICY']._serialized_end = 1563
    _globals['_ALERTCONFIG_ALERTPOLICY_RECIPIENT']._serialized_start = 1454
    _globals['_ALERTCONFIG_ALERTPOLICY_RECIPIENT']._serialized_end = 1488
    _globals['_ALERTCONFIG_ALERTPOLICY_ENROLLSTATUS']._serialized_start = 1490
    _globals['_ALERTCONFIG_ALERTPOLICY_ENROLLSTATUS']._serialized_end = 1563