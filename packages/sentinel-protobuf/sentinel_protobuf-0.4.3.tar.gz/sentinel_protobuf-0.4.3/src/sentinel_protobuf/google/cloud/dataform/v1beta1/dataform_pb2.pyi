from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.rpc import status_pb2 as _status_pb2
from google.type import interval_pb2 as _interval_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DataEncryptionState(_message.Message):
    __slots__ = ('kms_key_version_name',)
    KMS_KEY_VERSION_NAME_FIELD_NUMBER: _ClassVar[int]
    kms_key_version_name: str

    def __init__(self, kms_key_version_name: _Optional[str]=...) -> None:
        ...

class Repository(_message.Message):
    __slots__ = ('name', 'create_time', 'display_name', 'git_remote_settings', 'npmrc_environment_variables_secret_version', 'workspace_compilation_overrides', 'labels', 'set_authenticated_user_admin', 'service_account', 'kms_key_name', 'data_encryption_state', 'internal_metadata')

    class GitRemoteSettings(_message.Message):
        __slots__ = ('url', 'default_branch', 'authentication_token_secret_version', 'ssh_authentication_config', 'token_status')

        class TokenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TOKEN_STATUS_UNSPECIFIED: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            NOT_FOUND: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            INVALID: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
            VALID: _ClassVar[Repository.GitRemoteSettings.TokenStatus]
        TOKEN_STATUS_UNSPECIFIED: Repository.GitRemoteSettings.TokenStatus
        NOT_FOUND: Repository.GitRemoteSettings.TokenStatus
        INVALID: Repository.GitRemoteSettings.TokenStatus
        VALID: Repository.GitRemoteSettings.TokenStatus

        class SshAuthenticationConfig(_message.Message):
            __slots__ = ('user_private_key_secret_version', 'host_public_key')
            USER_PRIVATE_KEY_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
            HOST_PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
            user_private_key_secret_version: str
            host_public_key: str

            def __init__(self, user_private_key_secret_version: _Optional[str]=..., host_public_key: _Optional[str]=...) -> None:
                ...
        URL_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_BRANCH_FIELD_NUMBER: _ClassVar[int]
        AUTHENTICATION_TOKEN_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
        SSH_AUTHENTICATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
        TOKEN_STATUS_FIELD_NUMBER: _ClassVar[int]
        url: str
        default_branch: str
        authentication_token_secret_version: str
        ssh_authentication_config: Repository.GitRemoteSettings.SshAuthenticationConfig
        token_status: Repository.GitRemoteSettings.TokenStatus

        def __init__(self, url: _Optional[str]=..., default_branch: _Optional[str]=..., authentication_token_secret_version: _Optional[str]=..., ssh_authentication_config: _Optional[_Union[Repository.GitRemoteSettings.SshAuthenticationConfig, _Mapping]]=..., token_status: _Optional[_Union[Repository.GitRemoteSettings.TokenStatus, str]]=...) -> None:
            ...

    class WorkspaceCompilationOverrides(_message.Message):
        __slots__ = ('default_database', 'schema_suffix', 'table_prefix')
        DEFAULT_DATABASE_FIELD_NUMBER: _ClassVar[int]
        SCHEMA_SUFFIX_FIELD_NUMBER: _ClassVar[int]
        TABLE_PREFIX_FIELD_NUMBER: _ClassVar[int]
        default_database: str
        schema_suffix: str
        table_prefix: str

        def __init__(self, default_database: _Optional[str]=..., schema_suffix: _Optional[str]=..., table_prefix: _Optional[str]=...) -> None:
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
    DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    GIT_REMOTE_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NPMRC_ENVIRONMENT_VARIABLES_SECRET_VERSION_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_COMPILATION_OVERRIDES_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    SET_AUTHENTICATED_USER_ADMIN_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    DATA_ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    display_name: str
    git_remote_settings: Repository.GitRemoteSettings
    npmrc_environment_variables_secret_version: str
    workspace_compilation_overrides: Repository.WorkspaceCompilationOverrides
    labels: _containers.ScalarMap[str, str]
    set_authenticated_user_admin: bool
    service_account: str
    kms_key_name: str
    data_encryption_state: DataEncryptionState
    internal_metadata: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., display_name: _Optional[str]=..., git_remote_settings: _Optional[_Union[Repository.GitRemoteSettings, _Mapping]]=..., npmrc_environment_variables_secret_version: _Optional[str]=..., workspace_compilation_overrides: _Optional[_Union[Repository.WorkspaceCompilationOverrides, _Mapping]]=..., labels: _Optional[_Mapping[str, str]]=..., set_authenticated_user_admin: bool=..., service_account: _Optional[str]=..., kms_key_name: _Optional[str]=..., data_encryption_state: _Optional[_Union[DataEncryptionState, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class ListRepositoriesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListRepositoriesResponse(_message.Message):
    __slots__ = ('repositories', 'next_page_token', 'unreachable')
    REPOSITORIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    repositories: _containers.RepeatedCompositeFieldContainer[Repository]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, repositories: _Optional[_Iterable[_Union[Repository, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
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
    __slots__ = ('update_mask', 'repository')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    REPOSITORY_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    repository: Repository

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., repository: _Optional[_Union[Repository, _Mapping]]=...) -> None:
        ...

class DeleteRepositoryRequest(_message.Message):
    __slots__ = ('name', 'force')
    NAME_FIELD_NUMBER: _ClassVar[int]
    FORCE_FIELD_NUMBER: _ClassVar[int]
    name: str
    force: bool

    def __init__(self, name: _Optional[str]=..., force: bool=...) -> None:
        ...

class CommitRepositoryChangesRequest(_message.Message):
    __slots__ = ('name', 'commit_metadata', 'required_head_commit_sha', 'file_operations')

    class FileOperation(_message.Message):
        __slots__ = ('write_file', 'delete_file')

        class WriteFile(_message.Message):
            __slots__ = ('contents',)
            CONTENTS_FIELD_NUMBER: _ClassVar[int]
            contents: bytes

            def __init__(self, contents: _Optional[bytes]=...) -> None:
                ...

        class DeleteFile(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...
        WRITE_FILE_FIELD_NUMBER: _ClassVar[int]
        DELETE_FILE_FIELD_NUMBER: _ClassVar[int]
        write_file: CommitRepositoryChangesRequest.FileOperation.WriteFile
        delete_file: CommitRepositoryChangesRequest.FileOperation.DeleteFile

        def __init__(self, write_file: _Optional[_Union[CommitRepositoryChangesRequest.FileOperation.WriteFile, _Mapping]]=..., delete_file: _Optional[_Union[CommitRepositoryChangesRequest.FileOperation.DeleteFile, _Mapping]]=...) -> None:
            ...

    class FileOperationsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: CommitRepositoryChangesRequest.FileOperation

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[CommitRepositoryChangesRequest.FileOperation, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_METADATA_FIELD_NUMBER: _ClassVar[int]
    REQUIRED_HEAD_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    FILE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_metadata: CommitMetadata
    required_head_commit_sha: str
    file_operations: _containers.MessageMap[str, CommitRepositoryChangesRequest.FileOperation]

    def __init__(self, name: _Optional[str]=..., commit_metadata: _Optional[_Union[CommitMetadata, _Mapping]]=..., required_head_commit_sha: _Optional[str]=..., file_operations: _Optional[_Mapping[str, CommitRepositoryChangesRequest.FileOperation]]=...) -> None:
        ...

class CommitRepositoryChangesResponse(_message.Message):
    __slots__ = ('commit_sha',)
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    commit_sha: str

    def __init__(self, commit_sha: _Optional[str]=...) -> None:
        ...

class ReadRepositoryFileRequest(_message.Message):
    __slots__ = ('name', 'commit_sha', 'path')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_sha: str
    path: str

    def __init__(self, name: _Optional[str]=..., commit_sha: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class ReadRepositoryFileResponse(_message.Message):
    __slots__ = ('contents',)
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    contents: bytes

    def __init__(self, contents: _Optional[bytes]=...) -> None:
        ...

class QueryRepositoryDirectoryContentsRequest(_message.Message):
    __slots__ = ('name', 'commit_sha', 'path', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    commit_sha: str
    path: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., commit_sha: _Optional[str]=..., path: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryRepositoryDirectoryContentsResponse(_message.Message):
    __slots__ = ('directory_entries', 'next_page_token')
    DIRECTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    directory_entries: _containers.RepeatedCompositeFieldContainer[DirectoryEntry]
    next_page_token: str

    def __init__(self, directory_entries: _Optional[_Iterable[_Union[DirectoryEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class FetchRepositoryHistoryRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class FetchRepositoryHistoryResponse(_message.Message):
    __slots__ = ('commits', 'next_page_token')
    COMMITS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    commits: _containers.RepeatedCompositeFieldContainer[CommitLogEntry]
    next_page_token: str

    def __init__(self, commits: _Optional[_Iterable[_Union[CommitLogEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CommitLogEntry(_message.Message):
    __slots__ = ('commit_time', 'commit_sha', 'author', 'commit_message')
    COMMIT_TIME_FIELD_NUMBER: _ClassVar[int]
    COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    commit_time: _timestamp_pb2.Timestamp
    commit_sha: str
    author: CommitAuthor
    commit_message: str

    def __init__(self, commit_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., commit_sha: _Optional[str]=..., author: _Optional[_Union[CommitAuthor, _Mapping]]=..., commit_message: _Optional[str]=...) -> None:
        ...

class CommitMetadata(_message.Message):
    __slots__ = ('author', 'commit_message')
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    author: CommitAuthor
    commit_message: str

    def __init__(self, author: _Optional[_Union[CommitAuthor, _Mapping]]=..., commit_message: _Optional[str]=...) -> None:
        ...

class ComputeRepositoryAccessTokenStatusRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ComputeRepositoryAccessTokenStatusResponse(_message.Message):
    __slots__ = ('token_status',)

    class TokenStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TOKEN_STATUS_UNSPECIFIED: _ClassVar[ComputeRepositoryAccessTokenStatusResponse.TokenStatus]
        NOT_FOUND: _ClassVar[ComputeRepositoryAccessTokenStatusResponse.TokenStatus]
        INVALID: _ClassVar[ComputeRepositoryAccessTokenStatusResponse.TokenStatus]
        VALID: _ClassVar[ComputeRepositoryAccessTokenStatusResponse.TokenStatus]
    TOKEN_STATUS_UNSPECIFIED: ComputeRepositoryAccessTokenStatusResponse.TokenStatus
    NOT_FOUND: ComputeRepositoryAccessTokenStatusResponse.TokenStatus
    INVALID: ComputeRepositoryAccessTokenStatusResponse.TokenStatus
    VALID: ComputeRepositoryAccessTokenStatusResponse.TokenStatus
    TOKEN_STATUS_FIELD_NUMBER: _ClassVar[int]
    token_status: ComputeRepositoryAccessTokenStatusResponse.TokenStatus

    def __init__(self, token_status: _Optional[_Union[ComputeRepositoryAccessTokenStatusResponse.TokenStatus, str]]=...) -> None:
        ...

class FetchRemoteBranchesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchRemoteBranchesResponse(_message.Message):
    __slots__ = ('branches',)
    BRANCHES_FIELD_NUMBER: _ClassVar[int]
    branches: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, branches: _Optional[_Iterable[str]]=...) -> None:
        ...

class Workspace(_message.Message):
    __slots__ = ('name', 'create_time', 'data_encryption_state', 'internal_metadata')
    NAME_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    DATA_ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    create_time: _timestamp_pb2.Timestamp
    data_encryption_state: DataEncryptionState
    internal_metadata: str

    def __init__(self, name: _Optional[str]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., data_encryption_state: _Optional[_Union[DataEncryptionState, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class ListWorkspacesRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListWorkspacesResponse(_message.Message):
    __slots__ = ('workspaces', 'next_page_token', 'unreachable')
    WORKSPACES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workspaces: _containers.RepeatedCompositeFieldContainer[Workspace]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workspaces: _Optional[_Iterable[_Union[Workspace, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkspaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkspaceRequest(_message.Message):
    __slots__ = ('parent', 'workspace', 'workspace_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workspace: Workspace
    workspace_id: str

    def __init__(self, parent: _Optional[str]=..., workspace: _Optional[_Union[Workspace, _Mapping]]=..., workspace_id: _Optional[str]=...) -> None:
        ...

class DeleteWorkspaceRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CommitAuthor(_message.Message):
    __slots__ = ('name', 'email_address')
    NAME_FIELD_NUMBER: _ClassVar[int]
    EMAIL_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    name: str
    email_address: str

    def __init__(self, name: _Optional[str]=..., email_address: _Optional[str]=...) -> None:
        ...

class PullGitCommitsRequest(_message.Message):
    __slots__ = ('name', 'remote_branch', 'author')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str
    author: CommitAuthor

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=..., author: _Optional[_Union[CommitAuthor, _Mapping]]=...) -> None:
        ...

class PullGitCommitsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class PushGitCommitsRequest(_message.Message):
    __slots__ = ('name', 'remote_branch')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=...) -> None:
        ...

class PushGitCommitsResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FetchFileGitStatusesRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class FetchFileGitStatusesResponse(_message.Message):
    __slots__ = ('uncommitted_file_changes',)

    class UncommittedFileChange(_message.Message):
        __slots__ = ('path', 'state')

        class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATE_UNSPECIFIED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            ADDED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            DELETED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            MODIFIED: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
            HAS_CONFLICTS: _ClassVar[FetchFileGitStatusesResponse.UncommittedFileChange.State]
        STATE_UNSPECIFIED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        ADDED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        DELETED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        MODIFIED: FetchFileGitStatusesResponse.UncommittedFileChange.State
        HAS_CONFLICTS: FetchFileGitStatusesResponse.UncommittedFileChange.State
        PATH_FIELD_NUMBER: _ClassVar[int]
        STATE_FIELD_NUMBER: _ClassVar[int]
        path: str
        state: FetchFileGitStatusesResponse.UncommittedFileChange.State

        def __init__(self, path: _Optional[str]=..., state: _Optional[_Union[FetchFileGitStatusesResponse.UncommittedFileChange.State, str]]=...) -> None:
            ...
    UNCOMMITTED_FILE_CHANGES_FIELD_NUMBER: _ClassVar[int]
    uncommitted_file_changes: _containers.RepeatedCompositeFieldContainer[FetchFileGitStatusesResponse.UncommittedFileChange]

    def __init__(self, uncommitted_file_changes: _Optional[_Iterable[_Union[FetchFileGitStatusesResponse.UncommittedFileChange, _Mapping]]]=...) -> None:
        ...

class FetchGitAheadBehindRequest(_message.Message):
    __slots__ = ('name', 'remote_branch')
    NAME_FIELD_NUMBER: _ClassVar[int]
    REMOTE_BRANCH_FIELD_NUMBER: _ClassVar[int]
    name: str
    remote_branch: str

    def __init__(self, name: _Optional[str]=..., remote_branch: _Optional[str]=...) -> None:
        ...

class FetchGitAheadBehindResponse(_message.Message):
    __slots__ = ('commits_ahead', 'commits_behind')
    COMMITS_AHEAD_FIELD_NUMBER: _ClassVar[int]
    COMMITS_BEHIND_FIELD_NUMBER: _ClassVar[int]
    commits_ahead: int
    commits_behind: int

    def __init__(self, commits_ahead: _Optional[int]=..., commits_behind: _Optional[int]=...) -> None:
        ...

class CommitWorkspaceChangesRequest(_message.Message):
    __slots__ = ('name', 'author', 'commit_message', 'paths')
    NAME_FIELD_NUMBER: _ClassVar[int]
    AUTHOR_FIELD_NUMBER: _ClassVar[int]
    COMMIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    name: str
    author: CommitAuthor
    commit_message: str
    paths: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, name: _Optional[str]=..., author: _Optional[_Union[CommitAuthor, _Mapping]]=..., commit_message: _Optional[str]=..., paths: _Optional[_Iterable[str]]=...) -> None:
        ...

class CommitWorkspaceChangesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ResetWorkspaceChangesRequest(_message.Message):
    __slots__ = ('name', 'paths', 'clean')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PATHS_FIELD_NUMBER: _ClassVar[int]
    CLEAN_FIELD_NUMBER: _ClassVar[int]
    name: str
    paths: _containers.RepeatedScalarFieldContainer[str]
    clean: bool

    def __init__(self, name: _Optional[str]=..., paths: _Optional[_Iterable[str]]=..., clean: bool=...) -> None:
        ...

class ResetWorkspaceChangesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class FetchFileDiffRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class FetchFileDiffResponse(_message.Message):
    __slots__ = ('formatted_diff',)
    FORMATTED_DIFF_FIELD_NUMBER: _ClassVar[int]
    formatted_diff: str

    def __init__(self, formatted_diff: _Optional[str]=...) -> None:
        ...

class QueryDirectoryContentsRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'page_size', 'page_token')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    page_size: int
    page_token: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryDirectoryContentsResponse(_message.Message):
    __slots__ = ('directory_entries', 'next_page_token')
    DIRECTORY_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    directory_entries: _containers.RepeatedCompositeFieldContainer[DirectoryEntry]
    next_page_token: str

    def __init__(self, directory_entries: _Optional[_Iterable[_Union[DirectoryEntry, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class DirectoryEntry(_message.Message):
    __slots__ = ('file', 'directory')
    FILE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    file: str
    directory: str

    def __init__(self, file: _Optional[str]=..., directory: _Optional[str]=...) -> None:
        ...

class SearchFilesRequest(_message.Message):
    __slots__ = ('workspace', 'page_size', 'page_token', 'filter')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, workspace: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class SearchFilesResponse(_message.Message):
    __slots__ = ('search_results', 'next_page_token')
    SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    search_results: _containers.RepeatedCompositeFieldContainer[SearchResult]
    next_page_token: str

    def __init__(self, search_results: _Optional[_Iterable[_Union[SearchResult, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class SearchResult(_message.Message):
    __slots__ = ('file', 'directory')
    FILE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    file: FileSearchResult
    directory: DirectorySearchResult

    def __init__(self, file: _Optional[_Union[FileSearchResult, _Mapping]]=..., directory: _Optional[_Union[DirectorySearchResult, _Mapping]]=...) -> None:
        ...

class FileSearchResult(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class DirectorySearchResult(_message.Message):
    __slots__ = ('path',)
    PATH_FIELD_NUMBER: _ClassVar[int]
    path: str

    def __init__(self, path: _Optional[str]=...) -> None:
        ...

class MakeDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class MakeDirectoryResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class RemoveDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class RemoveDirectoryResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MoveDirectoryRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'new_path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    new_path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., new_path: _Optional[str]=...) -> None:
        ...

class MoveDirectoryResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReadFileRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'revision')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    REVISION_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    revision: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., revision: _Optional[str]=...) -> None:
        ...

class ReadFileResponse(_message.Message):
    __slots__ = ('file_contents',)
    FILE_CONTENTS_FIELD_NUMBER: _ClassVar[int]
    file_contents: bytes

    def __init__(self, file_contents: _Optional[bytes]=...) -> None:
        ...

class RemoveFileRequest(_message.Message):
    __slots__ = ('workspace', 'path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=...) -> None:
        ...

class RemoveFileResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class MoveFileRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'new_path')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    NEW_PATH_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    new_path: str

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., new_path: _Optional[str]=...) -> None:
        ...

class MoveFileResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WriteFileRequest(_message.Message):
    __slots__ = ('workspace', 'path', 'contents')
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    CONTENTS_FIELD_NUMBER: _ClassVar[int]
    workspace: str
    path: str
    contents: bytes

    def __init__(self, workspace: _Optional[str]=..., path: _Optional[str]=..., contents: _Optional[bytes]=...) -> None:
        ...

class WriteFileResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class InstallNpmPackagesRequest(_message.Message):
    __slots__ = ('workspace',)
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    workspace: str

    def __init__(self, workspace: _Optional[str]=...) -> None:
        ...

class InstallNpmPackagesResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class ReleaseConfig(_message.Message):
    __slots__ = ('name', 'git_commitish', 'code_compilation_config', 'cron_schedule', 'time_zone', 'recent_scheduled_release_records', 'release_compilation_result', 'disabled', 'internal_metadata')

    class ScheduledReleaseRecord(_message.Message):
        __slots__ = ('compilation_result', 'error_status', 'release_time')
        COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
        ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
        RELEASE_TIME_FIELD_NUMBER: _ClassVar[int]
        compilation_result: str
        error_status: _status_pb2.Status
        release_time: _timestamp_pb2.Timestamp

        def __init__(self, compilation_result: _Optional[str]=..., error_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., release_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    GIT_COMMITISH_FIELD_NUMBER: _ClassVar[int]
    CODE_COMPILATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    RECENT_SCHEDULED_RELEASE_RECORDS_FIELD_NUMBER: _ClassVar[int]
    RELEASE_COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    git_commitish: str
    code_compilation_config: CodeCompilationConfig
    cron_schedule: str
    time_zone: str
    recent_scheduled_release_records: _containers.RepeatedCompositeFieldContainer[ReleaseConfig.ScheduledReleaseRecord]
    release_compilation_result: str
    disabled: bool
    internal_metadata: str

    def __init__(self, name: _Optional[str]=..., git_commitish: _Optional[str]=..., code_compilation_config: _Optional[_Union[CodeCompilationConfig, _Mapping]]=..., cron_schedule: _Optional[str]=..., time_zone: _Optional[str]=..., recent_scheduled_release_records: _Optional[_Iterable[_Union[ReleaseConfig.ScheduledReleaseRecord, _Mapping]]]=..., release_compilation_result: _Optional[str]=..., disabled: bool=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class ListReleaseConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListReleaseConfigsResponse(_message.Message):
    __slots__ = ('release_configs', 'next_page_token', 'unreachable')
    RELEASE_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    release_configs: _containers.RepeatedCompositeFieldContainer[ReleaseConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, release_configs: _Optional[_Iterable[_Union[ReleaseConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetReleaseConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateReleaseConfigRequest(_message.Message):
    __slots__ = ('parent', 'release_config', 'release_config_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    release_config: ReleaseConfig
    release_config_id: str

    def __init__(self, parent: _Optional[str]=..., release_config: _Optional[_Union[ReleaseConfig, _Mapping]]=..., release_config_id: _Optional[str]=...) -> None:
        ...

class UpdateReleaseConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'release_config')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    release_config: ReleaseConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., release_config: _Optional[_Union[ReleaseConfig, _Mapping]]=...) -> None:
        ...

class DeleteReleaseConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CompilationResult(_message.Message):
    __slots__ = ('git_commitish', 'workspace', 'release_config', 'name', 'code_compilation_config', 'resolved_git_commit_sha', 'dataform_core_version', 'compilation_errors', 'data_encryption_state', 'create_time', 'internal_metadata')

    class CompilationError(_message.Message):
        __slots__ = ('message', 'stack', 'path', 'action_target')
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        STACK_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        ACTION_TARGET_FIELD_NUMBER: _ClassVar[int]
        message: str
        stack: str
        path: str
        action_target: Target

        def __init__(self, message: _Optional[str]=..., stack: _Optional[str]=..., path: _Optional[str]=..., action_target: _Optional[_Union[Target, _Mapping]]=...) -> None:
            ...
    GIT_COMMITISH_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CODE_COMPILATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_GIT_COMMIT_SHA_FIELD_NUMBER: _ClassVar[int]
    DATAFORM_CORE_VERSION_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_ERRORS_FIELD_NUMBER: _ClassVar[int]
    DATA_ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    git_commitish: str
    workspace: str
    release_config: str
    name: str
    code_compilation_config: CodeCompilationConfig
    resolved_git_commit_sha: str
    dataform_core_version: str
    compilation_errors: _containers.RepeatedCompositeFieldContainer[CompilationResult.CompilationError]
    data_encryption_state: DataEncryptionState
    create_time: _timestamp_pb2.Timestamp
    internal_metadata: str

    def __init__(self, git_commitish: _Optional[str]=..., workspace: _Optional[str]=..., release_config: _Optional[str]=..., name: _Optional[str]=..., code_compilation_config: _Optional[_Union[CodeCompilationConfig, _Mapping]]=..., resolved_git_commit_sha: _Optional[str]=..., dataform_core_version: _Optional[str]=..., compilation_errors: _Optional[_Iterable[_Union[CompilationResult.CompilationError, _Mapping]]]=..., data_encryption_state: _Optional[_Union[DataEncryptionState, _Mapping]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class CodeCompilationConfig(_message.Message):
    __slots__ = ('default_database', 'default_schema', 'default_location', 'assertion_schema', 'vars', 'database_suffix', 'schema_suffix', 'table_prefix', 'builtin_assertion_name_prefix', 'default_notebook_runtime_options')

    class VarsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DEFAULT_DATABASE_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_LOCATION_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_SCHEMA_FIELD_NUMBER: _ClassVar[int]
    VARS_FIELD_NUMBER: _ClassVar[int]
    DATABASE_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_SUFFIX_FIELD_NUMBER: _ClassVar[int]
    TABLE_PREFIX_FIELD_NUMBER: _ClassVar[int]
    BUILTIN_ASSERTION_NAME_PREFIX_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_NOTEBOOK_RUNTIME_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    default_database: str
    default_schema: str
    default_location: str
    assertion_schema: str
    vars: _containers.ScalarMap[str, str]
    database_suffix: str
    schema_suffix: str
    table_prefix: str
    builtin_assertion_name_prefix: str
    default_notebook_runtime_options: NotebookRuntimeOptions

    def __init__(self, default_database: _Optional[str]=..., default_schema: _Optional[str]=..., default_location: _Optional[str]=..., assertion_schema: _Optional[str]=..., vars: _Optional[_Mapping[str, str]]=..., database_suffix: _Optional[str]=..., schema_suffix: _Optional[str]=..., table_prefix: _Optional[str]=..., builtin_assertion_name_prefix: _Optional[str]=..., default_notebook_runtime_options: _Optional[_Union[NotebookRuntimeOptions, _Mapping]]=...) -> None:
        ...

class NotebookRuntimeOptions(_message.Message):
    __slots__ = ('gcs_output_bucket', 'ai_platform_notebook_runtime_template')
    GCS_OUTPUT_BUCKET_FIELD_NUMBER: _ClassVar[int]
    AI_PLATFORM_NOTEBOOK_RUNTIME_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    gcs_output_bucket: str
    ai_platform_notebook_runtime_template: str

    def __init__(self, gcs_output_bucket: _Optional[str]=..., ai_platform_notebook_runtime_template: _Optional[str]=...) -> None:
        ...

class ListCompilationResultsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListCompilationResultsResponse(_message.Message):
    __slots__ = ('compilation_results', 'next_page_token', 'unreachable')
    COMPILATION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    compilation_results: _containers.RepeatedCompositeFieldContainer[CompilationResult]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, compilation_results: _Optional[_Iterable[_Union[CompilationResult, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetCompilationResultRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCompilationResultRequest(_message.Message):
    __slots__ = ('parent', 'compilation_result')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    compilation_result: CompilationResult

    def __init__(self, parent: _Optional[str]=..., compilation_result: _Optional[_Union[CompilationResult, _Mapping]]=...) -> None:
        ...

class Target(_message.Message):
    __slots__ = ('database', 'schema', 'name')
    DATABASE_FIELD_NUMBER: _ClassVar[int]
    SCHEMA_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    database: str
    schema: str
    name: str

    def __init__(self, database: _Optional[str]=..., schema: _Optional[str]=..., name: _Optional[str]=...) -> None:
        ...

class RelationDescriptor(_message.Message):
    __slots__ = ('description', 'columns', 'bigquery_labels')

    class ColumnDescriptor(_message.Message):
        __slots__ = ('path', 'description', 'bigquery_policy_tags')
        PATH_FIELD_NUMBER: _ClassVar[int]
        DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        BIGQUERY_POLICY_TAGS_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedScalarFieldContainer[str]
        description: str
        bigquery_policy_tags: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, path: _Optional[_Iterable[str]]=..., description: _Optional[str]=..., bigquery_policy_tags: _Optional[_Iterable[str]]=...) -> None:
            ...

    class BigqueryLabelsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str

        def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
            ...
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    COLUMNS_FIELD_NUMBER: _ClassVar[int]
    BIGQUERY_LABELS_FIELD_NUMBER: _ClassVar[int]
    description: str
    columns: _containers.RepeatedCompositeFieldContainer[RelationDescriptor.ColumnDescriptor]
    bigquery_labels: _containers.ScalarMap[str, str]

    def __init__(self, description: _Optional[str]=..., columns: _Optional[_Iterable[_Union[RelationDescriptor.ColumnDescriptor, _Mapping]]]=..., bigquery_labels: _Optional[_Mapping[str, str]]=...) -> None:
        ...

class CompilationResultAction(_message.Message):
    __slots__ = ('relation', 'operations', 'assertion', 'declaration', 'notebook', 'data_preparation', 'target', 'canonical_target', 'file_path', 'internal_metadata')

    class Relation(_message.Message):
        __slots__ = ('dependency_targets', 'disabled', 'tags', 'relation_descriptor', 'relation_type', 'select_query', 'pre_operations', 'post_operations', 'incremental_table_config', 'partition_expression', 'cluster_expressions', 'partition_expiration_days', 'require_partition_filter', 'additional_options')

        class RelationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RELATION_TYPE_UNSPECIFIED: _ClassVar[CompilationResultAction.Relation.RelationType]
            TABLE: _ClassVar[CompilationResultAction.Relation.RelationType]
            VIEW: _ClassVar[CompilationResultAction.Relation.RelationType]
            INCREMENTAL_TABLE: _ClassVar[CompilationResultAction.Relation.RelationType]
            MATERIALIZED_VIEW: _ClassVar[CompilationResultAction.Relation.RelationType]
        RELATION_TYPE_UNSPECIFIED: CompilationResultAction.Relation.RelationType
        TABLE: CompilationResultAction.Relation.RelationType
        VIEW: CompilationResultAction.Relation.RelationType
        INCREMENTAL_TABLE: CompilationResultAction.Relation.RelationType
        MATERIALIZED_VIEW: CompilationResultAction.Relation.RelationType

        class IncrementalTableConfig(_message.Message):
            __slots__ = ('incremental_select_query', 'refresh_disabled', 'unique_key_parts', 'update_partition_filter', 'incremental_pre_operations', 'incremental_post_operations')
            INCREMENTAL_SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
            REFRESH_DISABLED_FIELD_NUMBER: _ClassVar[int]
            UNIQUE_KEY_PARTS_FIELD_NUMBER: _ClassVar[int]
            UPDATE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
            INCREMENTAL_PRE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
            INCREMENTAL_POST_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
            incremental_select_query: str
            refresh_disabled: bool
            unique_key_parts: _containers.RepeatedScalarFieldContainer[str]
            update_partition_filter: str
            incremental_pre_operations: _containers.RepeatedScalarFieldContainer[str]
            incremental_post_operations: _containers.RepeatedScalarFieldContainer[str]

            def __init__(self, incremental_select_query: _Optional[str]=..., refresh_disabled: bool=..., unique_key_parts: _Optional[_Iterable[str]]=..., update_partition_filter: _Optional[str]=..., incremental_pre_operations: _Optional[_Iterable[str]]=..., incremental_post_operations: _Optional[_Iterable[str]]=...) -> None:
                ...

        class AdditionalOptionsEntry(_message.Message):
            __slots__ = ('key', 'value')
            KEY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            key: str
            value: str

            def __init__(self, key: _Optional[str]=..., value: _Optional[str]=...) -> None:
                ...
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        RELATION_TYPE_FIELD_NUMBER: _ClassVar[int]
        SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
        PRE_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        POST_OPERATIONS_FIELD_NUMBER: _ClassVar[int]
        INCREMENTAL_TABLE_CONFIG_FIELD_NUMBER: _ClassVar[int]
        PARTITION_EXPRESSION_FIELD_NUMBER: _ClassVar[int]
        CLUSTER_EXPRESSIONS_FIELD_NUMBER: _ClassVar[int]
        PARTITION_EXPIRATION_DAYS_FIELD_NUMBER: _ClassVar[int]
        REQUIRE_PARTITION_FILTER_FIELD_NUMBER: _ClassVar[int]
        ADDITIONAL_OPTIONS_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        relation_descriptor: RelationDescriptor
        relation_type: CompilationResultAction.Relation.RelationType
        select_query: str
        pre_operations: _containers.RepeatedScalarFieldContainer[str]
        post_operations: _containers.RepeatedScalarFieldContainer[str]
        incremental_table_config: CompilationResultAction.Relation.IncrementalTableConfig
        partition_expression: str
        cluster_expressions: _containers.RepeatedScalarFieldContainer[str]
        partition_expiration_days: int
        require_partition_filter: bool
        additional_options: _containers.ScalarMap[str, str]

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=..., relation_type: _Optional[_Union[CompilationResultAction.Relation.RelationType, str]]=..., select_query: _Optional[str]=..., pre_operations: _Optional[_Iterable[str]]=..., post_operations: _Optional[_Iterable[str]]=..., incremental_table_config: _Optional[_Union[CompilationResultAction.Relation.IncrementalTableConfig, _Mapping]]=..., partition_expression: _Optional[str]=..., cluster_expressions: _Optional[_Iterable[str]]=..., partition_expiration_days: _Optional[int]=..., require_partition_filter: bool=..., additional_options: _Optional[_Mapping[str, str]]=...) -> None:
            ...

    class Operations(_message.Message):
        __slots__ = ('dependency_targets', 'disabled', 'tags', 'relation_descriptor', 'queries', 'has_output')
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        QUERIES_FIELD_NUMBER: _ClassVar[int]
        HAS_OUTPUT_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        relation_descriptor: RelationDescriptor
        queries: _containers.RepeatedScalarFieldContainer[str]
        has_output: bool

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=..., queries: _Optional[_Iterable[str]]=..., has_output: bool=...) -> None:
            ...

    class Assertion(_message.Message):
        __slots__ = ('dependency_targets', 'parent_action', 'disabled', 'tags', 'select_query', 'relation_descriptor')
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        PARENT_ACTION_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        SELECT_QUERY_FIELD_NUMBER: _ClassVar[int]
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        parent_action: Target
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]
        select_query: str
        relation_descriptor: RelationDescriptor

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., parent_action: _Optional[_Union[Target, _Mapping]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=..., select_query: _Optional[str]=..., relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=...) -> None:
            ...

    class Declaration(_message.Message):
        __slots__ = ('relation_descriptor',)
        RELATION_DESCRIPTOR_FIELD_NUMBER: _ClassVar[int]
        relation_descriptor: RelationDescriptor

        def __init__(self, relation_descriptor: _Optional[_Union[RelationDescriptor, _Mapping]]=...) -> None:
            ...

    class Notebook(_message.Message):
        __slots__ = ('dependency_targets', 'disabled', 'contents', 'tags')
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        contents: str
        tags: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., contents: _Optional[str]=..., tags: _Optional[_Iterable[str]]=...) -> None:
            ...

    class DataPreparation(_message.Message):
        __slots__ = ('contents_yaml', 'contents_sql', 'dependency_targets', 'disabled', 'tags')

        class SqlDefinition(_message.Message):
            __slots__ = ('query', 'error_table', 'load')
            QUERY_FIELD_NUMBER: _ClassVar[int]
            ERROR_TABLE_FIELD_NUMBER: _ClassVar[int]
            LOAD_FIELD_NUMBER: _ClassVar[int]
            query: str
            error_table: CompilationResultAction.DataPreparation.ErrorTable
            load: CompilationResultAction.LoadConfig

            def __init__(self, query: _Optional[str]=..., error_table: _Optional[_Union[CompilationResultAction.DataPreparation.ErrorTable, _Mapping]]=..., load: _Optional[_Union[CompilationResultAction.LoadConfig, _Mapping]]=...) -> None:
                ...

        class ErrorTable(_message.Message):
            __slots__ = ('target', 'retention_days')
            TARGET_FIELD_NUMBER: _ClassVar[int]
            RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
            target: Target
            retention_days: int

            def __init__(self, target: _Optional[_Union[Target, _Mapping]]=..., retention_days: _Optional[int]=...) -> None:
                ...
        CONTENTS_YAML_FIELD_NUMBER: _ClassVar[int]
        CONTENTS_SQL_FIELD_NUMBER: _ClassVar[int]
        DEPENDENCY_TARGETS_FIELD_NUMBER: _ClassVar[int]
        DISABLED_FIELD_NUMBER: _ClassVar[int]
        TAGS_FIELD_NUMBER: _ClassVar[int]
        contents_yaml: str
        contents_sql: CompilationResultAction.DataPreparation.SqlDefinition
        dependency_targets: _containers.RepeatedCompositeFieldContainer[Target]
        disabled: bool
        tags: _containers.RepeatedScalarFieldContainer[str]

        def __init__(self, contents_yaml: _Optional[str]=..., contents_sql: _Optional[_Union[CompilationResultAction.DataPreparation.SqlDefinition, _Mapping]]=..., dependency_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., disabled: bool=..., tags: _Optional[_Iterable[str]]=...) -> None:
            ...

    class LoadConfig(_message.Message):
        __slots__ = ('replace', 'append', 'maximum', 'unique')
        REPLACE_FIELD_NUMBER: _ClassVar[int]
        APPEND_FIELD_NUMBER: _ClassVar[int]
        MAXIMUM_FIELD_NUMBER: _ClassVar[int]
        UNIQUE_FIELD_NUMBER: _ClassVar[int]
        replace: CompilationResultAction.SimpleLoadMode
        append: CompilationResultAction.SimpleLoadMode
        maximum: CompilationResultAction.IncrementalLoadMode
        unique: CompilationResultAction.IncrementalLoadMode

        def __init__(self, replace: _Optional[_Union[CompilationResultAction.SimpleLoadMode, _Mapping]]=..., append: _Optional[_Union[CompilationResultAction.SimpleLoadMode, _Mapping]]=..., maximum: _Optional[_Union[CompilationResultAction.IncrementalLoadMode, _Mapping]]=..., unique: _Optional[_Union[CompilationResultAction.IncrementalLoadMode, _Mapping]]=...) -> None:
            ...

    class SimpleLoadMode(_message.Message):
        __slots__ = ()

        def __init__(self) -> None:
            ...

    class IncrementalLoadMode(_message.Message):
        __slots__ = ('column',)
        COLUMN_FIELD_NUMBER: _ClassVar[int]
        column: str

        def __init__(self, column: _Optional[str]=...) -> None:
            ...
    RELATION_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    ASSERTION_FIELD_NUMBER: _ClassVar[int]
    DECLARATION_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_FIELD_NUMBER: _ClassVar[int]
    DATA_PREPARATION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    relation: CompilationResultAction.Relation
    operations: CompilationResultAction.Operations
    assertion: CompilationResultAction.Assertion
    declaration: CompilationResultAction.Declaration
    notebook: CompilationResultAction.Notebook
    data_preparation: CompilationResultAction.DataPreparation
    target: Target
    canonical_target: Target
    file_path: str
    internal_metadata: str

    def __init__(self, relation: _Optional[_Union[CompilationResultAction.Relation, _Mapping]]=..., operations: _Optional[_Union[CompilationResultAction.Operations, _Mapping]]=..., assertion: _Optional[_Union[CompilationResultAction.Assertion, _Mapping]]=..., declaration: _Optional[_Union[CompilationResultAction.Declaration, _Mapping]]=..., notebook: _Optional[_Union[CompilationResultAction.Notebook, _Mapping]]=..., data_preparation: _Optional[_Union[CompilationResultAction.DataPreparation, _Mapping]]=..., target: _Optional[_Union[Target, _Mapping]]=..., canonical_target: _Optional[_Union[Target, _Mapping]]=..., file_path: _Optional[str]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class QueryCompilationResultActionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token', 'filter')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str
    filter: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class QueryCompilationResultActionsResponse(_message.Message):
    __slots__ = ('compilation_result_actions', 'next_page_token')
    COMPILATION_RESULT_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    compilation_result_actions: _containers.RepeatedCompositeFieldContainer[CompilationResultAction]
    next_page_token: str

    def __init__(self, compilation_result_actions: _Optional[_Iterable[_Union[CompilationResultAction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class WorkflowConfig(_message.Message):
    __slots__ = ('name', 'release_config', 'invocation_config', 'cron_schedule', 'time_zone', 'recent_scheduled_execution_records', 'disabled', 'create_time', 'update_time', 'internal_metadata')

    class ScheduledExecutionRecord(_message.Message):
        __slots__ = ('workflow_invocation', 'error_status', 'execution_time')
        WORKFLOW_INVOCATION_FIELD_NUMBER: _ClassVar[int]
        ERROR_STATUS_FIELD_NUMBER: _ClassVar[int]
        EXECUTION_TIME_FIELD_NUMBER: _ClassVar[int]
        workflow_invocation: str
        error_status: _status_pb2.Status
        execution_time: _timestamp_pb2.Timestamp

        def __init__(self, workflow_invocation: _Optional[str]=..., error_status: _Optional[_Union[_status_pb2.Status, _Mapping]]=..., execution_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    RELEASE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    CRON_SCHEDULE_FIELD_NUMBER: _ClassVar[int]
    TIME_ZONE_FIELD_NUMBER: _ClassVar[int]
    RECENT_SCHEDULED_EXECUTION_RECORDS_FIELD_NUMBER: _ClassVar[int]
    DISABLED_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    name: str
    release_config: str
    invocation_config: InvocationConfig
    cron_schedule: str
    time_zone: str
    recent_scheduled_execution_records: _containers.RepeatedCompositeFieldContainer[WorkflowConfig.ScheduledExecutionRecord]
    disabled: bool
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    internal_metadata: str

    def __init__(self, name: _Optional[str]=..., release_config: _Optional[str]=..., invocation_config: _Optional[_Union[InvocationConfig, _Mapping]]=..., cron_schedule: _Optional[str]=..., time_zone: _Optional[str]=..., recent_scheduled_execution_records: _Optional[_Iterable[_Union[WorkflowConfig.ScheduledExecutionRecord, _Mapping]]]=..., disabled: bool=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class InvocationConfig(_message.Message):
    __slots__ = ('included_targets', 'included_tags', 'transitive_dependencies_included', 'transitive_dependents_included', 'fully_refresh_incremental_tables_enabled', 'service_account')
    INCLUDED_TARGETS_FIELD_NUMBER: _ClassVar[int]
    INCLUDED_TAGS_FIELD_NUMBER: _ClassVar[int]
    TRANSITIVE_DEPENDENCIES_INCLUDED_FIELD_NUMBER: _ClassVar[int]
    TRANSITIVE_DEPENDENTS_INCLUDED_FIELD_NUMBER: _ClassVar[int]
    FULLY_REFRESH_INCREMENTAL_TABLES_ENABLED_FIELD_NUMBER: _ClassVar[int]
    SERVICE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    included_targets: _containers.RepeatedCompositeFieldContainer[Target]
    included_tags: _containers.RepeatedScalarFieldContainer[str]
    transitive_dependencies_included: bool
    transitive_dependents_included: bool
    fully_refresh_incremental_tables_enabled: bool
    service_account: str

    def __init__(self, included_targets: _Optional[_Iterable[_Union[Target, _Mapping]]]=..., included_tags: _Optional[_Iterable[str]]=..., transitive_dependencies_included: bool=..., transitive_dependents_included: bool=..., fully_refresh_incremental_tables_enabled: bool=..., service_account: _Optional[str]=...) -> None:
        ...

class ListWorkflowConfigsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListWorkflowConfigsResponse(_message.Message):
    __slots__ = ('workflow_configs', 'next_page_token', 'unreachable')
    WORKFLOW_CONFIGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workflow_configs: _containers.RepeatedCompositeFieldContainer[WorkflowConfig]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workflow_configs: _Optional[_Iterable[_Union[WorkflowConfig, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkflowConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkflowConfigRequest(_message.Message):
    __slots__ = ('parent', 'workflow_config', 'workflow_config_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workflow_config: WorkflowConfig
    workflow_config_id: str

    def __init__(self, parent: _Optional[str]=..., workflow_config: _Optional[_Union[WorkflowConfig, _Mapping]]=..., workflow_config_id: _Optional[str]=...) -> None:
        ...

class UpdateWorkflowConfigRequest(_message.Message):
    __slots__ = ('update_mask', 'workflow_config')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    workflow_config: WorkflowConfig

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., workflow_config: _Optional[_Union[WorkflowConfig, _Mapping]]=...) -> None:
        ...

class DeleteWorkflowConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class WorkflowInvocation(_message.Message):
    __slots__ = ('compilation_result', 'workflow_config', 'name', 'invocation_config', 'state', 'invocation_timing', 'resolved_compilation_result', 'data_encryption_state', 'internal_metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[WorkflowInvocation.State]
        RUNNING: _ClassVar[WorkflowInvocation.State]
        SUCCEEDED: _ClassVar[WorkflowInvocation.State]
        CANCELLED: _ClassVar[WorkflowInvocation.State]
        FAILED: _ClassVar[WorkflowInvocation.State]
        CANCELING: _ClassVar[WorkflowInvocation.State]
    STATE_UNSPECIFIED: WorkflowInvocation.State
    RUNNING: WorkflowInvocation.State
    SUCCEEDED: WorkflowInvocation.State
    CANCELLED: WorkflowInvocation.State
    FAILED: WorkflowInvocation.State
    CANCELING: WorkflowInvocation.State
    COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_CONFIG_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIMING_FIELD_NUMBER: _ClassVar[int]
    RESOLVED_COMPILATION_RESULT_FIELD_NUMBER: _ClassVar[int]
    DATA_ENCRYPTION_STATE_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    compilation_result: str
    workflow_config: str
    name: str
    invocation_config: InvocationConfig
    state: WorkflowInvocation.State
    invocation_timing: _interval_pb2.Interval
    resolved_compilation_result: str
    data_encryption_state: DataEncryptionState
    internal_metadata: str

    def __init__(self, compilation_result: _Optional[str]=..., workflow_config: _Optional[str]=..., name: _Optional[str]=..., invocation_config: _Optional[_Union[InvocationConfig, _Mapping]]=..., state: _Optional[_Union[WorkflowInvocation.State, str]]=..., invocation_timing: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., resolved_compilation_result: _Optional[str]=..., data_encryption_state: _Optional[_Union[DataEncryptionState, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class ListWorkflowInvocationsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token', 'order_by', 'filter')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ORDER_BY_FIELD_NUMBER: _ClassVar[int]
    FILTER_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str
    order_by: str
    filter: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=..., order_by: _Optional[str]=..., filter: _Optional[str]=...) -> None:
        ...

class ListWorkflowInvocationsResponse(_message.Message):
    __slots__ = ('workflow_invocations', 'next_page_token', 'unreachable')
    WORKFLOW_INVOCATIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    UNREACHABLE_FIELD_NUMBER: _ClassVar[int]
    workflow_invocations: _containers.RepeatedCompositeFieldContainer[WorkflowInvocation]
    next_page_token: str
    unreachable: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, workflow_invocations: _Optional[_Iterable[_Union[WorkflowInvocation, _Mapping]]]=..., next_page_token: _Optional[str]=..., unreachable: _Optional[_Iterable[str]]=...) -> None:
        ...

class GetWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateWorkflowInvocationRequest(_message.Message):
    __slots__ = ('parent', 'workflow_invocation')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    WORKFLOW_INVOCATION_FIELD_NUMBER: _ClassVar[int]
    parent: str
    workflow_invocation: WorkflowInvocation

    def __init__(self, parent: _Optional[str]=..., workflow_invocation: _Optional[_Union[WorkflowInvocation, _Mapping]]=...) -> None:
        ...

class DeleteWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelWorkflowInvocationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CancelWorkflowInvocationResponse(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class WorkflowInvocationAction(_message.Message):
    __slots__ = ('bigquery_action', 'notebook_action', 'data_preparation_action', 'target', 'canonical_target', 'state', 'failure_reason', 'invocation_timing', 'internal_metadata')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PENDING: _ClassVar[WorkflowInvocationAction.State]
        RUNNING: _ClassVar[WorkflowInvocationAction.State]
        SKIPPED: _ClassVar[WorkflowInvocationAction.State]
        DISABLED: _ClassVar[WorkflowInvocationAction.State]
        SUCCEEDED: _ClassVar[WorkflowInvocationAction.State]
        CANCELLED: _ClassVar[WorkflowInvocationAction.State]
        FAILED: _ClassVar[WorkflowInvocationAction.State]
    PENDING: WorkflowInvocationAction.State
    RUNNING: WorkflowInvocationAction.State
    SKIPPED: WorkflowInvocationAction.State
    DISABLED: WorkflowInvocationAction.State
    SUCCEEDED: WorkflowInvocationAction.State
    CANCELLED: WorkflowInvocationAction.State
    FAILED: WorkflowInvocationAction.State

    class BigQueryAction(_message.Message):
        __slots__ = ('sql_script', 'job_id')
        SQL_SCRIPT_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        sql_script: str
        job_id: str

        def __init__(self, sql_script: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
            ...

    class NotebookAction(_message.Message):
        __slots__ = ('contents', 'job_id')
        CONTENTS_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        contents: str
        job_id: str

        def __init__(self, contents: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
            ...

    class DataPreparationAction(_message.Message):
        __slots__ = ('contents_yaml', 'contents_sql', 'generated_sql', 'job_id')

        class ActionSqlDefinition(_message.Message):
            __slots__ = ('query', 'error_table', 'load_config')
            QUERY_FIELD_NUMBER: _ClassVar[int]
            ERROR_TABLE_FIELD_NUMBER: _ClassVar[int]
            LOAD_CONFIG_FIELD_NUMBER: _ClassVar[int]
            query: str
            error_table: WorkflowInvocationAction.DataPreparationAction.ActionErrorTable
            load_config: WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig

            def __init__(self, query: _Optional[str]=..., error_table: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionErrorTable, _Mapping]]=..., load_config: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionLoadConfig, _Mapping]]=...) -> None:
                ...

        class ActionErrorTable(_message.Message):
            __slots__ = ('target', 'retention_days')
            TARGET_FIELD_NUMBER: _ClassVar[int]
            RETENTION_DAYS_FIELD_NUMBER: _ClassVar[int]
            target: Target
            retention_days: int

            def __init__(self, target: _Optional[_Union[Target, _Mapping]]=..., retention_days: _Optional[int]=...) -> None:
                ...

        class ActionLoadConfig(_message.Message):
            __slots__ = ('replace', 'append', 'maximum', 'unique')
            REPLACE_FIELD_NUMBER: _ClassVar[int]
            APPEND_FIELD_NUMBER: _ClassVar[int]
            MAXIMUM_FIELD_NUMBER: _ClassVar[int]
            UNIQUE_FIELD_NUMBER: _ClassVar[int]
            replace: WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode
            append: WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode
            maximum: WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode
            unique: WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode

            def __init__(self, replace: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode, _Mapping]]=..., append: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionSimpleLoadMode, _Mapping]]=..., maximum: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode, _Mapping]]=..., unique: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionIncrementalLoadMode, _Mapping]]=...) -> None:
                ...

        class ActionSimpleLoadMode(_message.Message):
            __slots__ = ()

            def __init__(self) -> None:
                ...

        class ActionIncrementalLoadMode(_message.Message):
            __slots__ = ('column',)
            COLUMN_FIELD_NUMBER: _ClassVar[int]
            column: str

            def __init__(self, column: _Optional[str]=...) -> None:
                ...
        CONTENTS_YAML_FIELD_NUMBER: _ClassVar[int]
        CONTENTS_SQL_FIELD_NUMBER: _ClassVar[int]
        GENERATED_SQL_FIELD_NUMBER: _ClassVar[int]
        JOB_ID_FIELD_NUMBER: _ClassVar[int]
        contents_yaml: str
        contents_sql: WorkflowInvocationAction.DataPreparationAction.ActionSqlDefinition
        generated_sql: str
        job_id: str

        def __init__(self, contents_yaml: _Optional[str]=..., contents_sql: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction.ActionSqlDefinition, _Mapping]]=..., generated_sql: _Optional[str]=..., job_id: _Optional[str]=...) -> None:
            ...
    BIGQUERY_ACTION_FIELD_NUMBER: _ClassVar[int]
    NOTEBOOK_ACTION_FIELD_NUMBER: _ClassVar[int]
    DATA_PREPARATION_ACTION_FIELD_NUMBER: _ClassVar[int]
    TARGET_FIELD_NUMBER: _ClassVar[int]
    CANONICAL_TARGET_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FAILURE_REASON_FIELD_NUMBER: _ClassVar[int]
    INVOCATION_TIMING_FIELD_NUMBER: _ClassVar[int]
    INTERNAL_METADATA_FIELD_NUMBER: _ClassVar[int]
    bigquery_action: WorkflowInvocationAction.BigQueryAction
    notebook_action: WorkflowInvocationAction.NotebookAction
    data_preparation_action: WorkflowInvocationAction.DataPreparationAction
    target: Target
    canonical_target: Target
    state: WorkflowInvocationAction.State
    failure_reason: str
    invocation_timing: _interval_pb2.Interval
    internal_metadata: str

    def __init__(self, bigquery_action: _Optional[_Union[WorkflowInvocationAction.BigQueryAction, _Mapping]]=..., notebook_action: _Optional[_Union[WorkflowInvocationAction.NotebookAction, _Mapping]]=..., data_preparation_action: _Optional[_Union[WorkflowInvocationAction.DataPreparationAction, _Mapping]]=..., target: _Optional[_Union[Target, _Mapping]]=..., canonical_target: _Optional[_Union[Target, _Mapping]]=..., state: _Optional[_Union[WorkflowInvocationAction.State, str]]=..., failure_reason: _Optional[str]=..., invocation_timing: _Optional[_Union[_interval_pb2.Interval, _Mapping]]=..., internal_metadata: _Optional[str]=...) -> None:
        ...

class QueryWorkflowInvocationActionsRequest(_message.Message):
    __slots__ = ('name', 'page_size', 'page_token')
    NAME_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    name: str
    page_size: int
    page_token: str

    def __init__(self, name: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class QueryWorkflowInvocationActionsResponse(_message.Message):
    __slots__ = ('workflow_invocation_actions', 'next_page_token')
    WORKFLOW_INVOCATION_ACTIONS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    workflow_invocation_actions: _containers.RepeatedCompositeFieldContainer[WorkflowInvocationAction]
    next_page_token: str

    def __init__(self, workflow_invocation_actions: _Optional[_Iterable[_Union[WorkflowInvocationAction, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class Config(_message.Message):
    __slots__ = ('name', 'default_kms_key_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_KMS_KEY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    default_kms_key_name: str

    def __init__(self, name: _Optional[str]=..., default_kms_key_name: _Optional[str]=...) -> None:
        ...

class GetConfigRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateConfigRequest(_message.Message):
    __slots__ = ('config', 'update_mask')
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    config: Config
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, config: _Optional[_Union[Config, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...