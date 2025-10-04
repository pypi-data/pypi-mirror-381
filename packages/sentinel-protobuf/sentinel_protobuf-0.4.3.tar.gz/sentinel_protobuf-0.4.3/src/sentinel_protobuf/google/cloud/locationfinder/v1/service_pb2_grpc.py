"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.locationfinder.v1 import cloud_location_pb2 as google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/locationfinder/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class CloudLocationFinderStub(object):
    """Service describing handlers for resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListCloudLocations = channel.unary_unary('/google.cloud.locationfinder.v1.CloudLocationFinder/ListCloudLocations', request_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsResponse.FromString, _registered_method=True)
        self.GetCloudLocation = channel.unary_unary('/google.cloud.locationfinder.v1.CloudLocationFinder/GetCloudLocation', request_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.GetCloudLocationRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.CloudLocation.FromString, _registered_method=True)
        self.SearchCloudLocations = channel.unary_unary('/google.cloud.locationfinder.v1.CloudLocationFinder/SearchCloudLocations', request_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsResponse.FromString, _registered_method=True)

class CloudLocationFinderServicer(object):
    """Service describing handlers for resources
    """

    def ListCloudLocations(self, request, context):
        """Lists cloud locations under a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetCloudLocation(self, request, context):
        """Retrieves a resource containing information about a cloud location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchCloudLocations(self, request, context):
        """Searches for cloud locations from a given source location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_CloudLocationFinderServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListCloudLocations': grpc.unary_unary_rpc_method_handler(servicer.ListCloudLocations, request_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsRequest.FromString, response_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsResponse.SerializeToString), 'GetCloudLocation': grpc.unary_unary_rpc_method_handler(servicer.GetCloudLocation, request_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.GetCloudLocationRequest.FromString, response_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.CloudLocation.SerializeToString), 'SearchCloudLocations': grpc.unary_unary_rpc_method_handler(servicer.SearchCloudLocations, request_deserializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsRequest.FromString, response_serializer=google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.locationfinder.v1.CloudLocationFinder', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.locationfinder.v1.CloudLocationFinder', rpc_method_handlers)

class CloudLocationFinder(object):
    """Service describing handlers for resources
    """

    @staticmethod
    def ListCloudLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.locationfinder.v1.CloudLocationFinder/ListCloudLocations', google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsRequest.SerializeToString, google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.ListCloudLocationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetCloudLocation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.locationfinder.v1.CloudLocationFinder/GetCloudLocation', google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.GetCloudLocationRequest.SerializeToString, google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.CloudLocation.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SearchCloudLocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.locationfinder.v1.CloudLocationFinder/SearchCloudLocations', google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsRequest.SerializeToString, google_dot_cloud_dot_locationfinder_dot_v1_dot_cloud__location__pb2.SearchCloudLocationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)