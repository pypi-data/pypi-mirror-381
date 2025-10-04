"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/spanner/adapter/v1/adapter.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/spanner/adapter/v1/adapter.proto\x12\x19google.spanner.adapter.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x87\x02\n\x13AdaptMessageRequest\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session\x12\x15\n\x08protocol\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07payload\x18\x03 \x01(\x0cB\x03\xe0A\x01\x12Y\n\x0battachments\x18\x04 \x03(\x0b2?.google.spanner.adapter.v1.AdaptMessageRequest.AttachmentsEntryB\x03\xe0A\x01\x1a2\n\x10AttachmentsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xd3\x01\n\x14AdaptMessageResponse\x12\x14\n\x07payload\x18\x01 \x01(\x0cB\x03\xe0A\x01\x12]\n\rstate_updates\x18\x02 \x03(\x0b2A.google.spanner.adapter.v1.AdaptMessageResponse.StateUpdatesEntryB\x03\xe0A\x01\x12\x11\n\x04last\x18\x03 \x01(\x08B\x03\xe0A\x01\x1a3\n\x11StateUpdatesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa7\x01\n\x07Session\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08:\x88\x01\xeaA\x84\x01\n\x1espanner.googleapis.com/Session\x12Oprojects/{project}/instances/{instance}/databases/{database}/sessions/{session}*\x08sessions2\x07session"\x89\x01\n\x14CreateSessionRequest\x127\n\x06parent\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database\x128\n\x07session\x18\x02 \x01(\x0b2".google.spanner.adapter.v1.SessionB\x03\xe0A\x022\x93\x04\n\x07Adapter\x12\xc8\x01\n\rCreateSession\x12/.google.spanner.adapter.v1.CreateSessionRequest\x1a".google.spanner.adapter.v1.Session"b\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02K"@/v1/{parent=projects/*/instances/*/databases/*}/sessions:adapter:\x07session\x12\xc3\x01\n\x0cAdaptMessage\x12..google.spanner.adapter.v1.AdaptMessageRequest\x1a/.google.spanner.adapter.v1.AdaptMessageResponse"P\x82\xd3\xe4\x93\x02J"E/v1/{name=projects/*/instances/*/databases/*/sessions/*}:adaptMessage:\x01*0\x01\x1aw\xcaA\x16spanner.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.dataB\xba\x02\n\x1dcom.google.spanner.adapter.v1B\x0cAdapterProtoP\x01Z=cloud.google.com/go/spanner/adapter/apiv1/adapterpb;adapterpb\xaa\x02\x1fGoogle.Cloud.Spanner.Adapter.V1\xca\x02\x1fGoogle\\Cloud\\Spanner\\Adapter\\V1\xea\x02#Google::Cloud::Spanner::Adapter::V1\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.adapter.v1.adapter_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.spanner.adapter.v1B\x0cAdapterProtoP\x01Z=cloud.google.com/go/spanner/adapter/apiv1/adapterpb;adapterpb\xaa\x02\x1fGoogle.Cloud.Spanner.Adapter.V1\xca\x02\x1fGoogle\\Cloud\\Spanner\\Adapter\\V1\xea\x02#Google::Cloud::Spanner::Adapter::V1\xeaA_\n\x1fspanner.googleapis.com/Database\x12<projects/{project}/instances/{instance}/databases/{database}'
    _globals['_ADAPTMESSAGEREQUEST_ATTACHMENTSENTRY']._loaded_options = None
    _globals['_ADAPTMESSAGEREQUEST_ATTACHMENTSENTRY']._serialized_options = b'8\x01'
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1espanner.googleapis.com/Session'
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['protocol']._loaded_options = None
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['protocol']._serialized_options = b'\xe0A\x02'
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['payload']._loaded_options = None
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['payload']._serialized_options = b'\xe0A\x01'
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['attachments']._loaded_options = None
    _globals['_ADAPTMESSAGEREQUEST'].fields_by_name['attachments']._serialized_options = b'\xe0A\x01'
    _globals['_ADAPTMESSAGERESPONSE_STATEUPDATESENTRY']._loaded_options = None
    _globals['_ADAPTMESSAGERESPONSE_STATEUPDATESENTRY']._serialized_options = b'8\x01'
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['payload']._loaded_options = None
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['payload']._serialized_options = b'\xe0A\x01'
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['state_updates']._loaded_options = None
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['state_updates']._serialized_options = b'\xe0A\x01'
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['last']._loaded_options = None
    _globals['_ADAPTMESSAGERESPONSE'].fields_by_name['last']._serialized_options = b'\xe0A\x01'
    _globals['_SESSION'].fields_by_name['name']._loaded_options = None
    _globals['_SESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SESSION']._loaded_options = None
    _globals['_SESSION']._serialized_options = b'\xeaA\x84\x01\n\x1espanner.googleapis.com/Session\x12Oprojects/{project}/instances/{instance}/databases/{database}/sessions/{session}*\x08sessions2\x07session'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fspanner.googleapis.com/Database'
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._loaded_options = None
    _globals['_CREATESESSIONREQUEST'].fields_by_name['session']._serialized_options = b'\xe0A\x02'
    _globals['_ADAPTER']._loaded_options = None
    _globals['_ADAPTER']._serialized_options = b'\xcaA\x16spanner.googleapis.com\xd2A[https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/spanner.data'
    _globals['_ADAPTER'].methods_by_name['CreateSession']._loaded_options = None
    _globals['_ADAPTER'].methods_by_name['CreateSession']._serialized_options = b'\xdaA\x0eparent,session\x82\xd3\xe4\x93\x02K"@/v1/{parent=projects/*/instances/*/databases/*}/sessions:adapter:\x07session'
    _globals['_ADAPTER'].methods_by_name['AdaptMessage']._loaded_options = None
    _globals['_ADAPTER'].methods_by_name['AdaptMessage']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/v1/{name=projects/*/instances/*/databases/*/sessions/*}:adaptMessage:\x01*'
    _globals['_ADAPTMESSAGEREQUEST']._serialized_start = 186
    _globals['_ADAPTMESSAGEREQUEST']._serialized_end = 449
    _globals['_ADAPTMESSAGEREQUEST_ATTACHMENTSENTRY']._serialized_start = 399
    _globals['_ADAPTMESSAGEREQUEST_ATTACHMENTSENTRY']._serialized_end = 449
    _globals['_ADAPTMESSAGERESPONSE']._serialized_start = 452
    _globals['_ADAPTMESSAGERESPONSE']._serialized_end = 663
    _globals['_ADAPTMESSAGERESPONSE_STATEUPDATESENTRY']._serialized_start = 612
    _globals['_ADAPTMESSAGERESPONSE_STATEUPDATESENTRY']._serialized_end = 663
    _globals['_SESSION']._serialized_start = 666
    _globals['_SESSION']._serialized_end = 833
    _globals['_CREATESESSIONREQUEST']._serialized_start = 836
    _globals['_CREATESESSIONREQUEST']._serialized_end = 973
    _globals['_ADAPTER']._serialized_start = 976
    _globals['_ADAPTER']._serialized_end = 1507