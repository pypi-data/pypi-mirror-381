"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/document_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_document__pb2
from .....google.cloud.discoveryengine.v1 import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1 import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/discoveryengine/v1/document_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a.google/cloud/discoveryengine/v1/document.proto\x1a3google/cloud/discoveryengine/v1/import_config.proto\x1a2google/cloud/discoveryengine/v1/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"S\n\x12GetDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"|\n\x14ListDocumentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"n\n\x15ListDocumentsResponse\x12<\n\tdocuments\x18\x01 \x03(\x0b2).google.cloud.discoveryengine.v1.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb2\x01\n\x15CreateDocumentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12@\n\x08document\x18\x02 \x01(\x0b2).google.cloud.discoveryengine.v1.DocumentB\x03\xe0A\x02\x12\x18\n\x0bdocument_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa1\x01\n\x15UpdateDocumentRequest\x12@\n\x08document\x18\x01 \x01(\x0b2).google.cloud.discoveryengine.v1.DocumentB\x03\xe0A\x02\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"V\n\x15DeleteDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"\x9b\x04\n BatchGetDocumentsMetadataRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12_\n\x07matcher\x18\x02 \x01(\x0b2I.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest.MatcherB\x03\xe0A\x02\x1a\x1b\n\x0bUrisMatcher\x12\x0c\n\x04uris\x18\x01 \x03(\t\x1aU\n\x0bFhirMatcher\x12F\n\x0efhir_resources\x18\x01 \x03(\tB.\xe0A\x02\xfaA(\n&healthcare.googleapis.com/FhirResource\x1a\xe2\x01\n\x07Matcher\x12e\n\x0curis_matcher\x18\x01 \x01(\x0b2M.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest.UrisMatcherH\x00\x12e\n\x0cfhir_matcher\x18\x02 \x01(\x0b2M.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest.FhirMatcherH\x00B\t\n\x07matcher"\xa0\x05\n!BatchGetDocumentsMetadataResponse\x12o\n\x12documents_metadata\x18\x01 \x03(\x0b2S.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse.DocumentMetadata\x1a\xb2\x03\n\x10DocumentMetadata\x12w\n\rmatcher_value\x18\x02 \x01(\x0b2`.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue\x12W\n\x05state\x18\x03 \x01(\x0e2H.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse.State\x127\n\x13last_refreshed_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1d\n\x15data_ingestion_source\x18\x05 \x01(\t\x1at\n\x0cMatcherValue\x12\r\n\x03uri\x18\x01 \x01(\tH\x00\x12D\n\rfhir_resource\x18\x02 \x01(\tB+\xfaA(\n&healthcare.googleapis.com/FhirResourceH\x00B\x0f\n\rmatcher_value"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INDEXED\x10\x01\x12\x16\n\x12NOT_IN_TARGET_SITE\x10\x02\x12\x10\n\x0cNOT_IN_INDEX\x10\x032\x9d\x16\n\x0fDocumentService\x12\x9c\x02\n\x0bGetDocument\x123.google.cloud.discoveryengine.v1.GetDocumentRequest\x1a).google.cloud.discoveryengine.v1.Document"\xac\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9e\x01\x12E/v1/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZU\x12S/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\xaf\x02\n\rListDocuments\x125.google.cloud.discoveryengine.v1.ListDocumentsRequest\x1a6.google.cloud.discoveryengine.v1.ListDocumentsResponse"\xae\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x9e\x01\x12E/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZU\x12S/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents\x12\xcd\x02\n\x0eCreateDocument\x126.google.cloud.discoveryengine.v1.CreateDocumentRequest\x1a).google.cloud.discoveryengine.v1.Document"\xd7\x01\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xb2\x01"E/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZ_"S/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document\x12\xd8\x02\n\x0eUpdateDocument\x126.google.cloud.discoveryengine.v1.UpdateDocumentRequest\x1a).google.cloud.discoveryengine.v1.Document"\xe2\x01\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xc4\x012N/v1/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZh2\\/v1/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document\x12\x8f\x02\n\x0eDeleteDocument\x126.google.cloud.discoveryengine.v1.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"\xac\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x9e\x01*E/v1/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZU*S/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\x9a\x03\n\x0fImportDocuments\x127.google.cloud.discoveryengine.v1.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xae\x02\xcaAr\n7google.cloud.discoveryengine.v1.ImportDocumentsResponse\x127google.cloud.discoveryengine.v1.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xb2\x01"L/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Z_"Z/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*\x12\x94\x03\n\x0ePurgeDocuments\x126.google.cloud.discoveryengine.v1.PurgeDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xaa\x02\xcaAp\n6google.cloud.discoveryengine.v1.PurgeDocumentsResponse\x126google.cloud.discoveryengine.v1.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xb0\x01"K/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Z^"Y/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*\x12\xf3\x02\n\x19BatchGetDocumentsMetadata\x12A.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataRequest\x1aB.google.cloud.discoveryengine.v1.BatchGetDocumentsMetadataResponse"\xce\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xbe\x01\x12U/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZe\x12c/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x87\x02\n#com.google.cloud.discoveryengine.v1B\x14DocumentServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B\x14DocumentServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document_id']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER'].fields_by_name['fhir_resources']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER'].fields_by_name['fhir_resources']._serialized_options = b'\xe0A\x02\xfaA(\n&healthcare.googleapis.com/FhirResource'
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['matcher']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['matcher']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE'].fields_by_name['fhir_resource']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE'].fields_by_name['fhir_resource']._serialized_options = b'\xfaA(\n&healthcare.googleapis.com/FhirResource'
    _globals['_DOCUMENTSERVICE']._loaded_options = None
    _globals['_DOCUMENTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9e\x01\x12E/v1/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZU\x12S/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x9e\x01\x12E/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZU\x12S/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents'
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._serialized_options = b'\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xb2\x01"E/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZ_"S/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xc4\x012N/v1/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZh2\\/v1/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x9e\x01*E/v1/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZU*S/v1/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaAr\n7google.cloud.discoveryengine.v1.ImportDocumentsResponse\x127google.cloud.discoveryengine.v1.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xb2\x01"L/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Z_"Z/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._serialized_options = b'\xcaAp\n6google.cloud.discoveryengine.v1.PurgeDocumentsResponse\x126google.cloud.discoveryengine.v1.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xb0\x01"K/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Z^"Y/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xbe\x01\x12U/v1/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZe\x12c/v1/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata'
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 492
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 575
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 577
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 701
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 703
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 813
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 816
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 994
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 997
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1158
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1160
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1246
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_start = 1249
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_end = 1788
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_start = 1445
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_end = 1472
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER']._serialized_start = 1474
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER']._serialized_end = 1559
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_start = 1562
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_end = 1788
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_start = 1791
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_end = 2463
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_start = 1942
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_end = 2376
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_start = 2260
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_end = 2376
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_start = 2378
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_end = 2463
    _globals['_DOCUMENTSERVICE']._serialized_start = 2466
    _globals['_DOCUMENTSERVICE']._serialized_end = 5311