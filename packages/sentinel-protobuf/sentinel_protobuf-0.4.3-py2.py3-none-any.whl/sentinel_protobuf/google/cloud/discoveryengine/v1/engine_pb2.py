"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/engine.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import common_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/cloud/discoveryengine/v1/engine.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/discoveryengine/v1/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe1\x14\n\x06Engine\x12V\n\x12chat_engine_config\x18\x0b \x01(\x0b28.google.cloud.discoveryengine.v1.Engine.ChatEngineConfigH\x00\x12Z\n\x14search_engine_config\x18\r \x01(\x0b2:.google.cloud.discoveryengine.v1.Engine.SearchEngineConfigH\x00\x12u\n"media_recommendation_engine_config\x18\x0e \x01(\x0b2G.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfigH\x00\x12_\n\x14chat_engine_metadata\x18\x0c \x01(\x0b2:.google.cloud.discoveryengine.v1.Engine.ChatEngineMetadataB\x03\xe0A\x03H\x01\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x05\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1b\n\x0edata_store_ids\x18\x05 \x03(\tB\x03\xe0A\x01\x12I\n\rsolution_type\x18\x06 \x01(\x0e2-.google.cloud.discoveryengine.v1.SolutionTypeB\x03\xe0A\x02\x12Q\n\x11industry_vertical\x18\x10 \x01(\x0e21.google.cloud.discoveryengine.v1.IndustryVerticalB\x03\xe0A\x01\x12K\n\rcommon_config\x18\x0f \x01(\x0b24.google.cloud.discoveryengine.v1.Engine.CommonConfig\x12\x1e\n\x11disable_analytics\x18\x1a \x01(\x08B\x03\xe0A\x01\x1a\x9c\x01\n\x12SearchEngineConfig\x12@\n\x0bsearch_tier\x18\x01 \x01(\x0e2+.google.cloud.discoveryengine.v1.SearchTier\x12D\n\x0esearch_add_ons\x18\x02 \x03(\x0e2,.google.cloud.discoveryengine.v1.SearchAddOn\x1a\xb6\x08\n\x1fMediaRecommendationEngineConfig\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x16optimization_objective\x18\x02 \x01(\t\x12\x8a\x01\n\x1doptimization_objective_config\x18\x03 \x01(\x0b2c.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfig.OptimizationObjectiveConfig\x12m\n\x0etraining_state\x18\x04 \x01(\x0e2U.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfig.TrainingState\x12\x81\x01\n\x16engine_features_config\x18\x05 \x01(\x0b2\\.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfig.EngineFeaturesConfigB\x03\xe0A\x01\x1a_\n\x1bOptimizationObjectiveConfig\x12\x19\n\x0ctarget_field\x18\x01 \x01(\tB\x03\xe0A\x02\x12%\n\x18target_field_value_float\x18\x02 \x01(\x02B\x03\xe0A\x02\x1a\xbf\x02\n\x14EngineFeaturesConfig\x12\x8c\x01\n\x1arecommended_for_you_config\x18\x01 \x01(\x0b2f.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfig.RecommendedForYouFeatureConfigH\x00\x12\x7f\n\x13most_popular_config\x18\x02 \x01(\x0b2`.google.cloud.discoveryengine.v1.Engine.MediaRecommendationEngineConfig.MostPopularFeatureConfigH\x00B\x17\n\x15type_dedicated_config\x1a<\n\x1eRecommendedForYouFeatureConfig\x12\x1a\n\x12context_event_type\x18\x01 \x01(\t\x1a4\n\x18MostPopularFeatureConfig\x12\x18\n\x10time_window_days\x18\x01 \x01(\x03"I\n\rTrainingState\x12\x1e\n\x1aTRAINING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0c\n\x08TRAINING\x10\x02\x1a\xb4\x02\n\x10ChatEngineConfig\x12k\n\x15agent_creation_config\x18\x01 \x01(\x0b2L.google.cloud.discoveryengine.v1.Engine.ChatEngineConfig.AgentCreationConfig\x12 \n\x18dialogflow_agent_to_link\x18\x02 \x01(\t\x12\x1f\n\x12allow_cross_region\x18\x03 \x01(\x08B\x03\xe0A\x01\x1ap\n\x13AgentCreationConfig\x12\x10\n\x08business\x18\x01 \x01(\t\x12\x1d\n\x15default_language_code\x18\x02 \x01(\t\x12\x16\n\ttime_zone\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x10\n\x08location\x18\x04 \x01(\t\x1a$\n\x0cCommonConfig\x12\x14\n\x0ccompany_name\x18\x01 \x01(\t\x1a.\n\x12ChatEngineMetadata\x12\x18\n\x10dialogflow_agent\x18\x01 \x01(\t:}\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}B\x0f\n\rengine_configB\x11\n\x0fengine_metadataB\xfe\x01\n#com.google.cloud.discoveryengine.v1B\x0bEngineProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.engine_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x0bEngineProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field_value_float']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG'].fields_by_name['target_field_value_float']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['type']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['engine_features_config']._loaded_options = None
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG'].fields_by_name['engine_features_config']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._loaded_options = None
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE_CHATENGINECONFIG'].fields_by_name['allow_cross_region']._loaded_options = None
    _globals['_ENGINE_CHATENGINECONFIG'].fields_by_name['allow_cross_region']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE'].fields_by_name['chat_engine_metadata']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['chat_engine_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['name']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['name']._serialized_options = b'\xe0A\x05\xe0A\x08'
    _globals['_ENGINE'].fields_by_name['display_name']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE'].fields_by_name['create_time']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['update_time']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ENGINE'].fields_by_name['data_store_ids']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['data_store_ids']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE'].fields_by_name['solution_type']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['solution_type']._serialized_options = b'\xe0A\x02'
    _globals['_ENGINE'].fields_by_name['industry_vertical']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['industry_vertical']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE'].fields_by_name['disable_analytics']._loaded_options = None
    _globals['_ENGINE'].fields_by_name['disable_analytics']._serialized_options = b'\xe0A\x01'
    _globals['_ENGINE']._loaded_options = None
    _globals['_ENGINE']._serialized_options = b'\xeaAz\n%discoveryengine.googleapis.com/Engine\x12Qprojects/{project}/locations/{location}/collections/{collection}/engines/{engine}'
    _globals['_ENGINE']._serialized_start = 221
    _globals['_ENGINE']._serialized_end = 2878
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_start = 1081
    _globals['_ENGINE_SEARCHENGINECONFIG']._serialized_end = 1237
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG']._serialized_start = 1240
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG']._serialized_end = 2318
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG']._serialized_start = 1710
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_OPTIMIZATIONOBJECTIVECONFIG']._serialized_end = 1805
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_ENGINEFEATURESCONFIG']._serialized_start = 1808
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_ENGINEFEATURESCONFIG']._serialized_end = 2127
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_RECOMMENDEDFORYOUFEATURECONFIG']._serialized_start = 2129
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_RECOMMENDEDFORYOUFEATURECONFIG']._serialized_end = 2189
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_MOSTPOPULARFEATURECONFIG']._serialized_start = 2191
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_MOSTPOPULARFEATURECONFIG']._serialized_end = 2243
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_TRAININGSTATE']._serialized_start = 2245
    _globals['_ENGINE_MEDIARECOMMENDATIONENGINECONFIG_TRAININGSTATE']._serialized_end = 2318
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_start = 2321
    _globals['_ENGINE_CHATENGINECONFIG']._serialized_end = 2629
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_start = 2517
    _globals['_ENGINE_CHATENGINECONFIG_AGENTCREATIONCONFIG']._serialized_end = 2629
    _globals['_ENGINE_COMMONCONFIG']._serialized_start = 2631
    _globals['_ENGINE_COMMONCONFIG']._serialized_end = 2667
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_start = 2669
    _globals['_ENGINE_CHATENGINEMETADATA']._serialized_end = 2715