"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/lustre/v1/lustre.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.lustre.v1 import instance_pb2 as google_dot_cloud_dot_lustre_dot_v1_dot_instance__pb2
from .....google.cloud.lustre.v1 import transfer_pb2 as google_dot_cloud_dot_lustre_dot_v1_dot_transfer__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#google/cloud/lustre/v1/lustre.proto\x12\x16google.cloud.lustre.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a%google/cloud/lustre/v1/instance.proto\x1a%google/cloud/lustre/v1/transfer.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto2\xc5\x0b\n\x06Lustre\x12\xac\x01\n\rListInstances\x12,.google.cloud.lustre.v1.ListInstancesRequest\x1a-.google.cloud.lustre.v1.ListInstancesResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances\x12\x99\x01\n\x0bGetInstance\x12*.google.cloud.lustre.v1.GetInstanceRequest\x1a .google.cloud.lustre.v1.Instance"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}\x12\xdd\x01\n\x0eCreateInstance\x12-.google.cloud.lustre.v1.CreateInstanceRequest\x1a\x1d.google.longrunning.Operation"}\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance\x12\xdf\x01\n\x0eUpdateInstance\x12-.google.cloud.lustre.v1.UpdateInstanceRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance\x12\xc9\x01\n\x0eDeleteInstance\x12-.google.cloud.lustre.v1.DeleteInstanceRequest\x1a\x1d.google.longrunning.Operation"i\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}\x12\xcd\x01\n\nImportData\x12).google.cloud.lustre.v1.ImportDataRequest\x1a\x1d.google.longrunning.Operation"u\xcaA(\n\x12ImportDataResponse\x12\x12ImportDataMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:importData:\x01*\x12\xc6\x01\n\nExportData\x12).google.cloud.lustre.v1.ExportDataRequest\x1a\x1d.google.longrunning.Operation"n\xcaA(\n\x12ExportDataResponse\x12\x12ExportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:exportData:\x01*\x1aI\xcaA\x15lustre.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8c\x02\n\x1acom.google.cloud.lustre.v1B\x0bLustreProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepb\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.lustre.v1.lustre_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.lustre.v1B\x0bLustreProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepb\xeaAY\n!iam.googleapis.com/ServiceAccount\x124projects/{project}/serviceAccounts/{service_account}\xeaAN\n\x1ecompute.googleapis.com/Network\x12,projects/{project}/global/networks/{network}'
    _globals['_LUSTRE']._loaded_options = None
    _globals['_LUSTRE']._serialized_options = b'\xcaA\x15lustre.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_LUSTRE'].methods_by_name['ListInstances']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['ListInstances']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1/{parent=projects/*/locations/*}/instances'
    _globals['_LUSTRE'].methods_by_name['GetInstance']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['GetInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_LUSTRE'].methods_by_name['CreateInstance']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['CreateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x1bparent,instance,instance_id\x82\xd3\xe4\x93\x029"-/v1/{parent=projects/*/locations/*}/instances:\x08instance'
    _globals['_LUSTRE'].methods_by_name['UpdateInstance']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['UpdateInstance']._serialized_options = b'\xcaA\x1d\n\x08Instance\x12\x11OperationMetadata\xdaA\x14instance,update_mask\x82\xd3\xe4\x93\x02B26/v1/{instance.name=projects/*/locations/*/instances/*}:\x08instance'
    _globals['_LUSTRE'].methods_by_name['DeleteInstance']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['DeleteInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02/*-/v1/{name=projects/*/locations/*/instances/*}'
    _globals['_LUSTRE'].methods_by_name['ImportData']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['ImportData']._serialized_options = b'\xcaA(\n\x12ImportDataResponse\x12\x12ImportDataMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:importData:\x01*'
    _globals['_LUSTRE'].methods_by_name['ExportData']._loaded_options = None
    _globals['_LUSTRE'].methods_by_name['ExportData']._serialized_options = b'\xcaA(\n\x12ExportDataResponse\x12\x12ExportDataMetadata\x82\xd3\xe4\x93\x02="8/v1/{name=projects/*/locations/*/instances/*}:exportData:\x01*'
    _globals['_LUSTRE']._serialized_start = 290
    _globals['_LUSTRE']._serialized_end = 1767