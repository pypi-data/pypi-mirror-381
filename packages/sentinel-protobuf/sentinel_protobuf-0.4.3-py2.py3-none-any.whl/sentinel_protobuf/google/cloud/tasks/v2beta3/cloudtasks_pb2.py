"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/tasks/v2beta3/cloudtasks.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.tasks.v2beta3 import queue_pb2 as google_dot_cloud_dot_tasks_dot_v2beta3_dot_queue__pb2
from .....google.cloud.tasks.v2beta3 import task_pb2 as google_dot_cloud_dot_tasks_dot_v2beta3_dot_task__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/tasks/v2beta3/cloudtasks.proto\x12\x1agoogle.cloud.tasks.v2beta3\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/tasks/v2beta3/queue.proto\x1a%google/cloud/tasks/v2beta3/task.proto\x1a\x1egoogle/iam/v1/iam_policy.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb7\x01\n\x11ListQueuesRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"`\n\x12ListQueuesResponse\x121\n\x06queues\x18\x01 \x03(\x0b2!.google.cloud.tasks.v2beta3.Queue\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"|\n\x0fGetQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue\x122\n\tread_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\x84\x01\n\x12CreateQueueRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue\x125\n\x05queue\x18\x02 \x01(\x0b2!.google.cloud.tasks.v2beta3.QueueB\x03\xe0A\x02"|\n\x12UpdateQueueRequest\x125\n\x05queue\x18\x01 \x01(\x0b2!.google.cloud.tasks.v2beta3.QueueB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"K\n\x12DeleteQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"J\n\x11PurgeQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"J\n\x11PauseQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"K\n\x12ResumeQueueRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue"\xaf\x01\n\x10ListTasksRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task\x12<\n\rresponse_view\x18\x02 \x01(\x0e2%.google.cloud.tasks.v2beta3.Task.View\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"]\n\x11ListTasksResponse\x12/\n\x05tasks\x18\x01 \x03(\x0b2 .google.cloud.tasks.v2beta3.Task\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x84\x01\n\x0eGetTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task\x12<\n\rresponse_view\x18\x02 \x01(\x0e2%.google.cloud.tasks.v2beta3.Task.View"\xbe\x01\n\x11CreateTaskRequest\x126\n\x06parent\x18\x01 \x01(\tB&\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task\x123\n\x04task\x18\x02 \x01(\x0b2 .google.cloud.tasks.v2beta3.TaskB\x03\xe0A\x02\x12<\n\rresponse_view\x18\x03 \x01(\x0e2%.google.cloud.tasks.v2beta3.Task.View"I\n\x11DeleteTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task"\x84\x01\n\x0eRunTaskRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task\x12<\n\rresponse_view\x18\x02 \x01(\x0e2%.google.cloud.tasks.v2beta3.Task.View2\xa5\x16\n\nCloudTasks\x12\xad\x01\n\nListQueues\x12-.google.cloud.tasks.v2beta3.ListQueuesRequest\x1a..google.cloud.tasks.v2beta3.ListQueuesResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v2beta3/{parent=projects/*/locations/*}/queues\x12\x9a\x01\n\x08GetQueue\x12+.google.cloud.tasks.v2beta3.GetQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue">\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v2beta3/{name=projects/*/locations/*/queues/*}\x12\xaf\x01\n\x0bCreateQueue\x12..google.cloud.tasks.v2beta3.CreateQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue"M\xdaA\x0cparent,queue\x82\xd3\xe4\x93\x028"//v2beta3/{parent=projects/*/locations/*}/queues:\x05queue\x12\xba\x01\n\x0bUpdateQueue\x12..google.cloud.tasks.v2beta3.UpdateQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue"X\xdaA\x11queue,update_mask\x82\xd3\xe4\x93\x02>25/v2beta3/{queue.name=projects/*/locations/*/queues/*}:\x05queue\x12\x95\x01\n\x0bDeleteQueue\x12..google.cloud.tasks.v2beta3.DeleteQueueRequest\x1a\x16.google.protobuf.Empty">\xdaA\x04name\x82\xd3\xe4\x93\x021*//v2beta3/{name=projects/*/locations/*/queues/*}\x12\xa7\x01\n\nPurgeQueue\x12-.google.cloud.tasks.v2beta3.PurgeQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue"G\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v2beta3/{name=projects/*/locations/*/queues/*}:purge:\x01*\x12\xa7\x01\n\nPauseQueue\x12-.google.cloud.tasks.v2beta3.PauseQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue"G\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v2beta3/{name=projects/*/locations/*/queues/*}:pause:\x01*\x12\xaa\x01\n\x0bResumeQueue\x12..google.cloud.tasks.v2beta3.ResumeQueueRequest\x1a!.google.cloud.tasks.v2beta3.Queue"H\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v2beta3/{name=projects/*/locations/*/queues/*}:resume:\x01*\x12\xa1\x01\n\x0cGetIamPolicy\x12".google.iam.v1.GetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"V\xdaA\x08resource\x82\xd3\xe4\x93\x02E"@/v2beta3/{resource=projects/*/locations/*/queues/*}:getIamPolicy:\x01*\x12\xa8\x01\n\x0cSetIamPolicy\x12".google.iam.v1.SetIamPolicyRequest\x1a\x15.google.iam.v1.Policy"]\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02E"@/v2beta3/{resource=projects/*/locations/*/queues/*}:setIamPolicy:\x01*\x12\xd3\x01\n\x12TestIamPermissions\x12(.google.iam.v1.TestIamPermissionsRequest\x1a).google.iam.v1.TestIamPermissionsResponse"h\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02K"F/v2beta3/{resource=projects/*/locations/*/queues/*}:testIamPermissions:\x01*\x12\xb2\x01\n\tListTasks\x12,.google.cloud.tasks.v2beta3.ListTasksRequest\x1a-.google.cloud.tasks.v2beta3.ListTasksResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v2beta3/{parent=projects/*/locations/*/queues/*}/tasks\x12\x9f\x01\n\x07GetTask\x12*.google.cloud.tasks.v2beta3.GetTaskRequest\x1a .google.cloud.tasks.v2beta3.Task"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}\x12\xaf\x01\n\nCreateTask\x12-.google.cloud.tasks.v2beta3.CreateTaskRequest\x1a .google.cloud.tasks.v2beta3.Task"P\xdaA\x0bparent,task\x82\xd3\xe4\x93\x02<"7/v2beta3/{parent=projects/*/locations/*/queues/*}/tasks:\x01*\x12\x9b\x01\n\nDeleteTask\x12-.google.cloud.tasks.v2beta3.DeleteTaskRequest\x1a\x16.google.protobuf.Empty"F\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}\x12\xa6\x01\n\x07RunTask\x12*.google.cloud.tasks.v2beta3.RunTaskRequest\x1a .google.cloud.tasks.v2beta3.Task"M\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}:run:\x01*\x1aM\xcaA\x19cloudtasks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x01\n\x1ecom.google.cloud.tasks.v2beta3B\x0fCloudTasksProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta3/cloudtaskspb;cloudtaskspb\xa2\x02\x05TASKSb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.tasks.v2beta3.cloudtasks_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.tasks.v2beta3B\x0fCloudTasksProtoP\x01ZCcloud.google.com/go/cloudtasks/apiv2beta3/cloudtaskspb;cloudtaskspb\xa2\x02\x05TASKS'
    _globals['_LISTQUEUESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTQUEUESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue'
    _globals['_LISTQUEUESREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTQUEUESREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_GETQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_GETQUEUEREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_GETQUEUEREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\x12\x1fcloudtasks.googleapis.com/Queue'
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['queue']._loaded_options = None
    _globals['_CREATEQUEUEREQUEST'].fields_by_name['queue']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEQUEUEREQUEST'].fields_by_name['queue']._loaded_options = None
    _globals['_UPDATEQUEUEREQUEST'].fields_by_name['queue']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_PURGEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PURGEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_PAUSEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_PAUSEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_RESUMEQUEUEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESUMEQUEUEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fcloudtasks.googleapis.com/Queue'
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTTASKSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task'
    _globals['_GETTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA \x12\x1ecloudtasks.googleapis.com/Task'
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._loaded_options = None
    _globals['_CREATETASKREQUEST'].fields_by_name['task']._serialized_options = b'\xe0A\x02'
    _globals['_DELETETASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETETASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_RUNTASKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNTASKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1ecloudtasks.googleapis.com/Task'
    _globals['_CLOUDTASKS']._loaded_options = None
    _globals['_CLOUDTASKS']._serialized_options = b'\xcaA\x19cloudtasks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CLOUDTASKS'].methods_by_name['ListQueues']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ListQueues']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v2beta3/{parent=projects/*/locations/*}/queues'
    _globals['_CLOUDTASKS'].methods_by_name['GetQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021\x12//v2beta3/{name=projects/*/locations/*/queues/*}'
    _globals['_CLOUDTASKS'].methods_by_name['CreateQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['CreateQueue']._serialized_options = b'\xdaA\x0cparent,queue\x82\xd3\xe4\x93\x028"//v2beta3/{parent=projects/*/locations/*}/queues:\x05queue'
    _globals['_CLOUDTASKS'].methods_by_name['UpdateQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['UpdateQueue']._serialized_options = b'\xdaA\x11queue,update_mask\x82\xd3\xe4\x93\x02>25/v2beta3/{queue.name=projects/*/locations/*/queues/*}:\x05queue'
    _globals['_CLOUDTASKS'].methods_by_name['DeleteQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['DeleteQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x021*//v2beta3/{name=projects/*/locations/*/queues/*}'
    _globals['_CLOUDTASKS'].methods_by_name['PurgeQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['PurgeQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v2beta3/{name=projects/*/locations/*/queues/*}:purge:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['PauseQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['PauseQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02:"5/v2beta3/{name=projects/*/locations/*/queues/*}:pause:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['ResumeQueue']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ResumeQueue']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;"6/v2beta3/{name=projects/*/locations/*/queues/*}:resume:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['GetIamPolicy']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetIamPolicy']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02E"@/v2beta3/{resource=projects/*/locations/*/queues/*}:getIamPolicy:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['SetIamPolicy']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['SetIamPolicy']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02E"@/v2beta3/{resource=projects/*/locations/*/queues/*}:setIamPolicy:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['TestIamPermissions']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['TestIamPermissions']._serialized_options = b'\xdaA\x14resource,permissions\x82\xd3\xe4\x93\x02K"F/v2beta3/{resource=projects/*/locations/*/queues/*}:testIamPermissions:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['ListTasks']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['ListTasks']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v2beta3/{parent=projects/*/locations/*/queues/*}/tasks'
    _globals['_CLOUDTASKS'].methods_by_name['GetTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['GetTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}'
    _globals['_CLOUDTASKS'].methods_by_name['CreateTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['CreateTask']._serialized_options = b'\xdaA\x0bparent,task\x82\xd3\xe4\x93\x02<"7/v2beta3/{parent=projects/*/locations/*/queues/*}/tasks:\x01*'
    _globals['_CLOUDTASKS'].methods_by_name['DeleteTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['DeleteTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029*7/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}'
    _globals['_CLOUDTASKS'].methods_by_name['RunTask']._loaded_options = None
    _globals['_CLOUDTASKS'].methods_by_name['RunTask']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02@";/v2beta3/{name=projects/*/locations/*/queues/*/tasks/*}:run:\x01*'
    _globals['_LISTQUEUESREQUEST']._serialized_start = 393
    _globals['_LISTQUEUESREQUEST']._serialized_end = 576
    _globals['_LISTQUEUESRESPONSE']._serialized_start = 578
    _globals['_LISTQUEUESRESPONSE']._serialized_end = 674
    _globals['_GETQUEUEREQUEST']._serialized_start = 676
    _globals['_GETQUEUEREQUEST']._serialized_end = 800
    _globals['_CREATEQUEUEREQUEST']._serialized_start = 803
    _globals['_CREATEQUEUEREQUEST']._serialized_end = 935
    _globals['_UPDATEQUEUEREQUEST']._serialized_start = 937
    _globals['_UPDATEQUEUEREQUEST']._serialized_end = 1061
    _globals['_DELETEQUEUEREQUEST']._serialized_start = 1063
    _globals['_DELETEQUEUEREQUEST']._serialized_end = 1138
    _globals['_PURGEQUEUEREQUEST']._serialized_start = 1140
    _globals['_PURGEQUEUEREQUEST']._serialized_end = 1214
    _globals['_PAUSEQUEUEREQUEST']._serialized_start = 1216
    _globals['_PAUSEQUEUEREQUEST']._serialized_end = 1290
    _globals['_RESUMEQUEUEREQUEST']._serialized_start = 1292
    _globals['_RESUMEQUEUEREQUEST']._serialized_end = 1367
    _globals['_LISTTASKSREQUEST']._serialized_start = 1370
    _globals['_LISTTASKSREQUEST']._serialized_end = 1545
    _globals['_LISTTASKSRESPONSE']._serialized_start = 1547
    _globals['_LISTTASKSRESPONSE']._serialized_end = 1640
    _globals['_GETTASKREQUEST']._serialized_start = 1643
    _globals['_GETTASKREQUEST']._serialized_end = 1775
    _globals['_CREATETASKREQUEST']._serialized_start = 1778
    _globals['_CREATETASKREQUEST']._serialized_end = 1968
    _globals['_DELETETASKREQUEST']._serialized_start = 1970
    _globals['_DELETETASKREQUEST']._serialized_end = 2043
    _globals['_RUNTASKREQUEST']._serialized_start = 2046
    _globals['_RUNTASKREQUEST']._serialized_end = 2178
    _globals['_CLOUDTASKS']._serialized_start = 2181
    _globals['_CLOUDTASKS']._serialized_end = 5034