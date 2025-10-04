"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/feature_online_store_admin_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_online_store_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__online__store__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_view_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__view__pb2
from .....google.cloud.aiplatform.v1beta1 import feature_view_sync_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_feature__view__sync__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/cloud/aiplatform/v1beta1/feature_online_store_admin_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a:google/cloud/aiplatform/v1beta1/feature_online_store.proto\x1a2google/cloud/aiplatform/v1beta1/feature_view.proto\x1a7google/cloud/aiplatform/v1beta1/feature_view_sync.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xe5\x01\n\x1fCreateFeatureOnlineStoreRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore\x12V\n\x14feature_online_store\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreB\x03\xe0A\x02\x12$\n\x17feature_online_store_id\x18\x03 \x01(\tB\x03\xe0A\x02"b\n\x1cGetFeatureOnlineStoreRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore"\xaf\x01\n\x1eListFeatureOnlineStoresRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\x12,aiplatform.googleapis.com/FeatureOnlineStore\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x8e\x01\n\x1fListFeatureOnlineStoresResponse\x12R\n\x15feature_online_stores\x18\x01 \x03(\x0b23.google.cloud.aiplatform.v1beta1.FeatureOnlineStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xaa\x01\n\x1fUpdateFeatureOnlineStoreRequest\x12V\n\x14feature_online_store\x18\x01 \x01(\x0b23.google.cloud.aiplatform.v1beta1.FeatureOnlineStoreB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"t\n\x1fDeleteFeatureOnlineStoreRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore\x12\r\n\x05force\x18\x02 \x01(\x08"\xea\x01\n\x18CreateFeatureViewRequest\x12D\n\x06parent\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,aiplatform.googleapis.com/FeatureOnlineStore\x12G\n\x0cfeature_view\x18\x02 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.FeatureViewB\x03\xe0A\x02\x12\x1c\n\x0ffeature_view_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12!\n\x14run_sync_immediately\x18\x04 \x01(\x08B\x03\xe0A\x05"T\n\x15GetFeatureViewRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"\xa1\x01\n\x17ListFeatureViewsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\x12%aiplatform.googleapis.com/FeatureView\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"x\n\x18ListFeatureViewsResponse\x12C\n\rfeature_views\x18\x01 \x03(\x0b2,.google.cloud.aiplatform.v1beta1.FeatureView\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x94\x01\n\x18UpdateFeatureViewRequest\x12G\n\x0cfeature_view\x18\x01 \x01(\x0b2,.google.cloud.aiplatform.v1beta1.FeatureViewB\x03\xe0A\x02\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMask"W\n\x18DeleteFeatureViewRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"\x80\x01\n)CreateFeatureOnlineStoreOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x80\x01\n)UpdateFeatureOnlineStoreOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"y\n"CreateFeatureViewOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"y\n"UpdateFeatureViewOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"]\n\x16SyncFeatureViewRequest\x12C\n\x0cfeature_view\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView"4\n\x17SyncFeatureViewResponse\x12\x19\n\x11feature_view_sync\x18\x01 \x01(\t"\\\n\x19GetFeatureViewSyncRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/FeatureViewSync"\xa5\x01\n\x1bListFeatureViewSyncsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%aiplatform.googleapis.com/FeatureView\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x85\x01\n\x1cListFeatureViewSyncsResponse\x12L\n\x12feature_view_syncs\x18\x01 \x03(\x0b20.google.cloud.aiplatform.v1beta1.FeatureViewSync\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xf6\x1b\n\x1eFeatureOnlineStoreAdminService\x12\xd0\x02\n\x18CreateFeatureOnlineStore\x12@.google.cloud.aiplatform.v1beta1.CreateFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\xd2\x01\xcaA?\n\x12FeatureOnlineStore\x12)CreateFeatureOnlineStoreOperationMetadata\xdaA3parent,feature_online_store,feature_online_store_id\x82\xd3\xe4\x93\x02T"</v1beta1/{parent=projects/*/locations/*}/featureOnlineStores:\x14feature_online_store\x12\xd8\x01\n\x15GetFeatureOnlineStore\x12=.google.cloud.aiplatform.v1beta1.GetFeatureOnlineStoreRequest\x1a3.google.cloud.aiplatform.v1beta1.FeatureOnlineStore"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}\x12\xeb\x01\n\x17ListFeatureOnlineStores\x12?.google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresRequest\x1a@.google.cloud.aiplatform.v1beta1.ListFeatureOnlineStoresResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta1/{parent=projects/*/locations/*}/featureOnlineStores\x12\xd2\x02\n\x18UpdateFeatureOnlineStore\x12@.google.cloud.aiplatform.v1beta1.UpdateFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\xd4\x01\xcaA?\n\x12FeatureOnlineStore\x12)UpdateFeatureOnlineStoreOperationMetadata\xdaA feature_online_store,update_mask\x82\xd3\xe4\x93\x02i2Q/v1beta1/{feature_online_store.name=projects/*/locations/*/featureOnlineStores/*}:\x14feature_online_store\x12\x82\x02\n\x18DeleteFeatureOnlineStore\x12@.google.cloud.aiplatform.v1beta1.DeleteFeatureOnlineStoreRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x02>*</v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}\x12\xab\x02\n\x11CreateFeatureView\x129.google.cloud.aiplatform.v1beta1.CreateFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\xbb\x01\xcaA1\n\x0bFeatureView\x12"CreateFeatureViewOperationMetadata\xdaA#parent,feature_view,feature_view_id\x82\xd3\xe4\x93\x02["K/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews:\x0cfeature_view\x12\xd2\x01\n\x0eGetFeatureView\x126.google.cloud.aiplatform.v1beta1.GetFeatureViewRequest\x1a,.google.cloud.aiplatform.v1beta1.FeatureView"Z\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}\x12\xe5\x01\n\x10ListFeatureViews\x128.google.cloud.aiplatform.v1beta1.ListFeatureViewsRequest\x1a9.google.cloud.aiplatform.v1beta1.ListFeatureViewsResponse"\\\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews\x12\xad\x02\n\x11UpdateFeatureView\x129.google.cloud.aiplatform.v1beta1.UpdateFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\xbd\x01\xcaA1\n\x0bFeatureView\x12"UpdateFeatureViewOperationMetadata\xdaA\x18feature_view,update_mask\x82\xd3\xe4\x93\x02h2X/v1beta1/{feature_view.name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:\x0cfeature_view\x12\xfd\x01\n\x11DeleteFeatureView\x129.google.cloud.aiplatform.v1beta1.DeleteFeatureViewRequest\x1a\x1d.google.longrunning.Operation"\x8d\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02M*K/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}\x12\xf8\x01\n\x0fSyncFeatureView\x127.google.cloud.aiplatform.v1beta1.SyncFeatureViewRequest\x1a8.google.cloud.aiplatform.v1beta1.SyncFeatureViewResponse"r\xdaA\x0cfeature_view\x82\xd3\xe4\x93\x02]"X/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:sync:\x01*\x12\xf1\x01\n\x12GetFeatureViewSync\x12:.google.cloud.aiplatform.v1beta1.GetFeatureViewSyncRequest\x1a0.google.cloud.aiplatform.v1beta1.FeatureViewSync"m\xdaA\x04name\x82\xd3\xe4\x93\x02`\x12^/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/featureViewSyncs/*}\x12\x84\x02\n\x14ListFeatureViewSyncs\x12<.google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsRequest\x1a=.google.cloud.aiplatform.v1beta1.ListFeatureViewSyncsResponse"o\xdaA\x06parent\x82\xd3\xe4\x93\x02`\x12^/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/featureViewSyncs\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfa\x01\n#com.google.cloud.aiplatform.v1beta1B#FeatureOnlineStoreAdminServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.feature_online_store_admin_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B#FeatureOnlineStoreAdminServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
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
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureOnlineStore']._serialized_options = b'\xcaA?\n\x12FeatureOnlineStore\x12)CreateFeatureOnlineStoreOperationMetadata\xdaA3parent,feature_online_store,feature_online_store_id\x82\xd3\xe4\x93\x02T"</v1beta1/{parent=projects/*/locations/*}/featureOnlineStores:\x14feature_online_store'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureOnlineStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureOnlineStores']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureOnlineStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v1beta1/{parent=projects/*/locations/*}/featureOnlineStores'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureOnlineStore']._serialized_options = b'\xcaA?\n\x12FeatureOnlineStore\x12)UpdateFeatureOnlineStoreOperationMetadata\xdaA feature_online_store,update_mask\x82\xd3\xe4\x93\x02i2Q/v1beta1/{feature_online_store.name=projects/*/locations/*/featureOnlineStores/*}:\x14feature_online_store'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureOnlineStore']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureOnlineStore']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\nname,force\x82\xd3\xe4\x93\x02>*</v1beta1/{name=projects/*/locations/*/featureOnlineStores/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['CreateFeatureView']._serialized_options = b'\xcaA1\n\x0bFeatureView\x12"CreateFeatureViewOperationMetadata\xdaA#parent,feature_view,feature_view_id\x82\xd3\xe4\x93\x02["K/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews:\x0cfeature_view'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureView']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViews']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViews']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*}/featureViews'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['UpdateFeatureView']._serialized_options = b'\xcaA1\n\x0bFeatureView\x12"UpdateFeatureViewOperationMetadata\xdaA\x18feature_view,update_mask\x82\xd3\xe4\x93\x02h2X/v1beta1/{feature_view.name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:\x0cfeature_view'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['DeleteFeatureView']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02M*K/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['SyncFeatureView']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['SyncFeatureView']._serialized_options = b'\xdaA\x0cfeature_view\x82\xd3\xe4\x93\x02]"X/v1beta1/{feature_view=projects/*/locations/*/featureOnlineStores/*/featureViews/*}:sync:\x01*'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureViewSync']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['GetFeatureViewSync']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02`\x12^/v1beta1/{name=projects/*/locations/*/featureOnlineStores/*/featureViews/*/featureViewSyncs/*}'
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViewSyncs']._loaded_options = None
    _globals['_FEATUREONLINESTOREADMINSERVICE'].methods_by_name['ListFeatureViewSyncs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02`\x12^/v1beta1/{parent=projects/*/locations/*/featureOnlineStores/*/featureViews/*}/featureViewSyncs'
    _globals['_CREATEFEATUREONLINESTOREREQUEST']._serialized_start = 543
    _globals['_CREATEFEATUREONLINESTOREREQUEST']._serialized_end = 772
    _globals['_GETFEATUREONLINESTOREREQUEST']._serialized_start = 774
    _globals['_GETFEATUREONLINESTOREREQUEST']._serialized_end = 872
    _globals['_LISTFEATUREONLINESTORESREQUEST']._serialized_start = 875
    _globals['_LISTFEATUREONLINESTORESREQUEST']._serialized_end = 1050
    _globals['_LISTFEATUREONLINESTORESRESPONSE']._serialized_start = 1053
    _globals['_LISTFEATUREONLINESTORESRESPONSE']._serialized_end = 1195
    _globals['_UPDATEFEATUREONLINESTOREREQUEST']._serialized_start = 1198
    _globals['_UPDATEFEATUREONLINESTOREREQUEST']._serialized_end = 1368
    _globals['_DELETEFEATUREONLINESTOREREQUEST']._serialized_start = 1370
    _globals['_DELETEFEATUREONLINESTOREREQUEST']._serialized_end = 1486
    _globals['_CREATEFEATUREVIEWREQUEST']._serialized_start = 1489
    _globals['_CREATEFEATUREVIEWREQUEST']._serialized_end = 1723
    _globals['_GETFEATUREVIEWREQUEST']._serialized_start = 1725
    _globals['_GETFEATUREVIEWREQUEST']._serialized_end = 1809
    _globals['_LISTFEATUREVIEWSREQUEST']._serialized_start = 1812
    _globals['_LISTFEATUREVIEWSREQUEST']._serialized_end = 1973
    _globals['_LISTFEATUREVIEWSRESPONSE']._serialized_start = 1975
    _globals['_LISTFEATUREVIEWSRESPONSE']._serialized_end = 2095
    _globals['_UPDATEFEATUREVIEWREQUEST']._serialized_start = 2098
    _globals['_UPDATEFEATUREVIEWREQUEST']._serialized_end = 2246
    _globals['_DELETEFEATUREVIEWREQUEST']._serialized_start = 2248
    _globals['_DELETEFEATUREVIEWREQUEST']._serialized_end = 2335
    _globals['_CREATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_start = 2338
    _globals['_CREATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_end = 2466
    _globals['_UPDATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_start = 2469
    _globals['_UPDATEFEATUREONLINESTOREOPERATIONMETADATA']._serialized_end = 2597
    _globals['_CREATEFEATUREVIEWOPERATIONMETADATA']._serialized_start = 2599
    _globals['_CREATEFEATUREVIEWOPERATIONMETADATA']._serialized_end = 2720
    _globals['_UPDATEFEATUREVIEWOPERATIONMETADATA']._serialized_start = 2722
    _globals['_UPDATEFEATUREVIEWOPERATIONMETADATA']._serialized_end = 2843
    _globals['_SYNCFEATUREVIEWREQUEST']._serialized_start = 2845
    _globals['_SYNCFEATUREVIEWREQUEST']._serialized_end = 2938
    _globals['_SYNCFEATUREVIEWRESPONSE']._serialized_start = 2940
    _globals['_SYNCFEATUREVIEWRESPONSE']._serialized_end = 2992
    _globals['_GETFEATUREVIEWSYNCREQUEST']._serialized_start = 2994
    _globals['_GETFEATUREVIEWSYNCREQUEST']._serialized_end = 3086
    _globals['_LISTFEATUREVIEWSYNCSREQUEST']._serialized_start = 3089
    _globals['_LISTFEATUREVIEWSYNCSREQUEST']._serialized_end = 3254
    _globals['_LISTFEATUREVIEWSYNCSRESPONSE']._serialized_start = 3257
    _globals['_LISTFEATUREVIEWSYNCSRESPONSE']._serialized_end = 3390
    _globals['_FEATUREONLINESTOREADMINSERVICE']._serialized_start = 3393
    _globals['_FEATUREONLINESTOREADMINSERVICE']._serialized_end = 6967