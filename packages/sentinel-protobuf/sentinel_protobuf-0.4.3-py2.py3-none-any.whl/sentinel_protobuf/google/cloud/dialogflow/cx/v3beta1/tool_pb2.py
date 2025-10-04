"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3beta1/tool.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import data_store_connection_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_data__store__connection__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import inline_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_inline__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/dialogflow/cx/v3beta1/tool.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a>google/cloud/dialogflow/cx/v3beta1/data_store_connection.proto\x1a/google/cloud/dialogflow/cx/v3beta1/inline.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x88\x01\n\x11CreateToolRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x12;\n\x04tool\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.ToolB\x03\xe0A\x02"q\n\x10ListToolsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"e\n\x11ListToolsResponse\x127\n\x05tools\x18\x01 \x03(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Tool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"F\n\x0eGetToolRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool"\xed\x02\n\x12ExportToolsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool\x125\n\x05tools\x18\x02 \x03(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\x18\n\ttools_uri\x18\x03 \x01(\tB\x03\xe0A\x01H\x00\x12#\n\x14tools_content_inline\x18\x04 \x01(\x08B\x03\xe0A\x01H\x00\x12[\n\x0bdata_format\x18\x05 \x01(\x0e2A.google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest.DataFormatB\x03\xe0A\x01"=\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x08\n\x04JSON\x10\x02B\r\n\x0bdestination"\x83\x01\n\x13ExportToolsResponse\x12\x13\n\ttools_uri\x18\x01 \x01(\tH\x00\x12N\n\rtools_content\x18\x02 \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.InlineDestinationH\x00B\x07\n\x05tools"\x81\x01\n\x11UpdateToolRequest\x12;\n\x04tool\x18\x01 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.ToolB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"X\n\x11DeleteToolRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool\x12\r\n\x05force\x18\x02 \x01(\x08"\x9b \n\x04Tool\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x02\x12M\n\ropen_api_spec\x18\x04 \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.Tool.OpenApiToolH\x00\x12Q\n\x0fdata_store_spec\x18\x08 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.Tool.DataStoreToolH\x00\x12P\n\x0eextension_spec\x18\x0b \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.Tool.ExtensionToolH\x00\x12N\n\rfunction_spec\x18\r \x01(\x0b25.google.cloud.dialogflow.cx.v3beta1.Tool.FunctionToolH\x00\x12P\n\x0econnector_spec\x18\x0f \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.Tool.ConnectorToolH\x00\x12I\n\ttool_type\x18\x0c \x01(\x0e21.google.cloud.dialogflow.cx.v3beta1.Tool.ToolTypeB\x03\xe0A\x03\x1a\xbe\x02\n\x0bOpenApiTool\x12\x1a\n\x0btext_schema\x18\x01 \x01(\tB\x03\xe0A\x02H\x00\x12T\n\x0eauthentication\x18\x02 \x01(\x0b27.google.cloud.dialogflow.cx.v3beta1.Tool.AuthenticationB\x03\xe0A\x01\x12K\n\ntls_config\x18\x03 \x01(\x0b22.google.cloud.dialogflow.cx.v3beta1.Tool.TLSConfigB\x03\xe0A\x01\x12f\n\x18service_directory_config\x18\x04 \x01(\x0b2?.google.cloud.dialogflow.cx.v3beta1.Tool.ServiceDirectoryConfigB\x03\xe0A\x01B\x08\n\x06schema\x1a\xe4\x01\n\rDataStoreTool\x12\\\n\x16data_store_connections\x18\x01 \x03(\x0b27.google.cloud.dialogflow.cx.v3beta1.DataStoreConnectionB\x03\xe0A\x02\x12c\n\x0ffallback_prompt\x18\x03 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.Tool.DataStoreTool.FallbackPromptB\x03\xe0A\x02\x1a\x10\n\x0eFallbackPrompt\x1a"\n\rExtensionTool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x1aw\n\x0cFunctionTool\x122\n\x0cinput_schema\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x123\n\routput_schema\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a\xbb\x05\n\rConnectorTool\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\x07actions\x18\x02 \x03(\x0b2=.google.cloud.dialogflow.cx.v3beta1.Tool.ConnectorTool.ActionB\x03\xe0A\x02\x12]\n\x14end_user_auth_config\x18\x03 \x01(\x0b2:.google.cloud.dialogflow.cx.v3beta1.Tool.EndUserAuthConfigB\x03\xe0A\x01\x1a\xe2\x03\n\x06Action\x12\x1e\n\x14connection_action_id\x18\x04 \x01(\tH\x00\x12i\n\x10entity_operation\x18\x05 \x01(\x0b2M.google.cloud.dialogflow.cx.v3beta1.Tool.ConnectorTool.Action.EntityOperationH\x00\x12\x19\n\x0cinput_fields\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1a\n\routput_fields\x18\x03 \x03(\tB\x03\xe0A\x01\x1a\x86\x02\n\x0fEntityOperation\x12\x16\n\tentity_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12s\n\toperation\x18\x02 \x01(\x0e2[.google.cloud.dialogflow.cx.v3beta1.Tool.ConnectorTool.Action.EntityOperation.OperationTypeB\x03\xe0A\x02"f\n\rOperationType\x12\x1e\n\x1aOPERATION_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04LIST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\n\n\x06CREATE\x10\x03\x12\n\n\x06UPDATE\x10\x04\x12\n\n\x06DELETE\x10\x05B\r\n\x0baction_spec\x1a\x87\n\n\x0eAuthentication\x12^\n\x0eapi_key_config\x18\x01 \x01(\x0b2D.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ApiKeyConfigH\x00\x12[\n\x0coauth_config\x18\x02 \x01(\x0b2C.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.OAuthConfigH\x00\x12s\n\x19service_agent_auth_config\x18\x03 \x01(\x0b2N.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ServiceAgentAuthConfigH\x00\x12h\n\x13bearer_token_config\x18\x04 \x01(\x0b2I.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.BearerTokenConfigH\x00\x1a\xa3\x01\n\x0cApiKeyConfig\x12\x15\n\x08key_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07api_key\x18\x02 \x01(\tB\x03\xe0A\x01\x12f\n\x10request_location\x18\x03 \x01(\x0e2G.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.RequestLocationB\x03\xe0A\x02\x1a\xb1\x02\n\x0bOAuthConfig\x12q\n\x10oauth_grant_type\x18\x01 \x01(\x0e2R.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.OAuthConfig.OauthGrantTypeB\x03\xe0A\x02\x12\x16\n\tclient_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rclient_secret\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0etoken_endpoint\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06scopes\x18\x05 \x03(\tB\x03\xe0A\x01"I\n\x0eOauthGrantType\x12 \n\x1cOAUTH_GRANT_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11CLIENT_CREDENTIAL\x10\x01\x1a\xf3\x01\n\x16ServiceAgentAuthConfig\x12\x80\x01\n\x12service_agent_auth\x18\x01 \x01(\x0e2_.google.cloud.dialogflow.cx.v3beta1.Tool.Authentication.ServiceAgentAuthConfig.ServiceAgentAuthB\x03\xe0A\x01"V\n\x10ServiceAgentAuth\x12"\n\x1eSERVICE_AGENT_AUTH_UNSPECIFIED\x10\x00\x12\x0c\n\x08ID_TOKEN\x10\x01\x12\x10\n\x0cACCESS_TOKEN\x10\x02\x1a\'\n\x11BearerTokenConfig\x12\x12\n\x05token\x18\x01 \x01(\tB\x03\xe0A\x01"Q\n\x0fRequestLocation\x12 \n\x1cREQUEST_LOCATION_UNSPECIFIED\x10\x00\x12\n\n\x06HEADER\x10\x01\x12\x10\n\x0cQUERY_STRING\x10\x02B\r\n\x0bauth_config\x1a\x95\x01\n\tTLSConfig\x12P\n\x08ca_certs\x18\x01 \x03(\x0b29.google.cloud.dialogflow.cx.v3beta1.Tool.TLSConfig.CACertB\x03\xe0A\x02\x1a6\n\x06CACert\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04cert\x18\x02 \x01(\x0cB\x03\xe0A\x02\x1aZ\n\x16ServiceDirectoryConfig\x12@\n\x07service\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x1a\xa4\x03\n\x11EndUserAuthConfig\x12r\n\x17oauth2_auth_code_config\x18\x02 \x01(\x0b2O.google.cloud.dialogflow.cx.v3beta1.Tool.EndUserAuthConfig.Oauth2AuthCodeConfigH\x00\x12t\n\x18oauth2_jwt_bearer_config\x18\x03 \x01(\x0b2P.google.cloud.dialogflow.cx.v3beta1.Tool.EndUserAuthConfig.Oauth2JwtBearerConfigH\x00\x1a0\n\x14Oauth2AuthCodeConfig\x12\x18\n\x0boauth_token\x18\x01 \x01(\tB\x03\xe0A\x02\x1a[\n\x15Oauth2JwtBearerConfig\x12\x13\n\x06issuer\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07subject\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nclient_key\x18\x03 \x01(\tB\x03\xe0A\x02B\x16\n\x14end_user_auth_config"L\n\x08ToolType\x12\x19\n\x15TOOL_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fCUSTOMIZED_TOOL\x10\x01\x12\x10\n\x0cBUILTIN_TOOL\x10\x02:h\xeaAe\n\x1edialogflow.googleapis.com/Tool\x12Cprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}B\x0f\n\rspecification"\x89\x01\n\x17ListToolVersionsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/ToolVersion\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"{\n\x18ListToolVersionsResponse\x12F\n\rtool_versions\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.cx.v3beta1.ToolVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa5\x01\n\x18CreateToolVersionRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%dialogflow.googleapis.com/ToolVersion\x12J\n\x0ctool_version\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.ToolVersionB\x03\xe0A\x02"T\n\x15GetToolVersionRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/ToolVersion"k\n\x18DeleteToolVersionRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/ToolVersion\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"X\n\x19RestoreToolVersionRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%dialogflow.googleapis.com/ToolVersion"T\n\x1aRestoreToolVersionResponse\x126\n\x04tool\x18\x02 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.Tool"\x85\x03\n\x0bToolVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12;\n\x04tool\x18\x03 \x01(\x0b2(.google.cloud.dialogflow.cx.v3beta1.ToolB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\x9e\x01\xeaA\x9a\x01\n%dialogflow.googleapis.com/ToolVersion\x12Vprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}/versions/{version}*\x0ctoolVersions2\x0btoolVersion"\x15\n\x13ExportToolsMetadata2\xf0\x12\n\x05Tools\x12\xc2\x01\n\nCreateTool\x125.google.cloud.dialogflow.cx.v3beta1.CreateToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"S\xdaA\x0bparent,tool\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:\x04tool\x12\xc2\x01\n\tListTools\x124.google.cloud.dialogflow.cx.v3beta1.ListToolsRequest\x1a5.google.cloud.dialogflow.cx.v3beta1.ListToolsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/tools\x12\xdc\x01\n\x0bExportTools\x126.google.cloud.dialogflow.cx.v3beta1.ExportToolsRequest\x1a\x1d.google.longrunning.Operation"v\xcaA*\n\x13ExportToolsResponse\x12\x13ExportToolsMetadata\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:export:\x01*\x12\xaf\x01\n\x07GetTool\x122.google.cloud.dialogflow.cx.v3beta1.GetToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}\x12\xcc\x01\n\nUpdateTool\x125.google.cloud.dialogflow.cx.v3beta1.UpdateToolRequest\x1a(.google.cloud.dialogflow.cx.v3beta1.Tool"]\xdaA\x10tool,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{tool.name=projects/*/locations/*/agents/*/tools/*}:\x04tool\x12\xa3\x01\n\nDeleteTool\x125.google.cloud.dialogflow.cx.v3beta1.DeleteToolRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}\x12\xe2\x01\n\x10ListToolVersions\x12;.google.cloud.dialogflow.cx.v3beta1.ListToolVersionsRequest\x1a<.google.cloud.dialogflow.cx.v3beta1.ListToolVersionsResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{parent=projects/*/locations/*/agents/*/tools/*}/versions\x12\xf2\x01\n\x11CreateToolVersion\x12<.google.cloud.dialogflow.cx.v3beta1.CreateToolVersionRequest\x1a/.google.cloud.dialogflow.cx.v3beta1.ToolVersion"n\xdaA\x13parent,tool_version\x82\xd3\xe4\x93\x02R"B/v3beta1/{parent=projects/*/locations/*/agents/*/tools/*}/versions:\x0ctool_version\x12\xcf\x01\n\x0eGetToolVersion\x129.google.cloud.dialogflow.cx.v3beta1.GetToolVersionRequest\x1a/.google.cloud.dialogflow.cx.v3beta1.ToolVersion"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}\x12\xbc\x01\n\x11DeleteToolVersion\x12<.google.cloud.dialogflow.cx.v3beta1.DeleteToolVersionRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}\x12\xf1\x01\n\x12RestoreToolVersion\x12=.google.cloud.dialogflow.cx.v3beta1.RestoreToolVersionRequest\x1a>.google.cloud.dialogflow.cx.v3beta1.RestoreToolVersionResponse"\\\xdaA\x04name\x82\xd3\xe4\x93\x02O"J/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}:restore:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x97\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\tToolProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.tool_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\tToolProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1'
    _globals['_CREATETOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_CREATETOOLREQUEST'].fields_by_name['tool']._loaded_options = None
    _globals['_CREATETOOLREQUEST'].fields_by_name['tool']._serialized_options = b'\xe0A\x02'
    _globals['_LISTTOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_GETTOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_uri']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_content_inline']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['tools_content_inline']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_EXPORTTOOLSREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATETOOLREQUEST'].fields_by_name['tool']._loaded_options = None
    _globals['_UPDATETOOLREQUEST'].fields_by_name['tool']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['text_schema']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['text_schema']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['authentication']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['authentication']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['tls_config']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['tls_config']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['service_directory_config']._loaded_options = None
    _globals['_TOOL_OPENAPITOOL'].fields_by_name['service_directory_config']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['data_store_connections']._loaded_options = None
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['data_store_connections']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['fallback_prompt']._loaded_options = None
    _globals['_TOOL_DATASTORETOOL'].fields_by_name['fallback_prompt']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_EXTENSIONTOOL'].fields_by_name['name']._loaded_options = None
    _globals['_TOOL_EXTENSIONTOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['input_schema']._loaded_options = None
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['input_schema']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['output_schema']._loaded_options = None
    _globals['_TOOL_FUNCTIONTOOL'].fields_by_name['output_schema']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION'].fields_by_name['entity_id']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION'].fields_by_name['entity_id']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION'].fields_by_name['operation']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_CONNECTORTOOL_ACTION'].fields_by_name['input_fields']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL_ACTION'].fields_by_name['input_fields']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_CONNECTORTOOL_ACTION'].fields_by_name['output_fields']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL_ACTION'].fields_by_name['output_fields']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['name']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['actions']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['actions']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['end_user_auth_config']._loaded_options = None
    _globals['_TOOL_CONNECTORTOOL'].fields_by_name['end_user_auth_config']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['key_name']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['key_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['api_key']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['api_key']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['request_location']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG'].fields_by_name['request_location']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['oauth_grant_type']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['oauth_grant_type']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_id']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_secret']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['token_endpoint']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['token_endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['scopes']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG'].fields_by_name['scopes']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG'].fields_by_name['service_agent_auth']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG'].fields_by_name['service_agent_auth']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG'].fields_by_name['token']._loaded_options = None
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG'].fields_by_name['token']._serialized_options = b'\xe0A\x01'
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['display_name']._loaded_options = None
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['cert']._loaded_options = None
    _globals['_TOOL_TLSCONFIG_CACERT'].fields_by_name['cert']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_TLSCONFIG'].fields_by_name['ca_certs']._loaded_options = None
    _globals['_TOOL_TLSCONFIG'].fields_by_name['ca_certs']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._loaded_options = None
    _globals['_TOOL_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2AUTHCODECONFIG'].fields_by_name['oauth_token']._loaded_options = None
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2AUTHCODECONFIG'].fields_by_name['oauth_token']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['issuer']._loaded_options = None
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['issuer']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['subject']._loaded_options = None
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['subject']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['client_key']._loaded_options = None
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG'].fields_by_name['client_key']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL'].fields_by_name['display_name']._loaded_options = None
    _globals['_TOOL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL'].fields_by_name['description']._loaded_options = None
    _globals['_TOOL'].fields_by_name['description']._serialized_options = b'\xe0A\x02'
    _globals['_TOOL'].fields_by_name['tool_type']._loaded_options = None
    _globals['_TOOL'].fields_by_name['tool_type']._serialized_options = b'\xe0A\x03'
    _globals['_TOOL']._loaded_options = None
    _globals['_TOOL']._serialized_options = b'\xeaAe\n\x1edialogflow.googleapis.com/Tool\x12Cprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}'
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/ToolVersion"
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTOOLVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATETOOLVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETOOLVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%dialogflow.googleapis.com/ToolVersion"
    _globals['_CREATETOOLVERSIONREQUEST'].fields_by_name['tool_version']._loaded_options = None
    _globals['_CREATETOOLVERSIONREQUEST'].fields_by_name['tool_version']._serialized_options = b'\xe0A\x02'
    _globals['_GETTOOLVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTOOLVERSIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/ToolVersion"
    _globals['_DELETETOOLVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETOOLVERSIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/ToolVersion"
    _globals['_DELETETOOLVERSIONREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETETOOLVERSIONREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_RESTORETOOLVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTORETOOLVERSIONREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%dialogflow.googleapis.com/ToolVersion"
    _globals['_TOOLVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_TOOLVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TOOLVERSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_TOOLVERSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TOOLVERSION'].fields_by_name['tool']._loaded_options = None
    _globals['_TOOLVERSION'].fields_by_name['tool']._serialized_options = b'\xe0A\x02'
    _globals['_TOOLVERSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_TOOLVERSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TOOLVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_TOOLVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TOOLVERSION']._loaded_options = None
    _globals['_TOOLVERSION']._serialized_options = b'\xeaA\x9a\x01\n%dialogflow.googleapis.com/ToolVersion\x12Vprojects/{project}/locations/{location}/agents/{agent}/tools/{tool}/versions/{version}*\x0ctoolVersions2\x0btoolVersion'
    _globals['_TOOLS']._loaded_options = None
    _globals['_TOOLS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_TOOLS'].methods_by_name['CreateTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['CreateTool']._serialized_options = b'\xdaA\x0bparent,tool\x82\xd3\xe4\x93\x02?"7/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:\x04tool'
    _globals['_TOOLS'].methods_by_name['ListTools']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['ListTools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v3beta1/{parent=projects/*/locations/*/agents/*}/tools'
    _globals['_TOOLS'].methods_by_name['ExportTools']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['ExportTools']._serialized_options = b'\xcaA*\n\x13ExportToolsResponse\x12\x13ExportToolsMetadata\x82\xd3\xe4\x93\x02C">/v3beta1/{parent=projects/*/locations/*/agents/*}/tools:export:\x01*'
    _globals['_TOOLS'].methods_by_name['GetTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['GetTool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}'
    _globals['_TOOLS'].methods_by_name['UpdateTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['UpdateTool']._serialized_options = b'\xdaA\x10tool,update_mask\x82\xd3\xe4\x93\x02D2</v3beta1/{tool.name=projects/*/locations/*/agents/*/tools/*}:\x04tool'
    _globals['_TOOLS'].methods_by_name['DeleteTool']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['DeleteTool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v3beta1/{name=projects/*/locations/*/agents/*/tools/*}'
    _globals['_TOOLS'].methods_by_name['ListToolVersions']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['ListToolVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{parent=projects/*/locations/*/agents/*/tools/*}/versions'
    _globals['_TOOLS'].methods_by_name['CreateToolVersion']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['CreateToolVersion']._serialized_options = b'\xdaA\x13parent,tool_version\x82\xd3\xe4\x93\x02R"B/v3beta1/{parent=projects/*/locations/*/agents/*/tools/*}/versions:\x0ctool_version'
    _globals['_TOOLS'].methods_by_name['GetToolVersion']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['GetToolVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}'
    _globals['_TOOLS'].methods_by_name['DeleteToolVersion']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['DeleteToolVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D*B/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}'
    _globals['_TOOLS'].methods_by_name['RestoreToolVersion']._loaded_options = None
    _globals['_TOOLS'].methods_by_name['RestoreToolVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02O"J/v3beta1/{name=projects/*/locations/*/agents/*/tools/*/versions/*}:restore:\x01*'
    _globals['_CREATETOOLREQUEST']._serialized_start = 477
    _globals['_CREATETOOLREQUEST']._serialized_end = 613
    _globals['_LISTTOOLSREQUEST']._serialized_start = 615
    _globals['_LISTTOOLSREQUEST']._serialized_end = 728
    _globals['_LISTTOOLSRESPONSE']._serialized_start = 730
    _globals['_LISTTOOLSRESPONSE']._serialized_end = 831
    _globals['_GETTOOLREQUEST']._serialized_start = 833
    _globals['_GETTOOLREQUEST']._serialized_end = 903
    _globals['_EXPORTTOOLSREQUEST']._serialized_start = 906
    _globals['_EXPORTTOOLSREQUEST']._serialized_end = 1271
    _globals['_EXPORTTOOLSREQUEST_DATAFORMAT']._serialized_start = 1195
    _globals['_EXPORTTOOLSREQUEST_DATAFORMAT']._serialized_end = 1256
    _globals['_EXPORTTOOLSRESPONSE']._serialized_start = 1274
    _globals['_EXPORTTOOLSRESPONSE']._serialized_end = 1405
    _globals['_UPDATETOOLREQUEST']._serialized_start = 1408
    _globals['_UPDATETOOLREQUEST']._serialized_end = 1537
    _globals['_DELETETOOLREQUEST']._serialized_start = 1539
    _globals['_DELETETOOLREQUEST']._serialized_end = 1627
    _globals['_TOOL']._serialized_start = 1630
    _globals['_TOOL']._serialized_end = 5753
    _globals['_TOOL_OPENAPITOOL']._serialized_start = 2187
    _globals['_TOOL_OPENAPITOOL']._serialized_end = 2505
    _globals['_TOOL_DATASTORETOOL']._serialized_start = 2508
    _globals['_TOOL_DATASTORETOOL']._serialized_end = 2736
    _globals['_TOOL_DATASTORETOOL_FALLBACKPROMPT']._serialized_start = 2720
    _globals['_TOOL_DATASTORETOOL_FALLBACKPROMPT']._serialized_end = 2736
    _globals['_TOOL_EXTENSIONTOOL']._serialized_start = 2738
    _globals['_TOOL_EXTENSIONTOOL']._serialized_end = 2772
    _globals['_TOOL_FUNCTIONTOOL']._serialized_start = 2774
    _globals['_TOOL_FUNCTIONTOOL']._serialized_end = 2893
    _globals['_TOOL_CONNECTORTOOL']._serialized_start = 2896
    _globals['_TOOL_CONNECTORTOOL']._serialized_end = 3595
    _globals['_TOOL_CONNECTORTOOL_ACTION']._serialized_start = 3113
    _globals['_TOOL_CONNECTORTOOL_ACTION']._serialized_end = 3595
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION']._serialized_start = 3318
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION']._serialized_end = 3580
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION_OPERATIONTYPE']._serialized_start = 3478
    _globals['_TOOL_CONNECTORTOOL_ACTION_ENTITYOPERATION_OPERATIONTYPE']._serialized_end = 3580
    _globals['_TOOL_AUTHENTICATION']._serialized_start = 3598
    _globals['_TOOL_AUTHENTICATION']._serialized_end = 4885
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG']._serialized_start = 4029
    _globals['_TOOL_AUTHENTICATION_APIKEYCONFIG']._serialized_end = 4192
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG']._serialized_start = 4195
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG']._serialized_end = 4500
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG_OAUTHGRANTTYPE']._serialized_start = 4427
    _globals['_TOOL_AUTHENTICATION_OAUTHCONFIG_OAUTHGRANTTYPE']._serialized_end = 4500
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG']._serialized_start = 4503
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG']._serialized_end = 4746
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG_SERVICEAGENTAUTH']._serialized_start = 4660
    _globals['_TOOL_AUTHENTICATION_SERVICEAGENTAUTHCONFIG_SERVICEAGENTAUTH']._serialized_end = 4746
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG']._serialized_start = 4748
    _globals['_TOOL_AUTHENTICATION_BEARERTOKENCONFIG']._serialized_end = 4787
    _globals['_TOOL_AUTHENTICATION_REQUESTLOCATION']._serialized_start = 4789
    _globals['_TOOL_AUTHENTICATION_REQUESTLOCATION']._serialized_end = 4870
    _globals['_TOOL_TLSCONFIG']._serialized_start = 4888
    _globals['_TOOL_TLSCONFIG']._serialized_end = 5037
    _globals['_TOOL_TLSCONFIG_CACERT']._serialized_start = 4983
    _globals['_TOOL_TLSCONFIG_CACERT']._serialized_end = 5037
    _globals['_TOOL_SERVICEDIRECTORYCONFIG']._serialized_start = 5039
    _globals['_TOOL_SERVICEDIRECTORYCONFIG']._serialized_end = 5129
    _globals['_TOOL_ENDUSERAUTHCONFIG']._serialized_start = 5132
    _globals['_TOOL_ENDUSERAUTHCONFIG']._serialized_end = 5552
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2AUTHCODECONFIG']._serialized_start = 5387
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2AUTHCODECONFIG']._serialized_end = 5435
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG']._serialized_start = 5437
    _globals['_TOOL_ENDUSERAUTHCONFIG_OAUTH2JWTBEARERCONFIG']._serialized_end = 5528
    _globals['_TOOL_TOOLTYPE']._serialized_start = 5554
    _globals['_TOOL_TOOLTYPE']._serialized_end = 5630
    _globals['_LISTTOOLVERSIONSREQUEST']._serialized_start = 5756
    _globals['_LISTTOOLVERSIONSREQUEST']._serialized_end = 5893
    _globals['_LISTTOOLVERSIONSRESPONSE']._serialized_start = 5895
    _globals['_LISTTOOLVERSIONSRESPONSE']._serialized_end = 6018
    _globals['_CREATETOOLVERSIONREQUEST']._serialized_start = 6021
    _globals['_CREATETOOLVERSIONREQUEST']._serialized_end = 6186
    _globals['_GETTOOLVERSIONREQUEST']._serialized_start = 6188
    _globals['_GETTOOLVERSIONREQUEST']._serialized_end = 6272
    _globals['_DELETETOOLVERSIONREQUEST']._serialized_start = 6274
    _globals['_DELETETOOLVERSIONREQUEST']._serialized_end = 6381
    _globals['_RESTORETOOLVERSIONREQUEST']._serialized_start = 6383
    _globals['_RESTORETOOLVERSIONREQUEST']._serialized_end = 6471
    _globals['_RESTORETOOLVERSIONRESPONSE']._serialized_start = 6473
    _globals['_RESTORETOOLVERSIONRESPONSE']._serialized_end = 6557
    _globals['_TOOLVERSION']._serialized_start = 6560
    _globals['_TOOLVERSION']._serialized_end = 6949
    _globals['_EXPORTTOOLSMETADATA']._serialized_start = 6951
    _globals['_EXPORTTOOLSMETADATA']._serialized_end = 6972
    _globals['_TOOLS']._serialized_start = 6975
    _globals['_TOOLS']._serialized_end = 9391