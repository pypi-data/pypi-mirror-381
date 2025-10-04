from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.geminidataanalytics.v1alpha import datasource_pb2 as _datasource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Context(_message.Message):
    __slots__ = ('system_instruction', 'datasource_references', 'options', 'example_queries')
    SYSTEM_INSTRUCTION_FIELD_NUMBER: _ClassVar[int]
    DATASOURCE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    OPTIONS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLE_QUERIES_FIELD_NUMBER: _ClassVar[int]
    system_instruction: str
    datasource_references: _datasource_pb2.DatasourceReferences
    options: ConversationOptions
    example_queries: _containers.RepeatedCompositeFieldContainer[ExampleQuery]

    def __init__(self, system_instruction: _Optional[str]=..., datasource_references: _Optional[_Union[_datasource_pb2.DatasourceReferences, _Mapping]]=..., options: _Optional[_Union[ConversationOptions, _Mapping]]=..., example_queries: _Optional[_Iterable[_Union[ExampleQuery, _Mapping]]]=...) -> None:
        ...

class ExampleQuery(_message.Message):
    __slots__ = ('sql_query', 'natural_language_question')
    SQL_QUERY_FIELD_NUMBER: _ClassVar[int]
    NATURAL_LANGUAGE_QUESTION_FIELD_NUMBER: _ClassVar[int]
    sql_query: str
    natural_language_question: str

    def __init__(self, sql_query: _Optional[str]=..., natural_language_question: _Optional[str]=...) -> None:
        ...

class ConversationOptions(_message.Message):
    __slots__ = ('chart', 'analysis')
    CHART_FIELD_NUMBER: _ClassVar[int]
    ANALYSIS_FIELD_NUMBER: _ClassVar[int]
    chart: ChartOptions
    analysis: AnalysisOptions

    def __init__(self, chart: _Optional[_Union[ChartOptions, _Mapping]]=..., analysis: _Optional[_Union[AnalysisOptions, _Mapping]]=...) -> None:
        ...

class ChartOptions(_message.Message):
    __slots__ = ('image',)

    class ImageOptions(_message.Message):
        __slots__ = ('no_image', 'svg')

        class NoImage(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class SvgOptions(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        NO_IMAGE_FIELD_NUMBER: _ClassVar[int]
        SVG_FIELD_NUMBER: _ClassVar[int]
        no_image: ChartOptions.ImageOptions.NoImage
        svg: ChartOptions.ImageOptions.SvgOptions

        def __init__(self, no_image: _Optional[_Union[ChartOptions.ImageOptions.NoImage, _Mapping]]=..., svg: _Optional[_Union[ChartOptions.ImageOptions.SvgOptions, _Mapping]]=...) -> None:
            ...
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    image: ChartOptions.ImageOptions

    def __init__(self, image: _Optional[_Union[ChartOptions.ImageOptions, _Mapping]]=...) -> None:
        ...

class AnalysisOptions(_message.Message):
    __slots__ = ('python',)

    class Python(_message.Message):
        __slots__ = ('enabled',)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool

        def __init__(self, enabled: bool=...) -> None:
            ...
    PYTHON_FIELD_NUMBER: _ClassVar[int]
    python: AnalysisOptions.Python

    def __init__(self, python: _Optional[_Union[AnalysisOptions.Python, _Mapping]]=...) -> None:
        ...