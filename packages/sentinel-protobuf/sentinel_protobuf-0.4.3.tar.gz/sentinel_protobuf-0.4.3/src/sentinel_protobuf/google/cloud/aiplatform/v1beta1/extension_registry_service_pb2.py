"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/extension_registry_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import extension_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_extension__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/aiplatform/v1beta1/extension_registry_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/extension.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x97\x01\n\x16ImportExtensionRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12B\n\textension\x18\x02 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.ExtensionB\x03\xe0A\x02"w\n ImportExtensionOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"P\n\x13GetExtensionRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension"\x92\x01\n\x16UpdateExtensionRequest\x12B\n\textension\x18\x01 \x01(\x0b2*.google.cloud.aiplatform.v1beta1.ExtensionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\xaf\x01\n\x15ListExtensionsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x06 \x01(\tB\x03\xe0A\x01"q\n\x16ListExtensionsResponse\x12>\n\nextensions\x18\x01 \x03(\x0b2*.google.cloud.aiplatform.v1beta1.Extension\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"S\n\x16DeleteExtensionRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension2\xaf\t\n\x18ExtensionRegistryService\x12\xfc\x01\n\x0fImportExtension\x127.google.cloud.aiplatform.v1beta1.ImportExtensionRequest\x1a\x1d.google.longrunning.Operation"\x90\x01\xcaA-\n\tExtension\x12 ImportExtensionOperationMetadata\xdaA\x10parent,extension\x82\xd3\xe4\x93\x02G":/v1beta1/{parent=projects/*/locations/*}/extensions:import:\textension\x12\xb4\x01\n\x0cGetExtension\x124.google.cloud.aiplatform.v1beta1.GetExtensionRequest\x1a*.google.cloud.aiplatform.v1beta1.Extension"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/extensions/*}\x12\xc7\x01\n\x0eListExtensions\x126.google.cloud.aiplatform.v1beta1.ListExtensionsRequest\x1a7.google.cloud.aiplatform.v1beta1.ListExtensionsResponse"D\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/extensions\x12\xe0\x01\n\x0fUpdateExtension\x127.google.cloud.aiplatform.v1beta1.UpdateExtensionRequest\x1a*.google.cloud.aiplatform.v1beta1.Extension"h\xdaA\x15extension,update_mask\x82\xd3\xe4\x93\x02J2=/v1beta1/{extension.name=projects/*/locations/*/extensions/*}:\textension\x12\xe0\x01\n\x0fDeleteExtension\x127.google.cloud.aiplatform.v1beta1.DeleteExtensionRequest\x1a\x1d.google.longrunning.Operation"u\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/extensions/*}\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf4\x01\n#com.google.cloud.aiplatform.v1beta1B\x1dExtensionRegistryServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.extension_registry_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1dExtensionRegistryServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_IMPORTEXTENSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_IMPORTEXTENSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_IMPORTEXTENSIONREQUEST'].fields_by_name['extension']._loaded_options = None
    _globals['_IMPORTEXTENSIONREQUEST'].fields_by_name['extension']._serialized_options = b'\xe0A\x02'
    _globals['_GETEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension'
    _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['extension']._loaded_options = None
    _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['extension']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEXTENSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTEXTENSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension'
    _globals['_EXTENSIONREGISTRYSERVICE']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['ImportExtension']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['ImportExtension']._serialized_options = b'\xcaA-\n\tExtension\x12 ImportExtensionOperationMetadata\xdaA\x10parent,extension\x82\xd3\xe4\x93\x02G":/v1beta1/{parent=projects/*/locations/*}/extensions:import:\textension'
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['GetExtension']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['GetExtension']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1beta1/{name=projects/*/locations/*/extensions/*}'
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['ListExtensions']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['ListExtensions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x025\x123/v1beta1/{parent=projects/*/locations/*}/extensions'
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['UpdateExtension']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['UpdateExtension']._serialized_options = b'\xdaA\x15extension,update_mask\x82\xd3\xe4\x93\x02J2=/v1beta1/{extension.name=projects/*/locations/*/extensions/*}:\textension'
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['DeleteExtension']._loaded_options = None
    _globals['_EXTENSIONREGISTRYSERVICE'].methods_by_name['DeleteExtension']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1beta1/{name=projects/*/locations/*/extensions/*}'
    _globals['_IMPORTEXTENSIONREQUEST']._serialized_start = 415
    _globals['_IMPORTEXTENSIONREQUEST']._serialized_end = 566
    _globals['_IMPORTEXTENSIONOPERATIONMETADATA']._serialized_start = 568
    _globals['_IMPORTEXTENSIONOPERATIONMETADATA']._serialized_end = 687
    _globals['_GETEXTENSIONREQUEST']._serialized_start = 689
    _globals['_GETEXTENSIONREQUEST']._serialized_end = 769
    _globals['_UPDATEEXTENSIONREQUEST']._serialized_start = 772
    _globals['_UPDATEEXTENSIONREQUEST']._serialized_end = 918
    _globals['_LISTEXTENSIONSREQUEST']._serialized_start = 921
    _globals['_LISTEXTENSIONSREQUEST']._serialized_end = 1096
    _globals['_LISTEXTENSIONSRESPONSE']._serialized_start = 1098
    _globals['_LISTEXTENSIONSRESPONSE']._serialized_end = 1211
    _globals['_DELETEEXTENSIONREQUEST']._serialized_start = 1213
    _globals['_DELETEEXTENSIONREQUEST']._serialized_end = 1296
    _globals['_EXTENSIONREGISTRYSERVICE']._serialized_start = 1299
    _globals['_EXTENSIONREGISTRYSERVICE']._serialized_end = 2498