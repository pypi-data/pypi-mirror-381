"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/recommendation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_document__pb2
from .....google.cloud.discoveryengine.v1 import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_user__event__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/discoveryengine/v1/recommendation_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/discoveryengine/v1/document.proto\x1a0google/cloud/discoveryengine/v1/user_event.proto\x1a\x1cgoogle/protobuf/struct.proto"\x80\x04\n\x10RecommendRequest\x12L\n\x0eserving_config\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig\x12C\n\nuser_event\x18\x02 \x01(\x0b2*.google.cloud.discoveryengine.v1.UserEventB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x15\n\rvalidate_only\x18\x05 \x01(\x08\x12M\n\x06params\x18\x06 \x03(\x0b2=.google.cloud.discoveryengine.v1.RecommendRequest.ParamsEntry\x12V\n\x0buser_labels\x18\x08 \x03(\x0b2A.google.cloud.discoveryengine.v1.RecommendRequest.UserLabelsEntry\x1aE\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xc8\x03\n\x11RecommendResponse\x12X\n\x07results\x18\x01 \x03(\x0b2G.google.cloud.discoveryengine.v1.RecommendResponse.RecommendationResult\x12\x19\n\x11attribution_token\x18\x02 \x01(\t\x12\x13\n\x0bmissing_ids\x18\x03 \x03(\t\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x1a\x91\x02\n\x14RecommendationResult\x12\n\n\x02id\x18\x01 \x01(\t\x12;\n\x08document\x18\x02 \x01(\x0b2).google.cloud.discoveryengine.v1.Document\x12g\n\x08metadata\x18\x03 \x03(\x0b2U.google.cloud.discoveryengine.v1.RecommendResponse.RecommendationResult.MetadataEntry\x1aG\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x012\x8f\x04\n\x15RecommendationService\x12\xa1\x03\n\tRecommend\x121.google.cloud.discoveryengine.v1.RecommendRequest\x1a2.google.cloud.discoveryengine.v1.RecommendResponse"\xac\x02\x82\xd3\xe4\x93\x02\xa5\x02"S/v1/{serving_config=projects/*/locations/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zf"a/v1/{serving_config=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zc"^/v1/{serving_config=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:recommend:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x8d\x02\n#com.google.cloud.discoveryengine.v1B\x1aRecommendationServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.recommendation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x1aRecommendationServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._loaded_options = None
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._serialized_options = b'8\x01'
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._loaded_options = None
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RECOMMENDREQUEST'].fields_by_name['serving_config']._loaded_options = None
    _globals['_RECOMMENDREQUEST'].fields_by_name['serving_config']._serialized_options = b'\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig'
    _globals['_RECOMMENDREQUEST'].fields_by_name['user_event']._loaded_options = None
    _globals['_RECOMMENDREQUEST'].fields_by_name['user_event']._serialized_options = b'\xe0A\x02'
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._loaded_options = None
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._serialized_options = b'8\x01'
    _globals['_RECOMMENDATIONSERVICE']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['Recommend']._loaded_options = None
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['Recommend']._serialized_options = b'\x82\xd3\xe4\x93\x02\xa5\x02"S/v1/{serving_config=projects/*/locations/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zf"a/v1/{serving_config=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zc"^/v1/{serving_config=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:recommend:\x01*'
    _globals['_RECOMMENDREQUEST']._serialized_start = 341
    _globals['_RECOMMENDREQUEST']._serialized_end = 853
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._serialized_start = 733
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._serialized_end = 802
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._serialized_start = 804
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._serialized_end = 853
    _globals['_RECOMMENDRESPONSE']._serialized_start = 856
    _globals['_RECOMMENDRESPONSE']._serialized_end = 1312
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT']._serialized_start = 1039
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT']._serialized_end = 1312
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._serialized_start = 1241
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._serialized_end = 1312
    _globals['_RECOMMENDATIONSERVICE']._serialized_start = 1315
    _globals['_RECOMMENDATIONSERVICE']._serialized_end = 1842