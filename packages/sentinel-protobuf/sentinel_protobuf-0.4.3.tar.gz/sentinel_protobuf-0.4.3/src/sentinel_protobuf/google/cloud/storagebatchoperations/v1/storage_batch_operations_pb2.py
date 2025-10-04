"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/storagebatchoperations/v1/storage_batch_operations.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.storagebatchoperations.v1 import storage_batch_operations_types_pb2 as google_dot_cloud_dot_storagebatchoperations_dot_v1_dot_storage__batch__operations__types__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/cloud/storagebatchoperations/v1/storage_batch_operations.proto\x12&google.cloud.storagebatchoperations.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aKgoogle/cloud/storagebatchoperations/v1/storage_batch_operations_types.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xb1\x01\n\x0fListJobsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)storagebatchoperations.googleapis.com/Job\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"{\n\x10ListJobsResponse\x129\n\x04jobs\x18\x01 \x03(\x0b2+.google.cloud.storagebatchoperations.v1.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"P\n\rGetJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job"\xc2\x01\n\x10CreateJobRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\x12)storagebatchoperations.googleapis.com/Job\x12\x13\n\x06job_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12=\n\x03job\x18\x03 \x01(\x0b2+.google.cloud.storagebatchoperations.v1.JobB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"l\n\x10CancelJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"l\n\x10DeleteJobRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\x13\n\x11CancelJobResponse"\x92\x02\n\x11OperationMetadata\x12\x16\n\toperation\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x08 \x01(\tB\x03\xe0A\x03\x12=\n\x03job\x18\n \x01(\x0b2+.google.cloud.storagebatchoperations.v1.JobB\x03\xe0A\x032\x82\x08\n\x16StorageBatchOperations\x12\xb8\x01\n\x08ListJobs\x127.google.cloud.storagebatchoperations.v1.ListJobsRequest\x1a8.google.cloud.storagebatchoperations.v1.ListJobsResponse"9\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs\x12\xa5\x01\n\x06GetJob\x125.google.cloud.storagebatchoperations.v1.GetJobRequest\x1a+.google.cloud.storagebatchoperations.v1.Job"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}\x12\xca\x01\n\tCreateJob\x128.google.cloud.storagebatchoperations.v1.CreateJobRequest\x1a\x1d.google.longrunning.Operation"d\xcaA\x18\n\x03Job\x12\x11OperationMetadata\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job\x12\x96\x01\n\tDeleteJob\x128.google.cloud.storagebatchoperations.v1.DeleteJobRequest\x1a\x16.google.protobuf.Empty"7\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}\x12\xc3\x01\n\tCancelJob\x128.google.cloud.storagebatchoperations.v1.CancelJobRequest\x1a9.google.cloud.storagebatchoperations.v1.CancelJobResponse"A\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/jobs/*}:cancel:\x01*\x1aY\xcaA%storagebatchoperations.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xad\x02\n*com.google.cloud.storagebatchoperations.v1B\x1bStorageBatchOperationsProtoP\x01Zbcloud.google.com/go/storagebatchoperations/apiv1/storagebatchoperationspb;storagebatchoperationspb\xaa\x02&Google.Cloud.StorageBatchOperations.V1\xca\x02&Google\\Cloud\\StorageBatchOperations\\V1\xea\x02)Google::Cloud::StorageBatchOperations::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.storagebatchoperations.v1.storage_batch_operations_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.storagebatchoperations.v1B\x1bStorageBatchOperationsProtoP\x01Zbcloud.google.com/go/storagebatchoperations/apiv1/storagebatchoperationspb;storagebatchoperationspb\xaa\x02&Google.Cloud.StorageBatchOperations.V1\xca\x02&Google\\Cloud\\StorageBatchOperations\\V1\xea\x02)Google::Cloud::StorageBatchOperations::V1'
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)storagebatchoperations.googleapis.com/Job'
    _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\x12)storagebatchoperations.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job_id']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job'
    _globals['_CANCELJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)storagebatchoperations.googleapis.com/Job'
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['operation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['operation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['job']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['job']._serialized_options = b'\xe0A\x03'
    _globals['_STORAGEBATCHOPERATIONS']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS']._serialized_options = b'\xcaA%storagebatchoperations.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02*\x12(/v1/{parent=projects/*/locations/*}/jobs'
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['GetJob']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['CreateJob']._serialized_options = b'\xcaA\x18\n\x03Job\x12\x11OperationMetadata\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x02/"(/v1/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['DeleteJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02**(/v1/{name=projects/*/locations/*/jobs/*}'
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['CancelJob']._loaded_options = None
    _globals['_STORAGEBATCHOPERATIONS'].methods_by_name['CancelJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024"//v1/{name=projects/*/locations/*/jobs/*}:cancel:\x01*'
    _globals['_LISTJOBSREQUEST']._serialized_start = 405
    _globals['_LISTJOBSREQUEST']._serialized_end = 582
    _globals['_LISTJOBSRESPONSE']._serialized_start = 584
    _globals['_LISTJOBSRESPONSE']._serialized_end = 707
    _globals['_GETJOBREQUEST']._serialized_start = 709
    _globals['_GETJOBREQUEST']._serialized_end = 789
    _globals['_CREATEJOBREQUEST']._serialized_start = 792
    _globals['_CREATEJOBREQUEST']._serialized_end = 986
    _globals['_CANCELJOBREQUEST']._serialized_start = 988
    _globals['_CANCELJOBREQUEST']._serialized_end = 1096
    _globals['_DELETEJOBREQUEST']._serialized_start = 1098
    _globals['_DELETEJOBREQUEST']._serialized_end = 1206
    _globals['_CANCELJOBRESPONSE']._serialized_start = 1208
    _globals['_CANCELJOBRESPONSE']._serialized_end = 1227
    _globals['_OPERATIONMETADATA']._serialized_start = 1230
    _globals['_OPERATIONMETADATA']._serialized_end = 1504
    _globals['_STORAGEBATCHOPERATIONS']._serialized_start = 1507
    _globals['_STORAGEBATCHOPERATIONS']._serialized_end = 2533