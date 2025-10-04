"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1beta1/session_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.aiplatform.v1beta1 import operation_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_operation__pb2
from .....google.cloud.aiplatform.v1beta1 import session_pb2 as google_dot_cloud_dot_aiplatform_dot_v1beta1_dot_session__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/aiplatform/v1beta1/session_service.proto\x12\x1fgoogle.cloud.aiplatform.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a/google/cloud/aiplatform/v1beta1/operation.proto\x1a-google/cloud/aiplatform/v1beta1/session.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\x99\x01\n\x14CreateSessionRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12>\n\x07session\x18\x02 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.SessionB\x03\xe0A\x02"u\n\x1eCreateSessionOperationMetadata\x12S\n\x10generic_metadata\x18\x01 \x01(\x0b29.google.cloud.aiplatform.v1beta1.GenericOperationMetadata"L\n\x11GetSessionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session"\xb5\x01\n\x13ListSessionsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"k\n\x14ListSessionsResponse\x12:\n\x08sessions\x18\x01 \x03(\x0b2(.google.cloud.aiplatform.v1beta1.Session\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8c\x01\n\x14UpdateSessionRequest\x12>\n\x07session\x18\x01 \x01(\x0b2(.google.cloud.aiplatform.v1beta1.SessionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"O\n\x14DeleteSessionRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session"\x94\x01\n\x11ListEventsRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01"t\n\x12ListEventsResponse\x12E\n\x0esession_events\x18\x01 \x03(\x0b2-.google.cloud.aiplatform.v1beta1.SessionEvent\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x90\x01\n\x12AppendEventRequest\x127\n\x04name\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session\x12A\n\x05event\x18\x02 \x01(\x0b2-.google.cloud.aiplatform.v1beta1.SessionEventB\x03\xe0A\x02"\x15\n\x13AppendEventResponse2\xa3\x10\n\x0eSessionService\x12\xb5\x02\n\rCreateSession\x125.google.cloud.aiplatform.v1beta1.CreateSessionRequest\x1a\x1d.google.longrunning.Operation"\xcd\x01\xcaA)\n\x07Session\x12\x1eCreateSessionOperationMetadata\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02\x89\x01"D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/sessions:\x07sessionZ8"-/v1beta1/{parent=reasoningEngines/*}/sessions:\x07session\x12\xf1\x01\n\nGetSession\x122.google.cloud.aiplatform.v1beta1.GetSessionRequest\x1a(.google.cloud.aiplatform.v1beta1.Session"\x84\x01\xdaA\x04name\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}Z/\x12-/v1beta1/{name=reasoningEngines/*/sessions/*}\x12\x84\x02\n\x0cListSessions\x124.google.cloud.aiplatform.v1beta1.ListSessionsRequest\x1a5.google.cloud.aiplatform.v1beta1.ListSessionsResponse"\x86\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/sessionsZ/\x12-/v1beta1/{parent=reasoningEngines/*}/sessions\x12\xa9\x02\n\rUpdateSession\x125.google.cloud.aiplatform.v1beta1.UpdateSessionRequest\x1a(.google.cloud.aiplatform.v1beta1.Session"\xb6\x01\xdaA\x13session,update_mask\x82\xd3\xe4\x93\x02\x99\x012L/v1beta1/{session.name=projects/*/locations/*/reasoningEngines/*/sessions/*}:\x07sessionZ@25/v1beta1/{session.name=reasoningEngines/*/sessions/*}:\x07session\x12\x9f\x02\n\rDeleteSession\x125.google.cloud.aiplatform.v1beta1.DeleteSessionRequest\x1a\x1d.google.longrunning.Operation"\xb7\x01\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02w*D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}Z/*-/v1beta1/{name=reasoningEngines/*/sessions/*}\x12\x91\x02\n\nListEvents\x122.google.cloud.aiplatform.v1beta1.ListEventsRequest\x1a3.google.cloud.aiplatform.v1beta1.ListEventsResponse"\x99\x01\xdaA\x06parent\x82\xd3\xe4\x93\x02\x89\x01\x12M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*/sessions/*}/eventsZ8\x126/v1beta1/{parent=reasoningEngines/*/sessions/*}/events\x12\xac\x02\n\x0bAppendEvent\x123.google.cloud.aiplatform.v1beta1.AppendEventRequest\x1a4.google.cloud.aiplatform.v1beta1.AppendEventResponse"\xb1\x01\xdaA\nname,event\x82\xd3\xe4\x93\x02\x9d\x01"P/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}:appendEvent:\x05eventZB"9/v1beta1/{name=reasoningEngines/*/sessions/*}:appendEvent:\x05event\x1aM\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xea\x01\n#com.google.cloud.aiplatform.v1beta1B\x13SessionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1beta1.session_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.aiplatform.v1beta1B\x13SessionServiceProtoP\x01ZCcloud.google.com/go/aiplatform/apiv1beta1/aiplatformpb;aiplatformpb\xaa\x02\x1fGoogle.Cloud.AIPlatform.V1Beta1\xca\x02\x1fGoogle\\Cloud\\AIPlatform\\V1beta1\xea\x02"Google::Cloud::AIPlatform::V1beta1'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETSESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)aiplatform.googleapis.com/ReasoningEngine'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTSESSIONSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATESESSIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_UPDATESESSIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATESESSIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATESESSIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETESESSIONREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTEVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTEVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_APPENDEVENTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_APPENDEVENTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA#\n!aiplatform.googleapis.com/Session'
    _globals['_APPENDEVENTREQUEST'].fields_by_name['event']._loaded_options = None
    _globals['_APPENDEVENTREQUEST'].fields_by_name['event']._serialized_options = b'\xe0A\x02'
    _globals['_SESSIONSERVICE']._loaded_options = None
    _globals['_SESSIONSERVICE']._serialized_options = b'\xcaA\x19aiplatform.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SESSIONSERVICE'].methods_by_name['CreateSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['CreateSession']._serialized_options = b'\xcaA)\n\x07Session\x12\x1eCreateSessionOperationMetadata\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02\x89\x01"D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/sessions:\x07sessionZ8"-/v1beta1/{parent=reasoningEngines/*}/sessions:\x07session'
    _globals['_SESSIONSERVICE'].methods_by_name['GetSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['GetSession']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}Z/\x12-/v1beta1/{name=reasoningEngines/*/sessions/*}'
    _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['ListSessions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02w\x12D/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*}/sessionsZ/\x12-/v1beta1/{parent=reasoningEngines/*}/sessions'
    _globals['_SESSIONSERVICE'].methods_by_name['UpdateSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['UpdateSession']._serialized_options = b'\xdaA\x13session,update_mask\x82\xd3\xe4\x93\x02\x99\x012L/v1beta1/{session.name=projects/*/locations/*/reasoningEngines/*/sessions/*}:\x07sessionZ@25/v1beta1/{session.name=reasoningEngines/*/sessions/*}:\x07session'
    _globals['_SESSIONSERVICE'].methods_by_name['DeleteSession']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['DeleteSession']._serialized_options = b'\xcaA0\n\x15google.protobuf.Empty\x12\x17DeleteOperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02w*D/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}Z/*-/v1beta1/{name=reasoningEngines/*/sessions/*}'
    _globals['_SESSIONSERVICE'].methods_by_name['ListEvents']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['ListEvents']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\x89\x01\x12M/v1beta1/{parent=projects/*/locations/*/reasoningEngines/*/sessions/*}/eventsZ8\x126/v1beta1/{parent=reasoningEngines/*/sessions/*}/events'
    _globals['_SESSIONSERVICE'].methods_by_name['AppendEvent']._loaded_options = None
    _globals['_SESSIONSERVICE'].methods_by_name['AppendEvent']._serialized_options = b'\xdaA\nname,event\x82\xd3\xe4\x93\x02\x9d\x01"P/v1beta1/{name=projects/*/locations/*/reasoningEngines/*/sessions/*}:appendEvent:\x05eventZB"9/v1beta1/{name=reasoningEngines/*/sessions/*}:appendEvent:\x05event'
    _globals['_CREATESESSIONREQUEST']._serialized_start = 402
    _globals['_CREATESESSIONREQUEST']._serialized_end = 555
    _globals['_CREATESESSIONOPERATIONMETADATA']._serialized_start = 557
    _globals['_CREATESESSIONOPERATIONMETADATA']._serialized_end = 674
    _globals['_GETSESSIONREQUEST']._serialized_start = 676
    _globals['_GETSESSIONREQUEST']._serialized_end = 752
    _globals['_LISTSESSIONSREQUEST']._serialized_start = 755
    _globals['_LISTSESSIONSREQUEST']._serialized_end = 936
    _globals['_LISTSESSIONSRESPONSE']._serialized_start = 938
    _globals['_LISTSESSIONSRESPONSE']._serialized_end = 1045
    _globals['_UPDATESESSIONREQUEST']._serialized_start = 1048
    _globals['_UPDATESESSIONREQUEST']._serialized_end = 1188
    _globals['_DELETESESSIONREQUEST']._serialized_start = 1190
    _globals['_DELETESESSIONREQUEST']._serialized_end = 1269
    _globals['_LISTEVENTSREQUEST']._serialized_start = 1272
    _globals['_LISTEVENTSREQUEST']._serialized_end = 1420
    _globals['_LISTEVENTSRESPONSE']._serialized_start = 1422
    _globals['_LISTEVENTSRESPONSE']._serialized_end = 1538
    _globals['_APPENDEVENTREQUEST']._serialized_start = 1541
    _globals['_APPENDEVENTREQUEST']._serialized_end = 1685
    _globals['_APPENDEVENTRESPONSE']._serialized_start = 1687
    _globals['_APPENDEVENTRESPONSE']._serialized_end = 1708
    _globals['_SESSIONSERVICE']._serialized_start = 1711
    _globals['_SESSIONSERVICE']._serialized_end = 3794