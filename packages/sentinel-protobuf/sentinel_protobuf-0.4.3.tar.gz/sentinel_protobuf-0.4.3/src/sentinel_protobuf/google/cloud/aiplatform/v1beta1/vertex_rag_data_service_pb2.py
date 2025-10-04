"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/vertex_rag_data_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import vertex_rag_data_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_vertex__rag__data__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/aiplatform/v1beta1/vertex_rag_data_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a5google/cloud/aiplatform/v1beta1/vertex_rag_data.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto"\x98\x01\n\x16CreateRagCorpusRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\nrag_corpus\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.RagCorpusB\x03\xe0A\x02"P\n\x13GetRagCorpusRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus"\x83\x01\n\x15ListRagCorporaRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"r\n\x16ListRagCorporaResponse\x12?\n\x0brag_corpora\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1beta1.RagCorpus\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"g\n\x16DeleteRagCorpusRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12\x12\n\x05force\x18\x02 \x01(\x08B\x03\xe0A\x01"\xef\x01\n\x14UploadRagFileRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12?\n\x08rag_file\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.RagFileB\x03\xe0A\x02\x12Y\n\x16upload_rag_file_config\x18\x05 \x01(\x0b24.google.cloud.aiplatform.v1beta1.UploadRagFileConfigB\x03\xe0A\x02"\x84\x01\n\x15UploadRagFileResponse\x12<\n\x08rag_file\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.RagFileH\x00\x12#\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.StatusH\x00B\x08\n\x06result"\xb1\x01\n\x15ImportRagFilesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12[\n\x17import_rag_files_config\x18\x02 \x01(\x0b25.google.cloud.aiplatform.v1beta1.ImportRagFilesConfigB\x03\xe0A\x02"\xe3\x01\n\x16ImportRagFilesResponse\x12#\n\x19partial_failures_gcs_path\x18\x04 \x01(\tH\x00\x12)\n\x1fpartial_failures_bigquery_table\x18\x05 \x01(\tH\x00\x12 \n\x18imported_rag_files_count\x18\x01 \x01(\x03\x12\x1e\n\x16failed_rag_files_count\x18\x02 \x01(\x03\x12\x1f\n\x17skipped_rag_files_count\x18\x03 \x01(\x03B\x16\n\x14partial_failure_sink"L\n\x11GetRagFileRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile"\x83\x01\n\x13ListRagFilesRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"l\n\x14ListRagFilesResponse\x12;\n\trag_files\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.RagFile\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"j\n\x14DeleteRagFileRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile\x12\x19\n\x0cforce_delete\x18\x02 \x01(\x08B\x03\xe0A\x01"w\n CreateRagCorpusOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\\\n\x19GetRagEngineConfigRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/RagEngineConfig"]\n\x16UpdateRagCorpusRequest\x12C\n\nrag_corpus\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.RagCorpusB\x03\xe0A\x02"w\n UpdateRagCorpusOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x87\x02\n\x1fImportRagFilesOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x15\n\rrag_corpus_id\x18\x02 \x01(\x03\x12[\n\x17import_rag_files_config\x18\x03 \x01(\x0b25.google.cloud.aiplatform.v1beta1.ImportRagFilesConfigB\x03\xe0A\x03\x12\x1b\n\x13progress_percentage\x18\x04 \x01(\x05"p\n\x1cUpdateRagEngineConfigRequest\x12P\n\x11rag_engine_config\x18\x01 \x01(\x0b20.google.cloud.aiplatform.v1beta1.RagEngineConfigB\x03\xe0A\x02"}\n&UpdateRagEngineConfigOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata2\xc7\x16\n\x14VertexRagDataService\x12\xf7\x01\n\x0fCreateRagCorpus\x127.google.cloud.aiplatform.v1beta1.CreateRagCorpusRequest\x1a\x1d.google.longrunning.Operation"\x8b\x01\xcaA-\n\tRagCorpus\x12 CreateRagCorpusOperationMetadata\xdaA\x11parent,rag_corpus\x82\xd3\xe4\x93\x02A"3/v1beta1/{parent=projects/*/locations/*}/ragCorpora:\nrag_corpus\x12\xfb\x01\n\x0fUpdateRagCorpus\x127.google.cloud.aiplatform.v1beta1.UpdateRagCorpusRequest\x1a\x1d.google.longrunning.Operation"\x8f\x01\xcaA-\n\tRagCorpus\x12 UpdateRagCorpusOperationMetadata\xdaA\nrag_corpus\x82\xd3\xe4\x93\x02L2>/v1beta1/{rag_corpus.name=projects/*/locations/*/ragCorpora/*}:\nrag_corpus\x12\xb4\x01\n\x0cGetRagCorpus\x124.google.cloud.aiplatform.v1beta1.GetRagCorpusRequest\x1a*.google.cloud.aiplatform.v1beta1.RagCorpus"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/ragCorpora/*}\x12\xc7\x01\n\x0eListRagCorpora\x126.google.cloud.aiplatform.v1beta1.ListRagCorporaRequest\x1a7.google.cloud.aiplatform.v1beta1.ListRagCorporaResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/ragCorpora\x12\xe0\x01\n\x0fDeleteRagCorpus\x127.google.cloud.aiplatform.v1beta1.DeleteRagCorpusRequest\x1a\x1d.google.longrunning.Operation"u\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/ragCorpora/*}\x12\xf9\x01\n\rUploadRagFile\x125.google.cloud.aiplatform.v1beta1.UploadRagFileRequest\x1a6.google.cloud.aiplatform.v1beta1.UploadRagFileResponse"y\xdaA&parent,rag_file,upload_rag_file_config\x82\xd3\xe4\x93\x02J"E/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:upload:\x01*\x12\x97\x02\n\x0eImportRagFiles\x126.google.cloud.aiplatform.v1beta1.ImportRagFilesRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA9\n\x16ImportRagFilesResponse\x12\x1fImportRagFilesOperationMetadata\xdaA\x1eparent,import_rag_files_config\x82\xd3\xe4\x93\x02J"E/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:import:\x01*\x12\xb9\x01\n\nGetRagFile\x122.google.cloud.aiplatform.v1beta1.GetRagFileRequest\x1a(.google.cloud.aiplatform.v1beta1.RagFile"M\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}\x12\xcc\x01\n\x0cListRagFiles\x124.google.cloud.aiplatform.v1beta1.ListRagFilesRequest\x1a5.google.cloud.aiplatform.v1beta1.ListRagFilesResponse"O\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles\x12\xe8\x01\n\rDeleteRagFile\x125.google.cloud.aiplatform.v1beta1.DeleteRagFileRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}\x12\xab\x02\n\x15UpdateRagEngineConfig\x12=.google.cloud.aiplatform.v1beta1.UpdateRagEngineConfigRequest\x1a\x1d.google.longrunning.Operation"\xb3\x01\xcaA9\n\x0fRagEngineConfig\x12&UpdateRagEngineConfigOperationMetadata\xdaA\x11rag_engine_config\x82\xd3\xe4\x93\x02]2H/v1beta1/{rag_engine_config.name=projects/*/locations/*/ragEngineConfig}:\x11rag_engine_config\x12\xc9\x01\n\x12GetRagEngineConfig\x12:.google.cloud.aiplatform.v1beta1.GetRagEngineConfigRequest\x1a0.google.cloud.aiplatform.v1beta1.RagEngineConfig"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/ragEngineConfig}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf0\x01\n#com.google.cloud.aiplatform.v1beta1B\x19VertexRagDataServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.vertex_rag_data_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x19VertexRagDataServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._loaded_options = None
    _globals['_CREATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._serialized_options = b'\xe0A\x02'
    _globals['_GETRAGCORPUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRAGCORPUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRAGCORPORAREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['force']._loaded_options = None
    _globals['_DELETERAGCORPUSREQUEST'].fields_by_name['force']._serialized_options = b'\xe0A\x01'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['rag_file']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['rag_file']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['upload_rag_file_config']._loaded_options = None
    _globals['_UPLOADRAGFILEREQUEST'].fields_by_name['upload_rag_file_config']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['import_rag_files_config']._loaded_options = None
    _globals['_IMPORTRAGFILESREQUEST'].fields_by_name['import_rag_files_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETRAGFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRAGFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/RagCorpus'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRAGFILESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/RagFile'
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['force_delete']._loaded_options = None
    _globals['_DELETERAGFILEREQUEST'].fields_by_name['force_delete']._serialized_options = b'\xe0A\x01'
    _globals['_GETRAGENGINECONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRAGENGINECONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/RagEngineConfig'
    _globals['_UPDATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._loaded_options = None
    _globals['_UPDATERAGCORPUSREQUEST'].fields_by_name['rag_corpus']._serialized_options = b'\xe0A\x02'
    _globals['_IMPORTRAGFILESOPERATIONMETADATA'].fields_by_name['import_rag_files_config']._loaded_options = None
    _globals['_IMPORTRAGFILESOPERATIONMETADATA'].fields_by_name['import_rag_files_config']._serialized_options = b'\xe0A\x03'
    _globals['_UPDATERAGENGINECONFIGREQUEST'].fields_by_name['rag_engine_config']._loaded_options = None
    _globals['_UPDATERAGENGINECONFIGREQUEST'].fields_by_name['rag_engine_config']._serialized_options = b'\xe0A\x02'
    _globals['_VERTEXRAGDATASERVICE']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['CreateRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['CreateRagCorpus']._serialized_options = b'\xcaA-\n\tRagCorpus\x12 CreateRagCorpusOperationMetadata\xdaA\x11parent,rag_corpus\x82\xd3\xe4\x93\x02A"3/v1beta1/{parent=projects/*/locations/*}/ragCorpora:\nrag_corpus'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagCorpus']._serialized_options = b'\xcaA-\n\tRagCorpus\x12 UpdateRagCorpusOperationMetadata\xdaA\nrag_corpus\x82\xd3\xe4\x93\x02L2>/v1beta1/{rag_corpus.name=projects/*/locations/*/ragCorpora/*}:\nrag_corpus'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagCorpus']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/ragCorpora/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagCorpora']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagCorpora']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/ragCorpora'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagCorpus']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagCorpus']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/ragCorpora/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UploadRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UploadRagFile']._serialized_options = b'\xdaA&parent,rag_file,upload_rag_file_config\x82\xd3\xe4\x93\x02J"E/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:upload:\x01*'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ImportRagFiles']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ImportRagFiles']._serialized_options = b'\xcaA9\n\x16ImportRagFilesResponse\x12\x1fImportRagFilesOperationMetadata\xdaA\x1eparent,import_rag_files_config\x82\xd3\xe4\x93\x02J"E/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles:import:\x01*'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagFile']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagFiles']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['ListRagFiles']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02@\x12>/v1beta1/{parent=projects/*/locations/*/ragCorpora/*}/ragFiles'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagFile']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['DeleteRagFile']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02@*>/v1beta1/{name=projects/*/locations/*/ragCorpora/*/ragFiles/*}'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagEngineConfig']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['UpdateRagEngineConfig']._serialized_options = b'\xcaA9\n\x0fRagEngineConfig\x12&UpdateRagEngineConfigOperationMetadata\xdaA\x11rag_engine_config\x82\xd3\xe4\x93\x02]2H/v1beta1/{rag_engine_config.name=projects/*/locations/*/ragEngineConfig}:\x11rag_engine_config'
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagEngineConfig']._loaded_options = None
    _globals['_VERTEXRAGDATASERVICE'].methods_by_name['GetRagEngineConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/ragEngineConfig}'
    _globals['_CREATERAGCORPUSREQUEST']._serialized_start = 409
    _globals['_CREATERAGCORPUSREQUEST']._serialized_end = 561
    _globals['_GETRAGCORPUSREQUEST']._serialized_start = 563
    _globals['_GETRAGCORPUSREQUEST']._serialized_end = 643
    _globals['_LISTRAGCORPORAREQUEST']._serialized_start = 646
    _globals['_LISTRAGCORPORAREQUEST']._serialized_end = 777
    _globals['_LISTRAGCORPORARESPONSE']._serialized_start = 779
    _globals['_LISTRAGCORPORARESPONSE']._serialized_end = 893
    _globals['_DELETERAGCORPUSREQUEST']._serialized_start = 895
    _globals['_DELETERAGCORPUSREQUEST']._serialized_end = 998
    _globals['_UPLOADRAGFILEREQUEST']._serialized_start = 1001
    _globals['_UPLOADRAGFILEREQUEST']._serialized_end = 1240
    _globals['_UPLOADRAGFILERESPONSE']._serialized_start = 1243
    _globals['_UPLOADRAGFILERESPONSE']._serialized_end = 1375
    _globals['_IMPORTRAGFILESREQUEST']._serialized_start = 1378
    _globals['_IMPORTRAGFILESREQUEST']._serialized_end = 1555
    _globals['_IMPORTRAGFILESRESPONSE']._serialized_start = 1558
    _globals['_IMPORTRAGFILESRESPONSE']._serialized_end = 1785
    _globals['_GETRAGFILEREQUEST']._serialized_start = 1787
    _globals['_GETRAGFILEREQUEST']._serialized_end = 1863
    _globals['_LISTRAGFILESREQUEST']._serialized_start = 1866
    _globals['_LISTRAGFILESREQUEST']._serialized_end = 1997
    _globals['_LISTRAGFILESRESPONSE']._serialized_start = 1999
    _globals['_LISTRAGFILESRESPONSE']._serialized_end = 2107
    _globals['_DELETERAGFILEREQUEST']._serialized_start = 2109
    _globals['_DELETERAGFILEREQUEST']._serialized_end = 2215
    _globals['_CREATERAGCORPUSOPERATIONMETADATA']._serialized_start = 2217
    _globals['_CREATERAGCORPUSOPERATIONMETADATA']._serialized_end = 2336
    _globals['_GETRAGENGINECONFIGREQUEST']._serialized_start = 2338
    _globals['_GETRAGENGINECONFIGREQUEST']._serialized_end = 2430
    _globals['_UPDATERAGCORPUSREQUEST']._serialized_start = 2432
    _globals['_UPDATERAGCORPUSREQUEST']._serialized_end = 2525
    _globals['_UPDATERAGCORPUSOPERATIONMETADATA']._serialized_start = 2527
    _globals['_UPDATERAGCORPUSOPERATIONMETADATA']._serialized_end = 2646
    _globals['_IMPORTRAGFILESOPERATIONMETADATA']._serialized_start = 2649
    _globals['_IMPORTRAGFILESOPERATIONMETADATA']._serialized_end = 2912
    _globals['_UPDATERAGENGINECONFIGREQUEST']._serialized_start = 2914
    _globals['_UPDATERAGENGINECONFIGREQUEST']._serialized_end = 3026
    _globals['_UPDATERAGENGINECONFIGOPERATIONMETADATA']._serialized_start = 3028
    _globals['_UPDATERAGENGINECONFIGOPERATIONMETADATA']._serialized_end = 3153
    _globals['_VERTEXRAGDATASERVICE']._serialized_start = 3156
    _globals['_VERTEXRAGDATASERVICE']._serialized_end = 6043