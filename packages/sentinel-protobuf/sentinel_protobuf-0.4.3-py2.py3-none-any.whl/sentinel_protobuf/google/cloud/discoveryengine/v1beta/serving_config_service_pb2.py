"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/serving_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import serving_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_serving__config__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/discoveryengine/v1beta/serving_config_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/discoveryengine/v1beta/serving_config.proto\x1a google/protobuf/field_mask.proto"\x9e\x01\n\x1aUpdateServingConfigRequest\x12O\n\x0eserving_config\x18\x01 \x01(\x0b22.google.cloud.discoveryengine.v1beta.ServingConfigB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"]\n\x17GetServingConfigRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig"\x92\x01\n\x19ListServingConfigsRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,discoveryengine.googleapis.com/ServingConfig\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x82\x01\n\x1aListServingConfigsResponse\x12K\n\x0fserving_configs\x18\x01 \x03(\x0b22.google.cloud.discoveryengine.v1beta.ServingConfig\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x82\x0b\n\x14ServingConfigService\x12\xfa\x03\n\x13UpdateServingConfig\x12?.google.cloud.discoveryengine.v1beta.UpdateServingConfigRequest\x1a2.google.cloud.discoveryengine.v1beta.ServingConfig"\xed\x02\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xc9\x022R/v1beta/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZr2`/v1beta/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZo2]/v1beta/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config\x12\x81\x03\n\x10GetServingConfig\x12<.google.cloud.discoveryengine.v1beta.GetServingConfigRequest\x1a2.google.cloud.discoveryengine.v1beta.ServingConfig"\xfa\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xec\x01\x12C/v1beta/{name=projects/*/locations/*/dataStores/*/servingConfigs/*}ZS\x12Q/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}ZP\x12N/v1beta/{name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}\x12\x94\x03\n\x12ListServingConfigs\x12>.google.cloud.discoveryengine.v1beta.ListServingConfigsRequest\x1a?.google.cloud.discoveryengine.v1beta.ListServingConfigsResponse"\xfc\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xec\x01\x12C/v1beta/{parent=projects/*/locations/*/dataStores/*}/servingConfigsZS\x12Q/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/servingConfigsZP\x12N/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/servingConfigs\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa0\x02\n\'com.google.cloud.discoveryengine.v1betaB\x19ServingConfigServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.serving_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x19ServingConfigServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['UpdateServingConfig']._serialized_options = b'\xdaA\x1aserving_config,update_mask\x82\xd3\xe4\x93\x02\xc9\x022R/v1beta/{serving_config.name=projects/*/locations/*/dataStores/*/servingConfigs/*}:\x0eserving_configZr2`/v1beta/{serving_config.name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:\x0eserving_configZo2]/v1beta/{serving_config.name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:\x0eserving_config'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['GetServingConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xec\x01\x12C/v1beta/{name=projects/*/locations/*/dataStores/*/servingConfigs/*}ZS\x12Q/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}ZP\x12N/v1beta/{name=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}'
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._loaded_options = None
    _globals['_SERVINGCONFIGSERVICE'].methods_by_name['ListServingConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xec\x01\x12C/v1beta/{parent=projects/*/locations/*/dataStores/*}/servingConfigsZS\x12Q/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*}/servingConfigsZP\x12N/v1beta/{parent=projects/*/locations/*/collections/*/engines/*}/servingConfigs'
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_start = 313
    _globals['_UPDATESERVINGCONFIGREQUEST']._serialized_end = 471
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_start = 473
    _globals['_GETSERVINGCONFIGREQUEST']._serialized_end = 566
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_start = 569
    _globals['_LISTSERVINGCONFIGSREQUEST']._serialized_end = 715
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_start = 718
    _globals['_LISTSERVINGCONFIGSRESPONSE']._serialized_end = 848
    _globals['_SERVINGCONFIGSERVICE']._serialized_start = 851
    _globals['_SERVINGCONFIGSERVICE']._serialized_end = 2261