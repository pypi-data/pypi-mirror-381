from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.support.v2beta import attachment_pb2 as _attachment_pb2
from google.cloud.support.v2beta import comment_pb2 as _comment_pb2
from google.cloud.support.v2beta import email_message_pb2 as _email_message_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeedItem(_message.Message):
    __slots__ = ('comment', 'attachment', 'email_message', 'deleted_attachment', 'event_time')
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    EMAIL_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETED_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIME_FIELD_NUMBER: _ClassVar[int]
    comment: _comment_pb2.Comment
    attachment: _attachment_pb2.Attachment
    email_message: _email_message_pb2.EmailMessage
    deleted_attachment: _attachment_pb2.Attachment
    event_time: _timestamp_pb2.Timestamp

    def __init__(self, comment: _Optional[_Union[_comment_pb2.Comment, _Mapping]]=..., attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]]=..., email_message: _Optional[_Union[_email_message_pb2.EmailMessage, _Mapping]]=..., deleted_attachment: _Optional[_Union[_attachment_pb2.Attachment, _Mapping]]=..., event_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...