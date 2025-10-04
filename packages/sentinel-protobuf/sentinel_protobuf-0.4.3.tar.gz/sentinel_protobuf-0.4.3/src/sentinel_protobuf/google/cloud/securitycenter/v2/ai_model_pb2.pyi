from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AiModel(_message.Message):
    __slots__ = ('name', 'domain', 'library', 'location', 'publisher', 'deployment_platform', 'display_name')

    class DeploymentPlatform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DEPLOYMENT_PLATFORM_UNSPECIFIED: _ClassVar[AiModel.DeploymentPlatform]
        VERTEX_AI: _ClassVar[AiModel.DeploymentPlatform]
        GKE: _ClassVar[AiModel.DeploymentPlatform]
        GCE: _ClassVar[AiModel.DeploymentPlatform]
        FINE_TUNED_MODEL: _ClassVar[AiModel.DeploymentPlatform]
    DEPLOYMENT_PLATFORM_UNSPECIFIED: AiModel.DeploymentPlatform
    VERTEX_AI: AiModel.DeploymentPlatform
    GKE: AiModel.DeploymentPlatform
    GCE: AiModel.DeploymentPlatform
    FINE_TUNED_MODEL: AiModel.DeploymentPlatform
    NAME_FIELD_NUMBER: _ClassVar[int]
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    PUBLISHER_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_PLATFORM_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    domain: str
    library: str
    location: str
    publisher: str
    deployment_platform: AiModel.DeploymentPlatform
    display_name: str

    def __init__(self, name: _Optional[str]=..., domain: _Optional[str]=..., library: _Optional[str]=..., location: _Optional[str]=..., publisher: _Optional[str]=..., deployment_platform: _Optional[_Union[AiModel.DeploymentPlatform, str]]=..., display_name: _Optional[str]=...) -> None:
        ...