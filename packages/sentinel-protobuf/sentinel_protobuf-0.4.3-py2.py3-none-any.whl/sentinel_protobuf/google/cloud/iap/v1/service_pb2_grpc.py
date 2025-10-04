"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.iap.v1 import service_pb2 as google_dot_cloud_dot_iap_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/iap/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class IdentityAwareProxyAdminServiceStub(object):
    """The Cloud Identity-Aware Proxy API.

    APIs for Identity-Aware Proxy Admin configurations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetIamPolicy = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/SetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.GetIamPolicy = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIamPolicy', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, _registered_method=True)
        self.TestIamPermissions = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/TestIamPermissions', request_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, response_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, _registered_method=True)
        self.GetIapSettings = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIapSettings', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIapSettingsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.FromString, _registered_method=True)
        self.UpdateIapSettings = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateIapSettings', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateIapSettingsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.FromString, _registered_method=True)
        self.ValidateIapAttributeExpression = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/ValidateIapAttributeExpression', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionResponse.FromString, _registered_method=True)
        self.ListTunnelDestGroups = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/ListTunnelDestGroups', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsResponse.FromString, _registered_method=True)
        self.CreateTunnelDestGroup = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/CreateTunnelDestGroup', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateTunnelDestGroupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, _registered_method=True)
        self.GetTunnelDestGroup = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetTunnelDestGroup', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetTunnelDestGroupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, _registered_method=True)
        self.DeleteTunnelDestGroup = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/DeleteTunnelDestGroup', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteTunnelDestGroupRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.UpdateTunnelDestGroup = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateTunnelDestGroup', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateTunnelDestGroupRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, _registered_method=True)

class IdentityAwareProxyAdminServiceServicer(object):
    """The Cloud Identity-Aware Proxy API.

    APIs for Identity-Aware Proxy Admin configurations.
    """

    def SetIamPolicy(self, request, context):
        """Sets the access control policy for an Identity-Aware Proxy protected
        resource. Replaces any existing policy.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIamPolicy(self, request, context):
        """Gets the access control policy for an Identity-Aware Proxy protected
        resource.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TestIamPermissions(self, request, context):
        """Returns permissions that a caller has on the Identity-Aware Proxy protected
        resource.
        More information about managing access via IAP can be found at:
        https://cloud.google.com/iap/docs/managing-access#managing_access_via_the_api
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIapSettings(self, request, context):
        """Gets the IAP settings on a particular IAP protected resource.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateIapSettings(self, request, context):
        """Updates the IAP settings on a particular IAP protected resource. It
        replaces all fields unless the `update_mask` is set.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ValidateIapAttributeExpression(self, request, context):
        """Validates that a given CEL expression conforms to IAP restrictions.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTunnelDestGroups(self, request, context):
        """Lists the existing TunnelDestGroups. To group across all locations, use a
        `-` as the location ID. For example:
        `/v1/projects/123/iap_tunnel/locations/-/destGroups`
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTunnelDestGroup(self, request, context):
        """Creates a new TunnelDestGroup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTunnelDestGroup(self, request, context):
        """Retrieves an existing TunnelDestGroup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTunnelDestGroup(self, request, context):
        """Deletes a TunnelDestGroup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTunnelDestGroup(self, request, context):
        """Updates a TunnelDestGroup.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_IdentityAwareProxyAdminServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'SetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.SetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'GetIamPolicy': grpc.unary_unary_rpc_method_handler(servicer.GetIamPolicy, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_policy__pb2.Policy.SerializeToString), 'TestIamPermissions': grpc.unary_unary_rpc_method_handler(servicer.TestIamPermissions, request_deserializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.FromString, response_serializer=google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.SerializeToString), 'GetIapSettings': grpc.unary_unary_rpc_method_handler(servicer.GetIapSettings, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIapSettingsRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.SerializeToString), 'UpdateIapSettings': grpc.unary_unary_rpc_method_handler(servicer.UpdateIapSettings, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateIapSettingsRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.SerializeToString), 'ValidateIapAttributeExpression': grpc.unary_unary_rpc_method_handler(servicer.ValidateIapAttributeExpression, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionResponse.SerializeToString), 'ListTunnelDestGroups': grpc.unary_unary_rpc_method_handler(servicer.ListTunnelDestGroups, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsResponse.SerializeToString), 'CreateTunnelDestGroup': grpc.unary_unary_rpc_method_handler(servicer.CreateTunnelDestGroup, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateTunnelDestGroupRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.SerializeToString), 'GetTunnelDestGroup': grpc.unary_unary_rpc_method_handler(servicer.GetTunnelDestGroup, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetTunnelDestGroupRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.SerializeToString), 'DeleteTunnelDestGroup': grpc.unary_unary_rpc_method_handler(servicer.DeleteTunnelDestGroup, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteTunnelDestGroupRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'UpdateTunnelDestGroup': grpc.unary_unary_rpc_method_handler(servicer.UpdateTunnelDestGroup, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateTunnelDestGroupRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.iap.v1.IdentityAwareProxyAdminService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.iap.v1.IdentityAwareProxyAdminService', rpc_method_handlers)

