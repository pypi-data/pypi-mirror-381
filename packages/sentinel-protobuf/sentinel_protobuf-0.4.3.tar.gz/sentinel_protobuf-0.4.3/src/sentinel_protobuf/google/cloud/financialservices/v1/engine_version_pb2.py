"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/engine_version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/financialservices/v1/engine_version.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb7\x04\n\rEngineVersion\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12J\n\x05state\x18\x02 \x01(\x0e26.google.cloud.financialservices.v1.EngineVersion.StateB\x03\xe0A\x03\x12G\n\x1eexpected_limitation_start_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x1aexpected_decommission_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12P\n\x10line_of_business\x18\x05 \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x03"K\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x0b\n\x07LIMITED\x10\x02\x12\x12\n\x0eDECOMMISSIONED\x10\x03:\x96\x01\xeaA\x92\x01\n.financialservices.googleapis.com/EngineVersion\x12`projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}"\xbb\x01\n\x19ListEngineVersionsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x95\x01\n\x1aListEngineVersionsResponse\x12I\n\x0fengine_versions\x18\x01 \x03(\x0b20.google.cloud.financialservices.v1.EngineVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"_\n\x17GetEngineVersionRequest\x12D\n\x04name\x18\x01 \x01(\tB6\xe0A\x02\xfaA0\n.financialservices.googleapis.com/EngineVersionB\x81\x02\n%com.google.cloud.financialservices.v1B\x12EngineVersionProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.engine_version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x12EngineVersionProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_ENGINEVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_ENGINEVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_ENGINEVERSION'].fields_by_name['state']._loaded_options = None
    _globals['_ENGINEVERSION'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINEVERSION'].fields_by_name['expected_limitation_start_time']._loaded_options = None
    _globals['_ENGINEVERSION'].fields_by_name['expected_limitation_start_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINEVERSION'].fields_by_name['expected_decommission_time']._loaded_options = None
    _globals['_ENGINEVERSION'].fields_by_name['expected_decommission_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINEVERSION'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_ENGINEVERSION'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINEVERSION']._loaded_options = None
    _globals['_ENGINEVERSION']._serialized_options = b'\xeaA\x92\x01\n.financialservices.googleapis.com/EngineVersion\x12`projects/{project_num}/locations/{location}/instances/{instance}/engineVersions/{engine_version}'
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTENGINEVERSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETENGINEVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENGINEVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA0\n.financialservices.googleapis.com/EngineVersion'
    _globals['_ENGINEVERSION']._serialized_start = 245
    _globals['_ENGINEVERSION']._serialized_end = 812
    _globals['_ENGINEVERSION_STATE']._serialized_start = 584
    _globals['_ENGINEVERSION_STATE']._serialized_end = 659
    _globals['_LISTENGINEVERSIONSREQUEST']._serialized_start = 815
    _globals['_LISTENGINEVERSIONSREQUEST']._serialized_end = 1002
    _globals['_LISTENGINEVERSIONSRESPONSE']._serialized_start = 1005
    _globals['_LISTENGINEVERSIONSRESPONSE']._serialized_end = 1154
    _globals['_GETENGINEVERSIONREQUEST']._serialized_start = 1156
    _globals['_GETENGINEVERSIONREQUEST']._serialized_end = 1251