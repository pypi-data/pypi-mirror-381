"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1beta/sample_query.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n6google/cloud/discoveryengine/v1beta/sample_query.proto\x12#google.cloud.discoveryengine.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x04\n\x0bSampleQuery\x12R\n\x0bquery_entry\x18\x02 \x01(\x0b2;.google.cloud.discoveryengine.v1beta.SampleQuery.QueryEntryH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\xc0\x01\n\nQueryEntry\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\x07targets\x18\x03 \x03(\x0b2B.google.cloud.discoveryengine.v1beta.SampleQuery.QueryEntry.Target\x1aI\n\x06Target\x12\x0b\n\x03uri\x18\x01 \x01(\t\x12\x14\n\x0cpage_numbers\x18\x02 \x03(\x05\x12\x12\n\x05score\x18\x03 \x01(\x01H\x00\x88\x01\x01B\x08\n\x06_score:\x99\x01\xeaA\x95\x01\n*discoveryengine.googleapis.com/SampleQuery\x12gprojects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}/sampleQueries/{sample_query}B\t\n\x07contentB\x97\x02\n\'com.google.cloud.discoveryengine.v1betaB\x10SampleQueryProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1beta.sample_query_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.cloud.discoveryengine.v1betaB\x10SampleQueryProtoP\x01ZQcloud.google.com/go/discoveryengine/apiv1beta/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02#Google.Cloud.DiscoveryEngine.V1Beta\xca\x02#Google\\Cloud\\DiscoveryEngine\\V1beta\xea\x02&Google::Cloud::DiscoveryEngine::V1beta"
    _globals['_SAMPLEQUERY_QUERYENTRY'].fields_by_name['query']._loaded_options = None
    _globals['_SAMPLEQUERY_QUERYENTRY'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_SAMPLEQUERY'].fields_by_name['name']._loaded_options = None
    _globals['_SAMPLEQUERY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SAMPLEQUERY'].fields_by_name['create_time']._loaded_options = None
    _globals['_SAMPLEQUERY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_SAMPLEQUERY']._loaded_options = None
    _globals['_SAMPLEQUERY']._serialized_options = b'\xeaA\x95\x01\n*discoveryengine.googleapis.com/SampleQuery\x12gprojects/{project}/locations/{location}/sampleQuerySets/{sample_query_set}/sampleQueries/{sample_query}'
    _globals['_SAMPLEQUERY']._serialized_start = 189
    _globals['_SAMPLEQUERY']._serialized_end = 721
    _globals['_SAMPLEQUERY_QUERYENTRY']._serialized_start = 362
    _globals['_SAMPLEQUERY_QUERYENTRY']._serialized_end = 554
    _globals['_SAMPLEQUERY_QUERYENTRY_TARGET']._serialized_start = 481
    _globals['_SAMPLEQUERY_QUERYENTRY_TARGET']._serialized_end = 554