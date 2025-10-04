from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class CustomClass(_message.Message):
    __slots__ = ('name', 'custom_class_id', 'items', 'kms_key_name', 'kms_key_version_name', 'uid', 'display_name', 'state', 'delete_time', 'expire_time', 'annotations', 'etag', 'reconciling')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[CustomClass.State]
        ACTIVE: _ClassVar[CustomClass.State]
        DELETED: _ClassVar[CustomClass.State]
    STATE_UNSPECIFIED: CustomClass.State
    ACTIVE: CustomClass.State
    DELETED: CustomClass.State

    class ClassItem(_message.Message):
        __slots__ = ('value',)
        VALUE_FIELD_NUMBER: _ClassVar[int]
        value: str

        def __init__(self, value: _Optional[str]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASS_ID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    name: str
    custom_class_id: str
    items: _containers.RepeatedCompositeFieldContainer[CustomClass.ClassItem]
    kms_key_name: str
    kms_key_version_name: str
    uid: str
    display_name: str
    state: CustomClass.State
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    reconciling: bool

    def __init__(self, name: _Optional[str]=..., custom_class_id: _Optional[str]=..., items: _Optional[_Iterable[_Union[CustomClass.ClassItem, _Mapping]]]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[CustomClass.State, str]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., reconciling: bool=...) -> None:
        ...

class PhraseSet(_message.Message):
    __slots__ = ('name', 'phrases', 'boost', 'kms_key_name', 'kms_key_version_name', 'uid', 'display_name', 'state', 'delete_time', 'expire_time', 'annotations', 'etag', 'reconciling')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PhraseSet.State]
        ACTIVE: _ClassVar[PhraseSet.State]
        DELETED: _ClassVar[PhraseSet.State]
    STATE_UNSPECIFIED: PhraseSet.State
    ACTIVE: PhraseSet.State
    DELETED: PhraseSet.State

    class Phrase(_message.Message):
        __slots__ = ('value', 'boost')
        VALUE_FIELD_NUMBER: _ClassVar[int]
        BOOST_FIELD_NUMBER: _ClassVar[int]
        value: str
        boost: float

        def __init__(self, value: _Optional[str]=..., boost: _Optional[float]=...) -> None:
            ...

    class AnnotationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    PHRASES_FIELD_NUMBER: _ClassVar[int]
    BOOST_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIME_FIELD_NUMBER: _ClassVar[int]
    EXPIRE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    RECONCILING_FIELD_NUMBER: _ClassVar[int]
    name: str
    phrases: _containers.RepeatedCompositeFieldContainer[PhraseSet.Phrase]
    boost: float
    kms_key_name: str
    kms_key_version_name: str
    uid: str
    display_name: str
    state: PhraseSet.State
    delete_time: _timestamp_pb2.Timestamp
    expire_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    reconciling: bool

    def __init__(self, name: _Optional[str]=..., phrases: _Optional[_Iterable[_Union[PhraseSet.Phrase, _Mapping]]]=..., boost: _Optional[float]=..., kms_key_name: _Optional[str]=..., kms_key_version_name: _Optional[str]=..., uid: _Optional[str]=..., display_name: _Optional[str]=..., state: _Optional[_Union[PhraseSet.State, str]]=..., delete_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., expire_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., reconciling: bool=...) -> None:
        ...

class SpeechAdaptation(_message.Message):
    __slots__ = ('phrase_sets', 'phrase_set_references', 'custom_classes', 'abnf_grammar')

    class ABNFGrammar(_message.Message):
        __slots__ = ('abnf_strings',)
        ABNF_STRINGS_FIELD_NUMBER: _ClassVar[int]
        abnf_strings: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, abnf_strings: _Optional[_Iterable[str]]=...) -> None:
            ...
    PHRASE_SETS_FIELD_NUMBER: _ClassVar[int]
    PHRASE_SET_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CLASSES_FIELD_NUMBER: _ClassVar[int]
    ABNF_GRAMMAR_FIELD_NUMBER: _ClassVar[int]
    phrase_sets: _containers.RepeatedCompositeFieldContainer[PhraseSet]
    phrase_set_references: _containers.RepeatedScalarFieldContainer[str]
    custom_classes: _containers.RepeatedCompositeFieldContainer[CustomClass]
    abnf_grammar: SpeechAdaptation.ABNFGrammar

    def __init__(self, phrase_sets: _Optional[_Iterable[_Union[PhraseSet, _Mapping]]]=..., phrase_set_references: _Optional[_Iterable[str]]=..., custom_classes: _Optional[_Iterable[_Union[CustomClass, _Mapping]]]=..., abnf_grammar: _Optional[_Union[SpeechAdaptation.ABNFGrammar, _Mapping]]=...) -> None:
        ...

class TranscriptNormalization(_message.Message):
    __slots__ = ('entries',)

    class Entry(_message.Message):
        __slots__ = ('search', 'replace', 'case_sensitive')
        SEARCH_FIELD_NUMBER: _ClassVar[int]
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        CASE_SENSITIVE_FIELD_NUMBER: _ClassVar[int]
        search: str
        replace: str
        case_sensitive: bool

        def __init__(self, search: _Optional[str]=..., replace: _Optional[str]=..., case_sensitive: bool=...) -> None:
            ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[TranscriptNormalization.Entry]

    def __init__(self, entries: _Optional[_Iterable[_Union[TranscriptNormalization.Entry, _Mapping]]]=...) -> None:
        ...