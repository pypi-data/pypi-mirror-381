"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/datapolicies/v2beta1/datapolicy.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/bigquery/datapolicies/v2beta1/datapolicy.proto\x12*google.cloud.bigquery.datapolicies.v2beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xce\x01\n\x17CreateDataPolicyRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x1b\n\x0edata_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\x0bdata_policy\x18\x03 \x01(\x0b26.google.cloud.bigquery.datapolicies.v2beta1.DataPolicyB\x03\xe0A\x02"\xa1\x01\n\x17UpdateDataPolicyRequest\x12P\n\x0bdata_policy\x18\x01 \x01(\x0b26.google.cloud.bigquery.datapolicies.v2beta1.DataPolicyB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"v\n\x12AddGranteesRequest\x12I\n\x0bdata_policy\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x15\n\x08grantees\x18\x02 \x03(\tB\x03\xe0A\x02"y\n\x15RemoveGranteesRequest\x12I\n\x0bdata_policy\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x15\n\x08grantees\x18\x02 \x03(\tB\x03\xe0A\x02"]\n\x17DeleteDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"Z\n\x14GetDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"\x90\x01\n\x17ListDataPoliciesRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x18ListDataPoliciesResponse\x12M\n\rdata_policies\x18\x01 \x03(\x0b26.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8a\x06\n\nDataPolicy\x12a\n\x13data_masking_policy\x18\x07 \x01(\x0b2=.google.cloud.bigquery.datapolicies.v2beta1.DataMaskingPolicyB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1b\n\x0edata_policy_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x0b \x01(\tH\x01\x88\x01\x01\x12d\n\x10data_policy_type\x18\x03 \x01(\x0e2E.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy.DataPolicyTypeB\x03\xe0A\x02\x12@\n\npolicy_tag\x18\x04 \x01(\tB,\xe0A\x03\xfaA&\n$datacatalog.googleapis.com/PolicyTag\x12\x15\n\x08grantees\x18\x08 \x03(\tB\x03\xe0A\x01\x12T\n\x07version\x18\t \x01(\x0e2>.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy.VersionB\x03\xe0A\x03"g\n\x0eDataPolicyType\x12 \n\x1cDATA_POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13DATA_MASKING_POLICY\x10\x01\x12\x1a\n\x16RAW_DATA_ACCESS_POLICY\x10\x02"2\n\x07Version\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02:\x90\x01\xeaA\x8c\x01\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12Bprojects/{project}/locations/{location}/dataPolicies/{data_policy}*\x0cdataPolicies2\ndataPolicyB\x08\n\x06policyB\x07\n\x05_etag"\x9a\x02\n\x11DataMaskingPolicy\x12x\n\x15predefined_expression\x18\x01 \x01(\x0e2R.google.cloud.bigquery.datapolicies.v2beta1.DataMaskingPolicy.PredefinedExpressionB\x03\xe0A\x01H\x00"u\n\x14PredefinedExpression\x12%\n!PREDEFINED_EXPRESSION_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\x0f\n\x0bALWAYS_NULL\x10\x02\x12\x19\n\x15DEFAULT_MASKING_VALUE\x10\x03B\x14\n\x12masking_expression2\xf5\x11\n\x11DataPolicyService\x12\xf5\x01\n\x10CreateDataPolicy\x12C.google.cloud.bigquery.datapolicies.v2beta1.CreateDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy"d\xdaA!parent,data_policy,data_policy_id\x82\xd3\xe4\x93\x02:"5/v2beta1/{parent=projects/*/locations/*}/dataPolicies:\x01*\x12\xf1\x01\n\x0bAddGrantees\x12>.google.cloud.bigquery.datapolicies.v2beta1.AddGranteesRequest\x1a6.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy"j\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02M"H/v2beta1/{data_policy=projects/*/locations/*/dataPolicies/*}:addGrantees:\x01*\x12\xfa\x01\n\x0eRemoveGrantees\x12A.google.cloud.bigquery.datapolicies.v2beta1.RemoveGranteesRequest\x1a6.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy"m\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02P"K/v2beta1/{data_policy=projects/*/locations/*/dataPolicies/*}:removeGrantees:\x01*\x12\x81\x02\n\x10UpdateDataPolicy\x12C.google.cloud.bigquery.datapolicies.v2beta1.UpdateDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy"p\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02P2A/v2beta1/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy\x12\xb5\x01\n\x10DeleteDataPolicy\x12C.google.cloud.bigquery.datapolicies.v2beta1.DeleteDataPolicyRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v2beta1/{name=projects/*/locations/*/dataPolicies/*}\x12\xcf\x01\n\rGetDataPolicy\x12@.google.cloud.bigquery.datapolicies.v2beta1.GetDataPolicyRequest\x1a6.google.cloud.bigquery.datapolicies.v2beta1.DataPolicy"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v2beta1/{name=projects/*/locations/*/dataPolicies/*}\x12\xe5\x01\n\x10ListDataPolicies\x12C.google.cloud.bigquery.datapolicies.v2beta1.ListDataPoliciesRequest\x1aD.google.cloud.bigquery.datapolicies.v2beta1.ListDataPoliciesResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v2beta1/{parent=projects/*/locations/*}/dataPolicies\x12\x9c\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Q\x82\xd3\xe4\x93\x02K"F/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*\x12\x9c\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"Q\x82\xd3\xe4\x93\x02K"F/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*\x12\xc2\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"W\x82\xd3\xe4\x93\x02Q"L/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*\x1a~\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xa2\x03\n.com.google.cloud.bigquery.datapolicies.v2beta1B\x0fDataPolicyProtoP\x01ZRcloud.google.com/go/bigquery/datapolicies/apiv2beta1/datapoliciespb;datapoliciespb\xaa\x02*Google.Cloud.BigQuery.DataPolicies.V2Beta1\xca\x02*Google\\Cloud\\BigQuery\\DataPolicies\\V2beta1\xea\x02.Google::Cloud::Bigquery::DataPolicies::V2beta1\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.datapolicies.v2beta1.datapolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n.com.google.cloud.bigquery.datapolicies.v2beta1B\x0fDataPolicyProtoP\x01ZRcloud.google.com/go/bigquery/datapolicies/apiv2beta1/datapoliciespb;datapoliciespb\xaa\x02*Google.Cloud.BigQuery.DataPolicies.V2Beta1\xca\x02*Google\\Cloud\\BigQuery\\DataPolicies\\V2beta1\xea\x02.Google::Cloud::Bigquery::DataPolicies::V2beta1\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}'
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy_id']._loaded_options = None
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_CREATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_ADDGRANTEESREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_ADDGRANTEESREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_ADDGRANTEESREQUEST'].fields_by_name['grantees']._loaded_options = None
    _globals['_ADDGRANTEESREQUEST'].fields_by_name['grantees']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEGRANTEESREQUEST'].fields_by_name['data_policy']._loaded_options = None
    _globals['_REMOVEGRANTEESREQUEST'].fields_by_name['data_policy']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_REMOVEGRANTEESREQUEST'].fields_by_name['grantees']._loaded_options = None
    _globals['_REMOVEGRANTEESREQUEST'].fields_by_name['grantees']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATAPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDATAPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_GETDATAPOLICYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDATAPOLICYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy'
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPOLICY'].fields_by_name['data_masking_policy']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['data_masking_policy']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_DATAPOLICY'].fields_by_name['data_policy_id']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['data_policy_id']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPOLICY'].fields_by_name['data_policy_type']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['data_policy_type']._serialized_options = b'\xe0A\x02'
    _globals['_DATAPOLICY'].fields_by_name['policy_tag']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['policy_tag']._serialized_options = b'\xe0A\x03\xfaA&\n$datacatalog.googleapis.com/PolicyTag'
    _globals['_DATAPOLICY'].fields_by_name['grantees']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['grantees']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPOLICY'].fields_by_name['version']._loaded_options = None
    _globals['_DATAPOLICY'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_DATAPOLICY']._loaded_options = None
    _globals['_DATAPOLICY']._serialized_options = b'\xeaA\x8c\x01\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12Bprojects/{project}/locations/{location}/dataPolicies/{data_policy}*\x0cdataPolicies2\ndataPolicy'
    _globals['_DATAMASKINGPOLICY'].fields_by_name['predefined_expression']._loaded_options = None
    _globals['_DATAMASKINGPOLICY'].fields_by_name['predefined_expression']._serialized_options = b'\xe0A\x01'
    _globals['_DATAPOLICYSERVICE']._loaded_options = None
    _globals['_DATAPOLICYSERVICE']._serialized_options = b'\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._serialized_options = b'\xdaA!parent,data_policy,data_policy_id\x82\xd3\xe4\x93\x02:"5/v2beta1/{parent=projects/*/locations/*}/dataPolicies:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['AddGrantees']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['AddGrantees']._serialized_options = b'\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02M"H/v2beta1/{data_policy=projects/*/locations/*/dataPolicies/*}:addGrantees:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['RemoveGrantees']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['RemoveGrantees']._serialized_options = b'\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02P"K/v2beta1/{data_policy=projects/*/locations/*/dataPolicies/*}:removeGrantees:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._serialized_options = b'\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02P2A/v2beta1/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v2beta1/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v2beta1/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v2beta1/{parent=projects/*/locations/*}/dataPolicies'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02Q"L/v2beta1/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*'
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_start = 346
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_end = 552
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_start = 555
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_end = 716
    _globals['_ADDGRANTEESREQUEST']._serialized_start = 718
    _globals['_ADDGRANTEESREQUEST']._serialized_end = 836
    _globals['_REMOVEGRANTEESREQUEST']._serialized_start = 838
    _globals['_REMOVEGRANTEESREQUEST']._serialized_end = 959
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_start = 961
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_end = 1054
    _globals['_GETDATAPOLICYREQUEST']._serialized_start = 1056
    _globals['_GETDATAPOLICYREQUEST']._serialized_end = 1146
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_start = 1149
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_end = 1293
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_start = 1296
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_end = 1426
    _globals['_DATAPOLICY']._serialized_start = 1429
    _globals['_DATAPOLICY']._serialized_end = 2207
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_start = 1886
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_end = 1989
    _globals['_DATAPOLICY_VERSION']._serialized_start = 1991
    _globals['_DATAPOLICY_VERSION']._serialized_end = 2041
    _globals['_DATAMASKINGPOLICY']._serialized_start = 2210
    _globals['_DATAMASKINGPOLICY']._serialized_end = 2492
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_start = 2353
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_end = 2470
    _globals['_DATAPOLICYSERVICE']._serialized_start = 2495
    _globals['_DATAPOLICYSERVICE']._serialized_end = 4788