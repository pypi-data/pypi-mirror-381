"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.lease.v1 import querier_pb2 as sentinel_dot_lease_dot_v1_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/lease/v1/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryLeases = channel.unary_unary('/sentinel.lease.v1.QueryService/QueryLeases', request_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesRequest.SerializeToString, response_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesResponse.FromString, _registered_method=True)
        self.QueryLeasesForNode = channel.unary_unary('/sentinel.lease.v1.QueryService/QueryLeasesForNode', request_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeRequest.SerializeToString, response_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeResponse.FromString, _registered_method=True)
        self.QueryLeasesForProvider = channel.unary_unary('/sentinel.lease.v1.QueryService/QueryLeasesForProvider', request_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderRequest.SerializeToString, response_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderResponse.FromString, _registered_method=True)
        self.QueryLease = channel.unary_unary('/sentinel.lease.v1.QueryService/QueryLease', request_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseRequest.SerializeToString, response_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseResponse.FromString, _registered_method=True)
        self.QueryParams = channel.unary_unary('/sentinel.lease.v1.QueryService/QueryParams', request_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, response_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryLeases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryLeasesForNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryLeasesForProvider(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryLease(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryParams(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_QueryServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'QueryLeases': grpc.unary_unary_rpc_method_handler(servicer.QueryLeases, request_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesRequest.FromString, response_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesResponse.SerializeToString), 'QueryLeasesForNode': grpc.unary_unary_rpc_method_handler(servicer.QueryLeasesForNode, request_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeRequest.FromString, response_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeResponse.SerializeToString), 'QueryLeasesForProvider': grpc.unary_unary_rpc_method_handler(servicer.QueryLeasesForProvider, request_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderRequest.FromString, response_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderResponse.SerializeToString), 'QueryLease': grpc.unary_unary_rpc_method_handler(servicer.QueryLease, request_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseRequest.FromString, response_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseResponse.SerializeToString), 'QueryParams': grpc.unary_unary_rpc_method_handler(servicer.QueryParams, request_deserializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsRequest.FromString, response_serializer=sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.lease.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.lease.v1.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryLeases(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.lease.v1.QueryService/QueryLeases', sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesRequest.SerializeToString, sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryLeasesForNode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.lease.v1.QueryService/QueryLeasesForNode', sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeRequest.SerializeToString, sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForNodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryLeasesForProvider(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.lease.v1.QueryService/QueryLeasesForProvider', sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderRequest.SerializeToString, sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeasesForProviderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryLease(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.lease.v1.QueryService/QueryLease', sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseRequest.SerializeToString, sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryLeaseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.lease.v1.QueryService/QueryParams', sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, sentinel_dot_lease_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)