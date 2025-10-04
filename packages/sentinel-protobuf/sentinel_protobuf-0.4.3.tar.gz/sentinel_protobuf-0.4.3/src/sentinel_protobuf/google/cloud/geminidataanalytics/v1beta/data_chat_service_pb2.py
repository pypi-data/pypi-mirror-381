"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/data_chat_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.geminidataanalytics.v1beta import context_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_context__pb2
from .....google.cloud.geminidataanalytics.v1beta import conversation_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_conversation__pb2
from .....google.cloud.geminidataanalytics.v1beta import credentials_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_credentials__pb2
from .....google.cloud.geminidataanalytics.v1beta import datasource_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_datasource__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/geminidataanalytics/v1beta/data_chat_service.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/geminidataanalytics/v1beta/context.proto\x1a:google/cloud/geminidataanalytics/v1beta/conversation.proto\x1a9google/cloud/geminidataanalytics/v1beta/credentials.proto\x1a8google/cloud/geminidataanalytics/v1beta/datasource.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa4\x01\n\x13ListMessagesRequest\x12G\n\x06parent\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x05 \x01(\tB\x03\xe0A\x01"z\n\x14ListMessagesResponse\x12I\n\x08messages\x18\x01 \x03(\x0b27.google.cloud.geminidataanalytics.v1beta.StorageMessage\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"g\n\x0eStorageMessage\x12\x12\n\nmessage_id\x18\x01 \x01(\t\x12A\n\x07message\x18\x02 \x01(\x0b20.google.cloud.geminidataanalytics.v1beta.Message"\xdd\x03\n\x0bChatRequest\x12O\n\x0einline_context\x18e \x01(\x0b20.google.cloud.geminidataanalytics.v1beta.ContextB\x03\xe0A\x01H\x00\x12e\n\x16conversation_reference\x18g \x01(\x0b2>.google.cloud.geminidataanalytics.v1beta.ConversationReferenceB\x03\xe0A\x01H\x00\x12\\\n\x12data_agent_context\x18h \x01(\x0b29.google.cloud.geminidataanalytics.v1beta.DataAgentContextB\x03\xe0A\x01H\x00\x12F\n\x07project\x18\x01 \x01(\tB5\x18\x01\xe0A\x01\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12\x13\n\x06parent\x18\x03 \x01(\tB\x03\xe0A\x02\x12G\n\x08messages\x18\x02 \x03(\x0b20.google.cloud.geminidataanalytics.v1beta.MessageB\x03\xe0A\x02B\x12\n\x10context_provider"\xe3\x02\n\x10DataAgentContext\x12H\n\ndata_agent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent\x12N\n\x0bcredentials\x18\x02 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.CredentialsB\x03\xe0A\x01\x12f\n\x0fcontext_version\x18\x03 \x01(\x0e2H.google.cloud.geminidataanalytics.v1beta.DataAgentContext.ContextVersionB\x03\xe0A\x01"M\n\x0eContextVersion\x12\x1f\n\x1bCONTEXT_VERSION_UNSPECIFIED\x10\x00\x12\x0b\n\x07STAGING\x10\x01\x12\r\n\tPUBLISHED\x10\x02"\xc2\x01\n\x15ConversationReference\x12M\n\x0cconversation\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation\x12Z\n\x12data_agent_context\x18\x03 \x01(\x0b29.google.cloud.geminidataanalytics.v1beta.DataAgentContextB\x03\xe0A\x02"\xfe\x01\n\x07Message\x12L\n\x0cuser_message\x18\x02 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.UserMessageH\x00\x12P\n\x0esystem_message\x18\x03 \x01(\x0b26.google.cloud.geminidataanalytics.v1beta.SystemMessageH\x00\x122\n\ttimestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x17\n\nmessage_id\x18\x04 \x01(\tB\x03\xe0A\x01B\x06\n\x04kind"%\n\x0bUserMessage\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00B\x06\n\x04kind"\xef\x03\n\rSystemMessage\x12D\n\x04text\x18\x01 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.TextMessageH\x00\x12H\n\x06schema\x18\x02 \x01(\x0b26.google.cloud.geminidataanalytics.v1beta.SchemaMessageH\x00\x12D\n\x04data\x18\x03 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.DataMessageH\x00\x12L\n\x08analysis\x18\x04 \x01(\x0b28.google.cloud.geminidataanalytics.v1beta.AnalysisMessageH\x00\x12F\n\x05chart\x18\x05 \x01(\x0b25.google.cloud.geminidataanalytics.v1beta.ChartMessageH\x00\x12F\n\x05error\x18\x06 \x01(\x0b25.google.cloud.geminidataanalytics.v1beta.ErrorMessageH\x00\x12\x15\n\x08group_id\x18\x0c \x01(\x05H\x01\x88\x01\x01B\x06\n\x04kindB\x0b\n\t_group_id"!\n\x0bTextMessage\x12\x12\n\x05parts\x18\x01 \x03(\tB\x03\xe0A\x01"\xa7\x01\n\rSchemaMessage\x12E\n\x05query\x18\x01 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.SchemaQueryH\x00\x12G\n\x06result\x18\x02 \x01(\x0b25.google.cloud.geminidataanalytics.v1beta.SchemaResultH\x00B\x06\n\x04kind"$\n\x0bSchemaQuery\x12\x15\n\x08question\x18\x01 \x01(\tB\x03\xe0A\x01"]\n\x0cSchemaResult\x12M\n\x0bdatasources\x18\x01 \x03(\x0b23.google.cloud.geminidataanalytics.v1beta.DatasourceB\x03\xe0A\x01"\xe1\x02\n\x0bDataMessage\x12C\n\x05query\x18\x01 \x01(\x0b22.google.cloud.geminidataanalytics.v1beta.DataQueryH\x00\x12\x17\n\rgenerated_sql\x18\x02 \x01(\tH\x00\x12E\n\x06result\x18\x03 \x01(\x0b23.google.cloud.geminidataanalytics.v1beta.DataResultH\x00\x12V\n\x16generated_looker_query\x18\x04 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.LookerQueryH\x00\x12M\n\rbig_query_job\x18\x05 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.BigQueryJobH\x00B\x06\n\x04kind"\x88\x02\n\x0bLookerQuery\x12\x12\n\x05model\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07explore\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06fields\x18\x03 \x03(\tB\x03\xe0A\x01\x12Q\n\x07filters\x18\x04 \x03(\x0b2;.google.cloud.geminidataanalytics.v1beta.LookerQuery.FilterB\x03\xe0A\x01\x12\x12\n\x05sorts\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x17\n\x05limit\x18\x06 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x1a0\n\x06Filter\x12\x12\n\x05field\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x02B\x08\n\x06_limit"\x84\x01\n\tDataQuery\x12\x15\n\x08question\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x01\x12M\n\x0bdatasources\x18\x02 \x03(\x0b23.google.cloud.geminidataanalytics.v1beta.DatasourceB\x03\xe0A\x01"\x91\x01\n\nDataResult\x12\x11\n\x04name\x18\x03 \x01(\tB\x03\xe0A\x01\x12D\n\x06schema\x18\x05 \x01(\x0b2/.google.cloud.geminidataanalytics.v1beta.SchemaB\x03\xe0A\x01\x12*\n\x04data\x18\x02 \x03(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01"\xf9\x01\n\x0bBigQueryJob\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08location\x18\x05 \x01(\tB\x03\xe0A\x01\x12_\n\x11destination_table\x18\x03 \x01(\x0b2?.google.cloud.geminidataanalytics.v1beta.BigQueryTableReferenceB\x03\xe0A\x01\x12D\n\x06schema\x18\x07 \x01(\x0b2/.google.cloud.geminidataanalytics.v1beta.SchemaB\x03\xe0A\x01"\xb4\x01\n\x0fAnalysisMessage\x12G\n\x05query\x18\x01 \x01(\x0b26.google.cloud.geminidataanalytics.v1beta.AnalysisQueryH\x00\x12P\n\x0eprogress_event\x18\x02 \x01(\x0b26.google.cloud.geminidataanalytics.v1beta.AnalysisEventH\x00B\x06\n\x04kind"F\n\rAnalysisQuery\x12\x15\n\x08question\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1e\n\x11data_result_names\x18\x02 \x03(\tB\x03\xe0A\x01"\xaa\x02\n\rAnalysisEvent\x12\x1b\n\x11planner_reasoning\x18\x02 \x01(\tH\x00\x12\x1b\n\x11coder_instruction\x18\x03 \x01(\tH\x00\x12\x0e\n\x04code\x18\x04 \x01(\tH\x00\x12\x1a\n\x10execution_output\x18\x05 \x01(\tH\x00\x12\x19\n\x0fexecution_error\x18\x06 \x01(\tH\x00\x12 \n\x16result_vega_chart_json\x18\x07 \x01(\tH\x00\x12!\n\x17result_natural_language\x18\x08 \x01(\tH\x00\x12\x19\n\x0fresult_csv_data\x18\t \x01(\tH\x00\x12\x1f\n\x15result_reference_data\x18\n \x01(\tH\x00\x12\x0f\n\x05error\x18\x0b \x01(\tH\x00B\x06\n\x04kind"\xa4\x01\n\x0cChartMessage\x12D\n\x05query\x18\x01 \x01(\x0b23.google.cloud.geminidataanalytics.v1beta.ChartQueryH\x00\x12F\n\x06result\x18\x02 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.ChartResultH\x00B\x06\n\x04kind"F\n\nChartQuery\x12\x19\n\x0cinstructions\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x10data_result_name\x18\x02 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x0bChartResult\x121\n\x0bvega_config\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12A\n\x05image\x18\x03 \x01(\x0b2-.google.cloud.geminidataanalytics.v1beta.BlobB\x03\xe0A\x01"!\n\x0cErrorMessage\x12\x11\n\x04text\x18\x01 \x01(\tB\x03\xe0A\x03"1\n\x04Blob\x12\x16\n\tmime_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04data\x18\x02 \x01(\x0cB\x03\xe0A\x022\xb2\t\n\x0fDataChatService\x12\xa9\x01\n\x04Chat\x124.google.cloud.geminidataanalytics.v1beta.ChatRequest\x1a0.google.cloud.geminidataanalytics.v1beta.Message"7\x82\xd3\xe4\x93\x021",/v1beta/{parent=projects/*/locations/*}:chat:\x01*0\x01\x12\x82\x02\n\x12CreateConversation\x12B.google.cloud.geminidataanalytics.v1beta.CreateConversationRequest\x1a5.google.cloud.geminidataanalytics.v1beta.Conversation"q\xdaA#parent,conversation,conversation_id\x82\xd3\xe4\x93\x02E"5/v1beta/{parent=projects/*/locations/*}/conversations:\x0cconversation\x12\xcf\x01\n\x0fGetConversation\x12?.google.cloud.geminidataanalytics.v1beta.GetConversationRequest\x1a5.google.cloud.geminidataanalytics.v1beta.Conversation"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta/{name=projects/*/locations/*/conversations/*}\x12\xe2\x01\n\x11ListConversations\x12A.google.cloud.geminidataanalytics.v1beta.ListConversationsRequest\x1aB.google.cloud.geminidataanalytics.v1beta.ListConversationsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta/{parent=projects/*/locations/*}/conversations\x12\xde\x01\n\x0cListMessages\x12<.google.cloud.geminidataanalytics.v1beta.ListMessagesRequest\x1a=.google.cloud.geminidataanalytics.v1beta.ListMessagesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta/{parent=projects/*/locations/*/conversations/*}/messages\x1aV\xcaA"geminidataanalytics.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa5\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x14DataChatServiceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.data_chat_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x14DataChatServiceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMESSAGESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_CHATREQUEST'].fields_by_name['inline_context']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['inline_context']._serialized_options = b'\xe0A\x01'
    _globals['_CHATREQUEST'].fields_by_name['conversation_reference']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['conversation_reference']._serialized_options = b'\xe0A\x01'
    _globals['_CHATREQUEST'].fields_by_name['data_agent_context']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['data_agent_context']._serialized_options = b'\xe0A\x01'
    _globals['_CHATREQUEST'].fields_by_name['project']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['project']._serialized_options = b'\x18\x01\xe0A\x01\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CHATREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CHATREQUEST'].fields_by_name['messages']._loaded_options = None
    _globals['_CHATREQUEST'].fields_by_name['messages']._serialized_options = b'\xe0A\x02'
    _globals['_DATAAGENTCONTEXT'].fields_by_name['data_agent']._loaded_options = None
    _globals['_DATAAGENTCONTEXT'].fields_by_name['data_agent']._serialized_options = b'\xe0A\x02\xfaA.\n,geminidataanalytics.googleapis.com/DataAgent'
    _globals['_DATAAGENTCONTEXT'].fields_by_name['credentials']._loaded_options = None
    _globals['_DATAAGENTCONTEXT'].fields_by_name['credentials']._serialized_options = b'\xe0A\x01'
    _globals['_DATAAGENTCONTEXT'].fields_by_name['context_version']._loaded_options = None
    _globals['_DATAAGENTCONTEXT'].fields_by_name['context_version']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONREFERENCE'].fields_by_name['conversation']._loaded_options = None
    _globals['_CONVERSATIONREFERENCE'].fields_by_name['conversation']._serialized_options = b'\xe0A\x02\xfaA1\n/geminidataanalytics.googleapis.com/Conversation'
    _globals['_CONVERSATIONREFERENCE'].fields_by_name['data_agent_context']._loaded_options = None
    _globals['_CONVERSATIONREFERENCE'].fields_by_name['data_agent_context']._serialized_options = b'\xe0A\x02'
    _globals['_MESSAGE'].fields_by_name['timestamp']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['timestamp']._serialized_options = b'\xe0A\x03'
    _globals['_MESSAGE'].fields_by_name['message_id']._loaded_options = None
    _globals['_MESSAGE'].fields_by_name['message_id']._serialized_options = b'\xe0A\x01'
    _globals['_TEXTMESSAGE'].fields_by_name['parts']._loaded_options = None
    _globals['_TEXTMESSAGE'].fields_by_name['parts']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMAQUERY'].fields_by_name['question']._loaded_options = None
    _globals['_SCHEMAQUERY'].fields_by_name['question']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMARESULT'].fields_by_name['datasources']._loaded_options = None
    _globals['_SCHEMARESULT'].fields_by_name['datasources']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKERQUERY_FILTER'].fields_by_name['field']._loaded_options = None
    _globals['_LOOKERQUERY_FILTER'].fields_by_name['field']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKERQUERY_FILTER'].fields_by_name['value']._loaded_options = None
    _globals['_LOOKERQUERY_FILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKERQUERY'].fields_by_name['model']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['model']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKERQUERY'].fields_by_name['explore']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['explore']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKERQUERY'].fields_by_name['fields']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['fields']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKERQUERY'].fields_by_name['filters']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['filters']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKERQUERY'].fields_by_name['sorts']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['sorts']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKERQUERY'].fields_by_name['limit']._loaded_options = None
    _globals['_LOOKERQUERY'].fields_by_name['limit']._serialized_options = b'\xe0A\x01'
    _globals['_DATAQUERY'].fields_by_name['question']._loaded_options = None
    _globals['_DATAQUERY'].fields_by_name['question']._serialized_options = b'\xe0A\x01'
    _globals['_DATAQUERY'].fields_by_name['name']._loaded_options = None
    _globals['_DATAQUERY'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DATAQUERY'].fields_by_name['datasources']._loaded_options = None
    _globals['_DATAQUERY'].fields_by_name['datasources']._serialized_options = b'\xe0A\x01'
    _globals['_DATARESULT'].fields_by_name['name']._loaded_options = None
    _globals['_DATARESULT'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_DATARESULT'].fields_by_name['schema']._loaded_options = None
    _globals['_DATARESULT'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_DATARESULT'].fields_by_name['data']._loaded_options = None
    _globals['_DATARESULT'].fields_by_name['data']._serialized_options = b'\xe0A\x01'
    _globals['_BIGQUERYJOB'].fields_by_name['project_id']._loaded_options = None
    _globals['_BIGQUERYJOB'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYJOB'].fields_by_name['job_id']._loaded_options = None
    _globals['_BIGQUERYJOB'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYJOB'].fields_by_name['location']._loaded_options = None
    _globals['_BIGQUERYJOB'].fields_by_name['location']._serialized_options = b'\xe0A\x01'
    _globals['_BIGQUERYJOB'].fields_by_name['destination_table']._loaded_options = None
    _globals['_BIGQUERYJOB'].fields_by_name['destination_table']._serialized_options = b'\xe0A\x01'
    _globals['_BIGQUERYJOB'].fields_by_name['schema']._loaded_options = None
    _globals['_BIGQUERYJOB'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_ANALYSISQUERY'].fields_by_name['question']._loaded_options = None
    _globals['_ANALYSISQUERY'].fields_by_name['question']._serialized_options = b'\xe0A\x01'
    _globals['_ANALYSISQUERY'].fields_by_name['data_result_names']._loaded_options = None
    _globals['_ANALYSISQUERY'].fields_by_name['data_result_names']._serialized_options = b'\xe0A\x01'
    _globals['_CHARTQUERY'].fields_by_name['instructions']._loaded_options = None
    _globals['_CHARTQUERY'].fields_by_name['instructions']._serialized_options = b'\xe0A\x01'
    _globals['_CHARTQUERY'].fields_by_name['data_result_name']._loaded_options = None
    _globals['_CHARTQUERY'].fields_by_name['data_result_name']._serialized_options = b'\xe0A\x01'
    _globals['_CHARTRESULT'].fields_by_name['vega_config']._loaded_options = None
    _globals['_CHARTRESULT'].fields_by_name['vega_config']._serialized_options = b'\xe0A\x01'
    _globals['_CHARTRESULT'].fields_by_name['image']._loaded_options = None
    _globals['_CHARTRESULT'].fields_by_name['image']._serialized_options = b'\xe0A\x01'
    _globals['_ERRORMESSAGE'].fields_by_name['text']._loaded_options = None
    _globals['_ERRORMESSAGE'].fields_by_name['text']._serialized_options = b'\xe0A\x03'
    _globals['_BLOB'].fields_by_name['mime_type']._loaded_options = None
    _globals['_BLOB'].fields_by_name['mime_type']._serialized_options = b'\xe0A\x02'
    _globals['_BLOB'].fields_by_name['data']._loaded_options = None
    _globals['_BLOB'].fields_by_name['data']._serialized_options = b'\xe0A\x02'
    _globals['_DATACHATSERVICE']._loaded_options = None
    _globals['_DATACHATSERVICE']._serialized_options = b'\xcaA"geminidataanalytics.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DATACHATSERVICE'].methods_by_name['Chat']._loaded_options = None
    _globals['_DATACHATSERVICE'].methods_by_name['Chat']._serialized_options = b'\x82\xd3\xe4\x93\x021",/v1beta/{parent=projects/*/locations/*}:chat:\x01*'
    _globals['_DATACHATSERVICE'].methods_by_name['CreateConversation']._loaded_options = None
    _globals['_DATACHATSERVICE'].methods_by_name['CreateConversation']._serialized_options = b'\xdaA#parent,conversation,conversation_id\x82\xd3\xe4\x93\x02E"5/v1beta/{parent=projects/*/locations/*}/conversations:\x0cconversation'
    _globals['_DATACHATSERVICE'].methods_by_name['GetConversation']._loaded_options = None
    _globals['_DATACHATSERVICE'].methods_by_name['GetConversation']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta/{name=projects/*/locations/*/conversations/*}'
    _globals['_DATACHATSERVICE'].methods_by_name['ListConversations']._loaded_options = None
    _globals['_DATACHATSERVICE'].methods_by_name['ListConversations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta/{parent=projects/*/locations/*}/conversations'
    _globals['_DATACHATSERVICE'].methods_by_name['ListMessages']._loaded_options = None
    _globals['_DATACHATSERVICE'].methods_by_name['ListMessages']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta/{parent=projects/*/locations/*/conversations/*}/messages'
    _globals['_LISTMESSAGESREQUEST']._serialized_start = 519
    _globals['_LISTMESSAGESREQUEST']._serialized_end = 683
    _globals['_LISTMESSAGESRESPONSE']._serialized_start = 685
    _globals['_LISTMESSAGESRESPONSE']._serialized_end = 807
    _globals['_STORAGEMESSAGE']._serialized_start = 809
    _globals['_STORAGEMESSAGE']._serialized_end = 912
    _globals['_CHATREQUEST']._serialized_start = 915
    _globals['_CHATREQUEST']._serialized_end = 1392
    _globals['_DATAAGENTCONTEXT']._serialized_start = 1395
    _globals['_DATAAGENTCONTEXT']._serialized_end = 1750
    _globals['_DATAAGENTCONTEXT_CONTEXTVERSION']._serialized_start = 1673
    _globals['_DATAAGENTCONTEXT_CONTEXTVERSION']._serialized_end = 1750
    _globals['_CONVERSATIONREFERENCE']._serialized_start = 1753
    _globals['_CONVERSATIONREFERENCE']._serialized_end = 1947
    _globals['_MESSAGE']._serialized_start = 1950
    _globals['_MESSAGE']._serialized_end = 2204
    _globals['_USERMESSAGE']._serialized_start = 2206
    _globals['_USERMESSAGE']._serialized_end = 2243
    _globals['_SYSTEMMESSAGE']._serialized_start = 2246
    _globals['_SYSTEMMESSAGE']._serialized_end = 2741
    _globals['_TEXTMESSAGE']._serialized_start = 2743
    _globals['_TEXTMESSAGE']._serialized_end = 2776
    _globals['_SCHEMAMESSAGE']._serialized_start = 2779
    _globals['_SCHEMAMESSAGE']._serialized_end = 2946
    _globals['_SCHEMAQUERY']._serialized_start = 2948
    _globals['_SCHEMAQUERY']._serialized_end = 2984
    _globals['_SCHEMARESULT']._serialized_start = 2986
    _globals['_SCHEMARESULT']._serialized_end = 3079
    _globals['_DATAMESSAGE']._serialized_start = 3082
    _globals['_DATAMESSAGE']._serialized_end = 3435
    _globals['_LOOKERQUERY']._serialized_start = 3438
    _globals['_LOOKERQUERY']._serialized_end = 3702
    _globals['_LOOKERQUERY_FILTER']._serialized_start = 3644
    _globals['_LOOKERQUERY_FILTER']._serialized_end = 3692
    _globals['_DATAQUERY']._serialized_start = 3705
    _globals['_DATAQUERY']._serialized_end = 3837
    _globals['_DATARESULT']._serialized_start = 3840
    _globals['_DATARESULT']._serialized_end = 3985
    _globals['_BIGQUERYJOB']._serialized_start = 3988
    _globals['_BIGQUERYJOB']._serialized_end = 4237
    _globals['_ANALYSISMESSAGE']._serialized_start = 4240
    _globals['_ANALYSISMESSAGE']._serialized_end = 4420
    _globals['_ANALYSISQUERY']._serialized_start = 4422
    _globals['_ANALYSISQUERY']._serialized_end = 4492
    _globals['_ANALYSISEVENT']._serialized_start = 4495
    _globals['_ANALYSISEVENT']._serialized_end = 4793
    _globals['_CHARTMESSAGE']._serialized_start = 4796
    _globals['_CHARTMESSAGE']._serialized_end = 4960
    _globals['_CHARTQUERY']._serialized_start = 4962
    _globals['_CHARTQUERY']._serialized_end = 5032
    _globals['_CHARTRESULT']._serialized_start = 5035
    _globals['_CHARTRESULT']._serialized_end = 5166
    _globals['_ERRORMESSAGE']._serialized_start = 5168
    _globals['_ERRORMESSAGE']._serialized_end = 5201
    _globals['_BLOB']._serialized_start = 5203
    _globals['_BLOB']._serialized_end = 5252
    _globals['_DATACHATSERVICE']._serialized_start = 5255
    _globals['_DATACHATSERVICE']._serialized_end = 6457