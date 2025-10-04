from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.cloudsecuritycompliance.v1 import common_pb2 as _common_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ListFrameworksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListFrameworksResponse(_message.Message):
    __slots__ = ('frameworks', 'next_page_token')
    FRAMEWORKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    frameworks: _containers.RepeatedCompositeFieldContainer[_common_pb2.Framework]
    next_page_token: str

    def __init__(self, frameworks: _Optional[_Iterable[_Union[_common_pb2.Framework, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetFrameworkRequest(_message.Message):
    __slots__ = ('name', 'major_revision_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    major_revision_id: int

    def __init__(self, name: _Optional[str]=..., major_revision_id: _Optional[int]=...) -> None:
        ...

class CreateFrameworkRequest(_message.Message):
    __slots__ = ('parent', 'framework_id', 'framework')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_ID_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    parent: str
    framework_id: str
    framework: _common_pb2.Framework

    def __init__(self, parent: _Optional[str]=..., framework_id: _Optional[str]=..., framework: _Optional[_Union[_common_pb2.Framework, _Mapping]]=...) -> None:
        ...

class UpdateFrameworkRequest(_message.Message):
    __slots__ = ('update_mask', 'framework', 'major_revision_id')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    MAJOR_REVISION_ID_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    framework: _common_pb2.Framework
    major_revision_id: int

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., framework: _Optional[_Union[_common_pb2.Framework, _Mapping]]=..., major_revision_id: _Optional[int]=...) -> None:
        ...

class DeleteFrameworkRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCloudControlsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListCloudControlsResponse(_message.Message):
    __slots__ = ('cloud_controls', 'next_page_token')
    CLOUD_CONTROLS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_controls: _containers.RepeatedCompositeFieldContainer[_common_pb2.CloudControl]
    next_page_token: str

    def __init__(self, cloud_controls: _Optional[_Iterable[_Union[_common_pb2.CloudControl, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCloudControlRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCloudControlRequest(_message.Message):
    __slots__ = ('parent', 'cloud_control_id', 'cloud_control')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_ID_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    cloud_control_id: str
    cloud_control: _common_pb2.CloudControl

    def __init__(self, parent: _Optional[str]=..., cloud_control_id: _Optional[str]=..., cloud_control: _Optional[_Union[_common_pb2.CloudControl, _Mapping]]=...) -> None:
        ...

class UpdateCloudControlRequest(_message.Message):
    __slots__ = ('update_mask', 'cloud_control')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    cloud_control: _common_pb2.CloudControl

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., cloud_control: _Optional[_Union[_common_pb2.CloudControl, _Mapping]]=...) -> None:
        ...

class DeleteCloudControlRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...