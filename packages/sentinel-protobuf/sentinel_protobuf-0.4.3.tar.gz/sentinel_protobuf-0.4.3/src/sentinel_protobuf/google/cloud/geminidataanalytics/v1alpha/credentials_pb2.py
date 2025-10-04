"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1alpha/credentials.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/geminidataanalytics/v1alpha/credentials.proto\x12(google.cloud.geminidataanalytics.v1alpha\x1a\x1fgoogle/api/field_behavior.proto"b\n\x0bCredentials\x12K\n\x05oauth\x18\x01 \x01(\x0b2:.google.cloud.geminidataanalytics.v1alpha.OAuthCredentialsH\x00B\x06\n\x04kind"\xb8\x02\n\x10OAuthCredentials\x12X\n\x06secret\x18\x02 \x01(\x0b2F.google.cloud.geminidataanalytics.v1alpha.OAuthCredentials.SecretBasedH\x00\x12V\n\x05token\x18\x03 \x01(\x0b2E.google.cloud.geminidataanalytics.v1alpha.OAuthCredentials.TokenBasedH\x00\x1aA\n\x0bSecretBased\x12\x16\n\tclient_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rclient_secret\x18\x03 \x01(\tB\x03\xe0A\x02\x1a\'\n\nTokenBased\x12\x19\n\x0caccess_token\x18\x01 \x01(\tB\x03\xe0A\x02B\x06\n\x04kindB\xa6\x02\n,com.google.cloud.geminidataanalytics.v1alphaB\x10CredentialsProtoP\x01Z^cloud.google.com/go/geminidataanalytics/apiv1alpha/geminidataanalyticspb;geminidataanalyticspb\xaa\x02(Google.Cloud.GeminiDataAnalytics.V1Alpha\xca\x02(Google\\Cloud\\GeminiDataAnalytics\\V1alpha\xea\x02+Google::Cloud::GeminiDataAnalytics::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1alpha.credentials_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.geminidataanalytics.v1alphaB\x10CredentialsProtoP\x01Z^cloud.google.com/go/geminidataanalytics/apiv1alpha/geminidataanalyticspb;geminidataanalyticspb\xaa\x02(Google.Cloud.GeminiDataAnalytics.V1Alpha\xca\x02(Google\\Cloud\\GeminiDataAnalytics\\V1alpha\xea\x02+Google::Cloud::GeminiDataAnalytics::V1alpha'
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_id']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_secret']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x02'
    _globals['_OAUTHCREDENTIALS_TOKENBASED'].fields_by_name['access_token']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_TOKENBASED'].fields_by_name['access_token']._serialized_options = b'\xe0A\x02'
    _globals['_CREDENTIALS']._serialized_start = 137
    _globals['_CREDENTIALS']._serialized_end = 235
    _globals['_OAUTHCREDENTIALS']._serialized_start = 238
    _globals['_OAUTHCREDENTIALS']._serialized_end = 550
    _globals['_OAUTHCREDENTIALS_SECRETBASED']._serialized_start = 436
    _globals['_OAUTHCREDENTIALS_SECRETBASED']._serialized_end = 501
    _globals['_OAUTHCREDENTIALS_TOKENBASED']._serialized_start = 503
    _globals['_OAUTHCREDENTIALS_TOKENBASED']._serialized_end = 542