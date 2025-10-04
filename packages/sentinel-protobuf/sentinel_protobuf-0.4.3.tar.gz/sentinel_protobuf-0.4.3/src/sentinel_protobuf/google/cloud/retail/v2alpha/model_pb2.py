"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/retail/v2alpha/model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.retail.v2alpha import common_pb2 as google_dot_cloud_dot_retail_dot_v2alpha_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/retail/v2alpha/model.proto\x12\x1bgoogle.cloud.retail.v2alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a(google/cloud/retail/v2alpha/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x81\x15\n\x05Model\x12b\n\x18page_optimization_config\x18\x11 \x01(\x0b29.google.cloud.retail.v2alpha.Model.PageOptimizationConfigB\x03\xe0A\x01H\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02\x12M\n\x0etraining_state\x18\x03 \x01(\x0e20.google.cloud.retail.v2alpha.Model.TrainingStateB\x03\xe0A\x01\x12K\n\rserving_state\x18\x04 \x01(\x0e2/.google.cloud.retail.v2alpha.Model.ServingStateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x11\n\x04type\x18\x07 \x01(\tB\x03\xe0A\x02\x12#\n\x16optimization_objective\x18\x08 \x01(\tB\x03\xe0A\x01\x12Z\n\x15periodic_tuning_state\x18\x0b \x01(\x0e26.google.cloud.retail.v2alpha.Model.PeriodicTuningStateB\x03\xe0A\x01\x127\n\x0elast_tune_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x1d\n\x10tuning_operation\x18\x0f \x01(\tB\x03\xe0A\x03\x12E\n\ndata_state\x18\x10 \x01(\x0e2,.google.cloud.retail.v2alpha.Model.DataStateB\x03\xe0A\x03\x12Z\n\x10filtering_option\x18\x12 \x01(\x0e2;.google.cloud.retail.v2alpha.RecommendationsFilteringOptionB\x03\xe0A\x01\x12W\n\x14serving_config_lists\x18\x13 \x03(\x0b24.google.cloud.retail.v2alpha.Model.ServingConfigListB\x03\xe0A\x03\x12Z\n\x15model_features_config\x18\x16 \x01(\x0b26.google.cloud.retail.v2alpha.Model.ModelFeaturesConfigB\x03\xe0A\x01\x1a\xc2\x05\n\x16PageOptimizationConfig\x12)\n\x1cpage_optimization_event_type\x18\x01 \x01(\tB\x03\xe0A\x02\x12T\n\x06panels\x18\x02 \x03(\x0b2?.google.cloud.retail.v2alpha.Model.PageOptimizationConfig.PanelB\x03\xe0A\x02\x12_\n\x0brestriction\x18\x03 \x01(\x0e2E.google.cloud.retail.v2alpha.Model.PageOptimizationConfig.RestrictionB\x03\xe0A\x01\x1a5\n\tCandidate\x12\x1b\n\x11serving_config_id\x18\x01 \x01(\tH\x00B\x0b\n\tcandidate\x1a\xe5\x01\n\x05Panel\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\\\n\ncandidates\x18\x02 \x03(\x0b2C.google.cloud.retail.v2alpha.Model.PageOptimizationConfig.CandidateB\x03\xe0A\x02\x12c\n\x11default_candidate\x18\x03 \x01(\x0b2C.google.cloud.retail.v2alpha.Model.PageOptimizationConfig.CandidateB\x03\xe0A\x02"\xa6\x01\n\x0bRestriction\x12\x1b\n\x17RESTRICTION_UNSPECIFIED\x10\x00\x12\x12\n\x0eNO_RESTRICTION\x10\x01\x12%\n!UNIQUE_SERVING_CONFIG_RESTRICTION\x10\x02\x12\x1c\n\x18UNIQUE_MODEL_RESTRICTION\x10\x03\x12!\n\x1dUNIQUE_MODEL_TYPE_RESTRICTION\x10\x04\x1a4\n\x11ServingConfigList\x12\x1f\n\x12serving_config_ids\x18\x01 \x03(\tB\x03\xe0A\x01\x1a\x84\x01\n&FrequentlyBoughtTogetherFeaturesConfig\x12Z\n\x15context_products_type\x18\x02 \x01(\x0e26.google.cloud.retail.v2alpha.Model.ContextProductsTypeB\x03\xe0A\x01\x1a\xa6\x01\n\x13ModelFeaturesConfig\x12v\n!frequently_bought_together_config\x18\x01 \x01(\x0b2I.google.cloud.retail.v2alpha.Model.FrequentlyBoughtTogetherFeaturesConfigH\x00B\x17\n\x15type_dedicated_config"R\n\x0cServingState\x12\x1d\n\x19SERVING_STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08INACTIVE\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\t\n\x05TUNED\x10\x03"I\n\rTrainingState\x12\x1e\n\x1aTRAINING_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06PAUSED\x10\x01\x12\x0c\n\x08TRAINING\x10\x02"\x90\x01\n\x13PeriodicTuningState\x12%\n!PERIODIC_TUNING_STATE_UNSPECIFIED\x10\x00\x12\x1c\n\x18PERIODIC_TUNING_DISABLED\x10\x01\x12\x17\n\x13ALL_TUNING_DISABLED\x10\x03\x12\x1b\n\x17PERIODIC_TUNING_ENABLED\x10\x02"D\n\tDataState\x12\x1a\n\x16DATA_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07DATA_OK\x10\x01\x12\x0e\n\nDATA_ERROR\x10\x02"w\n\x13ContextProductsType\x12%\n!CONTEXT_PRODUCTS_TYPE_UNSPECIFIED\x10\x00\x12\x1a\n\x16SINGLE_CONTEXT_PRODUCT\x10\x01\x12\x1d\n\x19MULTIPLE_CONTEXT_PRODUCTS\x10\x02:k\xeaAh\n\x1bretail.googleapis.com/Model\x12Iprojects/{project}/locations/{location}/catalogs/{catalog}/models/{model}B\x11\n\x0ftraining_configB\xce\x01\n\x1fcom.google.cloud.retail.v2alphaB\nModelProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.retail.v2alpha.model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.retail.v2alphaB\nModelProtoP\x01Z7cloud.google.com/go/retail/apiv2alpha/retailpb;retailpb\xa2\x02\x06RETAIL\xaa\x02\x1bGoogle.Cloud.Retail.V2Alpha\xca\x02\x1bGoogle\\Cloud\\Retail\\V2alpha\xea\x02\x1eGoogle::Cloud::Retail::V2alpha'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['display_name']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['candidates']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['candidates']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['default_candidate']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL'].fields_by_name['default_candidate']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['page_optimization_event_type']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['page_optimization_event_type']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['panels']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['panels']._serialized_options = b'\xe0A\x02'
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['restriction']._loaded_options = None
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG'].fields_by_name['restriction']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL_SERVINGCONFIGLIST'].fields_by_name['serving_config_ids']._loaded_options = None
    _globals['_MODEL_SERVINGCONFIGLIST'].fields_by_name['serving_config_ids']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG'].fields_by_name['context_products_type']._loaded_options = None
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG'].fields_by_name['context_products_type']._serialized_options = b'\xe0A\x01'
    _globals['_MODEL'].fields_by_name['page_optimization_config']._loaded_options = None
    _globals['_MODEL'].fields_by_name['page_optimization_config']._serialized_options = b'\xe0A\x01'
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
    _globals['_MODEL']._serialized_start = 208
    _globals['_MODEL']._serialized_end = 2897
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG']._serialized_start = 1208
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG']._serialized_end = 1914
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_CANDIDATE']._serialized_start = 1460
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_CANDIDATE']._serialized_end = 1513
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL']._serialized_start = 1516
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_PANEL']._serialized_end = 1745
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_RESTRICTION']._serialized_start = 1748
    _globals['_MODEL_PAGEOPTIMIZATIONCONFIG_RESTRICTION']._serialized_end = 1914
    _globals['_MODEL_SERVINGCONFIGLIST']._serialized_start = 1916
    _globals['_MODEL_SERVINGCONFIGLIST']._serialized_end = 1968
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG']._serialized_start = 1971
    _globals['_MODEL_FREQUENTLYBOUGHTTOGETHERFEATURESCONFIG']._serialized_end = 2103
    _globals['_MODEL_MODELFEATURESCONFIG']._serialized_start = 2106
    _globals['_MODEL_MODELFEATURESCONFIG']._serialized_end = 2272
    _globals['_MODEL_SERVINGSTATE']._serialized_start = 2274
    _globals['_MODEL_SERVINGSTATE']._serialized_end = 2356
    _globals['_MODEL_TRAININGSTATE']._serialized_start = 2358
    _globals['_MODEL_TRAININGSTATE']._serialized_end = 2431
    _globals['_MODEL_PERIODICTUNINGSTATE']._serialized_start = 2434
    _globals['_MODEL_PERIODICTUNINGSTATE']._serialized_end = 2578
    _globals['_MODEL_DATASTATE']._serialized_start = 2580
    _globals['_MODEL_DATASTATE']._serialized_end = 2648
    _globals['_MODEL_CONTEXTPRODUCTSTYPE']._serialized_start = 2650
    _globals['_MODEL_CONTEXTPRODUCTSTYPE']._serialized_end = 2769