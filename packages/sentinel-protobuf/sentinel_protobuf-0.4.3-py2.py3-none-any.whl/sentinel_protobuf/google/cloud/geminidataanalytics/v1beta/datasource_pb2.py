"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/geminidataanalytics/v1beta/datasource.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.geminidataanalytics.v1beta import credentials_pb2 as google_dot_cloud_dot_geminidataanalytics_dot_v1beta_dot_credentials__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/cloud/geminidataanalytics/v1beta/datasource.proto\x12\'google.cloud.geminidataanalytics.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a9google/cloud/geminidataanalytics/v1beta/credentials.proto"\x9f\x02\n\x14DatasourceReferences\x12N\n\x02bq\x18\x01 \x01(\x0b2@.google.cloud.geminidataanalytics.v1beta.BigQueryTableReferencesH\x00\x12U\n\x06studio\x18\x02 \x01(\x0b2C.google.cloud.geminidataanalytics.v1beta.StudioDatasourceReferencesH\x00\x12R\n\x06looker\x18\x03 \x01(\x0b2@.google.cloud.geminidataanalytics.v1beta.LookerExploreReferencesH\x00B\x0c\n\nreferences"y\n\x17BigQueryTableReferences\x12^\n\x10table_references\x18\x01 \x03(\x0b2?.google.cloud.geminidataanalytics.v1beta.BigQueryTableReferenceB\x03\xe0A\x02"\xa7\x01\n\x16BigQueryTableReference\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x03 \x01(\tB\x03\xe0A\x02\x12\x15\n\x08table_id\x18\x04 \x01(\tB\x03\xe0A\x02\x12D\n\x06schema\x18\x06 \x01(\x0b2/.google.cloud.geminidataanalytics.v1beta.SchemaB\x03\xe0A\x01"{\n\x1aStudioDatasourceReferences\x12]\n\x11studio_references\x18\x02 \x03(\x0b2B.google.cloud.geminidataanalytics.v1beta.StudioDatasourceReference"7\n\x19StudioDatasourceReference\x12\x1a\n\rdatasource_id\x18\x01 \x01(\tB\x03\xe0A\x02"\xcb\x01\n\x17LookerExploreReferences\x12`\n\x12explore_references\x18\x01 \x03(\x0b2?.google.cloud.geminidataanalytics.v1beta.LookerExploreReferenceB\x03\xe0A\x02\x12N\n\x0bcredentials\x18\x02 \x01(\x0b24.google.cloud.geminidataanalytics.v1beta.CredentialsB\x03\xe0A\x01"\xa6\x02\n\x16LookerExploreReference\x12\x1d\n\x13looker_instance_uri\x18\t \x01(\tH\x00\x12j\n\x1cprivate_looker_instance_info\x18\n \x01(\x0b2B.google.cloud.geminidataanalytics.v1beta.PrivateLookerInstanceInfoH\x00\x12\x19\n\x0clookml_model\x18\x04 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07explore\x18\x05 \x01(\tB\x03\xe0A\x02\x12D\n\x06schema\x18\x08 \x01(\x0b2/.google.cloud.geminidataanalytics.v1beta.SchemaB\x03\xe0A\x01B\n\n\x08instance"W\n\x19PrivateLookerInstanceInfo\x12\x1a\n\x12looker_instance_id\x18\x01 \x01(\t\x12\x1e\n\x16service_directory_name\x18\x02 \x01(\t"\xc9\x02\n\nDatasource\x12c\n\x18bigquery_table_reference\x18\x01 \x01(\x0b2?.google.cloud.geminidataanalytics.v1beta.BigQueryTableReferenceH\x00\x12\x1e\n\x14studio_datasource_id\x18\x02 \x01(\tH\x00\x12c\n\x18looker_explore_reference\x18\x04 \x01(\x0b2?.google.cloud.geminidataanalytics.v1beta.LookerExploreReferenceH\x00\x12D\n\x06schema\x18\x07 \x01(\x0b2/.google.cloud.geminidataanalytics.v1beta.SchemaB\x03\xe0A\x01B\x0b\n\treference"\xf7\x01\n\x06Schema\x12C\n\x06fields\x18\x01 \x03(\x0b2..google.cloud.geminidataanalytics.v1beta.FieldB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08synonyms\x18\x03 \x03(\tB\x03\xe0A\x01\x12\x11\n\x04tags\x18\x04 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12I\n\x07filters\x18\x06 \x03(\x0b23.google.cloud.geminidataanalytics.v1beta.DataFilterB\x03\xe0A\x01"\x99\x02\n\x05Field\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04type\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04mode\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08synonyms\x18\x06 \x03(\tB\x03\xe0A\x01\x12\x11\n\x04tags\x18\x07 \x03(\tB\x03\xe0A\x01\x12\x19\n\x0cdisplay_name\x18\x08 \x01(\tB\x03\xe0A\x01\x12F\n\tsubfields\x18\t \x03(\x0b2..google.cloud.geminidataanalytics.v1beta.FieldB\x03\xe0A\x01\x12\x15\n\x08category\x18\n \x01(\tB\x03\xe0A\x01\x12\x19\n\x0cvalue_format\x18\x0b \x01(\tB\x03\xe0A\x01"\x80\x01\n\nDataFilter\x12\x12\n\x05field\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05value\x18\x02 \x01(\tB\x03\xe0A\x01\x12J\n\x04type\x18\x03 \x01(\x0e27.google.cloud.geminidataanalytics.v1beta.DataFilterTypeB\x03\xe0A\x01*E\n\x0eDataFilterType\x12 \n\x1cDATA_FILTER_TYPE_UNSPECIFIED\x10\x00\x12\x11\n\rALWAYS_FILTER\x10\x01B\xa0\x02\n+com.google.cloud.geminidataanalytics.v1betaB\x0fDatasourceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02\'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02\'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.geminidataanalytics.v1beta.datasource_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n+com.google.cloud.geminidataanalytics.v1betaB\x0fDatasourceProtoP\x01Z]cloud.google.com/go/geminidataanalytics/apiv1beta/geminidataanalyticspb;geminidataanalyticspb\xaa\x02'Google.Cloud.GeminiDataAnalytics.V1Beta\xca\x02'Google\\Cloud\\GeminiDataAnalytics\\V1beta\xea\x02*Google::Cloud::GeminiDataAnalytics::V1beta"
    _globals['_BIGQUERYTABLEREFERENCES'].fields_by_name['table_references']._loaded_options = None
    _globals['_BIGQUERYTABLEREFERENCES'].fields_by_name['table_references']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['project_id']._loaded_options = None
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['table_id']._loaded_options = None
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['table_id']._serialized_options = b'\xe0A\x02'
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['schema']._loaded_options = None
    _globals['_BIGQUERYTABLEREFERENCE'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_STUDIODATASOURCEREFERENCE'].fields_by_name['datasource_id']._loaded_options = None
    _globals['_STUDIODATASOURCEREFERENCE'].fields_by_name['datasource_id']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKEREXPLOREREFERENCES'].fields_by_name['explore_references']._loaded_options = None
    _globals['_LOOKEREXPLOREREFERENCES'].fields_by_name['explore_references']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKEREXPLOREREFERENCES'].fields_by_name['credentials']._loaded_options = None
    _globals['_LOOKEREXPLOREREFERENCES'].fields_by_name['credentials']._serialized_options = b'\xe0A\x01'
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['lookml_model']._loaded_options = None
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['lookml_model']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['explore']._loaded_options = None
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['explore']._serialized_options = b'\xe0A\x02'
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['schema']._loaded_options = None
    _globals['_LOOKEREXPLOREREFERENCE'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_DATASOURCE'].fields_by_name['schema']._loaded_options = None
    _globals['_DATASOURCE'].fields_by_name['schema']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['fields']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['fields']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['description']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['synonyms']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['synonyms']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['tags']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['display_name']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['filters']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['filters']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['name']._loaded_options = None
    _globals['_FIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['type']._loaded_options = None
    _globals['_FIELD'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['description']._loaded_options = None
    _globals['_FIELD'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['mode']._loaded_options = None
    _globals['_FIELD'].fields_by_name['mode']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['synonyms']._loaded_options = None
    _globals['_FIELD'].fields_by_name['synonyms']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['tags']._loaded_options = None
    _globals['_FIELD'].fields_by_name['tags']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['display_name']._loaded_options = None
    _globals['_FIELD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['subfields']._loaded_options = None
    _globals['_FIELD'].fields_by_name['subfields']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['category']._loaded_options = None
    _globals['_FIELD'].fields_by_name['category']._serialized_options = b'\xe0A\x01'
    _globals['_FIELD'].fields_by_name['value_format']._loaded_options = None
    _globals['_FIELD'].fields_by_name['value_format']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFILTER'].fields_by_name['field']._loaded_options = None
    _globals['_DATAFILTER'].fields_by_name['field']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFILTER'].fields_by_name['value']._loaded_options = None
    _globals['_DATAFILTER'].fields_by_name['value']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFILTER'].fields_by_name['type']._loaded_options = None
    _globals['_DATAFILTER'].fields_by_name['type']._serialized_options = b'\xe0A\x01'
    _globals['_DATAFILTERTYPE']._serialized_start = 2547
    _globals['_DATAFILTERTYPE']._serialized_end = 2616
    _globals['_DATASOURCEREFERENCES']._serialized_start = 194
    _globals['_DATASOURCEREFERENCES']._serialized_end = 481
    _globals['_BIGQUERYTABLEREFERENCES']._serialized_start = 483
    _globals['_BIGQUERYTABLEREFERENCES']._serialized_end = 604
    _globals['_BIGQUERYTABLEREFERENCE']._serialized_start = 607
    _globals['_BIGQUERYTABLEREFERENCE']._serialized_end = 774
    _globals['_STUDIODATASOURCEREFERENCES']._serialized_start = 776
    _globals['_STUDIODATASOURCEREFERENCES']._serialized_end = 899
    _globals['_STUDIODATASOURCEREFERENCE']._serialized_start = 901
    _globals['_STUDIODATASOURCEREFERENCE']._serialized_end = 956
    _globals['_LOOKEREXPLOREREFERENCES']._serialized_start = 959
    _globals['_LOOKEREXPLOREREFERENCES']._serialized_end = 1162
    _globals['_LOOKEREXPLOREREFERENCE']._serialized_start = 1165
    _globals['_LOOKEREXPLOREREFERENCE']._serialized_end = 1459
    _globals['_PRIVATELOOKERINSTANCEINFO']._serialized_start = 1461
    _globals['_PRIVATELOOKERINSTANCEINFO']._serialized_end = 1548
    _globals['_DATASOURCE']._serialized_start = 1551
    _globals['_DATASOURCE']._serialized_end = 1880
    _globals['_SCHEMA']._serialized_start = 1883
    _globals['_SCHEMA']._serialized_end = 2130
    _globals['_FIELD']._serialized_start = 2133
    _globals['_FIELD']._serialized_end = 2414
    _globals['_DATAFILTER']._serialized_start = 2417
    _globals['_DATAFILTER']._serialized_end = 2545