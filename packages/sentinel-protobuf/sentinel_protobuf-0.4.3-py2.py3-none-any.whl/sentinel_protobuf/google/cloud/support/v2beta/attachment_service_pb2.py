"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/attachment_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import attachment_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_attachment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/cloud/support/v2beta/attachment_service.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/support/v2beta/attachment.proto"y\n\x16ListAttachmentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"T\n\x14GetAttachmentRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&cloudsupport.googleapis.com/Attachment"p\n\x17ListAttachmentsResponse\x12<\n\x0battachments\x18\x01 \x03(\x0b2\'.google.cloud.support.v2beta.Attachment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\x88\x04\n\x15CaseAttachmentService\x12\xf6\x01\n\x0fListAttachments\x123.google.cloud.support.v2beta.ListAttachmentsRequest\x1a4.google.cloud.support.v2beta.ListAttachmentsResponse"x\xdaA\x06parent\x82\xd3\xe4\x93\x02i\x12//v2beta/{parent=projects/*/cases/*}/attachmentsZ6\x124/v2beta/{parent=organizations/*/cases/*}/attachments\x12\xa4\x01\n\rGetAttachment\x121.google.cloud.support.v2beta.GetAttachmentRequest\x1a\'.google.cloud.support.v2beta.Attachment"7\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2beta/{name=*/*/cases/*/attachments/*}\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd3\x01\n\x1fcom.google.cloud.support.v2betaB\x16AttachmentServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.attachment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x16AttachmentServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTATTACHMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETATTACHMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&cloudsupport.googleapis.com/Attachment'
    _globals['_CASEATTACHMENTSERVICE']._loaded_options = None
    _globals['_CASEATTACHMENTSERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['ListAttachments']._loaded_options = None
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['ListAttachments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02i\x12//v2beta/{parent=projects/*/cases/*}/attachmentsZ6\x124/v2beta/{parent=organizations/*/cases/*}/attachments'
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['GetAttachment']._loaded_options = None
    _globals['_CASEATTACHMENTSERVICE'].methods_by_name['GetAttachment']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02*\x12(/v2beta/{name=*/*/cases/*/attachments/*}'
    _globals['_LISTATTACHMENTSREQUEST']._serialized_start = 246
    _globals['_LISTATTACHMENTSREQUEST']._serialized_end = 367
    _globals['_GETATTACHMENTREQUEST']._serialized_start = 369
    _globals['_GETATTACHMENTREQUEST']._serialized_end = 453
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_start = 455
    _globals['_LISTATTACHMENTSRESPONSE']._serialized_end = 567
    _globals['_CASEATTACHMENTSERVICE']._serialized_start = 570
    _globals['_CASEATTACHMENTSERVICE']._serialized_end = 1090