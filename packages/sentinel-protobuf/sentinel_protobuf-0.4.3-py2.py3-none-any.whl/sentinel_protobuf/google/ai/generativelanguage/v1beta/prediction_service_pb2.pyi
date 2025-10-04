from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PredictRequest(_message.Message):
    __slots__ = ('model', 'instances', 'parameters')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    parameters: _struct_pb2.Value

    def __init__(self, model: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class PredictLongRunningRequest(_message.Message):
    __slots__ = ('model', 'instances', 'parameters')
    MODEL_FIELD_NUMBER: _ClassVar[int]
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    PARAMETERS_FIELD_NUMBER: _ClassVar[int]
    model: str
    instances: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]
    parameters: _struct_pb2.Value

    def __init__(self, model: _Optional[str]=..., instances: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=..., parameters: _Optional[_Union[_struct_pb2.Value, _Mapping]]=...) -> None:
        ...

class PredictResponse(_message.Message):
    __slots__ = ('predictions',)
    PREDICTIONS_FIELD_NUMBER: _ClassVar[int]
    predictions: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Value]

    def __init__(self, predictions: _Optional[_Iterable[_Union[_struct_pb2.Value, _Mapping]]]=...) -> None:
        ...

class PredictLongRunningResponse(_message.Message):
    __slots__ = ('generate_video_response',)
    GENERATE_VIDEO_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    generate_video_response: GenerateVideoResponse

    def __init__(self, generate_video_response: _Optional[_Union[GenerateVideoResponse, _Mapping]]=...) -> None:
        ...

class PredictLongRunningMetadata(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class Media(_message.Message):
    __slots__ = ('video',)
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    video: Video

    def __init__(self, video: _Optional[_Union[Video, _Mapping]]=...) -> None:
        ...

class Video(_message.Message):
    __slots__ = ('video', 'uri')
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    video: bytes
    uri: str

    def __init__(self, video: _Optional[bytes]=..., uri: _Optional[str]=...) -> None:
        ...

class GenerateVideoResponse(_message.Message):
    __slots__ = ('generated_samples', 'rai_media_filtered_count', 'rai_media_filtered_reasons')
    GENERATED_SAMPLES_FIELD_NUMBER: _ClassVar[int]
    RAI_MEDIA_FILTERED_COUNT_FIELD_NUMBER: _ClassVar[int]
    RAI_MEDIA_FILTERED_REASONS_FIELD_NUMBER: _ClassVar[int]
    generated_samples: _containers.RepeatedCompositeFieldContainer[Media]
    rai_media_filtered_count: int
    rai_media_filtered_reasons: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, generated_samples: _Optional[_Iterable[_Union[Media, _Mapping]]]=..., rai_media_filtered_count: _Optional[int]=..., rai_media_filtered_reasons: _Optional[_Iterable[str]]=...) -> None:
        ...