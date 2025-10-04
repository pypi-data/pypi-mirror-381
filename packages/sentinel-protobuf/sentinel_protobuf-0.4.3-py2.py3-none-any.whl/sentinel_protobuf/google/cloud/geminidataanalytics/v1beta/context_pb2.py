"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/context.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.geminidataanalytics.v1beta import datasource_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_datasource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/cloud/geminidataanalytics/v1beta/context.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a8google/cloud/geminidataanalytics/v1beta/datasource.proto"\xb6\x02\n\x07Context\x12\x1f\n\x12system_instruction\x18\x01 \x01(\tB\x03\xe0A\x01\x12a\n\x15datasource_references\x18\x07 \x01(\x0b2=.google.cloud.geminidataanalytics.v1beta.DatasourceReferencesB\x03\xe0A\x02\x12R\n\x07options\x18\x03 \x01(\x0b2<.google.cloud.geminidataanalytics.v1beta.ConversationOptionsB\x03\xe0A\x01\x12S\n\x0fexample_queries\x18\x05 \x03(\x0b25.google.cloud.geminidataanalytics.v1beta.ExampleQueryB\x03\xe0A\x01"Y\n\x0cExampleQuery\x12\x18\n\tsql_query\x18e \x01(\tB\x03\xe0A\x01H\x00\x12&\n\x19natural_language_question\x18\x01 \x01(\tB\x03\xe0A\x01B\x07\n\x05query"\xb1\x01\n\x13ConversationOptions\x12I\n\x05chart\x18\x01 \x01(\x0b25.google.cloud.geminidataanalytics.v1beta.ChartOptionsB\x03\xe0A\x01\x12O\n\x08analysis\x18\x02 \x01(\x0b28.google.cloud.geminidataanalytics.v1beta.AnalysisOptionsB\x03\xe0A\x01"\xd6\x02\n\x0cChartOptions\x12V\n\x05image\x18\x01 \x01(\x0b2B.google.cloud.geminidataanalytics.v1beta.ChartOptions.ImageOptionsB\x03\xe0A\x01\x1a\xed\x01\n\x0cImageOptions\x12^\n\x08no_image\x18\x01 \x01(\x0b2J.google.cloud.geminidataanalytics.v1beta.ChartOptions.ImageOptions.NoImageH\x00\x12\\\n\x03svg\x18\x02 \x01(\x0b2M.google.cloud.geminidataanalytics.v1beta.ChartOptions.ImageOptions.SvgOptionsH\x00\x1a\t\n\x07NoImage\x1a\x0c\n\nSvgOptionsB\x06\n\x04kind"\x87\x01\n\x0fAnalysisOptions\x12T\n\x06python\x18\x01 \x01(\x0b2?.google.cloud.geminidataanalytics.v1beta.AnalysisOptions.PythonB\x03\xe0A\x01\x1a\x1e\n\x06Python\x12\x14\n\x07enabled\x18\x01 \x01(\x08B\x03\xe0A\x01B\x9d\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x0cContextProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x0cContextProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_CONTEXT'].fields_by_name['system_instruction']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['system_instruction']._serialized_options = b'\xe0A\x01'
    _globals['_CONTEXT'].fields_by_name['datasource_references']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['datasource_references']._serialized_options = b'\xe0A\x02'
    _globals['_CONTEXT'].fields_by_name['options']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['options']._serialized_options = b'\xe0A\x01'
    _globals['_CONTEXT'].fields_by_name['example_queries']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['example_queries']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLEQUERY'].fields_by_name['sql_query']._loaded_options = None
    _globals['_EXAMPLEQUERY'].fields_by_name['sql_query']._serialized_options = b'\xe0A\x01'
    _globals['_EXAMPLEQUERY'].fields_by_name['natural_language_question']._loaded_options = None
    _globals['_EXAMPLEQUERY'].fields_by_name['natural_language_question']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONOPTIONS'].fields_by_name['chart']._loaded_options = None
    _globals['_CONVERSATIONOPTIONS'].fields_by_name['chart']._serialized_options = b'\xe0A\x01'
    _globals['_CONVERSATIONOPTIONS'].fields_by_name['analysis']._loaded_options = None
    _globals['_CONVERSATIONOPTIONS'].fields_by_name['analysis']._serialized_options = b'\xe0A\x01'
    _globals['_CHARTOPTIONS'].fields_by_name['image']._loaded_options = None
    _globals['_CHARTOPTIONS'].fields_by_name['image']._serialized_options = b'\xe0A\x01'
    _globals['_ANALYSISOPTIONS_PYTHON'].fields_by_name['enabled']._loaded_options = None
    _globals['_ANALYSISOPTIONS_PYTHON'].fields_by_name['enabled']._serialized_options = b'\xe0A\x01'
    _globals['_ANALYSISOPTIONS'].fields_by_name['python']._loaded_options = None
    _globals['_ANALYSISOPTIONS'].fields_by_name['python']._serialized_options = b'\xe0A\x01'
    _globals['_CONTEXT']._serialized_start = 190
    _globals['_CONTEXT']._serialized_end = 500
    _globals['_EXAMPLEQUERY']._serialized_start = 502
    _globals['_EXAMPLEQUERY']._serialized_end = 591
    _globals['_CONVERSATIONOPTIONS']._serialized_start = 594
    _globals['_CONVERSATIONOPTIONS']._serialized_end = 771
    _globals['_CHARTOPTIONS']._serialized_start = 774
    _globals['_CHARTOPTIONS']._serialized_end = 1116
    _globals['_CHARTOPTIONS_IMAGEOPTIONS']._serialized_start = 879
    _globals['_CHARTOPTIONS_IMAGEOPTIONS']._serialized_end = 1116
    _globals['_CHARTOPTIONS_IMAGEOPTIONS_NOIMAGE']._serialized_start = 1085
    _globals['_CHARTOPTIONS_IMAGEOPTIONS_NOIMAGE']._serialized_end = 1094
    _globals['_CHARTOPTIONS_IMAGEOPTIONS_SVGOPTIONS']._serialized_start = 1096
    _globals['_CHARTOPTIONS_IMAGEOPTIONS_SVGOPTIONS']._serialized_end = 1108
    _globals['_ANALYSISOPTIONS']._serialized_start = 1119
    _globals['_ANALYSISOPTIONS']._serialized_end = 1254
    _globals['_ANALYSISOPTIONS_PYTHON']._serialized_start = 1224
    _globals['_ANALYSISOPTIONS_PYTHON']._serialized_end = 1254