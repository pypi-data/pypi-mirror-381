"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/job.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.bigquery.v2 import data_format_options_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_data__format__options__pb2
from .....google.cloud.bigquery.v2 import dataset_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_dataset__reference__pb2
from .....google.cloud.bigquery.v2 import encryption_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_encryption__config__pb2
from .....google.cloud.bigquery.v2 import error_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_error__pb2
from .....google.cloud.bigquery.v2 import job_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_job__config__pb2
from .....google.cloud.bigquery.v2 import job_creation_reason_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_job__creation__reason__pb2
from .....google.cloud.bigquery.v2 import job_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_job__reference__pb2
from .....google.cloud.bigquery.v2 import job_stats_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_job__stats__pb2
from .....google.cloud.bigquery.v2 import job_status_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_job__status__pb2
from .....google.cloud.bigquery.v2 import query_parameter_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_query__parameter__pb2
from .....google.cloud.bigquery.v2 import session_info_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_session__info__pb2
from .....google.cloud.bigquery.v2 import table_schema_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__schema__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/bigquery/v2/job.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/bigquery/v2/data_format_options.proto\x1a0google/cloud/bigquery/v2/dataset_reference.proto\x1a0google/cloud/bigquery/v2/encryption_config.proto\x1a$google/cloud/bigquery/v2/error.proto\x1a)google/cloud/bigquery/v2/job_config.proto\x1a2google/cloud/bigquery/v2/job_creation_reason.proto\x1a,google/cloud/bigquery/v2/job_reference.proto\x1a(google/cloud/bigquery/v2/job_stats.proto\x1a)google/cloud/bigquery/v2/job_status.proto\x1a.google/cloud/bigquery/v2/query_parameter.proto\x1a+google/cloud/bigquery/v2/session_info.proto\x1a+google/cloud/bigquery/v2/table_schema.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto"\x83\x04\n\x03Job\x12\x11\n\x04kind\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tself_link\x18\x04 \x01(\tB\x03\xe0A\x03\x12#\n\nuser_email\x18\x05 \x01(\tB\x03\xe0A\x03R\nuser_email\x12F\n\rconfiguration\x18\x06 \x01(\x0b2*.google.cloud.bigquery.v2.JobConfigurationB\x03\xe0A\x02\x12B\n\rjob_reference\x18\x07 \x01(\x0b2&.google.cloud.bigquery.v2.JobReferenceB\x03\xe0A\x01\x12@\n\nstatistics\x18\x08 \x01(\x0b2\'.google.cloud.bigquery.v2.JobStatisticsB\x03\xe0A\x03\x128\n\x06status\x18\t \x01(\x0b2#.google.cloud.bigquery.v2.JobStatusB\x03\xe0A\x03\x121\n\x11principal_subject\x18\r \x01(\tB\x03\xe0A\x03R\x11principal_subject\x12M\n\x13job_creation_reason\x18\x0e \x01(\x0b2+.google.cloud.bigquery.v2.JobCreationReasonB\x03\xe0A\x03"R\n\x10CancelJobRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x03 \x01(\t"M\n\x11JobCancelResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12*\n\x03job\x18\x02 \x01(\x0b2\x1d.google.cloud.bigquery.v2.Job"O\n\rGetJobRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x03 \x01(\t"R\n\x10InsertJobRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12*\n\x03job\x18\x03 \x01(\x0b2\x1d.google.cloud.bigquery.v2.Job"R\n\x10DeleteJobRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x03 \x01(\t"\x9b\x04\n\x0fListJobsRequest\x12\x12\n\nproject_id\x18\x01 \x01(\t\x12\x11\n\tall_users\x18\x02 \x01(\x08\x120\n\x0bmax_results\x18\x03 \x01(\x0b2\x1b.google.protobuf.Int32Value\x12\x19\n\x11min_creation_time\x18\x04 \x01(\x04\x127\n\x11max_creation_time\x18\x05 \x01(\x0b2\x1c.google.protobuf.UInt64Value\x12\x12\n\npage_token\x18\x06 \x01(\t\x12H\n\nprojection\x18\x07 \x01(\x0e24.google.cloud.bigquery.v2.ListJobsRequest.Projection\x12K\n\x0cstate_filter\x18\x08 \x03(\x0e25.google.cloud.bigquery.v2.ListJobsRequest.StateFilter\x12\x15\n\rparent_job_id\x18\t \x01(\t">\n\nProjection\x12\x0b\n\x07minimal\x10\x00\x12\x0b\n\x07MINIMAL\x10\x00\x12\x08\n\x04full\x10\x01\x12\x08\n\x04FULL\x10\x01\x1a\x02\x10\x01"Y\n\x0bStateFilter\x12\x08\n\x04done\x10\x00\x12\x08\n\x04DONE\x10\x00\x12\x0b\n\x07pending\x10\x01\x12\x0b\n\x07PENDING\x10\x01\x12\x0b\n\x07running\x10\x02\x12\x0b\n\x07RUNNING\x10\x02\x1a\x02\x10\x01"\xc0\x03\n\rListFormatJob\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12=\n\rjob_reference\x18\x03 \x01(\x0b2&.google.cloud.bigquery.v2.JobReference\x12\r\n\x05state\x18\x04 \x01(\t\x12:\n\x0cerror_result\x18\x05 \x01(\x0b2$.google.cloud.bigquery.v2.ErrorProto\x12@\n\nstatistics\x18\x06 \x01(\x0b2\'.google.cloud.bigquery.v2.JobStatisticsB\x03\xe0A\x03\x12F\n\rconfiguration\x18\x07 \x01(\x0b2*.google.cloud.bigquery.v2.JobConfigurationB\x03\xe0A\x02\x123\n\x06status\x18\x08 \x01(\x0b2#.google.cloud.bigquery.v2.JobStatus\x12\x1e\n\nuser_email\x18\t \x01(\tR\nuser_email\x12,\n\x11principal_subject\x18\n \x01(\tR\x11principal_subject"\x8a\x01\n\x07JobList\x12\x0c\n\x04etag\x18\x01 \x01(\t\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x125\n\x04jobs\x18\x04 \x03(\x0b2\'.google.cloud.bigquery.v2.ListFormatJob\x12\x13\n\x0bunreachable\x18\x05 \x03(\t"\xce\x02\n\x16GetQueryResultsRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x121\n\x0bstart_index\x18\x03 \x01(\x0b2\x1c.google.protobuf.UInt64Value\x12\x12\n\npage_token\x18\x04 \x01(\t\x121\n\x0bmax_results\x18\x05 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x120\n\ntimeout_ms\x18\x06 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x10\n\x08location\x18\x07 \x01(\t\x12H\n\x0eformat_options\x18\x08 \x01(\x0b2+.google.cloud.bigquery.v2.DataFormatOptionsB\x03\xe0A\x01"\xb1\x04\n\x17GetQueryResultsResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x04etag\x18\x02 \x01(\t\x125\n\x06schema\x18\x03 \x01(\x0b2%.google.cloud.bigquery.v2.TableSchema\x12=\n\rjob_reference\x18\x04 \x01(\x0b2&.google.cloud.bigquery.v2.JobReference\x120\n\ntotal_rows\x18\x05 \x01(\x0b2\x1c.google.protobuf.UInt64Value\x12\x12\n\npage_token\x18\x06 \x01(\t\x12%\n\x04rows\x18\x07 \x03(\x0b2\x17.google.protobuf.Struct\x12:\n\x15total_bytes_processed\x18\x08 \x01(\x0b2\x1b.google.protobuf.Int64Value\x120\n\x0cjob_complete\x18\t \x01(\x0b2\x1a.google.protobuf.BoolValue\x129\n\x06errors\x18\n \x03(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x03\xe0A\x03\x12-\n\tcache_hit\x18\x0b \x01(\x0b2\x1a.google.protobuf.BoolValue\x12?\n\x15num_dml_affected_rows\x18\x0c \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03"j\n\x10PostQueryRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12=\n\rquery_request\x18\x02 \x01(\x0b2&.google.cloud.bigquery.v2.QueryRequest"\x95\x0b\n\x0cQueryRequest\x12\x0c\n\x04kind\x18\x02 \x01(\t\x12\x12\n\x05query\x18\x03 \x01(\tB\x03\xe0A\x02\x126\n\x0bmax_results\x18\x04 \x01(\x0b2\x1c.google.protobuf.UInt32ValueB\x03\xe0A\x01\x12H\n\x0fdefault_dataset\x18\x05 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReferenceB\x03\xe0A\x01\x125\n\ntimeout_ms\x18\x06 \x01(\x0b2\x1c.google.protobuf.UInt32ValueB\x03\xe0A\x01\x12 \n\x0ejob_timeout_ms\x18\x1a \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x12\x1b\n\tmax_slots\x18\x1c \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12d\n$destination_encryption_configuration\x18\x1b \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfigurationB\x03\xe0A\x01\x12\x14\n\x07dry_run\x18\x07 \x01(\x08B\x03\xe0A\x01\x128\n\x0fuse_query_cache\x18\t \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x122\n\x0euse_legacy_sql\x18\n \x01(\x0b2\x1a.google.protobuf.BoolValue\x12\x16\n\x0eparameter_mode\x18\x0b \x01(\t\x12B\n\x10query_parameters\x18\x0c \x03(\x0b2(.google.cloud.bigquery.v2.QueryParameter\x12\x10\n\x08location\x18\r \x01(\t\x12H\n\x0eformat_options\x18\x0f \x01(\x0b2+.google.cloud.bigquery.v2.DataFormatOptionsB\x03\xe0A\x01\x12P\n\x15connection_properties\x18\x10 \x03(\x0b2,.google.cloud.bigquery.v2.ConnectionPropertyB\x03\xe0A\x01\x12G\n\x06labels\x18\x11 \x03(\x0b22.google.cloud.bigquery.v2.QueryRequest.LabelsEntryB\x03\xe0A\x01\x12>\n\x14maximum_bytes_billed\x18\x12 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x13 \x01(\tB\x03\xe0A\x01\x127\n\x0ecreate_session\x18\x14 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12V\n\x11job_creation_mode\x18\x16 \x01(\x0e26.google.cloud.bigquery.v2.QueryRequest.JobCreationModeB\x03\xe0A\x01\x12P\n\x0breservation\x18\x18 \x01(\tB6\xe0A\x01\xfaA0\n.bigqueryreservation.googleapis.com/ReservationH\x02\x88\x01\x01\x12&\n\x19write_incremental_results\x18\x19 \x01(\x08B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"j\n\x0fJobCreationMode\x12!\n\x1dJOB_CREATION_MODE_UNSPECIFIED\x10\x00\x12\x19\n\x15JOB_CREATION_REQUIRED\x10\x01\x12\x19\n\x15JOB_CREATION_OPTIONAL\x10\x02B\x11\n\x0f_job_timeout_msB\x0c\n\n_max_slotsB\x0e\n\x0c_reservation"\x88\x08\n\rQueryResponse\x12\x0c\n\x04kind\x18\x01 \x01(\t\x125\n\x06schema\x18\x02 \x01(\x0b2%.google.cloud.bigquery.v2.TableSchema\x12=\n\rjob_reference\x18\x03 \x01(\x0b2&.google.cloud.bigquery.v2.JobReference\x12M\n\x13job_creation_reason\x18\x0f \x01(\x0b2+.google.cloud.bigquery.v2.JobCreationReasonB\x03\xe0A\x01\x12\x10\n\x08query_id\x18\x0e \x01(\t\x12\x15\n\x08location\x18\x12 \x01(\tB\x03\xe0A\x03\x120\n\ntotal_rows\x18\x04 \x01(\x0b2\x1c.google.protobuf.UInt64Value\x12\x12\n\npage_token\x18\x05 \x01(\t\x12%\n\x04rows\x18\x06 \x03(\x0b2\x17.google.protobuf.Struct\x12:\n\x15total_bytes_processed\x18\x07 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12$\n\x12total_bytes_billed\x18\x10 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1f\n\rtotal_slot_ms\x18\x11 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x120\n\x0cjob_complete\x18\x08 \x01(\x0b2\x1a.google.protobuf.BoolValue\x129\n\x06errors\x18\t \x03(\x0b2$.google.cloud.bigquery.v2.ErrorProtoB\x03\xe0A\x03\x12-\n\tcache_hit\x18\n \x01(\x0b2\x1a.google.protobuf.BoolValue\x12?\n\x15num_dml_affected_rows\x18\x0b \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x03\x12@\n\x0csession_info\x18\x0c \x01(\x0b2%.google.cloud.bigquery.v2.SessionInfoB\x03\xe0A\x03\x12:\n\tdml_stats\x18\r \x01(\x0b2".google.cloud.bigquery.v2.DmlStatsB\x03\xe0A\x03\x12\x1f\n\rcreation_time\x18\x13 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1c\n\nstart_time\x18\x14 \x01(\x03B\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1a\n\x08end_time\x18\x15 \x01(\x03B\x03\xe0A\x03H\x04\x88\x01\x01B\x15\n\x13_total_bytes_billedB\x10\n\x0e_total_slot_msB\x10\n\x0e_creation_timeB\r\n\x0b_start_timeB\x0b\n\t_end_time2\xb1\x0b\n\nJobService\x12\xa9\x01\n\tCancelJob\x12*.google.cloud.bigquery.v2.CancelJobRequest\x1a+.google.cloud.bigquery.v2.JobCancelResponse"C\x82\xd3\xe4\x93\x02=";/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}/cancel\x12\x8e\x01\n\x06GetJob\x12\'.google.cloud.bigquery.v2.GetJobRequest\x1a\x1d.google.cloud.bigquery.v2.Job"<\x82\xd3\xe4\x93\x026\x124/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}\x12\x8e\x01\n\tInsertJob\x12*.google.cloud.bigquery.v2.InsertJobRequest\x1a\x1d.google.cloud.bigquery.v2.Job"6\x82\xd3\xe4\x93\x020")/bigquery/v2/projects/{project_id=*}/jobs:\x03job\x12\x94\x01\n\tDeleteJob\x12*.google.cloud.bigquery.v2.DeleteJobRequest\x1a\x16.google.protobuf.Empty"C\x82\xd3\xe4\x93\x02=*;/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}/delete\x12\x8b\x01\n\x08ListJobs\x12).google.cloud.bigquery.v2.ListJobsRequest\x1a!.google.cloud.bigquery.v2.JobList"1\x82\xd3\xe4\x93\x02+\x12)/bigquery/v2/projects/{project_id=*}/jobs\x12\xb7\x01\n\x0fGetQueryResults\x120.google.cloud.bigquery.v2.GetQueryResultsRequest\x1a1.google.cloud.bigquery.v2.GetQueryResultsResponse"?\x82\xd3\xe4\x93\x029\x127/bigquery/v2/projects/{project_id=*}/queries/{job_id=*}\x12\xa1\x01\n\x05Query\x12*.google.cloud.bigquery.v2.PostQueryRequest\x1a\'.google.cloud.bigquery.v2.QueryResponse"C\x82\xd3\xe4\x93\x02=",/bigquery/v2/projects/{project_id=*}/queries:\rquery_request\x1a\xd1\x02\xcaA\x17bigquery.googleapis.com\xd2A\xb3\x02https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/devstorage.full_control,https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/devstorage.read_writeBe\n\x1ccom.google.cloud.bigquery.v2B\x08JobProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.job_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x08JobProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_JOB'].fields_by_name['kind']._loaded_options = None
    _globals['_JOB'].fields_by_name['kind']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['etag']._loaded_options = None
    _globals['_JOB'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['id']._loaded_options = None
    _globals['_JOB'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['self_link']._loaded_options = None
    _globals['_JOB'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['user_email']._loaded_options = None
    _globals['_JOB'].fields_by_name['user_email']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['configuration']._loaded_options = None
    _globals['_JOB'].fields_by_name['configuration']._serialized_options = b'\xe0A\x02'
    _globals['_JOB'].fields_by_name['job_reference']._loaded_options = None
    _globals['_JOB'].fields_by_name['job_reference']._serialized_options = b'\xe0A\x01'
    _globals['_JOB'].fields_by_name['statistics']._loaded_options = None
    _globals['_JOB'].fields_by_name['statistics']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['status']._loaded_options = None
    _globals['_JOB'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['principal_subject']._loaded_options = None
    _globals['_JOB'].fields_by_name['principal_subject']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['job_creation_reason']._loaded_options = None
    _globals['_JOB'].fields_by_name['job_creation_reason']._serialized_options = b'\xe0A\x03'
    _globals['_CANCELJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_CANCELJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEJOBREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTJOBSREQUEST_PROJECTION']._loaded_options = None
    _globals['_LISTJOBSREQUEST_PROJECTION']._serialized_options = b'\x10\x01'
    _globals['_LISTJOBSREQUEST_STATEFILTER']._loaded_options = None
    _globals['_LISTJOBSREQUEST_STATEFILTER']._serialized_options = b'\x10\x01'
    _globals['_LISTFORMATJOB'].fields_by_name['statistics']._loaded_options = None
    _globals['_LISTFORMATJOB'].fields_by_name['statistics']._serialized_options = b'\xe0A\x03'
    _globals['_LISTFORMATJOB'].fields_by_name['configuration']._loaded_options = None
    _globals['_LISTFORMATJOB'].fields_by_name['configuration']._serialized_options = b'\xe0A\x02'
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['format_options']._loaded_options = None
    _globals['_GETQUERYRESULTSREQUEST'].fields_by_name['format_options']._serialized_options = b'\xe0A\x01'
    _globals['_GETQUERYRESULTSRESPONSE'].fields_by_name['errors']._loaded_options = None
    _globals['_GETQUERYRESULTSRESPONSE'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_GETQUERYRESULTSRESPONSE'].fields_by_name['num_dml_affected_rows']._loaded_options = None
    _globals['_GETQUERYRESULTSRESPONSE'].fields_by_name['num_dml_affected_rows']._serialized_options = b'\xe0A\x03'
    _globals['_POSTQUERYREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_POSTQUERYREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYREQUEST_LABELSENTRY']._loaded_options = None
    _globals['_QUERYREQUEST_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_QUERYREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYREQUEST'].fields_by_name['max_results']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['max_results']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['default_dataset']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['default_dataset']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['timeout_ms']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['timeout_ms']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['job_timeout_ms']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['job_timeout_ms']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['max_slots']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['max_slots']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['destination_encryption_configuration']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['destination_encryption_configuration']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['dry_run']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['dry_run']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['use_query_cache']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['use_query_cache']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['format_options']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['format_options']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['connection_properties']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['connection_properties']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['labels']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['maximum_bytes_billed']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['maximum_bytes_billed']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['create_session']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['create_session']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['job_creation_mode']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['job_creation_mode']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYREQUEST'].fields_by_name['reservation']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['reservation']._serialized_options = b'\xe0A\x01\xfaA0\n.bigqueryreservation.googleapis.com/Reservation'
    _globals['_QUERYREQUEST'].fields_by_name['write_incremental_results']._loaded_options = None
    _globals['_QUERYREQUEST'].fields_by_name['write_incremental_results']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYRESPONSE'].fields_by_name['job_creation_reason']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['job_creation_reason']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYRESPONSE'].fields_by_name['location']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['location']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['total_bytes_billed']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['total_bytes_billed']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['total_slot_ms']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['total_slot_ms']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['errors']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['num_dml_affected_rows']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['num_dml_affected_rows']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['session_info']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['session_info']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['dml_stats']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['dml_stats']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['creation_time']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['start_time']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_QUERYRESPONSE'].fields_by_name['end_time']._loaded_options = None
    _globals['_QUERYRESPONSE'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOBSERVICE']._loaded_options = None
    _globals['_JOBSERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\xb3\x02https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only,https://www.googleapis.com/auth/devstorage.full_control,https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/devstorage.read_write'
    _globals['_JOBSERVICE'].methods_by_name['CancelJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['CancelJob']._serialized_options = b'\x82\xd3\xe4\x93\x02=";/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}/cancel'
    _globals['_JOBSERVICE'].methods_by_name['GetJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetJob']._serialized_options = b'\x82\xd3\xe4\x93\x026\x124/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}'
    _globals['_JOBSERVICE'].methods_by_name['InsertJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['InsertJob']._serialized_options = b'\x82\xd3\xe4\x93\x020")/bigquery/v2/projects/{project_id=*}/jobs:\x03job'
    _globals['_JOBSERVICE'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['DeleteJob']._serialized_options = b'\x82\xd3\xe4\x93\x02=*;/bigquery/v2/projects/{project_id=*}/jobs/{job_id=*}/delete'
    _globals['_JOBSERVICE'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\x82\xd3\xe4\x93\x02+\x12)/bigquery/v2/projects/{project_id=*}/jobs'
    _globals['_JOBSERVICE'].methods_by_name['GetQueryResults']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['GetQueryResults']._serialized_options = b'\x82\xd3\xe4\x93\x029\x127/bigquery/v2/projects/{project_id=*}/queries/{job_id=*}'
    _globals['_JOBSERVICE'].methods_by_name['Query']._loaded_options = None
    _globals['_JOBSERVICE'].methods_by_name['Query']._serialized_options = b'\x82\xd3\xe4\x93\x02=",/bigquery/v2/projects/{project_id=*}/queries:\rquery_request'
    _globals['_JOB']._serialized_start = 825
    _globals['_JOB']._serialized_end = 1340
    _globals['_CANCELJOBREQUEST']._serialized_start = 1342
    _globals['_CANCELJOBREQUEST']._serialized_end = 1424
    _globals['_JOBCANCELRESPONSE']._serialized_start = 1426
    _globals['_JOBCANCELRESPONSE']._serialized_end = 1503
    _globals['_GETJOBREQUEST']._serialized_start = 1505
    _globals['_GETJOBREQUEST']._serialized_end = 1584
    _globals['_INSERTJOBREQUEST']._serialized_start = 1586
    _globals['_INSERTJOBREQUEST']._serialized_end = 1668
    _globals['_DELETEJOBREQUEST']._serialized_start = 1670
    _globals['_DELETEJOBREQUEST']._serialized_end = 1752
    _globals['_LISTJOBSREQUEST']._serialized_start = 1755
    _globals['_LISTJOBSREQUEST']._serialized_end = 2294
    _globals['_LISTJOBSREQUEST_PROJECTION']._serialized_start = 2141
    _globals['_LISTJOBSREQUEST_PROJECTION']._serialized_end = 2203
    _globals['_LISTJOBSREQUEST_STATEFILTER']._serialized_start = 2205
    _globals['_LISTJOBSREQUEST_STATEFILTER']._serialized_end = 2294
    _globals['_LISTFORMATJOB']._serialized_start = 2297
    _globals['_LISTFORMATJOB']._serialized_end = 2745
    _globals['_JOBLIST']._serialized_start = 2748
    _globals['_JOBLIST']._serialized_end = 2886
    _globals['_GETQUERYRESULTSREQUEST']._serialized_start = 2889
    _globals['_GETQUERYRESULTSREQUEST']._serialized_end = 3223
    _globals['_GETQUERYRESULTSRESPONSE']._serialized_start = 3226
    _globals['_GETQUERYRESULTSRESPONSE']._serialized_end = 3787
    _globals['_POSTQUERYREQUEST']._serialized_start = 3789
    _globals['_POSTQUERYREQUEST']._serialized_end = 3895
    _globals['_QUERYREQUEST']._serialized_start = 3898
    _globals['_QUERYREQUEST']._serialized_end = 5327
    _globals['_QUERYREQUEST_LABELSENTRY']._serialized_start = 5125
    _globals['_QUERYREQUEST_LABELSENTRY']._serialized_end = 5170
    _globals['_QUERYREQUEST_JOBCREATIONMODE']._serialized_start = 5172
    _globals['_QUERYREQUEST_JOBCREATIONMODE']._serialized_end = 5278
    _globals['_QUERYRESPONSE']._serialized_start = 5330
    _globals['_QUERYRESPONSE']._serialized_end = 6362
    _globals['_JOBSERVICE']._serialized_start = 6365
    _globals['_JOBSERVICE']._serialized_end = 7822