"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/deployment_resource_pool_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import deployed_model_ref_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_deployed__model__ref__pb2
from .....google.cloud.aiplatform.v1beta1 import deployment_resource_pool_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_deployment__resource__pool__pb2
from .....google.cloud.aiplatform.v1beta1 import endpoint_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_endpoint__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/cloud/aiplatform/v1beta1/deployment_resource_pool_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/aiplatform/v1beta1/deployed_model_ref.proto\x1a>google/cloud/aiplatform/v1beta1/deployment_resource_pool.proto\x1a.google/cloud/aiplatform/v1beta1/endpoint.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xea\x01\n#CreateDeploymentResourcePoolRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12^\n\x18deployment_resource_pool\x18\x02 \x01(\x0b27.google.cloud.aiplatform.v1beta1.DeploymentResourcePoolB\x03\xe0A\x02\x12(\n\x1bdeployment_resource_pool_id\x18\x03 \x01(\tB\x03\xe0A\x02"\x84\x01\n-CreateDeploymentResourcePoolOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"j\n GetDeploymentResourcePoolRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePool"\x86\x01\n"ListDeploymentResourcePoolsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\x12!locations.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x9a\x01\n#ListDeploymentResourcePoolsResponse\x12Z\n\x19deployment_resource_pools\x18\x01 \x03(\x0b27.google.cloud.aiplatform.v1beta1.DeploymentResourcePool\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xbb\x01\n#UpdateDeploymentResourcePoolRequest\x12^\n\x18deployment_resource_pool\x18\x01 \x01(\x0b27.google.cloud.aiplatform.v1beta1.DeploymentResourcePoolB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"\x84\x01\n-UpdateDeploymentResourcePoolOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"m\n#DeleteDeploymentResourcePoolRequest\x12F\n\x04name\x18\x01 \x01(\tB8\xe0A\x02\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePool"j\n\x1aQueryDeployedModelsRequest\x12%\n\x18deployment_resource_pool\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x95\x02\n\x1bQueryDeployedModelsResponse\x12K\n\x0fdeployed_models\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1beta1.DeployedModelB\x02\x18\x01\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12N\n\x13deployed_model_refs\x18\x03 \x03(\x0b21.google.cloud.aiplatform.v1beta1.DeployedModelRef\x12"\n\x1atotal_deployed_model_count\x18\x04 \x01(\x05\x12\x1c\n\x14total_endpoint_count\x18\x05 \x01(\x052\xd4\x0e\n\x1dDeploymentResourcePoolService\x12\xd9\x02\n\x1cCreateDeploymentResourcePool\x12D.google.cloud.aiplatform.v1beta1.CreateDeploymentResourcePoolRequest\x1a\x1d.google.longrunning.Operation"\xd3\x01\xcaAG\n\x16DeploymentResourcePool\x12-CreateDeploymentResourcePoolOperationMetadata\xdaA;parent,deployment_resource_pool,deployment_resource_pool_id\x82\xd3\xe4\x93\x02E"@/v1beta1/{parent=projects/*/locations/*}/deploymentResourcePools:\x01*\x12\xe8\x01\n\x19GetDeploymentResourcePool\x12A.google.cloud.aiplatform.v1beta1.GetDeploymentResourcePoolRequest\x1a7.google.cloud.aiplatform.v1beta1.DeploymentResourcePool"O\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}\x12\xfb\x01\n\x1bListDeploymentResourcePools\x12C.google.cloud.aiplatform.v1beta1.ListDeploymentResourcePoolsRequest\x1aD.google.cloud.aiplatform.v1beta1.ListDeploymentResourcePoolsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*}/deploymentResourcePools\x12\xf2\x02\n\x1cUpdateDeploymentResourcePool\x12D.google.cloud.aiplatform.v1beta1.UpdateDeploymentResourcePoolRequest\x1a\x1d.google.longrunning.Operation"\xec\x01\xcaAG\n\x16DeploymentResourcePool\x12-UpdateDeploymentResourcePoolOperationMetadata\xdaA$deployment_resource_pool,update_mask\x82\xd3\xe4\x93\x02u2Y/v1beta1/{deployment_resource_pool.name=projects/*/locations/*/deploymentResourcePools/*}:\x18deployment_resource_pool\x12\x88\x02\n\x1cDeleteDeploymentResourcePool\x12D.google.cloud.aiplatform.v1beta1.DeleteDeploymentResourcePoolRequest\x1a\x1d.google.longrunning.Operation"\x82\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}\x12\x9e\x02\n\x13QueryDeployedModels\x12;.google.cloud.aiplatform.v1beta1.QueryDeployedModelsRequest\x1a<.google.cloud.aiplatform.v1beta1.QueryDeployedModelsResponse"\x8b\x01\xdaA\x18deployment_resource_pool\x82\xd3\xe4\x93\x02j\x12h/v1beta1/{deployment_resource_pool=projects/*/locations/*/deploymentResourcePools/*}:queryDeployedModels\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf9\x01\n#com.google.cloud.aiplatform.v1beta1B"DeploymentResourcePoolServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.deployment_resource_pool_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B"DeploymentResourcePoolServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool']._loaded_options = None
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool_id']._loaded_options = None
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePool'
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\x12!locations.googleapis.com/Location'
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool']._loaded_options = None
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['deployment_resource_pool']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDEPLOYMENTRESOURCEPOOLREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA2\n0aiplatform.googleapis.com/DeploymentResourcePool'
    _globals['_QUERYDEPLOYEDMODELSREQUEST'].fields_by_name['deployment_resource_pool']._loaded_options = None
    _globals['_QUERYDEPLOYEDMODELSREQUEST'].fields_by_name['deployment_resource_pool']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYDEPLOYEDMODELSRESPONSE'].fields_by_name['deployed_models']._loaded_options = None
    _globals['_QUERYDEPLOYEDMODELSRESPONSE'].fields_by_name['deployed_models']._serialized_options = b'\x18\x01'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['CreateDeploymentResourcePool']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['CreateDeploymentResourcePool']._serialized_options = b'\xcaAG\n\x16DeploymentResourcePool\x12-CreateDeploymentResourcePoolOperationMetadata\xdaA;parent,deployment_resource_pool,deployment_resource_pool_id\x82\xd3\xe4\x93\x02E"@/v1beta1/{parent=projects/*/locations/*}/deploymentResourcePools:\x01*'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['GetDeploymentResourcePool']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['GetDeploymentResourcePool']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['ListDeploymentResourcePools']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['ListDeploymentResourcePools']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B\x12@/v1beta1/{parent=projects/*/locations/*}/deploymentResourcePools'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['UpdateDeploymentResourcePool']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['UpdateDeploymentResourcePool']._serialized_options = b'\xcaAG\n\x16DeploymentResourcePool\x12-UpdateDeploymentResourcePoolOperationMetadata\xdaA$deployment_resource_pool,update_mask\x82\xd3\xe4\x93\x02u2Y/v1beta1/{deployment_resource_pool.name=projects/*/locations/*/deploymentResourcePools/*}:\x18deployment_resource_pool'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['DeleteDeploymentResourcePool']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['DeleteDeploymentResourcePool']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02B*@/v1beta1/{name=projects/*/locations/*/deploymentResourcePools/*}'
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['QueryDeployedModels']._loaded_options = None
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE'].methods_by_name['QueryDeployedModels']._serialized_options = b'\xdaA\x18deployment_resource_pool\x82\xd3\xe4\x93\x02j\x12h/v1beta1/{deployment_resource_pool=projects/*/locations/*/deploymentResourcePools/*}:queryDeployedModels'
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_start = 542
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_end = 776
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLOPERATIONMETADATA']._serialized_start = 779
    _globals['_CREATEDEPLOYMENTRESOURCEPOOLOPERATIONMETADATA']._serialized_end = 911
    _globals['_GETDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_start = 913
    _globals['_GETDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_end = 1019
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSREQUEST']._serialized_start = 1022
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSREQUEST']._serialized_end = 1156
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSRESPONSE']._serialized_start = 1159
    _globals['_LISTDEPLOYMENTRESOURCEPOOLSRESPONSE']._serialized_end = 1313
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_start = 1316
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_end = 1503
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLOPERATIONMETADATA']._serialized_start = 1506
    _globals['_UPDATEDEPLOYMENTRESOURCEPOOLOPERATIONMETADATA']._serialized_end = 1638
    _globals['_DELETEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_start = 1640
    _globals['_DELETEDEPLOYMENTRESOURCEPOOLREQUEST']._serialized_end = 1749
    _globals['_QUERYDEPLOYEDMODELSREQUEST']._serialized_start = 1751
    _globals['_QUERYDEPLOYEDMODELSREQUEST']._serialized_end = 1857
    _globals['_QUERYDEPLOYEDMODELSRESPONSE']._serialized_start = 1860
    _globals['_QUERYDEPLOYEDMODELSRESPONSE']._serialized_end = 2137
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE']._serialized_start = 2140
    _globals['_DEPLOYMENTRESOURCEPOOLSERVICE']._serialized_end = 4016