"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/document_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import common_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_common__pb2
from .....google.cloud.contentwarehouse.v1 import document_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_document__pb2
from .....google.cloud.contentwarehouse.v1 import document_service_request_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_document__service__request__pb2
from .....google.cloud.contentwarehouse.v1 import histogram_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_histogram__pb2
from .....google.cloud.contentwarehouse.v1 import rule_engine_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_rule__engine__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/contentwarehouse/v1/document_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/contentwarehouse/v1/common.proto\x1a/google/cloud/contentwarehouse/v1/document.proto\x1a?google/cloud/contentwarehouse/v1/document_service_request.proto\x1a0google/cloud/contentwarehouse/v1/histogram.proto\x1a2google/cloud/contentwarehouse/v1/rule_engine.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto"\xac\x02\n\x16CreateDocumentResponse\x12<\n\x08document\x18\x01 \x01(\x0b2*.google.cloud.contentwarehouse.v1.Document\x12N\n\x12rule_engine_output\x18\x02 \x01(\x0b22.google.cloud.contentwarehouse.v1.RuleEngineOutput\x12D\n\x08metadata\x18\x03 \x01(\x0b22.google.cloud.contentwarehouse.v1.ResponseMetadata\x12>\n\x17long_running_operations\x18\x04 \x03(\x0b2\x1d.google.longrunning.Operation"\xec\x01\n\x16UpdateDocumentResponse\x12<\n\x08document\x18\x01 \x01(\x0b2*.google.cloud.contentwarehouse.v1.Document\x12N\n\x12rule_engine_output\x18\x02 \x01(\x0b22.google.cloud.contentwarehouse.v1.RuleEngineOutput\x12D\n\x08metadata\x18\x03 \x01(\x0b22.google.cloud.contentwarehouse.v1.ResponseMetadata"\xa3\x01\n\x08QAResult\x12H\n\nhighlights\x18\x01 \x03(\x0b24.google.cloud.contentwarehouse.v1.QAResult.Highlight\x12\x18\n\x10confidence_score\x18\x02 \x01(\x02\x1a3\n\tHighlight\x12\x13\n\x0bstart_index\x18\x01 \x01(\x05\x12\x11\n\tend_index\x18\x02 \x01(\x05"\xb9\x04\n\x17SearchDocumentsResponse\x12f\n\x12matching_documents\x18\x01 \x03(\x0b2J.google.cloud.contentwarehouse.v1.SearchDocumentsResponse.MatchingDocument\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05\x12D\n\x08metadata\x18\x04 \x01(\x0b22.google.cloud.contentwarehouse.v1.ResponseMetadata\x12W\n\x17histogram_query_results\x18\x06 \x03(\x0b26.google.cloud.contentwarehouse.v1.HistogramQueryResult\x12\x17\n\x0fquestion_answer\x18\x07 \x01(\t\x1a\xd0\x01\n\x10MatchingDocument\x12<\n\x08document\x18\x01 \x01(\x0b2*.google.cloud.contentwarehouse.v1.Document\x12\x1b\n\x13search_text_snippet\x18\x02 \x01(\t\x12=\n\tqa_result\x18\x03 \x01(\x0b2*.google.cloud.contentwarehouse.v1.QAResult\x12"\n\x1amatched_token_page_indices\x18\x04 \x03(\x03"\x7f\n\x10FetchAclResponse\x12%\n\x06policy\x18\x01 \x01(\x0b2\x15.google.iam.v1.Policy\x12D\n\x08metadata\x18\x02 \x01(\x0b22.google.cloud.contentwarehouse.v1.ResponseMetadata"}\n\x0eSetAclResponse\x12%\n\x06policy\x18\x01 \x01(\x0b2\x15.google.iam.v1.Policy\x12D\n\x08metadata\x18\x02 \x01(\x0b22.google.cloud.contentwarehouse.v1.ResponseMetadata2\xa2\x0f\n\x0fDocumentService\x12\xcf\x01\n\x0eCreateDocument\x127.google.cloud.contentwarehouse.v1.CreateDocumentRequest\x1a8.google.cloud.contentwarehouse.v1.CreateDocumentResponse"J\xdaA\x0fparent,document\x82\xd3\xe4\x93\x022"-/v1/{parent=projects/*/locations/*}/documents:\x01*\x12\xf9\x01\n\x0bGetDocument\x124.google.cloud.contentwarehouse.v1.GetDocumentRequest\x1a*.google.cloud.contentwarehouse.v1.Document"\x87\x01\xdaA\x04name\x82\xd3\xe4\x93\x02z"1/v1/{name=projects/*/locations/*/documents/*}:get:\x01*ZB"=/v1/{name=projects/*/locations/*/documents/referenceId/*}:get:\x01*\x12\x8e\x02\n\x0eUpdateDocument\x127.google.cloud.contentwarehouse.v1.UpdateDocumentRequest\x1a8.google.cloud.contentwarehouse.v1.UpdateDocumentResponse"\x88\x01\xdaA\rname,document\x82\xd3\xe4\x93\x02r2-/v1/{name=projects/*/locations/*/documents/*}:\x01*Z>29/v1/{name=projects/*/locations/*/documents/referenceId/*}:\x01*\x12\xf2\x01\n\x0eDeleteDocument\x127.google.cloud.contentwarehouse.v1.DeleteDocumentRequest\x1a\x16.google.protobuf.Empty"\x8e\x01\xdaA\x04name\x82\xd3\xe4\x93\x02\x80\x01"4/v1/{name=projects/*/locations/*/documents/*}:delete:\x01*ZE"@/v1/{name=projects/*/locations/*/documents/referenceId/*}:delete:\x01*\x12\xd0\x01\n\x0fSearchDocuments\x128.google.cloud.contentwarehouse.v1.SearchDocumentsRequest\x1a9.google.cloud.contentwarehouse.v1.SearchDocumentsResponse"H\xdaA\x06parent\x82\xd3\xe4\x93\x029"4/v1/{parent=projects/*/locations/*}/documents:search:\x01*\x12\xb7\x01\n\x0cLockDocument\x125.google.cloud.contentwarehouse.v1.LockDocumentRequest\x1a*.google.cloud.contentwarehouse.v1.Document"D\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/documents/*}:lock:\x01*\x12\xec\x01\n\x08FetchAcl\x121.google.cloud.contentwarehouse.v1.FetchAclRequest\x1a2.google.cloud.contentwarehouse.v1.FetchAclResponse"y\xdaA\x08resource\x82\xd3\xe4\x93\x02h":/v1/{resource=projects/*/locations/*/documents/*}:fetchAcl:\x01*Z\'""/v1/{resource=projects/*}:fetchAcl:\x01*\x12\xe9\x01\n\x06SetAcl\x12/.google.cloud.contentwarehouse.v1.SetAclRequest\x1a0.google.cloud.contentwarehouse.v1.SetAclResponse"|\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02d"8/v1/{resource=projects/*/locations/*/documents/*}:setAcl:\x01*Z%" /v1/{resource=projects/*}:setAcl:\x01*\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xfc\x01\n$com.google.cloud.contentwarehouse.v1B\x14DocumentServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x14DocumentServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_DOCUMENTSERVICE']._loaded_options = None
    _globals['_DOCUMENTSERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['CreateDocument']._serialized_options = b'\xdaA\x0fparent,document\x82\xd3\xe4\x93\x022"-/v1/{parent=projects/*/locations/*}/documents:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['GetDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02z"1/v1/{name=projects/*/locations/*/documents/*}:get:\x01*ZB"=/v1/{name=projects/*/locations/*/documents/referenceId/*}:get:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['UpdateDocument']._serialized_options = b'\xdaA\rname,document\x82\xd3\xe4\x93\x02r2-/v1/{name=projects/*/locations/*/documents/*}:\x01*Z>29/v1/{name=projects/*/locations/*/documents/referenceId/*}:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['DeleteDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x80\x01"4/v1/{name=projects/*/locations/*/documents/*}:delete:\x01*ZE"@/v1/{name=projects/*/locations/*/documents/referenceId/*}:delete:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['SearchDocuments']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['SearchDocuments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x029"4/v1/{parent=projects/*/locations/*}/documents:search:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['LockDocument']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['LockDocument']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027"2/v1/{name=projects/*/locations/*/documents/*}:lock:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['FetchAcl']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['FetchAcl']._serialized_options = b'\xdaA\x08resource\x82\xd3\xe4\x93\x02h":/v1/{resource=projects/*/locations/*/documents/*}:fetchAcl:\x01*Z\'""/v1/{resource=projects/*}:fetchAcl:\x01*'
    _globals['_DOCUMENTSERVICE'].methods_by_name['SetAcl']._loaded_options = None
    _globals['_DOCUMENTSERVICE'].methods_by_name['SetAcl']._serialized_options = b'\xdaA\x0fresource,policy\x82\xd3\xe4\x93\x02d"8/v1/{resource=projects/*/locations/*/documents/*}:setAcl:\x01*Z%" /v1/{resource=projects/*}:setAcl:\x01*'
    _globals['_CREATEDOCUMENTRESPONSE']._serialized_start = 533
    _globals['_CREATEDOCUMENTRESPONSE']._serialized_end = 833
    _globals['_UPDATEDOCUMENTRESPONSE']._serialized_start = 836
    _globals['_UPDATEDOCUMENTRESPONSE']._serialized_end = 1072
    _globals['_QARESULT']._serialized_start = 1075
    _globals['_QARESULT']._serialized_end = 1238
    _globals['_QARESULT_HIGHLIGHT']._serialized_start = 1187
    _globals['_QARESULT_HIGHLIGHT']._serialized_end = 1238
    _globals['_SEARCHDOCUMENTSRESPONSE']._serialized_start = 1241
    _globals['_SEARCHDOCUMENTSRESPONSE']._serialized_end = 1810
    _globals['_SEARCHDOCUMENTSRESPONSE_MATCHINGDOCUMENT']._serialized_start = 1602
    _globals['_SEARCHDOCUMENTSRESPONSE_MATCHINGDOCUMENT']._serialized_end = 1810
    _globals['_FETCHACLRESPONSE']._serialized_start = 1812
    _globals['_FETCHACLRESPONSE']._serialized_end = 1939
    _globals['_SETACLRESPONSE']._serialized_start = 1941
    _globals['_SETACLRESPONSE']._serialized_end = 2066
    _globals['_DOCUMENTSERVICE']._serialized_start = 2069
    _globals['_DOCUMENTSERVICE']._serialized_end = 4023