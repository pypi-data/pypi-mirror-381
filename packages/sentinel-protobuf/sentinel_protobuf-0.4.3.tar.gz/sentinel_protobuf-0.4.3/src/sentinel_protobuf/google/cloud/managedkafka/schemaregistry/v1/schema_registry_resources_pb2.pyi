from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class SchemaRegistry(_message.Message):
    __slots__ = ('name', 'contexts')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONTEXTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    contexts: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., contexts: _Optional[_Iterable[str]]=...) -> None:
        ...

class Context(_message.Message):
    __slots__ = ('name', 'subjects')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    subjects: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., subjects: _Optional[_Iterable[str]]=...) -> None:
        ...

class Schema(_message.Message):
    __slots__ = ('schema_type', 'schema_payload', 'references')

    class SchemaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SCHEMA_TYPE_UNSPECIFIED: _ClassVar[Schema.SchemaType]
        AVRO: _ClassVar[Schema.SchemaType]
        JSON: _ClassVar[Schema.SchemaType]
        PROTOBUF: _ClassVar[Schema.SchemaType]
    SCHEMA_TYPE_UNSPECIFIED: Schema.SchemaType
    AVRO: Schema.SchemaType
    JSON: Schema.SchemaType
    PROTOBUF: Schema.SchemaType

    class SchemaReference(_message.Message):
        __slots__ = ('name', 'subject', 'version')
        NAME_FIELD_NUMBER: _ClassVar[int]
        SUBJECT_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        name: str
        subject: str
        version: int

        def __init__(self, name: _Optional[str]=..., subject: _Optional[str]=..., version: _Optional[int]=...) -> None:
            ...
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    schema_type: Schema.SchemaType
    schema_payload: str
    references: _containers.RepeatedCompositeFieldContainer[Schema.SchemaReference]

    def __init__(self, schema_type: _Optional[_Union[Schema.SchemaType, str]]=..., schema_payload: _Optional[str]=..., references: _Optional[_Iterable[_Union[Schema.SchemaReference, _Mapping]]]=...) -> None:
        ...

class SchemaSubject(_message.Message):
    __slots__ = ('name', 'versions')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    versions: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., versions: _Optional[_Iterable[str]]=...) -> None:
        ...

class SchemaVersion(_message.Message):
    __slots__ = ('subject', 'version_id', 'schema_id', 'schema_type', 'schema_payload', 'references')
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    VERSION_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    subject: str
    version_id: int
    schema_id: int
    schema_type: Schema.SchemaType
    schema_payload: str
    references: _containers.RepeatedCompositeFieldContainer[Schema.SchemaReference]

    def __init__(self, subject: _Optional[str]=..., version_id: _Optional[int]=..., schema_id: _Optional[int]=..., schema_type: _Optional[_Union[Schema.SchemaType, str]]=..., schema_payload: _Optional[str]=..., references: _Optional[_Iterable[_Union[Schema.SchemaReference, _Mapping]]]=...) -> None:
        ...

class SchemaConfig(_message.Message):
    __slots__ = ('compatibility', 'normalize', 'alias')

    class CompatibilityType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SchemaConfig.CompatibilityType]
        BACKWARD: _ClassVar[SchemaConfig.CompatibilityType]
        BACKWARD_TRANSITIVE: _ClassVar[SchemaConfig.CompatibilityType]
        FORWARD: _ClassVar[SchemaConfig.CompatibilityType]
        FORWARD_TRANSITIVE: _ClassVar[SchemaConfig.CompatibilityType]
        FULL: _ClassVar[SchemaConfig.CompatibilityType]
        FULL_TRANSITIVE: _ClassVar[SchemaConfig.CompatibilityType]
    NONE: SchemaConfig.CompatibilityType
    BACKWARD: SchemaConfig.CompatibilityType
    BACKWARD_TRANSITIVE: SchemaConfig.CompatibilityType
    FORWARD: SchemaConfig.CompatibilityType
    FORWARD_TRANSITIVE: SchemaConfig.CompatibilityType
    FULL: SchemaConfig.CompatibilityType
    FULL_TRANSITIVE: SchemaConfig.CompatibilityType
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    compatibility: SchemaConfig.CompatibilityType
    normalize: bool
    alias: str

    def __init__(self, compatibility: _Optional[_Union[SchemaConfig.CompatibilityType, str]]=..., normalize: bool=..., alias: _Optional[str]=...) -> None:
        ...

class SchemaMode(_message.Message):
    __slots__ = ('mode',)

    class ModeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NONE: _ClassVar[SchemaMode.ModeType]
        READONLY: _ClassVar[SchemaMode.ModeType]
        READWRITE: _ClassVar[SchemaMode.ModeType]
        IMPORT: _ClassVar[SchemaMode.ModeType]
    NONE: SchemaMode.ModeType
    READONLY: SchemaMode.ModeType
    READWRITE: SchemaMode.ModeType
    IMPORT: SchemaMode.ModeType
    MODE_FIELD_NUMBER: _ClassVar[int]
    mode: SchemaMode.ModeType

    def __init__(self, mode: _Optional[_Union[SchemaMode.ModeType, str]]=...) -> None:
        ...