from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import content_pb2 as _content_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class ContentsExample(_message.Message):
    __slots__ = ('contents', 'expected_contents')

    class ExpectedContent(_message.Message):
        __slots__ = ('content',)
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        content: _content_pb2.Content

        def __init__(self, content: _Optional[_Union[_content_pb2.Content, _Mapping]]=...) -> None:
            ...
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    EXPECTED_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    contents: _containers.RepeatedCompositeFieldContainer[_content_pb2.Content]
    expected_contents: _containers.RepeatedCompositeFieldContainer[ContentsExample.ExpectedContent]

    def __init__(self, contents: _Optional[_Iterable[_Union[_content_pb2.Content, _Mapping]]]=..., expected_contents: _Optional[_Iterable[_Union[ContentsExample.ExpectedContent, _Mapping]]]=...) -> None:
        ...

class StoredContentsExample(_message.Message):
    __slots__ = ('search_key', 'contents_example', 'search_key_generation_method')

    class SearchKeyGenerationMethod(_message.Message):
        __slots__ = ('last_entry',)

        class LastEntry(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        LAST_ENTRY_FIELD_NUMBER: _ClassVar[int]
        last_entry: StoredContentsExample.SearchKeyGenerationMethod.LastEntry

        def __init__(self, last_entry: _Optional[_Union[StoredContentsExample.SearchKeyGenerationMethod.LastEntry, _Mapping]]=...) -> None:
            ...
    SEARCH_KEY_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_EXAMPLE_FIELD_NUMBER: _ClassVar[int]
    SEARCH_KEY_GENERATION_METHOD_FIELD_NUMBER: _ClassVar[int]
    search_key: str
    contents_example: ContentsExample
    search_key_generation_method: StoredContentsExample.SearchKeyGenerationMethod

    def __init__(self, search_key: _Optional[str]=..., contents_example: _Optional[_Union[ContentsExample, _Mapping]]=..., search_key_generation_method: _Optional[_Union[StoredContentsExample.SearchKeyGenerationMethod, _Mapping]]=...) -> None:
        ...