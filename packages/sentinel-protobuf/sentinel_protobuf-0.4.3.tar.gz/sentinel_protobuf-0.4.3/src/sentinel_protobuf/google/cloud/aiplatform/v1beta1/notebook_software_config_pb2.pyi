from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.aiplatform.v1beta1 import env_var_pb2 as _env_var_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PostStartupScriptConfig(_message.Message):
    __slots__ = ('post_startup_script', 'post_startup_script_url', 'post_startup_script_behavior')

    class PostStartupScriptBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED: _ClassVar[PostStartupScriptConfig.PostStartupScriptBehavior]
        RUN_ONCE: _ClassVar[PostStartupScriptConfig.PostStartupScriptBehavior]
        RUN_EVERY_START: _ClassVar[PostStartupScriptConfig.PostStartupScriptBehavior]
        DOWNLOAD_AND_RUN_EVERY_START: _ClassVar[PostStartupScriptConfig.PostStartupScriptBehavior]
    POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED: PostStartupScriptConfig.PostStartupScriptBehavior
    RUN_ONCE: PostStartupScriptConfig.PostStartupScriptBehavior
    RUN_EVERY_START: PostStartupScriptConfig.PostStartupScriptBehavior
    DOWNLOAD_AND_RUN_EVERY_START: PostStartupScriptConfig.PostStartupScriptBehavior
    POST_STARTUP_SCRIPT_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_URL_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
    post_startup_script: str
    post_startup_script_url: str
    post_startup_script_behavior: PostStartupScriptConfig.PostStartupScriptBehavior

    def __init__(self, post_startup_script: _Optional[str]=..., post_startup_script_url: _Optional[str]=..., post_startup_script_behavior: _Optional[_Union[PostStartupScriptConfig.PostStartupScriptBehavior, str]]=...) -> None:
        ...

class ColabImage(_message.Message):
    __slots__ = ('release_name', 'description')
    RELEASE_NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    release_name: str
    description: str

    def __init__(self, release_name: _Optional[str]=..., description: _Optional[str]=...) -> None:
        ...

class NotebookSoftwareConfig(_message.Message):
    __slots__ = ('colab_image', 'env', 'post_startup_script_config')
    COLAB_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ENV_FIELD_NUMBER: _ClassVar[int]
    POST_STARTUP_SCRIPT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    colab_image: ColabImage
    env: _containers.RepeatedCompositeFieldContainer[_env_var_pb2.EnvVar]
    post_startup_script_config: PostStartupScriptConfig

    def __init__(self, colab_image: _Optional[_Union[ColabImage, _Mapping]]=..., env: _Optional[_Iterable[_Union[_env_var_pb2.EnvVar, _Mapping]]]=..., post_startup_script_config: _Optional[_Union[PostStartupScriptConfig, _Mapping]]=...) -> None:
        ...