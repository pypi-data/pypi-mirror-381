"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3beta1/agent.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import audio_config_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_audio__config__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import bigquery_export_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_bigquery__export__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import flow_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_flow__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_generative__settings__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/dialogflow/cx/v3beta1/agent.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/dialogflow/cx/v3beta1/advanced_settings.proto\x1a5google/cloud/dialogflow/cx/v3beta1/audio_config.proto\x1a8google/cloud/dialogflow/cx/v3beta1/bigquery_export.proto\x1a-google/cloud/dialogflow/cx/v3beta1/flow.proto\x1a<google/cloud/dialogflow/cx/v3beta1/generative_settings.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/protobuf/struct.proto"8\n\x14SpeechToTextSettings\x12 \n\x18enable_speech_adaptation\x18\x01 \x01(\x08"\x99\x15\n\x05Agent\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12%\n\x15default_language_code\x18\x03 \x01(\tB\x06\xe0A\x02\xe0A\x05\x12 \n\x18supported_language_codes\x18\x04 \x03(\t\x12\x16\n\ttime_zone\x18\x05 \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x06 \x01(\t\x12\x12\n\navatar_uri\x18\x07 \x01(\t\x12Y\n\x17speech_to_text_settings\x18\r \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.SpeechToTextSettings\x129\n\nstart_flow\x18\x10 \x01(\tB#\xfaA \n\x1edialogflow.googleapis.com/FlowH\x00\x12A\n\x0estart_playbook\x18\' \x01(\tB\'\xfaA$\n"dialogflow.googleapis.com/PlaybookH\x00\x12J\n\x11security_settings\x18\x11 \x01(\tB/\xfaA,\n*dialogflow.googleapis.com/SecuritySettings\x12&\n\x1aenable_stackdriver_logging\x18\x12 \x01(\x08B\x02\x18\x01\x12\x1f\n\x17enable_spell_correction\x18\x14 \x01(\x08\x12+\n\x1eenable_multi_language_training\x18( \x01(\x08B\x03\xe0A\x01\x12\x0e\n\x06locked\x18\x1b \x01(\x08\x12O\n\x11advanced_settings\x18\x16 \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings\x12b\n\x18git_integration_settings\x18\x1e \x01(\x0b2@.google.cloud.dialogflow.cx.v3beta1.Agent.GitIntegrationSettings\x12a\n\x18bigquery_export_settings\x18\x1d \x01(\x0b2:.google.cloud.dialogflow.cx.v3beta1.BigQueryExportSettingsB\x03\xe0A\x01\x12Y\n\x17text_to_speech_settings\x18\x1f \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.TextToSpeechSettings\x12f\n\x18gen_app_builder_settings\x18! \x01(\x0b2?.google.cloud.dialogflow.cx.v3beta1.Agent.GenAppBuilderSettingsH\x01\x88\x01\x01\x12g\n\x18answer_feedback_settings\x18& \x01(\x0b2@.google.cloud.dialogflow.cx.v3beta1.Agent.AnswerFeedbackSettingsB\x03\xe0A\x01\x12h\n\x18personalization_settings\x18* \x01(\x0b2A.google.cloud.dialogflow.cx.v3beta1.Agent.PersonalizationSettingsB\x03\xe0A\x01\x12m\n\x1bclient_certificate_settings\x18+ \x01(\x0b2C.google.cloud.dialogflow.cx.v3beta1.Agent.ClientCertificateSettingsB\x03\xe0A\x01\x12"\n\rsatisfies_pzs\x18- \x01(\x08B\x06\xe0A\x01\xe0A\x03H\x02\x88\x01\x01\x12"\n\rsatisfies_pzi\x18. \x01(\x08B\x06\xe0A\x01\xe0A\x03H\x03\x88\x01\x01\x1a\xfd\x04\n\x16GitIntegrationSettings\x12j\n\x0fgithub_settings\x18\x01 \x01(\x0b2O.google.cloud.dialogflow.cx.v3beta1.Agent.GitIntegrationSettings.GithubSettingsH\x00\x12y\n\x17git_connection_settings\x18\x02 \x01(\x0b2V.google.cloud.dialogflow.cx.v3beta1.Agent.GitIntegrationSettings.GitConnectionSettingsH\x00\x1a\x7f\n\x0eGithubSettings\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x16\n\x0erepository_uri\x18\x02 \x01(\t\x12\x17\n\x0ftracking_branch\x18\x03 \x01(\t\x12\x14\n\x0caccess_token\x18\x04 \x01(\t\x12\x10\n\x08branches\x18\x05 \x03(\t\x1a\xea\x01\n\x15GitConnectionSettings\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1b\n\x0erepository_uri\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x1c\n\x0ftracking_branch\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08branches\x18\x04 \x03(\tB\x03\xe0A\x01\x12N\n\x13access_token_secret\x18\x05 \x01(\tB/\xfaA,\n*secretmanager.googleapis.com/SecretVersionH\x00B\x14\n\x12git_authenticationB\x0e\n\x0cgit_settings\x1a,\n\x15GenAppBuilderSettings\x12\x13\n\x06engine\x18\x01 \x01(\tB\x03\xe0A\x02\x1a=\n\x16AnswerFeedbackSettings\x12#\n\x16enable_answer_feedback\x18\x01 \x01(\x08B\x03\xe0A\x01\x1aZ\n\x17PersonalizationSettings\x12?\n\x19default_end_user_metadata\x18\x01 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x1a\xca\x01\n\x19ClientCertificateSettings\x12\x1c\n\x0fssl_certificate\x18\x01 \x01(\tB\x03\xe0A\x02\x12G\n\x0bprivate_key\x18\x02 \x01(\tB2\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion\x12F\n\npassphrase\x18\x03 \x01(\tB2\xe0A\x01\xfaA,\n*secretmanager.googleapis.com/SecretVersion:\\\xeaAY\n\x1fdialogflow.googleapis.com/Agent\x126projects/{project}/locations/{location}/agents/{agent}B\x18\n\x16session_entry_resourceB\x1b\n\x19_gen_app_builder_settingsB\x10\n\x0e_satisfies_pzsB\x10\n\x0e_satisfies_pzi"s\n\x11ListAgentsRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"h\n\x12ListAgentsResponse\x129\n\x06agents\x18\x01 \x03(\x0b2).google.cloud.dialogflow.cx.v3beta1.Agent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"H\n\x0fGetAgentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent"\x8c\x01\n\x12CreateAgentRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent\x12=\n\x05agent\x18\x02 \x01(\x0b2).google.cloud.dialogflow.cx.v3beta1.AgentB\x03\xe0A\x02"\x84\x01\n\x12UpdateAgentRequest\x12=\n\x05agent\x18\x01 \x01(\x0b2).google.cloud.dialogflow.cx.v3beta1.AgentB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x12DeleteAgentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent"\xa2\x04\n\x12ExportAgentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12\x16\n\tagent_uri\x18\x02 \x01(\tB\x03\xe0A\x01\x12[\n\x0bdata_format\x18\x03 \x01(\x0e2A.google.cloud.dialogflow.cx.v3beta1.ExportAgentRequest.DataFormatB\x03\xe0A\x01\x12B\n\x0benvironment\x18\x05 \x01(\tB-\xe0A\x01\xfaA\'\n%dialogflow.googleapis.com/Environment\x12c\n\x0fgit_destination\x18\x06 \x01(\x0b2E.google.cloud.dialogflow.cx.v3beta1.ExportAgentRequest.GitDestinationB\x03\xe0A\x01\x12-\n include_bigquery_export_settings\x18\x07 \x01(\x08B\x03\xe0A\x01\x1aA\n\x0eGitDestination\x12\x17\n\x0ftracking_branch\x18\x01 \x01(\t\x12\x16\n\x0ecommit_message\x18\x02 \x01(\t"E\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04BLOB\x10\x01\x12\x10\n\x0cJSON_PACKAGE\x10\x04"b\n\x13ExportAgentResponse\x12\x13\n\tagent_uri\x18\x01 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x02 \x01(\x0cH\x00\x12\x14\n\ncommit_sha\x18\x03 \x01(\tH\x00B\x07\n\x05agent"\xaa\x03\n\x13RestoreAgentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12\x13\n\tagent_uri\x18\x02 \x01(\tH\x00\x12\x17\n\ragent_content\x18\x03 \x01(\x0cH\x00\x12W\n\ngit_source\x18\x06 \x01(\x0b2A.google.cloud.dialogflow.cx.v3beta1.RestoreAgentRequest.GitSourceH\x00\x12]\n\x0erestore_option\x18\x05 \x01(\x0e2E.google.cloud.dialogflow.cx.v3beta1.RestoreAgentRequest.RestoreOption\x1a$\n\tGitSource\x12\x17\n\x0ftracking_branch\x18\x01 \x01(\t"G\n\rRestoreOption\x12\x1e\n\x1aRESTORE_OPTION_UNSPECIFIED\x10\x00\x12\x08\n\x04KEEP\x10\x01\x12\x0c\n\x08FALLBACK\x10\x02B\x07\n\x05agent"d\n\x14ValidateAgentRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\x7f\n\x1fGetAgentValidationResultRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/dialogflow.googleapis.com/AgentValidationResult\x12\x15\n\rlanguage_code\x18\x02 \x01(\t"\xff\x01\n\x15AgentValidationResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12Y\n\x17flow_validation_results\x18\x02 \x03(\x0b28.google.cloud.dialogflow.cx.v3beta1.FlowValidationResult:}\xeaAz\n/dialogflow.googleapis.com/AgentValidationResult\x12Gprojects/{project}/locations/{location}/agents/{agent}/validationResult"\x83\x01\n\x1cGetGenerativeSettingsRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1dialogflow.googleapis.com/AgentGenerativeSettings\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x02"\xb1\x01\n\x1fUpdateGenerativeSettingsRequest\x12X\n\x13generative_settings\x18\x01 \x01(\x0b26.google.cloud.dialogflow.cx.v3beta1.GenerativeSettingsB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x012\xb8\x13\n\x06Agents\x12\xbd\x01\n\nListAgents\x125.google.cloud.dialogflow.cx.v3beta1.ListAgentsRequest\x1a6.google.cloud.dialogflow.cx.v3beta1.ListAgentsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v3beta1/{parent=projects/*/locations/*}/agents\x12\xaa\x01\n\x08GetAgent\x123.google.cloud.dialogflow.cx.v3beta1.GetAgentRequest\x1a).google.cloud.dialogflow.cx.v3beta1.Agent">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v3beta1/{name=projects/*/locations/*/agents/*}\x12\xbf\x01\n\x0bCreateAgent\x126.google.cloud.dialogflow.cx.v3beta1.CreateAgentRequest\x1a).google.cloud.dialogflow.cx.v3beta1.Agent"M\xdaA\x0cparent,agent\x82\xd3\xe4\x93\x028"//v3beta1/{parent=projects/*/locations/*}/agents:\x05agent\x12\xca\x01\n\x0bUpdateAgent\x126.google.cloud.dialogflow.cx.v3beta1.UpdateAgentRequest\x1a).google.cloud.dialogflow.cx.v3beta1.Agent"X\xdaA\x11agent,update_mask\x82\xd3\xe4\x93\x02>25/v3beta1/{agent.name=projects/*/locations/*/agents/*}:\x05agent\x12\x9d\x01\n\x0bDeleteAgent\x126.google.cloud.dialogflow.cx.v3beta1.DeleteAgentRequest\x1a\x16.google.protobuf.Empty">\xdaA\x04name\x82\xd3\xe4\x93\x021*//v3beta1/{name=projects/*/locations/*/agents/*}\x12\xd7\x01\n\x0bExportAgent\x126.google.cloud.dialogflow.cx.v3beta1.ExportAgentRequest\x1a\x1d.google.longrunning.Operation"q\xcaA-\n\x13ExportAgentResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02;"6/v3beta1/{name=projects/*/locations/*/agents/*}:export:\x01*\x12\xdc\x01\n\x0cRestoreAgent\x127.google.cloud.dialogflow.cx.v3beta1.RestoreAgentRequest\x1a\x1d.google.longrunning.Operation"t\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02<"7/v3beta1/{name=projects/*/locations/*/agents/*}:restore:\x01*\x12\xc9\x01\n\rValidateAgent\x128.google.cloud.dialogflow.cx.v3beta1.ValidateAgentRequest\x1a9.google.cloud.dialogflow.cx.v3beta1.AgentValidationResult"C\x82\xd3\xe4\x93\x02="8/v3beta1/{name=projects/*/locations/*/agents/*}:validate:\x01*\x12\xeb\x01\n\x18GetAgentValidationResult\x12C.google.cloud.dialogflow.cx.v3beta1.GetAgentValidationResultRequest\x1a9.google.cloud.dialogflow.cx.v3beta1.AgentValidationResult"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v3beta1/{name=projects/*/locations/*/agents/*/validationResult}\x12\xf2\x01\n\x15GetGenerativeSettings\x12@.google.cloud.dialogflow.cx.v3beta1.GetGenerativeSettingsRequest\x1a6.google.cloud.dialogflow.cx.v3beta1.GenerativeSettings"_\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/generativeSettings}\x12\xaf\x02\n\x18UpdateGenerativeSettings\x12C.google.cloud.dialogflow.cx.v3beta1.UpdateGenerativeSettingsRequest\x1a6.google.cloud.dialogflow.cx.v3beta1.GenerativeSettings"\x95\x01\xdaA\x1fgenerative_settings,update_mask\x82\xd3\xe4\x93\x02m2V/v3beta1/{generative_settings.name=projects/*/locations/*/agents/*/generativeSettings}:\x13generative_settings\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xa8\x02\n&com.google.cloud.dialogflow.cx.v3beta1B\nAgentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\nAgentProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1\xeaAd\n*secretmanager.googleapis.com/SecretVersion\x126projects/{project}/secrets/{secret}/versions/{version}'
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['display_name']._loaded_options = None
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['repository_uri']._loaded_options = None
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['repository_uri']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['tracking_branch']._loaded_options = None
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['tracking_branch']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['branches']._loaded_options = None
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['branches']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['access_token_secret']._loaded_options = None
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS'].fields_by_name['access_token_secret']._serialized_options = b'\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_AGENT_GENAPPBUILDERSETTINGS'].fields_by_name['engine']._loaded_options = None
    _globals['_AGENT_GENAPPBUILDERSETTINGS'].fields_by_name['engine']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT_ANSWERFEEDBACKSETTINGS'].fields_by_name['enable_answer_feedback']._loaded_options = None
    _globals['_AGENT_ANSWERFEEDBACKSETTINGS'].fields_by_name['enable_answer_feedback']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT_PERSONALIZATIONSETTINGS'].fields_by_name['default_end_user_metadata']._loaded_options = None
    _globals['_AGENT_PERSONALIZATIONSETTINGS'].fields_by_name['default_end_user_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['ssl_certificate']._loaded_options = None
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['ssl_certificate']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['private_key']._loaded_options = None
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['private_key']._serialized_options = b'\xe0A\x02\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['passphrase']._loaded_options = None
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS'].fields_by_name['passphrase']._serialized_options = b'\xe0A\x01\xfaA,\n*secretmanager.googleapis.com/SecretVersion'
    _globals['_AGENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_AGENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT'].fields_by_name['default_language_code']._loaded_options = None
    _globals['_AGENT'].fields_by_name['default_language_code']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_AGENT'].fields_by_name['time_zone']._loaded_options = None
    _globals['_AGENT'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_AGENT'].fields_by_name['start_flow']._loaded_options = None
    _globals['_AGENT'].fields_by_name['start_flow']._serialized_options = b'\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_AGENT'].fields_by_name['start_playbook']._loaded_options = None
    _globals['_AGENT'].fields_by_name['start_playbook']._serialized_options = b'\xfaA$\n"dialogflow.googleapis.com/Playbook'
    _globals['_AGENT'].fields_by_name['security_settings']._loaded_options = None
    _globals['_AGENT'].fields_by_name['security_settings']._serialized_options = b'\xfaA,\n*dialogflow.googleapis.com/SecuritySettings'
    _globals['_AGENT'].fields_by_name['enable_stackdriver_logging']._loaded_options = None
    _globals['_AGENT'].fields_by_name['enable_stackdriver_logging']._serialized_options = b'\x18\x01'
    _globals['_AGENT'].fields_by_name['enable_multi_language_training']._loaded_options = None
    _globals['_AGENT'].fields_by_name['enable_multi_language_training']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT'].fields_by_name['bigquery_export_settings']._loaded_options = None
    _globals['_AGENT'].fields_by_name['bigquery_export_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT'].fields_by_name['answer_feedback_settings']._loaded_options = None
    _globals['_AGENT'].fields_by_name['answer_feedback_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT'].fields_by_name['personalization_settings']._loaded_options = None
    _globals['_AGENT'].fields_by_name['personalization_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT'].fields_by_name['client_certificate_settings']._loaded_options = None
    _globals['_AGENT'].fields_by_name['client_certificate_settings']._serialized_options = b'\xe0A\x01'
    _globals['_AGENT'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_AGENT'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_AGENT'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_AGENT'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_AGENT']._loaded_options = None
    _globals['_AGENT']._serialized_options = b'\xeaAY\n\x1fdialogflow.googleapis.com/Agent\x126projects/{project}/locations/{location}/agents/{agent}'
    _globals['_LISTAGENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAGENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_GETAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_CREATEAGENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAGENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fdialogflow.googleapis.com/Agent'
    _globals['_CREATEAGENTREQUEST'].fields_by_name['agent']._loaded_options = None
    _globals['_CREATEAGENTREQUEST'].fields_by_name['agent']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEAGENTREQUEST'].fields_by_name['agent']._loaded_options = None
    _globals['_UPDATEAGENTREQUEST'].fields_by_name['agent']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['agent_uri']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['agent_uri']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['environment']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['environment']._serialized_options = b"\xe0A\x01\xfaA'\n%dialogflow.googleapis.com/Environment"
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['git_destination']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['git_destination']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['include_bigquery_export_settings']._loaded_options = None
    _globals['_EXPORTAGENTREQUEST'].fields_by_name['include_bigquery_export_settings']._serialized_options = b'\xe0A\x01'
    _globals['_RESTOREAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESTOREAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_VALIDATEAGENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_VALIDATEAGENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fdialogflow.googleapis.com/Agent'
    _globals['_GETAGENTVALIDATIONRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAGENTVALIDATIONRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/dialogflow.googleapis.com/AgentValidationResult'
    _globals['_AGENTVALIDATIONRESULT']._loaded_options = None
    _globals['_AGENTVALIDATIONRESULT']._serialized_options = b'\xeaAz\n/dialogflow.googleapis.com/AgentValidationResult\x12Gprojects/{project}/locations/{location}/agents/{agent}/validationResult'
    _globals['_GETGENERATIVESETTINGSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGENERATIVESETTINGSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1dialogflow.googleapis.com/AgentGenerativeSettings'
    _globals['_GETGENERATIVESETTINGSREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETGENERATIVESETTINGSREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGENERATIVESETTINGSREQUEST'].fields_by_name['generative_settings']._loaded_options = None
    _globals['_UPDATEGENERATIVESETTINGSREQUEST'].fields_by_name['generative_settings']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGENERATIVESETTINGSREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGENERATIVESETTINGSREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_AGENTS']._loaded_options = None
    _globals['_AGENTS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_AGENTS'].methods_by_name['ListAgents']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['ListAgents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v3beta1/{parent=projects/*/locations/*}/agents'
    _globals['_AGENTS'].methods_by_name['GetAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['GetAgent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v3beta1/{name=projects/*/locations/*/agents/*}'
    _globals['_AGENTS'].methods_by_name['CreateAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['CreateAgent']._serialized_options = b'\xdaA\x0cparent,agent\x82\xd3\xe4\x93\x028"//v3beta1/{parent=projects/*/locations/*}/agents:\x05agent'
    _globals['_AGENTS'].methods_by_name['UpdateAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['UpdateAgent']._serialized_options = b'\xdaA\x11agent,update_mask\x82\xd3\xe4\x93\x02>25/v3beta1/{agent.name=projects/*/locations/*/agents/*}:\x05agent'
    _globals['_AGENTS'].methods_by_name['DeleteAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['DeleteAgent']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021*//v3beta1/{name=projects/*/locations/*/agents/*}'
    _globals['_AGENTS'].methods_by_name['ExportAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['ExportAgent']._serialized_options = b'\xcaA-\n\x13ExportAgentResponse\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02;"6/v3beta1/{name=projects/*/locations/*/agents/*}:export:\x01*'
    _globals['_AGENTS'].methods_by_name['RestoreAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['RestoreAgent']._serialized_options = b'\xcaA/\n\x15google.protobuf.Empty\x12\x16google.protobuf.Struct\x82\xd3\xe4\x93\x02<"7/v3beta1/{name=projects/*/locations/*/agents/*}:restore:\x01*'
    _globals['_AGENTS'].methods_by_name['ValidateAgent']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['ValidateAgent']._serialized_options = b'\x82\xd3\xe4\x93\x02="8/v3beta1/{name=projects/*/locations/*/agents/*}:validate:\x01*'
    _globals['_AGENTS'].methods_by_name['GetAgentValidationResult']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['GetAgentValidationResult']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v3beta1/{name=projects/*/locations/*/agents/*/validationResult}'
    _globals['_AGENTS'].methods_by_name['GetGenerativeSettings']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['GetGenerativeSettings']._serialized_options = b'\xdaA\x12name,language_code\x82\xd3\xe4\x93\x02D\x12B/v3beta1/{name=projects/*/locations/*/agents/*/generativeSettings}'
    _globals['_AGENTS'].methods_by_name['UpdateGenerativeSettings']._loaded_options = None
    _globals['_AGENTS'].methods_by_name['UpdateGenerativeSettings']._serialized_options = b'\xdaA\x1fgenerative_settings,update_mask\x82\xd3\xe4\x93\x02m2V/v3beta1/{generative_settings.name=projects/*/locations/*/agents/*/generativeSettings}:\x13generative_settings'
    _globals['_SPEECHTOTEXTSETTINGS']._serialized_start = 613
    _globals['_SPEECHTOTEXTSETTINGS']._serialized_end = 669
    _globals['_AGENT']._serialized_start = 672
    _globals['_AGENT']._serialized_end = 3385
    _globals['_AGENT_GITINTEGRATIONSETTINGS']._serialized_start = 2157
    _globals['_AGENT_GITINTEGRATIONSETTINGS']._serialized_end = 2794
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITHUBSETTINGS']._serialized_start = 2414
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITHUBSETTINGS']._serialized_end = 2541
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS']._serialized_start = 2544
    _globals['_AGENT_GITINTEGRATIONSETTINGS_GITCONNECTIONSETTINGS']._serialized_end = 2778
    _globals['_AGENT_GENAPPBUILDERSETTINGS']._serialized_start = 2796
    _globals['_AGENT_GENAPPBUILDERSETTINGS']._serialized_end = 2840
    _globals['_AGENT_ANSWERFEEDBACKSETTINGS']._serialized_start = 2842
    _globals['_AGENT_ANSWERFEEDBACKSETTINGS']._serialized_end = 2903
    _globals['_AGENT_PERSONALIZATIONSETTINGS']._serialized_start = 2905
    _globals['_AGENT_PERSONALIZATIONSETTINGS']._serialized_end = 2995
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS']._serialized_start = 2998
    _globals['_AGENT_CLIENTCERTIFICATESETTINGS']._serialized_end = 3200
    _globals['_LISTAGENTSREQUEST']._serialized_start = 3387
    _globals['_LISTAGENTSREQUEST']._serialized_end = 3502
    _globals['_LISTAGENTSRESPONSE']._serialized_start = 3504
    _globals['_LISTAGENTSRESPONSE']._serialized_end = 3608
    _globals['_GETAGENTREQUEST']._serialized_start = 3610
    _globals['_GETAGENTREQUEST']._serialized_end = 3682
    _globals['_CREATEAGENTREQUEST']._serialized_start = 3685
    _globals['_CREATEAGENTREQUEST']._serialized_end = 3825
    _globals['_UPDATEAGENTREQUEST']._serialized_start = 3828
    _globals['_UPDATEAGENTREQUEST']._serialized_end = 3960
    _globals['_DELETEAGENTREQUEST']._serialized_start = 3962
    _globals['_DELETEAGENTREQUEST']._serialized_end = 4037
    _globals['_EXPORTAGENTREQUEST']._serialized_start = 4040
    _globals['_EXPORTAGENTREQUEST']._serialized_end = 4586
    _globals['_EXPORTAGENTREQUEST_GITDESTINATION']._serialized_start = 4450
    _globals['_EXPORTAGENTREQUEST_GITDESTINATION']._serialized_end = 4515
    _globals['_EXPORTAGENTREQUEST_DATAFORMAT']._serialized_start = 4517
    _globals['_EXPORTAGENTREQUEST_DATAFORMAT']._serialized_end = 4586
    _globals['_EXPORTAGENTRESPONSE']._serialized_start = 4588
    _globals['_EXPORTAGENTRESPONSE']._serialized_end = 4686
    _globals['_RESTOREAGENTREQUEST']._serialized_start = 4689
    _globals['_RESTOREAGENTREQUEST']._serialized_end = 5115
    _globals['_RESTOREAGENTREQUEST_GITSOURCE']._serialized_start = 4997
    _globals['_RESTOREAGENTREQUEST_GITSOURCE']._serialized_end = 5033
    _globals['_RESTOREAGENTREQUEST_RESTOREOPTION']._serialized_start = 5035
    _globals['_RESTOREAGENTREQUEST_RESTOREOPTION']._serialized_end = 5106
    _globals['_VALIDATEAGENTREQUEST']._serialized_start = 5117
    _globals['_VALIDATEAGENTREQUEST']._serialized_end = 5217
    _globals['_GETAGENTVALIDATIONRESULTREQUEST']._serialized_start = 5219
    _globals['_GETAGENTVALIDATIONRESULTREQUEST']._serialized_end = 5346
    _globals['_AGENTVALIDATIONRESULT']._serialized_start = 5349
    _globals['_AGENTVALIDATIONRESULT']._serialized_end = 5604
    _globals['_GETGENERATIVESETTINGSREQUEST']._serialized_start = 5607
    _globals['_GETGENERATIVESETTINGSREQUEST']._serialized_end = 5738
    _globals['_UPDATEGENERATIVESETTINGSREQUEST']._serialized_start = 5741
    _globals['_UPDATEGENERATIVESETTINGSREQUEST']._serialized_end = 5918
    _globals['_AGENTS']._serialized_start = 5921
    _globals['_AGENTS']._serialized_end = 8409