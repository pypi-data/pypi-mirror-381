"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.provider.v1 import querier_pb2 as sentinel_dot_provider_dot_v1_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/provider/v1/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryProviders = channel.unary_unary('/sentinel.provider.v1.QueryService/QueryProviders', request_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersRequest.SerializeToString, response_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersResponse.FromString, _registered_method=True)
        self.QueryProvider = channel.unary_unary('/sentinel.provider.v1.QueryService/QueryProvider', request_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderRequest.SerializeToString, response_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderResponse.FromString, _registered_method=True)
        self.QueryParams = channel.unary_unary('/sentinel.provider.v1.QueryService/QueryParams', request_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, response_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryProviders(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryProvider(self, request, context):
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
    rpc_method_handlers = {'QueryProviders': grpc.unary_unary_rpc_method_handler(servicer.QueryProviders, request_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersRequest.FromString, response_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersResponse.SerializeToString), 'QueryProvider': grpc.unary_unary_rpc_method_handler(servicer.QueryProvider, request_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderRequest.FromString, response_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderResponse.SerializeToString), 'QueryParams': grpc.unary_unary_rpc_method_handler(servicer.QueryParams, request_deserializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsRequest.FromString, response_serializer=sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.provider.v1.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.provider.v1.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryProviders(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.provider.v1.QueryService/QueryProviders', sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersRequest.SerializeToString, sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProvidersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryProvider(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.provider.v1.QueryService/QueryProvider', sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderRequest.SerializeToString, sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryProviderResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.provider.v1.QueryService/QueryParams', sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsRequest.SerializeToString, sentinel_dot_provider_dot_v1_dot_querier__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)