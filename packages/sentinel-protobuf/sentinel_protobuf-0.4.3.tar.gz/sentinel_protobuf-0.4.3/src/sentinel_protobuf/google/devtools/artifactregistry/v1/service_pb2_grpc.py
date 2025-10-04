"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.devtools.artifactregistry.v1 import apt_artifact_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_apt__artifact__pb2
from .....google.devtools.artifactregistry.v1 import artifact_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2
from .....google.devtools.artifactregistry.v1 import attachment_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2
from .....google.devtools.artifactregistry.v1 import file_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2
from .....google.devtools.artifactregistry.v1 import package_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2
from .....google.devtools.artifactregistry.v1 import repository_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2
from .....google.devtools.artifactregistry.v1 import rule_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2
from .....google.devtools.artifactregistry.v1 import settings_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2
from .....google.devtools.artifactregistry.v1 import tag_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2
from .....google.devtools.artifactregistry.v1 import version_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2
from .....google.devtools.artifactregistry.v1 import vpcsc_config_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2
from .....google.devtools.artifactregistry.v1 import yum_artifact_pb2 as google_dot_devtools_dot_artifactregistry_dot_v1_dot_yum__artifact__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/devtools/artifactregistry/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class ArtifactRegistryStub(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListDockerImages = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListDockerImages', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesResponse.FromString, _registered_method=True)
        self.GetDockerImage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetDockerImage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetDockerImageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.DockerImage.FromString, _registered_method=True)
        self.ListMavenArtifacts = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListMavenArtifacts', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsResponse.FromString, _registered_method=True)
        self.GetMavenArtifact = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetMavenArtifact', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetMavenArtifactRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.MavenArtifact.FromString, _registered_method=True)
        self.ListNpmPackages = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListNpmPackages', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesResponse.FromString, _registered_method=True)
        self.GetNpmPackage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetNpmPackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetNpmPackageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.NpmPackage.FromString, _registered_method=True)
        self.ListPythonPackages = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPythonPackages', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesResponse.FromString, _registered_method=True)
        self.GetPythonPackage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPythonPackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetPythonPackageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.PythonPackage.FromString, _registered_method=True)
        self.ImportAptArtifacts = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportAptArtifacts', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_apt__artifact__pb2.ImportAptArtifactsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ImportYumArtifacts = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportYumArtifacts', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_yum__artifact__pb2.ImportYumArtifactsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListRepositories = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRepositories', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesResponse.FromString, _registered_method=True)
        self.GetRepository = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.GetRepositoryRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.FromString, _registered_method=True)
        self.CreateRepository = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.CreateRepositoryRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateRepository = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.FromString, _registered_method=True)
        self.DeleteRepository = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRepository', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.DeleteRepositoryRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListPackages = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPackages', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesResponse.FromString, _registered_method=True)
        self.GetPackage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.GetPackageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.FromString, _registered_method=True)
        self.DeletePackage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeletePackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.DeletePackageRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.ListVersions = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListVersions', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsResponse.FromString, _registered_method=True)
        self.GetVersion = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVersion', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.GetVersionRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.FromString, _registered_method=True)
        self.DeleteVersion = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteVersion', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.DeleteVersionRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.BatchDeleteVersions = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/BatchDeleteVersions', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.BatchDeleteVersionsRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateVersion = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVersion', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.UpdateVersionRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.FromString, _registered_method=True)
        self.ListFiles = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListFiles', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesResponse.FromString, _registered_method=True)
        self.GetFile = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetFile', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.GetFileRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.FromString, _registered_method=True)
        self.DeleteFile = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteFile', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.DeleteFileRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateFile = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateFile', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.UpdateFileRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.FromString, _registered_method=True)
        self.ListTags = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListTags', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsResponse.FromString, _registered_method=True)
        self.GetTag = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.GetTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.CreateTag = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.CreateTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.UpdateTag = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.UpdateTagRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, _registered_method=True)
        self.DeleteTag = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteTag', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.DeleteTagRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.CreateRule = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRule', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.CreateRuleRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, _registered_method=True)
        self.ListRules = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRules', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesResponse.FromString, _registered_method=True)
        self.GetRule = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRule', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.GetRuleRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, _registered_method=True)
        self.UpdateRule = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRule', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.UpdateRuleRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, _registered_method=True)
        self.DeleteRule = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRule', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.DeleteRuleRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.SetIamPolicy = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/SetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.GetIamPolicy = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.TestIamPermissions = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/TestIamPermissions', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, _registered_method=True)
        self.GetProjectSettings = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetProjectSettings', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.GetProjectSettingsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.FromString, _registered_method=True)
        self.UpdateProjectSettings = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateProjectSettings', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.UpdateProjectSettingsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.FromString, _registered_method=True)
        self.GetVPCSCConfig = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVPCSCConfig', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.GetVPCSCConfigRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.FromString, _registered_method=True)
        self.UpdateVPCSCConfig = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVPCSCConfig', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.UpdateVPCSCConfigRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.FromString, _registered_method=True)
        self.UpdatePackage = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdatePackage', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.UpdatePackageRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.FromString, _registered_method=True)
        self.ListAttachments = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/ListAttachments', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.FromString, _registered_method=True)
        self.GetAttachment = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/GetAttachment', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.GetAttachmentRequest.SerializeToString, response_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.Attachment.FromString, _registered_method=True)
        self.CreateAttachment = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateAttachment', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteAttachment = channel.unary_unary('/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteAttachment', request_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class ArtifactRegistryServicer(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    def ListDockerImages(self, request, context):
        """Lists docker images.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDockerImage(self, request, context):
        """Gets a docker image.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMavenArtifacts(self, request, context):
        """Lists maven artifacts.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMavenArtifact(self, request, context):
        """Gets a maven artifact.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListNpmPackages(self, request, context):
        """Lists npm packages.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetNpmPackage(self, request, context):
        """Gets a npm package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPythonPackages(self, request, context):
        """Lists python packages.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPythonPackage(self, request, context):
        """Gets a python package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportAptArtifacts(self, request, context):
        """Imports Apt artifacts. The returned Operation will complete once the
        resources are imported. Package, Version, and File resources are created
        based on the imported artifacts. Imported artifacts that conflict with
        existing resources are ignored.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImportYumArtifacts(self, request, context):
        """Imports Yum (RPM) artifacts. The returned Operation will complete once the
        resources are imported. Package, Version, and File resources are created
        based on the imported artifacts. Imported artifacts that conflict with
        existing resources are ignored.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRepositories(self, request, context):
        """Lists repositories.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRepository(self, request, context):
        """Gets a repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRepository(self, request, context):
        """Creates a repository. The returned Operation will finish once the
        repository has been created. Its response will be the created Repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRepository(self, request, context):
        """Updates a repository.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRepository(self, request, context):
        """Deletes a repository and all of its contents. The returned Operation will
        finish once the repository has been deleted. It will not have any Operation
        metadata and will return a google.protobuf.Empty response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListPackages(self, request, context):
        """Lists packages.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPackage(self, request, context):
        """Gets a package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeletePackage(self, request, context):
        """Deletes a package and all of its versions and tags. The returned operation
        will complete once the package has been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListVersions(self, request, context):
        """Lists versions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVersion(self, request, context):
        """Gets a version
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteVersion(self, request, context):
        """Deletes a version and all of its content. The returned operation will
        complete once the version has been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDeleteVersions(self, request, context):
        """Deletes multiple versions across a repository. The returned operation will
        complete once the versions have been deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVersion(self, request, context):
        """Updates a version.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFiles(self, request, context):
        """Lists files.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFile(self, request, context):
        """Gets a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFile(self, request, context):
        """Deletes a file and all of its content. It is only allowed on generic
        repositories. The returned operation will complete once the file has been
        deleted.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFile(self, request, context):
        """Updates a file.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTags(self, request, context):
        """Lists tags.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTag(self, request, context):
        """Gets a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTag(self, request, context):
        """Creates a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTag(self, request, context):
        """Updates a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTag(self, request, context):
        """Deletes a tag.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRule(self, request, context):
        """Creates a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRules(self, request, context):
        """Lists rules.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRule(self, request, context):
        """Gets a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateRule(self, request, context):
        """Updates a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRule(self, request, context):
        """Deletes a rule.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIamPolicy(self, request, context):
        """Updates the IAM policy for a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIamPolicy(self, request, context):
        """Gets the IAM policy for a given resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestIamPermissions(self, request, context):
        """Tests if the caller has a list of permissions on a resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetProjectSettings(self, request, context):
        """Retrieves the Settings for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateProjectSettings(self, request, context):
        """Updates the Settings for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetVPCSCConfig(self, request, context):
        """Retrieves the VPCSC Config for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateVPCSCConfig(self, request, context):
        """Updates the VPCSC Config for the Project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdatePackage(self, request, context):
        """Updates a package.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListAttachments(self, request, context):
        """Lists attachments.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAttachment(self, request, context):
        """Gets an attachment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAttachment(self, request, context):
        """Creates an attachment. The returned Operation will finish once the
        attachment has been created. Its response will be the created attachment.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteAttachment(self, request, context):
        """Deletes an attachment. The returned Operation will
        finish once the attachments has been deleted. It will not have any
        Operation metadata and will return a `google.protobuf.Empty` response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ArtifactRegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListDockerImages': grpc.unary_unary_rpc_method_handler(servicer.ListDockerImages, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesResponse.SerializeToString), 'GetDockerImage': grpc.unary_unary_rpc_method_handler(servicer.GetDockerImage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetDockerImageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.DockerImage.SerializeToString), 'ListMavenArtifacts': grpc.unary_unary_rpc_method_handler(servicer.ListMavenArtifacts, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsResponse.SerializeToString), 'GetMavenArtifact': grpc.unary_unary_rpc_method_handler(servicer.GetMavenArtifact, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetMavenArtifactRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.MavenArtifact.SerializeToString), 'ListNpmPackages': grpc.unary_unary_rpc_method_handler(servicer.ListNpmPackages, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesResponse.SerializeToString), 'GetNpmPackage': grpc.unary_unary_rpc_method_handler(servicer.GetNpmPackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetNpmPackageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.NpmPackage.SerializeToString), 'ListPythonPackages': grpc.unary_unary_rpc_method_handler(servicer.ListPythonPackages, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesResponse.SerializeToString), 'GetPythonPackage': grpc.unary_unary_rpc_method_handler(servicer.GetPythonPackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetPythonPackageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.PythonPackage.SerializeToString), 'ImportAptArtifacts': grpc.unary_unary_rpc_method_handler(servicer.ImportAptArtifacts, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_apt__artifact__pb2.ImportAptArtifactsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ImportYumArtifacts': grpc.unary_unary_rpc_method_handler(servicer.ImportYumArtifacts, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_yum__artifact__pb2.ImportYumArtifactsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListRepositories': grpc.unary_unary_rpc_method_handler(servicer.ListRepositories, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesResponse.SerializeToString), 'GetRepository': grpc.unary_unary_rpc_method_handler(servicer.GetRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.GetRepositoryRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.SerializeToString), 'CreateRepository': grpc.unary_unary_rpc_method_handler(servicer.CreateRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.CreateRepositoryRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateRepository': grpc.unary_unary_rpc_method_handler(servicer.UpdateRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.SerializeToString), 'DeleteRepository': grpc.unary_unary_rpc_method_handler(servicer.DeleteRepository, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.DeleteRepositoryRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListPackages': grpc.unary_unary_rpc_method_handler(servicer.ListPackages, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesResponse.SerializeToString), 'GetPackage': grpc.unary_unary_rpc_method_handler(servicer.GetPackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.GetPackageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.SerializeToString), 'DeletePackage': grpc.unary_unary_rpc_method_handler(servicer.DeletePackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.DeletePackageRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'ListVersions': grpc.unary_unary_rpc_method_handler(servicer.ListVersions, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsResponse.SerializeToString), 'GetVersion': grpc.unary_unary_rpc_method_handler(servicer.GetVersion, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.GetVersionRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.SerializeToString), 'DeleteVersion': grpc.unary_unary_rpc_method_handler(servicer.DeleteVersion, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.DeleteVersionRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'BatchDeleteVersions': grpc.unary_unary_rpc_method_handler(servicer.BatchDeleteVersions, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.BatchDeleteVersionsRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateVersion': grpc.unary_unary_rpc_method_handler(servicer.UpdateVersion, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.UpdateVersionRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.SerializeToString), 'ListFiles': grpc.unary_unary_rpc_method_handler(servicer.ListFiles, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesResponse.SerializeToString), 'GetFile': grpc.unary_unary_rpc_method_handler(servicer.GetFile, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.GetFileRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.SerializeToString), 'DeleteFile': grpc.unary_unary_rpc_method_handler(servicer.DeleteFile, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.DeleteFileRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateFile': grpc.unary_unary_rpc_method_handler(servicer.UpdateFile, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.UpdateFileRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.SerializeToString), 'ListTags': grpc.unary_unary_rpc_method_handler(servicer.ListTags, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsResponse.SerializeToString), 'GetTag': grpc.unary_unary_rpc_method_handler(servicer.GetTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.GetTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.SerializeToString), 'CreateTag': grpc.unary_unary_rpc_method_handler(servicer.CreateTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.CreateTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.SerializeToString), 'UpdateTag': grpc.unary_unary_rpc_method_handler(servicer.UpdateTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.UpdateTagRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.SerializeToString), 'DeleteTag': grpc.unary_unary_rpc_method_handler(servicer.DeleteTag, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.DeleteTagRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'CreateRule': grpc.unary_unary_rpc_method_handler(servicer.CreateRule, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.CreateRuleRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.SerializeToString), 'ListRules': grpc.unary_unary_rpc_method_handler(servicer.ListRules, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesResponse.SerializeToString), 'GetRule': grpc.unary_unary_rpc_method_handler(servicer.GetRule, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.GetRuleRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.SerializeToString), 'UpdateRule': grpc.unary_unary_rpc_method_handler(servicer.UpdateRule, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.UpdateRuleRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.SerializeToString), 'DeleteRule': grpc.unary_unary_rpc_method_handler(servicer.DeleteRule, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.DeleteRuleRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'SetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.SetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'GetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'TestIamPermissions': grpc.unary_unary_rpc_method_handler(servicer.TestIamPermissions, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString), 'GetProjectSettings': grpc.unary_unary_rpc_method_handler(servicer.GetProjectSettings, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.GetProjectSettingsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.SerializeToString), 'UpdateProjectSettings': grpc.unary_unary_rpc_method_handler(servicer.UpdateProjectSettings, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.UpdateProjectSettingsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.SerializeToString), 'GetVPCSCConfig': grpc.unary_unary_rpc_method_handler(servicer.GetVPCSCConfig, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.GetVPCSCConfigRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.SerializeToString), 'UpdateVPCSCConfig': grpc.unary_unary_rpc_method_handler(servicer.UpdateVPCSCConfig, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.UpdateVPCSCConfigRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.SerializeToString), 'UpdatePackage': grpc.unary_unary_rpc_method_handler(servicer.UpdatePackage, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.UpdatePackageRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.SerializeToString), 'ListAttachments': grpc.unary_unary_rpc_method_handler(servicer.ListAttachments, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.SerializeToString), 'GetAttachment': grpc.unary_unary_rpc_method_handler(servicer.GetAttachment, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.GetAttachmentRequest.FromString, response_serializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.Attachment.SerializeToString), 'CreateAttachment': grpc.unary_unary_rpc_method_handler(servicer.CreateAttachment, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteAttachment': grpc.unary_unary_rpc_method_handler(servicer.DeleteAttachment, request_deserializer=google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.devtools.artifactregistry.v1.ArtifactRegistry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.devtools.artifactregistry.v1.ArtifactRegistry', rpc_method_handlers)

class ArtifactRegistry(object):
    """The Artifact Registry API service.

    Artifact Registry is an artifact management system for storing artifacts
    from different package management systems.

    The resources managed by this API are:

    * Repositories, which group packages and their data.
    * Packages, which group versions and their tags.
    * Versions, which are specific forms of a package.
    * Tags, which represent alternative names for versions.
    * Files, which contain content and are optionally associated with a Package
    or Version.
    """

    @staticmethod
    def ListDockerImages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListDockerImages', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListDockerImagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetDockerImage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetDockerImage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetDockerImageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.DockerImage.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListMavenArtifacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListMavenArtifacts', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListMavenArtifactsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMavenArtifact(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetMavenArtifact', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetMavenArtifactRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.MavenArtifact.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListNpmPackages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListNpmPackages', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListNpmPackagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetNpmPackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetNpmPackage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetNpmPackageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.NpmPackage.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPythonPackages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPythonPackages', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.ListPythonPackagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPythonPackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPythonPackage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.GetPythonPackageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_artifact__pb2.PythonPackage.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportAptArtifacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportAptArtifacts', google_dot_devtools_dot_artifactregistry_dot_v1_dot_apt__artifact__pb2.ImportAptArtifactsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ImportYumArtifacts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ImportYumArtifacts', google_dot_devtools_dot_artifactregistry_dot_v1_dot_yum__artifact__pb2.ImportYumArtifactsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListRepositories(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRepositories', google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.ListRepositoriesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRepository', google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.GetRepositoryRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRepository', google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.CreateRepositoryRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRepository', google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.UpdateRepositoryRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.Repository.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteRepository(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRepository', google_dot_devtools_dot_artifactregistry_dot_v1_dot_repository__pb2.DeleteRepositoryRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListPackages(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListPackages', google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.ListPackagesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetPackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetPackage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.GetPackageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeletePackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeletePackage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.DeletePackageRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListVersions', google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.ListVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVersion', google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.GetVersionRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteVersion', google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.DeleteVersionRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def BatchDeleteVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/BatchDeleteVersions', google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.BatchDeleteVersionsRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVersion', google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.UpdateVersionRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_version__pb2.Version.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListFiles(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListFiles', google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.ListFilesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetFile', google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.GetFileRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteFile', google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.DeleteFileRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateFile(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateFile', google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.UpdateFileRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_file__pb2.File.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTags(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListTags', google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.ListTagsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetTag', google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.GetTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateTag', google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.CreateTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateTag', google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.UpdateTagRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.Tag.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteTag(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteTag', google_dot_devtools_dot_artifactregistry_dot_v1_dot_tag__pb2.DeleteTagRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateRule', google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.CreateRuleRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListRules(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListRules', google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.ListRulesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetRule', google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.GetRuleRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateRule', google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.UpdateRuleRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.Rule.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteRule(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteRule', google_dot_devtools_dot_artifactregistry_dot_v1_dot_rule__pb2.DeleteRuleRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/SetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TestIamPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/TestIamPermissions', google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetProjectSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetProjectSettings', google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.GetProjectSettingsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateProjectSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateProjectSettings', google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.UpdateProjectSettingsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_settings__pb2.ProjectSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetVPCSCConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetVPCSCConfig', google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.GetVPCSCConfigRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateVPCSCConfig(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdateVPCSCConfig', google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.UpdateVPCSCConfigRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_vpcsc__config__pb2.VPCSCConfig.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdatePackage(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/UpdatePackage', google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.UpdatePackageRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_package__pb2.Package.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListAttachments(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/ListAttachments', google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.ListAttachmentsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/GetAttachment', google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.GetAttachmentRequest.SerializeToString, google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.Attachment.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/CreateAttachment', google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.CreateAttachmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteAttachment(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.devtools.artifactregistry.v1.ArtifactRegistry/DeleteAttachment', google_dot_devtools_dot_artifactregistry_dot_v1_dot_attachment__pb2.DeleteAttachmentRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)