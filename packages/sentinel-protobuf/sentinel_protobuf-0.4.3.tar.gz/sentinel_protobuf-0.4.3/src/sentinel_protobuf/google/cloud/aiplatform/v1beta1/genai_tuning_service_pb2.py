"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/genai_tuning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_io__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import tuning_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_tuning__job__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/aiplatform/v1beta1/genai_tuning_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/aiplatform/v1beta1/io.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a0google/cloud/aiplatform/v1beta1/tuning_job.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"\x98\x01\n\x16CreateTuningJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12C\n\ntuning_job\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.TuningJobB\x03\xe0A\x02"P\n\x13GetTuningJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob"\x98\x01\n\x15ListTuningJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"r\n\x16ListTuningJobsResponse\x12?\n\x0btuning_jobs\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1beta1.TuningJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x16CancelTuningJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob"\xe1\x02\n\x17RebaseTunedModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12L\n\x0ftuned_model_ref\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.TunedModelRefB\x03\xe0A\x02\x12C\n\ntuning_job\x18\x03 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.TuningJobB\x03\xe0A\x01\x12R\n\x14artifact_destination\x18\x04 \x01(\x0b2/.google.cloud.aiplatform.v1beta1.GcsDestinationB\x03\xe0A\x01\x12$\n\x17deploy_to_same_endpoint\x18\x05 \x01(\x08B\x03\xe0A\x01"x\n!RebaseTunedModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata2\xf7\x08\n\x12GenAiTuningService\x12\xd3\x01\n\x0fCreateTuningJob\x127.google.cloud.aiplatform.v1beta1.CreateTuningJobRequest\x1a*.google.cloud.aiplatform.v1beta1.TuningJob"[\xdaA\x11parent,tuning_job\x82\xd3\xe4\x93\x02A"3/v1beta1/{parent=projects/*/locations/*}/tuningJobs:\ntuning_job\x12\xb4\x01\n\x0cGetTuningJob\x124.google.cloud.aiplatform.v1beta1.GetTuningJobRequest\x1a*.google.cloud.aiplatform.v1beta1.TuningJob"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/tuningJobs/*}\x12\xc7\x01\n\x0eListTuningJobs\x126.google.cloud.aiplatform.v1beta1.ListTuningJobsRequest\x1a7.google.cloud.aiplatform.v1beta1.ListTuningJobsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/tuningJobs\x12\xb0\x01\n\x0fCancelTuningJob\x127.google.cloud.aiplatform.v1beta1.CancelTuningJobRequest\x1a\x16.google.protobuf.Empty"L\xdaA\x04name\x82\xd3\xe4\x93\x02?":/v1beta1/{name=projects/*/locations/*/tuningJobs/*}:cancel:\x01*\x12\x87\x02\n\x10RebaseTunedModel\x128.google.cloud.aiplatform.v1beta1.RebaseTunedModelRequest\x1a\x1d.google.longrunning.Operation"\x99\x01\xcaA.\n\tTuningJob\x12!RebaseTunedModelOperationMetadata\xdaA\x16parent,tuned_model_ref\x82\xd3\xe4\x93\x02I"D/v1beta1/{parent=projects/*/locations/*}/tuningJobs:rebaseTunedModel:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xee\x01\n#com.google.cloud.aiplatform.v1beta1B\x17GenAiTuningServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.genai_tuning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x17GenAiTuningServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATETUNINGJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETUNINGJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATETUNINGJOBREQUEST'].fields_by_name['tuning_job']._loaded_options = None
    _globals['_CREATETUNINGJOBREQUEST'].fields_by_name['tuning_job']._serialized_options = b'\xe0A\x02'
    _globals['_GETTUNINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTUNINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob'
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTTUNINGJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELTUNINGJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELTUNINGJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob'
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['tuned_model_ref']._loaded_options = None
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['tuned_model_ref']._serialized_options = b'\xe0A\x02'
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['tuning_job']._loaded_options = None
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['tuning_job']._serialized_options = b'\xe0A\x01'
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['artifact_destination']._loaded_options = None
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['artifact_destination']._serialized_options = b'\xe0A\x01'
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['deploy_to_same_endpoint']._loaded_options = None
    _globals['_REBASETUNEDMODELREQUEST'].fields_by_name['deploy_to_same_endpoint']._serialized_options = b'\xe0A\x01'
    _globals['_GENAITUNINGSERVICE']._loaded_options = None
    _globals['_GENAITUNINGSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CreateTuningJob']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CreateTuningJob']._serialized_options = b'\xdaA\x11parent,tuning_job\x82\xd3\xe4\x93\x02A"3/v1beta1/{parent=projects/*/locations/*}/tuningJobs:\ntuning_job'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['GetTuningJob']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['GetTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/tuningJobs/*}'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['ListTuningJobs']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['ListTuningJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/tuningJobs'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CancelTuningJob']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CancelTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02?":/v1beta1/{name=projects/*/locations/*/tuningJobs/*}:cancel:\x01*'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['RebaseTunedModel']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['RebaseTunedModel']._serialized_options = b'\xcaA.\n\tTuningJob\x12!RebaseTunedModelOperationMetadata\xdaA\x16parent,tuned_model_ref\x82\xd3\xe4\x93\x02I"D/v1beta1/{parent=projects/*/locations/*}/tuningJobs:rebaseTunedModel:\x01*'
    _globals['_CREATETUNINGJOBREQUEST']._serialized_start = 418
    _globals['_CREATETUNINGJOBREQUEST']._serialized_end = 570
    _globals['_GETTUNINGJOBREQUEST']._serialized_start = 572
    _globals['_GETTUNINGJOBREQUEST']._serialized_end = 652
    _globals['_LISTTUNINGJOBSREQUEST']._serialized_start = 655
    _globals['_LISTTUNINGJOBSREQUEST']._serialized_end = 807
    _globals['_LISTTUNINGJOBSRESPONSE']._serialized_start = 809
    _globals['_LISTTUNINGJOBSRESPONSE']._serialized_end = 923
    _globals['_CANCELTUNINGJOBREQUEST']._serialized_start = 925
    _globals['_CANCELTUNINGJOBREQUEST']._serialized_end = 1008
    _globals['_REBASETUNEDMODELREQUEST']._serialized_start = 1011
    _globals['_REBASETUNEDMODELREQUEST']._serialized_end = 1364
    _globals['_REBASETUNEDMODELOPERATIONMETADATA']._serialized_start = 1366
    _globals['_REBASETUNEDMODELOPERATIONMETADATA']._serialized_end = 1486
    _globals['_GENAITUNINGSERVICE']._serialized_start = 1489
    _globals['_GENAITUNINGSERVICE']._serialized_end = 2632