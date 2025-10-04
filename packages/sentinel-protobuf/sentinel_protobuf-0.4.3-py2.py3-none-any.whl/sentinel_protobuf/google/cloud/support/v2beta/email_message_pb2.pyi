from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.support.v2beta import actor_pb2 as _actor_pb2
from google.cloud.support.v2beta import content_pb2 as _content_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EmailMessage(_message.Message):
    __slots__ = ('name', 'create_time', 'actor', 'subject', 'recipient_email_addresses', 'cc_email_addresses', 'body_content')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ACTOR_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    RECIPIENT_EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    CC_EMAIL_ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    BODY_CONTENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    actor: _actor_pb2.Actor
    subject: str
    recipient_email_addresses: _containers.RepeatedScalarFieldContainer[str]
    cc_email_addresses: _containers.RepeatedScalarFieldContainer[str]
    body_content: _content_pb2.TextContent

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., actor: _Optional[_Union[_actor_pb2.Actor, _Mapping]]=..., subject: _Optional[str]=..., recipient_email_addresses: _Optional[_Iterable[str]]=..., cc_email_addresses: _Optional[_Iterable[str]]=..., body_content: _Optional[_Union[_content_pb2.TextContent, _Mapping]]=...) -> None:
        ...