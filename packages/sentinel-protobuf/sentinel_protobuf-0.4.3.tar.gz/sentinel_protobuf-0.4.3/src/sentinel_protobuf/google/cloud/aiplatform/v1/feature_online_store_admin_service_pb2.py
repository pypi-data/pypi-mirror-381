"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/feature_online_store_admin_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1 import feature_online_store_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__online__store__pb2
from .....google.cloud.aiplatform.v1 import feature_view_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__view__pb2
from .....google.cloud.aiplatform.v1 import feature_view_sync_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_feature__view__sync__pb2
from .....google.cloud.aiplatform.v1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/cloud/aiplatform/v1/feature_online_store_admin_service.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a5google/cloud/aiplatform/v1/feature_online_store.proto\x1a-google/cloud/aiplatform/v1/feature_view.proto\x1a2google/cloud/aiplatform/v1/feature_view_sync.proto\x1a*google/cloud/aiplatform/v1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xe0\x01\n\x1fCreateFeatureOnlineStoreRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore\x12Q\n\x14feature_online_store\x18\x02 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureOnlineStoreB\x03\xe0A\x02\x12$\n\x17feature_online_store_id\x18\x03 \x01(\tB\x03\xe0A\x02"b\n\x1cGetFeatureOnlineStoreRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore"\xaf\x01\n\x1eListFeatureOnlineStoresRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x89\x01\n\x1fListFeatureOnlineStoresResponse\x12M\n\x15feature_online_stores\x18\x01 \x03(\x0b2..google.cloud.aiplatform.v1.FeatureOnlineStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa5\x01\n\x1fUpdateFeatureOnlineStoreRequest\x12Q\n\x14feature_online_store\x18\x01 \x01(\x0b2..google.cloud.aiplatform.v1.FeatureOnlineStoreB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"t\n\x1fDeleteFeatureOnlineStoreRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore\x12\r\n\x05force\x18\x02 \x01(\x08"\xe5\x01\n\x18CreateFeatureViewRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore\x12B\n\x0cfeature_view\x18\x02 \x01(\x0b2\'.google.cloud.aiplatform.v1.FeatureViewB\x03\xe0A\x02\x12\x1c\n\x0ffeature_view_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12!\n\x14run_sync_immediately\x18\x04 \x01(\x08B\x03\xe0A\x05"T\n\x15GetFeatureViewRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"\xa1\x01\n\x17ListFeatureViewsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%aiplatform.googleapis.com/FeatureView\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"s\n\x18ListFeatureViewsResponse\x12>\n\rfeature_views\x18\x01 \x03(\x0b2\'.google.cloud.aiplatform.v1.FeatureView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8f\x01\n\x18UpdateFeatureViewRequest\x12B\n\x0cfeature_view\x18\x01 \x01(\x0b2\'.google.cloud.aiplatform.v1.FeatureViewB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"W\n\x18DeleteFeatureViewRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"{\n)CreateFeatureOnlineStoreOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"{\n)UpdateFeatureOnlineStoreOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"t\n"CreateFeatureViewOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"t\n"UpdateFeatureViewOperationMetadata\x12N\n\x10generic_metadata\x18\x01 \x01(\x0b24.google.cloud.aiplatform.v1.GenericOperationMetadata"]\n\x16SyncFeatureViewRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"4\n\x17SyncFeatureViewResponse\x12\x19\n\x11feature_view_sync\x18\x01 \x01(\t"\\\n\x19GetFeatureViewSyncRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/FeatureViewSync"\xa5\x01\n\x1bListFeatureViewSyncsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x80\x01\n\x1cListFeatureViewSyncsResponse\x12G\n\x12feature_view_syncs\x18\x01 \x03(\x0b2+.google.cloud.aiplatform.v1.FeatureViewSync\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xd0\x1a\n\x1eFeatureOnlineStoreAdminService\x12\xc6\x02\n\x18CreateFeatureOnlineStore\x12;.google.cloud.aiplatform.v1.CreateFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\xcd\x01\xcaA?\n\x12FeatureOnlineStore\x12)CreateFeatureOnlineStoreOperationMetadata\xdaA3parent,feature_online_store,feature_online_store_id\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/featureOnlineStores:\x14feature_online_store\x12\xc9\x01\n\x15GetFeatureOnlineStore\x128.google.cloud.aiplatform.v1.GetFeatureOnlineStoreRequest\x1a..google.cloud.aiplatform.v1.FeatureOnlineStore"F\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/featureOnlineStores/*}\x12\xdc\x01\n\x17ListFeatureOnlineStores\x12:.google.cloud.aiplatform.v1.ListFeatureOnlineStoresRequest\x1a;.google.cloud.aiplatform.v1.ListFeatureOnlineStoresResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/featureOnlineStores\x12\xc8\x02\n\x18UpdateFeatureOnlineStore\x12;.google.cloud.aiplatform.v1.UpdateFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\xcf\x01\xcaA?\n\x12FeatureOnlineStore\x12)UpdateFeatureOnlineStoreOperationMetadata\xdaA feature_online_store,update_mask\x82\xd3\xe4\x93\x02d2L/v1/{feature_online_store.name=projects/*/locations/*/featureOnlineStores/*}:\x14feature_online_store\x12\xf7\x01\n\x18DeleteFeatureOnlineStore\x12;.google.cloud.aiplatform.v1.DeleteFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\x7f\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/featureOnlineStores/*}\x12\xa1\x02\n\x11CreateFeatureView\x124.google.cloud.aiplatform.v1.CreateFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\xb6\x01\xcaA1\n\x0bFeatureView\x12"CreateFeatureViewOperationMetadata\xdaA#parent,feature_view,feature_view_id\x82\xd3\xe4\x93\x02V"F/v1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews:\x0cfeature_view\x12\xc3\x01\n\x0eGetFeatureView\x121.google.cloud.aiplatform.v1.GetFeatureViewRequest\x1a\'.google.cloud.aiplatform.v1.FeatureView"U\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}\x12\xd6\x01\n\x10ListFeatureViews\x123.google.cloud.aiplatform.v1.ListFeatureViewsRequest\x1a4.google.cloud.aiplatform.v1.ListFeatureViewsResponse"W\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews\x12\xa3\x02\n\x11UpdateFeatureView\x124.google.cloud.aiplatform.v1.UpdateFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\xb8\x01\xcaA1\n\x0bFeatureView\x12"UpdateFeatureViewOperationMetadata\xdaA\x18feature_view,update_mask\x82\xd3\xe4\x93\x02c2S/v1/{feature_view.name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:\x0cfeature_view\x12\xf3\x01\n\x11DeleteFeatureView\x124.google.cloud.aiplatform.v1.DeleteFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\x88\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}\x12\xe9\x01\n\x0fSyncFeatureView\x122.google.cloud.aiplatform.v1.SyncFeatureViewRequest\x1a3.google.cloud.aiplatform.v1.SyncFeatureViewResponse"m\xdaA\x0cfeature_view\x82\xd3\xe4\x93\x02X"S/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:sync:\x01*\x12\xe2\x01\n\x12GetFeatureViewSync\x125.google.cloud.aiplatform.v1.GetFeatureViewSyncRequest\x1a+.google.cloud.aiplatform.v1.FeatureViewSync"h\xdaA\x04name\x82\xd3\xe4\x93\x02[\x12Y/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/featureViewSyncs/*}\x12\xf5\x01\n\x14ListFeatureViewSyncs\x127.google.cloud.aiplatform.v1.ListFeatureViewSyncsRequest\x1a8.google.cloud.aiplatform.v1.ListFeatureViewSyncsResponse"j\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12Y/v1/{parent=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/featureViewSyncs\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xe1\x01\n\x1ecom.google.cloud.aiplatform.v1B#FeatureOnlineStoreAdminServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.feature_online_store_admin_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B#FeatureOnlineStoreAdminServiceProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore'
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store']._loaded_options = None
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store_id']._loaded_options = None
    _globals['_CREATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETFEATUREONLINESTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREONLINESTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore'
    _globals['_LISTFEATUREONLINESTORESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREONLINESTORESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore'
    _globals['_UPDATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store']._loaded_options = None
    _globals['_UPDATEFEATUREONLINESTOREREQUEST'].fields_by_name['feature_online_store']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFEATUREONLINESTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREONLINESTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore'
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore'
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['feature_view']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['feature_view_id']._loaded_options = None
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['feature_view_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['run_sync_immediately']._loaded_options = None
    _globals['_CREATEFEATUREVIEWREQUEST'].fields_by_name['run_sync_immediately']._serialized_options = b'\xe0A\x05'
    _globals['_GETFEATUREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREVIEWREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_LISTFEATUREVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\x12%aiplatform.googleapis.com/FeatureView"
    _globals['_UPDATEFEATUREVIEWREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_UPDATEFEATUREVIEWREQUEST'].fields_by_name['feature_view']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEFEATUREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEFEATUREVIEWREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_SYNCFEATUREVIEWREQUEST'].fields_by_name['feature_view']._loaded_options = None
    _globals['_SYNCFEATUREVIEWREQUEST'].fields_by_name['feature_view']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_GETFEATUREVIEWSYNCREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETFEATUREVIEWSYNCREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/FeatureViewSync'
    _globals['_LISTFEATUREVIEWSYNCSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTFEATUREVIEWSYNCSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%aiplatform.googleapis.com/FeatureView"
    _globals['_FEATUREONLINESTOREADMINSERVICE']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureOnlineStore']._serialized_options = b'\xcaA?\n\x12FeatureOnlineStore\x12)CreateFeatureOnlineStoreOperationMetadata\xdaA3parent,feature_online_store,feature_online_store_id\x82\xd3\xe4\x93\x02O"7/v1/{parent=projects/*/locations/*}/featureOnlineStores:\x14feature_online_store'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureOnlineStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x029\x127/v1/{name=projects/*/locations/*/featureOnlineStores/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureOnlineStores']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureOnlineStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029\x127/v1/{parent=projects/*/locations/*}/featureOnlineStores'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureOnlineStore']._serialized_options = b'\xcaA?\n\x12FeatureOnlineStore\x12)UpdateFeatureOnlineStoreOperationMetadata\xdaA feature_online_store,update_mask\x82\xd3\xe4\x93\x02d2L/v1/{feature_online_store.name=projects/*/locations/*/featureOnlineStores/*}:\x14feature_online_store'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureOnlineStore']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x029*7/v1/{name=projects/*/locations/*/featureOnlineStores/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureView']._serialized_options = b'\xcaA1\n\x0bFeatureView\x12"CreateFeatureViewOperationMetadata\xdaA#parent,feature_view,feature_view_id\x82\xd3\xe4\x93\x02V"F/v1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews:\x0cfeature_view'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureView']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02H\x12F/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViews']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViews']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02H\x12F/v1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureView']._serialized_options = b'\xcaA1\n\x0bFeatureView\x12"UpdateFeatureViewOperationMetadata\xdaA\x18feature_view,update_mask\x82\xd3\xe4\x93\x02c2S/v1/{feature_view.name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:\x0cfeature_view'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureView']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02H*F/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['SyncFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['SyncFeatureView']._serialized_options = b'\xdaA\x0cfeature_view\x82\xd3\xe4\x93\x02X"S/v1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:sync:\x01*'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureViewSync']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureViewSync']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02[\x12Y/v1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/featureViewSyncs/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViewSyncs']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViewSyncs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02[\x12Y/v1/{parent=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/featureViewSyncs'
    _globals['_CREATEFEATUREONLINESTOREREQUEST']._serialized_start = 513
    _globals['_CREATEFEATUREONLINESTOREREQUEST']._serialized_end = 737
    _globals['_GETFEATUREONLINESTOREREQUEST']._serialized_start = 739
    _globals['_GETFEATUREONLINESTOREREQUEST']._serialized_end = 837
    _globals['_LISTFEATUREONLINESTORESREQUEST']._serialized_start = 840
    _globals['_LISTFEATUREONLINESTORESREQUEST']._serialized_end = 1015
    _globals['_LISTFEATUREONLINESTORESRESPONSE']._serialized_start = 1018
    _globals['_LISTFEATUREONLINESTORESRESPONSE']._serialized_end = 1155
    _globals['_UPDATEFEATUREONLINESTOREREQUEST']._serialized_start = 1158
    _globals['_UPDATEFEATUREONLINESTOREREQUEST']._serialized_end = 1323
    _globals['_DELETEFEATUREONLINESTOREREQUEST']._serialized_start = 1325
    _globals['_DELETEFEATUREONLINESTOREREQUEST']._serialized_end = 1441
    _globals['_CREATEFEATUREVIEWREQUEST']._serialized_start = 1444
    _globals['_CREATEFEATUREVIEWREQUEST']._serialized_end = 1673
    _globals['_GETFEATUREVIEWREQUEST']._serialized_start = 1675
    _globals['_GETFEATUREVIEWREQUEST']._serialized_end = 1759
    _globals['_LISTFEATUREVIEWSREQUEST']._serialized_start = 1762
    _globals['_LISTFEATUREVIEWSREQUEST']._serialized_end = 1923
    _globals['_LISTFEATUREVIEWSRESPONSE']._serialized_start = 1925
    _globals['_LISTFEATUREVIEWSRESPONSE']._serialized_end = 2040
    _globals['_UPDATEFEATUREVIEWREQUEST']._serialized_start = 2043
    _globals['_UPDATEFEATUREVIEWREQUEST']._serialized_end = 2186
    _globals['_DELETEFEATUREVIEWREQUEST']._serialized_start = 2188
    _globals['_DELETEFEATUREVIEWREQUEST']._serialized_end = 2275
    _globals['_CREATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_start = 2277
    _globals['_CREATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_end = 2400
    _globals['_UPDATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_start = 2402
    _globals['_UPDATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_end = 2525
    _globals['_CREATEFEATUREVIEWOPERATIONMETADATA']._serialized_start = 2527
    _globals['_CREATEFEATUREVIEWOPERATIONMETADATA']._serialized_end = 2643
    _globals['_UPDATEFEATUREVIEWOPERATIONMETADATA']._serialized_start = 2645
    _globals['_UPDATEFEATUREVIEWOPERATIONMETADATA']._serialized_end = 2761
    _globals['_SYNCFEATUREVIEWREQUEST']._serialized_start = 2763
    _globals['_SYNCFEATUREVIEWREQUEST']._serialized_end = 2856
    _globals['_SYNCFEATUREVIEWRESPONSE']._serialized_start = 2858
    _globals['_SYNCFEATUREVIEWRESPONSE']._serialized_end = 2910
    _globals['_GETFEATUREVIEWSYNCREQUEST']._serialized_start = 2912
    _globals['_GETFEATUREVIEWSYNCREQUEST']._serialized_end = 3004
    _globals['_LISTFEATUREVIEWSYNCSREQUEST']._serialized_start = 3007
    _globals['_LISTFEATUREVIEWSYNCSREQUEST']._serialized_end = 3172
    _globals['_LISTFEATUREVIEWSYNCSRESPONSE']._serialized_start = 3175
    _globals['_LISTFEATUREVIEWSYNCSRESPONSE']._serialized_end = 3303
    _globals['_FEATUREONLINESTOREADMINSERVICE']._serialized_start = 3306
    _globals['_FEATUREONLINESTOREADMINSERVICE']._serialized_end = 6714