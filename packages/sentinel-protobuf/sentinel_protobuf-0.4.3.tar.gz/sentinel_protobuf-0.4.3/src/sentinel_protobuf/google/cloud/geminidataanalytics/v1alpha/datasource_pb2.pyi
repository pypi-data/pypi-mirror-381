from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.geminidataanalytics.v1alpha import credentials_pb2 as _credentials_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataFilterType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DATA_FILTER_TYPE_UNSPECIFIED: _ClassVar[DataFilterType]
    ALWAYS_FILTER: _ClassVar[DataFilterType]
DATA_FILTER_TYPE_UNSPECIFIED: DataFilterType
ALWAYS_FILTER: DataFilterType

class DatasourceReferences(_message.Message):
    __slots__ = ('bq', 'studio', 'looker')
    BQ_FIELD_NUMBER: _ClassVar[int]
    STUDIO_FIELD_NUMBER: _ClassVar[int]
    LOOKER_FIELD_NUMBER: _ClassVar[int]
    bq: BigQueryTableReferences
    studio: StudioDatasourceReferences
    looker: LookerExploreReferences

    def __init__(self, bq: _Optional[_Union[BigQueryTableReferences, _Mapping]]=..., studio: _Optional[_Union[StudioDatasourceReferences, _Mapping]]=..., looker: _Optional[_Union[LookerExploreReferences, _Mapping]]=...) -> None:
        ...

class BigQueryTableReferences(_message.Message):
    __slots__ = ('table_references',)
    TABLE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    table_references: _containers.RepeatedCompositeFieldContainer[BigQueryTableReference]

    def __init__(self, table_references: _Optional[_Iterable[_Union[BigQueryTableReference, _Mapping]]]=...) -> None:
        ...

class BigQueryTableReference(_message.Message):
    __slots__ = ('project_id', 'dataset_id', 'table_id', 'schema')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    DATASET_ID_FIELD_NUMBER: _ClassVar[int]
    TABLE_ID_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    dataset_id: str
    table_id: str
    schema: Schema

    def __init__(self, project_id: _Optional[str]=..., dataset_id: _Optional[str]=..., table_id: _Optional[str]=..., schema: _Optional[_Union[Schema, _Mapping]]=...) -> None:
        ...

class StudioDatasourceReferences(_message.Message):
    __slots__ = ('studio_references',)
    STUDIO_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    studio_references: _containers.RepeatedCompositeFieldContainer[StudioDatasourceReference]

    def __init__(self, studio_references: _Optional[_Iterable[_Union[StudioDatasourceReference, _Mapping]]]=...) -> None:
        ...

class StudioDatasourceReference(_message.Message):
    __slots__ = ('datasource_id',)
    DATASOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    datasource_id: str

    def __init__(self, datasource_id: _Optional[str]=...) -> None:
        ...

class LookerExploreReferences(_message.Message):
    __slots__ = ('explore_references', 'credentials')
    EXPLORE_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CREDENTIALS_FIELD_NUMBER: _ClassVar[int]
    explore_references: _containers.RepeatedCompositeFieldContainer[LookerExploreReference]
    credentials: _credentials_pb2.Credentials

    def __init__(self, explore_references: _Optional[_Iterable[_Union[LookerExploreReference, _Mapping]]]=..., credentials: _Optional[_Union[_credentials_pb2.Credentials, _Mapping]]=...) -> None:
        ...

class LookerExploreReference(_message.Message):
    __slots__ = ('looker_instance_uri', 'private_looker_instance_info', 'lookml_model', 'explore', 'schema')
    LOOKER_INSTANCE_URI_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_LOOKER_INSTANCE_INFO_FIELD_NUMBER: _ClassVar[int]
    LOOKML_MODEL_FIELD_NUMBER: _ClassVar[int]
    EXPLORE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    looker_instance_uri: str
    private_looker_instance_info: PrivateLookerInstanceInfo
    lookml_model: str
    explore: str
    schema: Schema

    def __init__(self, looker_instance_uri: _Optional[str]=..., private_looker_instance_info: _Optional[_Union[PrivateLookerInstanceInfo, _Mapping]]=..., lookml_model: _Optional[str]=..., explore: _Optional[str]=..., schema: _Optional[_Union[Schema, _Mapping]]=...) -> None:
        ...

class PrivateLookerInstanceInfo(_message.Message):
    __slots__ = ('looker_instance_id', 'service_directory_name')
    LOOKER_INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    SERVICE_DIRECTORY_NAME_FIELD_NUMBER: _ClassVar[int]
    looker_instance_id: str
    service_directory_name: str

    def __init__(self, looker_instance_id: _Optional[str]=..., service_directory_name: _Optional[str]=...) -> None:
        ...

class Datasource(_message.Message):
    __slots__ = ('bigquery_table_reference', 'studio_datasource_id', 'looker_explore_reference', 'schema')
    BIGQUERY_TABLE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    STUDIO_DATASOURCE_ID_FIELD_NUMBER: _ClassVar[int]
    LOOKER_EXPLORE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    bigquery_table_reference: BigQueryTableReference
    studio_datasource_id: str
    looker_explore_reference: LookerExploreReference
    schema: Schema

    def __init__(self, bigquery_table_reference: _Optional[_Union[BigQueryTableReference, _Mapping]]=..., studio_datasource_id: _Optional[str]=..., looker_explore_reference: _Optional[_Union[LookerExploreReference, _Mapping]]=..., schema: _Optional[_Union[Schema, _Mapping]]=...) -> None:
        ...

class Schema(_message.Message):
    __slots__ = ('fields', 'description', 'synonyms', 'tags', 'display_name', 'filters')
    FIELDS_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    FILTERS_FIELD_NUMBER: _ClassVar[int]
    fields: _containers.RepeatedCompositeFieldContainer[Field]
    description: str
    synonyms: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    filters: _containers.RepeatedCompositeFieldContainer[DataFilter]

    def __init__(self, fields: _Optional[_Iterable[_Union[Field, _Mapping]]]=..., description: _Optional[str]=..., synonyms: _Optional[_Iterable[str]]=..., tags: _Optional[_Iterable[str]]=..., display_name: _Optional[str]=..., filters: _Optional[_Iterable[_Union[DataFilter, _Mapping]]]=...) -> None:
        ...

class Field(_message.Message):
    __slots__ = ('name', 'type', 'description', 'mode', 'synonyms', 'tags', 'display_name', 'subfields', 'category', 'value_format')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SYNONYMS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    SUBFIELDS_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FORMAT_FIELD_NUMBER: _ClassVar[int]
    name: str
    type: str
    description: str
    mode: str
    synonyms: _containers.RepeatedScalarFieldContainer[str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    display_name: str
    subfields: _containers.RepeatedCompositeFieldContainer[Field]
    category: str
    value_format: str

    def __init__(self, name: _Optional[str]=..., type: _Optional[str]=..., description: _Optional[str]=..., mode: _Optional[str]=..., synonyms: _Optional[_Iterable[str]]=..., tags: _Optional[_Iterable[str]]=..., display_name: _Optional[str]=..., subfields: _Optional[_Iterable[_Union[Field, _Mapping]]]=..., category: _Optional[str]=..., value_format: _Optional[str]=...) -> None:
        ...

class DataFilter(_message.Message):
    __slots__ = ('field', 'value', 'type')
    FIELD_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    field: str
    value: str
    type: DataFilterType

    def __init__(self, field: _Optional[str]=..., value: _Optional[str]=..., type: _Optional[_Union[DataFilterType, str]]=...) -> None:
        ...