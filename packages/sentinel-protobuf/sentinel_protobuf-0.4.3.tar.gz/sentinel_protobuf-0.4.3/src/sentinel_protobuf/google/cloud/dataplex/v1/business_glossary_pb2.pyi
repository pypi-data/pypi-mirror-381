from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.dataplex.v1 import service_pb2 as _service_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Glossary(_message.Message):
    __slots__ = ('name', 'uid', 'display_name', 'description', 'create_time', 'update_time', 'labels', 'term_count', 'category_count', 'etag')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    TERM_COUNT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_COUNT_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    term_count: int
    category_count: int
    etag: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., term_count: _Optional[int]=..., category_count: _Optional[int]=..., etag: _Optional[str]=...) -> None:
        ...

class GlossaryCategory(_message.Message):
    __slots__ = ('name', 'uid', 'display_name', 'description', 'create_time', 'update_time', 'labels', 'parent')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    parent: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., parent: _Optional[str]=...) -> None:
        ...

class GlossaryTerm(_message.Message):
    __slots__ = ('name', 'uid', 'display_name', 'description', 'create_time', 'update_time', 'labels', 'parent')

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    display_name: str
    description: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    parent: str

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., parent: _Optional[str]=...) -> None:
        ...

class CreateGlossaryRequest(_message.Message):
    __slots__ = ('parent', 'glossary_id', 'glossary', 'validate_only')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_ID_FIELD_NUMBER: _ClassVar[int]
    GLOSSARY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    glossary_id: str
    glossary: Glossary
    validate_only: bool

    def __init__(self, parent: _Optional[str]=..., glossary_id: _Optional[str]=..., glossary: _Optional[_Union[Glossary, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class UpdateGlossaryRequest(_message.Message):
    __slots__ = ('glossary', 'update_mask', 'validate_only')
    GLOSSARY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    glossary: Glossary
    update_mask: _field_mask_pb2.FieldMask
    validate_only: bool

    def __init__(self, glossary: _Optional[_Union[Glossary, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteGlossaryRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class GetGlossaryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGlossariesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListGlossariesResponse(_message.Message):
    __slots__ = ('glossaries', 'next_page_token', 'unreachable_locations')
    GLOSSARIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    glossaries: _containers.RepeatedCompositeFieldContainer[Glossary]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, glossaries: _Optional[_Iterable[_Union[Glossary, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateGlossaryCategoryRequest(_message.Message):
    __slots__ = ('parent', 'category_id', 'category')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    category_id: str
    category: GlossaryCategory

    def __init__(self, parent: _Optional[str]=..., category_id: _Optional[str]=..., category: _Optional[_Union[GlossaryCategory, _Mapping]]=...) -> None:
        ...

class UpdateGlossaryCategoryRequest(_message.Message):
    __slots__ = ('category', 'update_mask')
    CATEGORY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    category: GlossaryCategory
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, category: _Optional[_Union[GlossaryCategory, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteGlossaryCategoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetGlossaryCategoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGlossaryCategoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListGlossaryCategoriesResponse(_message.Message):
    __slots__ = ('categories', 'next_page_token', 'unreachable_locations')
    CATEGORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    categories: _containers.RepeatedCompositeFieldContainer[GlossaryCategory]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, categories: _Optional[_Iterable[_Union[GlossaryCategory, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...

class CreateGlossaryTermRequest(_message.Message):
    __slots__ = ('parent', 'term_id', 'term')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    TERM_ID_FIELD_NUMBER: _ClassVar[int]
    TERM_FIELD_NUMBER: _ClassVar[int]
    parent: str
    term_id: str
    term: GlossaryTerm

    def __init__(self, parent: _Optional[str]=..., term_id: _Optional[str]=..., term: _Optional[_Union[GlossaryTerm, _Mapping]]=...) -> None:
        ...

class UpdateGlossaryTermRequest(_message.Message):
    __slots__ = ('term', 'update_mask')
    TERM_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    term: GlossaryTerm
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, term: _Optional[_Union[GlossaryTerm, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteGlossaryTermRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetGlossaryTermRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListGlossaryTermsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListGlossaryTermsResponse(_message.Message):
    __slots__ = ('terms', 'next_page_token', 'unreachable_locations')
    TERMS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_LOCATIONS_FIELD_NUMBER: _ClassVar[int]
    terms: _containers.RepeatedCompositeFieldContainer[GlossaryTerm]
    next_page_token: str
    unreachable_locations: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, terms: _Optional[_Iterable[_Union[GlossaryTerm, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable_locations: _Optional[_Iterable[str]]=...) -> None:
        ...