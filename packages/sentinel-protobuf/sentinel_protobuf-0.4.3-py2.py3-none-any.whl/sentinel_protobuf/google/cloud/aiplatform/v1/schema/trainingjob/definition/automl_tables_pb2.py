"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/schema/trainingjob/definition/automl_tables.proto')
_sym_db = _symbol_database.Default()
from ........google.cloud.aiplatform.v1.schema.trainingjob.definition import export_evaluated_data_items_config_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_schema_dot_trainingjob_dot_definition_dot_export__evaluated__data__items__config__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nLgoogle/cloud/aiplatform/v1/schema/trainingjob/definition/automl_tables.proto\x128google.cloud.aiplatform.v1.schema.trainingjob.definition\x1aagoogle/cloud/aiplatform/v1/schema/trainingjob/definition/export_evaluated_data_items_config.proto"\xce\x01\n\x0cAutoMlTables\x12\\\n\x06inputs\x18\x01 \x01(\x0b2L.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs\x12`\n\x08metadata\x18\x02 \x01(\x0b2N.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesMetadata"\xf4\x11\n\x12AutoMlTablesInputs\x12-\n#optimization_objective_recall_value\x18\x05 \x01(\x02H\x00\x120\n&optimization_objective_precision_value\x18\x06 \x01(\x02H\x00\x12\x17\n\x0fprediction_type\x18\x01 \x01(\t\x12\x15\n\rtarget_column\x18\x02 \x01(\t\x12t\n\x0ftransformations\x18\x03 \x03(\x0b2[.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation\x12\x1e\n\x16optimization_objective\x18\x04 \x01(\t\x12%\n\x1dtrain_budget_milli_node_hours\x18\x07 \x01(\x03\x12\x1e\n\x16disable_early_stopping\x18\x08 \x01(\x08\x12\x1a\n\x12weight_column_name\x18\t \x01(\t\x12\x84\x01\n"export_evaluated_data_items_config\x18\n \x01(\x0b2X.google.cloud.aiplatform.v1.schema.trainingjob.definition.ExportEvaluatedDataItemsConfig\x12\x1e\n\x16additional_experiments\x18\x0b \x03(\t\x1a\x80\r\n\x0eTransformation\x12~\n\x04auto\x18\x01 \x01(\x0b2n.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.AutoTransformationH\x00\x12\x84\x01\n\x07numeric\x18\x02 \x01(\x0b2q.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.NumericTransformationH\x00\x12\x8c\x01\n\x0bcategorical\x18\x03 \x01(\x0b2u.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.CategoricalTransformationH\x00\x12\x88\x01\n\ttimestamp\x18\x04 \x01(\x0b2s.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.TimestampTransformationH\x00\x12~\n\x04text\x18\x05 \x01(\x0b2n.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.TextTransformationH\x00\x12\x92\x01\n\x10repeated_numeric\x18\x06 \x01(\x0b2v.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.NumericArrayTransformationH\x00\x12\x9a\x01\n\x14repeated_categorical\x18\x07 \x01(\x0b2z.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.CategoricalArrayTransformationH\x00\x12\x8c\x01\n\rrepeated_text\x18\x08 \x01(\x0b2s.google.cloud.aiplatform.v1.schema.trainingjob.definition.AutoMlTablesInputs.Transformation.TextArrayTransformationH\x00\x1a)\n\x12AutoTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x1aL\n\x15NumericTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x12\x1e\n\x16invalid_values_allowed\x18\x02 \x01(\x08\x1a0\n\x19CategoricalTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x1ac\n\x17TimestampTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x12\x13\n\x0btime_format\x18\x02 \x01(\t\x12\x1e\n\x16invalid_values_allowed\x18\x03 \x01(\x08\x1a)\n\x12TextTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x1aQ\n\x1aNumericArrayTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x12\x1e\n\x16invalid_values_allowed\x18\x02 \x01(\x08\x1a5\n\x1eCategoricalArrayTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\t\x1a.\n\x17TextArrayTransformation\x12\x13\n\x0bcolumn_name\x18\x01 \x01(\tB\x17\n\x15transformation_detailB*\n(additional_optimization_objective_config";\n\x14AutoMlTablesMetadata\x12#\n\x1btrain_cost_milli_node_hours\x18\x01 \x01(\x03B\xe8\x02\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x11AutoMLTablesProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definitionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.schema.trainingjob.definition.automl_tables_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n<com.google.cloud.aiplatform.v1.schema.trainingjob.definitionB\x11AutoMLTablesProtoP\x01Z\\cloud.google.com/go/aiplatform/apiv1/schema/trainingjob/definition/definitionpb;definitionpb\xaa\x028Google.Cloud.AIPlatform.V1.Schema.TrainingJob.Definition\xca\x028Google\\Cloud\\AIPlatform\\V1\\Schema\\TrainingJob\\Definition\xea\x02>Google::Cloud::AIPlatform::V1::Schema::TrainingJob::Definition'
    _globals['_AUTOMLTABLES']._serialized_start = 238
    _globals['_AUTOMLTABLES']._serialized_end = 444
    _globals['_AUTOMLTABLESINPUTS']._serialized_start = 447
    _globals['_AUTOMLTABLESINPUTS']._serialized_end = 2739
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION']._serialized_start = 1031
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION']._serialized_end = 2695
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_AUTOTRANSFORMATION']._serialized_start = 2171
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_AUTOTRANSFORMATION']._serialized_end = 2212
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_NUMERICTRANSFORMATION']._serialized_start = 2214
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_NUMERICTRANSFORMATION']._serialized_end = 2290
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_CATEGORICALTRANSFORMATION']._serialized_start = 2292
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_CATEGORICALTRANSFORMATION']._serialized_end = 2340
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TIMESTAMPTRANSFORMATION']._serialized_start = 2342
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TIMESTAMPTRANSFORMATION']._serialized_end = 2441
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TEXTTRANSFORMATION']._serialized_start = 2443
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TEXTTRANSFORMATION']._serialized_end = 2484
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_NUMERICARRAYTRANSFORMATION']._serialized_start = 2486
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_NUMERICARRAYTRANSFORMATION']._serialized_end = 2567
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_CATEGORICALARRAYTRANSFORMATION']._serialized_start = 2569
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_CATEGORICALARRAYTRANSFORMATION']._serialized_end = 2622
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TEXTARRAYTRANSFORMATION']._serialized_start = 2624
    _globals['_AUTOMLTABLESINPUTS_TRANSFORMATION_TEXTARRAYTRANSFORMATION']._serialized_end = 2670
    _globals['_AUTOMLTABLESMETADATA']._serialized_start = 2741
    _globals['_AUTOMLTABLESMETADATA']._serialized_end = 2800