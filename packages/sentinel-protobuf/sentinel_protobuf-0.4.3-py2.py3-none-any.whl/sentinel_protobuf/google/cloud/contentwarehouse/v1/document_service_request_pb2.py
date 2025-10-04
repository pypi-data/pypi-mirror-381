"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/document_service_request.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import common_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_common__pb2
from .....google.cloud.contentwarehouse.v1 import document_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_document__pb2
from .....google.cloud.contentwarehouse.v1 import filters_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_filters__pb2
from .....google.cloud.contentwarehouse.v1 import histogram_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_histogram__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n?google/cloud/contentwarehouse/v1/document_service_request.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/contentwarehouse/v1/common.proto\x1a/google/cloud/contentwarehouse/v1/document.proto\x1a.google/cloud/contentwarehouse/v1/filters.proto\x1a0google/cloud/contentwarehouse/v1/histogram.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a google/protobuf/field_mask.proto"\xa7\x02\n\x15CloudAIDocumentOption\x12#\n\x1benable_entities_conversions\x18\x01 \x01(\x08\x12\x98\x01\n*customized_entities_properties_conversions\x18\x02 \x03(\x0b2d.google.cloud.contentwarehouse.v1.CloudAIDocumentOption.CustomizedEntitiesPropertiesConversionsEntry\x1aN\n,CustomizedEntitiesPropertiesConversionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\x9c\x03\n\x15CreateDocumentRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12A\n\x08document\x18\x02 \x01(\x0b2*.google.cloud.contentwarehouse.v1.DocumentB\x03\xe0A\x02\x12K\n\x10request_metadata\x18\x03 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata\x12%\n\x06policy\x18\x04 \x01(\x0b2\x15.google.iam.v1.Policy\x12Y\n\x18cloud_ai_document_option\x18\x05 \x01(\x0b27.google.cloud.contentwarehouse.v1.CloudAIDocumentOption\x12/\n\x0bcreate_mask\x18\x06 \x01(\x0b2\x1a.google.protobuf.FieldMask"\xa1\x01\n\x12GetDocumentRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata"\x8b\x03\n\x15UpdateDocumentRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12A\n\x08document\x18\x02 \x01(\x0b2*.google.cloud.contentwarehouse.v1.DocumentB\x03\xe0A\x02\x12K\n\x10request_metadata\x18\x03 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata\x12Y\n\x18cloud_ai_document_option\x18\x05 \x01(\x0b27.google.cloud.contentwarehouse.v1.CloudAIDocumentOption\x12G\n\x0eupdate_options\x18\x06 \x01(\x0b2/.google.cloud.contentwarehouse.v1.UpdateOptions"\xa4\x01\n\x15DeleteDocumentRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata"\xf9\x04\n\x16SearchDocumentsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location\x12K\n\x10request_metadata\x18\x03 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata\x12G\n\x0edocument_query\x18\x04 \x01(\x0b2/.google.cloud.contentwarehouse.v1.DocumentQuery\x12\x0e\n\x06offset\x18\x05 \x01(\x05\x12\x11\n\tpage_size\x18\x06 \x01(\x05\x12\x12\n\npage_token\x18\x07 \x01(\t\x12\x10\n\x08order_by\x18\x08 \x01(\t\x12K\n\x11histogram_queries\x18\t \x03(\x0b20.google.cloud.contentwarehouse.v1.HistogramQuery\x12\x1a\n\x12require_total_size\x18\n \x01(\x08\x12c\n\x11total_result_size\x18\x0c \x01(\x0e2H.google.cloud.contentwarehouse.v1.SearchDocumentsRequest.TotalResultSize\x12\x15\n\rqa_size_limit\x18\x0b \x01(\x05"Y\n\x0fTotalResultSize\x12!\n\x1dTOTAL_RESULT_SIZE_UNSPECIFIED\x10\x00\x12\x12\n\x0eESTIMATED_SIZE\x10\x01\x12\x0f\n\x0bACTUAL_SIZE\x10\x02"\xae\x01\n\x13LockDocumentRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12\x15\n\rcollection_id\x18\x02 \x01(\t\x12@\n\x0clocking_user\x18\x03 \x01(\x0b2*.google.cloud.contentwarehouse.v1.UserInfo"\x8c\x01\n\x0fFetchAclRequest\x12\x15\n\x08resource\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata\x12\x15\n\rproject_owner\x18\x03 \x01(\x08"\xb6\x01\n\rSetAclRequest\x12\x15\n\x08resource\x18\x01 \x01(\tB\x03\xe0A\x02\x12*\n\x06policy\x18\x02 \x01(\x0b2\x15.google.iam.v1.PolicyB\x03\xe0A\x02\x12K\n\x10request_metadata\x18\x03 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata\x12\x15\n\rproject_owner\x18\x04 \x01(\x08B\x83\x02\n$com.google.cloud.contentwarehouse.v1B\x1bDocumentServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_service_request_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x1bDocumentServiceRequestProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_CLOUDAIDOCUMENTOPTION_CUSTOMIZEDENTITIESPROPERTIESCONVERSIONSENTRY']._loaded_options = None
    _globals['_CLOUDAIDOCUMENTOPTION_CUSTOMIZEDENTITIESPROPERTIESCONVERSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_CREATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._loaded_options = None
    _globals['_UPDATEDOCUMENTREQUEST'].fields_by_name['document']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_SEARCHDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_SEARCHDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Location'
    _globals['_LOCKDOCUMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LOCKDOCUMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_FETCHACLREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_FETCHACLREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_SETACLREQUEST'].fields_by_name['resource']._loaded_options = None
    _globals['_SETACLREQUEST'].fields_by_name['resource']._serialized_options = b'\xe0A\x02'
    _globals['_SETACLREQUEST'].fields_by_name['policy']._loaded_options = None
    _globals['_SETACLREQUEST'].fields_by_name['policy']._serialized_options = b'\xe0A\x02'
    _globals['_CLOUDAIDOCUMENTOPTION']._serialized_start = 418
    _globals['_CLOUDAIDOCUMENTOPTION']._serialized_end = 713
    _globals['_CLOUDAIDOCUMENTOPTION_CUSTOMIZEDENTITIESPROPERTIESCONVERSIONSENTRY']._serialized_start = 635
    _globals['_CLOUDAIDOCUMENTOPTION_CUSTOMIZEDENTITIESPROPERTIESCONVERSIONSENTRY']._serialized_end = 713
    _globals['_CREATEDOCUMENTREQUEST']._serialized_start = 716
    _globals['_CREATEDOCUMENTREQUEST']._serialized_end = 1128
    _globals['_GETDOCUMENTREQUEST']._serialized_start = 1131
    _globals['_GETDOCUMENTREQUEST']._serialized_end = 1292
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_start = 1295
    _globals['_UPDATEDOCUMENTREQUEST']._serialized_end = 1690
    _globals['_DELETEDOCUMENTREQUEST']._serialized_start = 1693
    _globals['_DELETEDOCUMENTREQUEST']._serialized_end = 1857
    _globals['_SEARCHDOCUMENTSREQUEST']._serialized_start = 1860
    _globals['_SEARCHDOCUMENTSREQUEST']._serialized_end = 2493
    _globals['_SEARCHDOCUMENTSREQUEST_TOTALRESULTSIZE']._serialized_start = 2404
    _globals['_SEARCHDOCUMENTSREQUEST_TOTALRESULTSIZE']._serialized_end = 2493
    _globals['_LOCKDOCUMENTREQUEST']._serialized_start = 2496
    _globals['_LOCKDOCUMENTREQUEST']._serialized_end = 2670
    _globals['_FETCHACLREQUEST']._serialized_start = 2673
    _globals['_FETCHACLREQUEST']._serialized_end = 2813
    _globals['_SETACLREQUEST']._serialized_start = 2816
    _globals['_SETACLREQUEST']._serialized_end = 2998