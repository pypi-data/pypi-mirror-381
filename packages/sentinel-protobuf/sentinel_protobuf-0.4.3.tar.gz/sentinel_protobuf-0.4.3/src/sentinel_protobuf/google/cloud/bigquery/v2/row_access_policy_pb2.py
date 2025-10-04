"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/row_access_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import row_access_policy_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_row__access__policy__reference__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/bigquery/v2/row_access_policy.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a:google/cloud/bigquery/v2/row_access_policy_reference.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8e\x01\n\x1cListRowAccessPoliciesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x11\n\tpage_size\x18\x05 \x01(\x05"\x80\x01\n\x1dListRowAccessPoliciesResponse\x12F\n\x13row_access_policies\x18\x01 \x03(\x0b2).google.cloud.bigquery.v2.RowAccessPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"|\n\x19GetRowAccessPolicyRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpolicy_id\x18\x04 \x01(\tB\x03\xe0A\x02"\xb2\x01\n\x1cCreateRowAccessPolicyRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12I\n\x11row_access_policy\x18\x04 \x01(\x0b2).google.cloud.bigquery.v2.RowAccessPolicyB\x03\xe0A\x02"\xca\x01\n\x1cUpdateRowAccessPolicyRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpolicy_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12I\n\x11row_access_policy\x18\x05 \x01(\x0b2).google.cloud.bigquery.v2.RowAccessPolicyB\x03\xe0A\x02"\x9d\x01\n\x1cDeleteRowAccessPolicyRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x16\n\tpolicy_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05force\x18\x05 \x01(\x08H\x00\x88\x01\x01B\x08\n\x06_force"\xa5\x01\n#BatchDeleteRowAccessPoliciesRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x17\n\npolicy_ids\x18\x04 \x03(\tB\x03\xe0A\x02\x12\x12\n\x05force\x18\x05 \x01(\x08H\x00\x88\x01\x01B\x08\n\x06_force"\xb0\x02\n\x0fRowAccessPolicy\x12\x11\n\x04etag\x18\x01 \x01(\tB\x03\xe0A\x03\x12\\\n\x1brow_access_policy_reference\x18\x02 \x01(\x0b22.google.cloud.bigquery.v2.RowAccessPolicyReferenceB\x03\xe0A\x02\x12\x1d\n\x10filter_predicate\x18\x03 \x01(\tB\x03\xe0A\x02\x126\n\rcreation_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12;\n\x12last_modified_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x18\n\x08grantees\x18\x06 \x03(\tB\x06\xe0A\x04\xe0A\x012\x90\r\n\x16RowAccessPolicyService\x12\xf4\x01\n\x15ListRowAccessPolicies\x126.google.cloud.bigquery.v2.ListRowAccessPoliciesRequest\x1a7.google.cloud.bigquery.v2.ListRowAccessPoliciesResponse"j\x82\xd3\xe4\x93\x02d\x12b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies\x12\xee\x01\n\x12GetRowAccessPolicy\x123.google.cloud.bigquery.v2.GetRowAccessPolicyRequest\x1a).google.cloud.bigquery.v2.RowAccessPolicy"x\x82\xd3\xe4\x93\x02r\x12p/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}\x12\xf9\x01\n\x15CreateRowAccessPolicy\x126.google.cloud.bigquery.v2.CreateRowAccessPolicyRequest\x1a).google.cloud.bigquery.v2.RowAccessPolicy"}\x82\xd3\xe4\x93\x02w"b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies:\x11row_access_policy\x12\x89\x02\n\x15UpdateRowAccessPolicy\x126.google.cloud.bigquery.v2.UpdateRowAccessPolicyRequest\x1a).google.cloud.bigquery.v2.RowAccessPolicy"\x8c\x01\x82\xd3\xe4\x93\x02\x85\x01\x1ap/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}:\x11row_access_policy\x12\xe1\x01\n\x15DeleteRowAccessPolicy\x126.google.cloud.bigquery.v2.DeleteRowAccessPolicyRequest\x1a\x16.google.protobuf.Empty"x\x82\xd3\xe4\x93\x02r*p/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}\x12\xf0\x01\n\x1cBatchDeleteRowAccessPolicies\x12=.google.cloud.bigquery.v2.BatchDeleteRowAccessPoliciesRequest\x1a\x16.google.protobuf.Empty"y\x82\xd3\xe4\x93\x02s"n/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies:batchDelete:\x01*\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBs\n\x1ccom.google.cloud.bigquery.v2B\x14RowAccessPolicyProtoP\x01Z;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.row_access_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x14RowAccessPolicyProtoP\x01Z;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_LISTROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._loaded_options = None
    _globals['_GETROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['row_access_policy']._loaded_options = None
    _globals['_CREATEROWACCESSPOLICYREQUEST'].fields_by_name['row_access_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._loaded_options = None
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['row_access_policy']._loaded_options = None
    _globals['_UPDATEROWACCESSPOLICYREQUEST'].fields_by_name['row_access_policy']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._loaded_options = None
    _globals['_DELETEROWACCESSPOLICYREQUEST'].fields_by_name['policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._loaded_options = None
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['policy_ids']._loaded_options = None
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST'].fields_by_name['policy_ids']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['etag']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICY'].fields_by_name['row_access_policy_reference']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['row_access_policy_reference']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['filter_predicate']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['filter_predicate']._serialized_options = b'\xe0A\x02'
    _globals['_ROWACCESSPOLICY'].fields_by_name['creation_time']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICY'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_ROWACCESSPOLICY'].fields_by_name['grantees']._loaded_options = None
    _globals['_ROWACCESSPOLICY'].fields_by_name['grantees']._serialized_options = b'\xe0A\x04\xe0A\x01'
    _globals['_ROWACCESSPOLICYSERVICE']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['ListRowAccessPolicies']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['ListRowAccessPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x02d\x12b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['GetRowAccessPolicy']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['GetRowAccessPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02r\x12p/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['CreateRowAccessPolicy']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['CreateRowAccessPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02w"b/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies:\x11row_access_policy'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['UpdateRowAccessPolicy']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['UpdateRowAccessPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x85\x01\x1ap/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}:\x11row_access_policy'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['DeleteRowAccessPolicy']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['DeleteRowAccessPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02r*p/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies/{policy_id=*}'
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['BatchDeleteRowAccessPolicies']._loaded_options = None
    _globals['_ROWACCESSPOLICYSERVICE'].methods_by_name['BatchDeleteRowAccessPolicies']._serialized_options = b'\x82\xd3\xe4\x93\x02s"n/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}/tables/{table_id=*}/rowAccessPolicies:batchDelete:\x01*'
    _globals['_LISTROWACCESSPOLICIESREQUEST']._serialized_start = 289
    _globals['_LISTROWACCESSPOLICIESREQUEST']._serialized_end = 431
    _globals['_LISTROWACCESSPOLICIESRESPONSE']._serialized_start = 434
    _globals['_LISTROWACCESSPOLICIESRESPONSE']._serialized_end = 562
    _globals['_GETROWACCESSPOLICYREQUEST']._serialized_start = 564
    _globals['_GETROWACCESSPOLICYREQUEST']._serialized_end = 688
    _globals['_CREATEROWACCESSPOLICYREQUEST']._serialized_start = 691
    _globals['_CREATEROWACCESSPOLICYREQUEST']._serialized_end = 869
    _globals['_UPDATEROWACCESSPOLICYREQUEST']._serialized_start = 872
    _globals['_UPDATEROWACCESSPOLICYREQUEST']._serialized_end = 1074
    _globals['_DELETEROWACCESSPOLICYREQUEST']._serialized_start = 1077
    _globals['_DELETEROWACCESSPOLICYREQUEST']._serialized_end = 1234
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST']._serialized_start = 1237
    _globals['_BATCHDELETEROWACCESSPOLICIESREQUEST']._serialized_end = 1402
    _globals['_ROWACCESSPOLICY']._serialized_start = 1405
    _globals['_ROWACCESSPOLICY']._serialized_end = 1709
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_start = 1712
    _globals['_ROWACCESSPOLICYSERVICE']._serialized_end = 3392