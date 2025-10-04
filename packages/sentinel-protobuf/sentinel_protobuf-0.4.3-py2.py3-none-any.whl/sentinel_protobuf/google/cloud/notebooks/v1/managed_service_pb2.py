"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/notebooks/v1/managed_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.notebooks.v1 import diagnostic_config_pb2 as google_dot_cloud_dot_notebooks_dot_v1_dot_diagnostic__config__pb2
from .....google.cloud.notebooks.v1 import event_pb2 as google_dot_cloud_dot_notebooks_dot_v1_dot_event__pb2
from .....google.cloud.notebooks.v1 import runtime_pb2 as google_dot_cloud_dot_notebooks_dot_v1_dot_runtime__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/notebooks/v1/managed_service.proto\x12\x19google.cloud.notebooks.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a1google/cloud/notebooks/v1/diagnostic_config.proto\x1a%google/cloud/notebooks/v1/event.proto\x1a\'google/cloud/notebooks/v1/runtime.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"v\n\x13ListRuntimesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\x12 notebooks.googleapis.com/Runtime\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"z\n\x14ListRuntimesResponse\x124\n\x08runtimes\x18\x01 \x03(\x0b2".google.cloud.notebooks.v1.Runtime\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"K\n\x11GetRuntimeRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime"\xb7\x01\n\x14CreateRuntimeRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime\x12\x17\n\nruntime_id\x18\x02 \x01(\tB\x03\xe0A\x02\x128\n\x07runtime\x18\x03 \x01(\x0b2".google.cloud.notebooks.v1.RuntimeB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x04 \x01(\t"b\n\x14DeleteRuntimeRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime\x12\x12\n\nrequest_id\x18\x02 \x01(\t"<\n\x13StartRuntimeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x02 \x01(\t";\n\x12StopRuntimeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\xa4\x01\n\x14SwitchRuntimeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x0cmachine_type\x18\x02 \x01(\t\x12O\n\x12accelerator_config\x18\x03 \x01(\x0b23.google.cloud.notebooks.v1.RuntimeAcceleratorConfig\x12\x12\n\nrequest_id\x18\x04 \x01(\t"<\n\x13ResetRuntimeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x02 \x01(\t">\n\x15UpgradeRuntimeRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x02 \x01(\t"\x9d\x01\n\x19ReportRuntimeEventRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime\x12\x12\n\x05vm_id\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x05event\x18\x03 \x01(\x0b2 .google.cloud.notebooks.v1.EventB\x03\xe0A\x02"\x9a\x01\n\x14UpdateRuntimeRequest\x128\n\x07runtime\x18\x01 \x01(\x0b2".google.cloud.notebooks.v1.RuntimeB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x12\n\nrequest_id\x18\x03 \x01(\t"p\n"RefreshRuntimeTokenInternalRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime\x12\x12\n\x05vm_id\x18\x02 \x01(\tB\x03\xe0A\x02"q\n#RefreshRuntimeTokenInternalResponse\x12\x14\n\x0caccess_token\x18\x01 \x01(\t\x124\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x9d\x01\n\x16DiagnoseRuntimeRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime\x12K\n\x11diagnostic_config\x18\x02 \x01(\x0b2+.google.cloud.notebooks.v1.DiagnosticConfigB\x03\xe0A\x022\xd2\x15\n\x16ManagedNotebookService\x12\xae\x01\n\x0cListRuntimes\x12..google.cloud.notebooks.v1.ListRuntimesRequest\x1a/.google.cloud.notebooks.v1.ListRuntimesResponse"=\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/runtimes\x12\x9b\x01\n\nGetRuntime\x12,.google.cloud.notebooks.v1.GetRuntimeRequest\x1a".google.cloud.notebooks.v1.Runtime";\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/runtimes/*}\x12\xd9\x01\n\rCreateRuntime\x12/.google.cloud.notebooks.v1.CreateRuntimeRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x19parent,runtime_id,runtime\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/runtimes:\x07runtime\x12\xdb\x01\n\rUpdateRuntime\x12/.google.cloud.notebooks.v1.UpdateRuntimeRequest\x1a\x1d.google.longrunning.Operation"z\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x13runtime,update_mask\x82\xd3\xe4\x93\x02?24/v1/{runtime.name=projects/*/locations/*/runtimes/*}:\x07runtime\x12\xc9\x01\n\rDeleteRuntime\x12/.google.cloud.notebooks.v1.DeleteRuntimeRequest\x1a\x1d.google.longrunning.Operation"h\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/runtimes/*}\x12\xc2\x01\n\x0cStartRuntime\x12..google.cloud.notebooks.v1.StartRuntimeRequest\x1a\x1d.google.longrunning.Operation"c\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/runtimes/*}:start:\x01*\x12\xbf\x01\n\x0bStopRuntime\x12-.google.cloud.notebooks.v1.StopRuntimeRequest\x1a\x1d.google.longrunning.Operation"b\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/runtimes/*}:stop:\x01*\x12\xc5\x01\n\rSwitchRuntime\x12/.google.cloud.notebooks.v1.SwitchRuntimeRequest\x1a\x1d.google.longrunning.Operation"d\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/runtimes/*}:switch:\x01*\x12\xc2\x01\n\x0cResetRuntime\x12..google.cloud.notebooks.v1.ResetRuntimeRequest\x1a\x1d.google.longrunning.Operation"c\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/runtimes/*}:reset:\x01*\x12\xc8\x01\n\x0eUpgradeRuntime\x120.google.cloud.notebooks.v1.UpgradeRuntimeRequest\x1a\x1d.google.longrunning.Operation"e\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/runtimes/*}:upgrade:\x01*\x12\xd4\x01\n\x12ReportRuntimeEvent\x124.google.cloud.notebooks.v1.ReportRuntimeEventRequest\x1a\x1d.google.longrunning.Operation"i\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/runtimes/*}:reportEvent:\x01*\x12\xfe\x01\n\x1bRefreshRuntimeTokenInternal\x12=.google.cloud.notebooks.v1.RefreshRuntimeTokenInternalRequest\x1a>.google.cloud.notebooks.v1.RefreshRuntimeTokenInternalResponse"`\xdaA\nname,vm_id\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/runtimes/*}:refreshRuntimeTokenInternal:\x01*\x12\xdd\x01\n\x0fDiagnoseRuntime\x121.google.cloud.notebooks.v1.DiagnoseRuntimeRequest\x1a\x1d.google.longrunning.Operation"x\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x16name,diagnostic_config\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/runtimes/*}:diagnose:\x01*\x1aL\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xcc\x01\n\x1dcom.google.cloud.notebooks.v1B\x15ManagedNotebooksProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V1\xca\x02\x19Google\\Cloud\\Notebooks\\V1\xea\x02\x1cGoogle::Cloud::Notebooks::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.notebooks.v1.managed_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.cloud.notebooks.v1B\x15ManagedNotebooksProtoP\x01Z;cloud.google.com/go/notebooks/apiv1/notebookspb;notebookspb\xaa\x02\x19Google.Cloud.Notebooks.V1\xca\x02\x19Google\\Cloud\\Notebooks\\V1\xea\x02\x1cGoogle::Cloud::Notebooks::V1'
    _globals['_LISTRUNTIMESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTRUNTIMESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\x12 notebooks.googleapis.com/Runtime'
    _globals['_GETRUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETRUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['runtime_id']._loaded_options = None
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['runtime_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['runtime']._loaded_options = None
    _globals['_CREATERUNTIMEREQUEST'].fields_by_name['runtime']._serialized_options = b'\xe0A\x02'
    _globals['_DELETERUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETERUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_STARTRUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STARTRUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_STOPRUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_STOPRUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SWITCHRUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SWITCHRUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_RESETRUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RESETRUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_UPGRADERUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPGRADERUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['vm_id']._loaded_options = None
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['vm_id']._serialized_options = b'\xe0A\x02'
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_REPORTRUNTIMEEVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATERUNTIMEREQUEST'].fields_by_name['runtime']._loaded_options = None
    _globals['_UPDATERUNTIMEREQUEST'].fields_by_name['runtime']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATERUNTIMEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATERUNTIMEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST'].fields_by_name['vm_id']._loaded_options = None
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST'].fields_by_name['vm_id']._serialized_options = b'\xe0A\x02'
    _globals['_REFRESHRUNTIMETOKENINTERNALRESPONSE'].fields_by_name['expire_time']._loaded_options = None
    _globals['_REFRESHRUNTIMETOKENINTERNALRESPONSE'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_DIAGNOSERUNTIMEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DIAGNOSERUNTIMEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n notebooks.googleapis.com/Runtime'
    _globals['_DIAGNOSERUNTIMEREQUEST'].fields_by_name['diagnostic_config']._loaded_options = None
    _globals['_DIAGNOSERUNTIMEREQUEST'].fields_by_name['diagnostic_config']._serialized_options = b'\xe0A\x02'
    _globals['_MANAGEDNOTEBOOKSERVICE']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE']._serialized_options = b'\xcaA\x18notebooks.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ListRuntimes']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ListRuntimes']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02.\x12,/v1/{parent=projects/*/locations/*}/runtimes'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['GetRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['GetRuntime']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02.\x12,/v1/{name=projects/*/locations/*/runtimes/*}'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['CreateRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['CreateRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x19parent,runtime_id,runtime\x82\xd3\xe4\x93\x027",/v1/{parent=projects/*/locations/*}/runtimes:\x07runtime'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['UpdateRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['UpdateRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x13runtime,update_mask\x82\xd3\xe4\x93\x02?24/v1/{runtime.name=projects/*/locations/*/runtimes/*}:\x07runtime'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['DeleteRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['DeleteRuntime']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02.*,/v1/{name=projects/*/locations/*/runtimes/*}'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['StartRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['StartRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/runtimes/*}:start:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['StopRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['StopRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x026"1/v1/{name=projects/*/locations/*/runtimes/*}:stop:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['SwitchRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['SwitchRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/locations/*/runtimes/*}:switch:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ResetRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ResetRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/runtimes/*}:reset:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['UpgradeRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['UpgradeRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x029"4/v1/{name=projects/*/locations/*/runtimes/*}:upgrade:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ReportRuntimeEvent']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['ReportRuntimeEvent']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/runtimes/*}:reportEvent:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['RefreshRuntimeTokenInternal']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['RefreshRuntimeTokenInternal']._serialized_options = b'\xdaA\nname,vm_id\x82\xd3\xe4\x93\x02M"H/v1/{name=projects/*/locations/*/runtimes/*}:refreshRuntimeTokenInternal:\x01*'
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['DiagnoseRuntime']._loaded_options = None
    _globals['_MANAGEDNOTEBOOKSERVICE'].methods_by_name['DiagnoseRuntime']._serialized_options = b'\xcaA\x1c\n\x07Runtime\x12\x11OperationMetadata\xdaA\x16name,diagnostic_config\x82\xd3\xe4\x93\x02:"5/v1/{name=projects/*/locations/*/runtimes/*}:diagnose:\x01*'
    _globals['_LISTRUNTIMESREQUEST']._serialized_start = 428
    _globals['_LISTRUNTIMESREQUEST']._serialized_end = 546
    _globals['_LISTRUNTIMESRESPONSE']._serialized_start = 548
    _globals['_LISTRUNTIMESRESPONSE']._serialized_end = 670
    _globals['_GETRUNTIMEREQUEST']._serialized_start = 672
    _globals['_GETRUNTIMEREQUEST']._serialized_end = 747
    _globals['_CREATERUNTIMEREQUEST']._serialized_start = 750
    _globals['_CREATERUNTIMEREQUEST']._serialized_end = 933
    _globals['_DELETERUNTIMEREQUEST']._serialized_start = 935
    _globals['_DELETERUNTIMEREQUEST']._serialized_end = 1033
    _globals['_STARTRUNTIMEREQUEST']._serialized_start = 1035
    _globals['_STARTRUNTIMEREQUEST']._serialized_end = 1095
    _globals['_STOPRUNTIMEREQUEST']._serialized_start = 1097
    _globals['_STOPRUNTIMEREQUEST']._serialized_end = 1156
    _globals['_SWITCHRUNTIMEREQUEST']._serialized_start = 1159
    _globals['_SWITCHRUNTIMEREQUEST']._serialized_end = 1323
    _globals['_RESETRUNTIMEREQUEST']._serialized_start = 1325
    _globals['_RESETRUNTIMEREQUEST']._serialized_end = 1385
    _globals['_UPGRADERUNTIMEREQUEST']._serialized_start = 1387
    _globals['_UPGRADERUNTIMEREQUEST']._serialized_end = 1449
    _globals['_REPORTRUNTIMEEVENTREQUEST']._serialized_start = 1452
    _globals['_REPORTRUNTIMEEVENTREQUEST']._serialized_end = 1609
    _globals['_UPDATERUNTIMEREQUEST']._serialized_start = 1612
    _globals['_UPDATERUNTIMEREQUEST']._serialized_end = 1766
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST']._serialized_start = 1768
    _globals['_REFRESHRUNTIMETOKENINTERNALREQUEST']._serialized_end = 1880
    _globals['_REFRESHRUNTIMETOKENINTERNALRESPONSE']._serialized_start = 1882
    _globals['_REFRESHRUNTIMETOKENINTERNALRESPONSE']._serialized_end = 1995
    _globals['_DIAGNOSERUNTIMEREQUEST']._serialized_start = 1998
    _globals['_DIAGNOSERUNTIMEREQUEST']._serialized_end = 2155
    _globals['_MANAGEDNOTEBOOKSERVICE']._serialized_start = 2158
    _globals['_MANAGEDNOTEBOOKSERVICE']._serialized_end = 4928