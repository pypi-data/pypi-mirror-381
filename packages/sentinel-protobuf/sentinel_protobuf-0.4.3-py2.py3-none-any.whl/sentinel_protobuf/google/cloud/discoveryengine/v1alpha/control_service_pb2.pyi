from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import control_pb2 as _control_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CreateControlRequest(_message.Message):
    __slots__ = ('parent', 'control', 'control_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    control: _control_pb2.Control
    control_id: str

    def __init__(self, parent: _Optional[str]=..., control: _Optional[_Union[_control_pb2.Control, _Mapping]]=..., control_id: _Optional[str]=...) -> None:
        ...

class UpdateControlRequest(_message.Message):
    __slots__ = ('control', 'update_mask')
    CONTROL_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    control: _control_pb2.Control
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, control: _Optional[_Union[_control_pb2.Control, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteControlRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetControlRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListControlsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListControlsResponse(_message.Message):
    __slots__ = ('controls', 'next_page_token')
    CONTROLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    controls: _containers.RepeatedCompositeFieldContainer[_control_pb2.Control]
    next_page_token: str

    def __init__(self, controls: _Optional[_Iterable[_Union[_control_pb2.Control, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...