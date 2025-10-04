from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ThreatType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    THREAT_TYPE_UNSPECIFIED: _ClassVar[ThreatType]
    MALWARE: _ClassVar[ThreatType]
    SOCIAL_ENGINEERING: _ClassVar[ThreatType]
    UNWANTED_SOFTWARE: _ClassVar[ThreatType]
    POTENTIALLY_HARMFUL_APPLICATION: _ClassVar[ThreatType]

class LikelySafeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    LIKELY_SAFE_TYPE_UNSPECIFIED: _ClassVar[LikelySafeType]
    GENERAL_BROWSING: _ClassVar[LikelySafeType]
    CSD: _ClassVar[LikelySafeType]
    DOWNLOAD: _ClassVar[LikelySafeType]

class ThreatAttribute(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    THREAT_ATTRIBUTE_UNSPECIFIED: _ClassVar[ThreatAttribute]
    CANARY: _ClassVar[ThreatAttribute]
    FRAME_ONLY: _ClassVar[ThreatAttribute]
THREAT_TYPE_UNSPECIFIED: ThreatType
MALWARE: ThreatType
SOCIAL_ENGINEERING: ThreatType
UNWANTED_SOFTWARE: ThreatType
POTENTIALLY_HARMFUL_APPLICATION: ThreatType
LIKELY_SAFE_TYPE_UNSPECIFIED: LikelySafeType
GENERAL_BROWSING: LikelySafeType
CSD: LikelySafeType
DOWNLOAD: LikelySafeType
THREAT_ATTRIBUTE_UNSPECIFIED: ThreatAttribute
CANARY: ThreatAttribute
FRAME_ONLY: ThreatAttribute

class SearchHashesRequest(_message.Message):
    __slots__ = ('hash_prefixes', 'filter')
    HASH_PREFIXES_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    hash_prefixes: _containers.RepeatedScalarFieldContainer[bytes]
    filter: str

    def __init__(self, hash_prefixes: _Optional[_Iterable[bytes]]=..., filter: _Optional[str]=...) -> None:
        ...

class SearchHashesResponse(_message.Message):
    __slots__ = ('full_hashes', 'cache_duration')
    FULL_HASHES_FIELD_NUMBER: _ClassVar[int]
    CACHE_DURATION_FIELD_NUMBER: _ClassVar[int]
    full_hashes: _containers.RepeatedCompositeFieldContainer[FullHash]
    cache_duration: _duration_pb2.Duration

    def __init__(self, full_hashes: _Optional[_Iterable[_Union[FullHash, _Mapping]]]=..., cache_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=...) -> None:
        ...

class FullHash(_message.Message):
    __slots__ = ('full_hash', 'full_hash_details')

    class FullHashDetail(_message.Message):
        __slots__ = ('threat_type', 'attributes')
        THREAT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
        threat_type: ThreatType
        attributes: _containers.RepeatedScalarFieldContainer[ThreatAttribute]

        def __init__(self, threat_type: _Optional[_Union[ThreatType, str]]=..., attributes: _Optional[_Iterable[_Union[ThreatAttribute, str]]]=...) -> None:
            ...
    FULL_HASH_FIELD_NUMBER: _ClassVar[int]
    FULL_HASH_DETAILS_FIELD_NUMBER: _ClassVar[int]
    full_hash: bytes
    full_hash_details: _containers.RepeatedCompositeFieldContainer[FullHash.FullHashDetail]

    def __init__(self, full_hash: _Optional[bytes]=..., full_hash_details: _Optional[_Iterable[_Union[FullHash.FullHashDetail, _Mapping]]]=...) -> None:
        ...

class GetHashListRequest(_message.Message):
    __slots__ = ('name', 'version', 'size_constraints')
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SIZE_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    version: bytes
    size_constraints: SizeConstraints

    def __init__(self, name: _Optional[str]=..., version: _Optional[bytes]=..., size_constraints: _Optional[_Union[SizeConstraints, _Mapping]]=...) -> None:
        ...

class SizeConstraints(_message.Message):
    __slots__ = ('max_update_entries', 'max_database_entries')
    MAX_UPDATE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    MAX_DATABASE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    max_update_entries: int
    max_database_entries: int

    def __init__(self, max_update_entries: _Optional[int]=..., max_database_entries: _Optional[int]=...) -> None:
        ...

class RiceDeltaEncoded32Bit(_message.Message):
    __slots__ = ('first_value', 'rice_parameter', 'entries_count', 'encoded_data')
    FIRST_VALUE_FIELD_NUMBER: _ClassVar[int]
    RICE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DATA_FIELD_NUMBER: _ClassVar[int]
    first_value: int
    rice_parameter: int
    entries_count: int
    encoded_data: bytes

    def __init__(self, first_value: _Optional[int]=..., rice_parameter: _Optional[int]=..., entries_count: _Optional[int]=..., encoded_data: _Optional[bytes]=...) -> None:
        ...

class RiceDeltaEncoded64Bit(_message.Message):
    __slots__ = ('first_value', 'rice_parameter', 'entries_count', 'encoded_data')
    FIRST_VALUE_FIELD_NUMBER: _ClassVar[int]
    RICE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DATA_FIELD_NUMBER: _ClassVar[int]
    first_value: int
    rice_parameter: int
    entries_count: int
    encoded_data: bytes

    def __init__(self, first_value: _Optional[int]=..., rice_parameter: _Optional[int]=..., entries_count: _Optional[int]=..., encoded_data: _Optional[bytes]=...) -> None:
        ...

class RiceDeltaEncoded128Bit(_message.Message):
    __slots__ = ('first_value_hi', 'first_value_lo', 'rice_parameter', 'entries_count', 'encoded_data')
    FIRST_VALUE_HI_FIELD_NUMBER: _ClassVar[int]
    FIRST_VALUE_LO_FIELD_NUMBER: _ClassVar[int]
    RICE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DATA_FIELD_NUMBER: _ClassVar[int]
    first_value_hi: int
    first_value_lo: int
    rice_parameter: int
    entries_count: int
    encoded_data: bytes

    def __init__(self, first_value_hi: _Optional[int]=..., first_value_lo: _Optional[int]=..., rice_parameter: _Optional[int]=..., entries_count: _Optional[int]=..., encoded_data: _Optional[bytes]=...) -> None:
        ...

class RiceDeltaEncoded256Bit(_message.Message):
    __slots__ = ('first_value_first_part', 'first_value_second_part', 'first_value_third_part', 'first_value_fourth_part', 'rice_parameter', 'entries_count', 'encoded_data')
    FIRST_VALUE_FIRST_PART_FIELD_NUMBER: _ClassVar[int]
    FIRST_VALUE_SECOND_PART_FIELD_NUMBER: _ClassVar[int]
    FIRST_VALUE_THIRD_PART_FIELD_NUMBER: _ClassVar[int]
    FIRST_VALUE_FOURTH_PART_FIELD_NUMBER: _ClassVar[int]
    RICE_PARAMETER_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_COUNT_FIELD_NUMBER: _ClassVar[int]
    ENCODED_DATA_FIELD_NUMBER: _ClassVar[int]
    first_value_first_part: int
    first_value_second_part: int
    first_value_third_part: int
    first_value_fourth_part: int
    rice_parameter: int
    entries_count: int
    encoded_data: bytes

    def __init__(self, first_value_first_part: _Optional[int]=..., first_value_second_part: _Optional[int]=..., first_value_third_part: _Optional[int]=..., first_value_fourth_part: _Optional[int]=..., rice_parameter: _Optional[int]=..., entries_count: _Optional[int]=..., encoded_data: _Optional[bytes]=...) -> None:
        ...

class HashListMetadata(_message.Message):
    __slots__ = ('threat_types', 'likely_safe_types', 'description', 'hash_length')

    class HashLength(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        HASH_LENGTH_UNSPECIFIED: _ClassVar[HashListMetadata.HashLength]
        FOUR_BYTES: _ClassVar[HashListMetadata.HashLength]
        EIGHT_BYTES: _ClassVar[HashListMetadata.HashLength]
        SIXTEEN_BYTES: _ClassVar[HashListMetadata.HashLength]
        THIRTY_TWO_BYTES: _ClassVar[HashListMetadata.HashLength]
    HASH_LENGTH_UNSPECIFIED: HashListMetadata.HashLength
    FOUR_BYTES: HashListMetadata.HashLength
    EIGHT_BYTES: HashListMetadata.HashLength
    SIXTEEN_BYTES: HashListMetadata.HashLength
    THIRTY_TWO_BYTES: HashListMetadata.HashLength
    THREAT_TYPES_FIELD_NUMBER: _ClassVar[int]
    LIKELY_SAFE_TYPES_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    HASH_LENGTH_FIELD_NUMBER: _ClassVar[int]
    threat_types: _containers.RepeatedScalarFieldContainer[ThreatType]
    likely_safe_types: _containers.RepeatedScalarFieldContainer[LikelySafeType]
    description: str
    hash_length: HashListMetadata.HashLength

    def __init__(self, threat_types: _Optional[_Iterable[_Union[ThreatType, str]]]=..., likely_safe_types: _Optional[_Iterable[_Union[LikelySafeType, str]]]=..., description: _Optional[str]=..., hash_length: _Optional[_Union[HashListMetadata.HashLength, str]]=...) -> None:
        ...

class HashList(_message.Message):
    __slots__ = ('additions_four_bytes', 'additions_eight_bytes', 'additions_sixteen_bytes', 'additions_thirty_two_bytes', 'name', 'version', 'partial_update', 'compressed_removals', 'minimum_wait_duration', 'sha256_checksum', 'metadata')
    ADDITIONS_FOUR_BYTES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_EIGHT_BYTES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_SIXTEEN_BYTES_FIELD_NUMBER: _ClassVar[int]
    ADDITIONS_THIRTY_TWO_BYTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_UPDATE_FIELD_NUMBER: _ClassVar[int]
    COMPRESSED_REMOVALS_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_WAIT_DURATION_FIELD_NUMBER: _ClassVar[int]
    SHA256_CHECKSUM_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    additions_four_bytes: RiceDeltaEncoded32Bit
    additions_eight_bytes: RiceDeltaEncoded64Bit
    additions_sixteen_bytes: RiceDeltaEncoded128Bit
    additions_thirty_two_bytes: RiceDeltaEncoded256Bit
    name: str
    version: bytes
    partial_update: bool
    compressed_removals: RiceDeltaEncoded32Bit
    minimum_wait_duration: _duration_pb2.Duration
    sha256_checksum: bytes
    metadata: HashListMetadata

    def __init__(self, additions_four_bytes: _Optional[_Union[RiceDeltaEncoded32Bit, _Mapping]]=..., additions_eight_bytes: _Optional[_Union[RiceDeltaEncoded64Bit, _Mapping]]=..., additions_sixteen_bytes: _Optional[_Union[RiceDeltaEncoded128Bit, _Mapping]]=..., additions_thirty_two_bytes: _Optional[_Union[RiceDeltaEncoded256Bit, _Mapping]]=..., name: _Optional[str]=..., version: _Optional[bytes]=..., partial_update: bool=..., compressed_removals: _Optional[_Union[RiceDeltaEncoded32Bit, _Mapping]]=..., minimum_wait_duration: _Optional[_Union[_duration_pb2.Duration, _Mapping]]=..., sha256_checksum: _Optional[bytes]=..., metadata: _Optional[_Union[HashListMetadata, _Mapping]]=...) -> None:
        ...

class BatchGetHashListsRequest(_message.Message):
    __slots__ = ('names', 'version', 'size_constraints')
    NAMES_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    SIZE_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    names: _containers.RepeatedScalarFieldContainer[str]
    version: _containers.RepeatedScalarFieldContainer[bytes]
    size_constraints: SizeConstraints

    def __init__(self, names: _Optional[_Iterable[str]]=..., version: _Optional[_Iterable[bytes]]=..., size_constraints: _Optional[_Union[SizeConstraints, _Mapping]]=...) -> None:
        ...

class BatchGetHashListsResponse(_message.Message):
    __slots__ = ('hash_lists',)
    HASH_LISTS_FIELD_NUMBER: _ClassVar[int]
    hash_lists: _containers.RepeatedCompositeFieldContainer[HashList]

    def __init__(self, hash_lists: _Optional[_Iterable[_Union[HashList, _Mapping]]]=...) -> None:
        ...

class ListHashListsRequest(_message.Message):
    __slots__ = ('page_size', 'page_token')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListHashListsResponse(_message.Message):
    __slots__ = ('hash_lists', 'next_page_token')
    HASH_LISTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hash_lists: _containers.RepeatedCompositeFieldContainer[HashList]
    next_page_token: str

    def __init__(self, hash_lists: _Optional[_Iterable[_Union[HashList, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...