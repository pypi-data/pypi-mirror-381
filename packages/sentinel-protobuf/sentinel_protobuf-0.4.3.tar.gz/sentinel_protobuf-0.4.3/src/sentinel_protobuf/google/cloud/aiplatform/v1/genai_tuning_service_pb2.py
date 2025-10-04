"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/genai_tuning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import io_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_io__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.cloud.aiplatform.v1 import tuning_job_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_tuning__job__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/genai_tuning_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/cloud/aiplatform/v1/io.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a+google/cloud/aiplatform/v1/tuning_job.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"\x93\x01\n\x16CreateTuningJobRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12>\n\ntuning_job\x18\x02 \x01(\x0b2%.google.cloud.aiplatform.v1.TuningJobB\x03\xe0A\x02"P\n\x13GetTuningJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob"\x98\x01\n\x15ListTuningJobsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"m\n\x16ListTuningJobsResponse\x12:\n\x0btuning_jobs\x18\x01 \x03(\x0b2%.google.cloud.aiplatform.v1.TuningJob\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x16CancelTuningJobRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/TuningJob"\xd2\x02\n\x17RebaseTunedModelRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12G\n\x0ftuned_model_ref\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1.TunedModelRefB\x03\xe0A\x02\x12>\n\ntuning_job\x18\x03 \x01(\x0b2%.google.cloud.aiplatform.v1.TuningJobB\x03\xe0A\x01\x12M\n\x14artifact_destination\x18\x04 \x01(\x0b2*.google.cloud.aiplatform.v1.GcsDestinationB\x03\xe0A\x01\x12$\n\x17deploy_to_same_endpoint\x18\x05 \x01(\x08B\x03\xe0A\x01"s\n!RebaseTunedModelOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata2\xb6\x08\n\x12GenAiTuningService\x12\xc4\x01\n\x0fCreateTuningJob\x122.google.cloud.aiplatform.v1.CreateTuningJobRequest\x1a%.google.cloud.aiplatform.v1.TuningJob"V\xdaA\x11parent,tuning_job\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/tuningJobs:\ntuning_job\x12\xa5\x01\n\x0cGetTuningJob\x12/.google.cloud.aiplatform.v1.GetTuningJobRequest\x1a%.google.cloud.aiplatform.v1.TuningJob"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/tuningJobs/*}\x12\xb8\x01\n\x0eListTuningJobs\x121.google.cloud.aiplatform.v1.ListTuningJobsRequest\x1a2.google.cloud.aiplatform.v1.ListTuningJobsResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/tuningJobs\x12\xa6\x01\n\x0fCancelTuningJob\x122.google.cloud.aiplatform.v1.CancelTuningJobRequest\x1a\x16.google.protobuf.Empty"G\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/tuningJobs/*}:cancel:\x01*\x12\xfd\x01\n\x10RebaseTunedModel\x123.google.cloud.aiplatform.v1.RebaseTunedModelRequest\x1a\x1d.google.longrunning.Operation"\x94\x01\xcaA.\n\tTuningJob\x12!RebaseTunedModelOperationMetadata\xdaA\x16parent,tuned_model_ref\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*}/tuningJobs:rebaseTunedModel:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd5\x01\n\x1ecom.google.cloud.aiplatform.v1B\x17GenAiTuningServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.genai_tuning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x17GenAiTuningServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
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
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CreateTuningJob']._serialized_options = b'\xdaA\x11parent,tuning_job\x82\xd3\xe4\x93\x02<"./v1/{parent=projects/*/locations/*}/tuningJobs:\ntuning_job'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['GetTuningJob']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['GetTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/tuningJobs/*}'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['ListTuningJobs']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['ListTuningJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/tuningJobs'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CancelTuningJob']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['CancelTuningJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/tuningJobs/*}:cancel:\x01*'
    _globals['_GENAITUNINGSERVICE'].methods_by_name['RebaseTunedModel']._loaded_options = None
    _globals['_GENAITUNINGSERVICE'].methods_by_name['RebaseTunedModel']._serialized_options = b'\xcaA.\n\tTuningJob\x12!RebaseTunedModelOperationMetadata\xdaA\x16parent,tuned_model_ref\x82\xd3\xe4\x93\x02D"?/v1/{parent=projects/*/locations/*}/tuningJobs:rebaseTunedModel:\x01*'
    _globals['_CREATETUNINGJOBREQUEST']._serialized_start = 393
    _globals['_CREATETUNINGJOBREQUEST']._serialized_end = 540
    _globals['_GETTUNINGJOBREQUEST']._serialized_start = 542
    _globals['_GETTUNINGJOBREQUEST']._serialized_end = 622
    _globals['_LISTTUNINGJOBSREQUEST']._serialized_start = 625
    _globals['_LISTTUNINGJOBSREQUEST']._serialized_end = 777
    _globals['_LISTTUNINGJOBSRESPONSE']._serialized_start = 779
    _globals['_LISTTUNINGJOBSRESPONSE']._serialized_end = 888
    _globals['_CANCELTUNINGJOBREQUEST']._serialized_start = 890
    _globals['_CANCELTUNINGJOBREQUEST']._serialized_end = 973
    _globals['_REBASETUNEDMODELREQUEST']._serialized_start = 976
    _globals['_REBASETUNEDMODELREQUEST']._serialized_end = 1314
    _globals['_REBASETUNEDMODELOPERATIONMETADATA']._serialized_start = 1316
    _globals['_REBASETUNEDMODELOPERATIONMETADATA']._serialized_end = 1431
    _globals['_GENAITUNINGSERVICE']._serialized_start = 1434
    _globals['_GENAITUNINGSERVICE']._serialized_end = 2512