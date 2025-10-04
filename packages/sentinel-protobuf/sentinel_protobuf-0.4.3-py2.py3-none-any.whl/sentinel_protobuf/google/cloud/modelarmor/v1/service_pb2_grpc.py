"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.cloud.modelarmor.v1 import service_pb2 as google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/cloud/modelarmor/v1/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class ModelArmorStub(object):
    """Service describing handlers for resources
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ListTemplates = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/ListTemplates', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesResponse.FromString, _registered_method=True)
        self.GetTemplate = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/GetTemplate', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetTemplateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, _registered_method=True)
        self.CreateTemplate = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/CreateTemplate', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.CreateTemplateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, _registered_method=True)
        self.UpdateTemplate = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/UpdateTemplate', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateTemplateRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, _registered_method=True)
        self.DeleteTemplate = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/DeleteTemplate', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.DeleteTemplateRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.GetFloorSetting = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/GetFloorSetting', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetFloorSettingRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.FromString, _registered_method=True)
        self.UpdateFloorSetting = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/UpdateFloorSetting', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateFloorSettingRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.FromString, _registered_method=True)
        self.SanitizeUserPrompt = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/SanitizeUserPrompt', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptResponse.FromString, _registered_method=True)
        self.SanitizeModelResponse = channel.unary_unary('/google.cloud.modelarmor.v1.ModelArmor/SanitizeModelResponse', request_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseRequest.SerializeToString, response_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseResponse.FromString, _registered_method=True)

class ModelArmorServicer(object):
    """Service describing handlers for resources
    """

    def ListTemplates(self, request, context):
        """Lists Templates in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTemplate(self, request, context):
        """Gets details of a single Template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTemplate(self, request, context):
        """Creates a new Template in a given project and location.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateTemplate(self, request, context):
        """Updates the parameters of a single Template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteTemplate(self, request, context):
        """Deletes a single Template.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFloorSetting(self, request, context):
        """Gets details of a single floor setting of a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateFloorSetting(self, request, context):
        """Updates the parameters of a single floor setting of a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SanitizeUserPrompt(self, request, context):
        """Sanitizes User Prompt.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SanitizeModelResponse(self, request, context):
        """Sanitizes Model Response.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ModelArmorServicer_to_server(servicer, server):
    rpc_method_handlers = {'ListTemplates': grpc.unary_unary_rpc_method_handler(servicer.ListTemplates, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesResponse.SerializeToString), 'GetTemplate': grpc.unary_unary_rpc_method_handler(servicer.GetTemplate, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetTemplateRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.SerializeToString), 'CreateTemplate': grpc.unary_unary_rpc_method_handler(servicer.CreateTemplate, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.CreateTemplateRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.SerializeToString), 'UpdateTemplate': grpc.unary_unary_rpc_method_handler(servicer.UpdateTemplate, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateTemplateRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.SerializeToString), 'DeleteTemplate': grpc.unary_unary_rpc_method_handler(servicer.DeleteTemplate, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.DeleteTemplateRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'GetFloorSetting': grpc.unary_unary_rpc_method_handler(servicer.GetFloorSetting, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetFloorSettingRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.SerializeToString), 'UpdateFloorSetting': grpc.unary_unary_rpc_method_handler(servicer.UpdateFloorSetting, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateFloorSettingRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.SerializeToString), 'SanitizeUserPrompt': grpc.unary_unary_rpc_method_handler(servicer.SanitizeUserPrompt, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptResponse.SerializeToString), 'SanitizeModelResponse': grpc.unary_unary_rpc_method_handler(servicer.SanitizeModelResponse, request_deserializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseRequest.FromString, response_serializer=google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.cloud.modelarmor.v1.ModelArmor', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.cloud.modelarmor.v1.ModelArmor', rpc_method_handlers)

class ModelArmor(object):
    """Service describing handlers for resources
    """

    @staticmethod
    def ListTemplates(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/ListTemplates', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.ListTemplatesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/GetTemplate', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetTemplateRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/CreateTemplate', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.CreateTemplateRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/UpdateTemplate', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateTemplateRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.Template.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteTemplate(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/DeleteTemplate', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.DeleteTemplateRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetFloorSetting(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/GetFloorSetting', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.GetFloorSettingRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateFloorSetting(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/UpdateFloorSetting', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.UpdateFloorSettingRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.FloorSetting.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SanitizeUserPrompt(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/SanitizeUserPrompt', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeUserPromptResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def SanitizeModelResponse(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.cloud.modelarmor.v1.ModelArmor/SanitizeModelResponse', google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseRequest.SerializeToString, google_dot_cloud_dot_modelarmor_dot_v1_dot_service__pb2.SanitizeModelResponseResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)