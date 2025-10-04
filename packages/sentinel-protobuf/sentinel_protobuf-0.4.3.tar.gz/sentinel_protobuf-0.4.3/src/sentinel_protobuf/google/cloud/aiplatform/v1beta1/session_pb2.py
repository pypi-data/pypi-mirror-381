"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/session.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import content_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_content__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/aiplatform/v1beta1/session.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/aiplatform/v1beta1/content.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x86\x04\n\x07Session\x126\n\x0bexpire_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x00\x120\n\x03ttl\x18\x0e \x01(\x0b2\x19.google.protobuf.DurationB\x06\xe0A\x01\xe0A\x04H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x123\n\rsession_state\x18\n \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x17\n\x07user_id\x18\x0c \x01(\tB\x06\xe0A\x05\xe0A\x02:\x9a\x01\xeaA\x96\x01\n!aiplatform.googleapis.com/Session\x12^projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}*\x08sessions2\x07sessionB\x0c\n\nexpiration"\xc8\x04\n\x0cSessionEvent\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x13\n\x06author\x18\x03 \x01(\tB\x03\xe0A\x02\x12>\n\x07content\x18\x04 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.ContentB\x03\xe0A\x01\x12\x1a\n\rinvocation_id\x18\x05 \x01(\tB\x03\xe0A\x02\x12C\n\x07actions\x18\x06 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.EventActionsB\x03\xe0A\x01\x122\n\ttimestamp\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x17\n\nerror_code\x18\t \x01(\tB\x03\xe0A\x01\x12\x1a\n\rerror_message\x18\n \x01(\tB\x03\xe0A\x01\x12K\n\x0eevent_metadata\x18\x0b \x01(\x0b2..google.cloud.aiplatform.v1beta1.EventMetadataB\x03\xe0A\x01:\xb8\x01\xeaA\xb4\x01\n&aiplatform.googleapis.com/SessionEvent\x12mprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}/events/{event}*\rsessionEvents2\x0csessionEvent"\x9b\x02\n\rEventMetadata\x12S\n\x12grounding_metadata\x18\x01 \x01(\x0b22.google.cloud.aiplatform.v1beta1.GroundingMetadataB\x03\xe0A\x01\x12\x14\n\x07partial\x18\x02 \x01(\x08B\x03\xe0A\x01\x12\x1a\n\rturn_complete\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x18\n\x0binterrupted\x18\x04 \x01(\x08B\x03\xe0A\x01\x12"\n\x15long_running_tool_ids\x18\x05 \x03(\tB\x03\xe0A\x01\x12\x13\n\x06branch\x18\x06 \x01(\tB\x03\xe0A\x01\x120\n\x0fcustom_metadata\x18\x07 \x01(\x0b2\x17.google.protobuf.Struct"\x88\x03\n\x0cEventActions\x12\x1f\n\x12skip_summarization\x18\x01 \x01(\x08B\x03\xe0A\x01\x121\n\x0bstate_delta\x18\x02 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12]\n\x0eartifact_delta\x18\x03 \x03(\x0b2@.google.cloud.aiplatform.v1beta1.EventActions.ArtifactDeltaEntryB\x03\xe0A\x01\x12\x1d\n\x11transfer_to_agent\x18\x05 \x01(\x08B\x02\x18\x01\x12\x15\n\x08escalate\x18\x06 \x01(\x08B\x03\xe0A\x01\x12<\n\x16requested_auth_configs\x18\x07 \x01(\x0b2\x17.google.protobuf.StructB\x03\xe0A\x01\x12\x1b\n\x0etransfer_agent\x18\x08 \x01(\tB\x03\xe0A\x01\x1a4\n\x12ArtifactDeltaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x05:\x028\x01B\xe3\x01\n#com.google.cloud.aiplatform.v1beta1B\x0cSessionProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x0cSessionProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_SESSION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['ttl']._loaded_options = None
    _globals['_SESSION'].fields_by_name['ttl']._serialized_options = b'\xe0A\x01\xe0A\x04'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SESSION'].fields_by_name['create_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['update_time']._loaded_options = None
    _globals['_SESSION'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_SESSION'].fields_by_name['display_name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['session_state']._loaded_options = None
    _globals['_SESSION'].fields_by_name['session_state']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['user_id']._loaded_options = None
    _globals['_SESSION'].fields_by_name['user_id']._serialized_options = b'\xe0A\x05\xe0A\x02'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\x96\x01\n!aiplatform.googleapis.com/Session\x12^projects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}*\x08sessions2\x07session'
    _globals['_SESSIONEVENT'].fields_by_name['name']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SESSIONEVENT'].fields_by_name['author']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['author']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONEVENT'].fields_by_name['content']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['content']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONEVENT'].fields_by_name['invocation_id']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['invocation_id']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONEVENT'].fields_by_name['actions']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['actions']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONEVENT'].fields_by_name['timestamp']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['timestamp']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONEVENT'].fields_by_name['error_code']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['error_code']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONEVENT'].fields_by_name['error_message']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['error_message']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONEVENT'].fields_by_name['event_metadata']._loaded_options = None
    _globals['_SESSIONEVENT'].fields_by_name['event_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_SESSIONEVENT']._loaded_options = None
    _globals['_SESSIONEVENT']._serialized_options = b'\xeaA\xb4\x01\n&aiplatform.googleapis.com/SessionEvent\x12mprojects/{project}/locations/{location}/reasoningEngines/{reasoning_engine}/sessions/{session}/events/{event}*\rsessionEvents2\x0csessionEvent'
    _globals['_EVENTMETADATA'].fields_by_name['grounding_metadata']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['grounding_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTMETADATA'].fields_by_name['partial']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['partial']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTMETADATA'].fields_by_name['turn_complete']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['turn_complete']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTMETADATA'].fields_by_name['interrupted']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['interrupted']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTMETADATA'].fields_by_name['long_running_tool_ids']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['long_running_tool_ids']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTMETADATA'].fields_by_name['branch']._loaded_options = None
    _globals['_EVENTMETADATA'].fields_by_name['branch']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS_ARTIFACTDELTAENTRY']._loaded_options = None
    _globals['_EVENTACTIONS_ARTIFACTDELTAENTRY']._serialized_options = b'8\x01'
    _globals['_EVENTACTIONS'].fields_by_name['skip_summarization']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['skip_summarization']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS'].fields_by_name['state_delta']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['state_delta']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS'].fields_by_name['artifact_delta']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['artifact_delta']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS'].fields_by_name['transfer_to_agent']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['transfer_to_agent']._serialized_options = b'\x18\x01'
    _globals['_EVENTACTIONS'].fields_by_name['escalate']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['escalate']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS'].fields_by_name['requested_auth_configs']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['requested_auth_configs']._serialized_options = b'\xe0A\x01'
    _globals['_EVENTACTIONS'].fields_by_name['transfer_agent']._loaded_options = None
    _globals['_EVENTACTIONS'].fields_by_name['transfer_agent']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION']._serialized_start = 285
    _globals['_SESSION']._serialized_end = 803
    _globals['_SESSIONEVENT']._serialized_start = 806
    _globals['_SESSIONEVENT']._serialized_end = 1390
    _globals['_EVENTMETADATA']._serialized_start = 1393
    _globals['_EVENTMETADATA']._serialized_end = 1676
    _globals['_EVENTACTIONS']._serialized_start = 1679
    _globals['_EVENTACTIONS']._serialized_end = 2071
    _globals['_EVENTACTIONS_ARTIFACTDELTAENTRY']._serialized_start = 2019
    _globals['_EVENTACTIONS_ARTIFACTDELTAENTRY']._serialized_end = 2071