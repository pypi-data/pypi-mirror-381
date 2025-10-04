"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/cmek_config_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/discoveryengine/v1/cmek_config_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"p\n\x17UpdateCmekConfigRequest\x12@\n\x06config\x18\x01 \x01(\x0b2+.google.cloud.discoveryengine.v1.CmekConfigB\x03\xe0A\x02\x12\x13\n\x0bset_default\x18\x02 \x01(\x08"W\n\x14GetCmekConfigRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/CmekConfig"N\n\x0fSingleRegionKey\x12;\n\x07kms_key\x18\x01 \x01(\tB*\xe0A\x02\xfaA$\n"cloudkms.googleapis.com/CryptoKeys"\xc1\x07\n\nCmekConfig\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x128\n\x07kms_key\x18\x02 \x01(\tB\'\xfaA$\n"cloudkms.googleapis.com/CryptoKeys\x12G\n\x0fkms_key_version\x18\x06 \x01(\tB.\xfaA+\n)cloudkms.googleapis.com/CryptoKeyVersions\x12E\n\x05state\x18\x03 \x01(\x0e21.google.cloud.discoveryengine.v1.CmekConfig.StateB\x03\xe0A\x03\x12\x17\n\nis_default\x18\x04 \x01(\x08B\x03\xe0A\x03\x12+\n\x1elast_rotation_timestamp_micros\x18\x05 \x01(\x03B\x03\xe0A\x03\x12Q\n\x12single_region_keys\x18\x07 \x03(\x0b20.google.cloud.discoveryengine.v1.SingleRegionKeyB\x03\xe0A\x01\x12Z\n\x10notebooklm_state\x18\x08 \x01(\x0e2;.google.cloud.discoveryengine.v1.CmekConfig.NotebookLMStateB\x03\xe0A\x03"\x98\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\r\n\tKEY_ISSUE\x10\x03\x12\x0c\n\x08DELETING\x10\x04\x12\x11\n\rDELETE_FAILED\x10\x07\x12\x0c\n\x08UNUSABLE\x10\x05\x12\x13\n\x0fACTIVE_ROTATING\x10\x06\x12\x0b\n\x07DELETED\x10\x08"\x83\x01\n\x0fNotebookLMState\x12!\n\x1dNOTEBOOK_LM_STATE_UNSPECIFIED\x10\x00\x12\x19\n\x15NOTEBOOK_LM_NOT_READY\x10\x01\x12\x15\n\x11NOTEBOOK_LM_READY\x10\x02\x12\x1b\n\x17NOTEBOOK_LM_NOT_ENABLED\x10\x03:\xbf\x01\xeaA\xbb\x01\n)discoveryengine.googleapis.com/CmekConfig\x122projects/{project}/locations/{location}/cmekConfig\x12Aprojects/{project}/locations/{location}/cmekConfigs/{cmek_config}*\x0bcmekConfigs2\ncmekConfig"|\n\x18UpdateCmekConfigMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"Y\n\x16ListCmekConfigsRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location"\\\n\x17ListCmekConfigsResponse\x12A\n\x0ccmek_configs\x18\x01 \x03(\x0b2+.google.cloud.discoveryengine.v1.CmekConfig"Z\n\x17DeleteCmekConfigRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/CmekConfig"|\n\x18DeleteCmekConfigMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\x81\t\n\x11CmekConfigService\x12\xe5\x02\n\x10UpdateCmekConfig\x128.google.cloud.discoveryengine.v1.UpdateCmekConfigRequest\x1a\x1d.google.longrunning.Operation"\xf7\x01\xcaAf\n*google.cloud.discoveryengine.v1.CmekConfig\x128google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata\xdaA\x06config\x82\xd3\xe4\x93\x02\x7f23/v1/{config.name=projects/*/locations/*/cmekConfig}:\x06configZ@26/v1/{config.name=projects/*/locations/*/cmekConfigs/*}:\x06config\x12\xe3\x01\n\rGetCmekConfig\x125.google.cloud.discoveryengine.v1.GetCmekConfigRequest\x1a+.google.cloud.discoveryengine.v1.CmekConfig"n\xdaA\x04name\x82\xd3\xe4\x93\x02a\x12,/v1/{name=projects/*/locations/*/cmekConfig}Z1\x12//v1/{name=projects/*/locations/*/cmekConfigs/*}\x12\xc6\x01\n\x0fListCmekConfigs\x127.google.cloud.discoveryengine.v1.ListCmekConfigsRequest\x1a8.google.cloud.discoveryengine.v1.ListCmekConfigsResponse"@\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/cmekConfigs\x12\x80\x02\n\x10DeleteCmekConfig\x128.google.cloud.discoveryengine.v1.DeleteCmekConfigRequest\x1a\x1d.google.longrunning.Operation"\x92\x01\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/cmekConfigs/*}\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x89\x02\n#com.google.cloud.discoveryengine.v1B\x16CmekConfigServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.cmek_config_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x16CmekConfigServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_UPDATECMEKCONFIGREQUEST'].fields_by_name['config']._loaded_options = None
    _globals['_UPDATECMEKCONFIGREQUEST'].fields_by_name['config']._serialized_options = b'\xe0A\x02'
    _globals['_GETCMEKCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCMEKCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/CmekConfig'
    _globals['_SINGLEREGIONKEY'].fields_by_name['kms_key']._loaded_options = None
    _globals['_SINGLEREGIONKEY'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x02\xfaA$\n"cloudkms.googleapis.com/CryptoKeys'
    _globals['_CMEKCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_CMEKCONFIG'].fields_by_name['kms_key']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['kms_key']._serialized_options = b'\xfaA$\n"cloudkms.googleapis.com/CryptoKeys'
    _globals['_CMEKCONFIG'].fields_by_name['kms_key_version']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['kms_key_version']._serialized_options = b'\xfaA+\n)cloudkms.googleapis.com/CryptoKeyVersions'
    _globals['_CMEKCONFIG'].fields_by_name['state']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_CMEKCONFIG'].fields_by_name['is_default']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['is_default']._serialized_options = b'\xe0A\x03'
    _globals['_CMEKCONFIG'].fields_by_name['last_rotation_timestamp_micros']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['last_rotation_timestamp_micros']._serialized_options = b'\xe0A\x03'
    _globals['_CMEKCONFIG'].fields_by_name['single_region_keys']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['single_region_keys']._serialized_options = b'\xe0A\x01'
    _globals['_CMEKCONFIG'].fields_by_name['notebooklm_state']._loaded_options = None
    _globals['_CMEKCONFIG'].fields_by_name['notebooklm_state']._serialized_options = b'\xe0A\x03'
    _globals['_CMEKCONFIG']._loaded_options = None
    _globals['_CMEKCONFIG']._serialized_options = b'\xeaA\xbb\x01\n)discoveryengine.googleapis.com/CmekConfig\x122projects/{project}/locations/{location}/cmekConfig\x12Aprojects/{project}/locations/{location}/cmekConfigs/{cmek_config}*\x0bcmekConfigs2\ncmekConfig'
    _globals['_LISTCMEKCONFIGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCMEKCONFIGSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_DELETECMEKCONFIGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETECMEKCONFIGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)discoveryengine.googleapis.com/CmekConfig'
    _globals['_CMEKCONFIGSERVICE']._loaded_options = None
    _globals['_CMEKCONFIGSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['UpdateCmekConfig']._loaded_options = None
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['UpdateCmekConfig']._serialized_options = b'\xcaAf\n*google.cloud.discoveryengine.v1.CmekConfig\x128google.cloud.discoveryengine.v1.UpdateCmekConfigMetadata\xdaA\x06config\x82\xd3\xe4\x93\x02\x7f23/v1/{config.name=projects/*/locations/*/cmekConfig}:\x06configZ@26/v1/{config.name=projects/*/locations/*/cmekConfigs/*}:\x06config'
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['GetCmekConfig']._loaded_options = None
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['GetCmekConfig']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02a\x12,/v1/{name=projects/*/locations/*/cmekConfig}Z1\x12//v1/{name=projects/*/locations/*/cmekConfigs/*}'
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['ListCmekConfigs']._loaded_options = None
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['ListCmekConfigs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x021\x12//v1/{parent=projects/*/locations/*}/cmekConfigs'
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['DeleteCmekConfig']._loaded_options = None
    _globals['_CMEKCONFIGSERVICE'].methods_by_name['DeleteCmekConfig']._serialized_options = b'\xcaAQ\n\x15google.protobuf.Empty\x128google.cloud.discoveryengine.v1.DeleteCmekConfigMetadata\xdaA\x04name\x82\xd3\xe4\x93\x021*//v1/{name=projects/*/locations/*/cmekConfigs/*}'
    _globals['_UPDATECMEKCONFIGREQUEST']._serialized_start = 308
    _globals['_UPDATECMEKCONFIGREQUEST']._serialized_end = 420
    _globals['_GETCMEKCONFIGREQUEST']._serialized_start = 422
    _globals['_GETCMEKCONFIGREQUEST']._serialized_end = 509
    _globals['_SINGLEREGIONKEY']._serialized_start = 511
    _globals['_SINGLEREGIONKEY']._serialized_end = 589
    _globals['_CMEKCONFIG']._serialized_start = 592
    _globals['_CMEKCONFIG']._serialized_end = 1553
    _globals['_CMEKCONFIG_STATE']._serialized_start = 1073
    _globals['_CMEKCONFIG_STATE']._serialized_end = 1225
    _globals['_CMEKCONFIG_NOTEBOOKLMSTATE']._serialized_start = 1228
    _globals['_CMEKCONFIG_NOTEBOOKLMSTATE']._serialized_end = 1359
    _globals['_UPDATECMEKCONFIGMETADATA']._serialized_start = 1555
    _globals['_UPDATECMEKCONFIGMETADATA']._serialized_end = 1679
    _globals['_LISTCMEKCONFIGSREQUEST']._serialized_start = 1681
    _globals['_LISTCMEKCONFIGSREQUEST']._serialized_end = 1770
    _globals['_LISTCMEKCONFIGSRESPONSE']._serialized_start = 1772
    _globals['_LISTCMEKCONFIGSRESPONSE']._serialized_end = 1864
    _globals['_DELETECMEKCONFIGREQUEST']._serialized_start = 1866
    _globals['_DELETECMEKCONFIGREQUEST']._serialized_end = 1956
    _globals['_DELETECMEKCONFIGMETADATA']._serialized_start = 1958
    _globals['_DELETECMEKCONFIGMETADATA']._serialized_end = 2082
    _globals['_CMEKCONFIGSERVICE']._serialized_start = 2085
    _globals['_CMEKCONFIGSERVICE']._serialized_end = 3238