from google.ads.googleads.v20.enums import application_instance_pb2 as _application_instance_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AdditionalApplicationInfo(_message.Message):
    __slots__ = ('application_id', 'application_instance')
    APPLICATION_ID_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_INSTANCE_FIELD_NUMBER: _ClassVar[int]
    application_id: str
    application_instance: _application_instance_pb2.ApplicationInstanceEnum.ApplicationInstance

    def __init__(self, application_id: _Optional[str]=..., application_instance: _Optional[_Union[_application_instance_pb2.ApplicationInstanceEnum.ApplicationInstance, str]]=...) -> None:
        ...