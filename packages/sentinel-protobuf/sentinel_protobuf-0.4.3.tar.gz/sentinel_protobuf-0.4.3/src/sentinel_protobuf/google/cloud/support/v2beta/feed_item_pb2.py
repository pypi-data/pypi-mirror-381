"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/support/v2beta/feed_item.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.support.v2beta import attachment_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_attachment__pb2
from .....google.cloud.support.v2beta import comment_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_comment__pb2
from .....google.cloud.support.v2beta import email_message_pb2 as google_dot_cloud_dot_support_dot_v2beta_dot_email__message__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/support/v2beta/feed_item.proto\x12\x1bgoogle.cloud.support.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a,google/cloud/support/v2beta/attachment.proto\x1a)google/cloud/support/v2beta/comment.proto\x1a/google/cloud/support/v2beta/email_message.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xe6\x02\n\x08FeedItem\x12<\n\x07comment\x18d \x01(\x0b2$.google.cloud.support.v2beta.CommentB\x03\xe0A\x03H\x00\x12B\n\nattachment\x18e \x01(\x0b2\'.google.cloud.support.v2beta.AttachmentB\x03\xe0A\x03H\x00\x12G\n\remail_message\x18f \x01(\x0b2).google.cloud.support.v2beta.EmailMessageB\x03\xe0A\x03H\x00\x12J\n\x12deleted_attachment\x18g \x01(\x0b2\'.google.cloud.support.v2beta.AttachmentB\x03\xe0A\x03H\x00\x123\n\nevent_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x0e\n\x0cevent_objectB\xca\x01\n\x1fcom.google.cloud.support.v2betaB\rFeedItemProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.support.v2beta.feed_item_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.support.v2betaB\rFeedItemProtoP\x01Z9cloud.google.com/go/support/apiv2beta/supportpb;supportpb\xaa\x02\x1bGoogle.Cloud.Support.V2Beta\xca\x02\x1bGoogle\\Cloud\\Support\\V2beta\xea\x02\x1eGoogle::Cloud::Support::V2beta'
    _globals['_FEEDITEM'].fields_by_name['comment']._loaded_options = None
    _globals['_FEEDITEM'].fields_by_name['comment']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEM'].fields_by_name['attachment']._loaded_options = None
    _globals['_FEEDITEM'].fields_by_name['attachment']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEM'].fields_by_name['email_message']._loaded_options = None
    _globals['_FEEDITEM'].fields_by_name['email_message']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEM'].fields_by_name['deleted_attachment']._loaded_options = None
    _globals['_FEEDITEM'].fields_by_name['deleted_attachment']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEM'].fields_by_name['event_time']._loaded_options = None
    _globals['_FEEDITEM'].fields_by_name['event_time']._serialized_options = b'\xe0A\x03'
    _globals['_FEEDITEM']._serialized_start = 281
    _globals['_FEEDITEM']._serialized_end = 639