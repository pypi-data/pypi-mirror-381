"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/pipeline_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import common_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_common__pb2
from .....google.cloud.contentwarehouse.v1 import pipelines_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_pipelines__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/contentwarehouse/v1/pipeline_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/contentwarehouse/v1/common.proto\x1a0google/cloud/contentwarehouse/v1/pipelines.proto\x1a#google/longrunning/operations.proto"\xb9\x04\n\x12RunPipelineRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12R\n\x13gcs_ingest_pipeline\x18\x02 \x01(\x0b23.google.cloud.contentwarehouse.v1.GcsIngestPipelineH\x00\x12|\n*gcs_ingest_with_doc_ai_processors_pipeline\x18\x03 \x01(\x0b2F.google.cloud.contentwarehouse.v1.GcsIngestWithDocAiProcessorsPipelineH\x00\x12T\n\x13export_cdw_pipeline\x18\x04 \x01(\x0b25.google.cloud.contentwarehouse.v1.ExportToCdwPipelineH\x00\x12b\n\x1cprocess_with_doc_ai_pipeline\x18\x05 \x01(\x0b2:.google.cloud.contentwarehouse.v1.ProcessWithDocAiPipelineH\x00\x12K\n\x10request_metadata\x18\x06 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadataB\n\n\x08pipeline2\xb9\x02\n\x0fPipelineService\x12\xd0\x01\n\x0bRunPipeline\x124.google.cloud.contentwarehouse.v1.RunPipelineRequest\x1a\x1d.google.longrunning.Operation"l\xcaA*\n\x13RunPipelineResponse\x12\x13RunPipelineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/locations/*}:runPipeline:\x01*\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfc\x01\n$com.google.cloud.contentwarehouse.v1B\x14PipelineServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.pipeline_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x14PipelineServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_RUNPIPELINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNPIPELINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_PIPELINESERVICE']._loaded_options = None
    _globals['_PIPELINESERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PIPELINESERVICE'].methods_by_name['RunPipeline']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['RunPipeline']._serialized_options = b'\xcaA*\n\x13RunPipelineResponse\x12\x13RunPipelineMetadata\xdaA\x04name\x82\xd3\xe4\x93\x022"-/v1/{name=projects/*/locations/*}:runPipeline:\x01*'
    _globals['_RUNPIPELINEREQUEST']._serialized_start = 343
    _globals['_RUNPIPELINEREQUEST']._serialized_end = 912
    _globals['_PIPELINESERVICE']._serialized_start = 915
    _globals['_PIPELINESERVICE']._serialized_end = 1228