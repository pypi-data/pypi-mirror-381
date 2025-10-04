"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/comment_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.support.v2beta import comment_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_comment__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/cloud/support/v2beta/comment_service.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a)google/cloud/support/v2beta/comment.proto"v\n\x13ListCommentsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12\x11\n\tpage_size\x18\x04 \x01(\x05\x12\x12\n\npage_token\x18\x05 \x01(\t"g\n\x14ListCommentsResponse\x126\n\x08comments\x18\x01 \x03(\x0b2$.google.cloud.support.v2beta.Comment\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8c\x01\n\x14CreateCommentRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case\x12:\n\x07comment\x18\x02 \x01(\x0b2$.google.cloud.support.v2beta.CommentB\x03\xe0A\x02"N\n\x11GetCommentRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#cloudsupport.googleapis.com/Comment2\xe0\x05\n\x0eCommentService\x12\xe7\x01\n\x0cListComments\x120.google.cloud.support.v2beta.ListCommentsRequest\x1a1.google.cloud.support.v2beta.ListCommentsResponse"r\xdaA\x06parent\x82\xd3\xe4\x93\x02c\x12,/v2beta/{parent=projects/*/cases/*}/commentsZ3\x121/v2beta/{parent=organizations/*/cases/*}/comments\x12\xf7\x01\n\rCreateComment\x121.google.cloud.support.v2beta.CreateCommentRequest\x1a$.google.cloud.support.v2beta.Comment"\x8c\x01\xdaA\x0eparent,comment\x82\xd3\xe4\x93\x02u",/v2beta/{parent=projects/*/cases/*}/comments:\x07commentZ<"1/v2beta/{parent=organizations/*/cases/*}/comments:\x07comment\x12\x98\x01\n\nGetComment\x12..google.cloud.support.v2beta.GetCommentRequest\x1a$.google.cloud.support.v2beta.Comment"4\xdaA\x04name\x82\xd3\xe4\x93\x02\'\x12%/v2beta/{name=*/*/cases/*/comments/*}\x1aO\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd0\x01\n\x1fcom.google.cloud.support.v2betaB\x13CommentServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.comment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\x13CommentServiceProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_LISTCOMMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCOMMENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n cloudsupport.googleapis.com/Case'
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['comment']._loaded_options = None
    _globals['_CREATECOMMENTREQUEST'].fields_by_name['comment']._serialized_options = b'\xe0A\x02'
    _globals['_GETCOMMENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCOMMENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#cloudsupport.googleapis.com/Comment'
    _globals['_COMMENTSERVICE']._loaded_options = None
    _globals['_COMMENTSERVICE']._serialized_options = b'\xcaA\x1bcloudsupport.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_COMMENTSERVICE'].methods_by_name['ListComments']._loaded_options = None
    _globals['_COMMENTSERVICE'].methods_by_name['ListComments']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02c\x12,/v2beta/{parent=projects/*/cases/*}/commentsZ3\x121/v2beta/{parent=organizations/*/cases/*}/comments'
    _globals['_COMMENTSERVICE'].methods_by_name['CreateComment']._loaded_options = None
    _globals['_COMMENTSERVICE'].methods_by_name['CreateComment']._serialized_options = b'\xdaA\x0eparent,comment\x82\xd3\xe4\x93\x02u",/v2beta/{parent=projects/*/cases/*}/comments:\x07commentZ<"1/v2beta/{parent=organizations/*/cases/*}/comments:\x07comment'
    _globals['_COMMENTSERVICE'].methods_by_name['GetComment']._loaded_options = None
    _globals['_COMMENTSERVICE'].methods_by_name['GetComment']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02'\x12%/v2beta/{name=*/*/cases/*/comments/*}"
    _globals['_LISTCOMMENTSREQUEST']._serialized_start = 240
    _globals['_LISTCOMMENTSREQUEST']._serialized_end = 358
    _globals['_LISTCOMMENTSRESPONSE']._serialized_start = 360
    _globals['_LISTCOMMENTSRESPONSE']._serialized_end = 463
    _globals['_CREATECOMMENTREQUEST']._serialized_start = 466
    _globals['_CREATECOMMENTREQUEST']._serialized_end = 606
    _globals['_GETCOMMENTREQUEST']._serialized_start = 608
    _globals['_GETCOMMENTREQUEST']._serialized_end = 686
    _globals['_COMMENTSERVICE']._serialized_start = 689
    _globals['_COMMENTSERVICE']._serialized_end = 1425