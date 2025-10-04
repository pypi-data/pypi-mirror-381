"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/batch_job.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import batch_job_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_batch__job__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/ads/googleads/v21/resources/batch_job.proto\x12"google.ads.googleads.v21.resources\x1a5google/ads/googleads/v21/enums/batch_job_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xdb\x07\n\x08BatchJob\x12@\n\rresource_name\x18\x01 \x01(\tB)\xe0A\x05\xfaA#\n!googleads.googleapis.com/BatchJob\x12\x14\n\x02id\x18\x07 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12)\n\x17next_add_sequence_token\x18\x08 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12T\n\x08metadata\x18\x04 \x01(\x0b2=.google.ads.googleads.v21.resources.BatchJob.BatchJobMetadataB\x03\xe0A\x03\x12V\n\x06status\x18\x05 \x01(\x0e2A.google.ads.googleads.v21.enums.BatchJobStatusEnum.BatchJobStatusB\x03\xe0A\x03\x12(\n\x16long_running_operation\x18\t \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x1a\xdb\x03\n\x10BatchJobMetadata\x12$\n\x12creation_date_time\x18\x08 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12!\n\x0fstart_date_time\x18\x07 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12&\n\x14completion_date_time\x18\t \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12,\n\x1aestimated_completion_ratio\x18\n \x01(\x01B\x03\xe0A\x03H\x03\x88\x01\x01\x12!\n\x0foperation_count\x18\x0b \x01(\x03B\x03\xe0A\x03H\x04\x88\x01\x01\x12*\n\x18executed_operation_count\x18\x0c \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12)\n\x17execution_limit_seconds\x18\r \x01(\x05B\x03\xe0A\x05H\x06\x88\x01\x01B\x15\n\x13_creation_date_timeB\x12\n\x10_start_date_timeB\x17\n\x15_completion_date_timeB\x1d\n\x1b_estimated_completion_ratioB\x12\n\x10_operation_countB\x1b\n\x19_executed_operation_countB\x1a\n\x18_execution_limit_seconds:X\xeaAU\n!googleads.googleapis.com/BatchJob\x120customers/{customer_id}/batchJobs/{batch_job_id}B\x05\n\x03_idB\x1a\n\x18_next_add_sequence_tokenB\x19\n\x17_long_running_operationB\xff\x01\n&com.google.ads.googleads.v21.resourcesB\rBatchJobProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.batch_job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\rBatchJobProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['start_date_time']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['start_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['completion_date_time']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['completion_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['estimated_completion_ratio']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['estimated_completion_ratio']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['operation_count']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['operation_count']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['executed_operation_count']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['executed_operation_count']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['execution_limit_seconds']._loaded_options = None
    _globals['_BATCHJOB_BATCHJOBMETADATA'].fields_by_name['execution_limit_seconds']._serialized_options = b'\xe0A\x05'
    _globals['_BATCHJOB'].fields_by_name['resource_name']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA#\n!googleads.googleapis.com/BatchJob'
    _globals['_BATCHJOB'].fields_by_name['id']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB'].fields_by_name['next_add_sequence_token']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['next_add_sequence_token']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB'].fields_by_name['metadata']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['metadata']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB'].fields_by_name['status']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB'].fields_by_name['long_running_operation']._loaded_options = None
    _globals['_BATCHJOB'].fields_by_name['long_running_operation']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHJOB']._loaded_options = None
    _globals['_BATCHJOB']._serialized_options = b'\xeaAU\n!googleads.googleapis.com/BatchJob\x120customers/{customer_id}/batchJobs/{batch_job_id}'
    _globals['_BATCHJOB']._serialized_start = 206
    _globals['_BATCHJOB']._serialized_end = 1193
    _globals['_BATCHJOB_BATCHJOBMETADATA']._serialized_start = 566
    _globals['_BATCHJOB_BATCHJOBMETADATA']._serialized_end = 1041