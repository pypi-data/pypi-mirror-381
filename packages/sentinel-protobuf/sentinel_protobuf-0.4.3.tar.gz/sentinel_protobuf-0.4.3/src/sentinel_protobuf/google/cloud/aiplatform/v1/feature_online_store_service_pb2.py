"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/feature_online_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import featurestore_online_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_featurestore__online__service__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/cloud/aiplatform/v1/feature_online_store_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/aiplatform/v1/featurestore_online_service.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa5\x01\n\x12FeatureViewDataKey\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12T\n\rcomposite_key\x18\x02 \x01(\x0b2;.google.cloud.aiplatform.v1.FeatureViewDataKey.CompositeKeyH\x00\x1a\x1d\n\x0cCompositeKey\x12\r\n\x05parts\x18\x01 \x03(\tB\x0b\n\tkey_oneof"\xf4\x01\n\x19FetchFeatureValuesRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12E\n\x08data_key\x18\x06 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureViewDataKeyB\x03\xe0A\x01\x12K\n\x0bdata_format\x18\x07 \x01(\x0e21.google.cloud.aiplatform.v1.FeatureViewDataFormatB\x03\xe0A\x01"\xfe\x03\n\x1aFetchFeatureValuesResponse\x12e\n\nkey_values\x18\x03 \x01(\x0b2O.google.cloud.aiplatform.v1.FetchFeatureValuesResponse.FeatureNameValuePairListH\x00\x12/\n\x0cproto_struct\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12@\n\x08data_key\x18\x04 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureViewDataKey\x1a\xfb\x01\n\x18FeatureNameValuePairList\x12v\n\x08features\x18\x01 \x03(\x0b2d.google.cloud.aiplatform.v1.FetchFeatureValuesResponse.FeatureNameValuePairList.FeatureNameValuePair\x1ag\n\x14FeatureNameValuePair\x129\n\x05value\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureValueH\x00\x12\x0c\n\x04name\x18\x01 \x01(\tB\x06\n\x04dataB\x08\n\x06format"\xa3\x08\n\x14NearestNeighborQuery\x12\x18\n\tentity_id\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x12T\n\tembedding\x18\x02 \x01(\x0b2:.google.cloud.aiplatform.v1.NearestNeighborQuery.EmbeddingB\x03\xe0A\x01H\x00\x12\x1b\n\x0eneighbor_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x12Z\n\x0estring_filters\x18\x04 \x03(\x0b2=.google.cloud.aiplatform.v1.NearestNeighborQuery.StringFilterB\x03\xe0A\x01\x12\\\n\x0fnumeric_filters\x18\x08 \x03(\x0b2>.google.cloud.aiplatform.v1.NearestNeighborQuery.NumericFilterB\x03\xe0A\x01\x122\n%per_crowding_attribute_neighbor_count\x18\x05 \x01(\x05B\x03\xe0A\x01\x12T\n\nparameters\x18\x07 \x01(\x0b2;.google.cloud.aiplatform.v1.NearestNeighborQuery.ParametersB\x03\xe0A\x01\x1a\x1f\n\tEmbedding\x12\x12\n\x05value\x18\x01 \x03(\x02B\x03\xe0A\x01\x1aV\n\x0cStringFilter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0callow_tokens\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x18\n\x0bdeny_tokens\x18\x03 \x03(\tB\x03\xe0A\x01\x1a\xcf\x02\n\rNumericFilter\x12\x13\n\tvalue_int\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bvalue_float\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cvalue_double\x18\x04 \x01(\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12]\n\x02op\x18\x05 \x01(\x0e2G.google.cloud.aiplatform.v1.NearestNeighborQuery.NumericFilter.OperatorB\x03\xe0A\x01H\x01\x88\x01\x01"x\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05EQUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06B\x07\n\x05ValueB\x05\n\x03_op\x1ac\n\nParameters\x12,\n\x1fapproximate_neighbor_candidates\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\'\n\x1aleaf_nodes_search_fraction\x18\x02 \x01(\x01B\x03\xe0A\x01B\n\n\x08instance"\xca\x01\n\x1cSearchNearestEntitiesRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12D\n\x05query\x18\x02 \x01(\x0b20.google.cloud.aiplatform.v1.NearestNeighborQueryB\x03\xe0A\x02\x12\x1f\n\x12return_full_entity\x18\x03 \x01(\x08B\x03\xe0A\x01"\xe1\x01\n\x10NearestNeighbors\x12H\n\tneighbors\x18\x01 \x03(\x0b25.google.cloud.aiplatform.v1.NearestNeighbors.Neighbor\x1a\x82\x01\n\x08Neighbor\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x10\n\x08distance\x18\x02 \x01(\x01\x12Q\n\x11entity_key_values\x18\x03 \x01(\x0b26.google.cloud.aiplatform.v1.FetchFeatureValuesResponse"h\n\x1dSearchNearestEntitiesResponse\x12G\n\x11nearest_neighbors\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1.NearestNeighbors"\x8b\x04\n\x1dFeatureViewDirectWriteRequest\x12@\n\x0cfeature_view\x18\x01 \x01(\tB*\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12{\n\x1bdata_key_and_feature_values\x18\x02 \x03(\x0b2Q.google.cloud.aiplatform.v1.FeatureViewDirectWriteRequest.DataKeyAndFeatureValuesB\x03\xe0A\x02\x1a\xaa\x02\n\x17DataKeyAndFeatureValues\x12@\n\x08data_key\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureViewDataKey\x12k\n\x08features\x18\x02 \x03(\x0b2Y.google.cloud.aiplatform.v1.FeatureViewDirectWriteRequest.DataKeyAndFeatureValues.Feature\x1a`\n\x07Feature\x129\n\x05value\x18\x03 \x01(\x0b2(.google.cloud.aiplatform.v1.FeatureValueH\x00\x12\x0c\n\x04name\x18\x01 \x01(\tB\x0c\n\ndata_oneof"\xb8\x02\n\x1eFeatureViewDirectWriteResponse\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12a\n\x0fwrite_responses\x18\x02 \x03(\x0b2H.google.cloud.aiplatform.v1.FeatureViewDirectWriteResponse.WriteResponse\x1a\x8e\x01\n\rWriteResponse\x12@\n\x08data_key\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureViewDataKey\x12;\n\x17online_store_write_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp*b\n\x15FeatureViewDataFormat\x12(\n$FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tKEY_VALUE\x10\x01\x12\x10\n\x0cPROTO_STRUCT\x10\x022\xf5\x06\n\x19FeatureOnlineStoreService\x12\x8b\x02\n\x12FetchFeatureValues\x125.google.cloud.aiplatform.v1.FetchFeatureValuesRequest\x1a6.google.cloud.aiplatform.v1.FetchFeatureValuesResponse"\x85\x01\xdaA\x16feature_view, data_key\x82\xd3\xe4\x93\x02f"a/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:fetchFeatureValues:\x01*\x12\xfd\x01\n\x15SearchNearestEntities\x128.google.cloud.aiplatform.v1.SearchNearestEntitiesRequest\x1a9.google.cloud.aiplatform.v1.SearchNearestEntitiesResponse"o\x82\xd3\xe4\x93\x02i"d/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:searchNearestEntities:\x01*\x12\xfa\x01\n\x16FeatureViewDirectWrite\x129.google.cloud.aiplatform.v1.FeatureViewDirectWriteRequest\x1a:.google.cloud.aiplatform.v1.FeatureViewDirectWriteResponse"e\x82\xd3\xe4\x93\x02_"Z/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:directWrite:\x01*(\x010\x01\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xdc\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1eFeatureOnlineStoreServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_online_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1eFeatureOnlineStoreServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_key']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_key']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING'].fields_by_name['value']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['name']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['allow_tokens']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['allow_tokens']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['deny_tokens']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER'].fields_by_name['deny_tokens']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER'].fields_by_name['name']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER'].fields_by_name['op']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER'].fields_by_name['op']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS'].fields_by_name['approximate_neighbor_candidates']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS'].fields_by_name['approximate_neighbor_candidates']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS'].fields_by_name['leaf_nodes_search_fraction']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS'].fields_by_name['leaf_nodes_search_fraction']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['entity_id']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['entity_id']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['embedding']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['embedding']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['neighbor_count']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['neighbor_count']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['string_filters']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['string_filters']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['numeric_filters']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['numeric_filters']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['per_crowding_attribute_neighbor_count']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['per_crowding_attribute_neighbor_count']._serialized_options = b'\xe0A\x01'
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['parameters']._loaded_options = None
    _globals['_NEARESTNEIGHBORQUERY'].fields_by_name['parameters']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['query']._loaded_options = None
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['return_full_entity']._loaded_options = None
    _globals['_SEARCHNEARESTENTITIESREQUEST'].fields_by_name['return_full_entity']._serialized_options = b'\xe0A\x01'
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST'].fields_by_name['data_key_and_feature_values']._loaded_options = None
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST'].fields_by_name['data_key_and_feature_values']._serialized_options = b'\xe0A\x02'
    _globals['_FEATUREONLINESTORESERVICE']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FetchFeatureValues']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FetchFeatureValues']._serialized_options = b'\xdaA\x16feature_view, data_key\x82\xd3\xe4\x93\x02f"a/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:fetchFeatureValues:\x01*'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['SearchNearestEntities']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['SearchNearestEntities']._serialized_options = b'\x82\xd3\xe4\x93\x02i"d/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:searchNearestEntities:\x01*'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FeatureViewDirectWrite']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FeatureViewDirectWrite']._serialized_options = b'\x82\xd3\xe4\x93\x02_"Z/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:directWrite:\x01*'
    _globals['_FEATUREVIEWDATAFORMAT']._serialized_start = 3728
    _globals['_FEATUREVIEWDATAFORMAT']._serialized_end = 3826
    _globals['_FEATUREVIEWDATAKEY']._serialized_start = 359
    _globals['_FEATUREVIEWDATAKEY']._serialized_end = 524
    _globals['_FEATUREVIEWDATAKEY_COMPOSITEKEY']._serialized_start = 482
    _globals['_FEATUREVIEWDATAKEY_COMPOSITEKEY']._serialized_end = 511
    _globals['_FETCHFEATUREVALUESREQUEST']._serialized_start = 527
    _globals['_FETCHFEATUREVALUESREQUEST']._serialized_end = 771
    _globals['_FETCHFEATUREVALUESRESPONSE']._serialized_start = 774
    _globals['_FETCHFEATUREVALUESRESPONSE']._serialized_end = 1284
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST']._serialized_start = 1023
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST']._serialized_end = 1274
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST_FEATURENAMEVALUEPAIR']._serialized_start = 1171
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST_FEATURENAMEVALUEPAIR']._serialized_end = 1274
    _globals['_NEARESTNEIGHBORQUERY']._serialized_start = 1287
    _globals['_NEARESTNEIGHBORQUERY']._serialized_end = 2346
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING']._serialized_start = 1776
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING']._serialized_end = 1807
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER']._serialized_start = 1809
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER']._serialized_end = 1895
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER']._serialized_start = 1898
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER']._serialized_end = 2233
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER_OPERATOR']._serialized_start = 2097
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER_OPERATOR']._serialized_end = 2217
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS']._serialized_start = 2235
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS']._serialized_end = 2334
    _globals['_SEARCHNEARESTENTITIESREQUEST']._serialized_start = 2349
    _globals['_SEARCHNEARESTENTITIESREQUEST']._serialized_end = 2551
    _globals['_NEARESTNEIGHBORS']._serialized_start = 2554
    _globals['_NEARESTNEIGHBORS']._serialized_end = 2779
    _globals['_NEARESTNEIGHBORS_NEIGHBOR']._serialized_start = 2649
    _globals['_NEARESTNEIGHBORS_NEIGHBOR']._serialized_end = 2779
    _globals['_SEARCHNEARESTENTITIESRESPONSE']._serialized_start = 2781
    _globals['_SEARCHNEARESTENTITIESRESPONSE']._serialized_end = 2885
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST']._serialized_start = 2888
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST']._serialized_end = 3411
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES']._serialized_start = 3113
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES']._serialized_end = 3411
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE']._serialized_start = 3315
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE']._serialized_end = 3411
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE']._serialized_start = 3414
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE']._serialized_end = 3726
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE_WRITERESPONSE']._serialized_start = 3584
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE_WRITERESPONSE']._serialized_end = 3726
    _globals['_FEATUREONLINESTORESERVICE']._serialized_start = 3829
    _globals['_FEATUREONLINESTORESERVICE']._serialized_end = 4714