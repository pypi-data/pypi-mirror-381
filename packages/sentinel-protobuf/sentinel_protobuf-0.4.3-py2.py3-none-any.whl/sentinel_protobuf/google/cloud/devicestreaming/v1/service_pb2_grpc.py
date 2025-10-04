"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.devicestreaming.v1 import adb_service_pb2 as google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2
from .....google.cloud.devicestreaming.v1 import service_pb2 as google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/devicestreaming/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class DirectAccessServiceStub(object):
    """A service for allocating Android devices and interacting with the
    live-allocated devices.

    Each Session will wait for available capacity, at a higher
    priority over Test Execution. When allocated, the session will be exposed
    through a stream for integration.

    DirectAccessService is currently available as a preview to select developers.
    You can register today on behalf of you and your team at
    https://developer.android.com/studio/preview/android-device-streaming
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateDeviceSession = channel.unary_unary('/google.cloud.devicestreaming.v1.DirectAccessService/CreateDeviceSession', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CreateDeviceSessionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, _registered_method=True)
        self.ListDeviceSessions = channel.unary_unary('/google.cloud.devicestreaming.v1.DirectAccessService/ListDeviceSessions', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsResponse.FromString, _registered_method=True)
        self.GetDeviceSession = channel.unary_unary('/google.cloud.devicestreaming.v1.DirectAccessService/GetDeviceSession', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.GetDeviceSessionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, _registered_method=True)
        self.CancelDeviceSession = channel.unary_unary('/google.cloud.devicestreaming.v1.DirectAccessService/CancelDeviceSession', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CancelDeviceSessionRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.UpdateDeviceSession = channel.unary_unary('/google.cloud.devicestreaming.v1.DirectAccessService/UpdateDeviceSession', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.UpdateDeviceSessionRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, _registered_method=True)
        self.AdbConnect = channel.stream_stream('/google.cloud.devicestreaming.v1.DirectAccessService/AdbConnect', request_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.AdbMessage.SerializeToString, response_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.DeviceMessage.FromString, _registered_method=True)

class DirectAccessServiceServicer(object):
    """A service for allocating Android devices and interacting with the
    live-allocated devices.

    Each Session will wait for available capacity, at a higher
    priority over Test Execution. When allocated, the session will be exposed
    through a stream for integration.

    DirectAccessService is currently available as a preview to select developers.
    You can register today on behalf of you and your team at
    https://developer.android.com/studio/preview/android-device-streaming
    """

    def CreateDeviceSession(self, request, context):
        """Creates a DeviceSession.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListDeviceSessions(self, request, context):
        """Lists DeviceSessions owned by the project user.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetDeviceSession(self, request, context):
        """Gets a DeviceSession, which documents the allocation status and
        whether the device is allocated. Clients making requests from this API
        must poll GetDeviceSession.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CancelDeviceSession(self, request, context):
        """Cancel a DeviceSession.
        This RPC changes the DeviceSession to state FINISHED and terminates all
        connections.
        Canceled sessions are not deleted and can be retrieved or
        listed by the user until they expire based on the 28 day deletion policy.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateDeviceSession(self, request, context):
        """Updates the current DeviceSession to the fields described by the
        update_mask.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AdbConnect(self, request_iterator, context):
        """Exposes an ADB connection if the device supports ADB.
        gRPC headers are used to authenticate the Connect RPC, as well as
        associate to a particular DeviceSession.
        In particular, the user must specify the "X-Omnilab-Session-Name" header.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_DirectAccessServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateDeviceSession': grpc.unary_unary_rpc_method_handler(servicer.CreateDeviceSession, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CreateDeviceSessionRequest.FromString, response_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.SerializeToString), 'ListDeviceSessions': grpc.unary_unary_rpc_method_handler(servicer.ListDeviceSessions, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsRequest.FromString, response_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsResponse.SerializeToString), 'GetDeviceSession': grpc.unary_unary_rpc_method_handler(servicer.GetDeviceSession, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.GetDeviceSessionRequest.FromString, response_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.SerializeToString), 'CancelDeviceSession': grpc.unary_unary_rpc_method_handler(servicer.CancelDeviceSession, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CancelDeviceSessionRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'UpdateDeviceSession': grpc.unary_unary_rpc_method_handler(servicer.UpdateDeviceSession, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.UpdateDeviceSessionRequest.FromString, response_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.SerializeToString), 'AdbConnect': grpc.stream_stream_rpc_method_handler(servicer.AdbConnect, request_deserializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.AdbMessage.FromString, response_serializer=google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.DeviceMessage.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.devicestreaming.v1.DirectAccessService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.devicestreaming.v1.DirectAccessService', rpc_method_handlers)

class DirectAccessService(object):
    """A service for allocating Android devices and interacting with the
    live-allocated devices.

    Each Session will wait for available capacity, at a higher
    priority over Test Execution. When allocated, the session will be exposed
    through a stream for integration.

    DirectAccessService is currently available as a preview to select developers.
    You can register today on behalf of you and your team at
    https://developer.android.com/studio/preview/android-device-streaming
    """

    @staticmethod
    def CreateDeviceSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.devicestreaming.v1.DirectAccessService/CreateDeviceSession', google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CreateDeviceSessionRequest.SerializeToString, google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListDeviceSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.devicestreaming.v1.DirectAccessService/ListDeviceSessions', google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsRequest.SerializeToString, google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.ListDeviceSessionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetDeviceSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.devicestreaming.v1.DirectAccessService/GetDeviceSession', google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.GetDeviceSessionRequest.SerializeToString, google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CancelDeviceSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.devicestreaming.v1.DirectAccessService/CancelDeviceSession', google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.CancelDeviceSessionRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateDeviceSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.devicestreaming.v1.DirectAccessService/UpdateDeviceSession', google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.UpdateDeviceSessionRequest.SerializeToString, google_dot_cloud_dot_devicestreaming_dot_v1_dot_service__pb2.DeviceSession.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def AdbConnect(request_iterator, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/google.cloud.devicestreaming.v1.DirectAccessService/AdbConnect', google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.AdbMessage.SerializeToString, google_dot_cloud_dot_devicestreaming_dot_v1_dot_adb__service__pb2.DeviceMessage.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)