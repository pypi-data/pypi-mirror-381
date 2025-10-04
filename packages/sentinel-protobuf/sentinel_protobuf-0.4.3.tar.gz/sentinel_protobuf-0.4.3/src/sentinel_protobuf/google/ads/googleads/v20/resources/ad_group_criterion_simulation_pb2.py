"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/ad_group_criterion_simulation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import simulation_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_simulation__pb2
from ......google.ads.googleads.v20.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_simulation__modification__method__pb2
from ......google.ads.googleads.v20.enums import simulation_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_simulation__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nFgoogle/ads/googleads/v20/resources/ad_group_criterion_simulation.proto\x12"google.ads.googleads.v20.resources\x1a0google/ads/googleads/v20/common/simulation.proto\x1aCgoogle/ads/googleads/v20/enums/simulation_modification_method.proto\x1a4google/ads/googleads/v20/enums/simulation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x9c\x07\n\x1aAdGroupCriterionSimulation\x12R\n\rresource_name\x18\x01 \x01(\tB;\xe0A\x03\xfaA5\n3googleads.googleapis.com/AdGroupCriterionSimulation\x12\x1d\n\x0bad_group_id\x18\t \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1e\n\x0ccriterion_id\x18\n \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12T\n\x04type\x18\x04 \x01(\x0e2A.google.ads.googleads.v20.enums.SimulationTypeEnum.SimulationTypeB\x03\xe0A\x03\x12\x7f\n\x13modification_method\x18\x05 \x01(\x0e2].google.ads.googleads.v20.enums.SimulationModificationMethodEnum.SimulationModificationMethodB\x03\xe0A\x03\x12\x1c\n\nstart_date\x18\x0b \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1a\n\x08end_date\x18\x0c \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12]\n\x12cpc_bid_point_list\x18\x08 \x01(\x0b2:.google.ads.googleads.v20.common.CpcBidSimulationPointListB\x03\xe0A\x03H\x00\x12l\n\x1apercent_cpc_bid_point_list\x18\r \x01(\x0b2A.google.ads.googleads.v20.common.PercentCpcBidSimulationPointListB\x03\xe0A\x03H\x00:\xc1\x01\xeaA\xbd\x01\n3googleads.googleapis.com/AdGroupCriterionSimulation\x12\x85\x01customers/{customer_id}/adGroupCriterionSimulations/{ad_group_id}~{criterion_id}~{type}~{modification_method}~{start_date}~{end_date}B\x0c\n\npoint_listB\x0e\n\x0c_ad_group_idB\x0f\n\r_criterion_idB\r\n\x0b_start_dateB\x0b\n\t_end_dateB\x91\x02\n&com.google.ads.googleads.v20.resourcesB\x1fAdGroupCriterionSimulationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.ad_group_criterion_simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x1fAdGroupCriterionSimulationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA5\n3googleads.googleapis.com/AdGroupCriterionSimulation'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['ad_group_id']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['ad_group_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['criterion_id']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['criterion_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['type']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['modification_method']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['modification_method']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['start_date']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['start_date']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['end_date']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['end_date']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['cpc_bid_point_list']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['cpc_bid_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['percent_cpc_bid_point_list']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION'].fields_by_name['percent_cpc_bid_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_ADGROUPCRITERIONSIMULATION']._loaded_options = None
    _globals['_ADGROUPCRITERIONSIMULATION']._serialized_options = b'\xeaA\xbd\x01\n3googleads.googleapis.com/AdGroupCriterionSimulation\x12\x85\x01customers/{customer_id}/adGroupCriterionSimulations/{ad_group_id}~{criterion_id}~{type}~{modification_method}~{start_date}~{end_date}'
    _globals['_ADGROUPCRITERIONSIMULATION']._serialized_start = 344
    _globals['_ADGROUPCRITERIONSIMULATION']._serialized_end = 1268