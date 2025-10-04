"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1alpha/data_agent.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.geminidataanalytics.v1alpha import data_analytics_agent_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1alpha_dot_data__analytics__agent__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/geminidataanalytics/v1alpha/data_agent.proto\x12(google.cloud.geminidataanalytics.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aCgoogle/cloud/geminidataanalytics/v1alpha/data_analytics_agent.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa5\x05\n\tDataAgent\x12\\\n\x14data_analytics_agent\x18e \x01(\x0b2<.google.cloud.geminidataanalytics.v1alpha.DataAnalyticsAgentH\x00\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x01\xe0A\x08\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x12T\n\x06labels\x18\x05 \x03(\x0b2?.google.cloud.geminidataanalytics.v1alpha.DataAgent.LabelsEntryB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bdelete_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\npurge_time\x18\r \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x8a\x01\xeaA\x86\x01\n,geminidataanalytics.googleapis.com/DataAgent\x12?projects/{project}/locations/{location}/dataAgents/{data_agent}*\ndataAgents2\tdataAgentB\x06\n\x04typeB\xa4\x02\n,com.google.cloud.geminidataanalytics.v1alphaB\x0eDataAgentProtoP\x01Z^cloud.google.com/go/geminidataanalytics/apiv1alpha/geminidataanalyticspb;geminidataanalyticspb\xaa\x02(Google.Cloud.GeminiDataAnalytics.V1Alpha\xca\x02(Google\\Cloud\\GeminiDataAnalytics\\V1alpha\xea\x02+Google::Cloud::GeminiDataAnalytics::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1alpha.data_agent_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.cloud.geminidataanalytics.v1alphaB\x0eDataAgentProtoP\x01Z^cloud.google.com/go/geminidataanalytics/apiv1alpha/geminidataanalyticspb;geminidataanalyticspb\xaa\x02(Google.Cloud.GeminiDataAnalytics.V1Alpha\xca\x02(Google\\Cloud\\GeminiDataAnalytics\\V1alpha\xea\x02+Google::Cloud::GeminiDataAnalytics::V1alpha'
    _globals['_DATAAGENT_LABELSENTRY']._loaded_options = None
    _globals['_DATAAGENT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATAAGENT'].fields_by_name['name']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['name']._serialized_options = b'\xe0A\x01\xe0A\x08'
    _globals['_DATAAGENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_DATAAGENT'].fields_by_name['description']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DATAAGENT'].fields_by_name['labels']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_DATAAGENT'].fields_by_name['create_time']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAAGENT'].fields_by_name['update_time']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAAGENT'].fields_by_name['delete_time']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['delete_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAAGENT'].fields_by_name['purge_time']._loaded_options = None
    _globals['_DATAAGENT'].fields_by_name['purge_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATAAGENT']._loaded_options = None
    _globals['_DATAAGENT']._serialized_options = b'\xeaA\x86\x01\n,geminidataanalytics.googleapis.com/DataAgent\x12?projects/{project}/locations/{location}/dataAgents/{data_agent}*\ndataAgents2\tdataAgent'
    _globals['_DATAAGENT']._serialized_start = 266
    _globals['_DATAAGENT']._serialized_end = 943
    _globals['_DATAAGENT_LABELSENTRY']._serialized_start = 749
    _globals['_DATAAGENT_LABELSENTRY']._serialized_end = 794