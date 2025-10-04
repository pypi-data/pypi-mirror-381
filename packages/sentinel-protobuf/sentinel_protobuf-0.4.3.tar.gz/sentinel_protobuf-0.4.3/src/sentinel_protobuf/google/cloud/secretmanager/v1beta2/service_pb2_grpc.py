"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.secretmanager.v1beta2 import resources_pb2 as google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2
from .....google.cloud.secretmanager.v1beta2 import service_pb2 as google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2
from .....google.iam.v1 import iam_policy_pb2 as google_dot_iam_dot_v1_dot_iam__policy__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/secretmanager/v1beta2/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class SecretManagerServiceStub(object):
    """Secret Manager Service

    Manages secrets and operations using those secrets. Implements a REST
    model with the following objects:

    * [Secret][google.cloud.secretmanager.v1beta2.Secret]
    * [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion]
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListSecrets = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/ListSecrets', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsResponse.FromString, _registered_method=True)
        self.CreateSecret = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/CreateSecret', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.CreateSecretRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, _registered_method=True)
        self.AddSecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/AddSecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AddSecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, _registered_method=True)
        self.GetSecret = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/GetSecret', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, _registered_method=True)
        self.UpdateSecret = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/UpdateSecret', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.UpdateSecretRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, _registered_method=True)
        self.DeleteSecret = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/DeleteSecret', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DeleteSecretRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.ListSecretVersions = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/ListSecretVersions', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsResponse.FromString, _registered_method=True)
        self.GetSecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/GetSecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, _registered_method=True)
        self.AccessSecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/AccessSecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionResponse.FromString, _registered_method=True)
        self.DisableSecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/DisableSecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DisableSecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, _registered_method=True)
        self.EnableSecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/EnableSecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.EnableSecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, _registered_method=True)
        self.DestroySecretVersion = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/DestroySecretVersion', request_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DestroySecretVersionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, _registered_method=True)
        self.SetIamPolicy = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/SetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.GetIamPolicy = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/GetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.TestIamPermissions = channel.unary_unary('/google.cloud.secretmanager.v1beta2.SecretManagerService/TestIamPermissions', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, _registered_method=True)

class SecretManagerServiceServicer(object):
    """Secret Manager Service

    Manages secrets and operations using those secrets. Implements a REST
    model with the following objects:

    * [Secret][google.cloud.secretmanager.v1beta2.Secret]
    * [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion]
    """

    def ListSecrets(self, request, context):
        """Lists [Secrets][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateSecret(self, request, context):
        """Creates a new [Secret][google.cloud.secretmanager.v1beta2.Secret]
        containing no
        [SecretVersions][google.cloud.secretmanager.v1beta2.SecretVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSecretVersion(self, request, context):
        """Creates a new
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion]
        containing secret data and attaches it to an existing
        [Secret][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSecret(self, request, context):
        """Gets metadata for a given
        [Secret][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSecret(self, request, context):
        """Updates metadata of an existing
        [Secret][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteSecret(self, request, context):
        """Deletes a [Secret][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListSecretVersions(self, request, context):
        """Lists [SecretVersions][google.cloud.secretmanager.v1beta2.SecretVersion].
        This call does not return secret data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSecretVersion(self, request, context):
        """Gets metadata for a
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].

        `projects/*/secrets/*/versions/latest` is an alias to the most recently
        created [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AccessSecretVersion(self, request, context):
        """Accesses a
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion]. This
        call returns the secret data.

        `projects/*/secrets/*/versions/latest` is an alias to the most recently
        created [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DisableSecretVersion(self, request, context):
        """Disables a
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].

        Sets the [state][google.cloud.secretmanager.v1beta2.SecretVersion.state] of
        the [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion] to
        [DISABLED][google.cloud.secretmanager.v1beta2.SecretVersion.State.DISABLED].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EnableSecretVersion(self, request, context):
        """Enables a
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].

        Sets the [state][google.cloud.secretmanager.v1beta2.SecretVersion.state] of
        the [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion] to
        [ENABLED][google.cloud.secretmanager.v1beta2.SecretVersion.State.ENABLED].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DestroySecretVersion(self, request, context):
        """Destroys a
        [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion].

        Sets the [state][google.cloud.secretmanager.v1beta2.SecretVersion.state] of
        the [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion] to
        [DESTROYED][google.cloud.secretmanager.v1beta2.SecretVersion.State.DESTROYED]
        and irrevocably destroys the secret data.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetIamPolicy(self, request, context):
        """Sets the access control policy on the specified secret. Replaces any
        existing policy.

        Permissions on
        [SecretVersions][google.cloud.secretmanager.v1beta2.SecretVersion] are
        enforced according to the policy set on the associated
        [Secret][google.cloud.secretmanager.v1beta2.Secret].
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIamPolicy(self, request, context):
        """Gets the access control policy for a secret.
        Returns empty policy if the secret exists and does not have a policy set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestIamPermissions(self, request, context):
        """Returns permissions that a caller has for the specified secret.
        If the secret does not exist, this call returns an empty set of
        permissions, not a NOT_FOUND error.

        Note: This operation is designed to be used for building permission-aware
        UIs and command-line tools, not for authorization checking. This operation
        may "fail open" without warning.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SecretManagerServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListSecrets': grpc.unary_unary_rpc_method_handler(servicer.ListSecrets, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsResponse.SerializeToString), 'CreateSecret': grpc.unary_unary_rpc_method_handler(servicer.CreateSecret, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.CreateSecretRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.SerializeToString), 'AddSecretVersion': grpc.unary_unary_rpc_method_handler(servicer.AddSecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AddSecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.SerializeToString), 'GetSecret': grpc.unary_unary_rpc_method_handler(servicer.GetSecret, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.SerializeToString), 'UpdateSecret': grpc.unary_unary_rpc_method_handler(servicer.UpdateSecret, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.UpdateSecretRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.SerializeToString), 'DeleteSecret': grpc.unary_unary_rpc_method_handler(servicer.DeleteSecret, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DeleteSecretRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'ListSecretVersions': grpc.unary_unary_rpc_method_handler(servicer.ListSecretVersions, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsResponse.SerializeToString), 'GetSecretVersion': grpc.unary_unary_rpc_method_handler(servicer.GetSecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.SerializeToString), 'AccessSecretVersion': grpc.unary_unary_rpc_method_handler(servicer.AccessSecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionResponse.SerializeToString), 'DisableSecretVersion': grpc.unary_unary_rpc_method_handler(servicer.DisableSecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DisableSecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.SerializeToString), 'EnableSecretVersion': grpc.unary_unary_rpc_method_handler(servicer.EnableSecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.EnableSecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.SerializeToString), 'DestroySecretVersion': grpc.unary_unary_rpc_method_handler(servicer.DestroySecretVersion, request_deserializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DestroySecretVersionRequest.FromString, response_serializer=google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.SerializeToString), 'SetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.SetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'GetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'TestIamPermissions': grpc.unary_unary_rpc_method_handler(servicer.TestIamPermissions, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.secretmanager.v1beta2.SecretManagerService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.secretmanager.v1beta2.SecretManagerService', rpc_method_handlers)