class IdentityAwareProxyAdminService(object):
    """The Cloud Identity-Aware Proxy API.

    APIs for Identity-Aware Proxy Admin configurations.
    """

    @staticmethod
    def SetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/SetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.SetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIamPolicy(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIamPolicy', google_dot_iam_dot_v1_dot_iam__policy__pb2.GetIamPolicyRequest.SerializeToString, google_dot_iam_dot_v1_dot_policy__pb2.Policy.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def TestIamPermissions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/TestIamPermissions', google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsRequest.SerializeToString, google_dot_iam_dot_v1_dot_iam__policy__pb2.TestIamPermissionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIapSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetIapSettings', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIapSettingsRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateIapSettings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateIapSettings', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateIapSettingsRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IapSettings.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ValidateIapAttributeExpression(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/ValidateIapAttributeExpression', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ValidateIapAttributeExpressionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTunnelDestGroups(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/ListTunnelDestGroups', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListTunnelDestGroupsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateTunnelDestGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/CreateTunnelDestGroup', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateTunnelDestGroupRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTunnelDestGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/GetTunnelDestGroup', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetTunnelDestGroupRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteTunnelDestGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/DeleteTunnelDestGroup', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteTunnelDestGroupRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateTunnelDestGroup(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyAdminService/UpdateTunnelDestGroup', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.UpdateTunnelDestGroupRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.TunnelDestGroup.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

class IdentityAwareProxyOAuthServiceStub(object):
    """API to programmatically create, list and retrieve Identity Aware Proxy (IAP)
    OAuth brands; and create, retrieve, delete and reset-secret of IAP OAuth
    clients.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListBrands = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListBrands', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsResponse.FromString, _registered_method=True)
        self.CreateBrand = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateBrand', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateBrandRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.FromString, _registered_method=True)
        self.GetBrand = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetBrand', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetBrandRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.FromString, _registered_method=True)
        self.CreateIdentityAwareProxyClient = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateIdentityAwareProxyClient', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateIdentityAwareProxyClientRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, _registered_method=True)
        self.ListIdentityAwareProxyClients = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListIdentityAwareProxyClients', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsResponse.FromString, _registered_method=True)
        self.GetIdentityAwareProxyClient = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetIdentityAwareProxyClient', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIdentityAwareProxyClientRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, _registered_method=True)
        self.ResetIdentityAwareProxyClientSecret = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ResetIdentityAwareProxyClientSecret', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ResetIdentityAwareProxyClientSecretRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, _registered_method=True)
        self.DeleteIdentityAwareProxyClient = channel.unary_unary('/google.cloud.iap.v1.IdentityAwareProxyOAuthService/DeleteIdentityAwareProxyClient', request_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteIdentityAwareProxyClientRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class IdentityAwareProxyOAuthServiceServicer(object):
    """API to programmatically create, list and retrieve Identity Aware Proxy (IAP)
    OAuth brands; and create, retrieve, delete and reset-secret of IAP OAuth
    clients.
    """

    def ListBrands(self, request, context):
        """Lists the existing brands for the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateBrand(self, request, context):
        """Constructs a new OAuth brand for the project if one does not exist.
        The created brand is "internal only", meaning that OAuth clients created
        under it only accept requests from users who belong to the same Google
        Workspace organization as the project. The brand is created in an
        un-reviewed status. NOTE: The "internal only" status can be manually
        changed in the Google Cloud Console. Requires that a brand does not already
        exist for the project, and that the specified support email is owned by the
        caller.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBrand(self, request, context):
        """Retrieves the OAuth brand of the project.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateIdentityAwareProxyClient(self, request, context):
        """Creates an Identity Aware Proxy (IAP) OAuth client. The client is owned
        by IAP. Requires that the brand for the project exists and that it is
        set for internal-only use.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListIdentityAwareProxyClients(self, request, context):
        """Lists the existing clients for the brand.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetIdentityAwareProxyClient(self, request, context):
        """Retrieves an Identity Aware Proxy (IAP) OAuth client.
        Requires that the client is owned by IAP.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetIdentityAwareProxyClientSecret(self, request, context):
        """Resets an Identity Aware Proxy (IAP) OAuth client secret. Useful if the
        secret was compromised. Requires that the client is owned by IAP.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteIdentityAwareProxyClient(self, request, context):
        """Deletes an Identity Aware Proxy (IAP) OAuth client. Useful for removing
        obsolete clients, managing the number of clients in a given project, and
        cleaning up after tests. Requires that the client is owned by IAP.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_IdentityAwareProxyOAuthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListBrands': grpc.unary_unary_rpc_method_handler(servicer.ListBrands, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsResponse.SerializeToString), 'CreateBrand': grpc.unary_unary_rpc_method_handler(servicer.CreateBrand, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateBrandRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.SerializeToString), 'GetBrand': grpc.unary_unary_rpc_method_handler(servicer.GetBrand, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetBrandRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.SerializeToString), 'CreateIdentityAwareProxyClient': grpc.unary_unary_rpc_method_handler(servicer.CreateIdentityAwareProxyClient, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateIdentityAwareProxyClientRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.SerializeToString), 'ListIdentityAwareProxyClients': grpc.unary_unary_rpc_method_handler(servicer.ListIdentityAwareProxyClients, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsResponse.SerializeToString), 'GetIdentityAwareProxyClient': grpc.unary_unary_rpc_method_handler(servicer.GetIdentityAwareProxyClient, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIdentityAwareProxyClientRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.SerializeToString), 'ResetIdentityAwareProxyClientSecret': grpc.unary_unary_rpc_method_handler(servicer.ResetIdentityAwareProxyClientSecret, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ResetIdentityAwareProxyClientSecretRequest.FromString, response_serializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.SerializeToString), 'DeleteIdentityAwareProxyClient': grpc.unary_unary_rpc_method_handler(servicer.DeleteIdentityAwareProxyClient, request_deserializer=google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteIdentityAwareProxyClientRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.iap.v1.IdentityAwareProxyOAuthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.iap.v1.IdentityAwareProxyOAuthService', rpc_method_handlers)

class IdentityAwareProxyOAuthService(object):
    """API to programmatically create, list and retrieve Identity Aware Proxy (IAP)
    OAuth brands; and create, retrieve, delete and reset-secret of IAP OAuth
    clients.
    """

    @staticmethod
    def ListBrands(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListBrands', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListBrandsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateBrand(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateBrand', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateBrandRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetBrand(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetBrand', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetBrandRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.Brand.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateIdentityAwareProxyClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/CreateIdentityAwareProxyClient', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.CreateIdentityAwareProxyClientRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListIdentityAwareProxyClients(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ListIdentityAwareProxyClients', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ListIdentityAwareProxyClientsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetIdentityAwareProxyClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/GetIdentityAwareProxyClient', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.GetIdentityAwareProxyClientRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ResetIdentityAwareProxyClientSecret(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/ResetIdentityAwareProxyClientSecret', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.ResetIdentityAwareProxyClientSecretRequest.SerializeToString, google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.IdentityAwareProxyClient.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteIdentityAwareProxyClient(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.iap.v1.IdentityAwareProxyOAuthService/DeleteIdentityAwareProxyClient', google_dot_cloud_dot_iap_dot_v1_dot_service__pb2.DeleteIdentityAwareProxyClientRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)