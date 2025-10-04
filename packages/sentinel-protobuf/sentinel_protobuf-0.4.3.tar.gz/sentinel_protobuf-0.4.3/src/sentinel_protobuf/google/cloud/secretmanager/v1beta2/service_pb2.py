"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/secretmanager/v1beta2/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.secretmanager.v1beta2 import resources_pb2 as google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/secretmanager/v1beta2/service.proto\x12"google.cloud.secretmanager.v1beta2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/secretmanager/v1beta2/resources.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x97\x01\n\x12ListSecretsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x7f\n\x13ListSecretsResponse\x12;\n\x07secrets\x18\x01 \x03(\x0b2*.google.cloud.secretmanager.v1beta2.Secret\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xab\x01\n\x13CreateSecretRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret\x12\x16\n\tsecret_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12?\n\x06secret\x18\x03 \x01(\x0b2*.google.cloud.secretmanager.v1beta2.SecretB\x03\xe0A\x02"\x9f\x01\n\x17AddSecretVersionRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12G\n\x07payload\x18\x02 \x01(\x0b21.google.cloud.secretmanager.v1beta2.SecretPayloadB\x03\xe0A\x02"M\n\x10GetSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret"\x9e\x01\n\x19ListSecretVersionsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x8e\x01\n\x1aListSecretVersionsResponse\x12C\n\x08versions\x18\x01 \x03(\x0b21.google.cloud.secretmanager.v1beta2.SecretVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"[\n\x17GetSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\x8c\x01\n\x13UpdateSecretRequest\x12?\n\x06secret\x18\x01 \x01(\x0b2*.google.cloud.secretmanager.v1beta2.SecretB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"^\n\x1aAccessSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\xa0\x01\n\x1bAccessSecretVersionResponse\x12=\n\x04name\x18\x01 \x01(\tB/\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12B\n\x07payload\x18\x02 \x01(\x0b21.google.cloud.secretmanager.v1beta2.SecretPayload"c\n\x13DeleteSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"r\n\x1bDisableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"q\n\x1aEnableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"r\n\x1bDestroySecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x012\xf7\x1e\n\x14SecretManagerService\x12\xe9\x01\n\x0bListSecrets\x126.google.cloud.secretmanager.v1beta2.ListSecretsRequest\x1a7.google.cloud.secretmanager.v1beta2.ListSecretsResponse"i\xdaA\x06parent\x82\xd3\xe4\x93\x02Z\x12$/v1beta2/{parent=projects/*}/secretsZ2\x120/v1beta2/{parent=projects/*/locations/*}/secrets\x12\x80\x02\n\x0cCreateSecret\x127.google.cloud.secretmanager.v1beta2.CreateSecretRequest\x1a*.google.cloud.secretmanager.v1beta2.Secret"\x8a\x01\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02j"$/v1beta2/{parent=projects/*}/secrets:\x06secretZ:"0/v1beta2/{parent=projects/*/locations/*}/secrets:\x06secret\x12\x96\x02\n\x10AddSecretVersion\x12;.google.cloud.secretmanager.v1beta2.AddSecretVersionRequest\x1a1.google.cloud.secretmanager.v1beta2.SecretVersion"\x91\x01\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x02z"1/v1beta2/{parent=projects/*/secrets/*}:addVersion:\x01*ZB"=/v1beta2/{parent=projects/*/locations/*/secrets/*}:addVersion:\x01*\x12\xd6\x01\n\tGetSecret\x124.google.cloud.secretmanager.v1beta2.GetSecretRequest\x1a*.google.cloud.secretmanager.v1beta2.Secret"g\xdaA\x04name\x82\xd3\xe4\x93\x02Z\x12$/v1beta2/{name=projects/*/secrets/*}Z2\x120/v1beta2/{name=projects/*/locations/*/secrets/*}\x12\x89\x02\n\x0cUpdateSecret\x127.google.cloud.secretmanager.v1beta2.UpdateSecretRequest\x1a*.google.cloud.secretmanager.v1beta2.Secret"\x93\x01\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x02x2+/v1beta2/{secret.name=projects/*/secrets/*}:\x06secretZA27/v1beta2/{secret.name=projects/*/locations/*/secrets/*}:\x06secret\x12\xc8\x01\n\x0cDeleteSecret\x127.google.cloud.secretmanager.v1beta2.DeleteSecretRequest\x1a\x16.google.protobuf.Empty"g\xdaA\x04name\x82\xd3\xe4\x93\x02Z*$/v1beta2/{name=projects/*/secrets/*}Z2*0/v1beta2/{name=projects/*/locations/*/secrets/*}\x12\x94\x02\n\x12ListSecretVersions\x12=.google.cloud.secretmanager.v1beta2.ListSecretVersionsRequest\x1a>.google.cloud.secretmanager.v1beta2.ListSecretVersionsResponse"\x7f\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12//v1beta2/{parent=projects/*/secrets/*}/versionsZ=\x12;/v1beta2/{parent=projects/*/locations/*/secrets/*}/versions\x12\x81\x02\n\x10GetSecretVersion\x12;.google.cloud.secretmanager.v1beta2.GetSecretVersionRequest\x1a1.google.cloud.secretmanager.v1beta2.SecretVersion"}\xdaA\x04name\x82\xd3\xe4\x93\x02p\x12//v1beta2/{name=projects/*/secrets/*/versions/*}Z=\x12;/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}\x12\xa4\x02\n\x13AccessSecretVersion\x12>.google.cloud.secretmanager.v1beta2.AccessSecretVersionRequest\x1a?.google.cloud.secretmanager.v1beta2.AccessSecretVersionResponse"\x8b\x01\xdaA\x04name\x82\xd3\xe4\x93\x02~\x126/v1beta2/{name=projects/*/secrets/*/versions/*}:accessZD\x12B/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:access\x12\xa1\x02\n\x14DisableSecretVersion\x12?.google.cloud.secretmanager.v1beta2.DisableSecretVersionRequest\x1a1.google.cloud.secretmanager.v1beta2.SecretVersion"\x94\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01"7/v1beta2/{name=projects/*/secrets/*/versions/*}:disable:\x01*ZH"C/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:disable:\x01*\x12\x9d\x02\n\x13EnableSecretVersion\x12>.google.cloud.secretmanager.v1beta2.EnableSecretVersionRequest\x1a1.google.cloud.secretmanager.v1beta2.SecretVersion"\x92\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x84\x01"6/v1beta2/{name=projects/*/secrets/*/versions/*}:enable:\x01*ZG"B/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:enable:\x01*\x12\xa1\x02\n\x14DestroySecretVersion\x12?.google.cloud.secretmanager.v1beta2.DestroySecretVersionRequest\x1a1.google.cloud.secretmanager.v1beta2.SecretVersion"\x94\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01"7/v1beta2/{name=projects/*/secrets/*/versions/*}:destroy:\x01*ZH"C/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:destroy:\x01*\x12\xd5\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x89\x01\x82\xd3\xe4\x93\x02\x82\x01"5/v1beta2/{resource=projects/*/secrets/*}:setIamPolicy:\x01*ZF"A/v1beta2/{resource=projects/*/locations/*/secrets/*}:setIamPolicy:\x01*\x12\xce\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"\x82\x01\x82\xd3\xe4\x93\x02|\x125/v1beta2/{resource=projects/*/secrets/*}:getIamPolicyZC\x12A/v1beta2/{resource=projects/*/locations/*/secrets/*}:getIamPolicy\x12\x81\x02\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\x95\x01\x82\xd3\xe4\x93\x02\x8e\x01";/v1beta2/{resource=projects/*/secrets/*}:testIamPermissions:\x01*ZL"G/v1beta2/{resource=projects/*/locations/*/secrets/*}:testIamPermissions:\x01*\x1aP\xcaA\x1csecretmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfe\x01\n&com.google.cloud.secretmanager.v1beta2B\x0cServiceProtoP\x01ZLcloud.google.com/go/secretmanager/apiv1beta2/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta2\xca\x02"Google\\Cloud\\SecretManager\\V1beta2\xea\x02%Google::Cloud::SecretManager::V1beta2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secretmanager.v1beta2.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.secretmanager.v1beta2B\x0cServiceProtoP\x01ZLcloud.google.com/go/secretmanager/apiv1beta2/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02"Google.Cloud.SecretManager.V1Beta2\xca\x02"Google\\Cloud\\SecretManager\\V1beta2\xea\x02%Google::Cloud::SecretManager::V1beta2'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSECRETSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CREATESECRETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret'
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret_id']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret']._loaded_options = None
    _globals['_CREATESECRETREQUEST'].fields_by_name['secret']._serialized_options = b'\xe0A\x02'
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_ADDSECRETVERSIONREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x02'
    _globals['_GETSECRETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSECRETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSECRETVERSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_GETSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_UPDATESECRETREQUEST'].fields_by_name['secret']._loaded_options = None
    _globals['_UPDATESECRETREQUEST'].fields_by_name['secret']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESECRETREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESECRETREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_ACCESSSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_ACCESSSECRETVERSIONRESPONSE'].fields_by_name['name']._loaded_options = None
    _globals['_ACCESSSECRETVERSIONRESPONSE'].fields_by_name['name']._serialized_options = b'\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_DELETESECRETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESECRETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret'
    _globals['_DELETESECRETREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETESECRETREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DISABLESECRETVERSIONREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_ENABLESECRETVERSIONREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DESTROYSECRETVERSIONREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_SECRETMANAGERSERVICE']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE']._serialized_options = b'\xcaA\x1csecretmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecrets']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecrets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02Z\x12$/v1beta2/{parent=projects/*}/secretsZ2\x120/v1beta2/{parent=projects/*/locations/*}/secrets'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._serialized_options = b'\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02j"$/v1beta2/{parent=projects/*}/secrets:\x06secretZ:"0/v1beta2/{parent=projects/*/locations/*}/secrets:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._serialized_options = b'\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x02z"1/v1beta2/{parent=projects/*/secrets/*}:addVersion:\x01*ZB"=/v1beta2/{parent=projects/*/locations/*/secrets/*}:addVersion:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Z\x12$/v1beta2/{name=projects/*/secrets/*}Z2\x120/v1beta2/{name=projects/*/locations/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._serialized_options = b'\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x02x2+/v1beta2/{secret.name=projects/*/secrets/*}:\x06secretZA27/v1beta2/{secret.name=projects/*/locations/*/secrets/*}:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02Z*$/v1beta2/{name=projects/*/secrets/*}Z2*0/v1beta2/{name=projects/*/locations/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02p\x12//v1beta2/{parent=projects/*/secrets/*}/versionsZ=\x12;/v1beta2/{parent=projects/*/locations/*/secrets/*}/versions'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02p\x12//v1beta2/{name=projects/*/secrets/*/versions/*}Z=\x12;/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02~\x126/v1beta2/{name=projects/*/secrets/*/versions/*}:accessZD\x12B/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:access'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01"7/v1beta2/{name=projects/*/secrets/*/versions/*}:disable:\x01*ZH"C/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:disable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x84\x01"6/v1beta2/{name=projects/*/secrets/*/versions/*}:enable:\x01*ZG"B/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:enable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x86\x01"7/v1beta2/{name=projects/*/secrets/*/versions/*}:destroy:\x01*ZH"C/v1beta2/{name=projects/*/locations/*/secrets/*/versions/*}:destroy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02\x82\x01"5/v1beta2/{resource=projects/*/secrets/*}:setIamPolicy:\x01*ZF"A/v1beta2/{resource=projects/*/locations/*/secrets/*}:setIamPolicy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02|\x125/v1beta2/{resource=projects/*/secrets/*}:getIamPolicyZC\x12A/v1beta2/{resource=projects/*/locations/*/secrets/*}:getIamPolicy'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x8e\x01";/v1beta2/{resource=projects/*/secrets/*}:testIamPermissions:\x01*ZL"G/v1beta2/{resource=projects/*/locations/*/secrets/*}:testIamPermissions:\x01*'
    _globals['_LISTSECRETSREQUEST']._serialized_start = 379
    _globals['_LISTSECRETSREQUEST']._serialized_end = 530
    _globals['_LISTSECRETSRESPONSE']._serialized_start = 532
    _globals['_LISTSECRETSRESPONSE']._serialized_end = 659
    _globals['_CREATESECRETREQUEST']._serialized_start = 662
    _globals['_CREATESECRETREQUEST']._serialized_end = 833
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_start = 836
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_end = 995
    _globals['_GETSECRETREQUEST']._serialized_start = 997
    _globals['_GETSECRETREQUEST']._serialized_end = 1074
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_start = 1077
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_end = 1235
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_start = 1238
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_end = 1380
    _globals['_GETSECRETVERSIONREQUEST']._serialized_start = 1382
    _globals['_GETSECRETVERSIONREQUEST']._serialized_end = 1473
    _globals['_UPDATESECRETREQUEST']._serialized_start = 1476
    _globals['_UPDATESECRETREQUEST']._serialized_end = 1616
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_start = 1618
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_end = 1712
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_start = 1715
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_end = 1875
    _globals['_DELETESECRETREQUEST']._serialized_start = 1877
    _globals['_DELETESECRETREQUEST']._serialized_end = 1976
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_start = 1978
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_end = 2092
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_start = 2094
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_end = 2207
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_start = 2209
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_end = 2323
    _globals['_SECRETMANAGERSERVICE']._serialized_start = 2326
    _globals['_SECRETMANAGERSERVICE']._serialized_end = 6285