from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Modality(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    MODALITY_UNSPECIFIED: _ClassVar[Modality]
    TEXT: _ClassVar[Modality]
    IMAGE: _ClassVar[Modality]
    VIDEO: _ClassVar[Modality]
    AUDIO: _ClassVar[Modality]
    DOCUMENT: _ClassVar[Modality]
MODALITY_UNSPECIFIED: Modality
TEXT: Modality
IMAGE: Modality
VIDEO: Modality
AUDIO: Modality
DOCUMENT: Modality

class Content(_message.Message):
    __slots__ = ('parts', 'role')
    PARTS_FIELD_NUMBER: _ClassVar[int]
    ROLE_FIELD_NUMBER: _ClassVar[int]
    parts: _containers.RepeatedCompositeFieldContainer[Part]
    role: str

    def __init__(self, parts: _Optional[_Iterable[_Union[Part, _Mapping]]]=..., role: _Optional[str]=...) -> None:
        ...

class Part(_message.Message):
    __slots__ = ('text', 'inline_data', 'video_metadata')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    INLINE_DATA_FIELD_NUMBER: _ClassVar[int]
    VIDEO_METADATA_FIELD_NUMBER: _ClassVar[int]
    text: str
    inline_data: Blob
    video_metadata: VideoMetadata

    def __init__(self, text: _Optional[str]=..., inline_data: _Optional[_Union[Blob, _Mapping]]=..., video_metadata: _Optional[_Union[VideoMetadata, _Mapping]]=...) -> None:
        ...

class Blob(_message.Message):
    __slots__ = ('mime_type', 'data')
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    mime_type: str
    data: bytes

    def __init__(self, mime_type: _Optional[str]=..., data: _Optional[bytes]=...) -> None:
        ...

class VideoMetadata(_message.Message):
    __slots__ = ('start_offset', 'end_offset', 'fps')
    START_OFFSET_FIELD_NUMBER: _ClassVar[int]
    END_OFFSET_FIELD_NUMBER: _ClassVar[int]
    FPS_FIELD_NUMBER: _ClassVar[int]
    start_offset: _duration_pb2.Duration
    end_offset: _duration_pb2.Duration
    fps: float

    def __init__(self, start_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., end_offset: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., fps: _Optional[float]=...) -> None:
        ...

class ModalityTokenCount(_message.Message):
    __slots__ = ('modality', 'token_count')
    MODALITY_FIELD_NUMBER: _ClassVar[int]
    TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
    modality: Modality
    token_count: int

    def __init__(self, modality: _Optional[_Union[Modality, str]]=..., token_count: _Optional[int]=...) -> None:
        ...