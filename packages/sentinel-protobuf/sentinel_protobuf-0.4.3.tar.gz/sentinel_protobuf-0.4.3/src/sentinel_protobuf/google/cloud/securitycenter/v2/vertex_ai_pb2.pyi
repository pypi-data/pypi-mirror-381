from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class VertexAi(_message.Message):
    __slots__ = ('datasets', 'pipelines')

    class Dataset(_message.Message):
        __slots__ = ('name', 'display_name', 'source')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str
        source: str

        def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., source: _Optional[str]=...) -> None:
            ...

    class Pipeline(_message.Message):
        __slots__ = ('name', 'display_name')
        NAME_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        display_name: str

        def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=...) -> None:
            ...
    DATASETS_FIELD_NUMBER: _ClassVar[int]
    PIPELINES_FIELD_NUMBER: _ClassVar[int]
    datasets: _containers.RepeatedCompositeFieldContainer[VertexAi.Dataset]
    pipelines: _containers.RepeatedCompositeFieldContainer[VertexAi.Pipeline]

    def __init__(self, datasets: _Optional[_Iterable[_Union[VertexAi.Dataset, _Mapping]]]=..., pipelines: _Optional[_Iterable[_Union[VertexAi.Pipeline, _Mapping]]]=...) -> None:
        ...