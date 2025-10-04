"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/security/publicca/v1alpha1/service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.security.publicca.v1alpha1 import resources_pb2 as google_dot_cloud_dot_security_dot_publicca_dot_v1alpha1_dot_resources__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/security/publicca/v1alpha1/service.proto\x12\'google.cloud.security.publicca.v1alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/security/publicca/v1alpha1/resources.proto"\xc5\x01\n\x1fCreateExternalAccountKeyRequest\x12B\n\x06parent\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\x12*publicca.googleapis.com/ExternalAccountKey\x12^\n\x14external_account_key\x18\x02 \x01(\x0b2;.google.cloud.security.publicca.v1alpha1.ExternalAccountKeyB\x03\xe0A\x022\x8f\x03\n!PublicCertificateAuthorityService\x12\x9c\x02\n\x18CreateExternalAccountKey\x12H.google.cloud.security.publicca.v1alpha1.CreateExternalAccountKeyRequest\x1a;.google.cloud.security.publicca.v1alpha1.ExternalAccountKey"y\xdaA\x1bparent,external_account_key\x82\xd3\xe4\x93\x02U"=/v1alpha1/{parent=projects/*/locations/*}/externalAccountKeys:\x14external_account_key\x1aK\xcaA\x17publicca.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x88\x02\n+com.google.cloud.security.publicca.v1alpha1B\x0cServiceProtoP\x01ZGcloud.google.com/go/security/publicca/apiv1alpha1/publiccapb;publiccapb\xaa\x02\'Google.Cloud.Security.PublicCA.V1Alpha1\xca\x02\'Google\\Cloud\\Security\\PublicCA\\V1alpha1\xea\x02+Google::Cloud::Security::PublicCA::V1alpha1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.security.publicca.v1alpha1.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.security.publicca.v1alpha1B\x0cServiceProtoP\x01ZGcloud.google.com/go/security/publicca/apiv1alpha1/publiccapb;publiccapb\xaa\x02'Google.Cloud.Security.PublicCA.V1Alpha1\xca\x02'Google\\Cloud\\Security\\PublicCA\\V1alpha1\xea\x02+Google::Cloud::Security::PublicCA::V1alpha1"
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*publicca.googleapis.com/ExternalAccountKey'
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST'].fields_by_name['external_account_key']._loaded_options = None
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST'].fields_by_name['external_account_key']._serialized_options = b'\xe0A\x02'
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE']._loaded_options = None
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE']._serialized_options = b'\xcaA\x17publicca.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE'].methods_by_name['CreateExternalAccountKey']._loaded_options = None
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE'].methods_by_name['CreateExternalAccountKey']._serialized_options = b'\xdaA\x1bparent,external_account_key\x82\xd3\xe4\x93\x02U"=/v1alpha1/{parent=projects/*/locations/*}/externalAccountKeys:\x14external_account_key'
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST']._serialized_start = 271
    _globals['_CREATEEXTERNALACCOUNTKEYREQUEST']._serialized_end = 468
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE']._serialized_start = 471
    _globals['_PUBLICCERTIFICATEAUTHORITYSERVICE']._serialized_end = 870