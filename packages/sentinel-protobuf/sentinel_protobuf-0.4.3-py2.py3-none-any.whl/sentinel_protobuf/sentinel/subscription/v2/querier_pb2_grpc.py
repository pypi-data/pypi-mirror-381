"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from ....sentinel.subscription.v2 import querier_pb2 as sentinel_dot_subscription_dot_v2_dot_querier__pb2
GRPC_GENERATED_VERSION = '1.71.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False
try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True
if _version_not_supported:
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in sentinel/subscription/v2/querier_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class QueryServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.QueryAllocation = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryAllocation', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationResponse.FromString, _registered_method=True)
        self.QueryAllocations = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryAllocations', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsResponse.FromString, _registered_method=True)
        self.QueryPayouts = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryPayouts', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsResponse.FromString, _registered_method=True)
        self.QueryPayoutsForAccount = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryPayoutsForAccount', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountResponse.FromString, _registered_method=True)
        self.QueryPayoutsForNode = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryPayoutsForNode', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeResponse.FromString, _registered_method=True)
        self.QueryPayout = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryPayout', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutResponse.FromString, _registered_method=True)
        self.QuerySubscriptions = channel.unary_unary('/sentinel.subscription.v2.QueryService/QuerySubscriptions', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsResponse.FromString, _registered_method=True)
        self.QuerySubscriptionsForAccount = channel.unary_unary('/sentinel.subscription.v2.QueryService/QuerySubscriptionsForAccount', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountResponse.FromString, _registered_method=True)
        self.QuerySubscriptionsForNode = channel.unary_unary('/sentinel.subscription.v2.QueryService/QuerySubscriptionsForNode', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeResponse.FromString, _registered_method=True)
        self.QuerySubscriptionsForPlan = channel.unary_unary('/sentinel.subscription.v2.QueryService/QuerySubscriptionsForPlan', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanResponse.FromString, _registered_method=True)
        self.QuerySubscription = channel.unary_unary('/sentinel.subscription.v2.QueryService/QuerySubscription', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionResponse.FromString, _registered_method=True)
        self.QueryParams = channel.unary_unary('/sentinel.subscription.v2.QueryService/QueryParams', request_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsRequest.SerializeToString, response_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsResponse.FromString, _registered_method=True)

class QueryServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def QueryAllocation(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryAllocations(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPayouts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPayoutsForAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPayoutsForNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QueryPayout(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptions(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptionsForAccount(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptionsForNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscriptionsForPlan(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuerySubscription(self, request, context):
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
    rpc_method_handlers = {'QueryAllocation': grpc.unary_unary_rpc_method_handler(servicer.QueryAllocation, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationResponse.SerializeToString), 'QueryAllocations': grpc.unary_unary_rpc_method_handler(servicer.QueryAllocations, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsResponse.SerializeToString), 'QueryPayouts': grpc.unary_unary_rpc_method_handler(servicer.QueryPayouts, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsResponse.SerializeToString), 'QueryPayoutsForAccount': grpc.unary_unary_rpc_method_handler(servicer.QueryPayoutsForAccount, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountResponse.SerializeToString), 'QueryPayoutsForNode': grpc.unary_unary_rpc_method_handler(servicer.QueryPayoutsForNode, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeResponse.SerializeToString), 'QueryPayout': grpc.unary_unary_rpc_method_handler(servicer.QueryPayout, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutResponse.SerializeToString), 'QuerySubscriptions': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptions, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsResponse.SerializeToString), 'QuerySubscriptionsForAccount': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptionsForAccount, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountResponse.SerializeToString), 'QuerySubscriptionsForNode': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptionsForNode, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeResponse.SerializeToString), 'QuerySubscriptionsForPlan': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscriptionsForPlan, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanResponse.SerializeToString), 'QuerySubscription': grpc.unary_unary_rpc_method_handler(servicer.QuerySubscription, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionResponse.SerializeToString), 'QueryParams': grpc.unary_unary_rpc_method_handler(servicer.QueryParams, request_deserializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsRequest.FromString, response_serializer=sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('sentinel.subscription.v2.QueryService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('sentinel.subscription.v2.QueryService', rpc_method_handlers)

class QueryService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def QueryAllocation(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryAllocation', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryAllocations(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryAllocations', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryAllocationsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPayouts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryPayouts', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPayoutsForAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryPayoutsForAccount', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPayoutsForNode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryPayoutsForNode', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutsForNodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryPayout(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryPayout', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryPayoutResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QuerySubscriptions', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptionsForAccount(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QuerySubscriptionsForAccount', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForAccountResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptionsForNode(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QuerySubscriptionsForNode', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForNodeResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscriptionsForPlan(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QuerySubscriptionsForPlan', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionsForPlanResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QuerySubscription(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QuerySubscription', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QuerySubscriptionResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def QueryParams(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/sentinel.subscription.v2.QueryService/QueryParams', sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsRequest.SerializeToString, sentinel_dot_subscription_dot_v2_dot_querier__pb2.QueryParamsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)