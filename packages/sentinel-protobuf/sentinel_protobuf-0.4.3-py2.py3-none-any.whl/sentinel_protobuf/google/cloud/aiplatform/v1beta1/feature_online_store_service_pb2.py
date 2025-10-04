"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature_online_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import featurestore_online_service_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_featurestore__online__service__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/aiplatform/v1beta1/feature_online_store_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aAgoogle/cloud/aiplatform/v1beta1/featurestore_online_service.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xaa\x01\n\x12FeatureViewDataKey\x12\r\n\x03key\x18\x01 \x01(\tH\x00\x12Y\n\rcomposite_key\x18\x02 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.FeatureViewDataKey.CompositeKeyH\x00\x1a\x1d\n\x0cCompositeKey\x12\r\n\x05parts\x18\x01 \x03(\tB\x0b\n\tkey_oneof"\xbb\x03\n\x19FetchFeatureValuesRequest\x12\x10\n\x02id\x18\x03 \x01(\tB\x02\x18\x01H\x00\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12J\n\x08data_key\x18\x06 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKeyB\x03\xe0A\x01\x12P\n\x0bdata_format\x18\x07 \x01(\x0e26.google.cloud.aiplatform.v1beta1.FeatureViewDataFormatB\x03\xe0A\x01\x12U\n\x06format\x18\x05 \x01(\x0e2A.google.cloud.aiplatform.v1beta1.FetchFeatureValuesRequest.FormatB\x02\x18\x01"E\n\x06Format\x12\x16\n\x12FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tKEY_VALUE\x10\x01\x12\x10\n\x0cPROTO_STRUCT\x10\x02\x1a\x02\x18\x01B\x0b\n\tentity_id"\x92\x04\n\x1aFetchFeatureValuesResponse\x12j\n\nkey_values\x18\x03 \x01(\x0b2T.google.cloud.aiplatform.v1beta1.FetchFeatureValuesResponse.FeatureNameValuePairListH\x00\x12/\n\x0cproto_struct\x18\x02 \x01(\x0b2\x17.google.protobuf.StructH\x00\x12E\n\x08data_key\x18\x04 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKey\x1a\x85\x02\n\x18FeatureNameValuePairList\x12{\n\x08features\x18\x01 \x03(\x0b2i.google.cloud.aiplatform.v1beta1.FetchFeatureValuesResponse.FeatureNameValuePairList.FeatureNameValuePair\x1al\n\x14FeatureNameValuePair\x12>\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValueH\x00\x12\x0c\n\x04name\x18\x01 \x01(\tB\x06\n\x04dataB\x08\n\x06format"\xfe\x01\n"StreamingFetchFeatureValuesRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12F\n\tdata_keys\x18\x02 \x03(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKey\x12K\n\x0bdata_format\x18\x03 \x01(\x0e26.google.cloud.aiplatform.v1beta1.FeatureViewDataFormat"\xe7\x01\n#StreamingFetchFeatureValuesResponse\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12I\n\x04data\x18\x02 \x03(\x0b2;.google.cloud.aiplatform.v1beta1.FetchFeatureValuesResponse\x12Q\n\x14data_keys_with_error\x18\x03 \x03(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKey"\xbc\x08\n\x14NearestNeighborQuery\x12\x18\n\tentity_id\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x12Y\n\tembedding\x18\x02 \x01(\x0b2?.google.cloud.aiplatform.v1beta1.NearestNeighborQuery.EmbeddingB\x03\xe0A\x01H\x00\x12\x1b\n\x0eneighbor_count\x18\x03 \x01(\x05B\x03\xe0A\x01\x12_\n\x0estring_filters\x18\x04 \x03(\x0b2B.google.cloud.aiplatform.v1beta1.NearestNeighborQuery.StringFilterB\x03\xe0A\x01\x12a\n\x0fnumeric_filters\x18\x08 \x03(\x0b2C.google.cloud.aiplatform.v1beta1.NearestNeighborQuery.NumericFilterB\x03\xe0A\x01\x122\n%per_crowding_attribute_neighbor_count\x18\x05 \x01(\x05B\x03\xe0A\x01\x12Y\n\nparameters\x18\x07 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.NearestNeighborQuery.ParametersB\x03\xe0A\x01\x1a\x1f\n\tEmbedding\x12\x12\n\x05value\x18\x01 \x03(\x02B\x03\xe0A\x01\x1aV\n\x0cStringFilter\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0callow_tokens\x18\x02 \x03(\tB\x03\xe0A\x01\x12\x18\n\x0bdeny_tokens\x18\x03 \x03(\tB\x03\xe0A\x01\x1a\xd4\x02\n\rNumericFilter\x12\x13\n\tvalue_int\x18\x02 \x01(\x03H\x00\x12\x15\n\x0bvalue_float\x18\x03 \x01(\x02H\x00\x12\x16\n\x0cvalue_double\x18\x04 \x01(\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12b\n\x02op\x18\x05 \x01(\x0e2L.google.cloud.aiplatform.v1beta1.NearestNeighborQuery.NumericFilter.OperatorB\x03\xe0A\x01H\x01\x88\x01\x01"x\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x08\n\x04LESS\x10\x01\x12\x0e\n\nLESS_EQUAL\x10\x02\x12\t\n\x05EQUAL\x10\x03\x12\x11\n\rGREATER_EQUAL\x10\x04\x12\x0b\n\x07GREATER\x10\x05\x12\r\n\tNOT_EQUAL\x10\x06B\x07\n\x05ValueB\x05\n\x03_op\x1ac\n\nParameters\x12,\n\x1fapproximate_neighbor_candidates\x18\x01 \x01(\x05B\x03\xe0A\x01\x12\'\n\x1aleaf_nodes_search_fraction\x18\x02 \x01(\x01B\x03\xe0A\x01B\n\n\x08instance"\xcf\x01\n\x1cSearchNearestEntitiesRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12I\n\x05query\x18\x02 \x01(\x0b25.google.cloud.aiplatform.v1beta1.NearestNeighborQueryB\x03\xe0A\x02\x12\x1f\n\x12return_full_entity\x18\x03 \x01(\x08B\x03\xe0A\x01"\xeb\x01\n\x10NearestNeighbors\x12M\n\tneighbors\x18\x01 \x03(\x0b2:.google.cloud.aiplatform.v1beta1.NearestNeighbors.Neighbor\x1a\x87\x01\n\x08Neighbor\x12\x11\n\tentity_id\x18\x01 \x01(\t\x12\x10\n\x08distance\x18\x02 \x01(\x01\x12V\n\x11entity_key_values\x18\x03 \x01(\x0b2;.google.cloud.aiplatform.v1beta1.FetchFeatureValuesResponse"m\n\x1dSearchNearestEntitiesResponse\x12L\n\x11nearest_neighbors\x18\x01 \x01(\x0b21.google.cloud.aiplatform.v1beta1.NearestNeighbors"\xc4\x06\n\x1dFeatureViewDirectWriteRequest\x12@\n\x0cfeature_view\x18\x01 \x01(\tB*\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12\x80\x01\n\x1bdata_key_and_feature_values\x18\x02 \x03(\x0b2V.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteRequest.DataKeyAndFeatureValuesB\x03\xe0A\x02\x1a\xdd\x04\n\x17DataKeyAndFeatureValues\x12E\n\x08data_key\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKey\x12p\n\x08features\x18\x02 \x03(\x0b2^.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteRequest.DataKeyAndFeatureValues.Feature\x1a\x88\x03\n\x07Feature\x12>\n\x05value\x18\x03 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValueH\x00\x12\x96\x01\n\x13value_and_timestamp\x18\x02 \x01(\x0b2w.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteRequest.DataKeyAndFeatureValues.Feature.FeatureValueAndTimestampH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x87\x01\n\x18FeatureValueAndTimestamp\x12<\n\x05value\x18\x01 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.FeatureValue\x12-\n\ttimestamp\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x0c\n\ndata_oneof"\xc2\x02\n\x1eFeatureViewDirectWriteResponse\x12"\n\x06status\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12f\n\x0fwrite_responses\x18\x02 \x03(\x0b2M.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteResponse.WriteResponse\x1a\x93\x01\n\rWriteResponse\x12E\n\x08data_key\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureViewDataKey\x12;\n\x17online_store_write_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp*b\n\x15FeatureViewDataFormat\x12(\n$FEATURE_VIEW_DATA_FORMAT_UNSPECIFIED\x10\x00\x12\r\n\tKEY_VALUE\x10\x01\x12\x10\n\x0cPROTO_STRUCT\x10\x022\xe8\t\n\x19FeatureOnlineStoreService\x12\x9a\x02\n\x12FetchFeatureValues\x12:.google.cloud.aiplatform.v1beta1.FetchFeatureValuesRequest\x1a;.google.cloud.aiplatform.v1beta1.FetchFeatureValuesResponse"\x8a\x01\xdaA\x16feature_view, data_key\x82\xd3\xe4\x93\x02k"f/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:fetchFeatureValues:\x01*\x12\xc3\x02\n\x1bStreamingFetchFeatureValues\x12C.google.cloud.aiplatform.v1beta1.StreamingFetchFeatureValuesRequest\x1aD.google.cloud.aiplatform.v1beta1.StreamingFetchFeatureValuesResponse"\x94\x01\xdaA\x17feature_view, data_keys\x82\xd3\xe4\x93\x02t"o/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:streamingFetchFeatureValues:\x01*(\x010\x01\x12\x8c\x02\n\x15SearchNearestEntities\x12=.google.cloud.aiplatform.v1beta1.SearchNearestEntitiesRequest\x1a>.google.cloud.aiplatform.v1beta1.SearchNearestEntitiesResponse"t\x82\xd3\xe4\x93\x02n"i/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:searchNearestEntities:\x01*\x12\x89\x02\n\x16FeatureViewDirectWrite\x12>.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteRequest\x1a?.google.cloud.aiplatform.v1beta1.FeatureViewDirectWriteResponse"j\x82\xd3\xe4\x93\x02d"_/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:directWrite:\x01*(\x010\x01\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xf5\x01\n#com.google.cloud.aiplatform.v1beta1B\x1eFeatureOnlineStoreServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_online_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x1eFeatureOnlineStoreServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_FETCHFEATUREVALUESREQUEST_FORMAT']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST_FORMAT']._serialized_options = b'\x18\x01'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['id']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['id']._serialized_options = b'\x18\x01'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_key']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_key']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_format']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['data_format']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['format']._loaded_options = None
    _globals['_FETCHFEATUREVALUESREQUEST'].fields_by_name['format']._serialized_options = b'\x18\x01'
    _globals['_STREAMINGFETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_STREAMINGFETCHFEATUREVALUESREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
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
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FetchFeatureValues']._serialized_options = b'\xdaA\x16feature_view, data_key\x82\xd3\xe4\x93\x02k"f/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:fetchFeatureValues:\x01*'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['StreamingFetchFeatureValues']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['StreamingFetchFeatureValues']._serialized_options = b'\xdaA\x17feature_view, data_keys\x82\xd3\xe4\x93\x02t"o/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:streamingFetchFeatureValues:\x01*'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['SearchNearestEntities']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['SearchNearestEntities']._serialized_options = b'\x82\xd3\xe4\x93\x02n"i/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:searchNearestEntities:\x01*'
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FeatureViewDirectWrite']._loaded_options = None
    _globals['_FEATUREONLINESTORESERVICE'].methods_by_name['FeatureViewDirectWrite']._serialized_options = b'\x82\xd3\xe4\x93\x02d"_/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:directWrite:\x01*'
    _globals['_FEATUREVIEWDATAFORMAT']._serialized_start = 4826
    _globals['_FEATUREVIEWDATAFORMAT']._serialized_end = 4924
    _globals['_FEATUREVIEWDATAKEY']._serialized_start = 374
    _globals['_FEATUREVIEWDATAKEY']._serialized_end = 544
    _globals['_FEATUREVIEWDATAKEY_COMPOSITEKEY']._serialized_start = 502
    _globals['_FEATUREVIEWDATAKEY_COMPOSITEKEY']._serialized_end = 531
    _globals['_FETCHFEATUREVALUESREQUEST']._serialized_start = 547
    _globals['_FETCHFEATUREVALUESREQUEST']._serialized_end = 990
    _globals['_FETCHFEATUREVALUESREQUEST_FORMAT']._serialized_start = 908
    _globals['_FETCHFEATUREVALUESREQUEST_FORMAT']._serialized_end = 977
    _globals['_FETCHFEATUREVALUESRESPONSE']._serialized_start = 993
    _globals['_FETCHFEATUREVALUESRESPONSE']._serialized_end = 1523
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST']._serialized_start = 1252
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST']._serialized_end = 1513
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST_FEATURENAMEVALUEPAIR']._serialized_start = 1405
    _globals['_FETCHFEATUREVALUESRESPONSE_FEATURENAMEVALUEPAIRLIST_FEATURENAMEVALUEPAIR']._serialized_end = 1513
    _globals['_STREAMINGFETCHFEATUREVALUESREQUEST']._serialized_start = 1526
    _globals['_STREAMINGFETCHFEATUREVALUESREQUEST']._serialized_end = 1780
    _globals['_STREAMINGFETCHFEATUREVALUESRESPONSE']._serialized_start = 1783
    _globals['_STREAMINGFETCHFEATUREVALUESRESPONSE']._serialized_end = 2014
    _globals['_NEARESTNEIGHBORQUERY']._serialized_start = 2017
    _globals['_NEARESTNEIGHBORQUERY']._serialized_end = 3101
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING']._serialized_start = 2526
    _globals['_NEARESTNEIGHBORQUERY_EMBEDDING']._serialized_end = 2557
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER']._serialized_start = 2559
    _globals['_NEARESTNEIGHBORQUERY_STRINGFILTER']._serialized_end = 2645
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER']._serialized_start = 2648
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER']._serialized_end = 2988
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER_OPERATOR']._serialized_start = 2852
    _globals['_NEARESTNEIGHBORQUERY_NUMERICFILTER_OPERATOR']._serialized_end = 2972
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS']._serialized_start = 2990
    _globals['_NEARESTNEIGHBORQUERY_PARAMETERS']._serialized_end = 3089
    _globals['_SEARCHNEARESTENTITIESREQUEST']._serialized_start = 3104
    _globals['_SEARCHNEARESTENTITIESREQUEST']._serialized_end = 3311
    _globals['_NEARESTNEIGHBORS']._serialized_start = 3314
    _globals['_NEARESTNEIGHBORS']._serialized_end = 3549
    _globals['_NEARESTNEIGHBORS_NEIGHBOR']._serialized_start = 3414
    _globals['_NEARESTNEIGHBORS_NEIGHBOR']._serialized_end = 3549
    _globals['_SEARCHNEARESTENTITIESRESPONSE']._serialized_start = 3551
    _globals['_SEARCHNEARESTENTITIESRESPONSE']._serialized_end = 3660
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST']._serialized_start = 3663
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST']._serialized_end = 4499
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES']._serialized_start = 3894
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES']._serialized_end = 4499
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE']._serialized_start = 4107
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE']._serialized_end = 4499
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE_FEATUREVALUEANDTIMESTAMP']._serialized_start = 4350
    _globals['_FEATUREVIEWDIRECTWRITEREQUEST_DATAKEYANDFEATUREVALUES_FEATURE_FEATUREVALUEANDTIMESTAMP']._serialized_end = 4485
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE']._serialized_start = 4502
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE']._serialized_end = 4824
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE_WRITERESPONSE']._serialized_start = 4677
    _globals['_FEATUREVIEWDIRECTWRITERESPONSE_WRITERESPONSE']._serialized_end = 4824
    _globals['_FEATUREONLINESTORESERVICE']._serialized_start = 4927
    _globals['_FEATUREONLINESTORESERVICE']._serialized_end = 6183