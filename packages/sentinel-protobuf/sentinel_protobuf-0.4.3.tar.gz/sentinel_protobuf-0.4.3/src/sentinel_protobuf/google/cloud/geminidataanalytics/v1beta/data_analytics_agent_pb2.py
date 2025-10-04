"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/data_analytics_agent.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.geminidataanalytics.v1beta import context_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_context__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/cloud/geminidataanalytics/v1beta/data_analytics_agent.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a5google/cloud/geminidataanalytics/v1beta/context.proto"\x8d\x02\n\x12DataAnalyticsAgent\x12N\n\x0fstaging_context\x18\x05 \x01(\x0b20.google.cloud.geminidataanalytics.v1beta.ContextB\x03\xe0A\x01\x12P\n\x11published_context\x18\x06 \x01(\x0b20.google.cloud.geminidataanalytics.v1beta.ContextB\x03\xe0A\x01\x12U\n\x16last_published_context\x18\x07 \x01(\x0b20.google.cloud.geminidataanalytics.v1beta.ContextB\x03\xe0A\x03B\xa8\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x17DataAnalyticsAgentProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.data_analytics_agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x17DataAnalyticsAgentProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_DATAANALYTICSAGENT'].fields_by_name['staging_context']._loaded_options = None
    _globals['_DATAANALYTICSAGENT'].fields_by_name['staging_context']._serialized_options = b'\xe0A\x01'
    _globals['_DATAANALYTICSAGENT'].fields_by_name['published_context']._loaded_options = None
    _globals['_DATAANALYTICSAGENT'].fields_by_name['published_context']._serialized_options = b'\xe0A\x01'
    _globals['_DATAANALYTICSAGENT'].fields_by_name['last_published_context']._loaded_options = None
    _globals['_DATAANALYTICSAGENT'].fields_by_name['last_published_context']._serialized_options = b'\xe0A\x03'
    _globals['_DATAANALYTICSAGENT']._serialized_start = 200
    _globals['_DATAANALYTICSAGENT']._serialized_end = 469