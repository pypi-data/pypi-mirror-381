"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.gkehub.v1alpha import feature_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_feature__pb2
from .....google.cloud.gkehub.v1alpha import service_pb2 as google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/gkehub/v1alpha/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class GkeHubStub(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1alpha.Membership]
    * [Feature][google.cloud.gkehub.v1alpha.Feature]

    GKE Hub is currently only available in the global region.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListFeatures = channel.unary_unary('/google.cloud.gkehub.v1alpha.GkeHub/ListFeatures', request_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesResponse.FromString, _registered_method=True)
        self.GetFeature = channel.unary_unary('/google.cloud.gkehub.v1alpha.GkeHub/GetFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.GetFeatureRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_feature__pb2.Feature.FromString, _registered_method=True)
        self.CreateFeature = channel.unary_unary('/google.cloud.gkehub.v1alpha.GkeHub/CreateFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.CreateFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.DeleteFeature = channel.unary_unary('/google.cloud.gkehub.v1alpha.GkeHub/DeleteFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.DeleteFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)
        self.UpdateFeature = channel.unary_unary('/google.cloud.gkehub.v1alpha.GkeHub/UpdateFeature', request_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.UpdateFeatureRequest.SerializeToString, response_deserializer=google_dot_longrunning_dot_operations__pb2.Operation.FromString, _registered_method=True)

class GkeHubServicer(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1alpha.Membership]
    * [Feature][google.cloud.gkehub.v1alpha.Feature]

    GKE Hub is currently only available in the global region.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    def ListFeatures(self, request, context):
        """Lists Features in a given project and location.
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

    def CreateFeature(self, request, context):
        """Adds a new Feature.
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

    def UpdateFeature(self, request, context):
        """Updates an existing Feature.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_GkeHubServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListFeatures': grpc.unary_unary_rpc_method_handler(servicer.ListFeatures, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesResponse.SerializeToString), 'GetFeature': grpc.unary_unary_rpc_method_handler(servicer.GetFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.GetFeatureRequest.FromString, response_serializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_feature__pb2.Feature.SerializeToString), 'CreateFeature': grpc.unary_unary_rpc_method_handler(servicer.CreateFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.CreateFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'DeleteFeature': grpc.unary_unary_rpc_method_handler(servicer.DeleteFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.DeleteFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString), 'UpdateFeature': grpc.unary_unary_rpc_method_handler(servicer.UpdateFeature, request_deserializer=google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.UpdateFeatureRequest.FromString, response_serializer=google_dot_longrunning_dot_operations__pb2.Operation.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.gkehub.v1alpha.GkeHub', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.gkehub.v1alpha.GkeHub', rpc_method_handlers)

class GkeHub(object):
    """The GKE Hub service handles the registration of many Kubernetes clusters to
    Google Cloud, and the management of multi-cluster features over those
    clusters.

    The GKE Hub service operates on the following resources:

    * [Membership][google.cloud.gkehub.v1alpha.Membership]
    * [Feature][google.cloud.gkehub.v1alpha.Feature]

    GKE Hub is currently only available in the global region.

    **Membership management may be non-trivial:** it is recommended to use one
    of the Google-provided client libraries or tools where possible when working
    with Membership resources.
    """

    @staticmethod
    def ListFeatures(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1alpha.GkeHub/ListFeatures', google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.ListFeaturesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1alpha.GkeHub/GetFeature', google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.GetFeatureRequest.SerializeToString, google_dot_cloud_dot_gkehub_dot_v1alpha_dot_feature__pb2.Feature.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1alpha.GkeHub/CreateFeature', google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.CreateFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1alpha.GkeHub/DeleteFeature', google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.DeleteFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateFeature(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.gkehub.v1alpha.GkeHub/UpdateFeature', google_dot_cloud_dot_gkehub_dot_v1alpha_dot_service__pb2.UpdateFeatureRequest.SerializeToString, google_dot_longrunning_dot_operations__pb2.Operation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)