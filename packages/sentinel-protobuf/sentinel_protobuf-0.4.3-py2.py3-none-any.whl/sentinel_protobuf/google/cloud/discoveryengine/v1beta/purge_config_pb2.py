"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/purge_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1beta import import_config_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1beta_dot_import__config__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/discoveryengine/v1beta/purge_config.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a7google/cloud/discoveryengine/v1beta/import_config.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"~\n\x16PurgeUserEventsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12\r\n\x05force\x18\x03 \x01(\x08".\n\x17PurgeUserEventsResponse\x12\x13\n\x0bpurge_count\x18\x01 \x01(\x03"\xa9\x01\n\x17PurgeUserEventsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03"7\n\x10PurgeErrorConfig\x12\x14\n\ngcs_prefix\x18\x01 \x01(\tH\x00B\r\n\x0bdestination"\xcd\x03\n\x15PurgeDocumentsRequest\x12D\n\ngcs_source\x18\x05 \x01(\x0b2..google.cloud.discoveryengine.v1beta.GcsSourceH\x00\x12`\n\rinline_source\x18\x06 \x01(\x0b2G.google.cloud.discoveryengine.v1beta.PurgeDocumentsRequest.InlineSourceH\x00\x12=\n\x06parent\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%discoveryengine.googleapis.com/Branch\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x12K\n\x0cerror_config\x18\x07 \x01(\x0b25.google.cloud.discoveryengine.v1beta.PurgeErrorConfig\x12\r\n\x05force\x18\x03 \x01(\x08\x1aR\n\x0cInlineSource\x12B\n\tdocuments\x18\x01 \x03(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/DocumentB\x08\n\x06source"q\n\x16PurgeDocumentsResponse\x12\x13\n\x0bpurge_count\x18\x01 \x01(\x03\x12B\n\x0cpurge_sample\x18\x02 \x03(\tB,\xfaA)\n\'discoveryengine.googleapis.com/Document"\xbf\x01\n\x16PurgeDocumentsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x15\n\rsuccess_count\x18\x03 \x01(\x03\x12\x15\n\rfailure_count\x18\x04 \x01(\x03\x12\x15\n\rignored_count\x18\x05 \x01(\x03"i\n%PurgeSuggestionDenyListEntriesRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"h\n&PurgeSuggestionDenyListEntriesResponse\x12\x13\n\x0bpurge_count\x18\x01 \x01(\x03\x12)\n\rerror_samples\x18\x02 \x03(\x0b2\x12.google.rpc.Status"\x8a\x01\n&PurgeSuggestionDenyListEntriesMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"e\n!PurgeCompletionSuggestionsRequest\x12@\n\x06parent\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore"h\n"PurgeCompletionSuggestionsResponse\x12\x17\n\x0fpurge_succeeded\x18\x01 \x01(\x08\x12)\n\rerror_samples\x18\x02 \x03(\x0b2\x12.google.rpc.Status"\x86\x01\n"PurgeCompletionSuggestionsMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x97\x02\n\'com.google.cloud.discoveryengine.v1betaB\x10PurgeConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.purge_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x10PurgeConfigProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PURGEUSEREVENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PURGEDOCUMENTSREQUEST_INLINESOURCE'].fields_by_name['documents']._loaded_options = None
    _globals['_PURGEDOCUMENTSREQUEST_INLINESOURCE'].fields_by_name['documents']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_PURGEDOCUMENTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGEDOCUMENTSREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA'\n%discoveryengine.googleapis.com/Branch"
    _globals['_PURGEDOCUMENTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_PURGEDOCUMENTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_PURGEDOCUMENTSRESPONSE'].fields_by_name['purge_sample']._loaded_options = None
    _globals['_PURGEDOCUMENTSRESPONSE'].fields_by_name['purge_sample']._serialized_options = b"\xfaA)\n'discoveryengine.googleapis.com/Document"
    _globals['_PURGESUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGESUGGESTIONDENYLISTENTRIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_PURGECOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_PURGECOMPLETIONSUGGESTIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA*\n(discoveryengine.googleapis.com/DataStore'
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_start = 270
    _globals['_PURGEUSEREVENTSREQUEST']._serialized_end = 396
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_start = 398
    _globals['_PURGEUSEREVENTSRESPONSE']._serialized_end = 444
    _globals['_PURGEUSEREVENTSMETADATA']._serialized_start = 447
    _globals['_PURGEUSEREVENTSMETADATA']._serialized_end = 616
    _globals['_PURGEERRORCONFIG']._serialized_start = 618
    _globals['_PURGEERRORCONFIG']._serialized_end = 673
    _globals['_PURGEDOCUMENTSREQUEST']._serialized_start = 676
    _globals['_PURGEDOCUMENTSREQUEST']._serialized_end = 1137
    _globals['_PURGEDOCUMENTSREQUEST_INLINESOURCE']._serialized_start = 1045
    _globals['_PURGEDOCUMENTSREQUEST_INLINESOURCE']._serialized_end = 1127
    _globals['_PURGEDOCUMENTSRESPONSE']._serialized_start = 1139
    _globals['_PURGEDOCUMENTSRESPONSE']._serialized_end = 1252
    _globals['_PURGEDOCUMENTSMETADATA']._serialized_start = 1255
    _globals['_PURGEDOCUMENTSMETADATA']._serialized_end = 1446
    _globals['_PURGESUGGESTIONDENYLISTENTRIESREQUEST']._serialized_start = 1448
    _globals['_PURGESUGGESTIONDENYLISTENTRIESREQUEST']._serialized_end = 1553
    _globals['_PURGESUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_start = 1555
    _globals['_PURGESUGGESTIONDENYLISTENTRIESRESPONSE']._serialized_end = 1659
    _globals['_PURGESUGGESTIONDENYLISTENTRIESMETADATA']._serialized_start = 1662
    _globals['_PURGESUGGESTIONDENYLISTENTRIESMETADATA']._serialized_end = 1800
    _globals['_PURGECOMPLETIONSUGGESTIONSREQUEST']._serialized_start = 1802
    _globals['_PURGECOMPLETIONSUGGESTIONSREQUEST']._serialized_end = 1903
    _globals['_PURGECOMPLETIONSUGGESTIONSRESPONSE']._serialized_start = 1905
    _globals['_PURGECOMPLETIONSUGGESTIONSRESPONSE']._serialized_end = 2009
    _globals['_PURGECOMPLETIONSUGGESTIONSMETADATA']._serialized_start = 2012
    _globals['_PURGECOMPLETIONSUGGESTIONSMETADATA']._serialized_end = 2146