"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/batch/v1alpha/batch.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.batch.v1alpha import job_pb2 as google_dot_cloud_dot_batch_dot_v1alpha_dot_job__pb2
from .....google.cloud.batch.v1alpha import resource_allowance_pb2 as google_dot_cloud_dot_batch_dot_v1alpha_dot_resource__allowance__pb2
from .....google.cloud.batch.v1alpha import task_pb2 as google_dot_cloud_dot_batch_dot_v1alpha_dot_task__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/batch/v1alpha/batch.proto\x12\x1agoogle.cloud.batch.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a$google/cloud/batch/v1alpha/job.proto\x1a3google/cloud/batch/v1alpha/resource_allowance.proto\x1a%google/cloud/batch/v1alpha/task.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa0\x01\n\x10CreateJobRequest\x120\n\x06parent\x18\x01 \x01(\tB \xe0A\x02\xfaA\x1a\x12\x18batch.googleapis.com/Job\x12\x0e\n\x06job_id\x18\x02 \x01(\t\x121\n\x03job\x18\x03 \x01(\x0b2\x1f.google.cloud.batch.v1alpha.JobB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"?\n\rGetJobRequest\x12.\n\x04name\x18\x01 \x01(\tB \xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job"N\n\x10DeleteJobRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x06reason\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"c\n\x10CancelJobRequest\x12.\n\x04name\x18\x01 \x01(\tB \xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x13\n\x11CancelJobResponse"\x9c\x01\n\x10UpdateJobRequest\x121\n\x03job\x18\x01 \x01(\x0b2\x1f.google.cloud.batch.v1alpha.JobB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"o\n\x0fListJobsRequest\x12\x0e\n\x06parent\x18\x01 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"o\n\x10ListJobsResponse\x12-\n\x04jobs\x18\x01 \x03(\x0b2\x1f.google.cloud.batch.v1alpha.Job\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\x93\x01\n\x10ListTasksRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ebatch.googleapis.com/TaskGroup\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"r\n\x11ListTasksResponse\x12/\n\x05tasks\x18\x01 \x03(\x0b2 .google.cloud.batch.v1alpha.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"A\n\x0eGetTaskRequest\x12/\n\x04name\x18\x01 \x01(\tB!\xe0A\x02\xfaA\x1b\n\x19batch.googleapis.com/Task"\xf0\x01\n\x1eCreateResourceAllowanceRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&batch.googleapis.com/ResourceAllowance\x12\x1d\n\x15resource_allowance_id\x18\x02 \x01(\t\x12N\n\x12resource_allowance\x18\x03 \x01(\x0b2-.google.cloud.batch.v1alpha.ResourceAllowanceB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"[\n\x1bGetResourceAllowanceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&batch.googleapis.com/ResourceAllowance"\x94\x01\n\x1eDeleteResourceAllowanceRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&batch.googleapis.com/ResourceAllowance\x12\x13\n\x06reason\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x90\x01\n\x1dListResourceAllowancesRequest\x12>\n\x06parent\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\x12&batch.googleapis.com/ResourceAllowance\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x9a\x01\n\x1eListResourceAllowancesResponse\x12J\n\x13resource_allowances\x18\x01 \x03(\x0b2-.google.cloud.batch.v1alpha.ResourceAllowance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"\xc7\x01\n\x1eUpdateResourceAllowanceRequest\x12N\n\x12resource_allowance\x18\x01 \x01(\x0b2-.google.cloud.batch.v1alpha.ResourceAllowanceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x1f\n\nrequest_id\x18\x03 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01"\x80\x02\n\x11OperationMetadata\x124\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x05 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x06 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x07 \x01(\tB\x03\xe0A\x032\xa4\x16\n\x0cBatchService\x12\xaa\x01\n\tCreateJob\x12,.google.cloud.batch.v1alpha.CreateJobRequest\x1a\x1f.google.cloud.batch.v1alpha.Job"N\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x024"-/v1alpha/{parent=projects/*/locations/*}/jobs:\x03job\x12\x92\x01\n\x06GetJob\x12).google.cloud.batch.v1alpha.GetJobRequest\x1a\x1f.google.cloud.batch.v1alpha.Job"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1alpha/{name=projects/*/locations/*/jobs/*}\x12\xdf\x01\n\tDeleteJob\x12,.google.cloud.batch.v1alpha.DeleteJobRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaAE\n\x15google.protobuf.Empty\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1alpha/{name=projects/*/locations/*/jobs/*}\x12\x80\x02\n\tCancelJob\x12,.google.cloud.batch.v1alpha.CancelJobRequest\x1a\x1d.google.longrunning.Operation"\xa5\x01\xcaA\\\n,google.cloud.batch.v1alpha.CancelJobResponse\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1alpha/{name=projects/*/locations/*/jobs/*}:cancel:\x01*\x12\xac\x01\n\tUpdateJob\x12,.google.cloud.batch.v1alpha.UpdateJobRequest\x1a\x1f.google.cloud.batch.v1alpha.Job"P\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x02821/v1alpha/{job.name=projects/*/locations/*/jobs/*}:\x03job\x12\xa5\x01\n\x08ListJobs\x12+.google.cloud.batch.v1alpha.ListJobsRequest\x1a,.google.cloud.batch.v1alpha.ListJobsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1alpha/{parent=projects/*/locations/*}/jobs\x12\xaa\x01\n\x07GetTask\x12*.google.cloud.batch.v1alpha.GetTaskRequest\x1a .google.cloud.batch.v1alpha.Task"Q\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1alpha/{name=projects/*/locations/*/jobs/*/taskGroups/*/tasks/*}\x12\xbd\x01\n\tListTasks\x12,.google.cloud.batch.v1alpha.ListTasksRequest\x1a-.google.cloud.batch.v1alpha.ListTasksResponse"S\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1alpha/{parent=projects/*/locations/*/jobs/*/taskGroups/*}/tasks\x12\x90\x02\n\x17CreateResourceAllowance\x12:.google.cloud.batch.v1alpha.CreateResourceAllowanceRequest\x1a-.google.cloud.batch.v1alpha.ResourceAllowance"\x89\x01\xdaA/parent,resource_allowance,resource_allowance_id\x82\xd3\xe4\x93\x02Q";/v1alpha/{parent=projects/*/locations/*}/resourceAllowances:\x12resource_allowance\x12\xca\x01\n\x14GetResourceAllowance\x127.google.cloud.batch.v1alpha.GetResourceAllowanceRequest\x1a-.google.cloud.batch.v1alpha.ResourceAllowance"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha/{name=projects/*/locations/*/resourceAllowances/*}\x12\x89\x02\n\x17DeleteResourceAllowance\x12:.google.cloud.batch.v1alpha.DeleteResourceAllowanceRequest\x1a\x1d.google.longrunning.Operation"\x92\x01\xcaAE\n\x15google.protobuf.Empty\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha/{name=projects/*/locations/*/resourceAllowances/*}\x12\xdd\x01\n\x16ListResourceAllowances\x129.google.cloud.batch.v1alpha.ListResourceAllowancesRequest\x1a:.google.cloud.batch.v1alpha.ListResourceAllowancesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha/{parent=projects/*/locations/*}/resourceAllowances\x12\x92\x02\n\x17UpdateResourceAllowance\x12:.google.cloud.batch.v1alpha.UpdateResourceAllowanceRequest\x1a-.google.cloud.batch.v1alpha.ResourceAllowance"\x8b\x01\xdaA\x1eresource_allowance,update_mask\x82\xd3\xe4\x93\x02d2N/v1alpha/{resource_allowance.name=projects/*/locations/*/resourceAllowances/*}:\x12resource_allowance\x1aH\xcaA\x14batch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xc4\x01\n\x1ecom.google.cloud.batch.v1alphaB\nBatchProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1alpha.batch_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.batch.v1alphaB\nBatchProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alpha'
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1a\x12\x18batch.googleapis.com/Job'
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_GETJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job'
    _globals['_DELETEJOBREQUEST'].fields_by_name['reason']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['reason']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_CANCELJOBREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1a\n\x18batch.googleapis.com/Job'
    _globals['_CANCELJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CANCELJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._loaded_options = None
    _globals['_UPDATEJOBREQUEST'].fields_by_name['job']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEJOBREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEJOBREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEJOBREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEJOBREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTJOBSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \n\x1ebatch.googleapis.com/TaskGroup'
    _globals['_GETTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA\x1b\n\x19batch.googleapis.com/Task'
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&batch.googleapis.com/ResourceAllowance'
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['resource_allowance']._loaded_options = None
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['resource_allowance']._serialized_options = b'\xe0A\x02'
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GETRESOURCEALLOWANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRESOURCEALLOWANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&batch.googleapis.com/ResourceAllowance'
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&batch.googleapis.com/ResourceAllowance'
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['reason']._loaded_options = None
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['reason']._serialized_options = b'\xe0A\x01'
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&batch.googleapis.com/ResourceAllowance'
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTRESOURCEALLOWANCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['resource_allowance']._loaded_options = None
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['resource_allowance']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATERESOURCEALLOWANCEREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_OPERATIONMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_BATCHSERVICE']._loaded_options = None
    _globals['_BATCHSERVICE']._serialized_options = b'\xcaA\x14batch.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BATCHSERVICE'].methods_by_name['CreateJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['CreateJob']._serialized_options = b'\xdaA\x11parent,job,job_id\x82\xd3\xe4\x93\x024"-/v1alpha/{parent=projects/*/locations/*}/jobs:\x03job'
    _globals['_BATCHSERVICE'].methods_by_name['GetJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['GetJob']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1alpha/{name=projects/*/locations/*/jobs/*}'
    _globals['_BATCHSERVICE'].methods_by_name['DeleteJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['DeleteJob']._serialized_options = b'\xcaAE\n\x15google.protobuf.Empty\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1alpha/{name=projects/*/locations/*/jobs/*}'
    _globals['_BATCHSERVICE'].methods_by_name['CancelJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['CancelJob']._serialized_options = b'\xcaA\\\n,google.cloud.batch.v1alpha.CancelJobResponse\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1alpha/{name=projects/*/locations/*/jobs/*}:cancel:\x01*'
    _globals['_BATCHSERVICE'].methods_by_name['UpdateJob']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['UpdateJob']._serialized_options = b'\xdaA\x0fjob,update_mask\x82\xd3\xe4\x93\x02821/v1alpha/{job.name=projects/*/locations/*/jobs/*}:\x03job'
    _globals['_BATCHSERVICE'].methods_by_name['ListJobs']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['ListJobs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1alpha/{parent=projects/*/locations/*}/jobs'
    _globals['_BATCHSERVICE'].methods_by_name['GetTask']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['GetTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02D\x12B/v1alpha/{name=projects/*/locations/*/jobs/*/taskGroups/*/tasks/*}'
    _globals['_BATCHSERVICE'].methods_by_name['ListTasks']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['ListTasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02D\x12B/v1alpha/{parent=projects/*/locations/*/jobs/*/taskGroups/*}/tasks'
    _globals['_BATCHSERVICE'].methods_by_name['CreateResourceAllowance']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['CreateResourceAllowance']._serialized_options = b'\xdaA/parent,resource_allowance,resource_allowance_id\x82\xd3\xe4\x93\x02Q";/v1alpha/{parent=projects/*/locations/*}/resourceAllowances:\x12resource_allowance'
    _globals['_BATCHSERVICE'].methods_by_name['GetResourceAllowance']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['GetResourceAllowance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1alpha/{name=projects/*/locations/*/resourceAllowances/*}'
    _globals['_BATCHSERVICE'].methods_by_name['DeleteResourceAllowance']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['DeleteResourceAllowance']._serialized_options = b'\xcaAE\n\x15google.protobuf.Empty\x12,google.cloud.batch.v1alpha.OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1alpha/{name=projects/*/locations/*/resourceAllowances/*}'
    _globals['_BATCHSERVICE'].methods_by_name['ListResourceAllowances']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['ListResourceAllowances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1alpha/{parent=projects/*/locations/*}/resourceAllowances'
    _globals['_BATCHSERVICE'].methods_by_name['UpdateResourceAllowance']._loaded_options = None
    _globals['_BATCHSERVICE'].methods_by_name['UpdateResourceAllowance']._serialized_options = b'\xdaA\x1eresource_allowance,update_mask\x82\xd3\xe4\x93\x02d2N/v1alpha/{resource_allowance.name=projects/*/locations/*/resourceAllowances/*}:\x12resource_allowance'
    _globals['_CREATEJOBREQUEST']._serialized_start = 478
    _globals['_CREATEJOBREQUEST']._serialized_end = 638
    _globals['_GETJOBREQUEST']._serialized_start = 640
    _globals['_GETJOBREQUEST']._serialized_end = 703
    _globals['_DELETEJOBREQUEST']._serialized_start = 705
    _globals['_DELETEJOBREQUEST']._serialized_end = 783
    _globals['_CANCELJOBREQUEST']._serialized_start = 785
    _globals['_CANCELJOBREQUEST']._serialized_end = 884
    _globals['_CANCELJOBRESPONSE']._serialized_start = 886
    _globals['_CANCELJOBRESPONSE']._serialized_end = 905
    _globals['_UPDATEJOBREQUEST']._serialized_start = 908
    _globals['_UPDATEJOBREQUEST']._serialized_end = 1064
    _globals['_LISTJOBSREQUEST']._serialized_start = 1066
    _globals['_LISTJOBSREQUEST']._serialized_end = 1177
    _globals['_LISTJOBSRESPONSE']._serialized_start = 1179
    _globals['_LISTJOBSRESPONSE']._serialized_end = 1290
    _globals['_LISTTASKSREQUEST']._serialized_start = 1293
    _globals['_LISTTASKSREQUEST']._serialized_end = 1440
    _globals['_LISTTASKSRESPONSE']._serialized_start = 1442
    _globals['_LISTTASKSRESPONSE']._serialized_end = 1556
    _globals['_GETTASKREQUEST']._serialized_start = 1558
    _globals['_GETTASKREQUEST']._serialized_end = 1623
    _globals['_CREATERESOURCEALLOWANCEREQUEST']._serialized_start = 1626
    _globals['_CREATERESOURCEALLOWANCEREQUEST']._serialized_end = 1866
    _globals['_GETRESOURCEALLOWANCEREQUEST']._serialized_start = 1868
    _globals['_GETRESOURCEALLOWANCEREQUEST']._serialized_end = 1959
    _globals['_DELETERESOURCEALLOWANCEREQUEST']._serialized_start = 1962
    _globals['_DELETERESOURCEALLOWANCEREQUEST']._serialized_end = 2110
    _globals['_LISTRESOURCEALLOWANCESREQUEST']._serialized_start = 2113
    _globals['_LISTRESOURCEALLOWANCESREQUEST']._serialized_end = 2257
    _globals['_LISTRESOURCEALLOWANCESRESPONSE']._serialized_start = 2260
    _globals['_LISTRESOURCEALLOWANCESRESPONSE']._serialized_end = 2414
    _globals['_UPDATERESOURCEALLOWANCEREQUEST']._serialized_start = 2417
    _globals['_UPDATERESOURCEALLOWANCEREQUEST']._serialized_end = 2616
    _globals['_OPERATIONMETADATA']._serialized_start = 2619
    _globals['_OPERATIONMETADATA']._serialized_end = 2875
    _globals['_BATCHSERVICE']._serialized_start = 2878
    _globals['_BATCHSERVICE']._serialized_end = 5730