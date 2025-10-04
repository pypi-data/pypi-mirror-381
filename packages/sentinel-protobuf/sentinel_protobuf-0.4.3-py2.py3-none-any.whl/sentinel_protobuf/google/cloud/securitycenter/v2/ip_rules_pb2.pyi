from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class IpRules(_message.Message):
    __slots__ = ('direction', 'allowed', 'denied', 'source_ip_ranges', 'destination_ip_ranges', 'exposed_services')

    class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DIRECTION_UNSPECIFIED: _ClassVar[IpRules.Direction]
        INGRESS: _ClassVar[IpRules.Direction]
        EGRESS: _ClassVar[IpRules.Direction]
    DIRECTION_UNSPECIFIED: IpRules.Direction
    INGRESS: IpRules.Direction
    EGRESS: IpRules.Direction
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    ALLOWED_FIELD_NUMBER: _ClassVar[int]
    DENIED_FIELD_NUMBER: _ClassVar[int]
    SOURCE_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_IP_RANGES_FIELD_NUMBER: _ClassVar[int]
    EXPOSED_SERVICES_FIELD_NUMBER: _ClassVar[int]
    direction: IpRules.Direction
    allowed: Allowed
    denied: Denied
    source_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    destination_ip_ranges: _containers.RepeatedScalarFieldContainer[str]
    exposed_services: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, direction: _Optional[_Union[IpRules.Direction, str]]=..., allowed: _Optional[_Union[Allowed, _Mapping]]=..., denied: _Optional[_Union[Denied, _Mapping]]=..., source_ip_ranges: _Optional[_Iterable[str]]=..., destination_ip_ranges: _Optional[_Iterable[str]]=..., exposed_services: _Optional[_Iterable[str]]=...) -> None:
        ...

class IpRule(_message.Message):
    __slots__ = ('protocol', 'port_ranges')

    class PortRange(_message.Message):
        __slots__ = ('min', 'max')
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        min: int
        max: int

        def __init__(self, min: _Optional[int]=..., max: _Optional[int]=...) -> None:
            ...
    PROTOCOL_FIELD_NUMBER: _ClassVar[int]
    PORT_RANGES_FIELD_NUMBER: _ClassVar[int]
    protocol: str
    port_ranges: _containers.RepeatedCompositeFieldContainer[IpRule.PortRange]

    def __init__(self, protocol: _Optional[str]=..., port_ranges: _Optional[_Iterable[_Union[IpRule.PortRange, _Mapping]]]=...) -> None:
        ...

class Allowed(_message.Message):
    __slots__ = ('ip_rules',)
    IP_RULES_FIELD_NUMBER: _ClassVar[int]
    ip_rules: _containers.RepeatedCompositeFieldContainer[IpRule]

    def __init__(self, ip_rules: _Optional[_Iterable[_Union[IpRule, _Mapping]]]=...) -> None:
        ...

class Denied(_message.Message):
    __slots__ = ('ip_rules',)
    IP_RULES_FIELD_NUMBER: _ClassVar[int]
    ip_rules: _containers.RepeatedCompositeFieldContainer[IpRule]

    def __init__(self, ip_rules: _Optional[_Iterable[_Union[IpRule, _Mapping]]]=...) -> None:
        ...