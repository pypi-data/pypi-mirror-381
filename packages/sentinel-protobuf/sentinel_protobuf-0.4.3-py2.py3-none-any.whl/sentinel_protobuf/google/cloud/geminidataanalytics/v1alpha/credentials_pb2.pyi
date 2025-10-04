from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Credentials(_message.Message):
    __slots__ = ('oauth',)
    OAUTH_FIELD_NUMBER: _ClassVar[int]
    oauth: OAuthCredentials

    def __init__(self, oauth: _Optional[_Union[OAuthCredentials, _Mapping]]=...) -> None:
        ...

class OAuthCredentials(_message.Message):
    __slots__ = ('secret', 'token')

    class SecretBased(_message.Message):
        __slots__ = ('client_id', 'client_secret')
        CLIENT_ID_FIELD_NUMBER: _ClassVar[int]
        CLIENT_SECRET_FIELD_NUMBER: _ClassVar[int]
        client_id: str
        client_secret: str

        def __init__(self, client_id: _Optional[str]=..., client_secret: _Optional[str]=...) -> None:
            ...

    class TokenBased(_message.Message):
        __slots__ = ('access_token',)
        ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
        access_token: str

        def __init__(self, access_token: _Optional[str]=...) -> None:
            ...
    SECRET_FIELD_NUMBER: _ClassVar[int]
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    secret: OAuthCredentials.SecretBased
    token: OAuthCredentials.TokenBased

    def __init__(self, secret: _Optional[_Union[OAuthCredentials.SecretBased, _Mapping]]=..., token: _Optional[_Union[OAuthCredentials.TokenBased, _Mapping]]=...) -> None:
        ...