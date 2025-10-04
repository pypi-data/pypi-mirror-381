"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/serving_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_common__pb2
from .....google.cloud.discoveryengine.v1beta import search_service_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_search__service__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/discoveryengine/v1beta/serving_config.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a0google/cloud/discoveryengine/v1beta/common.proto\x1a8google/cloud/discoveryengine/v1beta/search_service.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa5\r\n\rServingConfig\x12V\n\x0cmedia_config\x18\x07 \x01(\x0b2>.google.cloud.discoveryengine.v1beta.ServingConfig.MediaConfigH\x00\x12Z\n\x0egeneric_config\x18\n \x01(\x0b2@.google.cloud.discoveryengine.v1beta.ServingConfig.GenericConfigH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x05\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12P\n\rsolution_type\x18\x03 \x01(\x0e21.google.cloud.discoveryengine.v1beta.SolutionTypeB\x06\xe0A\x02\xe0A\x05\x12\x10\n\x08model_id\x18\x04 \x01(\t\x12\x17\n\x0fdiversity_level\x18\x05 \x01(\t\x12N\n\x10embedding_config\x18\x14 \x01(\x0b24.google.cloud.discoveryengine.v1beta.EmbeddingConfig\x12\x1a\n\x12ranking_expression\x18\x15 \x01(\t\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1a\n\x12filter_control_ids\x18\x0b \x03(\t\x12\x19\n\x11boost_control_ids\x18\x0c \x03(\t\x12\x1c\n\x14redirect_control_ids\x18\x0e \x03(\t\x12\x1c\n\x14synonyms_control_ids\x18\x0f \x03(\t\x12#\n\x1boneway_synonyms_control_ids\x18\x10 \x03(\t\x12\x1e\n\x16dissociate_control_ids\x18\x11 \x03(\t\x12\x1f\n\x17replacement_control_ids\x18\x12 \x03(\t\x12\x1a\n\x12ignore_control_ids\x18\x13 \x03(\t\x12d\n\x14personalization_spec\x18\x19 \x01(\x0b2F.google.cloud.discoveryengine.v1beta.SearchRequest.PersonalizationSpec\x1a\xf7\x01\n\x0bMediaConfig\x12.\n$content_watched_percentage_threshold\x18\x02 \x01(\x02H\x00\x12+\n!content_watched_seconds_threshold\x18\x05 \x01(\x02H\x00\x12\x1b\n\x13demotion_event_type\x18\x01 \x01(\t\x12-\n demote_content_watched_past_days\x18% \x01(\x05B\x03\xe0A\x01\x12%\n\x1dcontent_freshness_cutoff_days\x18\x04 \x01(\x05B\x18\n\x16demote_content_watched\x1ar\n\rGenericConfig\x12a\n\x13content_search_spec\x18\x01 \x01(\x0b2D.google.cloud.discoveryengine.v1beta.SearchRequest.ContentSearchSpec:\x80\x03\xeaA\xfc\x02\n,discoveryengine.googleapis.com/ServingConfig\x12_projects/{project}/locations/{location}/dataStores/{data_store}/servingConfigs/{serving_config}\x12xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/servingConfigs/{serving_config}\x12qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/servingConfigs/{serving_config}B\x11\n\x0fvertical_configB\x99\x02\n\'com.google.cloud.discoveryengine.v1betaB\x12ServingConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.serving_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x12ServingConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_SERVINGCONFIG_MEDIACONFIG'].fields_by_name['demote_content_watched_past_days']._loaded_options = None
    _globals['_SERVINGCONFIG_MEDIACONFIG'].fields_by_name['demote_content_watched_past_days']._serialized_options = b'\xe0A\x01'
    _globals['_SERVINGCONFIG'].fields_by_name['name']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['name']._serialized_options = b'\xe0A\x05'
    _globals['_SERVINGCONFIG'].fields_by_name['display_name']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_SERVINGCONFIG'].fields_by_name['solution_type']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['solution_type']._serialized_options = b'\xe0A\x02\xe0A\x05'
    _globals['_SERVINGCONFIG'].fields_by_name['create_time']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVINGCONFIG'].fields_by_name['update_time']._loaded_options = None
    _globals['_SERVINGCONFIG'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SERVINGCONFIG']._loaded_options = None
    _globals['_SERVINGCONFIG']._serialized_options = b'\xeaA\xfc\x02\n,discoveryengine.googleapis.com/ServingConfig\x12_projects/{project}/locations/{location}/dataStores/{data_store}/servingConfigs/{serving_config}\x12xprojects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store}/servingConfigs/{serving_config}\x12qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}/servingConfigs/{serving_config}'
    _globals['_SERVINGCONFIG']._serialized_start = 299
    _globals['_SERVINGCONFIG']._serialized_end = 2000
    _globals['_SERVINGCONFIG_MEDIACONFIG']._serialized_start = 1231
    _globals['_SERVINGCONFIG_MEDIACONFIG']._serialized_end = 1478
    _globals['_SERVINGCONFIG_GENERICCONFIG']._serialized_start = 1480
    _globals['_SERVINGCONFIG_GENERICCONFIG']._serialized_end = 1594