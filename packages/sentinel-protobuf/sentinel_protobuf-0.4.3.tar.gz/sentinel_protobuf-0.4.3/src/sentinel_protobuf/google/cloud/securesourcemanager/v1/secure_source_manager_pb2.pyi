from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.iam.v1 import iam_policy_pb2 as _iam_policy_pb2
from google.iam.v1 import policy_pb2 as _policy_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class Instance(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'labels', 'private_config', 'state', 'state_note', 'kms_key', 'host_config', 'workforce_identity_federation_config')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Instance.State]
        CREATING: _ClassVar[Instance.State]
        ACTIVE: _ClassVar[Instance.State]
        DELETING: _ClassVar[Instance.State]
        PAUSED: _ClassVar[Instance.State]
        UNKNOWN: _ClassVar[Instance.State]
    STATE_UNSPECIFIED: Instance.State
    CREATING: Instance.State
    ACTIVE: Instance.State
    DELETING: Instance.State
    PAUSED: Instance.State
    UNKNOWN: Instance.State

    class StateNote(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_NOTE_UNSPECIFIED: _ClassVar[Instance.StateNote]
        PAUSED_CMEK_UNAVAILABLE: _ClassVar[Instance.StateNote]
        INSTANCE_RESUMING: _ClassVar[Instance.StateNote]
    STATE_NOTE_UNSPECIFIED: Instance.StateNote
    PAUSED_CMEK_UNAVAILABLE: Instance.StateNote
    INSTANCE_RESUMING: Instance.StateNote

    class HostConfig(_message.Message):
        __slots__ = ('html', 'api', 'git_http', 'git_ssh')
        HTML_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        GIT_HTTP_FIELD_NUMBER: _ClassVar[int]
        GIT_SSH_FIELD_NUMBER: _ClassVar[int]
        html: str
        api: str
        git_http: str
        git_ssh: str

        def __init__(self, html: _Optional[str]=..., api: _Optional[str]=..., git_http: _Optional[str]=..., git_ssh: _Optional[str]=...) -> None:
            ...

    class PrivateConfig(_message.Message):
        __slots__ = ('is_private', 'ca_pool', 'http_service_attachment', 'ssh_service_attachment', 'psc_allowed_projects')
        IS_PRIVATE_FIELD_NUMBER: _ClassVar[int]
        CA_POOL_FIELD_NUMBER: _ClassVar[int]
        HTTP_SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        SSH_SERVICE_ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
        PSC_ALLOWED_PROJECTS_FIELD_NUMBER: _ClassVar[int]
        is_private: bool
        ca_pool: str
        http_service_attachment: str
        ssh_service_attachment: str
        psc_allowed_projects: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, is_private: bool=..., ca_pool: _Optional[str]=..., http_service_attachment: _Optional[str]=..., ssh_service_attachment: _Optional[str]=..., psc_allowed_projects: _Optional[_Iterable[str]]=...) -> None:
            ...

    class WorkforceIdentityFederationConfig(_message.Message):
        __slots__ = ('enabled',)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool

        def __init__(self, enabled: bool=...) -> None:
            ...

    class LabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    PRIVATE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    STATE_NOTE_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_FIELD_NUMBER: _ClassVar[int]
    HOST_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKFORCE_IDENTITY_FEDERATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    labels: _containers.ScalarMap[str, str]
    private_config: Instance.PrivateConfig
    state: Instance.State
    state_note: Instance.StateNote
    kms_key: str
    host_config: Instance.HostConfig
    workforce_identity_federation_config: Instance.WorkforceIdentityFederationConfig

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., private_config: _Optional[_Union[Instance.PrivateConfig, _Mapping]]=..., state: _Optional[_Union[Instance.State, str]]=..., state_note: _Optional[_Union[Instance.StateNote, str]]=..., kms_key: _Optional[str]=..., host_config: _Optional[_Union[Instance.HostConfig, _Mapping]]=..., workforce_identity_federation_config: _Optional[_Union[Instance.WorkforceIdentityFederationConfig, _Mapping]]=...) -> None:
        ...

