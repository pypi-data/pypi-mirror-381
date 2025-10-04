"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/extension.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import tool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_tool__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/aiplatform/v1beta1/extension.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/aiplatform/v1beta1/tool.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x06\n\tExtension\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x07 \x01(\tB\x03\xe0A\x01\x12I\n\x08manifest\x18\t \x01(\x0b22.google.cloud.aiplatform.v1beta1.ExtensionManifestB\x03\xe0A\x02\x12V\n\x14extension_operations\x18\x0b \x03(\x0b23.google.cloud.aiplatform.v1beta1.ExtensionOperationB\x03\xe0A\x03\x12K\n\x0eruntime_config\x18\r \x01(\x0b2..google.cloud.aiplatform.v1beta1.RuntimeConfigB\x03\xe0A\x01\x12O\n\x11tool_use_examples\x18\x0f \x03(\x0b2/.google.cloud.aiplatform.v1beta1.ToolUseExampleB\x03\xe0A\x01\x12r\n\x1eprivate_service_connect_config\x18\x10 \x01(\x0b2E.google.cloud.aiplatform.v1beta1.ExtensionPrivateServiceConnectConfigB\x03\xe0A\x01:\x7f\xeaA|\n#aiplatform.googleapis.com/Extension\x12>projects/{project}/locations/{location}/extensions/{extension}*\nextensions2\textension"\xac\x02\n\x11ExtensionManifest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x02\x12T\n\x08api_spec\x18\x03 \x01(\x0b2:.google.cloud.aiplatform.v1beta1.ExtensionManifest.ApiSpecB\x06\xe0A\x05\xe0A\x02\x12H\n\x0bauth_config\x18\x05 \x01(\x0b2+.google.cloud.aiplatform.v1beta1.AuthConfigB\x06\xe0A\x05\xe0A\x02\x1aJ\n\x07ApiSpec\x12\x17\n\ropen_api_yaml\x18\x01 \x01(\tH\x00\x12\x1a\n\x10open_api_gcs_uri\x18\x02 \x01(\tH\x00B\n\n\x08api_spec"\x83\x01\n\x12ExtensionOperation\x12\x14\n\x0coperation_id\x18\x01 \x01(\t\x12W\n\x14function_declaration\x18\x03 \x01(\x0b24.google.cloud.aiplatform.v1beta1.FunctionDeclarationB\x03\xe0A\x03"\xab\x08\n\nAuthConfig\x12R\n\x0eapi_key_config\x18\x02 \x01(\x0b28.google.cloud.aiplatform.v1beta1.AuthConfig.ApiKeyConfigH\x00\x12a\n\x16http_basic_auth_config\x18\x03 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.AuthConfig.HttpBasicAuthConfigH\x00\x12o\n\x1dgoogle_service_account_config\x18\x04 \x01(\x0b2F.google.cloud.aiplatform.v1beta1.AuthConfig.GoogleServiceAccountConfigH\x00\x12O\n\x0coauth_config\x18\x05 \x01(\x0b27.google.cloud.aiplatform.v1beta1.AuthConfig.OauthConfigH\x00\x12M\n\x0boidc_config\x18\x07 \x01(\x0b26.google.cloud.aiplatform.v1beta1.AuthConfig.OidcConfigH\x00\x12<\n\tauth_type\x18e \x01(\x0e2).google.cloud.aiplatform.v1beta1.AuthType\x1a\xc7\x01\n\x0cApiKeyConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12J\n\x0eapi_key_secret\x18\x02 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12X\n\x15http_element_location\x18\x03 \x01(\x0e24.google.cloud.aiplatform.v1beta1.HttpElementLocationB\x03\xe0A\x02\x1ad\n\x13HttpBasicAuthConfig\x12M\n\x11credential_secret\x18\x02 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x1a:\n\x1aGoogleServiceAccountConfig\x12\x1c\n\x0fservice_account\x18\x01 \x01(\tB\x03\xe0A\x01\x1aP\n\x0bOauthConfig\x12\x16\n\x0caccess_token\x18\x01 \x01(\tH\x00\x12\x19\n\x0fservice_account\x18\x02 \x01(\tH\x00B\x0e\n\x0coauth_config\x1aJ\n\nOidcConfig\x12\x12\n\x08id_token\x18\x01 \x01(\tH\x00\x12\x19\n\x0fservice_account\x18\x02 \x01(\tH\x00B\r\n\x0boidc_configB\r\n\x0bauth_config"\x99\x04\n\rRuntimeConfig\x12v\n\x1fcode_interpreter_runtime_config\x18\x02 \x01(\x0b2K.google.cloud.aiplatform.v1beta1.RuntimeConfig.CodeInterpreterRuntimeConfigH\x00\x12u\n\x1fvertex_ai_search_runtime_config\x18\x06 \x01(\x0b2J.google.cloud.aiplatform.v1beta1.RuntimeConfig.VertexAISearchRuntimeConfigH\x00\x124\n\x0edefault_params\x18\x04 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1ag\n\x1cCodeInterpreterRuntimeConfig\x12"\n\x15file_input_gcs_bucket\x18\x01 \x01(\tB\x03\xe0A\x01\x12#\n\x16file_output_gcs_bucket\x18\x02 \x01(\tB\x03\xe0A\x01\x1aW\n\x1bVertexAISearchRuntimeConfig\x12 \n\x13serving_config_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x16\n\tengine_id\x18\x02 \x01(\tB\x03\xe0A\x01B!\n\x1fGoogleFirstPartyExtensionConfig"r\n$ExtensionPrivateServiceConnectConfig\x12J\n\x11service_directory\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service*\x8d\x01\n\x13HttpElementLocation\x12\x17\n\x13HTTP_IN_UNSPECIFIED\x10\x00\x12\x11\n\rHTTP_IN_QUERY\x10\x01\x12\x12\n\x0eHTTP_IN_HEADER\x10\x02\x12\x10\n\x0cHTTP_IN_PATH\x10\x03\x12\x10\n\x0cHTTP_IN_BODY\x10\x04\x12\x12\n\x0eHTTP_IN_COOKIE\x10\x05*\x94\x01\n\x08AuthType\x12\x19\n\x15AUTH_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07NO_AUTH\x10\x01\x12\x10\n\x0cAPI_KEY_AUTH\x10\x02\x12\x13\n\x0fHTTP_BASIC_AUTH\x10\x03\x12\x1f\n\x1bGOOGLE_SERVICE_ACCOUNT_AUTH\x10\x04\x12\t\n\x05OAUTH\x10\x06\x12\r\n\tOIDC_AUTH\x10\x08B\xa7\x04\n#com.google.cloud.aiplatform.v1beta1B\x0eExtensionProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaA\xbf\x01\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}\x12Rprojects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.extension_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0eExtensionProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1\xeaA\xbf\x01\n*secretmanager.googleapis.com/SecretVersion\x12=projects/{project}/secrets/{secret}/versions/{secret_version}\x12Rprojects/{project}/locations/{location}/secrets/{secret}/versions/{secret_version}\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}'
    _globals['_EXTENSION'].fields_by_name['name']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_EXTENSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSION'].fields_by_name['description']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXTENSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXTENSION'].fields_by_name['etag']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSION'].fields_by_name['manifest']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['manifest']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSION'].fields_by_name['extension_operations']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['extension_operations']._serialized_options = b'\xe0A\x03'
    _globals['_EXTENSION'].fields_by_name['runtime_config']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['runtime_config']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSION'].fields_by_name['tool_use_examples']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['tool_use_examples']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSION'].fields_by_name['private_service_connect_config']._loaded_options = None
    _globals['_EXTENSION'].fields_by_name['private_service_connect_config']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSION']._loaded_options = None
    _globals['_EXTENSION']._serialized_options = b'\xeaA|\n#aiplatform.googleapis.com/Extension\x12>projects/{project}/locations/{location}/extensions/{extension}*\nextensions2\textension'
    _globals['_EXTENSIONMANIFEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXTENSIONMANIFEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONMANIFEST'].fields_by_name['description']._loaded_options = None
    _globals['_EXTENSIONMANIFEST'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONMANIFEST'].fields_by_name['api_spec']._loaded_options = None
    _globals['_EXTENSIONMANIFEST'].fields_by_name['api_spec']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_EXTENSIONMANIFEST'].fields_by_name['auth_config']._loaded_options = None
    _globals['_EXTENSIONMANIFEST'].fields_by_name['auth_config']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_EXTENSIONOPERATION'].fields_by_name['function_declaration']._loaded_options = None
    _globals['_EXTENSIONOPERATION'].fields_by_name['function_declaration']._serialized_options = b'\xe0A\x03'
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['api_key_secret']._loaded_options = None
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['api_key_secret']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['http_element_location']._loaded_options = None
    _globals['_AUTHCONFIG_APIKEYCONFIG'].fields_by_name['http_element_location']._serialized_options = b'\xe0A\x02'
    _globals['_AUTHCONFIG_HTTPBASICAUTHCONFIG'].fields_by_name['credential_secret']._loaded_options = None
    _globals['_AUTHCONFIG_HTTPBASICAUTHCONFIG'].fields_by_name['credential_secret']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_AUTHCONFIG_GOOGLESERVICEACCOUNTCONFIG'].fields_by_name['service_account']._loaded_options = None
    _globals['_AUTHCONFIG_GOOGLESERVICEACCOUNTCONFIG'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG'].fields_by_name['file_input_gcs_bucket']._loaded_options = None
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG'].fields_by_name['file_input_gcs_bucket']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG'].fields_by_name['file_output_gcs_bucket']._loaded_options = None
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG'].fields_by_name['file_output_gcs_bucket']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG'].fields_by_name['serving_config_name']._loaded_options = None
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG'].fields_by_name['serving_config_name']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG'].fields_by_name['engine_id']._loaded_options = None
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG'].fields_by_name['engine_id']._serialized_options = b'\xe0A\x01'
    _globals['_RUNTIMECONFIG'].fields_by_name['default_params']._loaded_options = None
    _globals['_RUNTIMECONFIG'].fields_by_name['default_params']._serialized_options = b'\xe0A\x01'
    _globals['_EXTENSIONPRIVATESERVICECONNECTCONFIG'].fields_by_name['service_directory']._loaded_options = None
    _globals['_EXTENSIONPRIVATESERVICECONNECTCONFIG'].fields_by_name['service_directory']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_HTTPELEMENTLOCATION']._serialized_start = 3194
    _globals['_HTTPELEMENTLOCATION']._serialized_end = 3335
    _globals['_AUTHTYPE']._serialized_start = 3338
    _globals['_AUTHTYPE']._serialized_end = 3486
    _globals['_EXTENSION']._serialized_start = 252
    _globals['_EXTENSION']._serialized_end = 1028
    _globals['_EXTENSIONMANIFEST']._serialized_start = 1031
    _globals['_EXTENSIONMANIFEST']._serialized_end = 1331
    _globals['_EXTENSIONMANIFEST_APISPEC']._serialized_start = 1257
    _globals['_EXTENSIONMANIFEST_APISPEC']._serialized_end = 1331
    _globals['_EXTENSIONOPERATION']._serialized_start = 1334
    _globals['_EXTENSIONOPERATION']._serialized_end = 1465
    _globals['_AUTHCONFIG']._serialized_start = 1468
    _globals['_AUTHCONFIG']._serialized_end = 2535
    _globals['_AUTHCONFIG_APIKEYCONFIG']._serialized_start = 2001
    _globals['_AUTHCONFIG_APIKEYCONFIG']._serialized_end = 2200
    _globals['_AUTHCONFIG_HTTPBASICAUTHCONFIG']._serialized_start = 2202
    _globals['_AUTHCONFIG_HTTPBASICAUTHCONFIG']._serialized_end = 2302
    _globals['_AUTHCONFIG_GOOGLESERVICEACCOUNTCONFIG']._serialized_start = 2304
    _globals['_AUTHCONFIG_GOOGLESERVICEACCOUNTCONFIG']._serialized_end = 2362
    _globals['_AUTHCONFIG_OAUTHCONFIG']._serialized_start = 2364
    _globals['_AUTHCONFIG_OAUTHCONFIG']._serialized_end = 2444
    _globals['_AUTHCONFIG_OIDCCONFIG']._serialized_start = 2446
    _globals['_AUTHCONFIG_OIDCCONFIG']._serialized_end = 2520
    _globals['_RUNTIMECONFIG']._serialized_start = 2538
    _globals['_RUNTIMECONFIG']._serialized_end = 3075
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG']._serialized_start = 2848
    _globals['_RUNTIMECONFIG_CODEINTERPRETERRUNTIMECONFIG']._serialized_end = 2951
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG']._serialized_start = 2953
    _globals['_RUNTIMECONFIG_VERTEXAISEARCHRUNTIMECONFIG']._serialized_end = 3040
    _globals['_EXTENSIONPRIVATESERVICECONNECTCONFIG']._serialized_start = 3077
    _globals['_EXTENSIONPRIVATESERVICECONNECTCONFIG']._serialized_end = 3191