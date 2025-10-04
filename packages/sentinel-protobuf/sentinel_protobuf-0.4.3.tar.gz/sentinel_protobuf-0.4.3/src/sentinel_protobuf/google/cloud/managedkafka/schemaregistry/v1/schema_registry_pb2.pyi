from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import httpbody_pb2 as _httpbody_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.managedkafka.schemaregistry.v1 import schema_registry_resources_pb2 as _schema_registry_resources_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetSchemaRegistryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListSchemaRegistriesRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListSchemaRegistriesResponse(_message.Message):
    __slots__ = ('schema_registries',)
    SCHEMA_REGISTRIES_FIELD_NUMBER: _ClassVar[int]
    schema_registries: _containers.RepeatedCompositeFieldContainer[_schema_registry_resources_pb2.SchemaRegistry]

    def __init__(self, schema_registries: _Optional[_Iterable[_Union[_schema_registry_resources_pb2.SchemaRegistry, _Mapping]]]=...) -> None:
        ...

class CreateSchemaRegistryRequest(_message.Message):
    __slots__ = ('parent', 'schema_registry_id', 'schema_registry')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REGISTRY_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_REGISTRY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    schema_registry_id: str
    schema_registry: _schema_registry_resources_pb2.SchemaRegistry

    def __init__(self, parent: _Optional[str]=..., schema_registry_id: _Optional[str]=..., schema_registry: _Optional[_Union[_schema_registry_resources_pb2.SchemaRegistry, _Mapping]]=...) -> None:
        ...

class DeleteSchemaRegistryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetContextRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListContextsRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class GetSchemaRequest(_message.Message):
    __slots__ = ('name', 'subject')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    name: str
    subject: str

    def __init__(self, name: _Optional[str]=..., subject: _Optional[str]=...) -> None:
        ...

class ListSchemaTypesRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class ListSchemaVersionsRequest(_message.Message):
    __slots__ = ('parent', 'subject', 'deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subject: str
    deleted: bool

    def __init__(self, parent: _Optional[str]=..., subject: _Optional[str]=..., deleted: bool=...) -> None:
        ...

class ListSubjectsRequest(_message.Message):
    __slots__ = ('parent', 'subject_prefix', 'deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subject_prefix: str
    deleted: bool

    def __init__(self, parent: _Optional[str]=..., subject_prefix: _Optional[str]=..., deleted: bool=...) -> None:
        ...

class ListSubjectsBySchemaIdRequest(_message.Message):
    __slots__ = ('parent', 'subject', 'deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SUBJECT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    subject: str
    deleted: bool

    def __init__(self, parent: _Optional[str]=..., subject: _Optional[str]=..., deleted: bool=...) -> None:
        ...

class ListVersionsRequest(_message.Message):
    __slots__ = ('parent', 'deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    deleted: bool

    def __init__(self, parent: _Optional[str]=..., deleted: bool=...) -> None:
        ...

class DeleteSubjectRequest(_message.Message):
    __slots__ = ('name', 'permanent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    permanent: bool

    def __init__(self, name: _Optional[str]=..., permanent: bool=...) -> None:
        ...

class GetVersionRequest(_message.Message):
    __slots__ = ('name', 'deleted')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    name: str
    deleted: bool

    def __init__(self, name: _Optional[str]=..., deleted: bool=...) -> None:
        ...

class CreateVersionRequest(_message.Message):
    __slots__ = ('parent', 'version', 'id', 'schema_type', 'schema', 'references', 'normalize')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    version: int
    id: int
    schema_type: _schema_registry_resources_pb2.Schema.SchemaType
    schema: str
    references: _containers.RepeatedCompositeFieldContainer[_schema_registry_resources_pb2.Schema.SchemaReference]
    normalize: bool

    def __init__(self, parent: _Optional[str]=..., version: _Optional[int]=..., id: _Optional[int]=..., schema_type: _Optional[_Union[_schema_registry_resources_pb2.Schema.SchemaType, str]]=..., schema: _Optional[str]=..., references: _Optional[_Iterable[_Union[_schema_registry_resources_pb2.Schema.SchemaReference, _Mapping]]]=..., normalize: bool=...) -> None:
        ...

class CreateVersionResponse(_message.Message):
    __slots__ = ('id',)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int

    def __init__(self, id: _Optional[int]=...) -> None:
        ...

class LookupVersionRequest(_message.Message):
    __slots__ = ('parent', 'schema_type', 'schema', 'references', 'normalize', 'deleted')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_FIELD_NUMBER: _ClassVar[int]
    DELETED_FIELD_NUMBER: _ClassVar[int]
    parent: str
    schema_type: _schema_registry_resources_pb2.Schema.SchemaType
    schema: str
    references: _containers.RepeatedCompositeFieldContainer[_schema_registry_resources_pb2.Schema.SchemaReference]
    normalize: bool
    deleted: bool

    def __init__(self, parent: _Optional[str]=..., schema_type: _Optional[_Union[_schema_registry_resources_pb2.Schema.SchemaType, str]]=..., schema: _Optional[str]=..., references: _Optional[_Iterable[_Union[_schema_registry_resources_pb2.Schema.SchemaReference, _Mapping]]]=..., normalize: bool=..., deleted: bool=...) -> None:
        ...

class DeleteVersionRequest(_message.Message):
    __slots__ = ('name', 'permanent')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PERMANENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    permanent: bool

    def __init__(self, name: _Optional[str]=..., permanent: bool=...) -> None:
        ...

class ListReferencedSchemasRequest(_message.Message):
    __slots__ = ('parent',)
    PARENT_FIELD_NUMBER: _ClassVar[int]
    parent: str

    def __init__(self, parent: _Optional[str]=...) -> None:
        ...

class CheckCompatibilityRequest(_message.Message):
    __slots__ = ('name', 'schema_type', 'schema', 'references', 'verbose')
    NAME_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_TYPE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    REFERENCES_FIELD_NUMBER: _ClassVar[int]
    VERBOSE_FIELD_NUMBER: _ClassVar[int]
    name: str
    schema_type: _schema_registry_resources_pb2.Schema.SchemaType
    schema: str
    references: _containers.RepeatedCompositeFieldContainer[_schema_registry_resources_pb2.Schema.SchemaReference]
    verbose: bool

    def __init__(self, name: _Optional[str]=..., schema_type: _Optional[_Union[_schema_registry_resources_pb2.Schema.SchemaType, str]]=..., schema: _Optional[str]=..., references: _Optional[_Iterable[_Union[_schema_registry_resources_pb2.Schema.SchemaReference, _Mapping]]]=..., verbose: bool=...) -> None:
        ...

class CheckCompatibilityResponse(_message.Message):
    __slots__ = ('is_compatible', 'messages')
    IS_COMPATIBLE_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    is_compatible: bool
    messages: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, is_compatible: bool=..., messages: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetSchemaConfigRequest(_message.Message):
    __slots__ = ('name', 'default_to_global')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TO_GLOBAL_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_to_global: bool

    def __init__(self, name: _Optional[str]=..., default_to_global: bool=...) -> None:
        ...

class UpdateSchemaConfigRequest(_message.Message):
    __slots__ = ('name', 'compatibility', 'normalize')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMPATIBILITY_FIELD_NUMBER: _ClassVar[int]
    NORMALIZE_FIELD_NUMBER: _ClassVar[int]
    name: str
    compatibility: _schema_registry_resources_pb2.SchemaConfig.CompatibilityType
    normalize: bool

    def __init__(self, name: _Optional[str]=..., compatibility: _Optional[_Union[_schema_registry_resources_pb2.SchemaConfig.CompatibilityType, str]]=..., normalize: bool=...) -> None:
        ...

class DeleteSchemaConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetSchemaModeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateSchemaModeRequest(_message.Message):
    __slots__ = ('name', 'mode')
    NAME_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    mode: _schema_registry_resources_pb2.SchemaMode.ModeType

    def __init__(self, name: _Optional[str]=..., mode: _Optional[_Union[_schema_registry_resources_pb2.SchemaMode.ModeType, str]]=...) -> None:
        ...

class DeleteSchemaModeRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...