"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3/webhook.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3 import response_message_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3_dot_response__message__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/dialogflow/cx/v3/webhook.proto\x12\x1dgoogle.cloud.dialogflow.cx.v3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/dialogflow/cx/v3/response_message.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"\xce\x0e\n\x07Webhook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12W\n\x13generic_web_service\x18\x04 \x01(\x0b28.google.cloud.dialogflow.cx.v3.Webhook.GenericWebServiceH\x00\x12Z\n\x11service_directory\x18\x07 \x01(\x0b2=.google.cloud.dialogflow.cx.v3.Webhook.ServiceDirectoryConfigH\x00\x12*\n\x07timeout\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x10\n\x08disabled\x18\x05 \x01(\x08\x1a\xf4\t\n\x11GenericWebService\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x08username\x18\x02 \x01(\tB\x02\x18\x01\x12\x14\n\x08password\x18\x03 \x01(\tB\x02\x18\x01\x12e\n\x0frequest_headers\x18\x04 \x03(\x0b2L.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.RequestHeadersEntry\x12\x1d\n\x10allowed_ca_certs\x18\x05 \x03(\x0cB\x03\xe0A\x01\x12_\n\x0coauth_config\x18\x0b \x01(\x0b2D.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.OAuthConfigB\x03\xe0A\x01\x12j\n\x12service_agent_auth\x18\x0c \x01(\x0e2I.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.ServiceAgentAuthB\x03\xe0A\x01\x12_\n\x0cwebhook_type\x18\x06 \x01(\x0e2D.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.WebhookTypeB\x03\xe0A\x01\x12]\n\x0bhttp_method\x18\x07 \x01(\x0e2C.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.HttpMethodB\x03\xe0A\x01\x12\x19\n\x0crequest_body\x18\x08 \x01(\tB\x03\xe0A\x01\x12n\n\x11parameter_mapping\x18\t \x03(\x0b2N.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService.ParameterMappingEntryB\x03\xe0A\x01\x1as\n\x0bOAuthConfig\x12\x16\n\tclient_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rclient_secret\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0etoken_endpoint\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06scopes\x18\x04 \x03(\tB\x03\xe0A\x01\x1a5\n\x13RequestHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a7\n\x15ParameterMappingEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"`\n\x10ServiceAgentAuth\x12"\n\x1eSERVICE_AGENT_AUTH_UNSPECIFIED\x10\x00\x12\x08\n\x04NONE\x10\x01\x12\x0c\n\x08ID_TOKEN\x10\x02\x12\x10\n\x0cACCESS_TOKEN\x10\x03"G\n\x0bWebhookType\x12\x1c\n\x18WEBHOOK_TYPE_UNSPECIFIED\x10\x00\x12\x0c\n\x08STANDARD\x10\x01\x12\x0c\n\x08FLEXIBLE\x10\x02"s\n\nHttpMethod\x12\x1b\n\x17HTTP_METHOD_UNSPECIFIED\x10\x00\x12\x08\n\x04POST\x10\x01\x12\x07\n\x03GET\x10\x02\x12\x08\n\x04HEAD\x10\x03\x12\x07\n\x03PUT\x10\x04\x12\n\n\x06DELETE\x10\x05\x12\t\n\x05PATCH\x10\x06\x12\x0b\n\x07OPTIONS\x10\x07\x1a\xb1\x01\n\x16ServiceDirectoryConfig\x12@\n\x07service\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'servicedirectory.googleapis.com/Service\x12U\n\x13generic_web_service\x18\x02 \x01(\x0b28.google.cloud.dialogflow.cx.v3.Webhook.GenericWebService:q\xeaAn\n!dialogflow.googleapis.com/Webhook\x12Iprojects/{project}/locations/{location}/agents/{agent}/webhooks/{webhook}B\t\n\x07webhook"w\n\x13ListWebhooksRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Webhook\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"i\n\x14ListWebhooksResponse\x128\n\x08webhooks\x18\x01 \x03(\x0b2&.google.cloud.dialogflow.cx.v3.Webhook\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"L\n\x11GetWebhookRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Webhook"\x8f\x01\n\x14CreateWebhookRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Webhook\x12<\n\x07webhook\x18\x02 \x01(\x0b2&.google.cloud.dialogflow.cx.v3.WebhookB\x03\xe0A\x02"\x85\x01\n\x14UpdateWebhookRequest\x12<\n\x07webhook\x18\x01 \x01(\x0b2&.google.cloud.dialogflow.cx.v3.WebhookB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"^\n\x14DeleteWebhookRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Webhook\x12\r\n\x05force\x18\x02 \x01(\x08"\xc5\n\n\x0eWebhookRequest\x12!\n\x19detect_intent_response_id\x18\x01 \x01(\t\x12\x0e\n\x04text\x18\n \x01(\tH\x00\x12?\n\x0etrigger_intent\x18\x0b \x01(\tB%\xfaA"\n dialogflow.googleapis.com/IntentH\x00\x12\x14\n\ntranscript\x18\x0c \x01(\tH\x00\x12\x17\n\rtrigger_event\x18\x0e \x01(\tH\x00\x12\x15\n\x0bdtmf_digits\x18\x11 \x01(\tH\x00\x12\x15\n\rlanguage_code\x18\x0f \x01(\t\x12W\n\x10fulfillment_info\x18\x06 \x01(\x0b2=.google.cloud.dialogflow.cx.v3.WebhookRequest.FulfillmentInfo\x12M\n\x0bintent_info\x18\x03 \x01(\x0b28.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo\x12:\n\tpage_info\x18\x04 \x01(\x0b2\'.google.cloud.dialogflow.cx.v3.PageInfo\x12@\n\x0csession_info\x18\x05 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.SessionInfo\x12@\n\x08messages\x18\x07 \x03(\x0b2..google.cloud.dialogflow.cx.v3.ResponseMessage\x12(\n\x07payload\x18\x08 \x01(\x0b2\x17.google.protobuf.Struct\x12h\n\x19sentiment_analysis_result\x18\t \x01(\x0b2E.google.cloud.dialogflow.cx.v3.WebhookRequest.SentimentAnalysisResult\x12B\n\rlanguage_info\x18\x12 \x01(\x0b2+.google.cloud.dialogflow.cx.v3.LanguageInfo\x1a\x1e\n\x0fFulfillmentInfo\x12\x0b\n\x03tag\x18\x01 \x01(\t\x1a\xbb\x03\n\nIntentInfo\x12B\n\x13last_matched_intent\x18\x01 \x01(\tB%\xfaA"\n dialogflow.googleapis.com/Intent\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t\x12\\\n\nparameters\x18\x02 \x03(\x0b2H.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo.ParametersEntry\x12\x12\n\nconfidence\x18\x04 \x01(\x02\x1a^\n\x14IntentParameterValue\x12\x16\n\x0eoriginal_value\x18\x01 \x01(\t\x12.\n\x0eresolved_value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x1a\x80\x01\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\\\n\x05value\x18\x02 \x01(\x0b2M.google.cloud.dialogflow.cx.v3.WebhookRequest.IntentInfo.IntentParameterValue:\x028\x01\x1a;\n\x17SentimentAnalysisResult\x12\r\n\x05score\x18\x01 \x01(\x02\x12\x11\n\tmagnitude\x18\x02 \x01(\x02B\x07\n\x05query"\xaf\x05\n\x0fWebhookResponse\x12`\n\x14fulfillment_response\x18\x01 \x01(\x0b2B.google.cloud.dialogflow.cx.v3.WebhookResponse.FulfillmentResponse\x12:\n\tpage_info\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.cx.v3.PageInfo\x12@\n\x0csession_info\x18\x03 \x01(\x0b2*.google.cloud.dialogflow.cx.v3.SessionInfo\x12(\n\x07payload\x18\x04 \x01(\x0b2\x17.google.protobuf.Struct\x12:\n\x0btarget_page\x18\x05 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/PageH\x00\x12:\n\x0btarget_flow\x18\x06 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/FlowH\x00\x1a\x8b\x02\n\x13FulfillmentResponse\x12@\n\x08messages\x18\x01 \x03(\x0b2..google.cloud.dialogflow.cx.v3.ResponseMessage\x12h\n\x0emerge_behavior\x18\x02 \x01(\x0e2P.google.cloud.dialogflow.cx.v3.WebhookResponse.FulfillmentResponse.MergeBehavior"H\n\rMergeBehavior\x12\x1e\n\x1aMERGE_BEHAVIOR_UNSPECIFIED\x10\x00\x12\n\n\x06APPEND\x10\x01\x12\x0b\n\x07REPLACE\x10\x02B\x0c\n\ntransition"\xb3\x04\n\x08PageInfo\x129\n\x0ccurrent_page\x18\x01 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/Page\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12C\n\tform_info\x18\x03 \x01(\x0b20.google.cloud.dialogflow.cx.v3.PageInfo.FormInfo\x1a\x90\x03\n\x08FormInfo\x12V\n\x0eparameter_info\x18\x02 \x03(\x0b2>.google.cloud.dialogflow.cx.v3.PageInfo.FormInfo.ParameterInfo\x1a\xab\x02\n\rParameterInfo\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x10\n\x08required\x18\x02 \x01(\x08\x12\\\n\x05state\x18\x03 \x01(\x0e2M.google.cloud.dialogflow.cx.v3.PageInfo.FormInfo.ParameterInfo.ParameterState\x12%\n\x05value\x18\x04 \x01(\x0b2\x16.google.protobuf.Value\x12\x16\n\x0ejust_collected\x18\x05 \x01(\x08"U\n\x0eParameterState\x12\x1f\n\x1bPARAMETER_STATE_UNSPECIFIED\x10\x00\x12\t\n\x05EMPTY\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\n\n\x06FILLED\x10\x03"\xe1\x01\n\x0bSessionInfo\x127\n\x07session\x18\x01 \x01(\tB&\xfaA#\n!dialogflow.googleapis.com/Session\x12N\n\nparameters\x18\x02 \x03(\x0b2:.google.cloud.dialogflow.cx.v3.SessionInfo.ParametersEntry\x1aI\n\x0fParametersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01"e\n\x0cLanguageInfo\x12\x1b\n\x13input_language_code\x18\x01 \x01(\t\x12\x1e\n\x16resolved_language_code\x18\x02 \x01(\t\x12\x18\n\x10confidence_score\x18\x03 \x01(\x022\xb7\x08\n\x08Webhooks\x12\xbf\x01\n\x0cListWebhooks\x122.google.cloud.dialogflow.cx.v3.ListWebhooksRequest\x1a3.google.cloud.dialogflow.cx.v3.ListWebhooksResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v3/{parent=projects/*/locations/*/agents/*}/webhooks\x12\xac\x01\n\nGetWebhook\x120.google.cloud.dialogflow.cx.v3.GetWebhookRequest\x1a&.google.cloud.dialogflow.cx.v3.Webhook"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v3/{name=projects/*/locations/*/agents/*/webhooks/*}\x12\xc5\x01\n\rCreateWebhook\x123.google.cloud.dialogflow.cx.v3.CreateWebhookRequest\x1a&.google.cloud.dialogflow.cx.v3.Webhook"W\xdaA\x0eparent,webhook\x82\xd3\xe4\x93\x02@"5/v3/{parent=projects/*/locations/*/agents/*}/webhooks:\x07webhook\x12\xd2\x01\n\rUpdateWebhook\x123.google.cloud.dialogflow.cx.v3.UpdateWebhookRequest\x1a&.google.cloud.dialogflow.cx.v3.Webhook"d\xdaA\x13webhook,update_mask\x82\xd3\xe4\x93\x02H2=/v3/{webhook.name=projects/*/locations/*/agents/*/webhooks/*}:\x07webhook\x12\xa2\x01\n\rDeleteWebhook\x123.google.cloud.dialogflow.cx.v3.DeleteWebhookRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v3/{name=projects/*/locations/*/agents/*/webhooks/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xae\x02\n!com.google.cloud.dialogflow.cx.v3B\x0cWebhookProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA|\n\'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3.webhook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n!com.google.cloud.dialogflow.cx.v3B\x0cWebhookProtoP\x01Z1cloud.google.com/go/dialogflow/cx/apiv3/cxpb;cxpb\xa2\x02\x02DF\xaa\x02\x1dGoogle.Cloud.Dialogflow.Cx.V3\xea\x02!Google::Cloud::Dialogflow::CX::V3\xeaA|\n'servicedirectory.googleapis.com/Service\x12Qprojects/{project}/locations/{location}/namespaces/{namespace}/services/{service}"
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['client_id']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['client_id']._serialized_options = b'\xe0A\x02'
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['client_secret']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['client_secret']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['token_endpoint']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['token_endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['scopes']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG'].fields_by_name['scopes']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_options = b'8\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE_PARAMETERMAPPINGENTRY']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE_PARAMETERMAPPINGENTRY']._serialized_options = b'8\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['uri']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['username']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['username']._serialized_options = b'\x18\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['password']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['password']._serialized_options = b'\x18\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['allowed_ca_certs']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['allowed_ca_certs']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['oauth_config']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['oauth_config']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['service_agent_auth']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['service_agent_auth']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['webhook_type']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['webhook_type']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['http_method']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['http_method']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['request_body']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['request_body']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['parameter_mapping']._loaded_options = None
    _globals['_WEBHOOK_GENERICWEBSERVICE'].fields_by_name['parameter_mapping']._serialized_options = b'\xe0A\x01'
    _globals['_WEBHOOK_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._loaded_options = None
    _globals['_WEBHOOK_SERVICEDIRECTORYCONFIG'].fields_by_name['service']._serialized_options = b"\xe0A\x02\xfaA)\n'servicedirectory.googleapis.com/Service"
    _globals['_WEBHOOK'].fields_by_name['display_name']._loaded_options = None
    _globals['_WEBHOOK'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_WEBHOOK']._loaded_options = None
    _globals['_WEBHOOK']._serialized_options = b'\xeaAn\n!dialogflow.googleapis.com/Webhook\x12Iprojects/{project}/locations/{location}/agents/{agent}/webhooks/{webhook}'
    _globals['_LISTWEBHOOKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTWEBHOOKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Webhook'
    _globals['_GETWEBHOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWEBHOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Webhook'
    _globals['_CREATEWEBHOOKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWEBHOOKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!dialogflow.googleapis.com/Webhook'
    _globals['_CREATEWEBHOOKREQUEST'].fields_by_name['webhook']._loaded_options = None
    _globals['_CREATEWEBHOOKREQUEST'].fields_by_name['webhook']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEWEBHOOKREQUEST'].fields_by_name['webhook']._loaded_options = None
    _globals['_UPDATEWEBHOOKREQUEST'].fields_by_name['webhook']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEWEBHOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEWEBHOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!dialogflow.googleapis.com/Webhook'
    _globals['_WEBHOOKREQUEST_INTENTINFO_PARAMETERSENTRY']._loaded_options = None
    _globals['_WEBHOOKREQUEST_INTENTINFO_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_WEBHOOKREQUEST_INTENTINFO'].fields_by_name['last_matched_intent']._loaded_options = None
    _globals['_WEBHOOKREQUEST_INTENTINFO'].fields_by_name['last_matched_intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_WEBHOOKREQUEST'].fields_by_name['trigger_intent']._loaded_options = None
    _globals['_WEBHOOKREQUEST'].fields_by_name['trigger_intent']._serialized_options = b'\xfaA"\n dialogflow.googleapis.com/Intent'
    _globals['_WEBHOOKRESPONSE'].fields_by_name['target_page']._loaded_options = None
    _globals['_WEBHOOKRESPONSE'].fields_by_name['target_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_WEBHOOKRESPONSE'].fields_by_name['target_flow']._loaded_options = None
    _globals['_WEBHOOKRESPONSE'].fields_by_name['target_flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_PAGEINFO'].fields_by_name['current_page']._loaded_options = None
    _globals['_PAGEINFO'].fields_by_name['current_page']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Page'
    _globals['_SESSIONINFO_PARAMETERSENTRY']._loaded_options = None
    _globals['_SESSIONINFO_PARAMETERSENTRY']._serialized_options = b'8\x01'
    _globals['_SESSIONINFO'].fields_by_name['session']._loaded_options = None
    _globals['_SESSIONINFO'].fields_by_name['session']._serialized_options = b'\xfaA#\n!dialogflow.googleapis.com/Session'
    _globals['_WEBHOOKS']._loaded_options = None
    _globals['_WEBHOOKS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_WEBHOOKS'].methods_by_name['ListWebhooks']._loaded_options = None
    _globals['_WEBHOOKS'].methods_by_name['ListWebhooks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v3/{parent=projects/*/locations/*/agents/*}/webhooks'
    _globals['_WEBHOOKS'].methods_by_name['GetWebhook']._loaded_options = None
    _globals['_WEBHOOKS'].methods_by_name['GetWebhook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v3/{name=projects/*/locations/*/agents/*/webhooks/*}'
    _globals['_WEBHOOKS'].methods_by_name['CreateWebhook']._loaded_options = None
    _globals['_WEBHOOKS'].methods_by_name['CreateWebhook']._serialized_options = b'\xdaA\x0eparent,webhook\x82\xd3\xe4\x93\x02@"5/v3/{parent=projects/*/locations/*/agents/*}/webhooks:\x07webhook'
    _globals['_WEBHOOKS'].methods_by_name['UpdateWebhook']._loaded_options = None
    _globals['_WEBHOOKS'].methods_by_name['UpdateWebhook']._serialized_options = b'\xdaA\x13webhook,update_mask\x82\xd3\xe4\x93\x02H2=/v3/{webhook.name=projects/*/locations/*/agents/*/webhooks/*}:\x07webhook'
    _globals['_WEBHOOKS'].methods_by_name['DeleteWebhook']._loaded_options = None
    _globals['_WEBHOOKS'].methods_by_name['DeleteWebhook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v3/{name=projects/*/locations/*/agents/*/webhooks/*}'
    _globals['_WEBHOOK']._serialized_start = 373
    _globals['_WEBHOOK']._serialized_end = 2243
    _globals['_WEBHOOK_GENERICWEBSERVICE']._serialized_start = 669
    _globals['_WEBHOOK_GENERICWEBSERVICE']._serialized_end = 1937
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG']._serialized_start = 1422
    _globals['_WEBHOOK_GENERICWEBSERVICE_OAUTHCONFIG']._serialized_end = 1537
    _globals['_WEBHOOK_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_start = 1539
    _globals['_WEBHOOK_GENERICWEBSERVICE_REQUESTHEADERSENTRY']._serialized_end = 1592
    _globals['_WEBHOOK_GENERICWEBSERVICE_PARAMETERMAPPINGENTRY']._serialized_start = 1594
    _globals['_WEBHOOK_GENERICWEBSERVICE_PARAMETERMAPPINGENTRY']._serialized_end = 1649
    _globals['_WEBHOOK_GENERICWEBSERVICE_SERVICEAGENTAUTH']._serialized_start = 1651
    _globals['_WEBHOOK_GENERICWEBSERVICE_SERVICEAGENTAUTH']._serialized_end = 1747
    _globals['_WEBHOOK_GENERICWEBSERVICE_WEBHOOKTYPE']._serialized_start = 1749
    _globals['_WEBHOOK_GENERICWEBSERVICE_WEBHOOKTYPE']._serialized_end = 1820
    _globals['_WEBHOOK_GENERICWEBSERVICE_HTTPMETHOD']._serialized_start = 1822
    _globals['_WEBHOOK_GENERICWEBSERVICE_HTTPMETHOD']._serialized_end = 1937
    _globals['_WEBHOOK_SERVICEDIRECTORYCONFIG']._serialized_start = 1940
    _globals['_WEBHOOK_SERVICEDIRECTORYCONFIG']._serialized_end = 2117
    _globals['_LISTWEBHOOKSREQUEST']._serialized_start = 2245
    _globals['_LISTWEBHOOKSREQUEST']._serialized_end = 2364
    _globals['_LISTWEBHOOKSRESPONSE']._serialized_start = 2366
    _globals['_LISTWEBHOOKSRESPONSE']._serialized_end = 2471
    _globals['_GETWEBHOOKREQUEST']._serialized_start = 2473
    _globals['_GETWEBHOOKREQUEST']._serialized_end = 2549
    _globals['_CREATEWEBHOOKREQUEST']._serialized_start = 2552
    _globals['_CREATEWEBHOOKREQUEST']._serialized_end = 2695
    _globals['_UPDATEWEBHOOKREQUEST']._serialized_start = 2698
    _globals['_UPDATEWEBHOOKREQUEST']._serialized_end = 2831
    _globals['_DELETEWEBHOOKREQUEST']._serialized_start = 2833
    _globals['_DELETEWEBHOOKREQUEST']._serialized_end = 2927
    _globals['_WEBHOOKREQUEST']._serialized_start = 2930
    _globals['_WEBHOOKREQUEST']._serialized_end = 4279
    _globals['_WEBHOOKREQUEST_FULFILLMENTINFO']._serialized_start = 3733
    _globals['_WEBHOOKREQUEST_FULFILLMENTINFO']._serialized_end = 3763
    _globals['_WEBHOOKREQUEST_INTENTINFO']._serialized_start = 3766
    _globals['_WEBHOOKREQUEST_INTENTINFO']._serialized_end = 4209
    _globals['_WEBHOOKREQUEST_INTENTINFO_INTENTPARAMETERVALUE']._serialized_start = 3984
    _globals['_WEBHOOKREQUEST_INTENTINFO_INTENTPARAMETERVALUE']._serialized_end = 4078
    _globals['_WEBHOOKREQUEST_INTENTINFO_PARAMETERSENTRY']._serialized_start = 4081
    _globals['_WEBHOOKREQUEST_INTENTINFO_PARAMETERSENTRY']._serialized_end = 4209
    _globals['_WEBHOOKREQUEST_SENTIMENTANALYSISRESULT']._serialized_start = 4211
    _globals['_WEBHOOKREQUEST_SENTIMENTANALYSISRESULT']._serialized_end = 4270
    _globals['_WEBHOOKRESPONSE']._serialized_start = 4282
    _globals['_WEBHOOKRESPONSE']._serialized_end = 4969
    _globals['_WEBHOOKRESPONSE_FULFILLMENTRESPONSE']._serialized_start = 4688
    _globals['_WEBHOOKRESPONSE_FULFILLMENTRESPONSE']._serialized_end = 4955
    _globals['_WEBHOOKRESPONSE_FULFILLMENTRESPONSE_MERGEBEHAVIOR']._serialized_start = 4883
    _globals['_WEBHOOKRESPONSE_FULFILLMENTRESPONSE_MERGEBEHAVIOR']._serialized_end = 4955
    _globals['_PAGEINFO']._serialized_start = 4972
    _globals['_PAGEINFO']._serialized_end = 5535
    _globals['_PAGEINFO_FORMINFO']._serialized_start = 5135
    _globals['_PAGEINFO_FORMINFO']._serialized_end = 5535
    _globals['_PAGEINFO_FORMINFO_PARAMETERINFO']._serialized_start = 5236
    _globals['_PAGEINFO_FORMINFO_PARAMETERINFO']._serialized_end = 5535
    _globals['_PAGEINFO_FORMINFO_PARAMETERINFO_PARAMETERSTATE']._serialized_start = 5450
    _globals['_PAGEINFO_FORMINFO_PARAMETERINFO_PARAMETERSTATE']._serialized_end = 5535
    _globals['_SESSIONINFO']._serialized_start = 5538
    _globals['_SESSIONINFO']._serialized_end = 5763
    _globals['_SESSIONINFO_PARAMETERSENTRY']._serialized_start = 5690
    _globals['_SESSIONINFO_PARAMETERSENTRY']._serialized_end = 5763
    _globals['_LANGUAGEINFO']._serialized_start = 5765
    _globals['_LANGUAGEINFO']._serialized_end = 5866
    _globals['_WEBHOOKS']._serialized_start = 5869
    _globals['_WEBHOOKS']._serialized_end = 6948