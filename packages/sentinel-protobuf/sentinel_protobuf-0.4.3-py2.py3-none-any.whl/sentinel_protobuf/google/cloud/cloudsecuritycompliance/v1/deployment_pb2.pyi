from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.cloud.cloudsecuritycompliance.v1 import common_pb2 as _common_pb2
from google.longrunning import operations_pb2 as _operations_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STATE_UNSPECIFIED: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_VALIDATING: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_CREATING: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_DELETING: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_FAILED: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_READY: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_PARTIALLY_DEPLOYED: _ClassVar[DeploymentState]
    DEPLOYMENT_STATE_PARTIALLY_DELETED: _ClassVar[DeploymentState]
DEPLOYMENT_STATE_UNSPECIFIED: DeploymentState
DEPLOYMENT_STATE_VALIDATING: DeploymentState
DEPLOYMENT_STATE_CREATING: DeploymentState
DEPLOYMENT_STATE_DELETING: DeploymentState
DEPLOYMENT_STATE_FAILED: DeploymentState
DEPLOYMENT_STATE_READY: DeploymentState
DEPLOYMENT_STATE_PARTIALLY_DEPLOYED: DeploymentState
DEPLOYMENT_STATE_PARTIALLY_DELETED: DeploymentState

class FrameworkDeployment(_message.Message):
    __slots__ = ('name', 'target_resource_config', 'computed_target_resource', 'framework', 'description', 'cloud_control_metadata', 'deployment_state', 'create_time', 'update_time', 'etag', 'target_resource_display_name', 'cloud_control_deployment_references')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    COMPUTED_TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_METADATA_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_DEPLOYMENT_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_resource_config: TargetResourceConfig
    computed_target_resource: str
    framework: _common_pb2.FrameworkReference
    description: str
    cloud_control_metadata: _containers.RepeatedCompositeFieldContainer[CloudControlMetadata]
    deployment_state: DeploymentState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    target_resource_display_name: str
    cloud_control_deployment_references: _containers.RepeatedCompositeFieldContainer[CloudControlDeploymentReference]

    def __init__(self, name: _Optional[str]=..., target_resource_config: _Optional[_Union[TargetResourceConfig, _Mapping]]=..., computed_target_resource: _Optional[str]=..., framework: _Optional[_Union[_common_pb2.FrameworkReference, _Mapping]]=..., description: _Optional[str]=..., cloud_control_metadata: _Optional[_Iterable[_Union[CloudControlMetadata, _Mapping]]]=..., deployment_state: _Optional[_Union[DeploymentState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., target_resource_display_name: _Optional[str]=..., cloud_control_deployment_references: _Optional[_Iterable[_Union[CloudControlDeploymentReference, _Mapping]]]=...) -> None:
        ...

class CloudControlDeployment(_message.Message):
    __slots__ = ('name', 'target_resource_config', 'target_resource', 'cloud_control_metadata', 'description', 'deployment_state', 'create_time', 'update_time', 'etag', 'parameter_substituted_cloud_control', 'framework_deployment_references', 'target_resource_display_name')
    NAME_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_CONFIG_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    CLOUD_CONTROL_METADATA_FIELD_NUMBER: _ClassVar[int]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DEPLOYMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIME_FIELD_NUMBER: _ClassVar[int]
    UPDATE_TIME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_SUBSTITUTED_CLOUD_CONTROL_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_DEPLOYMENT_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    target_resource_config: TargetResourceConfig
    target_resource: str
    cloud_control_metadata: CloudControlMetadata
    description: str
    deployment_state: DeploymentState
    create_time: _timestamp_pb2.Timestamp
    update_time: _timestamp_pb2.Timestamp
    etag: str
    parameter_substituted_cloud_control: _common_pb2.CloudControl
    framework_deployment_references: _containers.RepeatedCompositeFieldContainer[FrameworkDeploymentReference]
    target_resource_display_name: str

    def __init__(self, name: _Optional[str]=..., target_resource_config: _Optional[_Union[TargetResourceConfig, _Mapping]]=..., target_resource: _Optional[str]=..., cloud_control_metadata: _Optional[_Union[CloudControlMetadata, _Mapping]]=..., description: _Optional[str]=..., deployment_state: _Optional[_Union[DeploymentState, str]]=..., create_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., update_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., etag: _Optional[str]=..., parameter_substituted_cloud_control: _Optional[_Union[_common_pb2.CloudControl, _Mapping]]=..., framework_deployment_references: _Optional[_Iterable[_Union[FrameworkDeploymentReference, _Mapping]]]=..., target_resource_display_name: _Optional[str]=...) -> None:
        ...

class TargetResourceConfig(_message.Message):
    __slots__ = ('existing_target_resource', 'target_resource_creation_config')
    EXISTING_TARGET_RESOURCE_FIELD_NUMBER: _ClassVar[int]
    TARGET_RESOURCE_CREATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    existing_target_resource: str
    target_resource_creation_config: TargetResourceCreationConfig

    def __init__(self, existing_target_resource: _Optional[str]=..., target_resource_creation_config: _Optional[_Union[TargetResourceCreationConfig, _Mapping]]=...) -> None:
        ...

class TargetResourceCreationConfig(_message.Message):
    __slots__ = ('folder_creation_config', 'project_creation_config')
    FOLDER_CREATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    PROJECT_CREATION_CONFIG_FIELD_NUMBER: _ClassVar[int]
    folder_creation_config: FolderCreationConfig
    project_creation_config: ProjectCreationConfig

    def __init__(self, folder_creation_config: _Optional[_Union[FolderCreationConfig, _Mapping]]=..., project_creation_config: _Optional[_Union[ProjectCreationConfig, _Mapping]]=...) -> None:
        ...

class FolderCreationConfig(_message.Message):
    __slots__ = ('parent', 'folder_display_name')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FOLDER_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    parent: str
    folder_display_name: str

    def __init__(self, parent: _Optional[str]=..., folder_display_name: _Optional[str]=...) -> None:
        ...

class ProjectCreationConfig(_message.Message):
    __slots__ = ('parent', 'project_display_name', 'billing_account_id')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PROJECT_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    BILLING_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    parent: str
    project_display_name: str
    billing_account_id: str

    def __init__(self, parent: _Optional[str]=..., project_display_name: _Optional[str]=..., billing_account_id: _Optional[str]=...) -> None:
        ...

class CloudControlMetadata(_message.Message):
    __slots__ = ('cloud_control_details', 'enforcement_mode')
    CLOUD_CONTROL_DETAILS_FIELD_NUMBER: _ClassVar[int]
    ENFORCEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    cloud_control_details: _common_pb2.CloudControlDetails
    enforcement_mode: _common_pb2.EnforcementMode

    def __init__(self, cloud_control_details: _Optional[_Union[_common_pb2.CloudControlDetails, _Mapping]]=..., enforcement_mode: _Optional[_Union[_common_pb2.EnforcementMode, str]]=...) -> None:
        ...

class CreateFrameworkDeploymentRequest(_message.Message):
    __slots__ = ('parent', 'framework_deployment_id', 'framework_deployment')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_DEPLOYMENT_ID_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    parent: str
    framework_deployment_id: str
    framework_deployment: FrameworkDeployment

    def __init__(self, parent: _Optional[str]=..., framework_deployment_id: _Optional[str]=..., framework_deployment: _Optional[_Union[FrameworkDeployment, _Mapping]]=...) -> None:
        ...

class DeleteFrameworkDeploymentRequest(_message.Message):
    __slots__ = ('name', 'etag')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ETAG_FIELD_NUMBER: _ClassVar[int]
    name: str
    etag: str

    def __init__(self, name: _Optional[str]=..., etag: _Optional[str]=...) -> None:
        ...

class GetFrameworkDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListFrameworkDeploymentsRequest(_message.Message):
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

class ListFrameworkDeploymentsResponse(_message.Message):
    __slots__ = ('framework_deployments', 'next_page_token')
    FRAMEWORK_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    framework_deployments: _containers.RepeatedCompositeFieldContainer[FrameworkDeployment]
    next_page_token: str

    def __init__(self, framework_deployments: _Optional[_Iterable[_Union[FrameworkDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class GetCloudControlDeploymentRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListCloudControlDeploymentsRequest(_message.Message):
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

class ListCloudControlDeploymentsResponse(_message.Message):
    __slots__ = ('cloud_control_deployments', 'next_page_token')
    CLOUD_CONTROL_DEPLOYMENTS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    cloud_control_deployments: _containers.RepeatedCompositeFieldContainer[CloudControlDeployment]
    next_page_token: str

    def __init__(self, cloud_control_deployments: _Optional[_Iterable[_Union[CloudControlDeployment, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CloudControlDeploymentReference(_message.Message):
    __slots__ = ('cloud_control_deployment',)
    CLOUD_CONTROL_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    cloud_control_deployment: str

    def __init__(self, cloud_control_deployment: _Optional[str]=...) -> None:
        ...

class FrameworkDeploymentReference(_message.Message):
    __slots__ = ('framework_deployment', 'framework_reference', 'framework_display_name')
    FRAMEWORK_DEPLOYMENT_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    FRAMEWORK_DISPLAY_NAME_FIELD_NUMBER: _ClassVar[int]
    framework_deployment: str
    framework_reference: _common_pb2.FrameworkReference
    framework_display_name: str

    def __init__(self, framework_deployment: _Optional[str]=..., framework_reference: _Optional[_Union[_common_pb2.FrameworkReference, _Mapping]]=..., framework_display_name: _Optional[str]=...) -> None:
        ...