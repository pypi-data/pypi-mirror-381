"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/persistent_resource_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import persistent_resource_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_persistent__resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/aiplatform/v1beta1/persistent_resource_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a9google/cloud/aiplatform/v1beta1/persistent_resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xd8\x01\n\x1fCreatePersistentResourceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12U\n\x13persistent_resource\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PersistentResourceB\x03\xe0A\x02\x12#\n\x16persistent_resource_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x9a\x01\n)CreatePersistentResourceOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x18\n\x10progress_message\x18\x02 \x01(\t"\x9a\x01\n)UpdatePersistentResourceOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x18\n\x10progress_message\x18\x02 \x01(\t"\x9a\x01\n)RebootPersistentResourceOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12\x18\n\x10progress_message\x18\x02 \x01(\t"b\n\x1cGetPersistentResourceRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource"\x8c\x01\n\x1eListPersistentResourcesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"\x8d\x01\n\x1fListPersistentResourcesResponse\x12Q\n\x14persistent_resources\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1beta1.PersistentResource\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"e\n\x1fDeletePersistentResourceRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource"\xae\x01\n\x1fUpdatePersistentResourceRequest\x12U\n\x13persistent_resource\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.PersistentResourceB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"e\n\x1fRebootPersistentResourceRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource2\xeb\r\n\x19PersistentResourceService\x12\xcd\x02\n\x18CreatePersistentResource\x12@.google.cloud.aiplatform.v1beta1.CreatePersistentResourceRequest\x1a\x1d.google.longrunning.Operation"\xcf\x01\xcaA?\n\x12PersistentResource\x12)CreatePersistentResourceOperationMetadata\xdaA1parent,persistent_resource,persistent_resource_id\x82\xd3\xe4\x93\x02S"</v1beta1/{parent=projects/*/locations/*}/persistentResources:\x13persistent_resource\x12\xd8\x01\n\x15GetPersistentResource\x12=.google.cloud.aiplatform.v1beta1.GetPersistentResourceRequest\x1a3.google.cloud.aiplatform.v1beta1.PersistentResource"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/persistentResources/*}\x12\xeb\x01\n\x17ListPersistentResources\x12?.google.cloud.aiplatform.v1beta1.ListPersistentResourcesRequest\x1a@.google.cloud.aiplatform.v1beta1.ListPersistentResourcesResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta1/{parent=projects/*/locations/*}/persistentResources\x12\xfb\x01\n\x18DeletePersistentResource\x12@.google.cloud.aiplatform.v1beta1.DeletePersistentResourceRequest\x1a\x1d.google.longrunning.Operation"~\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1beta1/{name=projects/*/locations/*/persistentResources/*}\x12\xcf\x02\n\x18UpdatePersistentResource\x12@.google.cloud.aiplatform.v1beta1.UpdatePersistentResourceRequest\x1a\x1d.google.longrunning.Operation"\xd1\x01\xcaA?\n\x12PersistentResource\x12)UpdatePersistentResourceOperationMetadata\xdaA\x1fpersistent_resource,update_mask\x82\xd3\xe4\x93\x02g2P/v1beta1/{persistent_resource.name=projects/*/locations/*/persistentResources/*}:\x13persistent_resource\x12\x95\x02\n\x18RebootPersistentResource\x12@.google.cloud.aiplatform.v1beta1.RebootPersistentResourceRequest\x1a\x1d.google.longrunning.Operation"\x97\x01\xcaA?\n\x12PersistentResource\x12)RebootPersistentResourceOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/*/persistentResources/*}:reboot:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n#com.google.cloud.aiplatform.v1beta1B\x1ePersistentResourceServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.persistent_resource_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1ePersistentResourceServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource']._loaded_options = None
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource_id']._loaded_options = None
    _globals['_CREATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource'
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTPERSISTENTRESOURCESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource'
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource']._loaded_options = None
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST'].fields_by_name['persistent_resource']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_REBOOTPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_REBOOTPERSISTENTRESOURCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/PersistentResource'
    _globals['_PERSISTENTRESOURCESERVICE']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['CreatePersistentResource']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['CreatePersistentResource']._serialized_options = b'\xcaA?\n\x12PersistentResource\x12)CreatePersistentResourceOperationMetadata\xdaA1parent,persistent_resource,persistent_resource_id\x82\xd3\xe4\x93\x02S"</v1beta1/{parent=projects/*/locations/*}/persistentResources:\x13persistent_resource'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['GetPersistentResource']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['GetPersistentResource']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/persistentResources/*}'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['ListPersistentResources']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['ListPersistentResources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta1/{parent=projects/*/locations/*}/persistentResources'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['DeletePersistentResource']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['DeletePersistentResource']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02>*</v1beta1/{name=projects/*/locations/*/persistentResources/*}'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['UpdatePersistentResource']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['UpdatePersistentResource']._serialized_options = b'\xcaA?\n\x12PersistentResource\x12)UpdatePersistentResourceOperationMetadata\xdaA\x1fpersistent_resource,update_mask\x82\xd3\xe4\x93\x02g2P/v1beta1/{persistent_resource.name=projects/*/locations/*/persistentResources/*}:\x13persistent_resource'
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['RebootPersistentResource']._loaded_options = None
    _globals['_PERSISTENTRESOURCESERVICE'].methods_by_name['RebootPersistentResource']._serialized_options = b'\xcaA?\n\x12PersistentResource\x12)RebootPersistentResourceOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H"C/v1beta1/{name=projects/*/locations/*/persistentResources/*}:reboot:\x01*'
    _globals['_CREATEPERSISTENTRESOURCEREQUEST']._serialized_start = 426
    _globals['_CREATEPERSISTENTRESOURCEREQUEST']._serialized_end = 642
    _globals['_CREATEPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_start = 645
    _globals['_CREATEPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_end = 799
    _globals['_UPDATEPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_start = 802
    _globals['_UPDATEPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_end = 956
    _globals['_REBOOTPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_start = 959
    _globals['_REBOOTPERSISTENTRESOURCEOPERATIONMETADATA']._serialized_end = 1113
    _globals['_GETPERSISTENTRESOURCEREQUEST']._serialized_start = 1115
    _globals['_GETPERSISTENTRESOURCEREQUEST']._serialized_end = 1213
    _globals['_LISTPERSISTENTRESOURCESREQUEST']._serialized_start = 1216
    _globals['_LISTPERSISTENTRESOURCESREQUEST']._serialized_end = 1356
    _globals['_LISTPERSISTENTRESOURCESRESPONSE']._serialized_start = 1359
    _globals['_LISTPERSISTENTRESOURCESRESPONSE']._serialized_end = 1500
    _globals['_DELETEPERSISTENTRESOURCEREQUEST']._serialized_start = 1502
    _globals['_DELETEPERSISTENTRESOURCEREQUEST']._serialized_end = 1603
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST']._serialized_start = 1606
    _globals['_UPDATEPERSISTENTRESOURCEREQUEST']._serialized_end = 1780
    _globals['_REBOOTPERSISTENTRESOURCEREQUEST']._serialized_start = 1782
    _globals['_REBOOTPERSISTENTRESOURCEREQUEST']._serialized_end = 1883
    _globals['_PERSISTENTRESOURCESERVICE']._serialized_start = 1886
    _globals['_PERSISTENTRESOURCESERVICE']._serialized_end = 3657