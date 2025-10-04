from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PSCAutomationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PSC_AUTOMATION_STATE_UNSPECIFIED: _ClassVar[PSCAutomationState]
    PSC_AUTOMATION_STATE_SUCCESSFUL: _ClassVar[PSCAutomationState]
    PSC_AUTOMATION_STATE_FAILED: _ClassVar[PSCAutomationState]
PSC_AUTOMATION_STATE_UNSPECIFIED: PSCAutomationState
PSC_AUTOMATION_STATE_SUCCESSFUL: PSCAutomationState
PSC_AUTOMATION_STATE_FAILED: PSCAutomationState

class PSCAutomationConfig(_message.Message):
    __slots__ = ('project_id', 'network', 'ip_address', 'forwarding_rule', 'state', 'error_message')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    IP_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    FORWARDING_RULE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    ERROR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    network: str
    ip_address: str
    forwarding_rule: str
    state: PSCAutomationState
    error_message: str

    def __init__(self, project_id: _Optional[str]=..., network: _Optional[str]=..., ip_address: _Optional[str]=..., forwarding_rule: _Optional[str]=..., state: _Optional[_Union[PSCAutomationState, str]]=..., error_message: _Optional[str]=...) -> None:
        ...

class PrivateServiceConnectConfig(_message.Message):
    __slots__ = ('enable_private_service_connect', 'project_allowlist', 'psc_automation_configs', 'service_attachment')
    ENABLE_PRIVATE_SERVICE_CONNECT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_ALLOWLIST_FIELD_NUMBER: _ClassVar[int]
    PSC_AUTOMATION_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    enable_private_service_connect: bool
    project_allowlist: _containers.RepeatedScalarFieldContainer[str]
    psc_automation_configs: _containers.RepeatedCompositeFieldContainer[PSCAutomationConfig]
    service_attachment: str

    def __init__(self, enable_private_service_connect: bool=..., project_allowlist: _Optional[_Iterable[str]]=..., psc_automation_configs: _Optional[_Iterable[_Union[PSCAutomationConfig, _Mapping]]]=..., service_attachment: _Optional[str]=...) -> None:
        ...

class PscAutomatedEndpoints(_message.Message):
    __slots__ = ('project_id', 'network', 'match_address')
    PROJECT_ID_FIELD_NUMBER: _ClassVar[int]
    NETWORK_FIELD_NUMBER: _ClassVar[int]
    MATCH_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    project_id: str
    network: str
    match_address: str

    def __init__(self, project_id: _Optional[str]=..., network: _Optional[str]=..., match_address: _Optional[str]=...) -> None:
        ...

class PscInterfaceConfig(_message.Message):
    __slots__ = ('network_attachment', 'dns_peering_configs')
    NETWORK_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    DNS_PEERING_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    network_attachment: str
    dns_peering_configs: _containers.RepeatedCompositeFieldContainer[DnsPeeringConfig]

    def __init__(self, network_attachment: _Optional[str]=..., dns_peering_configs: _Optional[_Iterable[_Union[DnsPeeringConfig, _Mapping]]]=...) -> None:
        ...

class DnsPeeringConfig(_message.Message):
    __slots__ = ('domain', 'target_project', 'target_network')
    DOMAIN_FIELD_NUMBER: _ClassVar[int]
    TARGET_PROJECT_FIELD_NUMBER: _ClassVar[int]
    TARGET_NETWORK_FIELD_NUMBER: _ClassVar[int]
    domain: str
    target_project: str
    target_network: str

    def __init__(self, domain: _Optional[str]=..., target_project: _Optional[str]=..., target_network: _Optional[str]=...) -> None:
        ...