class SecretManagerService(object):
    """Secret Manager Service

    Manages secrets and operations using those secrets. Implements a REST
    model with the following objects:

    * [Secret][google.cloud.secretmanager.v1beta2.Secret]
    * [SecretVersion][google.cloud.secretmanager.v1beta2.SecretVersion]
    """

    @staticmethod
    def ListSecrets(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/ListSecrets', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateSecret(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/CreateSecret', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.CreateSecretRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AddSecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/AddSecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AddSecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSecret(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/GetSecret', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateSecret(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/UpdateSecret', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.UpdateSecretRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.Secret.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteSecret(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/DeleteSecret', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DeleteSecretRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListSecretVersions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/ListSecretVersions', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.ListSecretVersionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/GetSecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.GetSecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AccessSecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/AccessSecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.AccessSecretVersionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DisableSecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/DisableSecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DisableSecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def EnableSecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/EnableSecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.EnableSecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DestroySecretVersion(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/DestroySecretVersion', google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_service__pb2.DestroySecretVersionRequest.SerializeToString, google_dot_cloud_dot_secretmanager_dot_v1beta2_dot_resources__pb2.SecretVersion.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/SetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/GetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TestIamPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.secretmanager.v1beta2.SecretManagerService/TestIamPermissions', google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)