"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/model_garden_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_machine__resources__pb2
from .....google.cloud.aiplatform.v1 import model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_model__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.cloud.aiplatform.v1 import publisher_model_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_publisher__model__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1/model_garden_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/aiplatform/v1/machine_resources.proto\x1a&google/cloud/aiplatform/v1/model.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a0google/cloud/aiplatform/v1/publisher_model.proto\x1a#google/longrunning/operations.proto"\xfe\x01\n\x18GetPublisherModelRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/PublisherModel\x12\x1a\n\rlanguage_code\x18\x02 \x01(\tB\x03\xe0A\x01\x12A\n\x04view\x18\x03 \x01(\x0e2..google.cloud.aiplatform.v1.PublisherModelViewB\x03\xe0A\x01\x12"\n\x15is_hugging_face_model\x18\x05 \x01(\x08B\x03\xe0A\x01\x12\x1f\n\x12hugging_face_token\x18\x06 \x01(\tB\x03\xe0A\x01"\x9d\t\n\rDeployRequest\x12M\n\x14publisher_model_name\x18\x01 \x01(\tB-\xfaA*\n(aiplatform.googleapis.com/PublisherModelH\x00\x12\x1f\n\x15hugging_face_model_id\x18\x02 \x01(\tH\x00\x12>\n\x0bdestination\x18\x04 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12P\n\x0cmodel_config\x18\x05 \x01(\x0b25.google.cloud.aiplatform.v1.DeployRequest.ModelConfigB\x03\xe0A\x01\x12V\n\x0fendpoint_config\x18\x06 \x01(\x0b28.google.cloud.aiplatform.v1.DeployRequest.EndpointConfigB\x03\xe0A\x01\x12R\n\rdeploy_config\x18\x07 \x01(\x0b26.google.cloud.aiplatform.v1.DeployRequest.DeployConfigB\x03\xe0A\x01\x1a\x82\x02\n\x0bModelConfig\x12\x18\n\x0baccept_eula\x18\x01 \x01(\x08B\x03\xe0A\x01\x12&\n\x19hugging_face_access_token\x18\x02 \x01(\tB\x03\xe0A\x01\x12\'\n\x1ahugging_face_cache_enabled\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x1f\n\x12model_display_name\x18\x04 \x01(\tB\x03\xe0A\x01\x12K\n\x0econtainer_spec\x18\x05 \x01(\x0b2..google.cloud.aiplatform.v1.ModelContainerSpecB\x03\xe0A\x01\x12\x1a\n\rmodel_user_id\x18\x06 \x01(\tB\x03\xe0A\x01\x1a\xab\x01\n\x0eEndpointConfig\x12"\n\x15endpoint_display_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12)\n\x1adedicated_endpoint_enabled\x18\x02 \x01(\x08B\x05\x18\x01\xe0A\x01\x12(\n\x1bdedicated_endpoint_disabled\x18\x04 \x01(\x08B\x03\xe0A\x01\x12 \n\x10endpoint_user_id\x18\x03 \x01(\tB\x06\xe0A\x05\xe0A\x01\x1a\x9d\x02\n\x0cDeployConfig\x12P\n\x13dedicated_resources\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1.DedicatedResourcesB\x03\xe0A\x01\x12 \n\x13fast_tryout_enabled\x18\x02 \x01(\x08B\x03\xe0A\x01\x12d\n\rsystem_labels\x18\x03 \x03(\x0b2H.google.cloud.aiplatform.v1.DeployRequest.DeployConfig.SystemLabelsEntryB\x03\xe0A\x01\x1a3\n\x11SystemLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x0b\n\tartifacts"\xd1\x01\n\x0eDeployResponse\x12I\n\x0fpublisher_model\x18\x01 \x01(\tB0\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/PublisherModel\x12<\n\x08endpoint\x18\x02 \x01(\tB*\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Endpoint\x126\n\x05model\x18\x03 \x01(\tB\'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model"\xa8\x02\n\x17DeployOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata\x12I\n\x0fpublisher_model\x18\x02 \x01(\tB0\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/PublisherModel\x12>\n\x0bdestination\x18\x03 \x01(\tB)\xe0A\x03\xfaA#\n!locations.googleapis.com/Location\x12\x1b\n\x0eproject_number\x18\x04 \x01(\x03B\x03\xe0A\x03\x12\x15\n\x08model_id\x18\x05 \x01(\tB\x03\xe0A\x03*\xa1\x01\n\x12PublisherModelView\x12$\n PUBLISHER_MODEL_VIEW_UNSPECIFIED\x10\x00\x12\x1e\n\x1aPUBLISHER_MODEL_VIEW_BASIC\x10\x01\x12\x1d\n\x19PUBLISHER_MODEL_VIEW_FULL\x10\x02\x12&\n"PUBLISHER_MODEL_VERSION_VIEW_BASIC\x10\x032\xc9\x03\n\x12ModelGardenService\x12\xa6\x01\n\x11GetPublisherModel\x124.google.cloud.aiplatform.v1.GetPublisherModelRequest\x1a*.google.cloud.aiplatform.v1.PublisherModel"/\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1/{name=publishers/*/models/*}\x12\xba\x01\n\x06Deploy\x12).google.cloud.aiplatform.v1.DeployRequest\x1a\x1d.google.longrunning.Operation"f\xcaA)\n\x0eDeployResponse\x12\x17DeployOperationMetadata\x82\xd3\xe4\x93\x024"//v1/{destination=projects/*/locations/*}:deploy:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd5\x01\n\x1ecom.google.cloud.aiplatform.v1B\x17ModelGardenServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.model_garden_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x17ModelGardenServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(aiplatform.googleapis.com/PublisherModel'
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['language_code']._loaded_options = None
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['language_code']._serialized_options = b'\xe0A\x01'
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['view']._loaded_options = None
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['view']._serialized_options = b'\xe0A\x01'
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['is_hugging_face_model']._loaded_options = None
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['is_hugging_face_model']._serialized_options = b'\xe0A\x01'
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['hugging_face_token']._loaded_options = None
    _globals['_GETPUBLISHERMODELREQUEST'].fields_by_name['hugging_face_token']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['accept_eula']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['accept_eula']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['hugging_face_access_token']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['hugging_face_access_token']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['hugging_face_cache_enabled']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['hugging_face_cache_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['model_display_name']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['model_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['container_spec']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['container_spec']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['model_user_id']._loaded_options = None
    _globals['_DEPLOYREQUEST_MODELCONFIG'].fields_by_name['model_user_id']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['endpoint_display_name']._loaded_options = None
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['endpoint_display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['dedicated_endpoint_enabled']._loaded_options = None
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['dedicated_endpoint_enabled']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['dedicated_endpoint_disabled']._loaded_options = None
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['dedicated_endpoint_disabled']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['endpoint_user_id']._loaded_options = None
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG'].fields_by_name['endpoint_user_id']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG_SYSTEMLABELSENTRY']._loaded_options = None
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG_SYSTEMLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['dedicated_resources']._loaded_options = None
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['dedicated_resources']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['fast_tryout_enabled']._loaded_options = None
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['fast_tryout_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['system_labels']._loaded_options = None
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG'].fields_by_name['system_labels']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST'].fields_by_name['publisher_model_name']._loaded_options = None
    _globals['_DEPLOYREQUEST'].fields_by_name['publisher_model_name']._serialized_options = b'\xfaA*\n(aiplatform.googleapis.com/PublisherModel'
    _globals['_DEPLOYREQUEST'].fields_by_name['destination']._loaded_options = None
    _globals['_DEPLOYREQUEST'].fields_by_name['destination']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DEPLOYREQUEST'].fields_by_name['model_config']._loaded_options = None
    _globals['_DEPLOYREQUEST'].fields_by_name['model_config']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST'].fields_by_name['endpoint_config']._loaded_options = None
    _globals['_DEPLOYREQUEST'].fields_by_name['endpoint_config']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYREQUEST'].fields_by_name['deploy_config']._loaded_options = None
    _globals['_DEPLOYREQUEST'].fields_by_name['deploy_config']._serialized_options = b'\xe0A\x01'
    _globals['_DEPLOYRESPONSE'].fields_by_name['publisher_model']._loaded_options = None
    _globals['_DEPLOYRESPONSE'].fields_by_name['publisher_model']._serialized_options = b'\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/PublisherModel'
    _globals['_DEPLOYRESPONSE'].fields_by_name['endpoint']._loaded_options = None
    _globals['_DEPLOYRESPONSE'].fields_by_name['endpoint']._serialized_options = b'\xe0A\x03\xfaA$\n"aiplatform.googleapis.com/Endpoint'
    _globals['_DEPLOYRESPONSE'].fields_by_name['model']._loaded_options = None
    _globals['_DEPLOYRESPONSE'].fields_by_name['model']._serialized_options = b'\xe0A\x03\xfaA!\n\x1faiplatform.googleapis.com/Model'
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['publisher_model']._loaded_options = None
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['publisher_model']._serialized_options = b'\xe0A\x03\xfaA*\n(aiplatform.googleapis.com/PublisherModel'
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['destination']._loaded_options = None
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['destination']._serialized_options = b'\xe0A\x03\xfaA#\n!locations.googleapis.com/Location'
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['project_number']._loaded_options = None
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['project_number']._serialized_options = b'\xe0A\x03'
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['model_id']._loaded_options = None
    _globals['_DEPLOYOPERATIONMETADATA'].fields_by_name['model_id']._serialized_options = b'\xe0A\x03'
    _globals['_MODELGARDENSERVICE']._loaded_options = None
    _globals['_MODELGARDENSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_MODELGARDENSERVICE'].methods_by_name['GetPublisherModel']._loaded_options = None
    _globals['_MODELGARDENSERVICE'].methods_by_name['GetPublisherModel']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02"\x12 /v1/{name=publishers/*/models/*}'
    _globals['_MODELGARDENSERVICE'].methods_by_name['Deploy']._loaded_options = None
    _globals['_MODELGARDENSERVICE'].methods_by_name['Deploy']._serialized_options = b'\xcaA)\n\x0eDeployResponse\x12\x17DeployOperationMetadata\x82\xd3\xe4\x93\x024"//v1/{destination=projects/*/locations/*}:deploy:\x01*'
    _globals['_PUBLISHERMODELVIEW']._serialized_start = 2376
    _globals['_PUBLISHERMODELVIEW']._serialized_end = 2537
    _globals['_GETPUBLISHERMODELREQUEST']._serialized_start = 424
    _globals['_GETPUBLISHERMODELREQUEST']._serialized_end = 678
    _globals['_DEPLOYREQUEST']._serialized_start = 681
    _globals['_DEPLOYREQUEST']._serialized_end = 1862
    _globals['_DEPLOYREQUEST_MODELCONFIG']._serialized_start = 1129
    _globals['_DEPLOYREQUEST_MODELCONFIG']._serialized_end = 1387
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG']._serialized_start = 1390
    _globals['_DEPLOYREQUEST_ENDPOINTCONFIG']._serialized_end = 1561
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG']._serialized_start = 1564
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG']._serialized_end = 1849
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG_SYSTEMLABELSENTRY']._serialized_start = 1798
    _globals['_DEPLOYREQUEST_DEPLOYCONFIG_SYSTEMLABELSENTRY']._serialized_end = 1849
    _globals['_DEPLOYRESPONSE']._serialized_start = 1865
    _globals['_DEPLOYRESPONSE']._serialized_end = 2074
    _globals['_DEPLOYOPERATIONMETADATA']._serialized_start = 2077
    _globals['_DEPLOYOPERATIONMETADATA']._serialized_end = 2373
    _globals['_MODELGARDENSERVICE']._serialized_start = 2540
    _globals['_MODELGARDENSERVICE']._serialized_end = 2997