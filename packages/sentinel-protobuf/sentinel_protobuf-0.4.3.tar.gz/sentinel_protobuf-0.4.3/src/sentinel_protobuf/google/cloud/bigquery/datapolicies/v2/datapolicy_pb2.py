"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/datapolicies/v2/datapolicy.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from ......google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/bigquery/datapolicies/v2/datapolicy.proto\x12%google.cloud.bigquery.datapolicies.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xc9\x01\n\x17CreateDataPolicyRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x1b\n\x0edata_policy_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\x0bdata_policy\x18\x03 \x01(\x0b21.google.cloud.bigquery.datapolicies.v2.DataPolicyB\x03\xe0A\x02"\xb8\x01\n\x17UpdateDataPolicyRequest\x12K\n\x0bdata_policy\x18\x01 \x01(\x0b21.google.cloud.bigquery.datapolicies.v2.DataPolicyB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12\x1a\n\rallow_missing\x18\x03 \x01(\x08B\x03\xe0A\x01"v\n\x12AddGranteesRequest\x12I\n\x0bdata_policy\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x15\n\x08grantees\x18\x02 \x03(\tB\x03\xe0A\x02"y\n\x15RemoveGranteesRequest\x12I\n\x0bdata_policy\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x15\n\x08grantees\x18\x02 \x03(\tB\x03\xe0A\x02"]\n\x17DeleteDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"Z\n\x14GetDataPolicyRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,bigquerydatapolicy.googleapis.com/DataPolicy"\xa5\x01\n\x17ListDataPoliciesRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,bigquerydatapolicy.googleapis.com/DataPolicy\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"}\n\x18ListDataPoliciesResponse\x12H\n\rdata_policies\x18\x01 \x03(\x0b21.google.cloud.bigquery.datapolicies.v2.DataPolicy\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x9e\x06\n\nDataPolicy\x12\\\n\x13data_masking_policy\x18\x07 \x01(\x0b28.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicyB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1b\n\x0edata_policy_id\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x0b \x01(\tH\x01\x88\x01\x01\x12_\n\x10data_policy_type\x18\x03 \x01(\x0e2@.google.cloud.bigquery.datapolicies.v2.DataPolicy.DataPolicyTypeB\x03\xe0A\x02\x12@\n\npolicy_tag\x18\x04 \x01(\tB,\xe0A\x03\xfaA&\n$datacatalog.googleapis.com/PolicyTag\x12\x15\n\x08grantees\x18\x08 \x03(\tB\x03\xe0A\x01\x12O\n\x07version\x18\t \x01(\x0e29.google.cloud.bigquery.datapolicies.v2.DataPolicy.VersionB\x03\xe0A\x03"\x89\x01\n\x0eDataPolicyType\x12 \n\x1cDATA_POLICY_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13DATA_MASKING_POLICY\x10\x01\x12\x1a\n\x16RAW_DATA_ACCESS_POLICY\x10\x02\x12 \n\x1cCOLUMN_LEVEL_SECURITY_POLICY\x10\x03"2\n\x07Version\x12\x17\n\x13VERSION_UNSPECIFIED\x10\x00\x12\x06\n\x02V1\x10\x01\x12\x06\n\x02V2\x10\x02:\x90\x01\xeaA\x8c\x01\n,bigquerydatapolicy.googleapis.com/DataPolicy\x12Bprojects/{project}/locations/{location}/dataPolicies/{data_policy}*\x0cdataPolicies2\ndataPolicyB\x08\n\x06policyB\x07\n\x05_etag"\xbc\x03\n\x11DataMaskingPolicy\x12s\n\x15predefined_expression\x18\x01 \x01(\x0e2M.google.cloud.bigquery.datapolicies.v2.DataMaskingPolicy.PredefinedExpressionB\x03\xe0A\x01H\x00\x12:\n\x07routine\x18\x02 \x01(\tB\'\xe0A\x01\xfaA!\n\x1fbigquery.googleapis.com/RoutineH\x00"\xdf\x01\n\x14PredefinedExpression\x12%\n!PREDEFINED_EXPRESSION_UNSPECIFIED\x10\x00\x12\n\n\x06SHA256\x10\x01\x12\x0f\n\x0bALWAYS_NULL\x10\x02\x12\x19\n\x15DEFAULT_MASKING_VALUE\x10\x03\x12\x18\n\x14LAST_FOUR_CHARACTERS\x10\x04\x12\x19\n\x15FIRST_FOUR_CHARACTERS\x10\x05\x12\x0e\n\nEMAIL_MASK\x10\x06\x12\x12\n\x0eDATE_YEAR_MASK\x10\x07\x12\x0f\n\x0bRANDOM_HASH\x10\x08B\x14\n\x12masking_expression2\x82\x11\n\x11DataPolicyService\x12\xe6\x01\n\x10CreateDataPolicy\x12>.google.cloud.bigquery.datapolicies.v2.CreateDataPolicyRequest\x1a1.google.cloud.bigquery.datapolicies.v2.DataPolicy"_\xdaA!parent,data_policy,data_policy_id\x82\xd3\xe4\x93\x025"0/v2/{parent=projects/*/locations/*}/dataPolicies:\x01*\x12\xe2\x01\n\x0bAddGrantees\x129.google.cloud.bigquery.datapolicies.v2.AddGranteesRequest\x1a1.google.cloud.bigquery.datapolicies.v2.DataPolicy"e\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02H"C/v2/{data_policy=projects/*/locations/*/dataPolicies/*}:addGrantees:\x01*\x12\xeb\x01\n\x0eRemoveGrantees\x12<.google.cloud.bigquery.datapolicies.v2.RemoveGranteesRequest\x1a1.google.cloud.bigquery.datapolicies.v2.DataPolicy"h\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02K"F/v2/{data_policy=projects/*/locations/*/dataPolicies/*}:removeGrantees:\x01*\x12\xf2\x01\n\x10UpdateDataPolicy\x12>.google.cloud.bigquery.datapolicies.v2.UpdateDataPolicyRequest\x1a1.google.cloud.bigquery.datapolicies.v2.DataPolicy"k\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02K2</v2/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy\x12\xab\x01\n\x10DeleteDataPolicy\x12>.google.cloud.bigquery.datapolicies.v2.DeleteDataPolicyRequest\x1a\x16.google.protobuf.Empty"?\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v2/{name=projects/*/locations/*/dataPolicies/*}\x12\xc0\x01\n\rGetDataPolicy\x12;.google.cloud.bigquery.datapolicies.v2.GetDataPolicyRequest\x1a1.google.cloud.bigquery.datapolicies.v2.DataPolicy"?\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2/{name=projects/*/locations/*/dataPolicies/*}\x12\xd6\x01\n\x10ListDataPolicies\x12>.google.cloud.bigquery.datapolicies.v2.ListDataPoliciesRequest\x1a?.google.cloud.bigquery.datapolicies.v2.ListDataPoliciesResponse"A\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2/{parent=projects/*/locations/*}/dataPolicies\x12\x97\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"L\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*\x12\x97\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"L\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*\x12\xbd\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"R\x82\xd3\xe4\x93\x02L"G/v2/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*\x1a~\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xe7\x03\n)com.google.cloud.bigquery.datapolicies.v2B\x0fDataPolicyProtoP\x01ZMcloud.google.com/go/bigquery/datapolicies/apiv2/datapoliciespb;datapoliciespb\xaa\x02%Google.Cloud.BigQuery.DataPolicies.V2\xca\x02%Google\\Cloud\\BigQuery\\DataPolicies\\V2\xea\x02)Google::Cloud::Bigquery::DataPolicies::V2\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}\xeaA[\n\x1fbigquery.googleapis.com/Routine\x128projects/{project}/datasets/{dataset}/routines/{routine}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.datapolicies.v2.datapolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.cloud.bigquery.datapolicies.v2B\x0fDataPolicyProtoP\x01ZMcloud.google.com/go/bigquery/datapolicies/apiv2/datapoliciespb;datapoliciespb\xaa\x02%Google.Cloud.BigQuery.DataPolicies.V2\xca\x02%Google\\Cloud\\BigQuery\\DataPolicies\\V2\xea\x02)Google::Cloud::Bigquery::DataPolicies::V2\xeaA}\n$datacatalog.googleapis.com/PolicyTag\x12Uprojects/{project}/locations/{location}/taxonomies/{taxonomy}/policyTags/{policy_tag}\xeaA[\n\x1fbigquery.googleapis.com/Routine\x128projects/{project}/datasets/{dataset}/routines/{routine}'
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
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['allow_missing']._loaded_options = None
    _globals['_UPDATEDATAPOLICYREQUEST'].fields_by_name['allow_missing']._serialized_options = b'\xe0A\x01'
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
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTDATAPOLICIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
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
    _globals['_DATAMASKINGPOLICY'].fields_by_name['routine']._loaded_options = None
    _globals['_DATAMASKINGPOLICY'].fields_by_name['routine']._serialized_options = b'\xe0A\x01\xfaA!\n\x1fbigquery.googleapis.com/Routine'
    _globals['_DATAPOLICYSERVICE']._loaded_options = None
    _globals['_DATAPOLICYSERVICE']._serialized_options = b'\xcaA!bigquerydatapolicy.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['CreateDataPolicy']._serialized_options = b'\xdaA!parent,data_policy,data_policy_id\x82\xd3\xe4\x93\x025"0/v2/{parent=projects/*/locations/*}/dataPolicies:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['AddGrantees']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['AddGrantees']._serialized_options = b'\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02H"C/v2/{data_policy=projects/*/locations/*/dataPolicies/*}:addGrantees:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['RemoveGrantees']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['RemoveGrantees']._serialized_options = b'\xdaA\x14data_policy,grantees\x82\xd3\xe4\x93\x02K"F/v2/{data_policy=projects/*/locations/*/dataPolicies/*}:removeGrantees:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['UpdateDataPolicy']._serialized_options = b'\xdaA\x17data_policy,update_mask\x82\xd3\xe4\x93\x02K2</v2/{data_policy.name=projects/*/locations/*/dataPolicies/*}:\x0bdata_policy'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['DeleteDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022*0/v2/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetDataPolicy']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x022\x120/v2/{name=projects/*/locations/*/dataPolicies/*}'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['ListDataPolicies']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x022\x120/v2/{parent=projects/*/locations/*}/dataPolicies'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/dataPolicies/*}:getIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02F"A/v2/{resource=projects/*/locations/*/dataPolicies/*}:setIamPolicy:\x01*'
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_DATAPOLICYSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02L"G/v2/{resource=projects/*/locations/*/dataPolicies/*}:testIamPermissions:\x01*'
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_start = 336
    _globals['_CREATEDATAPOLICYREQUEST']._serialized_end = 537
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_start = 540
    _globals['_UPDATEDATAPOLICYREQUEST']._serialized_end = 724
    _globals['_ADDGRANTEESREQUEST']._serialized_start = 726
    _globals['_ADDGRANTEESREQUEST']._serialized_end = 844
    _globals['_REMOVEGRANTEESREQUEST']._serialized_start = 846
    _globals['_REMOVEGRANTEESREQUEST']._serialized_end = 967
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_start = 969
    _globals['_DELETEDATAPOLICYREQUEST']._serialized_end = 1062
    _globals['_GETDATAPOLICYREQUEST']._serialized_start = 1064
    _globals['_GETDATAPOLICYREQUEST']._serialized_end = 1154
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_start = 1157
    _globals['_LISTDATAPOLICIESREQUEST']._serialized_end = 1322
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_start = 1324
    _globals['_LISTDATAPOLICIESRESPONSE']._serialized_end = 1449
    _globals['_DATAPOLICY']._serialized_start = 1452
    _globals['_DATAPOLICY']._serialized_end = 2250
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_start = 1895
    _globals['_DATAPOLICY_DATAPOLICYTYPE']._serialized_end = 2032
    _globals['_DATAPOLICY_VERSION']._serialized_start = 2034
    _globals['_DATAPOLICY_VERSION']._serialized_end = 2084
    _globals['_DATAMASKINGPOLICY']._serialized_start = 2253
    _globals['_DATAMASKINGPOLICY']._serialized_end = 2697
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_start = 2452
    _globals['_DATAMASKINGPOLICY_PREDEFINEDEXPRESSION']._serialized_end = 2675
    _globals['_DATAPOLICYSERVICE']._serialized_start = 2700
    _globals['_DATAPOLICYSERVICE']._serialized_end = 4878