class Repository(_message.Message):
    __slots__ = ('name', 'description', 'instance', 'uid', 'create_time', 'update_time', 'etag', 'uris', 'initial_config')

    class URIs(_message.Message):
        __slots__ = ('html', 'git_https', 'api')
        HTML_FIELD_NUMBER: _ClassVar[int]
        GIT_HTTPS_FIELD_NUMBER: _ClassVar[int]
        API_FIELD_NUMBER: _ClassVar[int]
        html: str
        git_https: str
        api: str

        def __init__(self, html: _Optional[str]=..., git_https: _Optional[str]=..., api: _Optional[str]=...) -> None:
            ...

    class InitialConfig(_message.Message):
        __slots__ = ('default_branch', 'gitignores', 'license', 'readme')
        DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
        GITIGNORES_FIELD_NUMBER: _ClassVar[int]
        LICENSE_FIELD_NUMBER: _ClassVar[int]
        README_FIELD_NUMBER: _ClassVar[int]
        default_branch: str
        gitignores: _containers.RepeatedScalarFieldContainer[str]
        license: str
        readme: str

        def __init__(self, default_branch: _Optional[str]=..., gitignores: _Optional[_Iterable[str]]=..., license: _Optional[str]=..., readme: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    URIS_FIELD_NUMBER: _ClassVar[int]
    INITIAL_CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    description: str
    instance: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    uris: Repository.URIs
    initial_config: Repository.InitialConfig

    def __init__(self, name: _Optional[str]=..., description: _Optional[str]=..., instance: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., uris: _Optional[_Union[Repository.URIs, _Mapping]]=..., initial_config: _Optional[_Union[Repository.InitialConfig, _Mapping]]=...) -> None:
        ...

class Hook(_message.Message):
    __slots__ = ('name', 'target_uri', 'disabled', 'events', 'create_time', 'update_time', 'uid', 'push_option', 'sensitive_query_string')

    class HookEventType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        UNSPECIFIED: _ClassVar[Hook.HookEventType]
        PUSH: _ClassVar[Hook.HookEventType]
        PULL_REQUEST: _ClassVar[Hook.HookEventType]
    UNSPECIFIED: Hook.HookEventType
    PUSH: Hook.HookEventType
    PULL_REQUEST: Hook.HookEventType

    class PushOption(_message.Message):
        __slots__ = ('branch_filter',)
        BRANCH_FILTER_FIELD_NUMBER: _ClassVar[int]
        branch_filter: str

        def __init__(self, branch_filter: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_URI_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    EVENTS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    PUSH_OPTION_FIELD_NUMBER: _ClassVar[int]
    SENSITIVE_QUERY_STRING_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_uri: str
    disabled: bool
    events: _containers.RepeatedScalarFieldContainer[Hook.HookEventType]
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    uid: str
    push_option: Hook.PushOption
    sensitive_query_string: str

    def __init__(self, name: _Optional[str]=..., target_uri: _Optional[str]=..., disabled: bool=..., events: _Optional[_Iterable[_Union[Hook.HookEventType, str]]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., uid: _Optional[str]=..., push_option: _Optional[_Union[Hook.PushOption, _Mapping]]=..., sensitive_query_string: _Optional[str]=...) -> None:
        ...

class BranchRule(_message.Message):
    __slots__ = ('name', 'uid', 'create_time', 'update_time', 'annotations', 'etag', 'include_pattern', 'disabled', 'require_pull_request', 'minimum_reviews_count', 'minimum_approvals_count', 'require_comments_resolved', 'allow_stale_reviews', 'require_linear_history', 'required_status_checks')

    class Check(_message.Message):
        __slots__ = ('context',)
        CONTEXT_FIELD_NUMBER: _ClassVar[int]
        context: str

        def __init__(self, context: _Optional[str]=...) -> None:
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
    UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ANNOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    INCLUDE_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_REVIEWS_COUNT_FIELD_NUMBER: _ClassVar[int]
    MINIMUM_APPROVALS_COUNT_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_COMMENTS_RESOLVED_FIELD_NUMBER: _ClassVar[int]
    ALLOW_STALE_REVIEWS_FIELD_NUMBER: _ClassVar[int]
    REQUIRE_LINEAR_HISTORY_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_STATUS_CHECKS_FIELD_NUMBER: _ClassVar[int]
    name: str
    uid: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    annotations: _containers.ScalarMap[str, str]
    etag: str
    include_pattern: str
    disabled: bool
    require_pull_request: bool
    minimum_reviews_count: int
    minimum_approvals_count: int
    require_comments_resolved: bool
    allow_stale_reviews: bool
    require_linear_history: bool
    required_status_checks: _containers.RepeatedCompositeFieldContainer[BranchRule.Check]

    def __init__(self, name: _Optional[str]=..., uid: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., annotations: _Optional[_Mapping[str, str]]=..., etag: _Optional[str]=..., include_pattern: _Optional[str]=..., disabled: bool=..., require_pull_request: bool=..., minimum_reviews_count: _Optional[int]=..., minimum_approvals_count: _Optional[int]=..., require_comments_resolved: bool=..., allow_stale_reviews: bool=..., require_linear_history: bool=..., required_status_checks: _Optional[_Iterable[_Union[BranchRule.Check, _Mapping]]]=...) -> None:
        ...

class PullRequest(_message.Message):
    __slots__ = ('name', 'title', 'body', 'base', 'head', 'state', 'create_time', 'update_time', 'close_time')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[PullRequest.State]
        OPEN: _ClassVar[PullRequest.State]
        CLOSED: _ClassVar[PullRequest.State]
        MERGED: _ClassVar[PullRequest.State]
    STATE_UNSPECIFIED: PullRequest.State
    OPEN: PullRequest.State
    CLOSED: PullRequest.State
    MERGED: PullRequest.State

    class Branch(_message.Message):
        __slots__ = ('ref', 'sha')
        REF_FIELD_NUMBER: _ClassVar[int]
        SHA_FIELD_NUMBER: _ClassVar[int]
        ref: str
        sha: str

        def __init__(self, ref: _Optional[str]=..., sha: _Optional[str]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    BASE_FIELD_NUMBER: _ClassVar[int]
    HEAD_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    body: str
    base: PullRequest.Branch
    head: PullRequest.Branch
    state: PullRequest.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    close_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., body: _Optional[str]=..., base: _Optional[_Union[PullRequest.Branch, _Mapping]]=..., head: _Optional[_Union[PullRequest.Branch, _Mapping]]=..., state: _Optional[_Union[PullRequest.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class FileDiff(_message.Message):
    __slots__ = ('name', 'action', 'sha', 'patch')

    class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ACTION_UNSPECIFIED: _ClassVar[FileDiff.Action]
        ADDED: _ClassVar[FileDiff.Action]
        MODIFIED: _ClassVar[FileDiff.Action]
        DELETED: _ClassVar[FileDiff.Action]
    ACTION_UNSPECIFIED: FileDiff.Action
    ADDED: FileDiff.Action
    MODIFIED: FileDiff.Action
    DELETED: FileDiff.Action
    NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    PATCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    action: FileDiff.Action
    sha: str
    patch: str

    def __init__(self, name: _Optional[str]=..., action: _Optional[_Union[FileDiff.Action, str]]=..., sha: _Optional[str]=..., patch: _Optional[str]=...) -> None:
        ...

class Issue(_message.Message):
    __slots__ = ('name', 'title', 'body', 'state', 'create_time', 'update_time', 'close_time', 'etag')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[Issue.State]
        OPEN: _ClassVar[Issue.State]
        CLOSED: _ClassVar[Issue.State]
    STATE_UNSPECIFIED: Issue.State
    OPEN: Issue.State
    CLOSED: Issue.State
    NAME_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    title: str
    body: str
    state: Issue.State
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    close_time: _timestamp_pb2.Timestamp
    etag: str

    def __init__(self, name: _Optional[str]=..., title: _Optional[str]=..., body: _Optional[str]=..., state: _Optional[_Union[Issue.State, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., close_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=...) -> None:
        ...

class IssueComment(_message.Message):
    __slots__ = ('name', 'body', 'create_time', 'update_time')
    NAME_FIELD_NUMBER: _ClassVar[int]
    BODY_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    name: str
    body: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp

    def __init__(self, name: _Optional[str]=..., body: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class PullRequestComment(_message.Message):
    __slots__ = ('name', 'create_time', 'update_time', 'review', 'comment', 'code')

    class Review(_message.Message):
        __slots__ = ('action_type', 'body', 'effective_commit_sha')

        class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_TYPE_UNSPECIFIED: _ClassVar[PullRequestComment.Review.ActionType]
            COMMENT: _ClassVar[PullRequestComment.Review.ActionType]
            CHANGE_REQUESTED: _ClassVar[PullRequestComment.Review.ActionType]
            APPROVED: _ClassVar[PullRequestComment.Review.ActionType]
        ACTION_TYPE_UNSPECIFIED: PullRequestComment.Review.ActionType
        COMMENT: PullRequestComment.Review.ActionType
        CHANGE_REQUESTED: PullRequestComment.Review.ActionType
        APPROVED: PullRequestComment.Review.ActionType
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        BODY_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
        action_type: PullRequestComment.Review.ActionType
        body: str
        effective_commit_sha: str

        def __init__(self, action_type: _Optional[_Union[PullRequestComment.Review.ActionType, str]]=..., body: _Optional[str]=..., effective_commit_sha: _Optional[str]=...) -> None:
            ...

    class Comment(_message.Message):
        __slots__ = ('body',)
        BODY_FIELD_NUMBER: _ClassVar[int]
        body: str

        def __init__(self, body: _Optional[str]=...) -> None:
            ...

    class Code(_message.Message):
        __slots__ = ('body', 'reply', 'position', 'effective_root_comment', 'resolved', 'effective_commit_sha')
        BODY_FIELD_NUMBER: _ClassVar[int]
        REPLY_FIELD_NUMBER: _ClassVar[int]
        POSITION_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_ROOT_COMMENT_FIELD_NUMBER: _ClassVar[int]
        RESOLVED_FIELD_NUMBER: _ClassVar[int]
        EFFECTIVE_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
        body: str
        reply: str
        position: PullRequestComment.Position
        effective_root_comment: str
        resolved: bool
        effective_commit_sha: str

        def __init__(self, body: _Optional[str]=..., reply: _Optional[str]=..., position: _Optional[_Union[PullRequestComment.Position, _Mapping]]=..., effective_root_comment: _Optional[str]=..., resolved: bool=..., effective_commit_sha: _Optional[str]=...) -> None:
            ...

    class Position(_message.Message):
        __slots__ = ('path', 'line')
        PATH_FIELD_NUMBER: _ClassVar[int]
        LINE_FIELD_NUMBER: _ClassVar[int]
        path: str
        line: int

        def __init__(self, path: _Optional[str]=..., line: _Optional[int]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    REVIEW_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    review: PullRequestComment.Review
    comment: PullRequestComment.Comment
    code: PullRequestComment.Code

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., review: _Optional[_Union[PullRequestComment.Review, _Mapping]]=..., comment: _Optional[_Union[PullRequestComment.Comment, _Mapping]]=..., code: _Optional[_Union[PullRequestComment.Code, _Mapping]]=...) -> None:
        ...

class ListInstancesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'order_by')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    order_by: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., order_by: _Optional[str]=...) -> None:
        ...

class ListInstancesResponse(_message.Message):
    __slots__ = ('instances', 'next_page_token', 'unreachable')
    INSTANCES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    instances: _containers.RepeatedCompositeFieldContainer[Instance]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, instances: _Optional[_Iterable[_Union[Instance, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetInstanceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateInstanceRequest(_message.Message):
    __slots__ = ('parent', 'instance_id', 'instance', 'request_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_ID_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    instance_id: str
    instance: Instance
    request_id: str

    def __init__(self, parent: _Optional[str]=..., instance_id: _Optional[str]=..., instance: _Optional[_Union[Instance, _Mapping]]=..., request_id: _Optional[str]=...) -> None:
        ...

class DeleteInstanceRequest(_message.Message):
    __slots__ = ('name', 'request_id')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REQUEST_ID_FIELD_NUMBER: _ClassVar[int]
    name: str
    request_id: str

    def __init__(self, name: _Optional[str]=..., request_id: _Optional[str]=...) -> None:
        ...

class OperationMetadata(_message.Message):
    __slots__ = ('create_time', 'end_time', 'target', 'verb', 'status_message', 'requested_cancellation', 'api_version')
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    END_TIME_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    VERB_FIELD_NUMBER: _ClassVar[int]
    STATUS_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REQUESTED_CANCELLATION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    create_time: _timestamp_pb2.Timestamp
    end_time: _timestamp_pb2.Timestamp
    target: str
    verb: str
    status_message: str
    requested_cancellation: bool
    api_version: str

    def __init__(self, create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., end_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., target: _Optional[str]=..., verb: _Optional[str]=..., status_message: _Optional[str]=..., requested_cancellation: bool=..., api_version: _Optional[str]=...) -> None:
        ...

class ListRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'filter', 'instance')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    INSTANCE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    filter: str
    instance: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=..., instance: _Optional[str]=...) -> None:
        ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetRepositoryRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateRepositoryRequest(_message.Message):
    __slots__ = ('parent', 'repository', 'repository_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    repository: Repository
    repository_id: str

    def __init__(self, parent: _Optional[str]=..., repository: _Optional[_Union[Repository, _Mapping]]=..., repository_id: _Optional[str]=...) -> None:
        ...

class UpdateRepositoryRequest(_message.Message):
    __slots__ = ('update_mask', 'repository', 'validate_only')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    repository: Repository
    validate_only: bool

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., repository: _Optional[_Union[Repository, _Mapping]]=..., validate_only: bool=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class ListHooksRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListHooksResponse(_message.Message):
    __slots__ = ('hooks', 'next_page_token')
    HOOKS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    hooks: _containers.RepeatedCompositeFieldContainer[Hook]
    next_page_token: str

    def __init__(self, hooks: _Optional[_Iterable[_Union[Hook, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetHookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateHookRequest(_message.Message):
    __slots__ = ('parent', 'hook', 'hook_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    HOOK_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    hook: Hook
    hook_id: str

    def __init__(self, parent: _Optional[str]=..., hook: _Optional[_Union[Hook, _Mapping]]=..., hook_id: _Optional[str]=...) -> None:
        ...

class UpdateHookRequest(_message.Message):
    __slots__ = ('update_mask', 'hook')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    HOOK_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    hook: Hook

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., hook: _Optional[_Union[Hook, _Mapping]]=...) -> None:
        ...

class DeleteHookRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetBranchRuleRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateBranchRuleRequest(_message.Message):
    __slots__ = ('parent', 'branch_rule', 'branch_rule_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    BRANCH_RULE_FIELD_NUMBER: _ClassVar[int]
    BRANCH_RULE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    branch_rule: BranchRule
    branch_rule_id: str

    def __init__(self, parent: _Optional[str]=..., branch_rule: _Optional[_Union[BranchRule, _Mapping]]=..., branch_rule_id: _Optional[str]=...) -> None:
        ...

class ListBranchRulesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class DeleteBranchRuleRequest(_message.Message):
    __slots__ = ('name', 'allow_missing')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ALLOW_MISSING_FIELD_NUMBER: _ClassVar[int]
    name: str
    allow_missing: bool

    def __init__(self, name: _Optional[str]=..., allow_missing: bool=...) -> None:
        ...

class UpdateBranchRuleRequest(_message.Message):
    __slots__ = ('branch_rule', 'validate_only', 'update_mask')
    BRANCH_RULE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    branch_rule: BranchRule
    validate_only: bool
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, branch_rule: _Optional[_Union[BranchRule, _Mapping]]=..., validate_only: bool=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class ListBranchRulesResponse(_message.Message):
    __slots__ = ('branch_rules', 'next_page_token')
    BRANCH_RULES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    branch_rules: _containers.RepeatedCompositeFieldContainer[BranchRule]
    next_page_token: str

    def __init__(self, branch_rules: _Optional[_Iterable[_Union[BranchRule, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreatePullRequestRequest(_message.Message):
    __slots__ = ('parent', 'pull_request')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pull_request: PullRequest

    def __init__(self, parent: _Optional[str]=..., pull_request: _Optional[_Union[PullRequest, _Mapping]]=...) -> None:
        ...

class GetPullRequestRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPullRequestsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPullRequestsResponse(_message.Message):
    __slots__ = ('pull_requests', 'next_page_token')
    PULL_REQUESTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    pull_requests: _containers.RepeatedCompositeFieldContainer[PullRequest]
    next_page_token: str

    def __init__(self, pull_requests: _Optional[_Iterable[_Union[PullRequest, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdatePullRequestRequest(_message.Message):
    __slots__ = ('pull_request', 'update_mask')
    PULL_REQUEST_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    pull_request: PullRequest
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, pull_request: _Optional[_Union[PullRequest, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class MergePullRequestRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class OpenPullRequestRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ClosePullRequestRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListPullRequestFileDiffsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPullRequestFileDiffsResponse(_message.Message):
    __slots__ = ('file_diffs', 'next_page_token')
    FILE_DIFFS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    file_diffs: _containers.RepeatedCompositeFieldContainer[FileDiff]
    next_page_token: str

    def __init__(self, file_diffs: _Optional[_Iterable[_Union[FileDiff, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateIssueRequest(_message.Message):
    __slots__ = ('parent', 'issue')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    parent: str
    issue: Issue

    def __init__(self, parent: _Optional[str]=..., issue: _Optional[_Union[Issue, _Mapping]]=...) -> None:
        ...

class GetIssueRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIssuesRequest(_message.Message):
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

class ListIssuesResponse(_message.Message):
    __slots__ = ('issues', 'next_page_token')
    ISSUES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    issues: _containers.RepeatedCompositeFieldContainer[Issue]
    next_page_token: str

    def __init__(self, issues: _Optional[_Iterable[_Union[Issue, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateIssueRequest(_message.Message):
    __slots__ = ('issue', 'update_mask')
    ISSUE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    issue: Issue
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, issue: _Optional[_Union[Issue, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteIssueRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class CloseIssueRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class OpenIssueRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class TreeEntry(_message.Message):
    __slots__ = ('type', 'sha', 'path', 'mode', 'size')

    class ObjectType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        OBJECT_TYPE_UNSPECIFIED: _ClassVar[TreeEntry.ObjectType]
        TREE: _ClassVar[TreeEntry.ObjectType]
        BLOB: _ClassVar[TreeEntry.ObjectType]
        COMMIT: _ClassVar[TreeEntry.ObjectType]
    OBJECT_TYPE_UNSPECIFIED: TreeEntry.ObjectType
    TREE: TreeEntry.ObjectType
    BLOB: TreeEntry.ObjectType
    COMMIT: TreeEntry.ObjectType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    type: TreeEntry.ObjectType
    sha: str
    path: str
    mode: str
    size: int

    def __init__(self, type: _Optional[_Union[TreeEntry.ObjectType, str]]=..., sha: _Optional[str]=..., path: _Optional[str]=..., mode: _Optional[str]=..., size: _Optional[int]=...) -> None:
        ...

class FetchTreeRequest(_message.Message):
    __slots__ = ('repository', 'ref', 'recursive', 'page_size', 'page_token')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    REF_FIELD_NUMBER: _ClassVar[int]
    RECURSIVE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    repository: str
    ref: str
    recursive: bool
    page_size: int
    page_token: str

    def __init__(self, repository: _Optional[str]=..., ref: _Optional[str]=..., recursive: bool=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchTreeResponse(_message.Message):
    __slots__ = ('tree_entries', 'next_page_token')
    TREE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    tree_entries: _containers.RepeatedCompositeFieldContainer[TreeEntry]
    next_page_token: str

    def __init__(self, tree_entries: _Optional[_Iterable[_Union[TreeEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class FetchBlobRequest(_message.Message):
    __slots__ = ('repository', 'sha')
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    SHA_FIELD_NUMBER: _ClassVar[int]
    repository: str
    sha: str

    def __init__(self, repository: _Optional[str]=..., sha: _Optional[str]=...) -> None:
        ...

class FetchBlobResponse(_message.Message):
    __slots__ = ('sha', 'content')
    SHA_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    sha: str
    content: str

    def __init__(self, sha: _Optional[str]=..., content: _Optional[str]=...) -> None:
        ...

class ListPullRequestCommentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListPullRequestCommentsResponse(_message.Message):
    __slots__ = ('pull_request_comments', 'next_page_token')
    PULL_REQUEST_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    pull_request_comments: _containers.RepeatedCompositeFieldContainer[PullRequestComment]
    next_page_token: str

    def __init__(self, pull_request_comments: _Optional[_Iterable[_Union[PullRequestComment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreatePullRequestCommentRequest(_message.Message):
    __slots__ = ('parent', 'pull_request_comment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PULL_REQUEST_COMMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    pull_request_comment: PullRequestComment

    def __init__(self, parent: _Optional[str]=..., pull_request_comment: _Optional[_Union[PullRequestComment, _Mapping]]=...) -> None:
        ...

class BatchCreatePullRequestCommentsRequest(_message.Message):
    __slots__ = ('parent', 'requests')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    requests: _containers.RepeatedCompositeFieldContainer[CreatePullRequestCommentRequest]

    def __init__(self, parent: _Optional[str]=..., requests: _Optional[_Iterable[_Union[CreatePullRequestCommentRequest, _Mapping]]]=...) -> None:
        ...

class BatchCreatePullRequestCommentsResponse(_message.Message):
    __slots__ = ('pull_request_comments',)
    PULL_REQUEST_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    pull_request_comments: _containers.RepeatedCompositeFieldContainer[PullRequestComment]

    def __init__(self, pull_request_comments: _Optional[_Iterable[_Union[PullRequestComment, _Mapping]]]=...) -> None:
        ...

class UpdatePullRequestCommentRequest(_message.Message):
    __slots__ = ('pull_request_comment', 'update_mask')
    PULL_REQUEST_COMMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    pull_request_comment: PullRequestComment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, pull_request_comment: _Optional[_Union[PullRequestComment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeletePullRequestCommentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class GetPullRequestCommentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ResolvePullRequestCommentsRequest(_message.Message):
    __slots__ = ('parent', 'names', 'auto_fill')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    AUTO_FILL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    auto_fill: bool

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., auto_fill: bool=...) -> None:
        ...

class ResolvePullRequestCommentsResponse(_message.Message):
    __slots__ = ('pull_request_comments',)
    PULL_REQUEST_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    pull_request_comments: _containers.RepeatedCompositeFieldContainer[PullRequestComment]

    def __init__(self, pull_request_comments: _Optional[_Iterable[_Union[PullRequestComment, _Mapping]]]=...) -> None:
        ...

class UnresolvePullRequestCommentsRequest(_message.Message):
    __slots__ = ('parent', 'names', 'auto_fill')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    NAMES_FIELD_NUMBER: _ClassVar[int]
    AUTO_FILL_FIELD_NUMBER: _ClassVar[int]
    parent: str
    names: _containers.RepeatedScalarFieldContainer[str]
    auto_fill: bool

    def __init__(self, parent: _Optional[str]=..., names: _Optional[_Iterable[str]]=..., auto_fill: bool=...) -> None:
        ...

class UnresolvePullRequestCommentsResponse(_message.Message):
    __slots__ = ('pull_request_comments',)
    PULL_REQUEST_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    pull_request_comments: _containers.RepeatedCompositeFieldContainer[PullRequestComment]

    def __init__(self, pull_request_comments: _Optional[_Iterable[_Union[PullRequestComment, _Mapping]]]=...) -> None:
        ...

class CreateIssueCommentRequest(_message.Message):
    __slots__ = ('parent', 'issue_comment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    ISSUE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    issue_comment: IssueComment

    def __init__(self, parent: _Optional[str]=..., issue_comment: _Optional[_Union[IssueComment, _Mapping]]=...) -> None:
        ...

class GetIssueCommentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListIssueCommentsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListIssueCommentsResponse(_message.Message):
    __slots__ = ('issue_comments', 'next_page_token')
    ISSUE_COMMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    issue_comments: _containers.RepeatedCompositeFieldContainer[IssueComment]
    next_page_token: str

    def __init__(self, issue_comments: _Optional[_Iterable[_Union[IssueComment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class UpdateIssueCommentRequest(_message.Message):
    __slots__ = ('issue_comment', 'update_mask')
    ISSUE_COMMENT_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    issue_comment: IssueComment
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, issue_comment: _Optional[_Union[IssueComment, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteIssueCommentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...