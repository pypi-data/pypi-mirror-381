from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import field_info_pb2 as _field_info_pb2
from google.api import resource_pb2 as _resource_pb2
from google.chat.v1 import user_pb2 as _user_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Reaction(_message.Message):
    __slots__ = ('name', 'user', 'emoji')
    NAME_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    name: str
    user: _user_pb2.User
    emoji: Emoji

    def __init__(self, name: _Optional[str]=..., user: _Optional[_Union[_user_pb2.User, _Mapping]]=..., emoji: _Optional[_Union[Emoji, _Mapping]]=...) -> None:
        ...

class Emoji(_message.Message):
    __slots__ = ('unicode', 'custom_emoji')
    UNICODE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_EMOJI_FIELD_NUMBER: _ClassVar[int]
    unicode: str
    custom_emoji: CustomEmoji

    def __init__(self, unicode: _Optional[str]=..., custom_emoji: _Optional[_Union[CustomEmoji, _Mapping]]=...) -> None:
        ...

class CustomEmoji(_message.Message):
    __slots__ = ('name', 'uid', 'emoji_name', 'temporary_image_uri', 'payload')

    class CustomEmojiPayload(_message.Message):
        __slots__ = ('file_content', 'filename')
        FILE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        FILENAME_FIELD_NUMBER: _ClassVar[int]
        file_content: bytes
        filename: str

        def __init__(self, file_content: _Optional[bytes]=..., filename: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    EMOJI_NAME_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    emoji_name: str
    temporary_image_uri: str
    payload: CustomEmoji.CustomEmojiPayload

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., emoji_name: _Optional[str]=..., temporary_image_uri: _Optional[str]=..., payload: _Optional[_Union[CustomEmoji.CustomEmojiPayload, _Mapping]]=...) -> None:
        ...

class EmojiReactionSummary(_message.Message):
    __slots__ = ('emoji', 'reaction_count')
    EMOJI_FIELD_NUMBER: _ClassVar[int]
    REACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
    emoji: Emoji
    reaction_count: int

    def __init__(self, emoji: _Optional[_Union[Emoji, _Mapping]]=..., reaction_count: _Optional[int]=...) -> None:
        ...

class CreateReactionRequest(_message.Message):
    __slots__ = ('parent', 'reaction')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REACTION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    reaction: Reaction

    def __init__(self, parent: _Optional[str]=..., reaction: _Optional[_Union[Reaction, _Mapping]]=...) -> None:
        ...

class ListReactionsRequest(_message.Message):
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

class ListReactionsResponse(_message.Message):
    __slots__ = ('reactions', 'next_page_token')
    REACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    reactions: _containers.RepeatedCompositeFieldContainer[Reaction]
    next_page_token: str

    def __init__(self, reactions: _Optional[_Iterable[_Union[Reaction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteReactionRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCustomEmojiRequest(_message.Message):
    __slots__ = ('custom_emoji',)
    CUSTOM_EMOJI_FIELD_NUMBER: _ClassVar[int]
    custom_emoji: CustomEmoji

    def __init__(self, custom_emoji: _Optional[_Union[CustomEmoji, _Mapping]]=...) -> None:
        ...

class GetCustomEmojiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCustomEmojisRequest(_message.Message):
    __slots__ = ('page_size', 'page_token', 'filter')
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    page_size: int
    page_token: str
    filter: str

    def __init__(self, page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListCustomEmojisResponse(_message.Message):
    __slots__ = ('custom_emojis', 'next_page_token')
    CUSTOM_EMOJIS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    custom_emojis: _containers.RepeatedCompositeFieldContainer[CustomEmoji]
    next_page_token: str

    def __init__(self, custom_emojis: _Optional[_Iterable[_Union[CustomEmoji, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DeleteCustomEmojiRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...