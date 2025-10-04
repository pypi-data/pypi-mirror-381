"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/privacy_policy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/bigquery/v2/privacy_policy.proto\x12\x18google.cloud.bigquery.v2\x1a\x1fgoogle/api/field_behavior.proto"j\n\x1aAggregationThresholdPolicy\x12\x1b\n\tthreshold\x18\x01 \x01(\x03B\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x14privacy_unit_columns\x18\x02 \x03(\tB\x03\xe0A\x01B\x0c\n\n_threshold"\x8d\x04\n\x19DifferentialPrivacyPolicy\x12\'\n\x15max_epsilon_per_query\x18\x01 \x01(\x01B\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x0fdelta_per_query\x18\x02 \x01(\x01B\x03\xe0A\x01H\x01\x88\x01\x01\x12(\n\x16max_groups_contributed\x18\x03 \x01(\x03B\x03\xe0A\x01H\x02\x88\x01\x01\x12%\n\x13privacy_unit_column\x18\x04 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12 \n\x0eepsilon_budget\x18\x05 \x01(\x01B\x03\xe0A\x01H\x04\x88\x01\x01\x12\x1e\n\x0cdelta_budget\x18\x06 \x01(\x01B\x03\xe0A\x01H\x05\x88\x01\x01\x12*\n\x18epsilon_budget_remaining\x18\x07 \x01(\x01B\x03\xe0A\x03H\x06\x88\x01\x01\x12(\n\x16delta_budget_remaining\x18\x08 \x01(\x01B\x03\xe0A\x03H\x07\x88\x01\x01B\x18\n\x16_max_epsilon_per_queryB\x12\n\x10_delta_per_queryB\x19\n\x17_max_groups_contributedB\x16\n\x14_privacy_unit_columnB\x11\n\x0f_epsilon_budgetB\x0f\n\r_delta_budgetB\x1b\n\x19_epsilon_budget_remainingB\x19\n\x17_delta_budget_remaining"\xa4\x02\n\x15JoinRestrictionPolicy\x12_\n\x0ejoin_condition\x18\x01 \x01(\x0e2=.google.cloud.bigquery.v2.JoinRestrictionPolicy.JoinConditionB\x03\xe0A\x01H\x00\x88\x01\x01\x12!\n\x14join_allowed_columns\x18\x02 \x03(\tB\x03\xe0A\x01"t\n\rJoinCondition\x12\x1e\n\x1aJOIN_CONDITION_UNSPECIFIED\x10\x00\x12\x0c\n\x08JOIN_ANY\x10\x01\x12\x0c\n\x08JOIN_ALL\x10\x02\x12\x15\n\x11JOIN_NOT_REQUIRED\x10\x03\x12\x10\n\x0cJOIN_BLOCKED\x10\x04B\x11\n\x0f_join_condition"\xdd\x02\n\rPrivacyPolicy\x12a\n\x1caggregation_threshold_policy\x18\x02 \x01(\x0b24.google.cloud.bigquery.v2.AggregationThresholdPolicyB\x03\xe0A\x01H\x00\x12_\n\x1bdifferential_privacy_policy\x18\x03 \x01(\x0b23.google.cloud.bigquery.v2.DifferentialPrivacyPolicyB\x03\xe0A\x01H\x00\x12Z\n\x17join_restriction_policy\x18\x01 \x01(\x0b2/.google.cloud.bigquery.v2.JoinRestrictionPolicyB\x03\xe0A\x01H\x01\x88\x01\x01B\x10\n\x0eprivacy_policyB\x1a\n\x18_join_restriction_policyBo\n\x1ccom.google.cloud.bigquery.v2B\x12PrivacyPolicyProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.privacy_policy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x12PrivacyPolicyProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_AGGREGATIONTHRESHOLDPOLICY'].fields_by_name['threshold']._loaded_options = None
    _globals['_AGGREGATIONTHRESHOLDPOLICY'].fields_by_name['threshold']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATIONTHRESHOLDPOLICY'].fields_by_name['privacy_unit_columns']._loaded_options = None
    _globals['_AGGREGATIONTHRESHOLDPOLICY'].fields_by_name['privacy_unit_columns']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['max_epsilon_per_query']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['max_epsilon_per_query']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_per_query']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_per_query']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['max_groups_contributed']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['max_groups_contributed']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['privacy_unit_column']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['privacy_unit_column']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['epsilon_budget']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['epsilon_budget']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_budget']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_budget']._serialized_options = b'\xe0A\x01'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['epsilon_budget_remaining']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['epsilon_budget_remaining']._serialized_options = b'\xe0A\x03'
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_budget_remaining']._loaded_options = None
    _globals['_DIFFERENTIALPRIVACYPOLICY'].fields_by_name['delta_budget_remaining']._serialized_options = b'\xe0A\x03'
    _globals['_JOINRESTRICTIONPOLICY'].fields_by_name['join_condition']._loaded_options = None
    _globals['_JOINRESTRICTIONPOLICY'].fields_by_name['join_condition']._serialized_options = b'\xe0A\x01'
    _globals['_JOINRESTRICTIONPOLICY'].fields_by_name['join_allowed_columns']._loaded_options = None
    _globals['_JOINRESTRICTIONPOLICY'].fields_by_name['join_allowed_columns']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVACYPOLICY'].fields_by_name['aggregation_threshold_policy']._loaded_options = None
    _globals['_PRIVACYPOLICY'].fields_by_name['aggregation_threshold_policy']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVACYPOLICY'].fields_by_name['differential_privacy_policy']._loaded_options = None
    _globals['_PRIVACYPOLICY'].fields_by_name['differential_privacy_policy']._serialized_options = b'\xe0A\x01'
    _globals['_PRIVACYPOLICY'].fields_by_name['join_restriction_policy']._loaded_options = None
    _globals['_PRIVACYPOLICY'].fields_by_name['join_restriction_policy']._serialized_options = b'\xe0A\x01'
    _globals['_AGGREGATIONTHRESHOLDPOLICY']._serialized_start = 108
    _globals['_AGGREGATIONTHRESHOLDPOLICY']._serialized_end = 214
    _globals['_DIFFERENTIALPRIVACYPOLICY']._serialized_start = 217
    _globals['_DIFFERENTIALPRIVACYPOLICY']._serialized_end = 742
    _globals['_JOINRESTRICTIONPOLICY']._serialized_start = 745
    _globals['_JOINRESTRICTIONPOLICY']._serialized_end = 1037
    _globals['_JOINRESTRICTIONPOLICY_JOINCONDITION']._serialized_start = 902
    _globals['_JOINRESTRICTIONPOLICY_JOINCONDITION']._serialized_end = 1018
    _globals['_PRIVACYPOLICY']._serialized_start = 1040
    _globals['_PRIVACYPOLICY']._serialized_end = 1389