"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/credentials.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/geminidataanalytics/v1beta/credentials.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1fgoogle/api/field_behavior.proto"a\n\x0bCredentials\x12J\n\x05oauth\x18\x01 \x01(\x0b29.google.cloud.geminidataanalytics.v1beta.OAuthCredentialsH\x00B\x06\n\x04kind"\xb6\x02\n\x10OAuthCredentials\x12W\n\x06secret\x18\x02 \x01(\x0b2E.google.cloud.geminidataanalytics.v1beta.OAuthCredentials.SecretBasedH\x00\x12U\n\x05token\x18\x03 \x01(\x0b2D.google.cloud.geminidataanalytics.v1beta.OAuthCredentials.TokenBasedH\x00\x1aA\n\x0bSecretBased\x12\x16\n\tclient_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rclient_secret\x18\x03 \x01(\tB\x03\xe0A\x02\x1a\'\n\nTokenBased\x12\x19\n\x0caccess_token\x18\x01 \x01(\tB\x03\xe0A\x02B\x06\n\x04kindB\xa1\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x10CredentialsProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.credentials_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x10CredentialsProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_id']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_secret']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_SECRETBASED'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x02'
    _globals['_OAUTHCREDENTIALS_TOKENBASED'].fields_by_name['access_token']._loaded_options = None
    _globals['_OAUTHCREDENTIALS_TOKENBASED'].fields_by_name['access_token']._serialized_options = b'\xe0A\x02'
    _globals['_CREDENTIALS']._serialized_start = 135
    _globals['_CREDENTIALS']._serialized_end = 232
    _globals['_OAUTHCREDENTIALS']._serialized_start = 235
    _globals['_OAUTHCREDENTIALS']._serialized_end = 545
    _globals['_OAUTHCREDENTIALS_SECRETBASED']._serialized_start = 431
    _globals['_OAUTHCREDENTIALS_SECRETBASED']._serialized_end = 496
    _globals['_OAUTHCREDENTIALS_TOKENBASED']._serialized_start = 498
    _globals['_OAUTHCREDENTIALS_TOKENBASED']._serialized_end = 537