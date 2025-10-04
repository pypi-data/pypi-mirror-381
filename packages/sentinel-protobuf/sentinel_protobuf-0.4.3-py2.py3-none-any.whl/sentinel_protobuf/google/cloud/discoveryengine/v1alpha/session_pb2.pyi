from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.discoveryengine.v1alpha import answer_pb2 as _answer_pb2
from google.cloud.discoveryengine.v1alpha import common_pb2 as _common_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FileSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FILE_SOURCE_UNSPECIFIED: _ClassVar[FileSource]
    FILE_SOURCE_INLINE: _ClassVar[FileSource]
    FILE_SOURCE_LOCAL: _ClassVar[FileSource]
    FILE_SOURCE_CLOUD_STORAGE: _ClassVar[FileSource]
    FILE_SOURCE_CLOUD_DRIVE: _ClassVar[FileSource]
    FILE_SOURCE_URL: _ClassVar[FileSource]
FILE_SOURCE_UNSPECIFIED: FileSource
FILE_SOURCE_INLINE: FileSource
FILE_SOURCE_LOCAL: FileSource
FILE_SOURCE_CLOUD_STORAGE: FileSource
FILE_SOURCE_CLOUD_DRIVE: FileSource
FILE_SOURCE_URL: FileSource

class Session(_message.Message):
    __slots__ = ('name', 'display_name', 'state', 'user_pseudo_id', 'turns', 'start_time', 'end_time', 'is_pinned')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Session.State]
        IN_PROGRESS: _ClassVar[Session.State]
    STATE_UNSPECIFIED: Session.State
    IN_PROGRESS: Session.State

    class Turn(_message.Message):
        __slots__ = ('query', 'answer', 'detailed_answer', 'query_config')

        class QueryConfigEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        QUERY_FIELD_NUMBER: _ClassVar[int]
        ANSWER_FIELD_NUMBER: _ClassVar[int]
        DETAILED_ANSWER_FIELD_NUMBER: _ClassVar[int]
        QUERY_CONFIG_FIELD_NUMBER: _ClassVar[int]
        query: Query
        answer: str
        detailed_answer: _answer_pb2.Answer
        query_config: _containers.ScalarMap[str, str]

        def __init__(self, query: _Optional[_Union[Query, _Mapping]]=..., answer: _Optional[str]=..., detailed_answer: _Optional[_Union[_answer_pb2.Answer, _Mapping]]=..., query_config: _Optional[_Mapping[str, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    USER_PSEUDO_ID_FIELD_NUMBER: _ClassVar[int]
    TURNS_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    IS_PINNED_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    state: Session.State
    user_pseudo_id: str
    turns: _containers.RepeatedCompositeFieldContainer[Session.Turn]
    start_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    is_pinned: bool

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[Session.State, str]]=..., user_pseudo_id: _Optional[str]=..., turns: _Optional[_Iterable[_Union[Session.Turn, _Mapping]]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., is_pinned: bool=...) -> None:
        ...

class Query(_message.Message):
    __slots__ = ('text', 'query_id')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    QUERY_ID_FIELD_NUMBER: _ClassVar[int]
    text: str
    query_id: str

    def __init__(self, text: _Optional[str]=..., query_id: _Optional[str]=...) -> None:
        ...

class ImageCharacteristics(_message.Message):
    __slots__ = ('width', 'height', 'color_space', 'bit_depth')

    class ColorSpace(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        COLOR_SPACE_UNSPECIFIED: _ClassVar[ImageCharacteristics.ColorSpace]
        RGB: _ClassVar[ImageCharacteristics.ColorSpace]
        CMYK: _ClassVar[ImageCharacteristics.ColorSpace]
        GRAYSCALE: _ClassVar[ImageCharacteristics.ColorSpace]
        YUV: _ClassVar[ImageCharacteristics.ColorSpace]
        OTHER_COLOR_SPACE: _ClassVar[ImageCharacteristics.ColorSpace]
    COLOR_SPACE_UNSPECIFIED: ImageCharacteristics.ColorSpace
    RGB: ImageCharacteristics.ColorSpace
    CMYK: ImageCharacteristics.ColorSpace
    GRAYSCALE: ImageCharacteristics.ColorSpace
    YUV: ImageCharacteristics.ColorSpace
    OTHER_COLOR_SPACE: ImageCharacteristics.ColorSpace
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    COLOR_SPACE_FIELD_NUMBER: _ClassVar[int]
    BIT_DEPTH_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    color_space: ImageCharacteristics.ColorSpace
    bit_depth: int

    def __init__(self, width: _Optional[int]=..., height: _Optional[int]=..., color_space: _Optional[_Union[ImageCharacteristics.ColorSpace, str]]=..., bit_depth: _Optional[int]=...) -> None:
        ...

class VideoCharacteristics(_message.Message):
    __slots__ = ('width', 'height', 'duration', 'frame_rate', 'audio_codecs', 'video_codecs', 'video_bitrate_kbps', 'audio_bitrate_kbps')
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_CODECS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CODECS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BITRATE_KBPS_FIELD_NUMBER: _ClassVar[int]
    width: int
    height: int
    duration: _duration_pb2.Duration
    frame_rate: float
    audio_codecs: _containers.RepeatedScalarFieldContainer[str]
    video_codecs: _containers.RepeatedScalarFieldContainer[str]
    video_bitrate_kbps: int
    audio_bitrate_kbps: int

    def __init__(self, width: _Optional[int]=..., height: _Optional[int]=..., duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., frame_rate: _Optional[float]=..., audio_codecs: _Optional[_Iterable[str]]=..., video_codecs: _Optional[_Iterable[str]]=..., video_bitrate_kbps: _Optional[int]=..., audio_bitrate_kbps: _Optional[int]=...) -> None:
        ...

class FileCharacteristics(_message.Message):
    __slots__ = ('characteristics',)

    class CharacteristicsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    characteristics: _containers.ScalarMap[str, str]

    def __init__(self, characteristics: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class FileView(_message.Message):
    __slots__ = ('image_characteristics', 'video_characteristics', 'file_characteristics', 'view_id', 'uri', 'mime_type', 'byte_size', 'create_time')
    IMAGE_CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    VIDEO_CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    FILE_CHARACTERISTICS_FIELD_NUMBER: _ClassVar[int]
    VIEW_ID_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    image_characteristics: ImageCharacteristics
    video_characteristics: VideoCharacteristics
    file_characteristics: FileCharacteristics
    view_id: str
    uri: str
    mime_type: str
    byte_size: int
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, image_characteristics: _Optional[_Union[ImageCharacteristics, _Mapping]]=..., video_characteristics: _Optional[_Union[VideoCharacteristics, _Mapping]]=..., file_characteristics: _Optional[_Union[FileCharacteristics, _Mapping]]=..., view_id: _Optional[str]=..., uri: _Optional[str]=..., mime_type: _Optional[str]=..., byte_size: _Optional[int]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FileMetadata(_message.Message):
    __slots__ = ('file_id', 'name', 'mime_type', 'byte_size', 'original_uri', 'original_source_type', 'upload_time', 'last_add_time', 'metadata', 'download_uri', 'file_origin_type', 'views')

    class MetadataEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...

    class ViewsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: FileView

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[FileView, _Mapping]]=...) -> None:
            ...
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    BYTE_SIZE_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_URI_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    UPLOAD_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_ADD_TIME_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_URI_FIELD_NUMBER: _ClassVar[int]
    FILE_ORIGIN_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    file_id: str
    name: str
    mime_type: str
    byte_size: int
    original_uri: str
    original_source_type: FileSource
    upload_time: _timestamp_pb2.Timestamp
    last_add_time: _timestamp_pb2.Timestamp
    metadata: _containers.ScalarMap[str, str]
    download_uri: str
    file_origin_type: _common_pb2.FileOriginType
    views: _containers.MessageMap[str, FileView]

    def __init__(self, file_id: _Optional[str]=..., name: _Optional[str]=..., mime_type: _Optional[str]=..., byte_size: _Optional[int]=..., original_uri: _Optional[str]=..., original_source_type: _Optional[_Union[FileSource, str]]=..., upload_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_add_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., metadata: _Optional[_Mapping[str, str]]=..., download_uri: _Optional[str]=..., file_origin_type: _Optional[_Union[_common_pb2.FileOriginType, str]]=..., views: _Optional[_Mapping[str, FileView]]=...) -> None:
        ...