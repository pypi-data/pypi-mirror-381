"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3beta1/playbook.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import advanced_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_advanced__settings__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import example_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_example__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import fulfillment_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_fulfillment__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import generative_settings_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_generative__settings__pb2
from ......google.cloud.dialogflow.cx.v3beta1 import parameter_definition_pb2 as google_dot_cloud_dot_dialogflow_dot_cx_dot_v3beta1_dot_parameter__definition__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/dialogflow/cx/v3beta1/playbook.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/dialogflow/cx/v3beta1/advanced_settings.proto\x1a0google/cloud/dialogflow/cx/v3beta1/example.proto\x1a4google/cloud/dialogflow/cx/v3beta1/fulfillment.proto\x1a<google/cloud/dialogflow/cx/v3beta1/generative_settings.proto\x1a=google/cloud/dialogflow/cx/v3beta1/parameter_definition.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x98\x01\n\x15CreatePlaybookRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Playbook\x12C\n\x08playbook\x18\x02 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.PlaybookB\x03\xe0A\x02"Q\n\x15DeletePlaybookRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook"y\n\x14ListPlaybooksRequest\x12:\n\x06parent\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Playbook\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"q\n\x15ListPlaybooksResponse\x12?\n\tplaybooks\x18\x01 \x03(\x0b2,.google.cloud.dialogflow.cx.v3beta1.Playbook\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"N\n\x12GetPlaybookRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook"\x8d\x01\n\x15UpdatePlaybookRequest\x12C\n\x08playbook\x18\x01 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.PlaybookB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xf2\t\n\x08Playbook\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x11\n\x04goal\x18\x03 \x01(\tB\x03\xe0A\x02\x12a\n\x1binput_parameter_definitions\x18\x05 \x03(\x0b27.google.cloud.dialogflow.cx.v3beta1.ParameterDefinitionB\x03\xe0A\x01\x12b\n\x1coutput_parameter_definitions\x18\x06 \x03(\x0b27.google.cloud.dialogflow.cx.v3beta1.ParameterDefinitionB\x03\xe0A\x01\x12M\n\x0binstruction\x18\x11 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.Playbook.Instruction\x12\x18\n\x0btoken_count\x18\x08 \x01(\x03B\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x14referenced_playbooks\x18\x0b \x03(\tB*\xe0A\x03\xfaA$\n"dialogflow.googleapis.com/Playbook\x12@\n\x10referenced_flows\x18\x0c \x03(\tB&\xe0A\x03\xfaA \n\x1edialogflow.googleapis.com/Flow\x12@\n\x10referenced_tools\x18\r \x03(\tB&\xe0A\x01\xfaA \n\x1edialogflow.googleapis.com/Tool\x12U\n\x12llm_model_settings\x18\x0e \x01(\x0b24.google.cloud.dialogflow.cx.v3beta1.LlmModelSettingsB\x03\xe0A\x01\x12a\n\x0fspeech_settings\x18\x14 \x01(\x0b2C.google.cloud.dialogflow.cx.v3beta1.AdvancedSettings.SpeechSettingsB\x03\xe0A\x01\x12B\n\x08handlers\x18\x10 \x03(\x0b2+.google.cloud.dialogflow.cx.v3beta1.HandlerB\x03\xe0A\x01\x1ag\n\x04Step\x12\x0e\n\x04text\x18\x01 \x01(\tH\x00\x12@\n\x05steps\x18\x02 \x03(\x0b21.google.cloud.dialogflow.cx.v3beta1.Playbook.StepB\r\n\x0binstruction\x1ac\n\x0bInstruction\x12\x12\n\nguidelines\x18\x01 \x01(\t\x12@\n\x05steps\x18\x02 \x03(\x0b21.google.cloud.dialogflow.cx.v3beta1.Playbook.Step:t\xeaAq\n"dialogflow.googleapis.com/Playbook\x12Kprojects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}"\xb5\x01\n\x1cCreatePlaybookVersionRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)dialogflow.googleapis.com/PlaybookVersion\x12R\n\x10playbook_version\x18\x02 \x01(\x0b23.google.cloud.dialogflow.cx.v3beta1.PlaybookVersionB\x03\xe0A\x02"\xad\x03\n\x0fPlaybookVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12C\n\x08playbook\x18\x03 \x01(\x0b2,.google.cloud.dialogflow.cx.v3beta1.PlaybookB\x03\xe0A\x03\x12B\n\x08examples\x18\x04 \x03(\x0b2+.google.cloud.dialogflow.cx.v3beta1.ExampleB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:\xb2\x01\xeaA\xae\x01\n)dialogflow.googleapis.com/PlaybookVersion\x12^projects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}/versions/{version}*\x10playbookVersions2\x0fplaybookVersion"\\\n\x19GetPlaybookVersionRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)dialogflow.googleapis.com/PlaybookVersion"\x91\x01\n\x1bListPlaybookVersionsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)dialogflow.googleapis.com/PlaybookVersion\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x87\x01\n\x1cListPlaybookVersionsResponse\x12N\n\x11playbook_versions\x18\x01 \x03(\x0b23.google.cloud.dialogflow.cx.v3beta1.PlaybookVersion\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"_\n\x1cDeletePlaybookVersionRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)dialogflow.googleapis.com/PlaybookVersion"\xe0\x03\n\x07Handler\x12Q\n\revent_handler\x18\x01 \x01(\x0b28.google.cloud.dialogflow.cx.v3beta1.Handler.EventHandlerH\x00\x12Y\n\x11lifecycle_handler\x18\x03 \x01(\x0b2<.google.cloud.dialogflow.cx.v3beta1.Handler.LifecycleHandlerH\x00\x1a\x85\x01\n\x0cEventHandler\x12\x12\n\x05event\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tcondition\x18\x03 \x01(\tB\x03\xe0A\x01\x12I\n\x0bfulfillment\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.FulfillmentB\x03\xe0A\x02\x1a\x93\x01\n\x10LifecycleHandler\x12\x1c\n\x0flifecycle_stage\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\tcondition\x18\x02 \x01(\tB\x03\xe0A\x01\x12I\n\x0bfulfillment\x18\x03 \x01(\x0b2/.google.cloud.dialogflow.cx.v3beta1.FulfillmentB\x03\xe0A\x02B\t\n\x07handler2\xc5\x10\n\tPlaybooks\x12\xda\x01\n\x0eCreatePlaybook\x129.google.cloud.dialogflow.cx.v3beta1.CreatePlaybookRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.Playbook"_\xdaA\x0fparent,playbook\x82\xd3\xe4\x93\x02G";/v3beta1/{parent=projects/*/locations/*/agents/*}/playbooks:\x08playbook\x12\xaf\x01\n\x0eDeletePlaybook\x129.google.cloud.dialogflow.cx.v3beta1.DeletePlaybookRequest\x1a\x16.google.protobuf.Empty"J\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*}\x12\xd2\x01\n\rListPlaybooks\x128.google.cloud.dialogflow.cx.v3beta1.ListPlaybooksRequest\x1a9.google.cloud.dialogflow.cx.v3beta1.ListPlaybooksResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{parent=projects/*/locations/*/agents/*}/playbooks\x12\xbf\x01\n\x0bGetPlaybook\x126.google.cloud.dialogflow.cx.v3beta1.GetPlaybookRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.Playbook"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*}\x12\xe8\x01\n\x0eUpdatePlaybook\x129.google.cloud.dialogflow.cx.v3beta1.UpdatePlaybookRequest\x1a,.google.cloud.dialogflow.cx.v3beta1.Playbook"m\xdaA\x14playbook,update_mask\x82\xd3\xe4\x93\x02P2D/v3beta1/{playbook.name=projects/*/locations/*/agents/*/playbooks/*}:\x08playbook\x12\x8a\x02\n\x15CreatePlaybookVersion\x12@.google.cloud.dialogflow.cx.v3beta1.CreatePlaybookVersionRequest\x1a3.google.cloud.dialogflow.cx.v3beta1.PlaybookVersion"z\xdaA\x17parent,playbook_version\x82\xd3\xe4\x93\x02Z"F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions:\x10playbook_version\x12\xdf\x01\n\x12GetPlaybookVersion\x12=.google.cloud.dialogflow.cx.v3beta1.GetPlaybookVersionRequest\x1a3.google.cloud.dialogflow.cx.v3beta1.PlaybookVersion"U\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}\x12\xf2\x01\n\x14ListPlaybookVersions\x12?.google.cloud.dialogflow.cx.v3beta1.ListPlaybookVersionsRequest\x1a@.google.cloud.dialogflow.cx.v3beta1.ListPlaybookVersionsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions\x12\xc8\x01\n\x15DeletePlaybookVersion\x12@.google.cloud.dialogflow.cx.v3beta1.DeletePlaybookVersionRequest\x1a\x16.google.protobuf.Empty"U\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9b\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\rPlaybookProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.playbook_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\rPlaybookProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1'
    _globals['_CREATEPLAYBOOKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPLAYBOOKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Playbook'
    _globals['_CREATEPLAYBOOKREQUEST'].fields_by_name['playbook']._loaded_options = None
    _globals['_CREATEPLAYBOOKREQUEST'].fields_by_name['playbook']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEPLAYBOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPLAYBOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook'
    _globals['_LISTPLAYBOOKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPLAYBOOKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA$\x12"dialogflow.googleapis.com/Playbook'
    _globals['_GETPLAYBOOKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPLAYBOOKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"dialogflow.googleapis.com/Playbook'
    _globals['_UPDATEPLAYBOOKREQUEST'].fields_by_name['playbook']._loaded_options = None
    _globals['_UPDATEPLAYBOOKREQUEST'].fields_by_name['playbook']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYBOOK'].fields_by_name['display_name']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYBOOK'].fields_by_name['goal']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['goal']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYBOOK'].fields_by_name['input_parameter_definitions']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['input_parameter_definitions']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOK'].fields_by_name['output_parameter_definitions']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['output_parameter_definitions']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOK'].fields_by_name['token_count']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['token_count']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOK'].fields_by_name['create_time']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOK'].fields_by_name['update_time']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOK'].fields_by_name['referenced_playbooks']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['referenced_playbooks']._serialized_options = b'\xe0A\x03\xfaA$\n"dialogflow.googleapis.com/Playbook'
    _globals['_PLAYBOOK'].fields_by_name['referenced_flows']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['referenced_flows']._serialized_options = b'\xe0A\x03\xfaA \n\x1edialogflow.googleapis.com/Flow'
    _globals['_PLAYBOOK'].fields_by_name['referenced_tools']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['referenced_tools']._serialized_options = b'\xe0A\x01\xfaA \n\x1edialogflow.googleapis.com/Tool'
    _globals['_PLAYBOOK'].fields_by_name['llm_model_settings']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['llm_model_settings']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOK'].fields_by_name['speech_settings']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['speech_settings']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOK'].fields_by_name['handlers']._loaded_options = None
    _globals['_PLAYBOOK'].fields_by_name['handlers']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOK']._loaded_options = None
    _globals['_PLAYBOOK']._serialized_options = b'\xeaAq\n"dialogflow.googleapis.com/Playbook\x12Kprojects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}'
    _globals['_CREATEPLAYBOOKVERSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPLAYBOOKVERSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)dialogflow.googleapis.com/PlaybookVersion'
    _globals['_CREATEPLAYBOOKVERSIONREQUEST'].fields_by_name['playbook_version']._loaded_options = None
    _globals['_CREATEPLAYBOOKVERSIONREQUEST'].fields_by_name['playbook_version']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYBOOKVERSION'].fields_by_name['description']._loaded_options = None
    _globals['_PLAYBOOKVERSION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_PLAYBOOKVERSION'].fields_by_name['playbook']._loaded_options = None
    _globals['_PLAYBOOKVERSION'].fields_by_name['playbook']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOKVERSION'].fields_by_name['examples']._loaded_options = None
    _globals['_PLAYBOOKVERSION'].fields_by_name['examples']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOKVERSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_PLAYBOOKVERSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PLAYBOOKVERSION']._loaded_options = None
    _globals['_PLAYBOOKVERSION']._serialized_options = b'\xeaA\xae\x01\n)dialogflow.googleapis.com/PlaybookVersion\x12^projects/{project}/locations/{location}/agents/{agent}/playbooks/{playbook}/versions/{version}*\x10playbookVersions2\x0fplaybookVersion'
    _globals['_GETPLAYBOOKVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPLAYBOOKVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)dialogflow.googleapis.com/PlaybookVersion'
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)dialogflow.googleapis.com/PlaybookVersion'
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPLAYBOOKVERSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPLAYBOOKVERSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPLAYBOOKVERSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)dialogflow.googleapis.com/PlaybookVersion'
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['event']._loaded_options = None
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['condition']._loaded_options = None
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['fulfillment']._loaded_options = None
    _globals['_HANDLER_EVENTHANDLER'].fields_by_name['fulfillment']._serialized_options = b'\xe0A\x02'
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['lifecycle_stage']._loaded_options = None
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['lifecycle_stage']._serialized_options = b'\xe0A\x02'
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['condition']._loaded_options = None
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['fulfillment']._loaded_options = None
    _globals['_HANDLER_LIFECYCLEHANDLER'].fields_by_name['fulfillment']._serialized_options = b'\xe0A\x02'
    _globals['_PLAYBOOKS']._loaded_options = None
    _globals['_PLAYBOOKS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_PLAYBOOKS'].methods_by_name['CreatePlaybook']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['CreatePlaybook']._serialized_options = b'\xdaA\x0fparent,playbook\x82\xd3\xe4\x93\x02G";/v3beta1/{parent=projects/*/locations/*/agents/*}/playbooks:\x08playbook'
    _globals['_PLAYBOOKS'].methods_by_name['DeletePlaybook']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['DeletePlaybook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*}'
    _globals['_PLAYBOOKS'].methods_by_name['ListPlaybooks']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['ListPlaybooks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{parent=projects/*/locations/*/agents/*}/playbooks'
    _globals['_PLAYBOOKS'].methods_by_name['GetPlaybook']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['GetPlaybook']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*}'
    _globals['_PLAYBOOKS'].methods_by_name['UpdatePlaybook']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['UpdatePlaybook']._serialized_options = b'\xdaA\x14playbook,update_mask\x82\xd3\xe4\x93\x02P2D/v3beta1/{playbook.name=projects/*/locations/*/agents/*/playbooks/*}:\x08playbook'
    _globals['_PLAYBOOKS'].methods_by_name['CreatePlaybookVersion']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['CreatePlaybookVersion']._serialized_options = b'\xdaA\x17parent,playbook_version\x82\xd3\xe4\x93\x02Z"F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions:\x10playbook_version'
    _globals['_PLAYBOOKS'].methods_by_name['GetPlaybookVersion']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['GetPlaybookVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}'
    _globals['_PLAYBOOKS'].methods_by_name['ListPlaybookVersions']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['ListPlaybookVersions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v3beta1/{parent=projects/*/locations/*/agents/*/playbooks/*}/versions'
    _globals['_PLAYBOOKS'].methods_by_name['DeletePlaybookVersion']._loaded_options = None
    _globals['_PLAYBOOKS'].methods_by_name['DeletePlaybookVersion']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v3beta1/{name=projects/*/locations/*/agents/*/playbooks/*/versions/*}'
    _globals['_CREATEPLAYBOOKREQUEST']._serialized_start = 590
    _globals['_CREATEPLAYBOOKREQUEST']._serialized_end = 742
    _globals['_DELETEPLAYBOOKREQUEST']._serialized_start = 744
    _globals['_DELETEPLAYBOOKREQUEST']._serialized_end = 825
    _globals['_LISTPLAYBOOKSREQUEST']._serialized_start = 827
    _globals['_LISTPLAYBOOKSREQUEST']._serialized_end = 948
    _globals['_LISTPLAYBOOKSRESPONSE']._serialized_start = 950
    _globals['_LISTPLAYBOOKSRESPONSE']._serialized_end = 1063
    _globals['_GETPLAYBOOKREQUEST']._serialized_start = 1065
    _globals['_GETPLAYBOOKREQUEST']._serialized_end = 1143
    _globals['_UPDATEPLAYBOOKREQUEST']._serialized_start = 1146
    _globals['_UPDATEPLAYBOOKREQUEST']._serialized_end = 1287
    _globals['_PLAYBOOK']._serialized_start = 1290
    _globals['_PLAYBOOK']._serialized_end = 2556
    _globals['_PLAYBOOK_STEP']._serialized_start = 2234
    _globals['_PLAYBOOK_STEP']._serialized_end = 2337
    _globals['_PLAYBOOK_INSTRUCTION']._serialized_start = 2339
    _globals['_PLAYBOOK_INSTRUCTION']._serialized_end = 2438
    _globals['_CREATEPLAYBOOKVERSIONREQUEST']._serialized_start = 2559
    _globals['_CREATEPLAYBOOKVERSIONREQUEST']._serialized_end = 2740
    _globals['_PLAYBOOKVERSION']._serialized_start = 2743
    _globals['_PLAYBOOKVERSION']._serialized_end = 3172
    _globals['_GETPLAYBOOKVERSIONREQUEST']._serialized_start = 3174
    _globals['_GETPLAYBOOKVERSIONREQUEST']._serialized_end = 3266
    _globals['_LISTPLAYBOOKVERSIONSREQUEST']._serialized_start = 3269
    _globals['_LISTPLAYBOOKVERSIONSREQUEST']._serialized_end = 3414
    _globals['_LISTPLAYBOOKVERSIONSRESPONSE']._serialized_start = 3417
    _globals['_LISTPLAYBOOKVERSIONSRESPONSE']._serialized_end = 3552
    _globals['_DELETEPLAYBOOKVERSIONREQUEST']._serialized_start = 3554
    _globals['_DELETEPLAYBOOKVERSIONREQUEST']._serialized_end = 3649
    _globals['_HANDLER']._serialized_start = 3652
    _globals['_HANDLER']._serialized_end = 4132
    _globals['_HANDLER_EVENTHANDLER']._serialized_start = 3838
    _globals['_HANDLER_EVENTHANDLER']._serialized_end = 3971
    _globals['_HANDLER_LIFECYCLEHANDLER']._serialized_start = 3974
    _globals['_HANDLER_LIFECYCLEHANDLER']._serialized_end = 4121
    _globals['_PLAYBOOKS']._serialized_start = 4135
    _globals['_PLAYBOOKS']._serialized_end = 6252