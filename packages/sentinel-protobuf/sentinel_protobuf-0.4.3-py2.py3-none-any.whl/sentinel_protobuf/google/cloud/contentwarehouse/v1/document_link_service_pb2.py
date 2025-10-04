"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/contentwarehouse/v1/document_link_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.contentwarehouse.v1 import common_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_common__pb2
from .....google.cloud.contentwarehouse.v1 import document_pb2 as google_dot_cloud_dot_contentwarehouse_dot_v1_dot_document__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/cloud/contentwarehouse/v1/document_link_service.proto\x12 google.cloud.contentwarehouse.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/contentwarehouse/v1/common.proto\x1a/google/cloud/contentwarehouse/v1/document.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto"|\n\x19ListLinkedTargetsResponse\x12F\n\x0edocument_links\x18\x01 \x03(\x0b2..google.cloud.contentwarehouse.v1.DocumentLink\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xa9\x01\n\x18ListLinkedTargetsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata"|\n\x19ListLinkedSourcesResponse\x12F\n\x0edocument_links\x18\x01 \x03(\x0b2..google.cloud.contentwarehouse.v1.DocumentLink\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd0\x01\n\x18ListLinkedSourcesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata"\xe1\x04\n\x0cDocumentLink\x12\x0c\n\x04name\x18\x01 \x01(\t\x12V\n\x19source_document_reference\x18\x02 \x01(\x0b23.google.cloud.contentwarehouse.v1.DocumentReference\x12V\n\x19target_document_reference\x18\x03 \x01(\x0b23.google.cloud.contentwarehouse.v1.DocumentReference\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x124\n\x0bupdate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x05state\x18\x07 \x01(\x0e24.google.cloud.contentwarehouse.v1.DocumentLink.State"<\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06ACTIVE\x10\x01\x12\x10\n\x0cSOFT_DELETED\x10\x02:\x8e\x01\xeaA\x8a\x01\n,contentwarehouse.googleapis.com/DocumentLink\x12Zprojects/{project}/locations/{location}/documents/{document}/documentLinks/{document_link}"\xf6\x01\n\x19CreateDocumentLinkRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document\x12J\n\rdocument_link\x18\x02 \x01(\x0b2..google.cloud.contentwarehouse.v1.DocumentLinkB\x03\xe0A\x02\x12K\n\x10request_metadata\x18\x03 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata"\xac\x01\n\x19DeleteDocumentLinkRequest\x12B\n\x04name\x18\x01 \x01(\tB4\xe0A\x02\xfaA.\n,contentwarehouse.googleapis.com/DocumentLink\x12K\n\x10request_metadata\x18\x02 \x01(\x0b21.google.cloud.contentwarehouse.v1.RequestMetadata2\xd7\x07\n\x13DocumentLinkService\x12\xdf\x01\n\x11ListLinkedTargets\x12:.google.cloud.contentwarehouse.v1.ListLinkedTargetsRequest\x1a;.google.cloud.contentwarehouse.v1.ListLinkedTargetsResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/linkedTargets:\x01*\x12\xdf\x01\n\x11ListLinkedSources\x12:.google.cloud.contentwarehouse.v1.ListLinkedSourcesRequest\x1a;.google.cloud.contentwarehouse.v1.ListLinkedSourcesResponse"Q\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/linkedSources:\x01*\x12\xe2\x01\n\x12CreateDocumentLink\x12;.google.cloud.contentwarehouse.v1.CreateDocumentLinkRequest\x1a..google.cloud.contentwarehouse.v1.DocumentLink"_\xdaA\x14parent,document_link\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/documentLinks:\x01*\x12\xc1\x01\n\x12DeleteDocumentLink\x12;.google.cloud.contentwarehouse.v1.DeleteDocumentLinkRequest\x1a\x16.google.protobuf.Empty"V\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1/{name=projects/*/locations/*/documents/*/documentLinks/*}:delete:\x01*\x1aS\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x80\x02\n$com.google.cloud.contentwarehouse.v1B\x18DocumentLinkServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.contentwarehouse.v1.document_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.contentwarehouse.v1B\x18DocumentLinkServiceProtoP\x01ZPcloud.google.com/go/contentwarehouse/apiv1/contentwarehousepb;contentwarehousepb\xaa\x02 Google.Cloud.ContentWarehouse.V1\xca\x02 Google\\Cloud\\ContentWarehouse\\V1\xea\x02#Google::Cloud::ContentWarehouse::V1'
    _globals['_LISTLINKEDTARGETSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLINKEDTARGETSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_LISTLINKEDSOURCESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTLINKEDSOURCESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_DOCUMENTLINK'].fields_by_name['update_time']._loaded_options = None
    _globals['_DOCUMENTLINK'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTLINK'].fields_by_name['create_time']._loaded_options = None
    _globals['_DOCUMENTLINK'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DOCUMENTLINK']._loaded_options = None
    _globals['_DOCUMENTLINK']._serialized_options = b'\xeaA\x8a\x01\n,contentwarehouse.googleapis.com/DocumentLink\x12Zprojects/{project}/locations/{location}/documents/{document}/documentLinks/{document_link}'
    _globals['_CREATEDOCUMENTLINKREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEDOCUMENTLINKREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(contentwarehouse.googleapis.com/Document'
    _globals['_CREATEDOCUMENTLINKREQUEST'].fields_by_name['document_link']._loaded_options = None
    _globals['_CREATEDOCUMENTLINKREQUEST'].fields_by_name['document_link']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDOCUMENTLINKREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEDOCUMENTLINKREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA.\n,contentwarehouse.googleapis.com/DocumentLink'
    _globals['_DOCUMENTLINKSERVICE']._loaded_options = None
    _globals['_DOCUMENTLINKSERVICE']._serialized_options = b'\xcaA\x1fcontentwarehouse.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['ListLinkedTargets']._loaded_options = None
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['ListLinkedTargets']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/linkedTargets:\x01*'
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['ListLinkedSources']._loaded_options = None
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['ListLinkedSources']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/linkedSources:\x01*'
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['CreateDocumentLink']._loaded_options = None
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['CreateDocumentLink']._serialized_options = b'\xdaA\x14parent,document_link\x82\xd3\xe4\x93\x02B"=/v1/{parent=projects/*/locations/*/documents/*}/documentLinks:\x01*'
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['DeleteDocumentLink']._loaded_options = None
    _globals['_DOCUMENTLINKSERVICE'].methods_by_name['DeleteDocumentLink']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02I"D/v1/{name=projects/*/locations/*/documents/*/documentLinks/*}:delete:\x01*'
    _globals['_LISTLINKEDTARGETSRESPONSE']._serialized_start = 371
    _globals['_LISTLINKEDTARGETSRESPONSE']._serialized_end = 495
    _globals['_LISTLINKEDTARGETSREQUEST']._serialized_start = 498
    _globals['_LISTLINKEDTARGETSREQUEST']._serialized_end = 667
    _globals['_LISTLINKEDSOURCESRESPONSE']._serialized_start = 669
    _globals['_LISTLINKEDSOURCESRESPONSE']._serialized_end = 793
    _globals['_LISTLINKEDSOURCESREQUEST']._serialized_start = 796
    _globals['_LISTLINKEDSOURCESREQUEST']._serialized_end = 1004
    _globals['_DOCUMENTLINK']._serialized_start = 1007
    _globals['_DOCUMENTLINK']._serialized_end = 1616
    _globals['_DOCUMENTLINK_STATE']._serialized_start = 1411
    _globals['_DOCUMENTLINK_STATE']._serialized_end = 1471
    _globals['_CREATEDOCUMENTLINKREQUEST']._serialized_start = 1619
    _globals['_CREATEDOCUMENTLINKREQUEST']._serialized_end = 1865
    _globals['_DELETEDOCUMENTLINKREQUEST']._serialized_start = 1868
    _globals['_DELETEDOCUMENTLINKREQUEST']._serialized_end = 2040
    _globals['_DOCUMENTLINKSERVICE']._serialized_start = 2043
    _globals['_DOCUMENTLINKSERVICE']._serialized_end = 3026