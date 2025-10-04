from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Watchlist(_message.Message):
    __slots__ = ('name', 'display_name', 'description', 'multiplying_factor', 'entity_population_mechanism', 'entity_count', 'create_time', 'update_time', 'watchlist_user_preferences')

    class EntityPopulationMechanism(_message.Message):
        __slots__ = ('manual',)

        class Manual(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        MANUAL_FIELD_NUMBER: _ClassVar[int]
        manual: Watchlist.EntityPopulationMechanism.Manual

        def __init__(self, manual: _Optional[_Union[Watchlist.EntityPopulationMechanism.Manual, _Mapping]]=...) -> None:
            ...

    class EntityCount(_message.Message):
        __slots__ = ('user', 'asset')
        USER_FIELD_NUMBER: _ClassVar[int]
        ASSET_FIELD_NUMBER: _ClassVar[int]
        user: int
        asset: int

        def __init__(self, user: _Optional[int]=..., asset: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    MULTIPLYING_FACTOR_FIELD_NUMBER: _ClassVar[int]
    ENTITY_POPULATION_MECHANISM_FIELD_NUMBER: _ClassVar[int]
    ENTITY_COUNT_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    WATCHLIST_USER_PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    display_name: str
    description: str
    multiplying_factor: float
    entity_population_mechanism: Watchlist.EntityPopulationMechanism
    entity_count: Watchlist.EntityCount
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    watchlist_user_preferences: WatchlistUserPreferences

    def __init__(self, name: _Optional[str]=..., display_name: _Optional[str]=..., description: _Optional[str]=..., multiplying_factor: _Optional[float]=..., entity_population_mechanism: _Optional[_Union[Watchlist.EntityPopulationMechanism, _Mapping]]=..., entity_count: _Optional[_Union[Watchlist.EntityCount, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., watchlist_user_preferences: _Optional[_Union[WatchlistUserPreferences, _Mapping]]=...) -> None:
        ...

class WatchlistUserPreferences(_message.Message):
    __slots__ = ('pinned',)
    PINNED_FIELD_NUMBER: _ClassVar[int]
    pinned: bool

    def __init__(self, pinned: bool=...) -> None:
        ...

class GetWatchlistRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListWatchlistsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListWatchlistsResponse(_message.Message):
    __slots__ = ('watchlists', 'next_page_token')
    WATCHLISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    watchlists: _containers.RepeatedCompositeFieldContainer[Watchlist]
    next_page_token: str

    def __init__(self, watchlists: _Optional[_Iterable[_Union[Watchlist, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateWatchlistRequest(_message.Message):
    __slots__ = ('parent', 'watchlist_id', 'watchlist')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WATCHLIST_ID_FIELD_NUMBER: _ClassVar[int]
    WATCHLIST_FIELD_NUMBER: _ClassVar[int]
    parent: str
    watchlist_id: str
    watchlist: Watchlist

    def __init__(self, parent: _Optional[str]=..., watchlist_id: _Optional[str]=..., watchlist: _Optional[_Union[Watchlist, _Mapping]]=...) -> None:
        ...

class UpdateWatchlistRequest(_message.Message):
    __slots__ = ('watchlist', 'update_mask')
    WATCHLIST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    watchlist: Watchlist
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, watchlist: _Optional[_Union[Watchlist, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteWatchlistRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...