"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings
from .....google.apps.meet.v2beta import resource_pb2 as google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2
from .....google.apps.meet.v2beta import service_pb2 as google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2
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
    raise RuntimeError(f'The grpc package installed is at version {GRPC_VERSION},' + f' but the generated code in google/apps/meet/v2beta/service_pb2_grpc.py depends on' + f' grpcio>={GRPC_GENERATED_VERSION}.' + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}' + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.')

class SpacesServiceStub(object):
    """REST API for services dealing with spaces.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateSpace = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/CreateSpace', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateSpaceRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, _registered_method=True)
        self.GetSpace = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/GetSpace', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetSpaceRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, _registered_method=True)
        self.UpdateSpace = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/UpdateSpace', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.UpdateSpaceRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, _registered_method=True)
        self.ConnectActiveConference = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/ConnectActiveConference', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceResponse.FromString, _registered_method=True)
        self.EndActiveConference = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/EndActiveConference', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.EndActiveConferenceRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)
        self.CreateMember = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/CreateMember', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateMemberRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.FromString, _registered_method=True)
        self.GetMember = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/GetMember', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetMemberRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.FromString, _registered_method=True)
        self.ListMembers = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/ListMembers', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersResponse.FromString, _registered_method=True)
        self.DeleteMember = channel.unary_unary('/google.apps.meet.v2beta.SpacesService/DeleteMember', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.DeleteMemberRequest.SerializeToString, response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString, _registered_method=True)

class SpacesServiceServicer(object):
    """REST API for services dealing with spaces.
    """

    def CreateSpace(self, request, context):
        """Creates a space.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSpace(self, request, context):
        """Gets details about a meeting space.

        For an example, see [Get a meeting
        space](https://developers.google.com/meet/api/guides/meeting-spaces#get-meeting-space).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateSpace(self, request, context):
        """Updates details about a meeting space.

        For an example, see [Update a meeting
        space](https://developers.google.com/meet/api/guides/meeting-spaces#update-meeting-space).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConnectActiveConference(self, request, context):
        """[Developer Preview](https://developers.google.com/workspace/preview):
        Broker a WebRTC connection to the active conference of a space.

        On success, clients must use the resulting SDP (Session Description
        Protocol) answer to establish a WebRTC connection. Once connected,
        additional functionality is available across WebRTC data channels.

        See [Meet Media API
        overview](https://developers.google.com/meet/media-api/guides/overview) for
        more details about this connection.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def EndActiveConference(self, request, context):
        """Ends an active conference (if there's one).

        For an example, see [End active
        conference](https://developers.google.com/meet/api/guides/meeting-spaces#end-active-conference).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateMember(self, request, context):
        """[Developer Preview](https://developers.google.com/workspace/preview):
        Create a member.

        This API supports the `fields` parameter in
        [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters).
        When the `fields` parameter is omitted, this API response will default to
        "name,email,role,user".
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetMember(self, request, context):
        """[Developer Preview](https://developers.google.com/workspace/preview):
        Get a member.

        This API supports the `fields` parameter in
        [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters).
        When the `fields` parameter is omitted, this API response will default to
        "name,email,role,user".
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListMembers(self, request, context):
        """[Developer Preview](https://developers.google.com/workspace/preview):
        List members.

        This API supports the `fields` parameter in
        [SystemParameterContext](https://cloud.google.com/apis/docs/system-parameters).
        When the `fields` parameter is omitted this API response will default to
        "name,email,role,user".
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteMember(self, request, context):
        """[Developer Preview](https://developers.google.com/workspace/preview):
        Delete the member who was previously assigned roles in the space.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_SpacesServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'CreateSpace': grpc.unary_unary_rpc_method_handler(servicer.CreateSpace, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateSpaceRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.SerializeToString), 'GetSpace': grpc.unary_unary_rpc_method_handler(servicer.GetSpace, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetSpaceRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.SerializeToString), 'UpdateSpace': grpc.unary_unary_rpc_method_handler(servicer.UpdateSpace, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.UpdateSpaceRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.SerializeToString), 'ConnectActiveConference': grpc.unary_unary_rpc_method_handler(servicer.ConnectActiveConference, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceResponse.SerializeToString), 'EndActiveConference': grpc.unary_unary_rpc_method_handler(servicer.EndActiveConference, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.EndActiveConferenceRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString), 'CreateMember': grpc.unary_unary_rpc_method_handler(servicer.CreateMember, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateMemberRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.SerializeToString), 'GetMember': grpc.unary_unary_rpc_method_handler(servicer.GetMember, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetMemberRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.SerializeToString), 'ListMembers': grpc.unary_unary_rpc_method_handler(servicer.ListMembers, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersResponse.SerializeToString), 'DeleteMember': grpc.unary_unary_rpc_method_handler(servicer.DeleteMember, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.DeleteMemberRequest.FromString, response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.apps.meet.v2beta.SpacesService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.apps.meet.v2beta.SpacesService', rpc_method_handlers)

class SpacesService(object):
    """REST API for services dealing with spaces.
    """

    @staticmethod
    def CreateSpace(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/CreateSpace', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateSpaceRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetSpace(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/GetSpace', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetSpaceRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def UpdateSpace(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/UpdateSpace', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.UpdateSpaceRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Space.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ConnectActiveConference(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/ConnectActiveConference', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ConnectActiveConferenceResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def EndActiveConference(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/EndActiveConference', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.EndActiveConferenceRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def CreateMember(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/CreateMember', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.CreateMemberRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetMember(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/GetMember', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetMemberRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Member.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListMembers(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/ListMembers', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListMembersResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def DeleteMember(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.SpacesService/DeleteMember', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.DeleteMemberRequest.SerializeToString, google_dot_protobuf_dot_empty__pb2.Empty.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

class ConferenceRecordsServiceStub(object):
    """REST API for services dealing with conference records.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetConferenceRecord = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetConferenceRecord', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetConferenceRecordRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ConferenceRecord.FromString, _registered_method=True)
        self.ListConferenceRecords = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListConferenceRecords', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsResponse.FromString, _registered_method=True)
        self.GetParticipant = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetParticipant', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Participant.FromString, _registered_method=True)
        self.ListParticipants = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListParticipants', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsResponse.FromString, _registered_method=True)
        self.GetParticipantSession = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetParticipantSession', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantSessionRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ParticipantSession.FromString, _registered_method=True)
        self.ListParticipantSessions = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListParticipantSessions', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsResponse.FromString, _registered_method=True)
        self.GetRecording = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetRecording', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetRecordingRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Recording.FromString, _registered_method=True)
        self.ListRecordings = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListRecordings', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsResponse.FromString, _registered_method=True)
        self.GetTranscript = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetTranscript', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Transcript.FromString, _registered_method=True)
        self.ListTranscripts = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListTranscripts', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsResponse.FromString, _registered_method=True)
        self.GetTranscriptEntry = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/GetTranscriptEntry', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptEntryRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.TranscriptEntry.FromString, _registered_method=True)
        self.ListTranscriptEntries = channel.unary_unary('/google.apps.meet.v2beta.ConferenceRecordsService/ListTranscriptEntries', request_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesRequest.SerializeToString, response_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesResponse.FromString, _registered_method=True)

class ConferenceRecordsServiceServicer(object):
    """REST API for services dealing with conference records.
    """

    def GetConferenceRecord(self, request, context):
        """Gets a conference record by conference ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListConferenceRecords(self, request, context):
        """Lists the conference records. By default, ordered by start time and in
        descending order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParticipant(self, request, context):
        """Gets a participant by participant ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListParticipants(self, request, context):
        """Lists the participants in a conference record. By default, ordered by join
        time and in descending order. This API supports `fields` as standard
        parameters like every other API. However, when the `fields` request
        parameter is omitted, this API defaults to `'participants/*,
        next_page_token'`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetParticipantSession(self, request, context):
        """Gets a participant session by participant session ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListParticipantSessions(self, request, context):
        """Lists the participant sessions of a participant in a conference record. By
        default, ordered by join time and in descending order. This API supports
        `fields` as standard parameters like every other API. However, when the
        `fields` request parameter is omitted this API defaults to
        `'participantsessions/*, next_page_token'`.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRecording(self, request, context):
        """Gets a recording by recording ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListRecordings(self, request, context):
        """Lists the recording resources from the conference record. By default,
        ordered by start time and in ascending order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTranscript(self, request, context):
        """Gets a transcript by transcript ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTranscripts(self, request, context):
        """Lists the set of transcripts from the conference record. By default,
        ordered by start time and in ascending order.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetTranscriptEntry(self, request, context):
        """Gets a `TranscriptEntry` resource by entry ID.

        Note: The transcript entries returned by the Google Meet API might not
        match the transcription found in the Google Docs transcript file. This can
        occur when the Google Docs transcript file is modified after generation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListTranscriptEntries(self, request, context):
        """Lists the structured transcript entries per transcript. By default, ordered
        by start time and in ascending order.

        Note: The transcript entries returned by the Google Meet API might not
        match the transcription found in the Google Docs transcript file. This can
        occur when the Google Docs transcript file is modified after generation.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

def add_ConferenceRecordsServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {'GetConferenceRecord': grpc.unary_unary_rpc_method_handler(servicer.GetConferenceRecord, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetConferenceRecordRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ConferenceRecord.SerializeToString), 'ListConferenceRecords': grpc.unary_unary_rpc_method_handler(servicer.ListConferenceRecords, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsResponse.SerializeToString), 'GetParticipant': grpc.unary_unary_rpc_method_handler(servicer.GetParticipant, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Participant.SerializeToString), 'ListParticipants': grpc.unary_unary_rpc_method_handler(servicer.ListParticipants, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsResponse.SerializeToString), 'GetParticipantSession': grpc.unary_unary_rpc_method_handler(servicer.GetParticipantSession, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantSessionRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ParticipantSession.SerializeToString), 'ListParticipantSessions': grpc.unary_unary_rpc_method_handler(servicer.ListParticipantSessions, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsResponse.SerializeToString), 'GetRecording': grpc.unary_unary_rpc_method_handler(servicer.GetRecording, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetRecordingRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Recording.SerializeToString), 'ListRecordings': grpc.unary_unary_rpc_method_handler(servicer.ListRecordings, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsResponse.SerializeToString), 'GetTranscript': grpc.unary_unary_rpc_method_handler(servicer.GetTranscript, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Transcript.SerializeToString), 'ListTranscripts': grpc.unary_unary_rpc_method_handler(servicer.ListTranscripts, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsResponse.SerializeToString), 'GetTranscriptEntry': grpc.unary_unary_rpc_method_handler(servicer.GetTranscriptEntry, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptEntryRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.TranscriptEntry.SerializeToString), 'ListTranscriptEntries': grpc.unary_unary_rpc_method_handler(servicer.ListTranscriptEntries, request_deserializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesRequest.FromString, response_serializer=google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesResponse.SerializeToString)}
    generic_handler = grpc.method_handlers_generic_handler('google.apps.meet.v2beta.ConferenceRecordsService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('google.apps.meet.v2beta.ConferenceRecordsService', rpc_method_handlers)

class ConferenceRecordsService(object):
    """REST API for services dealing with conference records.
    """

    @staticmethod
    def GetConferenceRecord(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetConferenceRecord', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetConferenceRecordRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ConferenceRecord.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListConferenceRecords(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListConferenceRecords', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListConferenceRecordsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetParticipant(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetParticipant', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Participant.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListParticipants(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListParticipants', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetParticipantSession(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetParticipantSession', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetParticipantSessionRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.ParticipantSession.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListParticipantSessions(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListParticipantSessions', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListParticipantSessionsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetRecording(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetRecording', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetRecordingRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Recording.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListRecordings(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListRecordings', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListRecordingsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTranscript(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetTranscript', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.Transcript.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTranscripts(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListTranscripts', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptsResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def GetTranscriptEntry(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/GetTranscriptEntry', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.GetTranscriptEntryRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_resource__pb2.TranscriptEntry.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)

    @staticmethod
    def ListTranscriptEntries(request, target, options=(), channel_credentials=None, call_credentials=None, insecure=False, compression=None, wait_for_ready=None, timeout=None, metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.apps.meet.v2beta.ConferenceRecordsService/ListTranscriptEntries', google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesRequest.SerializeToString, google_dot_apps_dot_meet_dot_v2beta_dot_service__pb2.ListTranscriptEntriesResponse.FromString, options, channel_credentials, insecure, call_credentials, compression, wait_for_ready, timeout, metadata, _registered_method=True)