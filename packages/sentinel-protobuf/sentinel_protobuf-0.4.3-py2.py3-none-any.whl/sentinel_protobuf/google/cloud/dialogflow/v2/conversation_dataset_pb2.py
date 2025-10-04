"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/v2/conversation_dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dialogflow.v2 import gcs_pb2 as google_dot_cloud_dot_dialogflow_dot_v2_dot_gcs__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/dialogflow/v2/conversation_dataset.proto\x12\x1agoogle.cloud.dialogflow.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/dialogflow/v2/gcs.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto".\n\x10ConversationInfo\x12\x1a\n\rlanguage_code\x18\x01 \x01(\tB\x03\xe0A\x01"U\n\x0bInputConfig\x12<\n\ngcs_source\x18\x01 \x01(\x0b2&.google.cloud.dialogflow.v2.GcsSourcesH\x00B\x08\n\x06source"\xb7\x04\n\x13ConversationDataset\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12B\n\x0cinput_config\x18\x05 \x01(\x0b2\'.google.cloud.dialogflow.v2.InputConfigB\x03\xe0A\x03\x12L\n\x11conversation_info\x18\x06 \x01(\x0b2,.google.cloud.dialogflow.v2.ConversationInfoB\x03\xe0A\x03\x12\x1f\n\x12conversation_count\x18\x07 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\rsatisfies_pzi\x18\x08 \x01(\x08B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1f\n\rsatisfies_pzs\x18\t \x01(\x08B\x03\xe0A\x03H\x01\x88\x01\x01:\x88\x01\xeaA\x84\x01\n-dialogflow.googleapis.com/ConversationDataset\x12Sprojects/{project}/locations/{location}/conversationDatasets/{conversation_dataset}B\x10\n\x0e_satisfies_pziB\x10\n\x0e_satisfies_pzs"\x8b\x01\n CreateConversationDatasetRequest\x12\x13\n\x06parent\x18\x01 \x01(\tB\x03\xe0A\x02\x12R\n\x14conversation_dataset\x18\x02 \x01(\x0b2/.google.cloud.dialogflow.v2.ConversationDatasetB\x03\xe0A\x02"d\n\x1dGetConversationDatasetRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset"\x99\x01\n\x1fListConversationDatasetsRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationDataset\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x8b\x01\n ListConversationDatasetsResponse\x12N\n\x15conversation_datasets\x18\x01 \x03(\x0b2/.google.cloud.dialogflow.v2.ConversationDataset\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"g\n DeleteConversationDatasetRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset"\xa8\x01\n\x1dImportConversationDataRequest\x12C\n\x04name\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset\x12B\n\x0cinput_config\x18\x02 \x01(\x0b2\'.google.cloud.dialogflow.v2.InputConfigB\x03\xe0A\x02"\xda\x01\n\'ImportConversationDataOperationMetadata\x12P\n\x14conversation_dataset\x18\x01 \x01(\tB2\xfaA/\n-dialogflow.googleapis.com/ConversationDataset\x12,\n\x10partial_failures\x18\x02 \x03(\x0b2\x12.google.rpc.Status\x12/\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.Timestamp"\x91\x01\n\'ImportConversationDataOperationResponse\x12P\n\x14conversation_dataset\x18\x01 \x01(\tB2\xfaA/\n-dialogflow.googleapis.com/ConversationDataset\x12\x14\n\x0cimport_count\x18\x03 \x01(\x05"~\n*CreateConversationDatasetOperationMetadata\x12P\n\x14conversation_dataset\x18\x01 \x01(\tB2\xfaA/\n-dialogflow.googleapis.com/ConversationDataset",\n*DeleteConversationDatasetOperationMetadata2\xd6\x0c\n\x14ConversationDatasets\x12\xb3\x02\n\x19CreateConversationDataset\x12<.google.cloud.dialogflow.v2.CreateConversationDatasetRequest\x1a\x1d.google.longrunning.Operation"\xb8\x01\xcaAA\n\x13ConversationDataset\x12*CreateConversationDatasetOperationMetadata\xdaA\x1bparent,conversation_dataset\x82\xd3\xe4\x93\x02P"8/v2/{parent=projects/*/locations/*}/conversationDatasets:\x14conversation_dataset\x12\xfd\x01\n\x16GetConversationDataset\x129.google.cloud.dialogflow.v2.GetConversationDatasetRequest\x1a/.google.cloud.dialogflow.v2.ConversationDataset"w\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2/{name=projects/*/conversationDatasets/*}Z:\x128/v2/{name=projects/*/locations/*/conversationDatasets/*}\x12\x90\x02\n\x18ListConversationDatasets\x12;.google.cloud.dialogflow.v2.ListConversationDatasetsRequest\x1a<.google.cloud.dialogflow.v2.ListConversationDatasetsResponse"y\xdaA\x06parent\x82\xd3\xe4\x93\x02j\x12,/v2/{parent=projects/*}/conversationDatasetsZ:\x128/v2/{parent=projects/*/locations/*}/conversationDatasets\x12\x88\x02\n\x19DeleteConversationDataset\x12<.google.cloud.dialogflow.v2.DeleteConversationDatasetRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaAC\n\x15google.protobuf.Empty\x12*DeleteConversationDatasetOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v2/{name=projects/*/locations/*/conversationDatasets/*}\x12\xef\x02\n\x16ImportConversationData\x129.google.cloud.dialogflow.v2.ImportConversationDataRequest\x1a\x1d.google.longrunning.Operation"\xfa\x01\xcaAR\n\'ImportConversationDataOperationResponse\x12\'ImportConversationDataOperationMetadata\x82\xd3\xe4\x93\x02\x9e\x01"C/v2/{name=projects/*/conversationDatasets/*}:importConversationData:\x01*ZT"O/v2/{name=projects/*/locations/*/conversationDatasets/*}:importConversationData:\x01*\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\x9e\x01\n\x1ecom.google.cloud.dialogflow.v2B\x18ConversationDatasetProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.v2.conversation_dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.dialogflow.v2B\x18ConversationDatasetProtoP\x01Z>cloud.google.com/go/dialogflow/apiv2/dialogflowpb;dialogflowpb\xa2\x02\x02DF\xaa\x02\x1aGoogle.Cloud.Dialogflow.V2'
    _globals['_CONVERSATIONINFO'].fields_by_name['language_code']._loaded_options = None
    _globals['_CONVERSATIONINFO'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONDATASET'].fields_by_name['name']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['display_name']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATIONDATASET'].fields_by_name['description']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONDATASET'].fields_by_name['create_time']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['input_config']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['input_config']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['conversation_info']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['conversation_info']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['conversation_count']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['conversation_count']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_CONVERSATIONDATASET'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_CONVERSATIONDATASET']._loaded_options = None
    _globals['_CONVERSATIONDATASET']._serialized_options = b'\xeaA\x84\x01\n-dialogflow.googleapis.com/ConversationDataset\x12Sprojects/{project}/locations/{location}/conversationDatasets/{conversation_dataset}'
    _globals['_CREATECONVERSATIONDATASETREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECONVERSATIONDATASETREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_CREATECONVERSATIONDATASETREQUEST'].fields_by_name['conversation_dataset']._loaded_options = None
    _globals['_CREATECONVERSATIONDATASETREQUEST'].fields_by_name['conversation_dataset']._serialized_options = b'\xe0A\x02'
    _globals['_GETCONVERSATIONDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCONVERSATIONDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\x12-dialogflow.googleapis.com/ConversationDataset'
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTCONVERSATIONDATASETSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETECONVERSATIONDATASETREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECONVERSATIONDATASETREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_IMPORTCONVERSATIONDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTCONVERSATIONDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_IMPORTCONVERSATIONDATAREQUEST'].fields_by_name['input_config']._loaded_options = None
    _globals['_IMPORTCONVERSATIONDATAREQUEST'].fields_by_name['input_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTCONVERSATIONDATAOPERATIONMETADATA'].fields_by_name['conversation_dataset']._loaded_options = None
    _globals['_IMPORTCONVERSATIONDATAOPERATIONMETADATA'].fields_by_name['conversation_dataset']._serialized_options = b'\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_IMPORTCONVERSATIONDATAOPERATIONRESPONSE'].fields_by_name['conversation_dataset']._loaded_options = None
    _globals['_IMPORTCONVERSATIONDATAOPERATIONRESPONSE'].fields_by_name['conversation_dataset']._serialized_options = b'\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_CREATECONVERSATIONDATASETOPERATIONMETADATA'].fields_by_name['conversation_dataset']._loaded_options = None
    _globals['_CREATECONVERSATIONDATASETOPERATIONMETADATA'].fields_by_name['conversation_dataset']._serialized_options = b'\xfaA/\n-dialogflow.googleapis.com/ConversationDataset'
    _globals['_CONVERSATIONDATASETS']._loaded_options = None
    _globals['_CONVERSATIONDATASETS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_CONVERSATIONDATASETS'].methods_by_name['CreateConversationDataset']._loaded_options = None
    _globals['_CONVERSATIONDATASETS'].methods_by_name['CreateConversationDataset']._serialized_options = b'\xcaAA\n\x13ConversationDataset\x12*CreateConversationDatasetOperationMetadata\xdaA\x1bparent,conversation_dataset\x82\xd3\xe4\x93\x02P"8/v2/{parent=projects/*/locations/*}/conversationDatasets:\x14conversation_dataset'
    _globals['_CONVERSATIONDATASETS'].methods_by_name['GetConversationDataset']._loaded_options = None
    _globals['_CONVERSATIONDATASETS'].methods_by_name['GetConversationDataset']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02j\x12,/v2/{name=projects/*/conversationDatasets/*}Z:\x128/v2/{name=projects/*/locations/*/conversationDatasets/*}'
    _globals['_CONVERSATIONDATASETS'].methods_by_name['ListConversationDatasets']._loaded_options = None
    _globals['_CONVERSATIONDATASETS'].methods_by_name['ListConversationDatasets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02j\x12,/v2/{parent=projects/*}/conversationDatasetsZ:\x128/v2/{parent=projects/*/locations/*}/conversationDatasets'
    _globals['_CONVERSATIONDATASETS'].methods_by_name['DeleteConversationDataset']._loaded_options = None
    _globals['_CONVERSATIONDATASETS'].methods_by_name['DeleteConversationDataset']._serialized_options = b'\xcaAC\n\x15google.protobuf.Empty\x12*DeleteConversationDatasetOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02:*8/v2/{name=projects/*/locations/*/conversationDatasets/*}'
    _globals['_CONVERSATIONDATASETS'].methods_by_name['ImportConversationData']._loaded_options = None
    _globals['_CONVERSATIONDATASETS'].methods_by_name['ImportConversationData']._serialized_options = b'\xcaAR\n\'ImportConversationDataOperationResponse\x12\'ImportConversationDataOperationMetadata\x82\xd3\xe4\x93\x02\x9e\x01"C/v2/{name=projects/*/conversationDatasets/*}:importConversationData:\x01*ZT"O/v2/{name=projects/*/locations/*/conversationDatasets/*}:importConversationData:\x01*'
    _globals['_CONVERSATIONINFO']._serialized_start = 362
    _globals['_CONVERSATIONINFO']._serialized_end = 408
    _globals['_INPUTCONFIG']._serialized_start = 410
    _globals['_INPUTCONFIG']._serialized_end = 495
    _globals['_CONVERSATIONDATASET']._serialized_start = 498
    _globals['_CONVERSATIONDATASET']._serialized_end = 1065
    _globals['_CREATECONVERSATIONDATASETREQUEST']._serialized_start = 1068
    _globals['_CREATECONVERSATIONDATASETREQUEST']._serialized_end = 1207
    _globals['_GETCONVERSATIONDATASETREQUEST']._serialized_start = 1209
    _globals['_GETCONVERSATIONDATASETREQUEST']._serialized_end = 1309
    _globals['_LISTCONVERSATIONDATASETSREQUEST']._serialized_start = 1312
    _globals['_LISTCONVERSATIONDATASETSREQUEST']._serialized_end = 1465
    _globals['_LISTCONVERSATIONDATASETSRESPONSE']._serialized_start = 1468
    _globals['_LISTCONVERSATIONDATASETSRESPONSE']._serialized_end = 1607
    _globals['_DELETECONVERSATIONDATASETREQUEST']._serialized_start = 1609
    _globals['_DELETECONVERSATIONDATASETREQUEST']._serialized_end = 1712
    _globals['_IMPORTCONVERSATIONDATAREQUEST']._serialized_start = 1715
    _globals['_IMPORTCONVERSATIONDATAREQUEST']._serialized_end = 1883
    _globals['_IMPORTCONVERSATIONDATAOPERATIONMETADATA']._serialized_start = 1886
    _globals['_IMPORTCONVERSATIONDATAOPERATIONMETADATA']._serialized_end = 2104
    _globals['_IMPORTCONVERSATIONDATAOPERATIONRESPONSE']._serialized_start = 2107
    _globals['_IMPORTCONVERSATIONDATAOPERATIONRESPONSE']._serialized_end = 2252
    _globals['_CREATECONVERSATIONDATASETOPERATIONMETADATA']._serialized_start = 2254
    _globals['_CREATECONVERSATIONDATASETOPERATIONMETADATA']._serialized_end = 2380
    _globals['_DELETECONVERSATIONDATASETOPERATIONMETADATA']._serialized_start = 2382
    _globals['_DELETECONVERSATIONDATASETOPERATIONMETADATA']._serialized_end = 2426
    _globals['_CONVERSATIONDATASETS']._serialized_start = 2429
    _globals['_CONVERSATIONDATASETS']._serialized_end = 4051