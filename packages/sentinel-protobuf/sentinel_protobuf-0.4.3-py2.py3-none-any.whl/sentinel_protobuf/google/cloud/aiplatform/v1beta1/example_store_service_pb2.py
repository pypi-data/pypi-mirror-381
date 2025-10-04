"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/example_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import example_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_example__pb2
from .....google.cloud.aiplatform.v1beta1 import example_store_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_example__store__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/aiplatform/v1beta1/example_store_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/example.proto\x1a3google/cloud/aiplatform/v1beta1/example_store.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xa1\x01\n\x19CreateExampleStoreRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12I\n\rexample_store\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.ExampleStoreB\x03\xe0A\x02"z\n#CreateExampleStoreOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"V\n\x16GetExampleStoreRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore"\x9c\x01\n\x19UpdateExampleStoreRequest\x12I\n\rexample_store\x18\x01 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.ExampleStoreB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"z\n#UpdateExampleStoreOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"Y\n\x19DeleteExampleStoreRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore"z\n#DeleteExampleStoreOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"\x9b\x01\n\x18ListExampleStoresRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x16\n\tpage_size\x18\x03 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x04 \x01(\tB\x03\xe0A\x01"{\n\x19ListExampleStoresResponse\x12E\n\x0eexample_stores\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.ExampleStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xe1\x01\n\x07Example\x12Y\n\x17stored_contents_example\x18\x06 \x01(\x0b26.google.cloud.aiplatform.v1beta1.StoredContentsExampleH\x00\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x1a\n\nexample_id\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x0e\n\x0cexample_type"\xb7\x01\n\x15UpsertExamplesRequest\x12E\n\rexample_store\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore\x12?\n\x08examples\x18\x02 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.ExampleB\x03\xe0A\x02\x12\x16\n\toverwrite\x18\x04 \x01(\x08B\x03\xe0A\x01"\xec\x01\n\x16UpsertExamplesResponse\x12U\n\x07results\x18\x01 \x03(\x0b2D.google.cloud.aiplatform.v1beta1.UpsertExamplesResponse.UpsertResult\x1a{\n\x0cUpsertResult\x12;\n\x07example\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ExampleH\x00\x12$\n\x06status\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00B\x08\n\x06result"\xf3\x01\n\x15RemoveExamplesRequest\x12f\n\x1estored_contents_example_filter\x18\x08 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.StoredContentsExampleFilterH\x00\x12E\n\rexample_store\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore\x12\x18\n\x0bexample_ids\x18\x06 \x03(\tB\x03\xe0A\x01B\x11\n\x0fmetadata_filter"-\n\x16RemoveExamplesResponse\x12\x13\n\x0bexample_ids\x18\x01 \x03(\t"\xf0\x01\n\x15SearchExamplesRequest\x12n\n"stored_contents_example_parameters\x18\x06 \x01(\x0b2@.google.cloud.aiplatform.v1beta1.StoredContentsExampleParametersH\x00\x12E\n\rexample_store\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore\x12\x12\n\x05top_k\x18\x02 \x01(\x03B\x03\xe0A\x01B\x0c\n\nparameters"\xd8\x01\n\x16SearchExamplesResponse\x12W\n\x07results\x18\x01 \x03(\x0b2F.google.cloud.aiplatform.v1beta1.SearchExamplesResponse.SimilarExample\x1ae\n\x0eSimilarExample\x129\n\x07example\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.Example\x12\x18\n\x10similarity_score\x18\x02 \x01(\x02"\xa3\x02\n\x14FetchExamplesRequest\x12f\n\x1estored_contents_example_filter\x18\x08 \x01(\x0b2<.google.cloud.aiplatform.v1beta1.StoredContentsExampleFilterH\x00\x12E\n\rexample_store\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bexample_ids\x18\x06 \x03(\tB\x03\xe0A\x01B\x11\n\x0fmetadata_filter"l\n\x15FetchExamplesResponse\x12:\n\x08examples\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.Example\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xe1\x11\n\x13ExampleStoreService\x12\xce\x02\n\x12CreateExampleStore\x12:.google.cloud.aiplatform.v1beta1.CreateExampleStoreRequest\x1a\x1d.google.longrunning.Operation"\xdc\x01\xcaA3\n\x0cExampleStore\x12#CreateExampleStoreOperationMetadata\xdaA\x14parent,example_store\x82\xd3\xe4\x93\x02\x88\x01"6/v1beta1/{parent=projects/*/locations/*}/exampleStores:\rexample_storeZ?"=/v1beta1/{parent=projects/*/locations/*}/exampleStores:create\x12\xc0\x01\n\x0fGetExampleStore\x127.google.cloud.aiplatform.v1beta1.GetExampleStoreRequest\x1a-.google.cloud.aiplatform.v1beta1.ExampleStore"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/exampleStores/*}\x12\x9f\x02\n\x12UpdateExampleStore\x12:.google.cloud.aiplatform.v1beta1.UpdateExampleStoreRequest\x1a\x1d.google.longrunning.Operation"\xad\x01\xcaA3\n\x0cExampleStore\x12#UpdateExampleStoreOperationMetadata\xdaA\x19example_store,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{example_store.name=projects/*/locations/*/exampleStores/*}:\rexample_store\x12\xf6\x01\n\x12DeleteExampleStore\x12:.google.cloud.aiplatform.v1beta1.DeleteExampleStoreRequest\x1a\x1d.google.longrunning.Operation"\x84\x01\xcaA<\n\x15google.protobuf.Empty\x12#DeleteExampleStoreOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/exampleStores/*}\x12\xd3\x01\n\x11ListExampleStores\x129.google.cloud.aiplatform.v1beta1.ListExampleStoresRequest\x1a:.google.cloud.aiplatform.v1beta1.ListExampleStoresResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/exampleStores\x12\xdc\x01\n\x0eUpsertExamples\x126.google.cloud.aiplatform.v1beta1.UpsertExamplesRequest\x1a7.google.cloud.aiplatform.v1beta1.UpsertExamplesResponse"Y\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:upsertExamples:\x01*\x12\xdc\x01\n\x0eRemoveExamples\x126.google.cloud.aiplatform.v1beta1.RemoveExamplesRequest\x1a7.google.cloud.aiplatform.v1beta1.RemoveExamplesResponse"Y\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:removeExamples:\x01*\x12\xdc\x01\n\x0eSearchExamples\x126.google.cloud.aiplatform.v1beta1.SearchExamplesRequest\x1a7.google.cloud.aiplatform.v1beta1.SearchExamplesResponse"Y\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:searchExamples:\x01*\x12\xd8\x01\n\rFetchExamples\x125.google.cloud.aiplatform.v1beta1.FetchExamplesRequest\x1a6.google.cloud.aiplatform.v1beta1.FetchExamplesResponse"X\x82\xd3\xe4\x93\x02R"M/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:fetchExamples:\x01*\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xef\x01\n#com.google.cloud.aiplatform.v1beta1B\x18ExampleStoreServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.example_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x18ExampleStoreServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATEEXAMPLESTOREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEEXAMPLESTOREREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEEXAMPLESTOREREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_CREATEEXAMPLESTOREREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02'
    _globals['_GETEXAMPLESTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETEXAMPLESTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_UPDATEEXAMPLESTOREREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_UPDATEEXAMPLESTOREREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEEXAMPLESTOREREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEEXAMPLESTOREREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEEXAMPLESTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEEXAMPLESTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEXAMPLESTORESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['display_name']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLE'].fields_by_name['example_id']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['example_id']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_EXAMPLE'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXAMPLE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['examples']._loaded_options = None
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['examples']._serialized_options = b'\xe0A\x02'
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['overwrite']._loaded_options = None
    _globals['_UPSERTEXAMPLESREQUEST'].fields_by_name['overwrite']._serialized_options = b'\xe0A\x01'
    _globals['_REMOVEEXAMPLESREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_REMOVEEXAMPLESREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_REMOVEEXAMPLESREQUEST'].fields_by_name['example_ids']._loaded_options = None
    _globals['_REMOVEEXAMPLESREQUEST'].fields_by_name['example_ids']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHEXAMPLESREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_SEARCHEXAMPLESREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_SEARCHEXAMPLESREQUEST'].fields_by_name['top_k']._loaded_options = None
    _globals['_SEARCHEXAMPLESREQUEST'].fields_by_name['top_k']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['example_store']._loaded_options = None
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['example_store']._serialized_options = b'\xe0A\x02\xfaA(\n&aiplatform.googleapis.com/ExampleStore'
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['example_ids']._loaded_options = None
    _globals['_FETCHEXAMPLESREQUEST'].fields_by_name['example_ids']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLESTORESERVICE']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['CreateExampleStore']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['CreateExampleStore']._serialized_options = b'\xcaA3\n\x0cExampleStore\x12#CreateExampleStoreOperationMetadata\xdaA\x14parent,example_store\x82\xd3\xe4\x93\x02\x88\x01"6/v1beta1/{parent=projects/*/locations/*}/exampleStores:\rexample_storeZ?"=/v1beta1/{parent=projects/*/locations/*}/exampleStores:create'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['GetExampleStore']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['GetExampleStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1beta1/{name=projects/*/locations/*/exampleStores/*}'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['UpdateExampleStore']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['UpdateExampleStore']._serialized_options = b'\xcaA3\n\x0cExampleStore\x12#UpdateExampleStoreOperationMetadata\xdaA\x19example_store,update_mask\x82\xd3\xe4\x93\x02U2D/v1beta1/{example_store.name=projects/*/locations/*/exampleStores/*}:\rexample_store'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['DeleteExampleStore']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['DeleteExampleStore']._serialized_options = b'\xcaA<\n\x15google.protobuf.Empty\x12#DeleteExampleStoreOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1beta1/{name=projects/*/locations/*/exampleStores/*}'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['ListExampleStores']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['ListExampleStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1beta1/{parent=projects/*/locations/*}/exampleStores'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['UpsertExamples']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['UpsertExamples']._serialized_options = b'\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:upsertExamples:\x01*'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['RemoveExamples']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['RemoveExamples']._serialized_options = b'\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:removeExamples:\x01*'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['SearchExamples']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['SearchExamples']._serialized_options = b'\x82\xd3\xe4\x93\x02S"N/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:searchExamples:\x01*'
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['FetchExamples']._loaded_options = None
    _globals['_EXAMPLESTORESERVICE'].methods_by_name['FetchExamples']._serialized_options = b'\x82\xd3\xe4\x93\x02R"M/v1beta1/{example_store=projects/*/locations/*/exampleStores/*}:fetchExamples:\x01*'
    _globals['_CREATEEXAMPLESTOREREQUEST']._serialized_start = 519
    _globals['_CREATEEXAMPLESTOREREQUEST']._serialized_end = 680
    _globals['_CREATEEXAMPLESTOREOPERATIONMETADATA']._serialized_start = 682
    _globals['_CREATEEXAMPLESTOREOPERATIONMETADATA']._serialized_end = 804
    _globals['_GETEXAMPLESTOREREQUEST']._serialized_start = 806
    _globals['_GETEXAMPLESTOREREQUEST']._serialized_end = 892
    _globals['_UPDATEEXAMPLESTOREREQUEST']._serialized_start = 895
    _globals['_UPDATEEXAMPLESTOREREQUEST']._serialized_end = 1051
    _globals['_UPDATEEXAMPLESTOREOPERATIONMETADATA']._serialized_start = 1053
    _globals['_UPDATEEXAMPLESTOREOPERATIONMETADATA']._serialized_end = 1175
    _globals['_DELETEEXAMPLESTOREREQUEST']._serialized_start = 1177
    _globals['_DELETEEXAMPLESTOREREQUEST']._serialized_end = 1266
    _globals['_DELETEEXAMPLESTOREOPERATIONMETADATA']._serialized_start = 1268
    _globals['_DELETEEXAMPLESTOREOPERATIONMETADATA']._serialized_end = 1390
    _globals['_LISTEXAMPLESTORESREQUEST']._serialized_start = 1393
    _globals['_LISTEXAMPLESTORESREQUEST']._serialized_end = 1548
    _globals['_LISTEXAMPLESTORESRESPONSE']._serialized_start = 1550
    _globals['_LISTEXAMPLESTORESRESPONSE']._serialized_end = 1673
    _globals['_EXAMPLE']._serialized_start = 1676
    _globals['_EXAMPLE']._serialized_end = 1901
    _globals['_UPSERTEXAMPLESREQUEST']._serialized_start = 1904
    _globals['_UPSERTEXAMPLESREQUEST']._serialized_end = 2087
    _globals['_UPSERTEXAMPLESRESPONSE']._serialized_start = 2090
    _globals['_UPSERTEXAMPLESRESPONSE']._serialized_end = 2326
    _globals['_UPSERTEXAMPLESRESPONSE_UPSERTRESULT']._serialized_start = 2203
    _globals['_UPSERTEXAMPLESRESPONSE_UPSERTRESULT']._serialized_end = 2326
    _globals['_REMOVEEXAMPLESREQUEST']._serialized_start = 2329
    _globals['_REMOVEEXAMPLESREQUEST']._serialized_end = 2572
    _globals['_REMOVEEXAMPLESRESPONSE']._serialized_start = 2574
    _globals['_REMOVEEXAMPLESRESPONSE']._serialized_end = 2619
    _globals['_SEARCHEXAMPLESREQUEST']._serialized_start = 2622
    _globals['_SEARCHEXAMPLESREQUEST']._serialized_end = 2862
    _globals['_SEARCHEXAMPLESRESPONSE']._serialized_start = 2865
    _globals['_SEARCHEXAMPLESRESPONSE']._serialized_end = 3081
    _globals['_SEARCHEXAMPLESRESPONSE_SIMILAREXAMPLE']._serialized_start = 2980
    _globals['_SEARCHEXAMPLESRESPONSE_SIMILAREXAMPLE']._serialized_end = 3081
    _globals['_FETCHEXAMPLESREQUEST']._serialized_start = 3084
    _globals['_FETCHEXAMPLESREQUEST']._serialized_end = 3375
    _globals['_FETCHEXAMPLESRESPONSE']._serialized_start = 3377
    _globals['_FETCHEXAMPLESRESPONSE']._serialized_end = 3485
    _globals['_EXAMPLESTORESERVICE']._serialized_start = 3488
    _globals['_EXAMPLESTORESERVICE']._serialized_end = 5761