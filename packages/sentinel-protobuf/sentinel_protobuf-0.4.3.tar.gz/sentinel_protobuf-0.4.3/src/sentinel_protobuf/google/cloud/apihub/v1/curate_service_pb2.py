"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/apihub/v1/curate_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/apihub/v1/curate_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa2\x01\n\x15CreateCurationRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1eapihub.googleapis.com/Curation\x12\x18\n\x0bcuration_id\x18\x02 \x01(\tB\x03\xe0A\x01\x127\n\x08curation\x18\x03 \x01(\x0b2 .google.cloud.apihub.v1.CurationB\x03\xe0A\x02"J\n\x12GetCurationRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1eapihub.googleapis.com/Curation"\x86\x01\n\x15UpdateCurationRequest\x127\n\x08curation\x18\x01 \x01(\x0b2 .google.cloud.apihub.v1.CurationB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"M\n\x15DeleteCurationRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1eapihub.googleapis.com/Curation"\x94\x01\n\x14ListCurationsRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1eapihub.googleapis.com/Curation\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"e\n\x15ListCurationsResponse\x123\n\tcurations\x18\x01 \x03(\x0b2 .google.cloud.apihub.v1.Curation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xc4\x07\n\x08Curation\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x127\n\x08endpoint\x18\x04 \x01(\x0b2 .google.cloud.apihub.v1.EndpointB\x03\xe0A\x02\x12]\n\x17plugin_instance_actions\x18\x05 \x03(\x0b27.google.cloud.apihub.v1.Curation.PluginInstanceActionIDB\x03\xe0A\x03\x12V\n\x14last_execution_state\x18\x06 \x01(\x0e23.google.cloud.apihub.v1.Curation.LastExecutionStateB\x03\xe0A\x03\x12R\n\x19last_execution_error_code\x18\x07 \x01(\x0e2*.google.cloud.apihub.v1.Curation.ErrorCodeB\x03\xe0A\x03\x12)\n\x1clast_execution_error_message\x18\x08 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1aw\n\x16PluginInstanceActionID\x12E\n\x0fplugin_instance\x18\x01 \x01(\tB,\xe0A\x03\xfaA&\n$apihub.googleapis.com/PluginInstance\x12\x16\n\taction_id\x18\x02 \x01(\tB\x03\xe0A\x03"U\n\x12LastExecutionState\x12$\n LAST_EXECUTION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02"M\n\tErrorCode\x12\x1a\n\x16ERROR_CODE_UNSPECIFIED\x10\x00\x12\x12\n\x0eINTERNAL_ERROR\x10\x01\x12\x10\n\x0cUNAUTHORIZED\x10\x02:v\xeaAs\n\x1eapihub.googleapis.com/Curation\x12<projects/{project}/locations/{location}/curations/{curation}*\tcurations2\x08curation"\x96\x01\n\x08Endpoint\x12v\n(application_integration_endpoint_details\x18\x01 \x01(\x0b2=.google.cloud.apihub.v1.ApplicationIntegrationEndpointDetailsB\x03\xe0A\x02H\x00B\x12\n\x10endpoint_details"R\n%ApplicationIntegrationEndpointDetails\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ntrigger_id\x18\x02 \x01(\tB\x03\xe0A\x022\xc4\x07\n\x0cApiHubCurate\x12\xc0\x01\n\x0eCreateCuration\x12-.google.cloud.apihub.v1.CreateCurationRequest\x1a .google.cloud.apihub.v1.Curation"]\xdaA\x1bparent,curation,curation_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/curations:\x08curation\x12\x99\x01\n\x0bGetCuration\x12*.google.cloud.apihub.v1.GetCurationRequest\x1a .google.cloud.apihub.v1.Curation"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/curations/*}\x12\xac\x01\n\rListCurations\x12,.google.cloud.apihub.v1.ListCurationsRequest\x1a-.google.cloud.apihub.v1.ListCurationsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/curations\x12\xc2\x01\n\x0eUpdateCuration\x12-.google.cloud.apihub.v1.UpdateCurationRequest\x1a .google.cloud.apihub.v1.Curation"_\xdaA\x14curation,update_mask\x82\xd3\xe4\x93\x02B26/v1/{curation.name=projects/*/locations/*/curations/*}:\x08curation\x12\x95\x01\n\x0eDeleteCuration\x12-.google.cloud.apihub.v1.DeleteCurationRequest\x1a\x16.google.protobuf.Empty"<\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/curations/*}\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xb4\x01\n\x1acom.google.cloud.apihub.v1B\x12CurateServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.curate_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x12CurateServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_CREATECURATIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECURATIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1eapihub.googleapis.com/Curation'
    _globals['_CREATECURATIONREQUEST'].fields_by_name['curation_id']._loaded_options = None
    _globals['_CREATECURATIONREQUEST'].fields_by_name['curation_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATECURATIONREQUEST'].fields_by_name['curation']._loaded_options = None
    _globals['_CREATECURATIONREQUEST'].fields_by_name['curation']._serialized_options = b'\xe0A\x02'
    _globals['_GETCURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1eapihub.googleapis.com/Curation'
    _globals['_UPDATECURATIONREQUEST'].fields_by_name['curation']._loaded_options = None
    _globals['_UPDATECURATIONREQUEST'].fields_by_name['curation']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATECURATIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATECURATIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECURATIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECURATIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1eapihub.googleapis.com/Curation'
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1eapihub.googleapis.com/Curation'
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCURATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CURATION_PLUGININSTANCEACTIONID'].fields_by_name['plugin_instance']._loaded_options = None
    _globals['_CURATION_PLUGININSTANCEACTIONID'].fields_by_name['plugin_instance']._serialized_options = b'\xe0A\x03\xfaA&\n$apihub.googleapis.com/PluginInstance'
    _globals['_CURATION_PLUGININSTANCEACTIONID'].fields_by_name['action_id']._loaded_options = None
    _globals['_CURATION_PLUGININSTANCEACTIONID'].fields_by_name['action_id']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['name']._loaded_options = None
    _globals['_CURATION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CURATION'].fields_by_name['display_name']._loaded_options = None
    _globals['_CURATION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CURATION'].fields_by_name['description']._loaded_options = None
    _globals['_CURATION'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CURATION'].fields_by_name['endpoint']._loaded_options = None
    _globals['_CURATION'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_CURATION'].fields_by_name['plugin_instance_actions']._loaded_options = None
    _globals['_CURATION'].fields_by_name['plugin_instance_actions']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['last_execution_state']._loaded_options = None
    _globals['_CURATION'].fields_by_name['last_execution_state']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['last_execution_error_code']._loaded_options = None
    _globals['_CURATION'].fields_by_name['last_execution_error_code']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['last_execution_error_message']._loaded_options = None
    _globals['_CURATION'].fields_by_name['last_execution_error_message']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['create_time']._loaded_options = None
    _globals['_CURATION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION'].fields_by_name['update_time']._loaded_options = None
    _globals['_CURATION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_CURATION']._loaded_options = None
    _globals['_CURATION']._serialized_options = b'\xeaAs\n\x1eapihub.googleapis.com/Curation\x12<projects/{project}/locations/{location}/curations/{curation}*\tcurations2\x08curation'
    _globals['_ENDPOINT'].fields_by_name['application_integration_endpoint_details']._loaded_options = None
    _globals['_ENDPOINT'].fields_by_name['application_integration_endpoint_details']._serialized_options = b'\xe0A\x02'
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS'].fields_by_name['uri']._loaded_options = None
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS'].fields_by_name['trigger_id']._loaded_options = None
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS'].fields_by_name['trigger_id']._serialized_options = b'\xe0A\x02'
    _globals['_APIHUBCURATE']._loaded_options = None
    _globals['_APIHUBCURATE']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_APIHUBCURATE'].methods_by_name['CreateCuration']._loaded_options = None
    _globals['_APIHUBCURATE'].methods_by_name['CreateCuration']._serialized_options = b'\xdaA\x1bparent,curation,curation_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/curations:\x08curation'
    _globals['_APIHUBCURATE'].methods_by_name['GetCuration']._loaded_options = None
    _globals['_APIHUBCURATE'].methods_by_name['GetCuration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/curations/*}'
    _globals['_APIHUBCURATE'].methods_by_name['ListCurations']._loaded_options = None
    _globals['_APIHUBCURATE'].methods_by_name['ListCurations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/curations'
    _globals['_APIHUBCURATE'].methods_by_name['UpdateCuration']._loaded_options = None
    _globals['_APIHUBCURATE'].methods_by_name['UpdateCuration']._serialized_options = b'\xdaA\x14curation,update_mask\x82\xd3\xe4\x93\x02B26/v1/{curation.name=projects/*/locations/*/curations/*}:\x08curation'
    _globals['_APIHUBCURATE'].methods_by_name['DeleteCuration']._loaded_options = None
    _globals['_APIHUBCURATE'].methods_by_name['DeleteCuration']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/curations/*}'
    _globals['_CREATECURATIONREQUEST']._serialized_start = 283
    _globals['_CREATECURATIONREQUEST']._serialized_end = 445
    _globals['_GETCURATIONREQUEST']._serialized_start = 447
    _globals['_GETCURATIONREQUEST']._serialized_end = 521
    _globals['_UPDATECURATIONREQUEST']._serialized_start = 524
    _globals['_UPDATECURATIONREQUEST']._serialized_end = 658
    _globals['_DELETECURATIONREQUEST']._serialized_start = 660
    _globals['_DELETECURATIONREQUEST']._serialized_end = 737
    _globals['_LISTCURATIONSREQUEST']._serialized_start = 740
    _globals['_LISTCURATIONSREQUEST']._serialized_end = 888
    _globals['_LISTCURATIONSRESPONSE']._serialized_start = 890
    _globals['_LISTCURATIONSRESPONSE']._serialized_end = 991
    _globals['_CURATION']._serialized_start = 994
    _globals['_CURATION']._serialized_end = 1958
    _globals['_CURATION_PLUGININSTANCEACTIONID']._serialized_start = 1553
    _globals['_CURATION_PLUGININSTANCEACTIONID']._serialized_end = 1672
    _globals['_CURATION_LASTEXECUTIONSTATE']._serialized_start = 1674
    _globals['_CURATION_LASTEXECUTIONSTATE']._serialized_end = 1759
    _globals['_CURATION_ERRORCODE']._serialized_start = 1761
    _globals['_CURATION_ERRORCODE']._serialized_end = 1838
    _globals['_ENDPOINT']._serialized_start = 1961
    _globals['_ENDPOINT']._serialized_end = 2111
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS']._serialized_start = 2113
    _globals['_APPLICATIONINTEGRATIONENDPOINTDETAILS']._serialized_end = 2195
    _globals['_APIHUBCURATE']._serialized_start = 2198
    _globals['_APIHUBCURATE']._serialized_end = 3162