from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class InsightsKnowledgeGraphEntityCapabilitiesEnum(_message.Message):
    __slots__ = ()

    class InsightsKnowledgeGraphEntityCapabilities(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
        UNKNOWN: _ClassVar[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
        CONTENT_TRENDING_INSIGHTS: _ClassVar[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
        CREATOR_ATTRIBUTE: _ClassVar[InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities]
    UNSPECIFIED: InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities
    UNKNOWN: InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities
    CONTENT_TRENDING_INSIGHTS: InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities
    CREATOR_ATTRIBUTE: InsightsKnowledgeGraphEntityCapabilitiesEnum.InsightsKnowledgeGraphEntityCapabilities

    def __init__(self) -> None:
        ...