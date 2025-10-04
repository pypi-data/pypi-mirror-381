from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.aiplatform.v1 import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateSyntheticDataRequest(_message.Message):
    __slots__ = ('task_description', 'location', 'count', 'output_field_specs', 'examples')
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_FIELD_SPECS_FIELD_NUMBER: _ClassVar[int]
    EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    task_description: TaskDescriptionStrategy
    location: str
    count: int
    output_field_specs: _containers.RepeatedCompositeFieldContainer[OutputFieldSpec]
    examples: _containers.RepeatedCompositeFieldContainer[SyntheticExample]

    def __init__(self, task_description: _Optional[_Union[TaskDescriptionStrategy, _Mapping]]=..., location: _Optional[str]=..., count: _Optional[int]=..., output_field_specs: _Optional[_Iterable[_Union[OutputFieldSpec, _Mapping]]]=..., examples: _Optional[_Iterable[_Union[SyntheticExample, _Mapping]]]=...) -> None:
        ...

class SyntheticField(_message.Message):
    __slots__ = ('field_name', 'content')
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    content: _content_pb2.Content

    def __init__(self, field_name: _Optional[str]=..., content: _Optional[_Union[_content_pb2.Content, _Mapping]]=...) -> None:
        ...

class SyntheticExample(_message.Message):
    __slots__ = ('fields',)
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[SyntheticField]

    def __init__(self, fields: _Optional[_Iterable[_Union[SyntheticField, _Mapping]]]=...) -> None:
        ...

class OutputFieldSpec(_message.Message):
    __slots__ = ('field_name', 'guidance', 'field_type')

    class FieldType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FIELD_TYPE_UNSPECIFIED: _ClassVar[OutputFieldSpec.FieldType]
        CONTENT: _ClassVar[OutputFieldSpec.FieldType]
        TEXT: _ClassVar[OutputFieldSpec.FieldType]
        IMAGE: _ClassVar[OutputFieldSpec.FieldType]
        AUDIO: _ClassVar[OutputFieldSpec.FieldType]
    FIELD_TYPE_UNSPECIFIED: OutputFieldSpec.FieldType
    CONTENT: OutputFieldSpec.FieldType
    TEXT: OutputFieldSpec.FieldType
    IMAGE: OutputFieldSpec.FieldType
    AUDIO: OutputFieldSpec.FieldType
    FIELD_NAME_FIELD_NUMBER: _ClassVar[int]
    GUIDANCE_FIELD_NUMBER: _ClassVar[int]
    FIELD_TYPE_FIELD_NUMBER: _ClassVar[int]
    field_name: str
    guidance: str
    field_type: OutputFieldSpec.FieldType

    def __init__(self, field_name: _Optional[str]=..., guidance: _Optional[str]=..., field_type: _Optional[_Union[OutputFieldSpec.FieldType, str]]=...) -> None:
        ...

class TaskDescriptionStrategy(_message.Message):
    __slots__ = ('task_description',)
    TASK_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    task_description: str

    def __init__(self, task_description: _Optional[str]=...) -> None:
        ...

class GenerateSyntheticDataResponse(_message.Message):
    __slots__ = ('synthetic_examples',)
    SYNTHETIC_EXAMPLES_FIELD_NUMBER: _ClassVar[int]
    synthetic_examples: _containers.RepeatedCompositeFieldContainer[SyntheticExample]

    def __init__(self, synthetic_examples: _Optional[_Iterable[_Union[SyntheticExample, _Mapping]]]=...) -> None:
        ...