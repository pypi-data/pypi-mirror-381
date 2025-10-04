"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/recommendation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_document__pb2
from .....google.cloud.discoveryengine.v1beta import user_event_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_user__event__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/cloud/discoveryengine/v1beta/recommendation_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/discoveryengine/v1beta/document.proto\x1a4google/cloud/discoveryengine/v1beta/user_event.proto\x1a\x1cgoogle/protobuf/struct.proto"\x8c\x04\n\x10RecommendRequest\x12L\n\x0eserving_config\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,discoveryengine.googleapis.com/ServingConfig\x12G\n\nuser_event\x18\x02 \x01(\x0b2..google.cloud.discoveryengine.v1beta.UserEventB\x03\xe0A\x02\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x15\n\rvalidate_only\x18\x05 \x01(\x08\x12Q\n\x06params\x18\x06 \x03(\x0b2A.google.cloud.discoveryengine.v1beta.RecommendRequest.ParamsEntry\x12Z\n\x0buser_labels\x18\x08 \x03(\x0b2E.google.cloud.discoveryengine.v1beta.RecommendRequest.UserLabelsEntry\x1aE\n\x0bParamsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x01\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd4\x03\n\x11RecommendResponse\x12\\\n\x07results\x18\x01 \x03(\x0b2K.google.cloud.discoveryengine.v1beta.RecommendResponse.RecommendationResult\x12\x19\n\x11attribution_token\x18\x02 \x01(\t\x12\x13\n\x0bmissing_ids\x18\x03 \x03(\t\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x1a\x99\x02\n\x14RecommendationResult\x12\n\n\x02id\x18\x01 \x01(\t\x12?\n\x08document\x18\x02 \x01(\x0b2-.google.cloud.discoveryengine.v1beta.Document\x12k\n\x08metadata\x18\x03 \x03(\x0b2Y.google.cloud.discoveryengine.v1beta.RecommendResponse.RecommendationResult.MetadataEntry\x1aG\n\rMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value:\x028\x012\xa3\x04\n\x15RecommendationService\x12\xb5\x03\n\tRecommend\x125.google.cloud.discoveryengine.v1beta.RecommendRequest\x1a6.google.cloud.discoveryengine.v1beta.RecommendResponse"\xb8\x02\x82\xd3\xe4\x93\x02\xb1\x02"W/v1beta/{serving_config=projects/*/locations/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zj"e/v1beta/{serving_config=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zg"b/v1beta/{serving_config=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:recommend:\x01*\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa1\x02\n\'com.google.cloud.discoveryengine.v1betaB\x1aRecommendationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.recommendation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x1aRecommendationServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_RECOMMENDATIONSERVICE'].methods_by_name['Recommend']._serialized_options = b'\x82\xd3\xe4\x93\x02\xb1\x02"W/v1beta/{serving_config=projects/*/locations/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zj"e/v1beta/{serving_config=projects/*/locations/*/collections/*/dataStores/*/servingConfigs/*}:recommend:\x01*Zg"b/v1beta/{serving_config=projects/*/locations/*/collections/*/engines/*/servingConfigs/*}:recommend:\x01*'
    _globals['_RECOMMENDREQUEST']._serialized_start = 357
    _globals['_RECOMMENDREQUEST']._serialized_end = 881
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._serialized_start = 761
    _globals['_RECOMMENDREQUEST_PARAMSENTRY']._serialized_end = 830
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._serialized_start = 832
    _globals['_RECOMMENDREQUEST_USERLABELSENTRY']._serialized_end = 881
    _globals['_RECOMMENDRESPONSE']._serialized_start = 884
    _globals['_RECOMMENDRESPONSE']._serialized_end = 1352
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT']._serialized_start = 1071
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT']._serialized_end = 1352
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._serialized_start = 1281
    _globals['_RECOMMENDRESPONSE_RECOMMENDATIONRESULT_METADATAENTRY']._serialized_end = 1352
    _globals['_RECOMMENDATIONSERVICE']._serialized_start = 1355
    _globals['_RECOMMENDATIONSERVICE']._serialized_end = 1902