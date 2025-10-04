"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/document_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_document__pb2
from .....google.cloud.discoveryengine.v1beta import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1beta import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/discoveryengine/v1beta/document_service.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a2google/cloud/discoveryengine/v1beta/document.proto\x1a7google/cloud/discoveryengine/v1beta/import_config.proto\x1a6google/cloud/discoveryengine/v1beta/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"S\n\x12GetDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"|\n\x14ListDocumentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"r\n\x15ListDocumentsResponse\x12@\n\tdocuments\x18\x01 \x03(\x0b2-.google.cloud.discoveryengine.v1beta.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb6\x01\n\x15CreateDocumentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12D\n\x08document\x18\x02 \x01(\x0b2-.google.cloud.discoveryengine.v1beta.DocumentB\x03\xe0A\x02\x12\x18\n\x0bdocument_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa5\x01\n\x15UpdateDocumentRequest\x12D\n\x08document\x18\x01 \x01(\x0b2-.google.cloud.discoveryengine.v1beta.DocumentB\x03\xe0A\x02\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"V\n\x15DeleteDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"\xa7\x04\n BatchGetDocumentsMetadataRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12c\n\x07matcher\x18\x02 \x01(\x0b2M.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataRequest.MatcherB\x03\xe0A\x02\x1a\x1b\n\x0bUrisMatcher\x12\x0c\n\x04uris\x18\x01 \x03(\t\x1aU\n\x0bFhirMatcher\x12F\n\x0efhir_resources\x18\x01 \x03(\tB.\xe0A\x02\xfaA(\n&healthcare.googleapis.com/FhirResource\x1a\xea\x01\n\x07Matcher\x12i\n\x0curis_matcher\x18\x01 \x01(\x0b2Q.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataRequest.UrisMatcherH\x00\x12i\n\x0cfhir_matcher\x18\x02 \x01(\x0b2Q.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataRequest.FhirMatcherH\x00B\t\n\x07matcher"\xac\x05\n!BatchGetDocumentsMetadataResponse\x12s\n\x12documents_metadata\x18\x01 \x03(\x0b2W.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataResponse.DocumentMetadata\x1a\xba\x03\n\x10DocumentMetadata\x12{\n\rmatcher_value\x18\x02 \x01(\x0b2d.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue\x12[\n\x05state\x18\x03 \x01(\x0e2L.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataResponse.State\x127\n\x13last_refreshed_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x1d\n\x15data_ingestion_source\x18\x05 \x01(\t\x1at\n\x0cMatcherValue\x12\r\n\x03uri\x18\x01 \x01(\tH\x00\x12D\n\rfhir_resource\x18\x02 \x01(\tB+\xfaA(\n&healthcare.googleapis.com/FhirResourceH\x00B\x0f\n\rmatcher_value"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INDEXED\x10\x01\x12\x16\n\x12NOT_IN_TARGET_SITE\x10\x02\x12\x10\n\x0cNOT_IN_INDEX\x10\x032\xa1\x17\n\x0fDocumentService\x12\xac\x02\n\x0bGetDocument\x127.google.cloud.discoveryengine.v1beta.GetDocumentRequest\x1a-.google.cloud.discoveryengine.v1beta.Document"\xb4\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa6\x01\x12I/v1beta/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZY\x12W/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\xbf\x02\n\rListDocuments\x129.google.cloud.discoveryengine.v1beta.ListDocumentsRequest\x1a:.google.cloud.discoveryengine.v1beta.ListDocumentsResponse"\xb6\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa6\x01\x12I/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZY\x12W/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents\x12\xdd\x02\n\x0eCreateDocument\x12:.google.cloud.discoveryengine.v1beta.CreateDocumentRequest\x1a-.google.cloud.discoveryengine.v1beta.Document"\xdf\x01\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xba\x01"I/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZc"W/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document\x12\xe8\x02\n\x0eUpdateDocument\x12:.google.cloud.discoveryengine.v1beta.UpdateDocumentRequest\x1a-.google.cloud.discoveryengine.v1beta.Document"\xea\x01\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xcc\x012R/v1beta/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZl2`/v1beta/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document\x12\x9b\x02\n\x0eDeleteDocument\x12:.google.cloud.discoveryengine.v1beta.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"\xb4\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa6\x01*I/v1beta/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZY*W/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\xae\x03\n\x0fImportDocuments\x12;.google.cloud.discoveryengine.v1beta.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xbe\x02\xcaAz\n;google.cloud.discoveryengine.v1beta.ImportDocumentsResponse\x12;google.cloud.discoveryengine.v1beta.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xba\x01"P/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Zc"^/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*\x12\xa8\x03\n\x0ePurgeDocuments\x12:.google.cloud.discoveryengine.v1beta.PurgeDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xba\x02\xcaAx\n:google.cloud.discoveryengine.v1beta.PurgeDocumentsResponse\x12:google.cloud.discoveryengine.v1beta.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xb8\x01"O/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Zb"]/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*\x12\x83\x03\n\x19BatchGetDocumentsMetadata\x12E.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataRequest\x1aF.google.cloud.discoveryengine.v1beta.BatchGetDocumentsMetadataResponse"\xd6\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc6\x01\x12Y/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZi\x12g/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9b\x02\n\'com.google.cloud.discoveryengine.v1betaB\x14DocumentServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x14DocumentServiceProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
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
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa6\x01\x12I/v1beta/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZY\x12W/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa6\x01\x12I/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZY\x12W/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents'
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._serialized_options = b'\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xba\x01"I/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZc"W/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xcc\x012R/v1beta/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZl2`/v1beta/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa6\x01*I/v1beta/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZY*W/v1beta/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaAz\n;google.cloud.discoveryengine.v1beta.ImportDocumentsResponse\x12;google.cloud.discoveryengine.v1beta.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xba\x01"P/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Zc"^/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._serialized_options = b'\xcaAx\n:google.cloud.discoveryengine.v1beta.PurgeDocumentsResponse\x12:google.cloud.discoveryengine.v1beta.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xb8\x01"O/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Zb"]/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc6\x01\x12Y/v1beta/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZi\x12g/v1beta/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata'
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 512
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 595
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 597
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 721
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 723
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 837
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 840
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1022
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 1025
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1190
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1192
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1278
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_start = 1281
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_end = 1832
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_start = 1481
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_end = 1508
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER']._serialized_start = 1510
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_FHIRMATCHER']._serialized_end = 1595
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_start = 1598
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_end = 1832
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_start = 1835
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_end = 2519
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_start = 1990
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_end = 2432
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_start = 2316
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_end = 2432
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_start = 2434
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_end = 2519
    _globals['_DOCUMENTSERVICE']._serialized_start = 2522
    _globals['_DOCUMENTSERVICE']._serialized_end = 5499