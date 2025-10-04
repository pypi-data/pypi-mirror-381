"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/feature_view.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import machine_resources_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_machine__resources__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1/feature_view.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/aiplatform/v1/machine_resources.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8a\x14\n\x0bFeatureView\x12W\n\x10big_query_source\x18\x06 \x01(\x0b26.google.cloud.aiplatform.v1.FeatureView.BigQuerySourceB\x03\xe0A\x01H\x00\x12e\n\x17feature_registry_source\x18\t \x01(\x0b2=.google.cloud.aiplatform.v1.FeatureView.FeatureRegistrySourceB\x03\xe0A\x01H\x00\x12Y\n\x11vertex_rag_source\x18\x12 \x01(\x0b27.google.cloud.aiplatform.v1.FeatureView.VertexRagSourceB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x04 \x01(\tB\x03\xe0A\x01\x12H\n\x06labels\x18\x05 \x03(\x0b23.google.cloud.aiplatform.v1.FeatureView.LabelsEntryB\x03\xe0A\x01\x12G\n\x0bsync_config\x18\x07 \x01(\x0b22.google.cloud.aiplatform.v1.FeatureView.SyncConfig\x12N\n\x0cindex_config\x18\x0f \x01(\x0b23.google.cloud.aiplatform.v1.FeatureView.IndexConfigB\x03\xe0A\x01\x12V\n\x10optimized_config\x18\x10 \x01(\x0b27.google.cloud.aiplatform.v1.FeatureView.OptimizedConfigB\x03\xe0A\x01\x12Y\n\x12service_agent_type\x18\x0e \x01(\x0e28.google.cloud.aiplatform.v1.FeatureView.ServiceAgentTypeB\x03\xe0A\x01\x12"\n\x15service_account_email\x18\r \x01(\tB\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzs\x18\x13 \x01(\x08B\x03\xe0A\x03\x12\x1a\n\rsatisfies_pzi\x18\x14 \x01(\x08B\x03\xe0A\x03\x1aB\n\x0eBigQuerySource\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1e\n\x11entity_id_columns\x18\x02 \x03(\tB\x03\xe0A\x02\x1a3\n\nSyncConfig\x12\x0c\n\x04cron\x18\x01 \x01(\t\x12\x17\n\ncontinuous\x18\x02 \x01(\x08B\x03\xe0A\x01\x1a\xe7\x05\n\x0bIndexConfig\x12_\n\x0etree_ah_config\x18\x06 \x01(\x0b2@.google.cloud.aiplatform.v1.FeatureView.IndexConfig.TreeAHConfigB\x03\xe0A\x01H\x00\x12g\n\x12brute_force_config\x18\x07 \x01(\x0b2D.google.cloud.aiplatform.v1.FeatureView.IndexConfig.BruteForceConfigB\x03\xe0A\x01H\x00\x12\x1d\n\x10embedding_column\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1b\n\x0efilter_columns\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x1c\n\x0fcrowding_column\x18\x03 \x01(\tB\x03\xe0A\x01\x12%\n\x13embedding_dimension\x18\x04 \x01(\x05B\x03\xe0A\x01H\x01\x88\x01\x01\x12k\n\x15distance_measure_type\x18\x05 \x01(\x0e2G.google.cloud.aiplatform.v1.FeatureView.IndexConfig.DistanceMeasureTypeB\x03\xe0A\x01\x1a\x12\n\x10BruteForceConfig\x1aY\n\x0cTreeAHConfig\x12+\n\x19leaf_node_embedding_count\x18\x01 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01B\x1c\n\x1a_leaf_node_embedding_count"\x84\x01\n\x13DistanceMeasureType\x12%\n!DISTANCE_MEASURE_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13SQUARED_L2_DISTANCE\x10\x01\x12\x13\n\x0fCOSINE_DISTANCE\x10\x02\x12\x18\n\x14DOT_PRODUCT_DISTANCE\x10\x03B\x12\n\x10algorithm_configB\x16\n\x14_embedding_dimension\x1a\xfe\x01\n\x15FeatureRegistrySource\x12g\n\x0efeature_groups\x18\x01 \x03(\x0b2J.google.cloud.aiplatform.v1.FeatureView.FeatureRegistrySource.FeatureGroupB\x03\xe0A\x02\x12 \n\x0eproject_number\x18\x02 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x1aG\n\x0cFeatureGroup\x12\x1d\n\x10feature_group_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x18\n\x0bfeature_ids\x18\x02 \x03(\tB\x03\xe0A\x02B\x11\n\x0f_project_number\x1a?\n\x0fVertexRagSource\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rrag_corpus_id\x18\x02 \x01(\x03B\x03\xe0A\x01\x1ac\n\x0fOptimizedConfig\x12P\n\x13automatic_resources\x18\x07 \x01(\x0b2..google.cloud.aiplatform.v1.AutomaticResourcesB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"{\n\x10ServiceAgentType\x12"\n\x1eSERVICE_AGENT_TYPE_UNSPECIFIED\x10\x00\x12\x1e\n\x1aSERVICE_AGENT_TYPE_PROJECT\x10\x01\x12#\n\x1fSERVICE_AGENT_TYPE_FEATURE_VIEW\x10\x02:\x9b\x01\xeaA\x97\x01\n%aiplatform.googleapis.com/FeatureView\x12nprojects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}B\x08\n\x06sourceB\xce\x01\n\x1ecom.google.cloud.aiplatform.v1B\x10FeatureViewProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_view_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x10FeatureViewProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_FEATUREVIEW_BIGQUERYSOURCE'].fields_by_name['uri']._loaded_options = None
    _globals['_FEATUREVIEW_BIGQUERYSOURCE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_BIGQUERYSOURCE'].fields_by_name['entity_id_columns']._loaded_options = None
    _globals['_FEATUREVIEW_BIGQUERYSOURCE'].fields_by_name['entity_id_columns']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_SYNCCONFIG'].fields_by_name['continuous']._loaded_options = None
    _globals['_FEATUREVIEW_SYNCCONFIG'].fields_by_name['continuous']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG_TREEAHCONFIG'].fields_by_name['leaf_node_embedding_count']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG_TREEAHCONFIG'].fields_by_name['leaf_node_embedding_count']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['tree_ah_config']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['tree_ah_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['brute_force_config']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['brute_force_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['embedding_column']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['embedding_column']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['filter_columns']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['filter_columns']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['crowding_column']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['crowding_column']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['embedding_dimension']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['embedding_dimension']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['distance_measure_type']._loaded_options = None
    _globals['_FEATUREVIEW_INDEXCONFIG'].fields_by_name['distance_measure_type']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP'].fields_by_name['feature_group_id']._loaded_options = None
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP'].fields_by_name['feature_group_id']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP'].fields_by_name['feature_ids']._loaded_options = None
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP'].fields_by_name['feature_ids']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE'].fields_by_name['feature_groups']._loaded_options = None
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE'].fields_by_name['feature_groups']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE'].fields_by_name['project_number']._loaded_options = None
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE'].fields_by_name['project_number']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE'].fields_by_name['uri']._loaded_options = None
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE'].fields_by_name['rag_corpus_id']._loaded_options = None
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE'].fields_by_name['rag_corpus_id']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_OPTIMIZEDCONFIG'].fields_by_name['automatic_resources']._loaded_options = None
    _globals['_FEATUREVIEW_OPTIMIZEDCONFIG'].fields_by_name['automatic_resources']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW_LABELSENTRY']._loaded_options = None
    _globals['_FEATUREVIEW_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_FEATUREVIEW'].fields_by_name['big_query_source']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['big_query_source']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['feature_registry_source']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['feature_registry_source']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['vertex_rag_source']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['vertex_rag_source']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_FEATUREVIEW'].fields_by_name['create_time']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEW'].fields_by_name['update_time']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEW'].fields_by_name['etag']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['labels']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['index_config']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['index_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['optimized_config']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['optimized_config']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['service_agent_type']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['service_agent_type']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEW'].fields_by_name['service_account_email']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['service_account_email']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEW'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEW'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_FEATUREVIEW'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_FEATUREVIEW']._loaded_options = None
    _globals['_FEATUREVIEW']._serialized_options = b'\xeaA\x97\x01\n%aiplatform.googleapis.com/FeatureView\x12nprojects/{project}/locations/{location}/featureOnlineStores/{feature_online_store}/featureViews/{feature_view}'
    _globals['_FEATUREVIEW']._serialized_start = 223
    _globals['_FEATUREVIEW']._serialized_end = 2793
    _globals['_FEATUREVIEW_BIGQUERYSOURCE']._serialized_start = 1165
    _globals['_FEATUREVIEW_BIGQUERYSOURCE']._serialized_end = 1231
    _globals['_FEATUREVIEW_SYNCCONFIG']._serialized_start = 1233
    _globals['_FEATUREVIEW_SYNCCONFIG']._serialized_end = 1284
    _globals['_FEATUREVIEW_INDEXCONFIG']._serialized_start = 1287
    _globals['_FEATUREVIEW_INDEXCONFIG']._serialized_end = 2030
    _globals['_FEATUREVIEW_INDEXCONFIG_BRUTEFORCECONFIG']._serialized_start = 1742
    _globals['_FEATUREVIEW_INDEXCONFIG_BRUTEFORCECONFIG']._serialized_end = 1760
    _globals['_FEATUREVIEW_INDEXCONFIG_TREEAHCONFIG']._serialized_start = 1762
    _globals['_FEATUREVIEW_INDEXCONFIG_TREEAHCONFIG']._serialized_end = 1851
    _globals['_FEATUREVIEW_INDEXCONFIG_DISTANCEMEASURETYPE']._serialized_start = 1854
    _globals['_FEATUREVIEW_INDEXCONFIG_DISTANCEMEASURETYPE']._serialized_end = 1986
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE']._serialized_start = 2033
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE']._serialized_end = 2287
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP']._serialized_start = 2197
    _globals['_FEATUREVIEW_FEATUREREGISTRYSOURCE_FEATUREGROUP']._serialized_end = 2268
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE']._serialized_start = 2289
    _globals['_FEATUREVIEW_VERTEXRAGSOURCE']._serialized_end = 2352
    _globals['_FEATUREVIEW_OPTIMIZEDCONFIG']._serialized_start = 2354
    _globals['_FEATUREVIEW_OPTIMIZEDCONFIG']._serialized_end = 2453
    _globals['_FEATUREVIEW_LABELSENTRY']._serialized_start = 2455
    _globals['_FEATUREVIEW_LABELSENTRY']._serialized_end = 2500
    _globals['_FEATUREVIEW_SERVICEAGENTTYPE']._serialized_start = 2502
    _globals['_FEATUREVIEW_SERVICEAGENTTYPE']._serialized_end = 2625