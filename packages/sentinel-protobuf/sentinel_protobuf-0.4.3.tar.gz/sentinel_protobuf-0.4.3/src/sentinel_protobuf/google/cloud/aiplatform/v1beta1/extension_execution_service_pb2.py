"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/extension_execution_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from .....google.cloud.aiplatform.v1beta1 import extension_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_extension__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/aiplatform/v1beta1/extension_execution_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a/google/cloud/aiplatform/v1beta1/extension.proto\x1a\x1cgoogle/protobuf/struct.proto"\xf6\x01\n\x17ExecuteExtensionRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension\x12\x19\n\x0coperation_id\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\x10operation_params\x18\x03 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12M\n\x13runtime_auth_config\x18\x04 \x01(\x0b2+.google.cloud.aiplatform.v1beta1.AuthConfigB\x03\xe0A\x01"+\n\x18ExecuteExtensionResponse\x12\x0f\n\x07content\x18\x02 \x01(\t"\x93\x01\n\x15QueryExtensionRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension\x12?\n\x08contents\x18\x02 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x02"j\n\x16QueryExtensionResponse\x127\n\x05steps\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.Content\x12\x17\n\x0ffailure_message\x18\x02 \x01(\t2\xaa\x04\n\x19ExtensionExecutionService\x12\xe3\x01\n\x10ExecuteExtension\x128.google.cloud.aiplatform.v1beta1.ExecuteExtensionRequest\x1a9.google.cloud.aiplatform.v1beta1.ExecuteExtensionResponse"Z\xdaA\x11name,operation_id\x82\xd3\xe4\x93\x02@";/v1beta1/{name=projects/*/locations/*/extensions/*}:execute:\x01*\x12\xd7\x01\n\x0eQueryExtension\x126.google.cloud.aiplatform.v1beta1.QueryExtensionRequest\x1a7.google.cloud.aiplatform.v1beta1.QueryExtensionResponse"T\xdaA\rname,contents\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/extensions/*}:query:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n#com.google.cloud.aiplatform.v1beta1B\x1eExtensionExecutionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.extension_execution_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1eExtensionExecutionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension'
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['operation_id']._loaded_options = None
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['operation_id']._serialized_options = b'\xe0A\x02'
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['operation_params']._loaded_options = None
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['operation_params']._serialized_options = b'\xe0A\x01'
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['runtime_auth_config']._loaded_options = None
    _globals['_EXECUTEEXTENSIONREQUEST'].fields_by_name['runtime_auth_config']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYEXTENSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYEXTENSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#aiplatform.googleapis.com/Extension'
    _globals['_QUERYEXTENSIONREQUEST'].fields_by_name['contents']._loaded_options = None
    _globals['_QUERYEXTENSIONREQUEST'].fields_by_name['contents']._serialized_options = b'\xe0A\x02'
    _globals['_EXTENSIONEXECUTIONSERVICE']._loaded_options = None
    _globals['_EXTENSIONEXECUTIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EXTENSIONEXECUTIONSERVICE'].methods_by_name['ExecuteExtension']._loaded_options = None
    _globals['_EXTENSIONEXECUTIONSERVICE'].methods_by_name['ExecuteExtension']._serialized_options = b'\xdaA\x11name,operation_id\x82\xd3\xe4\x93\x02@";/v1beta1/{name=projects/*/locations/*/extensions/*}:execute:\x01*'
    _globals['_EXTENSIONEXECUTIONSERVICE'].methods_by_name['QueryExtension']._loaded_options = None
    _globals['_EXTENSIONEXECUTIONSERVICE'].methods_by_name['QueryExtension']._serialized_options = b'\xdaA\rname,contents\x82\xd3\xe4\x93\x02>"9/v1beta1/{name=projects/*/locations/*/extensions/*}:query:\x01*'
    _globals['_EXECUTEEXTENSIONREQUEST']._serialized_start = 344
    _globals['_EXECUTEEXTENSIONREQUEST']._serialized_end = 590
    _globals['_EXECUTEEXTENSIONRESPONSE']._serialized_start = 592
    _globals['_EXECUTEEXTENSIONRESPONSE']._serialized_end = 635
    _globals['_QUERYEXTENSIONREQUEST']._serialized_start = 638
    _globals['_QUERYEXTENSIONREQUEST']._serialized_end = 785
    _globals['_QUERYEXTENSIONRESPONSE']._serialized_start = 787
    _globals['_QUERYEXTENSIONRESPONSE']._serialized_end = 893
    _globals['_EXTENSIONEXECUTIONSERVICE']._serialized_start = 896
    _globals['_EXTENSIONEXECUTIONSERVICE']._serialized_end = 1450