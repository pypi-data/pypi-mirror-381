"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/pipeline_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import pipeline_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_pipeline__job__pb2
from .....google.cloud.aiplatform.v1beta1 import training_pipeline_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_training__pipeline__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/pipeline_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a2google/cloud/aiplatform/v1beta1/pipeline_job.proto\x1a7google/cloud/aiplatform/v1beta1/training_pipeline.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x7f\n(BatchCancelPipelineJobsOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xad\x01\n\x1dCreateTrainingPipelineRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12Q\n\x11training_pipeline\x18\x02 \x01(\x0b21.google.cloud.aiplatform.v1beta1.TrainingPipelineB\x03\xe0A\x02"^\n\x1aGetTrainingPipelineRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline"\xbf\x01\n\x1cListTrainingPipelinesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12-\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMask"\x87\x01\n\x1dListTrainingPipelinesResponse\x12M\n\x12training_pipelines\x18\x01 \x03(\x0b21.google.cloud.aiplatform.v1beta1.TrainingPipeline\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"a\n\x1dDeleteTrainingPipelineRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline"a\n\x1dCancelTrainingPipelineRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline"\xb7\x01\n\x18CreatePipelineJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12G\n\x0cpipeline_job\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.PipelineJobB\x03\xe0A\x02\x12\x17\n\x0fpipeline_job_id\x18\x03 \x01(\t"T\n\x15GetPipelineJobRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/PipelineJob"\xcc\x01\n\x17ListPipelineJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x06 \x01(\t\x12-\n\tread_mask\x18\x07 \x01(\x0b2\x1a.google.protobuf.FieldMask"x\n\x18ListPipelineJobsResponse\x12C\n\rpipeline_jobs\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1beta1.PipelineJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"W\n\x18DeletePipelineJobRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/PipelineJob"\x9d\x01\n\x1eBatchDeletePipelineJobsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%aiplatform.googleapis.com/PipelineJob\x12<\n\x05names\x18\x02 \x03(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/PipelineJob"f\n\x1fBatchDeletePipelineJobsResponse\x12C\n\rpipeline_jobs\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1beta1.PipelineJob"W\n\x18CancelPipelineJobRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/PipelineJob"\x9d\x01\n\x1eBatchCancelPipelineJobsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%aiplatform.googleapis.com/PipelineJob\x12<\n\x05names\x18\x02 \x03(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/PipelineJob"f\n\x1fBatchCancelPipelineJobsResponse\x12C\n\rpipeline_jobs\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1beta1.PipelineJob2\xbd\x16\n\x0fPipelineService\x12\xfd\x01\n\x16CreateTrainingPipeline\x12>.google.cloud.aiplatform.v1beta1.CreateTrainingPipelineRequest\x1a1.google.cloud.aiplatform.v1beta1.TrainingPipeline"p\xdaA\x18parent,training_pipeline\x82\xd3\xe4\x93\x02O":/v1beta1/{parent=projects/*/locations/*}/trainingPipelines:\x11training_pipeline\x12\xd0\x01\n\x13GetTrainingPipeline\x12;.google.cloud.aiplatform.v1beta1.GetTrainingPipelineRequest\x1a1.google.cloud.aiplatform.v1beta1.TrainingPipeline"I\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}\x12\xe3\x01\n\x15ListTrainingPipelines\x12=.google.cloud.aiplatform.v1beta1.ListTrainingPipelinesRequest\x1a>.google.cloud.aiplatform.v1beta1.ListTrainingPipelinesResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{parent=projects/*/locations/*}/trainingPipelines\x12\xf5\x01\n\x16DeleteTrainingPipeline\x12>.google.cloud.aiplatform.v1beta1.DeleteTrainingPipelineRequest\x1a\x1d.google.longrunning.Operation"|\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}\x12\xc5\x01\n\x16CancelTrainingPipeline\x12>.google.cloud.aiplatform.v1beta1.CancelTrainingPipelineRequest\x1a\x16.google.protobuf.Empty"S\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}:cancel:\x01*\x12\xef\x01\n\x11CreatePipelineJob\x129.google.cloud.aiplatform.v1beta1.CreatePipelineJobRequest\x1a,.google.cloud.aiplatform.v1beta1.PipelineJob"q\xdaA#parent,pipeline_job,pipeline_job_id\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:\x0cpipeline_job\x12\xbc\x01\n\x0eGetPipelineJob\x126.google.cloud.aiplatform.v1beta1.GetPipelineJobRequest\x1a,.google.cloud.aiplatform.v1beta1.PipelineJob"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}\x12\xcf\x01\n\x10ListPipelineJobs\x128.google.cloud.aiplatform.v1beta1.ListPipelineJobsRequest\x1a9.google.cloud.aiplatform.v1beta1.ListPipelineJobsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/pipelineJobs\x12\xe6\x01\n\x11DeletePipelineJob\x129.google.cloud.aiplatform.v1beta1.DeletePipelineJobRequest\x1a\x1d.google.longrunning.Operation"w\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}\x12\x94\x02\n\x17BatchDeletePipelineJobs\x12?.google.cloud.aiplatform.v1beta1.BatchDeletePipelineJobsRequest\x1a\x1d.google.longrunning.Operation"\x98\x01\xcaA:\n\x1fBatchDeletePipelineJobsResponse\x12\x17DeleteOperationMetadata\xdaA\x0cparent,names\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:batchDelete:\x01*\x12\xb6\x01\n\x11CancelPipelineJob\x129.google.cloud.aiplatform.v1beta1.CancelPipelineJobRequest\x1a\x16.google.protobuf.Empty"N\xdaA\x04name\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/pipelineJobs/*}:cancel:\x01*\x12\xa5\x02\n\x17BatchCancelPipelineJobs\x12?.google.cloud.aiplatform.v1beta1.BatchCancelPipelineJobsRequest\x1a\x1d.google.longrunning.Operation"\xa9\x01\xcaAK\n\x1fBatchCancelPipelineJobsResponse\x12(BatchCancelPipelineJobsOperationMetadata\xdaA\x0cparent,names\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:batchCancel:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14PipelineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.pipeline_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14PipelineServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATETRAININGPIPELINEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETRAININGPIPELINEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATETRAININGPIPELINEREQUEST'].fields_by_name['training_pipeline']._loaded_options = None
    _globals['_CREATETRAININGPIPELINEREQUEST'].fields_by_name['training_pipeline']._serialized_options = b'\xe0A\x02'
    _globals['_GETTRAININGPIPELINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTRAININGPIPELINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline'
    _globals['_LISTTRAININGPIPELINESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTRAININGPIPELINESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETETRAININGPIPELINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETRAININGPIPELINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline'
    _globals['_CANCELTRAININGPIPELINEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELTRAININGPIPELINEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*aiplatform.googleapis.com/TrainingPipeline'
    _globals['_CREATEPIPELINEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPIPELINEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPIPELINEJOBREQUEST'].fields_by_name['pipeline_job']._loaded_options = None
    _globals['_CREATEPIPELINEJOBREQUEST'].fields_by_name['pipeline_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETPIPELINEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPIPELINEJOBREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_LISTPIPELINEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPIPELINEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DELETEPIPELINEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPIPELINEJOBREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%aiplatform.googleapis.com/PipelineJob"
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST'].fields_by_name['names']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_CANCELPIPELINEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELPIPELINEJOBREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%aiplatform.googleapis.com/PipelineJob"
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST'].fields_by_name['names']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/PipelineJob"
    _globals['_PIPELINESERVICE']._loaded_options = None
    _globals['_PIPELINESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PIPELINESERVICE'].methods_by_name['CreateTrainingPipeline']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['CreateTrainingPipeline']._serialized_options = b'\xdaA\x18parent,training_pipeline\x82\xd3\xe4\x93\x02O":/v1beta1/{parent=projects/*/locations/*}/trainingPipelines:\x11training_pipeline'
    _globals['_PIPELINESERVICE'].methods_by_name['GetTrainingPipeline']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['GetTrainingPipeline']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}'
    _globals['_PIPELINESERVICE'].methods_by_name['ListTrainingPipelines']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['ListTrainingPipelines']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1beta1/{parent=projects/*/locations/*}/trainingPipelines'
    _globals['_PIPELINESERVICE'].methods_by_name['DeleteTrainingPipeline']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['DeleteTrainingPipeline']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02<*:/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}'
    _globals['_PIPELINESERVICE'].methods_by_name['CancelTrainingPipeline']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['CancelTrainingPipeline']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F"A/v1beta1/{name=projects/*/locations/*/trainingPipelines/*}:cancel:\x01*'
    _globals['_PIPELINESERVICE'].methods_by_name['CreatePipelineJob']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['CreatePipelineJob']._serialized_options = b'\xdaA#parent,pipeline_job,pipeline_job_id\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:\x0cpipeline_job'
    _globals['_PIPELINESERVICE'].methods_by_name['GetPipelineJob']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['GetPipelineJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}'
    _globals['_PIPELINESERVICE'].methods_by_name['ListPipelineJobs']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['ListPipelineJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/pipelineJobs'
    _globals['_PIPELINESERVICE'].methods_by_name['DeletePipelineJob']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['DeletePipelineJob']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/pipelineJobs/*}'
    _globals['_PIPELINESERVICE'].methods_by_name['BatchDeletePipelineJobs']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['BatchDeletePipelineJobs']._serialized_options = b'\xcaA:\n\x1fBatchDeletePipelineJobsResponse\x12\x17DeleteOperationMetadata\xdaA\x0cparent,names\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:batchDelete:\x01*'
    _globals['_PIPELINESERVICE'].methods_by_name['CancelPipelineJob']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['CancelPipelineJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02A"</v1beta1/{name=projects/*/locations/*/pipelineJobs/*}:cancel:\x01*'
    _globals['_PIPELINESERVICE'].methods_by_name['BatchCancelPipelineJobs']._loaded_options = None
    _globals['_PIPELINESERVICE'].methods_by_name['BatchCancelPipelineJobs']._serialized_options = b'\xcaAK\n\x1fBatchCancelPipelineJobsResponse\x12(BatchCancelPipelineJobsOperationMetadata\xdaA\x0cparent,names\x82\xd3\xe4\x93\x02F"A/v1beta1/{parent=projects/*/locations/*}/pipelineJobs:batchCancel:\x01*'
    _globals['_BATCHCANCELPIPELINEJOBSOPERATIONMETADATA']._serialized_start = 464
    _globals['_BATCHCANCELPIPELINEJOBSOPERATIONMETADATA']._serialized_end = 591
    _globals['_CREATETRAININGPIPELINEREQUEST']._serialized_start = 594
    _globals['_CREATETRAININGPIPELINEREQUEST']._serialized_end = 767
    _globals['_GETTRAININGPIPELINEREQUEST']._serialized_start = 769
    _globals['_GETTRAININGPIPELINEREQUEST']._serialized_end = 863
    _globals['_LISTTRAININGPIPELINESREQUEST']._serialized_start = 866
    _globals['_LISTTRAININGPIPELINESREQUEST']._serialized_end = 1057
    _globals['_LISTTRAININGPIPELINESRESPONSE']._serialized_start = 1060
    _globals['_LISTTRAININGPIPELINESRESPONSE']._serialized_end = 1195
    _globals['_DELETETRAININGPIPELINEREQUEST']._serialized_start = 1197
    _globals['_DELETETRAININGPIPELINEREQUEST']._serialized_end = 1294
    _globals['_CANCELTRAININGPIPELINEREQUEST']._serialized_start = 1296
    _globals['_CANCELTRAININGPIPELINEREQUEST']._serialized_end = 1393
    _globals['_CREATEPIPELINEJOBREQUEST']._serialized_start = 1396
    _globals['_CREATEPIPELINEJOBREQUEST']._serialized_end = 1579
    _globals['_GETPIPELINEJOBREQUEST']._serialized_start = 1581
    _globals['_GETPIPELINEJOBREQUEST']._serialized_end = 1665
    _globals['_LISTPIPELINEJOBSREQUEST']._serialized_start = 1668
    _globals['_LISTPIPELINEJOBSREQUEST']._serialized_end = 1872
    _globals['_LISTPIPELINEJOBSRESPONSE']._serialized_start = 1874
    _globals['_LISTPIPELINEJOBSRESPONSE']._serialized_end = 1994
    _globals['_DELETEPIPELINEJOBREQUEST']._serialized_start = 1996
    _globals['_DELETEPIPELINEJOBREQUEST']._serialized_end = 2083
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST']._serialized_start = 2086
    _globals['_BATCHDELETEPIPELINEJOBSREQUEST']._serialized_end = 2243
    _globals['_BATCHDELETEPIPELINEJOBSRESPONSE']._serialized_start = 2245
    _globals['_BATCHDELETEPIPELINEJOBSRESPONSE']._serialized_end = 2347
    _globals['_CANCELPIPELINEJOBREQUEST']._serialized_start = 2349
    _globals['_CANCELPIPELINEJOBREQUEST']._serialized_end = 2436
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST']._serialized_start = 2439
    _globals['_BATCHCANCELPIPELINEJOBSREQUEST']._serialized_end = 2596
    _globals['_BATCHCANCELPIPELINEJOBSRESPONSE']._serialized_start = 2598
    _globals['_BATCHCANCELPIPELINEJOBSRESPONSE']._serialized_end = 2700
    _globals['_PIPELINESERVICE']._serialized_start = 2703
    _globals['_PIPELINESERVICE']._serialized_end = 5580