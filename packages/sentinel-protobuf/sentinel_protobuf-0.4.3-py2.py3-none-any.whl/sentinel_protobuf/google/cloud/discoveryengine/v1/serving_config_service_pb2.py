"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/serving_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import serving_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_serving__config__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/discoveryengine/v1/serving_config_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/discoveryengine/v1/serving_config.proto\x1a google/protobuf/field_mask.proto"\x9a\x01\n\x1aUpdateServingConfigRequest\x12K\n\x0eserving_config\x18\x01 \x01(\x0b2..google.cloud.discoveryengine.v1.ServingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask2\xd3\x04\n\x14ServingConfigService\x12\xe6\x03\n\x13UpdateServingConfig\x12;.google.cloud.discoveryengine.v1.UpdateServingConfigRequest\x1a..google.cloud.discoveryengine.v1.ServingConfig"\xe1\x02\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xbd\x022N/v1/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZn2\\/v1/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZk2Y/v1/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8c\x02\n#com.google.cloud.discoveryengine.v1B\x19ServingConfigServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.serving_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x19ServingConfigServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_SERVINGCONFIGSERVICE']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._serialized_options = b'\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xbd\x022N/v1/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZn2\\/v1/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZk2Y/v1/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config'
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_start = 301
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_end = 455
    _globals['_SERVINGCONFIGSERVICE']._serialized_start = 458
    _globals['_SERVINGCONFIGSERVICE']._serialized_end = 1053