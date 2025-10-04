"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/experiment.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import metric_goal_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_metric__goal__pb2
from ......google.ads.googleads.v21.enums import async_action_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_async__action__status__pb2
from ......google.ads.googleads.v21.enums import experiment_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_experiment__status__pb2
from ......google.ads.googleads.v21.enums import experiment_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_experiment__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/ads/googleads/v21/resources/experiment.proto\x12"google.ads.googleads.v21.resources\x1a1google/ads/googleads/v21/common/metric_goal.proto\x1a8google/ads/googleads/v21/enums/async_action_status.proto\x1a6google/ads/googleads/v21/enums/experiment_status.proto\x1a4google/ads/googleads/v21/enums/experiment_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xa6\x06\n\nExperiment\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x05\xfaA%\n#googleads.googleapis.com/Experiment\x12\x1f\n\rexperiment_id\x18\t \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\n \x01(\tB\x03\xe0A\x02\x12\x13\n\x0bdescription\x18\x0b \x01(\t\x12\x0e\n\x06suffix\x18\x0c \x01(\t\x12T\n\x04type\x18\r \x01(\x0e2A.google.ads.googleads.v21.enums.ExperimentTypeEnum.ExperimentTypeB\x03\xe0A\x02\x12U\n\x06status\x18\x0e \x01(\x0e2E.google.ads.googleads.v21.enums.ExperimentStatusEnum.ExperimentStatus\x12\x17\n\nstart_date\x18\x0f \x01(\tH\x01\x88\x01\x01\x12\x15\n\x08end_date\x18\x10 \x01(\tH\x02\x88\x01\x01\x12:\n\x05goals\x18\x11 \x03(\x0b2+.google.ads.googleads.v21.common.MetricGoal\x12(\n\x16long_running_operation\x18\x12 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12d\n\x0epromote_status\x18\x13 \x01(\x0e2G.google.ads.googleads.v21.enums.AsyncActionStatusEnum.AsyncActionStatusB\x03\xe0A\x03\x12\x1e\n\x0csync_enabled\x18\x14 \x01(\x08B\x03\xe0A\x05H\x04\x88\x01\x01:X\xeaAU\n#googleads.googleapis.com/Experiment\x12.customers/{customer_id}/experiments/{trial_id}B\x10\n\x0e_experiment_idB\r\n\x0b_start_dateB\x0b\n\t_end_dateB\x19\n\x17_long_running_operationB\x0f\n\r_sync_enabledB\x81\x02\n&com.google.ads.googleads.v21.resourcesB\x0fExperimentProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.experiment_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x0fExperimentProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_EXPERIMENT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_EXPERIMENT'].fields_by_name['experiment_id']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['experiment_id']._serialized_options = b'\xe0A\x03'
    _globals['_EXPERIMENT'].fields_by_name['name']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENT'].fields_by_name['type']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENT'].fields_by_name['long_running_operation']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['long_running_operation']._serialized_options = b'\xe0A\x03'
    _globals['_EXPERIMENT'].fields_by_name['promote_status']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['promote_status']._serialized_options = b'\xe0A\x03'
    _globals['_EXPERIMENT'].fields_by_name['sync_enabled']._loaded_options = None
    _globals['_EXPERIMENT'].fields_by_name['sync_enabled']._serialized_options = b'\xe0A\x05'
    _globals['_EXPERIMENT']._loaded_options = None
    _globals['_EXPERIMENT']._serialized_options = b'\xeaAU\n#googleads.googleapis.com/Experiment\x12.customers/{customer_id}/experiments/{trial_id}'
    _globals['_EXPERIMENT']._serialized_start = 371
    _globals['_EXPERIMENT']._serialized_end = 1177