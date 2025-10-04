"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2beta/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2beta import common_pb2 as google_dot_cloud_dot_retail_dot_v2beta_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/retail/v2beta/model.proto\x12\x1agoogle.cloud.retail.v2beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\'google/cloud/retail/v2beta/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xbc\x0e\n\x05Model\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12L\n\x0etraining_state\x18\x03 \x01(\x0e2/.google.cloud.retail.v2beta.Model.TrainingStateB\x03\xe0A\x01\x12J\n\rserving_state\x18\x04 \x01(\x0e2..google.cloud.retail.v2beta.Model.ServingStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04type\x18\x07 \x01(\tB\x03\xe0A\x02\x12#\n\x16optimization_objective\x18\x08 \x01(\tB\x03\xe0A\x01\x12Y\n\x15periodic_tuning_state\x18\x0b \x01(\x0e25.google.cloud.retail.v2beta.Model.PeriodicTuningStateB\x03\xe0A\x01\x127\n\x0elast_tune_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1d\n\x10tuning_operation\x18\x0f \x01(\tB\x03\xe0A\x03\x12D\n\ndata_state\x18\x10 \x01(\x0e2+.google.cloud.retail.v2beta.Model.DataStateB\x03\xe0A\x03\x12Y\n\x10filtering_option\x18\x12 \x01(\x0e2:.google.cloud.retail.v2beta.RecommendationsFilteringOptionB\x03\xe0A\x01\x12V\n\x14serving_config_lists\x18\x13 \x03(\x0b23.google.cloud.retail.v2beta.Model.ServingConfigListB\x03\xe0A\x03\x12Y\n\x15model_features_config\x18\x16 \x01(\x0b25.google.cloud.retail.v2beta.Model.ModelFeaturesConfigB\x03\xe0A\x01\x1a4\n\x11ServingConfigList\x12\x1f\n\x12serving_config_ids\x18\x01 \x03(\tB\x03\xe0A\x01\x1a\x83\x01\n&FrequentlyBoughtTogetherFeaturesConfig\x12Y\n\x15context_products_type\x18\x02 \x01(\x0e25.google.cloud.retail.v2beta.Model.ContextProductsTypeB\x03\xe0A\x01\x1a\xa5\x01\n\x13ModelFeaturesConfig\x12u\n!frequently_bought_together_config\x18\x01 \x01(\x0b2H.google.cloud.retail.v2beta.Model.FrequentlyBoughtTogetherFeaturesConfigH\x00B\x17\n\x15type_dedicated_config"R\n\x0cServingState\x12\x1d\n\x19SERVING_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\t\n\x05TUNED\x10\x03"I\n\rTrainingState\x12\x1e\n\x1aTRAINING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0c\n\x08TRAINING\x10\x02"\x90\x01\n\x13PeriodicTuningState\x12%\n!PERIODIC_TUNING_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERIODIC_TUNING_DISABLED\x10\x01\x12\x17\n\x13ALL_TUNING_DISABLED\x10\x03\x12\x1b\n\x17PERIODIC_TUNING_ENABLED\x10\x02"D\n\tDataState\x12\x1a\n\x16DATA_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DATA_OK\x10\x01\x12\x0e\n\nDATA_ERROR\x10\x02"w\n\x13ContextProductsType\x12%\n!CONTEXT_PRODUCTS_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SINGLE_CONTEXT_PRODUCT\x10\x01\x12\x1d\n\x19MULTIPLE_CONTEXT_PRODUCTS\x10\x02:k\xeaAh\n\x1bretail.googleapis.com/Model\x12Iprojects/{project}/locations/{location}/catalogs/{catalog}/models/{model}B\xc9\x01\n\x1ecom.google.cloud.retail.v2betaB\nModelProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2betab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2beta.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.retail.v2betaB\nModelProtoP\x01Z6cloud.google.com/go/retail/apiv2beta/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1aGoogle.Cloud.Retail.V2Beta\xca\x02\x1aGoogle\\Cloud\\Retail\\V2beta\xea\x02\x1dGoogle::Cloud::Retail::V2beta'
    _globals['_MODEL_SERVINGCONFIGLIST'].fields_by_name['serving_config_ids']._loaded_options = None
    _globals['_MODEL_SERVINGCONFIGLIST'].fields_by_name['serving_config_ids']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG'].fields_by_name['context_products_type']._loaded_options = None
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG'].fields_by_name['context_products_type']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['name']._loaded_options = None
    _globals['_MODEL'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['display_name']._loaded_options = None
    _globals['_MODEL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['training_state']._loaded_options = None
    _globals['_MODEL'].fields_by_name['training_state']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['serving_state']._loaded_options = None
    _globals['_MODEL'].fields_by_name['serving_state']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['type']._loaded_options = None
    _globals['_MODEL'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL'].fields_by_name['optimization_objective']._loaded_options = None
    _globals['_MODEL'].fields_by_name['optimization_objective']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['periodic_tuning_state']._loaded_options = None
    _globals['_MODEL'].fields_by_name['periodic_tuning_state']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['last_tune_time']._loaded_options = None
    _globals['_MODEL'].fields_by_name['last_tune_time']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['tuning_operation']._loaded_options = None
    _globals['_MODEL'].fields_by_name['tuning_operation']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['data_state']._loaded_options = None
    _globals['_MODEL'].fields_by_name['data_state']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['filtering_option']._loaded_options = None
    _globals['_MODEL'].fields_by_name['filtering_option']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['serving_config_lists']._loaded_options = None
    _globals['_MODEL'].fields_by_name['serving_config_lists']._serialized_options = b'\xe0A\x03'
    _globals['_MODEL'].fields_by_name['model_features_config']._loaded_options = None
    _globals['_MODEL'].fields_by_name['model_features_config']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAh\n\x1bretail.googleapis.com/Model\x12Iprojects/{project}/locations/{location}/catalogs/{catalog}/models/{model}'
    _globals['_MODEL']._serialized_start = 205
    _globals['_MODEL']._serialized_end = 2057
    _globals['_MODEL_SERVINGCONFIGLIST']._serialized_start = 1097
    _globals['_MODEL_SERVINGCONFIGLIST']._serialized_end = 1149
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG']._serialized_start = 1152
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG']._serialized_end = 1283
    _globals['_MODEL_MODELFEATURESCONFIG']._serialized_start = 1286
    _globals['_MODEL_MODELFEATURESCONFIG']._serialized_end = 1451
    _globals['_MODEL_SERVINGSTATE']._serialized_start = 1453
    _globals['_MODEL_SERVINGSTATE']._serialized_end = 1535
    _globals['_MODEL_TRAININGSTATE']._serialized_start = 1537
    _globals['_MODEL_TRAININGSTATE']._serialized_end = 1610
    _globals['_MODEL_PERIODICTUNINGSTATE']._serialized_start = 1613
    _globals['_MODEL_PERIODICTUNINGSTATE']._serialized_end = 1757
    _globals['_MODEL_DATASTATE']._serialized_start = 1759
    _globals['_MODEL_DATASTATE']._serialized_end = 1827
    _globals['_MODEL_CONTEXTPRODUCTSTYPE']._serialized_start = 1829
    _globals['_MODEL_CONTEXTPRODUCTSTYPE']._serialized_end = 1948