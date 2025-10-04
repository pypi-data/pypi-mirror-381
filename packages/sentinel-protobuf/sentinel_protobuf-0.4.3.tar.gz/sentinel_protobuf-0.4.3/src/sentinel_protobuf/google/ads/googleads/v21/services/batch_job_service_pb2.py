"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/batch_job_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v21.resources import batch_job_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_batch__job__pb2
from ......google.ads.googleads.v21.services import google_ads_service_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_services_dot_google__ads__service__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v21/services/batch_job_service.proto\x12!google.ads.googleads.v21.services\x1a:google/ads/googleads/v21/enums/response_content_type.proto\x1a2google/ads/googleads/v21/resources/batch_job.proto\x1a:google/ads/googleads/v21/services/google_ads_service.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x17google/rpc/status.proto"\x7f\n\x15MutateBatchJobRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12L\n\toperation\x18\x02 \x01(\x0b24.google.ads.googleads.v21.services.BatchJobOperationB\x03\xe0A\x02"\x9a\x01\n\x11BatchJobOperation\x12>\n\x06create\x18\x01 \x01(\x0b2,.google.ads.googleads.v21.resources.BatchJobH\x00\x128\n\x06remove\x18\x04 \x01(\tB&\xfaA#\n!googleads.googleapis.com/BatchJobH\x00B\x0b\n\toperation"a\n\x16MutateBatchJobResponse\x12G\n\x06result\x18\x01 \x01(\x0b27.google.ads.googleads.v21.services.MutateBatchJobResult"U\n\x14MutateBatchJobResult\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/BatchJob"V\n\x12RunBatchJobRequest\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob"\xcc\x01\n\x1cAddBatchJobOperationsRequest\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob\x12\x16\n\x0esequence_token\x18\x02 \x01(\t\x12R\n\x11mutate_operations\x18\x03 \x03(\x0b22.google.ads.googleads.v21.services.MutateOperationB\x03\xe0A\x02"V\n\x1dAddBatchJobOperationsResponse\x12\x18\n\x10total_operations\x18\x01 \x01(\x03\x12\x1b\n\x13next_sequence_token\x18\x02 \x01(\t"\xf1\x01\n\x1aListBatchJobResultsRequest\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12j\n\x15response_content_type\x18\x04 \x01(\x0e2K.google.ads.googleads.v21.enums.ResponseContentTypeEnum.ResponseContentType"z\n\x1bListBatchJobResultsResponse\x12B\n\x07results\x18\x01 \x03(\x0b21.google.ads.googleads.v21.services.BatchJobResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xac\x01\n\x0eBatchJobResult\x12\x17\n\x0foperation_index\x18\x01 \x01(\x03\x12]\n\x19mutate_operation_response\x18\x02 \x01(\x0b2:.google.ads.googleads.v21.services.MutateOperationResponse\x12"\n\x06status\x18\x03 \x01(\x0b2\x12.google.rpc.Status2\xe1\x08\n\x0fBatchJobService\x12\xd9\x01\n\x0eMutateBatchJob\x128.google.ads.googleads.v21.services.MutateBatchJobRequest\x1a9.google.ads.googleads.v21.services.MutateBatchJobResponse"R\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x024"//v21/customers/{customer_id=*}/batchJobs:mutate:\x01*\x12\xe6\x01\n\x13ListBatchJobResults\x12=.google.ads.googleads.v21.services.ListBatchJobResultsRequest\x1a>.google.ads.googleads.v21.services.ListBatchJobResultsResponse"P\xdaA\rresource_name\x82\xd3\xe4\x93\x02:\x128/v21/{resource_name=customers/*/batchJobs/*}:listResults\x12\x89\x02\n\x0bRunBatchJob\x125.google.ads.googleads.v21.services.RunBatchJobRequest\x1a\x1d.google.longrunning.Operation"\xa3\x01\xcaAU\n\x15google.protobuf.Empty\x12<google.ads.googleads.v21.resources.BatchJob.BatchJobMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x025"0/v21/{resource_name=customers/*/batchJobs/*}:run:\x01*\x12\xb5\x02\n\x15AddBatchJobOperations\x12?.google.ads.googleads.v21.services.AddBatchJobOperationsRequest\x1a@.google.ads.googleads.v21.services.AddBatchJobOperationsResponse"\x98\x01\xdaA.resource_name,sequence_token,mutate_operations\xdaA\x1fresource_name,mutate_operations\x82\xd3\xe4\x93\x02?":/v21/{resource_name=customers/*/batchJobs/*}:addOperations:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v21.servicesB\x14BatchJobServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.batch_job_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x14BatchJobServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEBATCHJOBREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEBATCHJOBREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEBATCHJOBREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATEBATCHJOBREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHJOBOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_BATCHJOBOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_MUTATEBATCHJOBRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEBATCHJOBRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_RUNBATCHJOBREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_RUNBATCHJOBREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_ADDBATCHJOBOPERATIONSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADDBATCHJOBOPERATIONSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_ADDBATCHJOBOPERATIONSREQUEST'].fields_by_name['mutate_operations']._loaded_options = None
    _globals['_ADDBATCHJOBOPERATIONSREQUEST'].fields_by_name['mutate_operations']._serialized_options = b'\xe0A\x02'
    _globals['_LISTBATCHJOBRESULTSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LISTBATCHJOBRESULTSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_BATCHJOBSERVICE']._loaded_options = None
    _globals['_BATCHJOBSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_BATCHJOBSERVICE'].methods_by_name['MutateBatchJob']._loaded_options = None
    _globals['_BATCHJOBSERVICE'].methods_by_name['MutateBatchJob']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x024"//v21/customers/{customer_id=*}/batchJobs:mutate:\x01*'
    _globals['_BATCHJOBSERVICE'].methods_by_name['ListBatchJobResults']._loaded_options = None
    _globals['_BATCHJOBSERVICE'].methods_by_name['ListBatchJobResults']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02:\x128/v21/{resource_name=customers/*/batchJobs/*}:listResults'
    _globals['_BATCHJOBSERVICE'].methods_by_name['RunBatchJob']._loaded_options = None
    _globals['_BATCHJOBSERVICE'].methods_by_name['RunBatchJob']._serialized_options = b'\xcaAU\n\x15google.protobuf.Empty\x12<google.ads.googleads.v21.resources.BatchJob.BatchJobMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x025"0/v21/{resource_name=customers/*/batchJobs/*}:run:\x01*'
    _globals['_BATCHJOBSERVICE'].methods_by_name['AddBatchJobOperations']._loaded_options = None
    _globals['_BATCHJOBSERVICE'].methods_by_name['AddBatchJobOperations']._serialized_options = b'\xdaA.resource_name,sequence_token,mutate_operations\xdaA\x1fresource_name,mutate_operations\x82\xd3\xe4\x93\x02?":/v21/{resource_name=customers/*/batchJobs/*}:addOperations:\x01*'
    _globals['_MUTATEBATCHJOBREQUEST']._serialized_start = 474
    _globals['_MUTATEBATCHJOBREQUEST']._serialized_end = 601
    _globals['_BATCHJOBOPERATION']._serialized_start = 604
    _globals['_BATCHJOBOPERATION']._serialized_end = 758
    _globals['_MUTATEBATCHJOBRESPONSE']._serialized_start = 760
    _globals['_MUTATEBATCHJOBRESPONSE']._serialized_end = 857
    _globals['_MUTATEBATCHJOBRESULT']._serialized_start = 859
    _globals['_MUTATEBATCHJOBRESULT']._serialized_end = 944
    _globals['_RUNBATCHJOBREQUEST']._serialized_start = 946
    _globals['_RUNBATCHJOBREQUEST']._serialized_end = 1032
    _globals['_ADDBATCHJOBOPERATIONSREQUEST']._serialized_start = 1035
    _globals['_ADDBATCHJOBOPERATIONSREQUEST']._serialized_end = 1239
    _globals['_ADDBATCHJOBOPERATIONSRESPONSE']._serialized_start = 1241
    _globals['_ADDBATCHJOBOPERATIONSRESPONSE']._serialized_end = 1327
    _globals['_LISTBATCHJOBRESULTSREQUEST']._serialized_start = 1330
    _globals['_LISTBATCHJOBRESULTSREQUEST']._serialized_end = 1571
    _globals['_LISTBATCHJOBRESULTSRESPONSE']._serialized_start = 1573
    _globals['_LISTBATCHJOBRESULTSRESPONSE']._serialized_end = 1695
    _globals['_BATCHJOBRESULT']._serialized_start = 1698
    _globals['_BATCHJOBRESULT']._serialized_end = 1870
    _globals['_BATCHJOBSERVICE']._serialized_start = 1873
    _globals['_BATCHJOBSERVICE']._serialized_end = 2994