from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.orgpolicy.v2 import constraint_pb2 as _constraint_pb2
from google.cloud.orgpolicy.v2 import orgpolicy_pb2 as _orgpolicy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class PreviewState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PREVIEW_STATE_UNSPECIFIED: _ClassVar[PreviewState]
    PREVIEW_PENDING: _ClassVar[PreviewState]
    PREVIEW_RUNNING: _ClassVar[PreviewState]
    PREVIEW_SUCCEEDED: _ClassVar[PreviewState]
    PREVIEW_FAILED: _ClassVar[PreviewState]
PREVIEW_STATE_UNSPECIFIED: PreviewState
PREVIEW_PENDING: PreviewState
PREVIEW_RUNNING: PreviewState
PREVIEW_SUCCEEDED: PreviewState
PREVIEW_FAILED: PreviewState

class OrgPolicyViolationsPreview(_message.Message):
    __slots__ = ('name', 'state', 'overlay', 'violations_count', 'resource_counts', 'custom_constraints', 'create_time')

    class ResourceCounts(_message.Message):
        __slots__ = ('scanned', 'noncompliant', 'compliant', 'unenforced', 'errors')
        SCANNED_FIELD_NUMBER: _ClassVar[int]
        NONCOMPLIANT_FIELD_NUMBER: _ClassVar[int]
        COMPLIANT_FIELD_NUMBER: _ClassVar[int]
        UNENFORCED_FIELD_NUMBER: _ClassVar[int]
        ERRORS_FIELD_NUMBER: _ClassVar[int]
        scanned: int
        noncompliant: int
        compliant: int
        unenforced: int
        errors: int

        def __init__(self, scanned: _Optional[int]=..., noncompliant: _Optional[int]=..., compliant: _Optional[int]=..., unenforced: _Optional[int]=..., errors: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    OVERLAY_FIELD_NUMBER: _ClassVar[int]
    VIOLATIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_COUNTS_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    state: PreviewState
    overlay: OrgPolicyOverlay
    violations_count: int
    resource_counts: OrgPolicyViolationsPreview.ResourceCounts
    custom_constraints: _containers.RepeatedScalarFieldContainer[str]
    create_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., state: _Optional[_Union[PreviewState, str]]=..., overlay: _Optional[_Union[OrgPolicyOverlay, _Mapping]]=..., violations_count: _Optional[int]=..., resource_counts: _Optional[_Union[OrgPolicyViolationsPreview.ResourceCounts, _Mapping]]=..., custom_constraints: _Optional[_Iterable[str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class OrgPolicyViolation(_message.Message):
    __slots__ = ('name', 'resource', 'custom_constraint', 'error')
    NAME_FIELD_NUMBER: _ClassVar[int]
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    name: str
    resource: ResourceContext
    custom_constraint: _constraint_pb2.CustomConstraint
    error: _status_pb2.Status

    def __init__(self, name: _Optional[str]=..., resource: _Optional[_Union[ResourceContext, _Mapping]]=..., custom_constraint: _Optional[_Union[_constraint_pb2.CustomConstraint, _Mapping]]=..., error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class ResourceContext(_message.Message):
    __slots__ = ('resource', 'asset_type', 'ancestors')
    RESOURCE_FIELD_NUMBER: _ClassVar[int]
    ASSET_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANCESTORS_FIELD_NUMBER: _ClassVar[int]
    resource: str
    asset_type: str
    ancestors: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, resource: _Optional[str]=..., asset_type: _Optional[str]=..., ancestors: _Optional[_Iterable[str]]=...) -> None:
        ...

class OrgPolicyOverlay(_message.Message):
    __slots__ = ('policies', 'custom_constraints')

    class PolicyOverlay(_message.Message):
        __slots__ = ('policy_parent', 'policy')
        POLICY_PARENT_FIELD_NUMBER: _ClassVar[int]
        POLICY_FIELD_NUMBER: _ClassVar[int]
        policy_parent: str
        policy: _orgpolicy_pb2.Policy

        def __init__(self, policy_parent: _Optional[str]=..., policy: _Optional[_Union[_orgpolicy_pb2.Policy, _Mapping]]=...) -> None:
            ...

    class CustomConstraintOverlay(_message.Message):
        __slots__ = ('custom_constraint_parent', 'custom_constraint')
        CUSTOM_CONSTRAINT_PARENT_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_CONSTRAINT_FIELD_NUMBER: _ClassVar[int]
        custom_constraint_parent: str
        custom_constraint: _constraint_pb2.CustomConstraint

        def __init__(self, custom_constraint_parent: _Optional[str]=..., custom_constraint: _Optional[_Union[_constraint_pb2.CustomConstraint, _Mapping]]=...) -> None:
            ...
    POLICIES_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_CONSTRAINTS_FIELD_NUMBER: _ClassVar[int]
    policies: _containers.RepeatedCompositeFieldContainer[OrgPolicyOverlay.PolicyOverlay]
    custom_constraints: _containers.RepeatedCompositeFieldContainer[OrgPolicyOverlay.CustomConstraintOverlay]

    def __init__(self, policies: _Optional[_Iterable[_Union[OrgPolicyOverlay.PolicyOverlay, _Mapping]]]=..., custom_constraints: _Optional[_Iterable[_Union[OrgPolicyOverlay.CustomConstraintOverlay, _Mapping]]]=...) -> None:
        ...

class CreateOrgPolicyViolationsPreviewOperationMetadata(_message.Message):
    __slots__ = ('request_time', 'start_time', 'state', 'resources_found', 'resources_scanned', 'resources_pending')
    REQUEST_TIME_FIELD_NUMBER: _ClassVar[int]
    START_TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_FOUND_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_SCANNED_FIELD_NUMBER: _ClassVar[int]
    RESOURCES_PENDING_FIELD_NUMBER: _ClassVar[int]
    request_time: _timestamp_pb2.Timestamp
    start_time: _timestamp_pb2.Timestamp
    state: PreviewState
    resources_found: int
    resources_scanned: int
    resources_pending: int

    def __init__(self, request_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., start_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., state: _Optional[_Union[PreviewState, str]]=..., resources_found: _Optional[int]=..., resources_scanned: _Optional[int]=..., resources_pending: _Optional[int]=...) -> None:
        ...

class ListOrgPolicyViolationsPreviewsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOrgPolicyViolationsPreviewsResponse(_message.Message):
    __slots__ = ('org_policy_violations_previews', 'next_page_token')
    ORG_POLICY_VIOLATIONS_PREVIEWS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    org_policy_violations_previews: _containers.RepeatedCompositeFieldContainer[OrgPolicyViolationsPreview]
    next_page_token: str

    def __init__(self, org_policy_violations_previews: _Optional[_Iterable[_Union[OrgPolicyViolationsPreview, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetOrgPolicyViolationsPreviewRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateOrgPolicyViolationsPreviewRequest(_message.Message):
    __slots__ = ('parent', 'org_policy_violations_preview', 'org_policy_violations_preview_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_VIOLATIONS_PREVIEW_FIELD_NUMBER: _ClassVar[int]
    ORG_POLICY_VIOLATIONS_PREVIEW_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    org_policy_violations_preview: OrgPolicyViolationsPreview
    org_policy_violations_preview_id: str

    def __init__(self, parent: _Optional[str]=..., org_policy_violations_preview: _Optional[_Union[OrgPolicyViolationsPreview, _Mapping]]=..., org_policy_violations_preview_id: _Optional[str]=...) -> None:
        ...

class ListOrgPolicyViolationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOrgPolicyViolationsResponse(_message.Message):
    __slots__ = ('org_policy_violations', 'next_page_token')
    ORG_POLICY_VIOLATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    org_policy_violations: _containers.RepeatedCompositeFieldContainer[OrgPolicyViolation]
    next_page_token: str

    def __init__(self, org_policy_violations: _Optional[_Iterable[_Union[OrgPolicyViolation, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...