"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/apihub/v1/provisioning_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.apihub.v1 import common_fields_pb2 as google_dot_cloud_dot_apihub_dot_v1_dot_common__fields__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/apihub/v1/provisioning_service.proto\x12\x16google.cloud.apihub.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/apihub/v1/common_fields.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"\xc1\x01\n\x1bCreateApiHubInstanceRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12 \n\x13api_hub_instance_id\x18\x02 \x01(\tB\x03\xe0A\x01\x12E\n\x10api_hub_instance\x18\x03 \x01(\x0b2&.google.cloud.apihub.v1.ApiHubInstanceB\x03\xe0A\x02"Y\n\x1bDeleteApiHubInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance"V\n\x18GetApiHubInstanceRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance"[\n\x1bLookupApiHubInstanceRequest\x12<\n\x06parent\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\x12$apihub.googleapis.com/ApiHubInstance"`\n\x1cLookupApiHubInstanceResponse\x12@\n\x10api_hub_instance\x18\x01 \x01(\x0b2&.google.cloud.apihub.v1.ApiHubInstance2\xcd\x07\n\x0cProvisioning\x12\x8e\x02\n\x14CreateApiHubInstance\x123.google.cloud.apihub.v1.CreateApiHubInstanceRequest\x1a\x1d.google.longrunning.Operation"\xa1\x01\xcaA#\n\x0eApiHubInstance\x12\x11OperationMetadata\xdaA+parent,api_hub_instance,api_hub_instance_id\x82\xd3\xe4\x93\x02G"3/v1/{parent=projects/*/locations/*}/apiHubInstances:\x10api_hub_instance\x12\xdb\x01\n\x14DeleteApiHubInstance\x123.google.cloud.apihub.v1.DeleteApiHubInstanceRequest\x1a\x1d.google.longrunning.Operation"o\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/apiHubInstances/*}\x12\xb1\x01\n\x11GetApiHubInstance\x120.google.cloud.apihub.v1.GetApiHubInstanceRequest\x1a&.google.cloud.apihub.v1.ApiHubInstance"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/apiHubInstances/*}\x12\xce\x01\n\x14LookupApiHubInstance\x123.google.cloud.apihub.v1.LookupApiHubInstanceRequest\x1a4.google.cloud.apihub.v1.LookupApiHubInstanceResponse"K\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/apiHubInstances:lookup\x1aI\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xba\x01\n\x1acom.google.cloud.apihub.v1B\x18ProvisioningServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.apihub.v1.provisioning_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.apihub.v1B\x18ProvisioningServiceProtoP\x01Z2cloud.google.com/go/apihub/apiv1/apihubpb;apihubpb\xaa\x02\x16Google.Cloud.ApiHub.V1\xca\x02\x16Google\\Cloud\\ApiHub\\V1\xea\x02\x19Google::Cloud::ApiHub::V1'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance_id']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance_id']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance']._loaded_options = None
    _globals['_CREATEAPIHUBINSTANCEREQUEST'].fields_by_name['api_hub_instance']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEAPIHUBINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEAPIHUBINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance'
    _globals['_GETAPIHUBINSTANCEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAPIHUBINSTANCEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$apihub.googleapis.com/ApiHubInstance'
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA&\x12$apihub.googleapis.com/ApiHubInstance'
    _globals['_PROVISIONING']._loaded_options = None
    _globals['_PROVISIONING']._serialized_options = b'\xcaA\x15apihub.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_PROVISIONING'].methods_by_name['CreateApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['CreateApiHubInstance']._serialized_options = b'\xcaA#\n\x0eApiHubInstance\x12\x11OperationMetadata\xdaA+parent,api_hub_instance,api_hub_instance_id\x82\xd3\xe4\x93\x02G"3/v1/{parent=projects/*/locations/*}/apiHubInstances:\x10api_hub_instance'
    _globals['_PROVISIONING'].methods_by_name['DeleteApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['DeleteApiHubInstance']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x025*3/v1/{name=projects/*/locations/*/apiHubInstances/*}'
    _globals['_PROVISIONING'].methods_by_name['GetApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['GetApiHubInstance']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=projects/*/locations/*/apiHubInstances/*}'
    _globals['_PROVISIONING'].methods_by_name['LookupApiHubInstance']._loaded_options = None
    _globals['_PROVISIONING'].methods_by_name['LookupApiHubInstance']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02<\x12:/v1/{parent=projects/*/locations/*}/apiHubInstances:lookup'
    _globals['_CREATEAPIHUBINSTANCEREQUEST']._serialized_start = 303
    _globals['_CREATEAPIHUBINSTANCEREQUEST']._serialized_end = 496
    _globals['_DELETEAPIHUBINSTANCEREQUEST']._serialized_start = 498
    _globals['_DELETEAPIHUBINSTANCEREQUEST']._serialized_end = 587
    _globals['_GETAPIHUBINSTANCEREQUEST']._serialized_start = 589
    _globals['_GETAPIHUBINSTANCEREQUEST']._serialized_end = 675
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST']._serialized_start = 677
    _globals['_LOOKUPAPIHUBINSTANCEREQUEST']._serialized_end = 768
    _globals['_LOOKUPAPIHUBINSTANCERESPONSE']._serialized_start = 770
    _globals['_LOOKUPAPIHUBINSTANCERESPONSE']._serialized_end = 866
    _globals['_PROVISIONING']._serialized_start = 869
    _globals['_PROVISIONING']._serialized_end = 1842