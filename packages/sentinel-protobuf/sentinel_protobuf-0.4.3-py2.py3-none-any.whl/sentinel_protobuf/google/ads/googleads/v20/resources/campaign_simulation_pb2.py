"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/campaign_simulation.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.common import simulation_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_common_dot_simulation__pb2
from ......google.ads.googleads.v20.enums import simulation_modification_method_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_simulation__modification__method__pb2
from ......google.ads.googleads.v20.enums import simulation_type_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_simulation__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v20/resources/campaign_simulation.proto\x12"google.ads.googleads.v20.resources\x1a0google/ads/googleads/v20/common/simulation.proto\x1aCgoogle/ads/googleads/v20/enums/simulation_modification_method.proto\x1a4google/ads/googleads/v20/enums/simulation_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xba\x08\n\x12CampaignSimulation\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x03\xfaA-\n+googleads.googleapis.com/CampaignSimulation\x12\x18\n\x0bcampaign_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12T\n\x04type\x18\x03 \x01(\x0e2A.google.ads.googleads.v20.enums.SimulationTypeEnum.SimulationTypeB\x03\xe0A\x03\x12\x7f\n\x13modification_method\x18\x04 \x01(\x0e2].google.ads.googleads.v20.enums.SimulationModificationMethodEnum.SimulationModificationMethodB\x03\xe0A\x03\x12\x17\n\nstart_date\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x15\n\x08end_date\x18\x06 \x01(\tB\x03\xe0A\x03\x12]\n\x12cpc_bid_point_list\x18\x07 \x01(\x0b2:.google.ads.googleads.v20.common.CpcBidSimulationPointListB\x03\xe0A\x03H\x00\x12c\n\x15target_cpa_point_list\x18\x08 \x01(\x0b2=.google.ads.googleads.v20.common.TargetCpaSimulationPointListB\x03\xe0A\x03H\x00\x12e\n\x16target_roas_point_list\x18\t \x01(\x0b2>.google.ads.googleads.v20.common.TargetRoasSimulationPointListB\x03\xe0A\x03H\x00\x12|\n"target_impression_share_point_list\x18\n \x01(\x0b2I.google.ads.googleads.v20.common.TargetImpressionShareSimulationPointListB\x03\xe0A\x03H\x00\x12\\\n\x11budget_point_list\x18\x0b \x01(\x0b2:.google.ads.googleads.v20.common.BudgetSimulationPointListB\x03\xe0A\x03H\x00:\xa1\x01\xeaA\x9d\x01\n+googleads.googleapis.com/CampaignSimulation\x12ncustomers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}B\x0c\n\npoint_listB\x89\x02\n&com.google.ads.googleads.v20.resourcesB\x17CampaignSimulationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.campaign_simulation_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x17CampaignSimulationProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA-\n+googleads.googleapis.com/CampaignSimulation'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['campaign_id']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['campaign_id']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['type']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['modification_method']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['modification_method']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['start_date']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['start_date']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['end_date']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['end_date']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['cpc_bid_point_list']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['cpc_bid_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_cpa_point_list']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_cpa_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_roas_point_list']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_roas_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_impression_share_point_list']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['target_impression_share_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['budget_point_list']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION'].fields_by_name['budget_point_list']._serialized_options = b'\xe0A\x03'
    _globals['_CAMPAIGNSIMULATION']._loaded_options = None
    _globals['_CAMPAIGNSIMULATION']._serialized_options = b'\xeaA\x9d\x01\n+googleads.googleapis.com/CampaignSimulation\x12ncustomers/{customer_id}/campaignSimulations/{campaign_id}~{type}~{modification_method}~{start_date}~{end_date}'
    _globals['_CAMPAIGNSIMULATION']._serialized_start = 334
    _globals['_CAMPAIGNSIMULATION']._serialized_end = 1416