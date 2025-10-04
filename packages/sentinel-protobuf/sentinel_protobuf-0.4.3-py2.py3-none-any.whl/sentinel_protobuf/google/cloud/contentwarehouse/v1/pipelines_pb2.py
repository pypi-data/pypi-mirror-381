"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/pipelines.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import common_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_common__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/contentwarehouse/v1/pipelines.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/contentwarehouse/v1/common.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x17google/rpc/status.proto"\x15\n\x13RunPipelineResponse"\xfa\x07\n\x13RunPipelineMetadata\x12\x18\n\x10total_file_count\x18\x01 \x01(\x05\x12\x19\n\x11failed_file_count\x18\x02 \x01(\x05\x12=\n\tuser_info\x18\x03 \x01(\x0b2*.google.cloud.contentwarehouse.v1.UserInfo\x12w\n\x1cgcs_ingest_pipeline_metadata\x18\x04 \x01(\x0b2O.google.cloud.contentwarehouse.v1.RunPipelineMetadata.GcsIngestPipelineMetadataH\x00\x12|\n\x1fexport_to_cdw_pipeline_metadata\x18\x06 \x01(\x0b2Q.google.cloud.contentwarehouse.v1.RunPipelineMetadata.ExportToCdwPipelineMetadataH\x00\x12\x87\x01\n%process_with_doc_ai_pipeline_metadata\x18\x07 \x01(\x0b2V.google.cloud.contentwarehouse.v1.RunPipelineMetadata.ProcessWithDocAiPipelineMetadataH\x00\x12t\n\x1cindividual_document_statuses\x18\x05 \x03(\x0b2N.google.cloud.contentwarehouse.v1.RunPipelineMetadata.IndividualDocumentStatus\x1a/\n\x19GcsIngestPipelineMetadata\x12\x12\n\ninput_path\x18\x01 \x01(\t\x1a]\n\x1bExportToCdwPipelineMetadata\x12\x11\n\tdocuments\x18\x01 \x03(\t\x12\x16\n\x0edoc_ai_dataset\x18\x02 \x01(\t\x12\x13\n\x0boutput_path\x18\x03 \x01(\t\x1a~\n ProcessWithDocAiPipelineMetadata\x12\x11\n\tdocuments\x18\x01 \x03(\t\x12G\n\x0eprocessor_info\x18\x02 \x01(\x0b2/.google.cloud.contentwarehouse.v1.ProcessorInfo\x1aS\n\x18IndividualDocumentStatus\x12\x13\n\x0bdocument_id\x18\x01 \x01(\t\x12"\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.StatusB\x13\n\x11pipeline_metadata"S\n\rProcessorInfo\x12\x16\n\x0eprocessor_name\x18\x01 \x01(\t\x12\x15\n\rdocument_type\x18\x02 \x01(\t\x12\x13\n\x0bschema_name\x18\x03 \x01(\t"\xd2\x01\n\x14IngestPipelineConfig\x122\n\x13document_acl_policy\x18\x01 \x01(\x0b2\x15.google.iam.v1.Policy\x12\'\n\x1fenable_document_text_extraction\x18\x02 \x01(\x08\x12\x13\n\x06folder\x18\x03 \x01(\tB\x03\xe0A\x01\x12H\n\x0ecloud_function\x18\x04 \x01(\tB0\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction"\xcb\x01\n\x11GcsIngestPipeline\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12\x13\n\x0bschema_name\x18\x02 \x01(\t\x12\x16\n\x0eprocessor_type\x18\x03 \x01(\t\x12\x1f\n\x17skip_ingested_documents\x18\x04 \x01(\x08\x12T\n\x0fpipeline_config\x18\x05 \x01(\x0b26.google.cloud.contentwarehouse.v1.IngestPipelineConfigB\x03\xe0A\x01"\x82\x03\n$GcsIngestWithDocAiProcessorsPipeline\x12\x12\n\ninput_path\x18\x01 \x01(\t\x12V\n\x1dsplit_classify_processor_info\x18\x02 \x01(\x0b2/.google.cloud.contentwarehouse.v1.ProcessorInfo\x12P\n\x17extract_processor_infos\x18\x03 \x03(\x0b2/.google.cloud.contentwarehouse.v1.ProcessorInfo\x12%\n\x1dprocessor_results_folder_path\x18\x04 \x01(\t\x12\x1f\n\x17skip_ingested_documents\x18\x05 \x01(\x08\x12T\n\x0fpipeline_config\x18\x06 \x01(\x0b26.google.cloud.contentwarehouse.v1.IngestPipelineConfigB\x03\xe0A\x01"\x7f\n\x13ExportToCdwPipeline\x12\x11\n\tdocuments\x18\x01 \x03(\t\x12\x1a\n\x12export_folder_path\x18\x02 \x01(\t\x12\x1b\n\x0edoc_ai_dataset\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x1c\n\x14training_split_ratio\x18\x04 \x01(\x02"\xb9\x01\n\x18ProcessWithDocAiPipeline\x12\x11\n\tdocuments\x18\x01 \x03(\t\x12\x1a\n\x12export_folder_path\x18\x02 \x01(\t\x12G\n\x0eprocessor_info\x18\x03 \x01(\x0b2/.google.cloud.contentwarehouse.v1.ProcessorInfo\x12%\n\x1dprocessor_results_folder_path\x18\x04 \x01(\tB\xe4\x02\n$com.google.cloud.contentwarehouse.v1B\x0ePipelinesProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.pipelines_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x0ePipelinesProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1\xeaAk\n+cloudfunctions.googleapis.com/CloudFunction\x12<projects/{project}/locations/{location}/functions/{function}'
    _globals['_INGESTPIPELINECONFIG'].fields_by_name['folder']._loaded_options = None
    _globals['_INGESTPIPELINECONFIG'].fields_by_name['folder']._serialized_options = b'\xe0A\x01'
    _globals['_INGESTPIPELINECONFIG'].fields_by_name['cloud_function']._loaded_options = None
    _globals['_INGESTPIPELINECONFIG'].fields_by_name['cloud_function']._serialized_options = b'\xfaA-\n+cloudfunctions.googleapis.com/CloudFunction'
    _globals['_GCSINGESTPIPELINE'].fields_by_name['pipeline_config']._loaded_options = None
    _globals['_GCSINGESTPIPELINE'].fields_by_name['pipeline_config']._serialized_options = b'\xe0A\x01'
    _globals['_GCSINGESTWITHDOCAIPROCESSORSPIPELINE'].fields_by_name['pipeline_config']._loaded_options = None
    _globals['_GCSINGESTWITHDOCAIPROCESSORSPIPELINE'].fields_by_name['pipeline_config']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTTOCDWPIPELINE'].fields_by_name['doc_ai_dataset']._loaded_options = None
    _globals['_EXPORTTOCDWPIPELINE'].fields_by_name['doc_ai_dataset']._serialized_options = b'\xe0A\x01'
    _globals['_RUNPIPELINERESPONSE']._serialized_start = 246
    _globals['_RUNPIPELINERESPONSE']._serialized_end = 267
    _globals['_RUNPIPELINEMETADATA']._serialized_start = 270
    _globals['_RUNPIPELINEMETADATA']._serialized_end = 1288
    _globals['_RUNPIPELINEMETADATA_GCSINGESTPIPELINEMETADATA']._serialized_start = 912
    _globals['_RUNPIPELINEMETADATA_GCSINGESTPIPELINEMETADATA']._serialized_end = 959
    _globals['_RUNPIPELINEMETADATA_EXPORTTOCDWPIPELINEMETADATA']._serialized_start = 961
    _globals['_RUNPIPELINEMETADATA_EXPORTTOCDWPIPELINEMETADATA']._serialized_end = 1054
    _globals['_RUNPIPELINEMETADATA_PROCESSWITHDOCAIPIPELINEMETADATA']._serialized_start = 1056
    _globals['_RUNPIPELINEMETADATA_PROCESSWITHDOCAIPIPELINEMETADATA']._serialized_end = 1182
    _globals['_RUNPIPELINEMETADATA_INDIVIDUALDOCUMENTSTATUS']._serialized_start = 1184
    _globals['_RUNPIPELINEMETADATA_INDIVIDUALDOCUMENTSTATUS']._serialized_end = 1267
    _globals['_PROCESSORINFO']._serialized_start = 1290
    _globals['_PROCESSORINFO']._serialized_end = 1373
    _globals['_INGESTPIPELINECONFIG']._serialized_start = 1376
    _globals['_INGESTPIPELINECONFIG']._serialized_end = 1586
    _globals['_GCSINGESTPIPELINE']._serialized_start = 1589
    _globals['_GCSINGESTPIPELINE']._serialized_end = 1792
    _globals['_GCSINGESTWITHDOCAIPROCESSORSPIPELINE']._serialized_start = 1795
    _globals['_GCSINGESTWITHDOCAIPROCESSORSPIPELINE']._serialized_end = 2181
    _globals['_EXPORTTOCDWPIPELINE']._serialized_start = 2183
    _globals['_EXPORTTOCDWPIPELINE']._serialized_end = 2310
    _globals['_PROCESSWITHDOCAIPIPELINE']._serialized_start = 2313
    _globals['_PROCESSWITHDOCAIPIPELINE']._serialized_end = 2498