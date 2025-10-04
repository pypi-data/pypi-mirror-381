from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class IndustryVertical(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    INDUSTRY_VERTICAL_UNSPECIFIED: _ClassVar[IndustryVertical]
    GENERIC: _ClassVar[IndustryVertical]
    MEDIA: _ClassVar[IndustryVertical]
    HEALTHCARE_FHIR: _ClassVar[IndustryVertical]

class SolutionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SOLUTION_TYPE_UNSPECIFIED: _ClassVar[SolutionType]
    SOLUTION_TYPE_RECOMMENDATION: _ClassVar[SolutionType]
    SOLUTION_TYPE_SEARCH: _ClassVar[SolutionType]
    SOLUTION_TYPE_CHAT: _ClassVar[SolutionType]
    SOLUTION_TYPE_GENERATIVE_CHAT: _ClassVar[SolutionType]

class SearchUseCase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_USE_CASE_UNSPECIFIED: _ClassVar[SearchUseCase]
    SEARCH_USE_CASE_SEARCH: _ClassVar[SearchUseCase]
    SEARCH_USE_CASE_BROWSE: _ClassVar[SearchUseCase]

class SearchTier(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_TIER_UNSPECIFIED: _ClassVar[SearchTier]
    SEARCH_TIER_STANDARD: _ClassVar[SearchTier]
    SEARCH_TIER_ENTERPRISE: _ClassVar[SearchTier]

class SearchAddOn(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEARCH_ADD_ON_UNSPECIFIED: _ClassVar[SearchAddOn]
    SEARCH_ADD_ON_LLM: _ClassVar[SearchAddOn]
INDUSTRY_VERTICAL_UNSPECIFIED: IndustryVertical
GENERIC: IndustryVertical
MEDIA: IndustryVertical
HEALTHCARE_FHIR: IndustryVertical
SOLUTION_TYPE_UNSPECIFIED: SolutionType
SOLUTION_TYPE_RECOMMENDATION: SolutionType
SOLUTION_TYPE_SEARCH: SolutionType
SOLUTION_TYPE_CHAT: SolutionType
SOLUTION_TYPE_GENERATIVE_CHAT: SolutionType
SEARCH_USE_CASE_UNSPECIFIED: SearchUseCase
SEARCH_USE_CASE_SEARCH: SearchUseCase
SEARCH_USE_CASE_BROWSE: SearchUseCase
SEARCH_TIER_UNSPECIFIED: SearchTier
SEARCH_TIER_STANDARD: SearchTier
SEARCH_TIER_ENTERPRISE: SearchTier
SEARCH_ADD_ON_UNSPECIFIED: SearchAddOn
SEARCH_ADD_ON_LLM: SearchAddOn

class Interval(_message.Message):
    __slots__ = ('minimum', 'exclusive_minimum', 'maximum', 'exclusive_maximum')
    MINIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MINIMUM_FIELD_NUMBER: _ClassVar[int]
    MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    EXCLUSIVE_MAXIMUM_FIELD_NUMBER: _ClassVar[int]
    minimum: float
    exclusive_minimum: float
    maximum: float
    exclusive_maximum: float

    def __init__(self, minimum: _Optional[float]=..., exclusive_minimum: _Optional[float]=..., maximum: _Optional[float]=..., exclusive_maximum: _Optional[float]=...) -> None:
        ...

class CustomAttribute(_message.Message):
    __slots__ = ('text', 'numbers')
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NUMBERS_FIELD_NUMBER: _ClassVar[int]
    text: _containers.RepeatedScalarFieldContainer[str]
    numbers: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, text: _Optional[_Iterable[str]]=..., numbers: _Optional[_Iterable[float]]=...) -> None:
        ...

class UserInfo(_message.Message):
    __slots__ = ('user_id', 'user_agent', 'time_zone')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    USER_AGENT_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    user_agent: str
    time_zone: str

    def __init__(self, user_id: _Optional[str]=..., user_agent: _Optional[str]=..., time_zone: _Optional[str]=...) -> None:
        ...

class DoubleList(_message.Message):
    __slots__ = ('values',)
    VALUES_FIELD_NUMBER: _ClassVar[int]
    values: _containers.RepeatedScalarFieldContainer[float]

    def __init__(self, values: _Optional[_Iterable[float]]=...) -> None:
        ...

class Principal(_message.Message):
    __slots__ = ('user_id', 'group_id', 'external_entity_id')
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ENTITY_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    group_id: str
    external_entity_id: str

    def __init__(self, user_id: _Optional[str]=..., group_id: _Optional[str]=..., external_entity_id: _Optional[str]=...) -> None:
        ...

class HealthcareFhirConfig(_message.Message):
    __slots__ = ('enable_configurable_schema', 'enable_static_indexing_for_batch_ingestion')
    ENABLE_CONFIGURABLE_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    ENABLE_STATIC_INDEXING_FOR_BATCH_INGESTION_FIELD_NUMBER: _ClassVar[int]
    enable_configurable_schema: bool
    enable_static_indexing_for_batch_ingestion: bool

    def __init__(self, enable_configurable_schema: bool=..., enable_static_indexing_for_batch_ingestion: bool=...) -> None:
        ...

class SearchLinkPromotion(_message.Message):
    __slots__ = ('title', 'uri', 'document', 'image_uri', 'description', 'enabled')
    TITLE_FIELD_NUMBER: _ClassVar[int]
    URI_FIELD_NUMBER: _ClassVar[int]
    DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ENABLED_FIELD_NUMBER: _ClassVar[int]
    title: str
    uri: str
    document: str
    image_uri: str
    description: str
    enabled: bool

    def __init__(self, title: _Optional[str]=..., uri: _Optional[str]=..., document: _Optional[str]=..., image_uri: _Optional[str]=..., description: _Optional[str]=..., enabled: bool=...) -> None:
        ...