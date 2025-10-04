from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar
DESCRIPTOR: _descriptor.FileDescriptor

class DeploymentStage(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    DEPLOYMENT_STAGE_UNSPECIFIED: _ClassVar[DeploymentStage]
    STARTING_DEPLOYMENT: _ClassVar[DeploymentStage]
    PREPARING_MODEL: _ClassVar[DeploymentStage]
    CREATING_SERVING_CLUSTER: _ClassVar[DeploymentStage]
    ADDING_NODES_TO_CLUSTER: _ClassVar[DeploymentStage]
    GETTING_CONTAINER_IMAGE: _ClassVar[DeploymentStage]
    STARTING_MODEL_SERVER: _ClassVar[DeploymentStage]
    FINISHING_UP: _ClassVar[DeploymentStage]
    DEPLOYMENT_TERMINATED: _ClassVar[DeploymentStage]
DEPLOYMENT_STAGE_UNSPECIFIED: DeploymentStage
STARTING_DEPLOYMENT: DeploymentStage
PREPARING_MODEL: DeploymentStage
CREATING_SERVING_CLUSTER: DeploymentStage
ADDING_NODES_TO_CLUSTER: DeploymentStage
GETTING_CONTAINER_IMAGE: DeploymentStage
STARTING_MODEL_SERVER: DeploymentStage
FINISHING_UP: DeploymentStage
DEPLOYMENT_TERMINATED: DeploymentStage