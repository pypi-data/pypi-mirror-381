"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/secretmanager/v1/service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.secretmanager.v1 import resources_pb2 as google_dot_cloud_dot_secretmanager_dot_v1_dot_resources__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/secretmanager/v1/service.proto\x12\x1dgoogle.cloud.secretmanager.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/secretmanager/v1/resources.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x97\x01\n\x12ListSecretsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"z\n\x13ListSecretsResponse\x126\n\x07secrets\x18\x01 \x03(\x0b2%.google.cloud.secretmanager.v1.Secret\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\xa6\x01\n\x13CreateSecretRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#secretmanager.googleapis.com/Secret\x12\x16\n\tsecret_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12:\n\x06secret\x18\x03 \x01(\x0b2%.google.cloud.secretmanager.v1.SecretB\x03\xe0A\x02"\x9a\x01\n\x17AddSecretVersionRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12B\n\x07payload\x18\x02 \x01(\x0b2,.google.cloud.secretmanager.v1.SecretPayloadB\x03\xe0A\x02"M\n\x10GetSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret"\x9e\x01\n\x19ListSecretVersionsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"\x89\x01\n\x1aListSecretVersionsResponse\x12>\n\x08versions\x18\x01 \x03(\x0b2,.google.cloud.secretmanager.v1.SecretVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"[\n\x17GetSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\x87\x01\n\x13UpdateSecretRequest\x12:\n\x06secret\x18\x01 \x01(\x0b2%.google.cloud.secretmanager.v1.SecretB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"^\n\x1aAccessSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion"\x9b\x01\n\x1bAccessSecretVersionResponse\x12=\n\x04name\x18\x01 \x01(\tB/\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12=\n\x07payload\x18\x02 \x01(\x0b2,.google.cloud.secretmanager.v1.SecretPayload"c\n\x13DeleteSecretRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#secretmanager.googleapis.com/Secret\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"r\n\x1bDisableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"q\n\x1aEnableSecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"r\n\x1bDestroySecretVersionRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x012\xe8\x1c\n\x14SecretManagerService\x12\xd5\x01\n\x0bListSecrets\x121.google.cloud.secretmanager.v1.ListSecretsRequest\x1a2.google.cloud.secretmanager.v1.ListSecretsResponse"_\xdaA\x06parent\x82\xd3\xe4\x93\x02P\x12\x1f/v1/{parent=projects/*}/secretsZ-\x12+/v1/{parent=projects/*/locations/*}/secrets\x12\xec\x01\n\x0cCreateSecret\x122.google.cloud.secretmanager.v1.CreateSecretRequest\x1a%.google.cloud.secretmanager.v1.Secret"\x80\x01\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02`"\x1f/v1/{parent=projects/*}/secrets:\x06secretZ5"+/v1/{parent=projects/*/locations/*}/secrets:\x06secret\x12\x82\x02\n\x10AddSecretVersion\x126.google.cloud.secretmanager.v1.AddSecretVersionRequest\x1a,.google.cloud.secretmanager.v1.SecretVersion"\x87\x01\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x02p",/v1/{parent=projects/*/secrets/*}:addVersion:\x01*Z="8/v1/{parent=projects/*/locations/*/secrets/*}:addVersion:\x01*\x12\xc2\x01\n\tGetSecret\x12/.google.cloud.secretmanager.v1.GetSecretRequest\x1a%.google.cloud.secretmanager.v1.Secret"]\xdaA\x04name\x82\xd3\xe4\x93\x02P\x12\x1f/v1/{name=projects/*/secrets/*}Z-\x12+/v1/{name=projects/*/locations/*/secrets/*}\x12\xf5\x01\n\x0cUpdateSecret\x122.google.cloud.secretmanager.v1.UpdateSecretRequest\x1a%.google.cloud.secretmanager.v1.Secret"\x89\x01\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x02n2&/v1/{secret.name=projects/*/secrets/*}:\x06secretZ<22/v1/{secret.name=projects/*/locations/*/secrets/*}:\x06secret\x12\xb9\x01\n\x0cDeleteSecret\x122.google.cloud.secretmanager.v1.DeleteSecretRequest\x1a\x16.google.protobuf.Empty"]\xdaA\x04name\x82\xd3\xe4\x93\x02P*\x1f/v1/{name=projects/*/secrets/*}Z-*+/v1/{name=projects/*/locations/*/secrets/*}\x12\x80\x02\n\x12ListSecretVersions\x128.google.cloud.secretmanager.v1.ListSecretVersionsRequest\x1a9.google.cloud.secretmanager.v1.ListSecretVersionsResponse"u\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v1/{parent=projects/*/secrets/*}/versionsZ8\x126/v1/{parent=projects/*/locations/*/secrets/*}/versions\x12\xed\x01\n\x10GetSecretVersion\x126.google.cloud.secretmanager.v1.GetSecretVersionRequest\x1a,.google.cloud.secretmanager.v1.SecretVersion"s\xdaA\x04name\x82\xd3\xe4\x93\x02f\x12*/v1/{name=projects/*/secrets/*/versions/*}Z8\x126/v1/{name=projects/*/locations/*/secrets/*/versions/*}\x12\x90\x02\n\x13AccessSecretVersion\x129.google.cloud.secretmanager.v1.AccessSecretVersionRequest\x1a:.google.cloud.secretmanager.v1.AccessSecretVersionResponse"\x81\x01\xdaA\x04name\x82\xd3\xe4\x93\x02t\x121/v1/{name=projects/*/secrets/*/versions/*}:accessZ?\x12=/v1/{name=projects/*/locations/*/secrets/*/versions/*}:access\x12\x8c\x02\n\x14DisableSecretVersion\x12:.google.cloud.secretmanager.v1.DisableSecretVersionRequest\x1a,.google.cloud.secretmanager.v1.SecretVersion"\x89\x01\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v1/{name=projects/*/secrets/*/versions/*}:disable:\x01*ZC">/v1/{name=projects/*/locations/*/secrets/*/versions/*}:disable:\x01*\x12\x88\x02\n\x13EnableSecretVersion\x129.google.cloud.secretmanager.v1.EnableSecretVersionRequest\x1a,.google.cloud.secretmanager.v1.SecretVersion"\x87\x01\xdaA\x04name\x82\xd3\xe4\x93\x02z"1/v1/{name=projects/*/secrets/*/versions/*}:enable:\x01*ZB"=/v1/{name=projects/*/locations/*/secrets/*/versions/*}:enable:\x01*\x12\x8c\x02\n\x14DestroySecretVersion\x12:.google.cloud.secretmanager.v1.DestroySecretVersionRequest\x1a,.google.cloud.secretmanager.v1.SecretVersion"\x89\x01\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v1/{name=projects/*/secrets/*/versions/*}:destroy:\x01*ZC">/v1/{name=projects/*/locations/*/secrets/*/versions/*}:destroy:\x01*\x12\xc9\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"~\x82\xd3\xe4\x93\x02x"0/v1/{resource=projects/*/secrets/*}:setIamPolicy:\x01*ZA"</v1/{resource=projects/*/locations/*/secrets/*}:setIamPolicy:\x01*\x12\xc3\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"x\x82\xd3\xe4\x93\x02r\x120/v1/{resource=projects/*/secrets/*}:getIamPolicyZ>\x12</v1/{resource=projects/*/locations/*/secrets/*}:getIamPolicy\x12\xf7\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"\x8b\x01\x82\xd3\xe4\x93\x02\x84\x01"6/v1/{resource=projects/*/secrets/*}:testIamPermissions:\x01*ZG"B/v1/{resource=projects/*/locations/*/secrets/*}:testIamPermissions:\x01*\x1aP\xcaA\x1csecretmanager.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe5\x01\n!com.google.cloud.secretmanager.v1B\x0cServiceProtoP\x01ZGcloud.google.com/go/secretmanager/apiv1/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02\x1dGoogle.Cloud.SecretManager.V1\xca\x02\x1dGoogle\\Cloud\\SecretManager\\V1\xea\x02 Google::Cloud::SecretManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.secretmanager.v1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n!com.google.cloud.secretmanager.v1B\x0cServiceProtoP\x01ZGcloud.google.com/go/secretmanager/apiv1/secretmanagerpb;secretmanagerpb\xa2\x02\x03GSM\xaa\x02\x1dGoogle.Cloud.SecretManager.V1\xca\x02\x1dGoogle\\Cloud\\SecretManager\\V1\xea\x02 Google::Cloud::SecretManager::V1'
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
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecrets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02P\x12\x1f/v1/{parent=projects/*}/secretsZ-\x12+/v1/{parent=projects/*/locations/*}/secrets'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['CreateSecret']._serialized_options = b'\xdaA\x17parent,secret_id,secret\x82\xd3\xe4\x93\x02`"\x1f/v1/{parent=projects/*}/secrets:\x06secretZ5"+/v1/{parent=projects/*/locations/*}/secrets:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AddSecretVersion']._serialized_options = b'\xdaA\x0eparent,payload\x82\xd3\xe4\x93\x02p",/v1/{parent=projects/*/secrets/*}:addVersion:\x01*Z="8/v1/{parent=projects/*/locations/*/secrets/*}:addVersion:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02P\x12\x1f/v1/{name=projects/*/secrets/*}Z-\x12+/v1/{name=projects/*/locations/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['UpdateSecret']._serialized_options = b'\xdaA\x12secret,update_mask\x82\xd3\xe4\x93\x02n2&/v1/{secret.name=projects/*/secrets/*}:\x06secretZ<22/v1/{secret.name=projects/*/locations/*/secrets/*}:\x06secret'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DeleteSecret']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02P*\x1f/v1/{name=projects/*/secrets/*}Z-*+/v1/{name=projects/*/locations/*/secrets/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['ListSecretVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02f\x12*/v1/{parent=projects/*/secrets/*}/versionsZ8\x126/v1/{parent=projects/*/locations/*/secrets/*}/versions'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02f\x12*/v1/{name=projects/*/secrets/*/versions/*}Z8\x126/v1/{name=projects/*/locations/*/secrets/*/versions/*}'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['AccessSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02t\x121/v1/{name=projects/*/secrets/*/versions/*}:accessZ?\x12=/v1/{name=projects/*/locations/*/secrets/*/versions/*}:access'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DisableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v1/{name=projects/*/secrets/*/versions/*}:disable:\x01*ZC">/v1/{name=projects/*/locations/*/secrets/*/versions/*}:disable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['EnableSecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02z"1/v1/{name=projects/*/secrets/*/versions/*}:enable:\x01*ZB"=/v1/{name=projects/*/locations/*/secrets/*/versions/*}:enable:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['DestroySecretVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02|"2/v1/{name=projects/*/secrets/*/versions/*}:destroy:\x01*ZC">/v1/{name=projects/*/locations/*/secrets/*/versions/*}:destroy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['SetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02x"0/v1/{resource=projects/*/secrets/*}:setIamPolicy:\x01*ZA"</v1/{resource=projects/*/locations/*/secrets/*}:setIamPolicy:\x01*'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['GetIamPolicy']._serialized_options = b'\x82\xd3\xe4\x93\x02r\x120/v1/{resource=projects/*/secrets/*}:getIamPolicyZ>\x12</v1/{resource=projects/*/locations/*/secrets/*}:getIamPolicy'
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_SECRETMANAGERSERVICE'].methods_by_name['TestIamPermissions']._serialized_options = b'\x82\xd3\xe4\x93\x02\x84\x01"6/v1/{resource=projects/*/secrets/*}:testIamPermissions:\x01*ZG"B/v1/{resource=projects/*/locations/*/secrets/*}:testIamPermissions:\x01*'
    _globals['_LISTSECRETSREQUEST']._serialized_start = 364
    _globals['_LISTSECRETSREQUEST']._serialized_end = 515
    _globals['_LISTSECRETSRESPONSE']._serialized_start = 517
    _globals['_LISTSECRETSRESPONSE']._serialized_end = 639
    _globals['_CREATESECRETREQUEST']._serialized_start = 642
    _globals['_CREATESECRETREQUEST']._serialized_end = 808
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_start = 811
    _globals['_ADDSECRETVERSIONREQUEST']._serialized_end = 965
    _globals['_GETSECRETREQUEST']._serialized_start = 967
    _globals['_GETSECRETREQUEST']._serialized_end = 1044
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_start = 1047
    _globals['_LISTSECRETVERSIONSREQUEST']._serialized_end = 1205
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_start = 1208
    _globals['_LISTSECRETVERSIONSRESPONSE']._serialized_end = 1345
    _globals['_GETSECRETVERSIONREQUEST']._serialized_start = 1347
    _globals['_GETSECRETVERSIONREQUEST']._serialized_end = 1438
    _globals['_UPDATESECRETREQUEST']._serialized_start = 1441
    _globals['_UPDATESECRETREQUEST']._serialized_end = 1576
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_start = 1578
    _globals['_ACCESSSECRETVERSIONREQUEST']._serialized_end = 1672
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_start = 1675
    _globals['_ACCESSSECRETVERSIONRESPONSE']._serialized_end = 1830
    _globals['_DELETESECRETREQUEST']._serialized_start = 1832
    _globals['_DELETESECRETREQUEST']._serialized_end = 1931
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_start = 1933
    _globals['_DISABLESECRETVERSIONREQUEST']._serialized_end = 2047
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_start = 2049
    _globals['_ENABLESECRETVERSIONREQUEST']._serialized_end = 2162
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_start = 2164
    _globals['_DESTROYSECRETVERSIONREQUEST']._serialized_end = 2278
    _globals['_SECRETMANAGERSERVICE']._serialized_start = 2281
    _globals['_SECRETMANAGERSERVICE']._serialized_end = 5969