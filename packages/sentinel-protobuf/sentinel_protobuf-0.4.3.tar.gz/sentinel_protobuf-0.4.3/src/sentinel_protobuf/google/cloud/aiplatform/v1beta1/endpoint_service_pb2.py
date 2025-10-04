"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/endpoint_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import deployment_stage_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_deployment__stage__pb2
from .....google.cloud.aiplatform.v1beta1 import endpoint_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_endpoint__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/aiplatform/v1beta1/endpoint_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a6google/cloud/aiplatform/v1beta1/deployment_stage.proto\x1a.google/cloud/aiplatform/v1beta1/endpoint.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xae\x01\n\x15CreateEndpointRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12@\n\x08endpoint\x18\x02 \x01(\x0b2).google.cloud.aiplatform.v1beta1.EndpointB\x03\xe0A\x02\x12\x18\n\x0bendpoint_id\x18\x04 \x01(\tB\x03\xe0A\x05"\xc7\x01\n\x1fCreateEndpointOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12O\n\x10deployment_stage\x18\x02 \x01(\x0e20.google.cloud.aiplatform.v1beta1.DeploymentStageB\x03\xe0A\x03"N\n\x12GetEndpointRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint"\xcb\x01\n\x14ListEndpointsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01\x122\n\tread_mask\x18\x05 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"n\n\x15ListEndpointsResponse\x12<\n\tendpoints\x18\x01 \x03(\x0b2).google.cloud.aiplatform.v1beta1.Endpoint\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8f\x01\n\x15UpdateEndpointRequest\x12@\n\x08endpoint\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1beta1.EndpointB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"d\n UpdateEndpointLongRunningRequest\x12@\n\x08endpoint\x18\x01 \x01(\x0b2).google.cloud.aiplatform.v1beta1.EndpointB\x03\xe0A\x02"v\n\x1fUpdateEndpointOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"Q\n\x15DeleteEndpointRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint"\xb2\x02\n\x12DeployModelRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12K\n\x0edeployed_model\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModelB\x03\xe0A\x02\x12\\\n\rtraffic_split\x18\x03 \x03(\x0b2E.google.cloud.aiplatform.v1beta1.DeployModelRequest.TrafficSplitEntry\x1a3\n\x11TrafficSplitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01"]\n\x13DeployModelResponse\x12F\n\x0edeployed_model\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModel"\xc4\x01\n\x1cDeployModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata\x12O\n\x10deployment_stage\x18\x02 \x01(\x0e20.google.cloud.aiplatform.v1beta1.DeploymentStageB\x03\xe0A\x03"\x89\x02\n\x14UndeployModelRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12\x1e\n\x11deployed_model_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12^\n\rtraffic_split\x18\x03 \x03(\x0b2G.google.cloud.aiplatform.v1beta1.UndeployModelRequest.TrafficSplitEntry\x1a3\n\x11TrafficSplitEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01"\x17\n\x15UndeployModelResponse"\xb6\x01\n\x1eSetPublisherModelConfigRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12Z\n\x16publisher_model_config\x18\x02 \x01(\x0b25.google.cloud.aiplatform.v1beta1.PublisherModelConfigB\x03\xe0A\x02"\x7f\n(SetPublisherModelConfigOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\\\n FetchPublisherModelConfigRequest\x128\n\x04name\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint"u\n\x1eUndeployModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\xdd\x01\n\x1aMutateDeployedModelRequest\x12<\n\x08endpoint\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint\x12K\n\x0edeployed_model\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModelB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"e\n\x1bMutateDeployedModelResponse\x12F\n\x0edeployed_model\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModel"{\n$MutateDeployedModelOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata2\xd4\x16\n\x0fEndpointService\x12\x8c\x02\n\x0eCreateEndpoint\x126.google.cloud.aiplatform.v1beta1.CreateEndpointRequest\x1a\x1d.google.longrunning.Operation"\xa2\x01\xcaA+\n\x08Endpoint\x12\x1fCreateEndpointOperationMetadata\xdaA\x0fparent,endpoint\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/endpoints:\x08endpoint\x12\xb0\x01\n\x0bGetEndpoint\x123.google.cloud.aiplatform.v1beta1.GetEndpointRequest\x1a).google.cloud.aiplatform.v1beta1.Endpoint"A\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/endpoints/*}\x12\xc3\x01\n\rListEndpoints\x125.google.cloud.aiplatform.v1beta1.ListEndpointsRequest\x1a6.google.cloud.aiplatform.v1beta1.ListEndpointsResponse"C\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/endpoints\x12\xd9\x01\n\x0eUpdateEndpoint\x126.google.cloud.aiplatform.v1beta1.UpdateEndpointRequest\x1a).google.cloud.aiplatform.v1beta1.Endpoint"d\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02G2;/v1beta1/{endpoint.name=projects/*/locations/*/endpoints/*}:\x08endpoint\x12\x86\x02\n\x19UpdateEndpointLongRunning\x12A.google.cloud.aiplatform.v1beta1.UpdateEndpointLongRunningRequest\x1a\x1d.google.longrunning.Operation"\x86\x01\xcaA+\n\x08Endpoint\x12\x1fUpdateEndpointOperationMetadata\xdaA\x08endpoint\x82\xd3\xe4\x93\x02G"B/v1beta1/{endpoint.name=projects/*/locations/*/endpoints/*}:update:\x01*\x12\xdd\x01\n\x0eDeleteEndpoint\x126.google.cloud.aiplatform.v1beta1.DeleteEndpointRequest\x1a\x1d.google.longrunning.Operation"t\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/endpoints/*}\x12\x8f\x02\n\x0bDeployModel\x123.google.cloud.aiplatform.v1beta1.DeployModelRequest\x1a\x1d.google.longrunning.Operation"\xab\x01\xcaA3\n\x13DeployModelResponse\x12\x1cDeployModelOperationMetadata\xdaA%endpoint,deployed_model,traffic_split\x82\xd3\xe4\x93\x02G"B/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:deployModel:\x01*\x12\x9c\x02\n\rUndeployModel\x125.google.cloud.aiplatform.v1beta1.UndeployModelRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaA7\n\x15UndeployModelResponse\x12\x1eUndeployModelOperationMetadata\xdaA(endpoint,deployed_model_id,traffic_split\x82\xd3\xe4\x93\x02I"D/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:undeployModel:\x01*\x12\xb5\x02\n\x13MutateDeployedModel\x12;.google.cloud.aiplatform.v1beta1.MutateDeployedModelRequest\x1a\x1d.google.longrunning.Operation"\xc1\x01\xcaAC\n\x1bMutateDeployedModelResponse\x12$MutateDeployedModelOperationMetadata\xdaA#endpoint,deployed_model,update_mask\x82\xd3\xe4\x93\x02O"J/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:mutateDeployedModel:\x01*\x12\xbc\x02\n\x17SetPublisherModelConfig\x12?.google.cloud.aiplatform.v1beta1.SetPublisherModelConfigRequest\x1a\x1d.google.longrunning.Operation"\xc0\x01\xcaA@\n\x14PublisherModelConfig\x12(SetPublisherModelConfigOperationMetadata\xdaA\x1bname,publisher_model_config\x82\xd3\xe4\x93\x02Y"T/v1beta1/{name=projects/*/locations/*/publishers/*/models/*}:setPublisherModelConfig:\x01*\x12\xfc\x01\n\x19FetchPublisherModelConfig\x12A.google.cloud.aiplatform.v1beta1.FetchPublisherModelConfigRequest\x1a5.google.cloud.aiplatform.v1beta1.PublisherModelConfig"e\xdaA\x04name\x82\xd3\xe4\x93\x02X\x12V/v1beta1/{name=projects/*/locations/*/publishers/*/models/*}:fetchPublisherModelConfig\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xeb\x01\n#com.google.cloud.aiplatform.v1beta1B\x14EndpointServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.endpoint_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x14EndpointServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._loaded_options = None
    _globals['_CREATEENDPOINTREQUEST'].fields_by_name['endpoint_id']._serialized_options = b'\xe0A\x05'
    _globals['_CREATEENDPOINTOPERATIONMETADATA'].fields_by_name['deployment_stage']._loaded_options = None
    _globals['_CREATEENDPOINTOPERATIONMETADATA'].fields_by_name['deployment_stage']._serialized_options = b'\xe0A\x03'
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['read_mask']._loaded_options = None
    _globals['_LISTENDPOINTSREQUEST'].fields_by_name['read_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEENDPOINTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEENDPOINTLONGRUNNINGREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_UPDATEENDPOINTLONGRUNNINGREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEENDPOINTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._loaded_options = None
    _globals['_DEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_options = b'8\x01'
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['deployed_model']._loaded_options = None
    _globals['_DEPLOYMODELREQUEST'].fields_by_name['deployed_model']._serialized_options = b'\xe0A\x02'
    _globals['_DEPLOYMODELOPERATIONMETADATA'].fields_by_name['deployment_stage']._loaded_options = None
    _globals['_DEPLOYMODELOPERATIONMETADATA'].fields_by_name['deployment_stage']._serialized_options = b'\xe0A\x03'
    _globals['_UNDEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._loaded_options = None
    _globals['_UNDEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_options = b'8\x01'
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['deployed_model_id']._loaded_options = None
    _globals['_UNDEPLOYMODELREQUEST'].fields_by_name['deployed_model_id']._serialized_options = b'\xe0A\x02'
    _globals['_SETPUBLISHERMODELCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SETPUBLISHERMODELCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_SETPUBLISHERMODELCONFIGREQUEST'].fields_by_name['publisher_model_config']._loaded_options = None
    _globals['_SETPUBLISHERMODELCONFIGREQUEST'].fields_by_name['publisher_model_config']._serialized_options = b'\xe0A\x02'
    _globals['_FETCHPUBLISHERMODELCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FETCHPUBLISHERMODELCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['endpoint']._loaded_options = None
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x02\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._loaded_options = None
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['deployed_model']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_MUTATEDEPLOYEDMODELREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_ENDPOINTSERVICE']._loaded_options = None
    _globals['_ENDPOINTSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ENDPOINTSERVICE'].methods_by_name['CreateEndpoint']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['CreateEndpoint']._serialized_options = b'\xcaA+\n\x08Endpoint\x12\x1fCreateEndpointOperationMetadata\xdaA\x0fparent,endpoint\xdaA\x1bparent,endpoint,endpoint_id\x82\xd3\xe4\x93\x02>"2/v1beta1/{parent=projects/*/locations/*}/endpoints:\x08endpoint'
    _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoint']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['GetEndpoint']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x024\x122/v1beta1/{name=projects/*/locations/*/endpoints/*}'
    _globals['_ENDPOINTSERVICE'].methods_by_name['ListEndpoints']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['ListEndpoints']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x024\x122/v1beta1/{parent=projects/*/locations/*}/endpoints'
    _globals['_ENDPOINTSERVICE'].methods_by_name['UpdateEndpoint']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['UpdateEndpoint']._serialized_options = b'\xdaA\x14endpoint,update_mask\x82\xd3\xe4\x93\x02G2;/v1beta1/{endpoint.name=projects/*/locations/*/endpoints/*}:\x08endpoint'
    _globals['_ENDPOINTSERVICE'].methods_by_name['UpdateEndpointLongRunning']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['UpdateEndpointLongRunning']._serialized_options = b'\xcaA+\n\x08Endpoint\x12\x1fUpdateEndpointOperationMetadata\xdaA\x08endpoint\x82\xd3\xe4\x93\x02G"B/v1beta1/{endpoint.name=projects/*/locations/*/endpoints/*}:update:\x01*'
    _globals['_ENDPOINTSERVICE'].methods_by_name['DeleteEndpoint']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['DeleteEndpoint']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x024*2/v1beta1/{name=projects/*/locations/*/endpoints/*}'
    _globals['_ENDPOINTSERVICE'].methods_by_name['DeployModel']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['DeployModel']._serialized_options = b'\xcaA3\n\x13DeployModelResponse\x12\x1cDeployModelOperationMetadata\xdaA%endpoint,deployed_model,traffic_split\x82\xd3\xe4\x93\x02G"B/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:deployModel:\x01*'
    _globals['_ENDPOINTSERVICE'].methods_by_name['UndeployModel']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['UndeployModel']._serialized_options = b'\xcaA7\n\x15UndeployModelResponse\x12\x1eUndeployModelOperationMetadata\xdaA(endpoint,deployed_model_id,traffic_split\x82\xd3\xe4\x93\x02I"D/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:undeployModel:\x01*'
    _globals['_ENDPOINTSERVICE'].methods_by_name['MutateDeployedModel']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['MutateDeployedModel']._serialized_options = b'\xcaAC\n\x1bMutateDeployedModelResponse\x12$MutateDeployedModelOperationMetadata\xdaA#endpoint,deployed_model,update_mask\x82\xd3\xe4\x93\x02O"J/v1beta1/{endpoint=projects/*/locations/*/endpoints/*}:mutateDeployedModel:\x01*'
    _globals['_ENDPOINTSERVICE'].methods_by_name['SetPublisherModelConfig']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['SetPublisherModelConfig']._serialized_options = b'\xcaA@\n\x14PublisherModelConfig\x12(SetPublisherModelConfigOperationMetadata\xdaA\x1bname,publisher_model_config\x82\xd3\xe4\x93\x02Y"T/v1beta1/{name=projects/*/locations/*/publishers/*/models/*}:setPublisherModelConfig:\x01*'
    _globals['_ENDPOINTSERVICE'].methods_by_name['FetchPublisherModelConfig']._loaded_options = None
    _globals['_ENDPOINTSERVICE'].methods_by_name['FetchPublisherModelConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02X\x12V/v1beta1/{name=projects/*/locations/*/publishers/*/models/*}:fetchPublisherModelConfig'
    _globals['_CREATEENDPOINTREQUEST']._serialized_start = 460
    _globals['_CREATEENDPOINTREQUEST']._serialized_end = 634
    _globals['_CREATEENDPOINTOPERATIONMETADATA']._serialized_start = 637
    _globals['_CREATEENDPOINTOPERATIONMETADATA']._serialized_end = 836
    _globals['_GETENDPOINTREQUEST']._serialized_start = 838
    _globals['_GETENDPOINTREQUEST']._serialized_end = 916
    _globals['_LISTENDPOINTSREQUEST']._serialized_start = 919
    _globals['_LISTENDPOINTSREQUEST']._serialized_end = 1122
    _globals['_LISTENDPOINTSRESPONSE']._serialized_start = 1124
    _globals['_LISTENDPOINTSRESPONSE']._serialized_end = 1234
    _globals['_UPDATEENDPOINTREQUEST']._serialized_start = 1237
    _globals['_UPDATEENDPOINTREQUEST']._serialized_end = 1380
    _globals['_UPDATEENDPOINTLONGRUNNINGREQUEST']._serialized_start = 1382
    _globals['_UPDATEENDPOINTLONGRUNNINGREQUEST']._serialized_end = 1482
    _globals['_UPDATEENDPOINTOPERATIONMETADATA']._serialized_start = 1484
    _globals['_UPDATEENDPOINTOPERATIONMETADATA']._serialized_end = 1602
    _globals['_DELETEENDPOINTREQUEST']._serialized_start = 1604
    _globals['_DELETEENDPOINTREQUEST']._serialized_end = 1685
    _globals['_DEPLOYMODELREQUEST']._serialized_start = 1688
    _globals['_DEPLOYMODELREQUEST']._serialized_end = 1994
    _globals['_DEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_start = 1943
    _globals['_DEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_end = 1994
    _globals['_DEPLOYMODELRESPONSE']._serialized_start = 1996
    _globals['_DEPLOYMODELRESPONSE']._serialized_end = 2089
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_start = 2092
    _globals['_DEPLOYMODELOPERATIONMETADATA']._serialized_end = 2288
    _globals['_UNDEPLOYMODELREQUEST']._serialized_start = 2291
    _globals['_UNDEPLOYMODELREQUEST']._serialized_end = 2556
    _globals['_UNDEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_start = 1943
    _globals['_UNDEPLOYMODELREQUEST_TRAFFICSPLITENTRY']._serialized_end = 1994
    _globals['_UNDEPLOYMODELRESPONSE']._serialized_start = 2558
    _globals['_UNDEPLOYMODELRESPONSE']._serialized_end = 2581
    _globals['_SETPUBLISHERMODELCONFIGREQUEST']._serialized_start = 2584
    _globals['_SETPUBLISHERMODELCONFIGREQUEST']._serialized_end = 2766
    _globals['_SETPUBLISHERMODELCONFIGOPERATIONMETADATA']._serialized_start = 2768
    _globals['_SETPUBLISHERMODELCONFIGOPERATIONMETADATA']._serialized_end = 2895
    _globals['_FETCHPUBLISHERMODELCONFIGREQUEST']._serialized_start = 2897
    _globals['_FETCHPUBLISHERMODELCONFIGREQUEST']._serialized_end = 2989
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_start = 2991
    _globals['_UNDEPLOYMODELOPERATIONMETADATA']._serialized_end = 3108
    _globals['_MUTATEDEPLOYEDMODELREQUEST']._serialized_start = 3111
    _globals['_MUTATEDEPLOYEDMODELREQUEST']._serialized_end = 3332
    _globals['_MUTATEDEPLOYEDMODELRESPONSE']._serialized_start = 3334
    _globals['_MUTATEDEPLOYEDMODELRESPONSE']._serialized_end = 3435
    _globals['_MUTATEDEPLOYEDMODELOPERATIONMETADATA']._serialized_start = 3437
    _globals['_MUTATEDEPLOYEDMODELOPERATIONMETADATA']._serialized_end = 3560
    _globals['_ENDPOINTSERVICE']._serialized_start = 3563
    _globals['_ENDPOINTSERVICE']._serialized_end = 6463