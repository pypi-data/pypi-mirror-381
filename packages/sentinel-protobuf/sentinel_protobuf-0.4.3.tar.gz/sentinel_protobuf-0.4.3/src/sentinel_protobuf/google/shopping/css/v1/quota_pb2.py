"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/css/v1/quota.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/shopping/css/v1/quota.proto\x12\x16google.shopping.css.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa3\x02\n\nQuotaGroup\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bquota_usage\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bquota_limit\x18\x03 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12quota_minute_limit\x18\x05 \x01(\x03B\x03\xe0A\x03\x12B\n\x0emethod_details\x18\x04 \x03(\x0b2%.google.shopping.css.v1.MethodDetailsB\x03\xe0A\x03:i\xeaAf\n\x1dcss.googleapis.com/QuotaGroup\x12,accounts/{account}/quotaGroups/{quota_group}*\x0bquotaGroups2\nquotaGroup"b\n\rMethodDetails\x12\x13\n\x06method\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x14\n\x07version\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06subapi\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04path\x18\x04 \x01(\tB\x03\xe0A\x03"\x80\x01\n\x16ListQuotaGroupsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\x12\x1dcss.googleapis.com/QuotaGroup\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"l\n\x17ListQuotaGroupsResponse\x128\n\x0cquota_groups\x18\x01 \x03(\x0b2".google.shopping.css.v1.QuotaGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf5\x01\n\x0cQuotaService\x12\xa3\x01\n\x0fListQuotaGroups\x12..google.shopping.css.v1.ListQuotaGroupsRequest\x1a/.google.shopping.css.v1.ListQuotaGroupsResponse"/\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=accounts/*}/quotas\x1a?\xcaA\x12css.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\xac\x01\n\x1acom.google.shopping.css.v1B\nQuotaProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.css.v1.quota_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.shopping.css.v1B\nQuotaProtoP\x01Z2cloud.google.com/go/shopping/css/apiv1/csspb;csspb\xaa\x02\x16Google.Shopping.Css.V1\xca\x02\x16Google\\Shopping\\Css\\V1\xea\x02\x19Google::Shopping::Css::V1'
    _globals['_QUOTAGROUP'].fields_by_name['name']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_QUOTAGROUP'].fields_by_name['quota_usage']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_usage']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['quota_limit']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_limit']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['quota_minute_limit']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['quota_minute_limit']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP'].fields_by_name['method_details']._loaded_options = None
    _globals['_QUOTAGROUP'].fields_by_name['method_details']._serialized_options = b'\xe0A\x03'
    _globals['_QUOTAGROUP']._loaded_options = None
    _globals['_QUOTAGROUP']._serialized_options = b'\xeaAf\n\x1dcss.googleapis.com/QuotaGroup\x12,accounts/{account}/quotaGroups/{quota_group}*\x0bquotaGroups2\nquotaGroup'
    _globals['_METHODDETAILS'].fields_by_name['method']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['method']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['version']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['subapi']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['subapi']._serialized_options = b'\xe0A\x03'
    _globals['_METHODDETAILS'].fields_by_name['path']._loaded_options = None
    _globals['_METHODDETAILS'].fields_by_name['path']._serialized_options = b'\xe0A\x03'
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\x12\x1dcss.googleapis.com/QuotaGroup'
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTQUOTAGROUPSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_QUOTASERVICE']._loaded_options = None
    _globals['_QUOTASERVICE']._serialized_options = b"\xcaA\x12css.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_QUOTASERVICE'].methods_by_name['ListQuotaGroups']._loaded_options = None
    _globals['_QUOTASERVICE'].methods_by_name['ListQuotaGroups']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02 \x12\x1e/v1/{parent=accounts/*}/quotas'
    _globals['_QUOTAGROUP']._serialized_start = 178
    _globals['_QUOTAGROUP']._serialized_end = 469
    _globals['_METHODDETAILS']._serialized_start = 471
    _globals['_METHODDETAILS']._serialized_end = 569
    _globals['_LISTQUOTAGROUPSREQUEST']._serialized_start = 572
    _globals['_LISTQUOTAGROUPSREQUEST']._serialized_end = 700
    _globals['_LISTQUOTAGROUPSRESPONSE']._serialized_start = 702
    _globals['_LISTQUOTAGROUPSRESPONSE']._serialized_end = 810
    _globals['_QUOTASERVICE']._serialized_start = 813
    _globals['_QUOTASERVICE']._serialized_end = 1058