"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/saasplatform/saasservicemgmt/v1beta1/common.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/saasplatform/saasservicemgmt/v1beta1/common.proto\x121google.cloud.saasplatform.saasservicemgmt.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"O\n\tBlueprint\x12\x17\n\x07package\x18\x01 \x01(\tB\x06\xe0A\x01\xe0A\x05\x12\x13\n\x06engine\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07version\x18\x03 \x01(\tB\x03\xe0A\x03"\xd5\x01\n\x0cUnitVariable\x12\x18\n\x08variable\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12Z\n\x04type\x18\x02 \x01(\x0e2D.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitVariable.TypeB\x06\xe0A\x01\xe0A\x05\x12\x12\n\x05value\x18\x03 \x01(\tB\x03\xe0A\x01";\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06STRING\x10\x01\x12\x07\n\x03INT\x10\x02\x12\x08\n\x04BOOL\x10\x03"\xfb\x03\n\rUnitCondition\x12\\\n\x06status\x18\x01 \x01(\x0e2G.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitCondition.StatusB\x03\xe0A\x02\x12X\n\x04type\x18\x02 \x01(\x0e2E.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitCondition.TypeB\x03\xe0A\x02\x12=\n\x14last_transition_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x14\n\x07message\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06reason\x18\x05 \x01(\tB\x03\xe0A\x02"W\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x01\x12\x0f\n\x0bSTATUS_TRUE\x10\x02\x12\x10\n\x0cSTATUS_FALSE\x10\x03"o\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x0e\n\nTYPE_READY\x10\x01\x12\x11\n\rTYPE_UPDATING\x10\x02\x12\x14\n\x10TYPE_PROVISIONED\x10\x03\x12\x18\n\x14TYPE_OPERATION_ERROR\x10\x04"\x91\x04\n\x16UnitOperationCondition\x12e\n\x06status\x18\x01 \x01(\x0e2P.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperationCondition.StatusB\x03\xe0A\x02\x12a\n\x04type\x18\x02 \x01(\x0e2N.google.cloud.saasplatform.saasservicemgmt.v1beta1.UnitOperationCondition.TypeB\x03\xe0A\x02\x12=\n\x14last_transition_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x14\n\x07message\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06reason\x18\x05 \x01(\tB\x03\xe0A\x02"W\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x12\n\x0eSTATUS_UNKNOWN\x10\x01\x12\x0f\n\x0bSTATUS_TRUE\x10\x02\x12\x10\n\x0cSTATUS_FALSE\x10\x03"j\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\x12\n\x0eTYPE_SCHEDULED\x10\x02\x12\x10\n\x0cTYPE_RUNNING\x10\x03\x12\x12\n\x0eTYPE_SUCCEEDED\x10\x04\x12\x12\n\x0eTYPE_CANCELLED\x10\x05"3\n\tAggregate\x12\x12\n\x05group\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05count\x18\x02 \x01(\x05B\x03\xe0A\x02*\x96\x01\n\x1aUnitOperationErrorCategory\x12-\n)UNIT_OPERATION_ERROR_CATEGORY_UNSPECIFIED\x10\x00\x12\x12\n\x0eNOT_APPLICABLE\x10\x01\x12\t\n\x05FATAL\x10\x02\x12\r\n\tRETRIABLE\x10\x03\x12\r\n\tIGNORABLE\x10\x04\x12\x0c\n\x08STANDARD\x10\x05B\xc7\x02\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x0bCommonProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.saasplatform.saasservicemgmt.v1beta1.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x0bCommonProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1'
    _globals['_BLUEPRINT'].fields_by_name['package']._loaded_options = None
    _globals['_BLUEPRINT'].fields_by_name['package']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_BLUEPRINT'].fields_by_name['engine']._loaded_options = None
    _globals['_BLUEPRINT'].fields_by_name['engine']._serialized_options = b'\xe0A\x03'
    _globals['_BLUEPRINT'].fields_by_name['version']._loaded_options = None
    _globals['_BLUEPRINT'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_UNITVARIABLE'].fields_by_name['variable']._loaded_options = None
    _globals['_UNITVARIABLE'].fields_by_name['variable']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_UNITVARIABLE'].fields_by_name['type']._loaded_options = None
    _globals['_UNITVARIABLE'].fields_by_name['type']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_UNITVARIABLE'].fields_by_name['value']._loaded_options = None
    _globals['_UNITVARIABLE'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_UNITCONDITION'].fields_by_name['status']._loaded_options = None
    _globals['_UNITCONDITION'].fields_by_name['status']._serialized_options = b'\xe0A\x02'
    _globals['_UNITCONDITION'].fields_by_name['type']._loaded_options = None
    _globals['_UNITCONDITION'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_UNITCONDITION'].fields_by_name['last_transition_time']._loaded_options = None
    _globals['_UNITCONDITION'].fields_by_name['last_transition_time']._serialized_options = b'\xe0A\x02'
    _globals['_UNITCONDITION'].fields_by_name['message']._loaded_options = None
    _globals['_UNITCONDITION'].fields_by_name['message']._serialized_options = b'\xe0A\x02'
    _globals['_UNITCONDITION'].fields_by_name['reason']._loaded_options = None
    _globals['_UNITCONDITION'].fields_by_name['reason']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['status']._loaded_options = None
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['status']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['type']._loaded_options = None
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['last_transition_time']._loaded_options = None
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['last_transition_time']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['message']._loaded_options = None
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['message']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['reason']._loaded_options = None
    _globals['_UNITOPERATIONCONDITION'].fields_by_name['reason']._serialized_options = b'\xe0A\x02'
    _globals['_AGGREGATE'].fields_by_name['group']._loaded_options = None
    _globals['_AGGREGATE'].fields_by_name['group']._serialized_options = b'\xe0A\x02'
    _globals['_AGGREGATE'].fields_by_name['count']._loaded_options = None
    _globals['_AGGREGATE'].fields_by_name['count']._serialized_options = b'\xe0A\x02'
    _globals['_UNITOPERATIONERRORCATEGORY']._serialized_start = 1576
    _globals['_UNITOPERATIONERRORCATEGORY']._serialized_end = 1726
    _globals['_BLUEPRINT']._serialized_start = 183
    _globals['_BLUEPRINT']._serialized_end = 262
    _globals['_UNITVARIABLE']._serialized_start = 265
    _globals['_UNITVARIABLE']._serialized_end = 478
    _globals['_UNITVARIABLE_TYPE']._serialized_start = 419
    _globals['_UNITVARIABLE_TYPE']._serialized_end = 478
    _globals['_UNITCONDITION']._serialized_start = 481
    _globals['_UNITCONDITION']._serialized_end = 988
    _globals['_UNITCONDITION_STATUS']._serialized_start = 788
    _globals['_UNITCONDITION_STATUS']._serialized_end = 875
    _globals['_UNITCONDITION_TYPE']._serialized_start = 877
    _globals['_UNITCONDITION_TYPE']._serialized_end = 988
    _globals['_UNITOPERATIONCONDITION']._serialized_start = 991
    _globals['_UNITOPERATIONCONDITION']._serialized_end = 1520
    _globals['_UNITOPERATIONCONDITION_STATUS']._serialized_start = 788
    _globals['_UNITOPERATIONCONDITION_STATUS']._serialized_end = 875
    _globals['_UNITOPERATIONCONDITION_TYPE']._serialized_start = 1414
    _globals['_UNITOPERATIONCONDITION_TYPE']._serialized_end = 1520
    _globals['_AGGREGATE']._serialized_start = 1522
    _globals['_AGGREGATE']._serialized_end = 1573