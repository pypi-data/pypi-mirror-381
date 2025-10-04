"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/customer_lifecycle_goal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import lifecycle_goals_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_lifecycle__goals__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v21/resources/customer_lifecycle_goal.proto\x12"google.ads.googleads.v21.resources\x1a5google/ads/googleads/v21/common/lifecycle_goals.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x82\x03\n\x15CustomerLifecycleGoal\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/CustomerLifecycleGoal\x12r\n(customer_acquisition_goal_value_settings\x18\x03 \x01(\x0b2;.google.ads.googleads.v21.common.LifecycleGoalValueSettingsB\x03\xe0A\x03\x12A\n\x0eowner_customer\x18\x04 \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer:c\xeaA`\n.googleads.googleapis.com/CustomerLifecycleGoal\x12.customers/{customer_id}/customerLifecycleGoalsB\x8c\x02\n&com.google.ads.googleads.v21.resourcesB\x1aCustomerLifecycleGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.customer_lifecycle_goal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x1aCustomerLifecycleGoalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/CustomerLifecycleGoal'
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['customer_acquisition_goal_value_settings']._loaded_options = None
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['customer_acquisition_goal_value_settings']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['owner_customer']._loaded_options = None
    _globals['_CUSTOMERLIFECYCLEGOAL'].fields_by_name['owner_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMERLIFECYCLEGOAL']._loaded_options = None
    _globals['_CUSTOMERLIFECYCLEGOAL']._serialized_options = b'\xeaA`\n.googleads.googleapis.com/CustomerLifecycleGoal\x12.customers/{customer_id}/customerLifecycleGoals'
    _globals['_CUSTOMERLIFECYCLEGOAL']._serialized_start = 220
    _globals['_CUSTOMERLIFECYCLEGOAL']._serialized_end = 606