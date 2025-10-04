"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dialogflow/cx/v3beta1/changelog.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/cloud/dialogflow/cx/v3beta1/changelog.proto\x12"google.cloud.dialogflow.cx.v3beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x8b\x01\n\x15ListChangelogsRequest\x12;\n\x06parent\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Changelog\x12\x0e\n\x06filter\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05\x12\x12\n\npage_token\x18\x04 \x01(\t"t\n\x16ListChangelogsResponse\x12A\n\nchangelogs\x18\x01 \x03(\x0b2-.google.cloud.dialogflow.cx.v3beta1.Changelog\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"P\n\x13GetChangelogRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Changelog"\xb4\x02\n\tChangelog\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nuser_email\x18\x02 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x07 \x01(\t\x12\x0e\n\x06action\x18\x0b \x01(\t\x12\x0c\n\x04type\x18\x08 \x01(\t\x12\x10\n\x08resource\x18\x03 \x01(\t\x12/\n\x0bcreate_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rlanguage_code\x18\x0e \x01(\t:w\xeaAt\n#dialogflow.googleapis.com/Changelog\x12Mprojects/{project}/locations/{location}/agents/{agent}/changelogs/{changelog}2\xa5\x04\n\nChangelogs\x12\xd6\x01\n\x0eListChangelogs\x129.google.cloud.dialogflow.cx.v3beta1.ListChangelogsRequest\x1a:.google.cloud.dialogflow.cx.v3beta1.ListChangelogsResponse"M\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v3beta1/{parent=projects/*/locations/*/agents/*}/changelogs\x12\xc3\x01\n\x0cGetChangelog\x127.google.cloud.dialogflow.cx.v3beta1.GetChangelogRequest\x1a-.google.cloud.dialogflow.cx.v3beta1.Changelog"K\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v3beta1/{name=projects/*/locations/*/agents/*/changelogs/*}\x1ax\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflowB\xc5\x01\n&com.google.cloud.dialogflow.cx.v3beta1B\x0eChangelogProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dialogflow.cx.v3beta1.changelog_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.cloud.dialogflow.cx.v3beta1B\x0eChangelogProtoP\x01Z6cloud.google.com/go/dialogflow/cx/apiv3beta1/cxpb;cxpb\xa2\x02\x02DF\xaa\x02"Google.Cloud.Dialogflow.Cx.V3Beta1\xea\x02&Google::Cloud::Dialogflow::CX::V3beta1'
    _globals['_LISTCHANGELOGSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTCHANGELOGSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA%\x12#dialogflow.googleapis.com/Changelog'
    _globals['_GETCHANGELOGREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETCHANGELOGREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#dialogflow.googleapis.com/Changelog'
    _globals['_CHANGELOG']._loaded_options = None
    _globals['_CHANGELOG']._serialized_options = b'\xeaAt\n#dialogflow.googleapis.com/Changelog\x12Mprojects/{project}/locations/{location}/agents/{agent}/changelogs/{changelog}'
    _globals['_CHANGELOGS']._loaded_options = None
    _globals['_CHANGELOGS']._serialized_options = b'\xcaA\x19dialogflow.googleapis.com\xd2AYhttps://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/dialogflow'
    _globals['_CHANGELOGS'].methods_by_name['ListChangelogs']._loaded_options = None
    _globals['_CHANGELOGS'].methods_by_name['ListChangelogs']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02>\x12</v3beta1/{parent=projects/*/locations/*/agents/*}/changelogs'
    _globals['_CHANGELOGS'].methods_by_name['GetChangelog']._loaded_options = None
    _globals['_CHANGELOGS'].methods_by_name['GetChangelog']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02>\x12</v3beta1/{name=projects/*/locations/*/agents/*/changelogs/*}'
    _globals['_LISTCHANGELOGSREQUEST']._serialized_start = 239
    _globals['_LISTCHANGELOGSREQUEST']._serialized_end = 378
    _globals['_LISTCHANGELOGSRESPONSE']._serialized_start = 380
    _globals['_LISTCHANGELOGSRESPONSE']._serialized_end = 496
    _globals['_GETCHANGELOGREQUEST']._serialized_start = 498
    _globals['_GETCHANGELOGREQUEST']._serialized_end = 578
    _globals['_CHANGELOG']._serialized_start = 581
    _globals['_CHANGELOG']._serialized_end = 889
    _globals['_CHANGELOGS']._serialized_start = 892
    _globals['_CHANGELOGS']._serialized_end = 1441