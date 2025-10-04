"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.gkehub.v1 import feature_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_feature__pb2
from .....google.cloud.gkehub.v1 import membership_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_membership__pb2
from .....google.cloud.gkehub.v1 import service_pb2 as google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/gkehub/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class GkeHubStub(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1.Membership]
    * [Feature][google.cloud.gkehub.v1.Feature]

    GKE Hub is currently available in the global region and all regions in
    https://cloud.google.com/compute/docs/regions-zones. Feature is only
    available in global region while membership is global region and all the
    regions.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListMemberships = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/ListMemberships', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsResponse.FromString, _registered_method=True)
        self.ListFeatures = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/ListFeatures', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesResponse.FromString, _registered_method=True)
        self.GetMembership = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/GetMembership', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetMembershipRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_membership__pb2.Membership.FromString, _registered_method=True)
        self.GetFeature = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/GetFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetFeatureRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_feature__pb2.Feature.FromString, _registered_method=True)
        self.CreateMembership = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/CreateMembership', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateMembershipRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.CreateFeature = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/CreateFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteMembership = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/DeleteMembership', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteMembershipRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteFeature = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/DeleteFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateMembership = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/UpdateMembership', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateMembershipRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateFeature = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/UpdateFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.GenerateConnectManifest = channel.unary_unary('/google.cloud.gkehub.v1.GkeHub/GenerateConnectManifest', request_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestResponse.FromString, _registered_method=True)

class GkeHubServicer(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1.Membership]
    * [Feature][google.cloud.gkehub.v1.Feature]

    GKE Hub is currently available in the global region and all regions in
    https://cloud.google.com/compute/docs/regions-zones. Feature is only
    available in global region while membership is global region and all the
    regions.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    def ListMemberships(self, request, context):
        """Lists Memberships in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListFeatures(self, request, context):
        """Lists Features in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMembership(self, request, context):
        """Gets the details of a Membership.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFeature(self, request, context):
        """Gets details of a single Feature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMembership(self, request, context):
        """Creates a new Membership.

        **This is currently only supported for GKE clusters on Google Cloud**.
        To register other clusters, follow the instructions at
        https://cloud.google.com/anthos/multicluster-management/connect/registering-a-cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateFeature(self, request, context):
        """Adds a new Feature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMembership(self, request, context):
        """Removes a Membership.

        **This is currently only supported for GKE clusters on Google Cloud**.
        To unregister other clusters, follow the instructions at
        https://cloud.google.com/anthos/multicluster-management/connect/unregistering-a-cluster.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteFeature(self, request, context):
        """Removes a Feature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateMembership(self, request, context):
        """Updates an existing Membership.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFeature(self, request, context):
        """Updates an existing Feature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateConnectManifest(self, request, context):
        """Generates the manifest for deployment of the GKE connect agent.

        **This method is used internally by Google-provided libraries.**
        Most clients should not need to call this method directly.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_GkeHubServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListMemberships': grpc.unary_unary_rpc_method_handler(servicer.ListMemberships, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsResponse.SerializeToString), 'ListFeatures': grpc.unary_unary_rpc_method_handler(servicer.ListFeatures, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesResponse.SerializeToString), 'GetMembership': grpc.unary_unary_rpc_method_handler(servicer.GetMembership, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetMembershipRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_membership__pb2.Membership.SerializeToString), 'GetFeature': grpc.unary_unary_rpc_method_handler(servicer.GetFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetFeatureRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_feature__pb2.Feature.SerializeToString), 'CreateMembership': grpc.unary_unary_rpc_method_handler(servicer.CreateMembership, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateMembershipRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'CreateFeature': grpc.unary_unary_rpc_method_handler(servicer.CreateFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteMembership': grpc.unary_unary_rpc_method_handler(servicer.DeleteMembership, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteMembershipRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteFeature': grpc.unary_unary_rpc_method_handler(servicer.DeleteFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateMembership': grpc.unary_unary_rpc_method_handler(servicer.UpdateMembership, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateMembershipRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateFeature': grpc.unary_unary_rpc_method_handler(servicer.UpdateFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'GenerateConnectManifest': grpc.unary_unary_rpc_method_handler(servicer.GenerateConnectManifest, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.gkehub.v1.GkeHub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.gkehub.v1.GkeHub', rpc_method_handlers)

class GkeHub(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1.Membership]
    * [Feature][google.cloud.gkehub.v1.Feature]

    GKE Hub is currently available in the global region and all regions in
    https://cloud.google.com/compute/docs/regions-zones. Feature is only
    available in global region while membership is global region and all the
    regions.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    @staticmethod
    def ListMemberships(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/ListMemberships', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListMembershipsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListFeatures(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/ListFeatures', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.ListFeaturesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMembership(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/GetMembership', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetMembershipRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1_dot_membership__pb2.Membership.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/GetFeature', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GetFeatureRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1_dot_feature__pb2.Feature.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateMembership(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/CreateMembership', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateMembershipRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/CreateFeature', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.CreateFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteMembership(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/DeleteMembership', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteMembershipRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/DeleteFeature', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.DeleteFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateMembership(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/UpdateMembership', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateMembershipRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/UpdateFeature', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.UpdateFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GenerateConnectManifest(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1.GkeHub/GenerateConnectManifest', google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1_dot_service__pb2.GenerateConnectManifestResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)