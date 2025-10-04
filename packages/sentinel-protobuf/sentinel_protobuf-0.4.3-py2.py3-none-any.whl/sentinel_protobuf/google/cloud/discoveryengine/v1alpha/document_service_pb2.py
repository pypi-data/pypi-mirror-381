"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1alpha/document_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1alpha import document_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_document__pb2
from .....google.cloud.discoveryengine.v1alpha import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_import__config__pb2
from .....google.cloud.discoveryengine.v1alpha import purge_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1alpha_dot_purge__config__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/cloud/discoveryengine/v1alpha/document_service.proto\x12$google.cloud.discoveryengine.v1alpha\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a3google/cloud/discoveryengine/v1alpha/document.proto\x1a8google/cloud/discoveryengine/v1alpha/import_config.proto\x1a7google/cloud/discoveryengine/v1alpha/purge_config.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"S\n\x12GetDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"|\n\x14ListDocumentsRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"s\n\x15ListDocumentsResponse\x12A\n\tdocuments\x18\x01 \x03(\x0b2..google.cloud.discoveryengine.v1alpha.Document\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xb7\x01\n\x15CreateDocumentRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12E\n\x08document\x18\x02 \x01(\x0b2..google.cloud.discoveryengine.v1alpha.DocumentB\x03\xe0A\x02\x12\x18\n\x0bdocument_id\x18\x03 \x01(\tB\x03\xe0A\x02"\xa6\x01\n\x15UpdateDocumentRequest\x12E\n\x08document\x18\x01 \x01(\x0b2..google.cloud.discoveryengine.v1alpha.DocumentB\x03\xe0A\x02\x12\x15\n\rallow_missing\x18\x02 \x01(\x08\x12/\n\x0bupdate_mask\x18\x03 \x01(\x0b2\x1a.google.protobuf.FieldMask"V\n\x15DeleteDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document"\xb3\x04\n\x1bGetProcessedDocumentRequest\x12=\n\x04name\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Document\x12}\n\x17processed_document_type\x18\x02 \x01(\x0e2W.google.cloud.discoveryengine.v1alpha.GetProcessedDocumentRequest.ProcessedDocumentTypeB\x03\xe0A\x02\x12|\n\x19processed_document_format\x18\x03 \x01(\x0e2Y.google.cloud.discoveryengine.v1alpha.GetProcessedDocumentRequest.ProcessedDocumentFormat"\x87\x01\n\x15ProcessedDocumentType\x12\'\n#PROCESSED_DOCUMENT_TYPE_UNSPECIFIED\x10\x00\x12\x13\n\x0fPARSED_DOCUMENT\x10\x01\x12\x14\n\x10CHUNKED_DOCUMENT\x10\x02\x12\x1a\n\x16PNG_CONVERTED_DOCUMENT\x10\x03"N\n\x17ProcessedDocumentFormat\x12)\n%PROCESSED_DOCUMENT_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04JSON\x10\x01"\xe7\x02\n BatchGetDocumentsMetadataRequest\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12d\n\x07matcher\x18\x02 \x01(\x0b2N.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataRequest.MatcherB\x03\xe0A\x02\x1a\x1b\n\x0bUrisMatcher\x12\x0c\n\x04uris\x18\x01 \x03(\t\x1a\x80\x01\n\x07Matcher\x12j\n\x0curis_matcher\x18\x01 \x01(\x0b2R.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataRequest.UrisMatcherH\x00B\t\n\x07matcher"\xca\x04\n!BatchGetDocumentsMetadataResponse\x12t\n\x12documents_metadata\x18\x01 \x03(\x0b2X.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataResponse.DocumentMetadata\x1a\xd7\x02\n\x10DocumentMetadata\x12|\n\rmatcher_value\x18\x02 \x01(\x0b2e.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataResponse.DocumentMetadata.MatcherValue\x12\\\n\x05state\x18\x03 \x01(\x0e2M.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataResponse.State\x127\n\x13last_refreshed_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a.\n\x0cMatcherValue\x12\r\n\x03uri\x18\x01 \x01(\tH\x00B\x0f\n\rmatcher_value"U\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07INDEXED\x10\x01\x12\x16\n\x12NOT_IN_TARGET_SITE\x10\x02\x12\x10\n\x0cNOT_IN_INDEX\x10\x032\xba\x1a\n\x0fDocumentService\x12\xb0\x02\n\x0bGetDocument\x128.google.cloud.discoveryengine.v1alpha.GetDocumentRequest\x1a..google.cloud.discoveryengine.v1alpha.Document"\xb6\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa8\x01\x12J/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZZ\x12X/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\xc3\x02\n\rListDocuments\x12:.google.cloud.discoveryengine.v1alpha.ListDocumentsRequest\x1a;.google.cloud.discoveryengine.v1alpha.ListDocumentsResponse"\xb8\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa8\x01\x12J/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZZ\x12X/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents\x12\xe1\x02\n\x0eCreateDocument\x12;.google.cloud.discoveryengine.v1alpha.CreateDocumentRequest\x1a..google.cloud.discoveryengine.v1alpha.Document"\xe1\x01\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xbc\x01"J/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZd"X/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document\x12\xec\x02\n\x0eUpdateDocument\x12;.google.cloud.discoveryengine.v1alpha.UpdateDocumentRequest\x1a..google.cloud.discoveryengine.v1alpha.Document"\xec\x01\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xce\x012S/v1alpha/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZm2a/v1alpha/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document\x12\x9e\x02\n\x0eDeleteDocument\x12;.google.cloud.discoveryengine.v1alpha.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"\xb6\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xa8\x01*J/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZZ*X/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}\x12\xb3\x03\n\x0fImportDocuments\x12<.google.cloud.discoveryengine.v1alpha.ImportDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xc2\x02\xcaA|\n<google.cloud.discoveryengine.v1alpha.ImportDocumentsResponse\x12<google.cloud.discoveryengine.v1alpha.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xbc\x01"Q/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Zd"_/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*\x12\xad\x03\n\x0ePurgeDocuments\x12;.google.cloud.discoveryengine.v1alpha.PurgeDocumentsRequest\x1a\x1d.google.longrunning.Operation"\xbe\x02\xcaAz\n;google.cloud.discoveryengine.v1alpha.PurgeDocumentsResponse\x12;google.cloud.discoveryengine.v1alpha.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xba\x01"P/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Zc"^/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*\x12\xf5\x02\n\x14GetProcessedDocument\x12A.google.cloud.discoveryengine.v1alpha.GetProcessedDocumentRequest\x1a7.google.cloud.discoveryengine.v1alpha.ProcessedDocument"\xe0\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\xd2\x01\x12_/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:getProcessedDocumentZo\x12m/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:getProcessedDocument\x12\x87\x03\n\x19BatchGetDocumentsMetadata\x12F.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataRequest\x1aG.google.cloud.discoveryengine.v1alpha.BatchGetDocumentsMetadataResponse"\xd8\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc8\x01\x12Z/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZj\x12h/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xa0\x02\n(com.google.cloud.discoveryengine.v1alphaB\x14DocumentServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02\'Google::Cloud::DiscoveryEngine::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1alpha.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n(com.google.cloud.discoveryengine.v1alphaB\x14DocumentServiceProtoP\x01ZRcloud.google.com/go/discoveryengine/apiv1alpha/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02$Google.Cloud.DiscoveryEngine.V1Alpha\xca\x02$Google\\Cloud\\DiscoveryEngine\\V1alpha\xea\x02'Google::Cloud::DiscoveryEngine::V1alpha"
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
    _globals['_GETPROCESSEDDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPROCESSEDDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_GETPROCESSEDDOCUMENTREQUEST'].fields_by_name['processed_document_type']._loaded_options = None
    _globals['_GETPROCESSEDDOCUMENTREQUEST'].fields_by_name['processed_document_type']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['matcher']._loaded_options = None
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST'].fields_by_name['matcher']._serialized_options = b'\xe0A\x02'
    _globals['_DOCUMENTSERVICE']._loaded_options = None
    _globals['_DOCUMENTSERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa8\x01\x12J/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZZ\x12X/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ListDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xa8\x01\x12J/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documentsZZ\x12X/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents'
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._serialized_options = b'\xdaA\x1bparent,document,document_id\x82\xd3\xe4\x93\x02\xbc\x01"J/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:\x08documentZd"X/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\x14document,update_mask\x82\xd3\xe4\x93\x02\xce\x012S/v1alpha/{document.name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:\x08documentZm2a/v1alpha/{document.name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:\x08document'
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xa8\x01*J/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}ZZ*X/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}'
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['ImportDocuments']._serialized_options = b'\xcaA|\n<google.cloud.discoveryengine.v1alpha.ImportDocumentsResponse\x12<google.cloud.discoveryengine.v1alpha.ImportDocumentsMetadata\x82\xd3\xe4\x93\x02\xbc\x01"Q/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:import:\x01*Zd"_/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:import:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['PurgeDocuments']._serialized_options = b'\xcaAz\n;google.cloud.discoveryengine.v1alpha.PurgeDocumentsResponse\x12;google.cloud.discoveryengine.v1alpha.PurgeDocumentsMetadata\x82\xd3\xe4\x93\x02\xba\x01"P/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/documents:purge:\x01*Zc"^/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/documents:purge:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetProcessedDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetProcessedDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\xd2\x01\x12_/v1alpha/{name=projects/*/locations/*/dataStores/*/branches/*/documents/*}:getProcessedDocumentZo\x12m/v1alpha/{name=projects/*/locations/*/collections/*/dataStores/*/branches/*/documents/*}:getProcessedDocument'
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['BatchGetDocumentsMetadata']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\xc8\x01\x12Z/v1alpha/{parent=projects/*/locations/*/dataStores/*/branches/*}/batchGetDocumentsMetadataZj\x12h/v1alpha/{parent=projects/*/locations/*/collections/*/dataStores/*/branches/*}/batchGetDocumentsMetadata'
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 517
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 600
    _globals['_LISTDOCUMENTSREQUEST']._serialized_start = 602
    _globals['_LISTDOCUMENTSREQUEST']._serialized_end = 726
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_start = 728
    _globals['_LISTDOCUMENTSRESPONSE']._serialized_end = 843
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 846
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1029
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 1032
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1198
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1200
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1286
    _globals['_GETPROCESSEDDOCUMENTREQUEST']._serialized_start = 1289
    _globals['_GETPROCESSEDDOCUMENTREQUEST']._serialized_end = 1852
    _globals['_GETPROCESSEDDOCUMENTREQUEST_PROCESSEDDOCUMENTTYPE']._serialized_start = 1637
    _globals['_GETPROCESSEDDOCUMENTREQUEST_PROCESSEDDOCUMENTTYPE']._serialized_end = 1772
    _globals['_GETPROCESSEDDOCUMENTREQUEST_PROCESSEDDOCUMENTFORMAT']._serialized_start = 1774
    _globals['_GETPROCESSEDDOCUMENTREQUEST_PROCESSEDDOCUMENTFORMAT']._serialized_end = 1852
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_start = 1855
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST']._serialized_end = 2214
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_start = 2056
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_URISMATCHER']._serialized_end = 2083
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_start = 2086
    _globals['_BATCHGETDOCUMENTSMETADATAREQUEST_MATCHER']._serialized_end = 2214
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_start = 2217
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE']._serialized_end = 2803
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_start = 2373
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA']._serialized_end = 2716
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_start = 2670
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_DOCUMENTMETADATA_MATCHERVALUE']._serialized_end = 2716
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_start = 2718
    _globals['_BATCHGETDOCUMENTSMETADATARESPONSE_STATE']._serialized_end = 2803
    _globals['_DOCUMENTSERVICE']._serialized_start = 2806
    _globals['_DOCUMENTSERVICE']._serialized_end = 6192