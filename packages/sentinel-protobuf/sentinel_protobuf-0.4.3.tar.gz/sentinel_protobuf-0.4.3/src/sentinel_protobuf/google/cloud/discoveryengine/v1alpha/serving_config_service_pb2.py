"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/serving_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import serving_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_serving__config__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/cloud/discoveryengine/v1alpha/serving_config_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a9google/cloud/discoveryengine/v1alpha/serving_config.proto\x1a google/protobuf/field_mask.proto"\x9f\x01\n\x1aUpdateServingConfigRequest\x12P\n\x0eserving_config\x18\x01 \x01(\x0b23.google.cloud.discoveryengine.v1alpha.ServingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"]\n\x17GetServingConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig"\x92\x01\n\x19ListServingConfigsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,discoveryengine.googleapis.com/ServingConfig\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x83\x01\n\x1aListServingConfigsResponse\x12L\n\x0fserving_configs\x18\x01 \x03(\x0b23.google.cloud.discoveryengine.v1alpha.ServingConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x91\x0b\n\x14ServingConfigService\x12\xff\x03\n\x13UpdateServingConfig\x12@.google.cloud.discoveryengine.v1alpha.UpdateServingConfigRequest\x1a3.google.cloud.discoveryengine.v1alpha.ServingConfig"\xf0\x02\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xcc\x022S/v1alpha/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZs2a/v1alpha/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZp2^/v1alpha/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config\x12\x86\x03\n\x10GetServingConfig\x12=.google.cloud.discoveryengine.v1alpha.GetServingConfigRequest\x1a3.google.cloud.discoveryengine.v1alpha.ServingConfig"\xfd\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xef\x01\x12D/v1alpha/{name=projects/*/locations/*/dataStores/*/servingConfigs/*}ZT\x12R/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}ZQ\x12O/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}\x12\x99\x03\n\x12ListServingConfigs\x12?.google.cloud.discoveryengine.v1alpha.ListServingConfigsRequest\x1a@.google.cloud.discoveryengine.v1alpha.ListServingConfigsResponse"\xff\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xef\x01\x12D/v1alpha/{parent=projects/*/locations/*/dataStores/*}/servingConfigsZT\x12R/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/servingConfigsZQ\x12O/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/servingConfigs\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa5\x02\n(com.google.cloud.discoveryengine.v1alphaB\x19ServingConfigServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.serving_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x19ServingConfigServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_UPDATESERVINGCONFIGREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02'
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSERVINGCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,discoveryengine.googleapis.com/ServingConfig'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSERVINGCONFIGSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_SERVINGCONFIGSERVICE']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._serialized_options = b'\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xcc\x022S/v1alpha/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZs2a/v1alpha/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZp2^/v1alpha/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xef\x01\x12D/v1alpha/{name=projects/*/locations/*/dataStores/*/servingConfigs/*}ZT\x12R/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}ZQ\x12O/v1alpha/{name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xef\x01\x12D/v1alpha/{parent=projects/*/locations/*/dataStores/*}/servingConfigsZT\x12R/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*}/servingConfigsZQ\x12O/v1alpha/{parent=projects/*/locations/*/collections/*/engines/*}/servingConfigs'
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_start = 316
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_end = 475
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_start = 477
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_end = 570
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_start = 573
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_end = 719
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_start = 722
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_end = 853
    _globals['_SERVINGCONFIGSERVICE']._serialized_start = 856
    _globals['_SERVINGCONFIGSERVICE']._serialized_end = 2281