"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/monitoring/v3/alert.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ....google.monitoring.v3 import common_pb2 as google_dot_monitoring_dot_v3_dot_common__pb2
from ....google.monitoring.v3 import mutation_record_pb2 as google_dot_monitoring_dot_v3_dot_mutation__record__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
from ....google.type import timeofday_pb2 as google_dot_type_dot_timeofday__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/monitoring/v3/alert.proto\x12\x14google.monitoring.v3\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a!google/monitoring/v3/common.proto\x1a*google/monitoring/v3/mutation_record.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto\x1a\x1bgoogle/type/timeofday.proto"\x95-\n\x0bAlertPolicy\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12F\n\rdocumentation\x18\r \x01(\x0b2/.google.monitoring.v3.AlertPolicy.Documentation\x12F\n\x0buser_labels\x18\x10 \x03(\x0b21.google.monitoring.v3.AlertPolicy.UserLabelsEntry\x12?\n\nconditions\x18\x0c \x03(\x0b2+.google.monitoring.v3.AlertPolicy.Condition\x12I\n\x08combiner\x18\x06 \x01(\x0e27.google.monitoring.v3.AlertPolicy.ConditionCombinerType\x12+\n\x07enabled\x18\x11 \x01(\x0b2\x1a.google.protobuf.BoolValue\x12$\n\x08validity\x18\x12 \x01(\x0b2\x12.google.rpc.Status\x12\x1d\n\x15notification_channels\x18\x0e \x03(\t\x12=\n\x0fcreation_record\x18\n \x01(\x0b2$.google.monitoring.v3.MutationRecord\x12=\n\x0fmutation_record\x18\x0b \x01(\x0b2$.google.monitoring.v3.MutationRecord\x12G\n\x0ealert_strategy\x18\x15 \x01(\x0b2/.google.monitoring.v3.AlertPolicy.AlertStrategy\x12A\n\x08severity\x18\x16 \x01(\x0e2*.google.monitoring.v3.AlertPolicy.SeverityB\x03\xe0A\x01\x1a\xbe\x01\n\rDocumentation\x12\x0f\n\x07content\x18\x01 \x01(\t\x12\x11\n\tmime_type\x18\x02 \x01(\t\x12\x14\n\x07subject\x18\x03 \x01(\tB\x03\xe0A\x01\x12H\n\x05links\x18\x04 \x03(\x0b24.google.monitoring.v3.AlertPolicy.Documentation.LinkB\x03\xe0A\x01\x1a)\n\x04Link\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x1a\xc6\x1d\n\tCondition\x12\x0c\n\x04name\x18\x0c \x01(\t\x12\x14\n\x0cdisplay_name\x18\x06 \x01(\t\x12Z\n\x13condition_threshold\x18\x01 \x01(\x0b2;.google.monitoring.v3.AlertPolicy.Condition.MetricThresholdH\x00\x12U\n\x10condition_absent\x18\x02 \x01(\x0b29.google.monitoring.v3.AlertPolicy.Condition.MetricAbsenceH\x00\x12U\n\x15condition_matched_log\x18\x14 \x01(\x0b24.google.monitoring.v3.AlertPolicy.Condition.LogMatchH\x00\x12{\n#condition_monitoring_query_language\x18\x13 \x01(\x0b2L.google.monitoring.v3.AlertPolicy.Condition.MonitoringQueryLanguageConditionH\x00\x12{\n#condition_prometheus_query_language\x18\x15 \x01(\x0b2L.google.monitoring.v3.AlertPolicy.Condition.PrometheusQueryLanguageConditionH\x00\x12Q\n\rcondition_sql\x18\x16 \x01(\x0b28.google.monitoring.v3.AlertPolicy.Condition.SqlConditionH\x00\x1a5\n\x07Trigger\x12\x0f\n\x05count\x18\x01 \x01(\x05H\x00\x12\x11\n\x07percent\x18\x02 \x01(\x01H\x00B\x06\n\x04type\x1a\x9e\x05\n\x0fMetricThreshold\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x0caggregations\x18\x08 \x03(\x0b2!.google.monitoring.v3.Aggregation\x12\x1a\n\x12denominator_filter\x18\t \x01(\t\x12C\n\x18denominator_aggregations\x18\n \x03(\x0b2!.google.monitoring.v3.Aggregation\x12e\n\x10forecast_options\x18\x0c \x01(\x0b2K.google.monitoring.v3.AlertPolicy.Condition.MetricThreshold.ForecastOptions\x128\n\ncomparison\x18\x04 \x01(\x0e2$.google.monitoring.v3.ComparisonType\x12\x17\n\x0fthreshold_value\x18\x05 \x01(\x01\x12+\n\x08duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\x07trigger\x18\x07 \x01(\x0b23.google.monitoring.v3.AlertPolicy.Condition.Trigger\x12b\n\x17evaluation_missing_data\x18\x0b \x01(\x0e2A.google.monitoring.v3.AlertPolicy.Condition.EvaluationMissingData\x1aK\n\x0fForecastOptions\x128\n\x10forecast_horizon\x18\x01 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02\x1a\xd0\x01\n\rMetricAbsence\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x127\n\x0caggregations\x18\x05 \x03(\x0b2!.google.monitoring.v3.Aggregation\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\x07trigger\x18\x03 \x01(\x0b23.google.monitoring.v3.AlertPolicy.Condition.Trigger\x1a\xbc\x01\n\x08LogMatch\x12\x13\n\x06filter\x18\x01 \x01(\tB\x03\xe0A\x02\x12c\n\x10label_extractors\x18\x02 \x03(\x0b2I.google.monitoring.v3.AlertPolicy.Condition.LogMatch.LabelExtractorsEntry\x1a6\n\x14LabelExtractorsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\x88\x02\n MonitoringQueryLanguageCondition\x12\r\n\x05query\x18\x01 \x01(\t\x12+\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration\x12D\n\x07trigger\x18\x03 \x01(\x0b23.google.monitoring.v3.AlertPolicy.Condition.Trigger\x12b\n\x17evaluation_missing_data\x18\x04 \x01(\x0e2A.google.monitoring.v3.AlertPolicy.Condition.EvaluationMissingData\x1a\x9d\x03\n PrometheusQueryLanguageCondition\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x120\n\x08duration\x18\x02 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12;\n\x13evaluation_interval\x18\x03 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01\x12m\n\x06labels\x18\x04 \x03(\x0b2X.google.monitoring.v3.AlertPolicy.Condition.PrometheusQueryLanguageCondition.LabelsEntryB\x03\xe0A\x01\x12\x17\n\nrule_group\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x17\n\nalert_rule\x18\x06 \x01(\tB\x03\xe0A\x01\x12&\n\x19disable_metric_validation\x18\x07 \x01(\x08B\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a\xd1\x06\n\x0cSqlCondition\x12\x12\n\x05query\x18\x01 \x01(\tB\x03\xe0A\x02\x12S\n\x07minutes\x18\x02 \x01(\x0b2@.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.MinutesH\x00\x12Q\n\x06hourly\x18\x03 \x01(\x0b2?.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.HourlyH\x00\x12O\n\x05daily\x18\x04 \x01(\x0b2>.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.DailyH\x00\x12_\n\x0erow_count_test\x18\x05 \x01(\x0b2E.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.RowCountTestH\x01\x12\\\n\x0cboolean_test\x18\x06 \x01(\x0b2D.google.monitoring.v3.AlertPolicy.Condition.SqlCondition.BooleanTestH\x01\x1a#\n\x07Minutes\x12\x18\n\x0bperiodicity\x18\x01 \x01(\x05B\x03\xe0A\x02\x1aU\n\x06Hourly\x12\x18\n\x0bperiodicity\x18\x01 \x01(\x05B\x03\xe0A\x02\x12\x1f\n\rminute_offset\x18\x02 \x01(\x05B\x03\xe0A\x01H\x00\x88\x01\x01B\x10\n\x0e_minute_offset\x1aV\n\x05Daily\x12\x18\n\x0bperiodicity\x18\x01 \x01(\x05B\x03\xe0A\x02\x123\n\x0eexecution_time\x18\x02 \x01(\x0b2\x16.google.type.TimeOfDayB\x03\xe0A\x01\x1ae\n\x0cRowCountTest\x12=\n\ncomparison\x18\x01 \x01(\x0e2$.google.monitoring.v3.ComparisonTypeB\x03\xe0A\x02\x12\x16\n\tthreshold\x18\x02 \x01(\x03B\x03\xe0A\x02\x1a"\n\x0bBooleanTest\x12\x13\n\x06column\x18\x01 \x01(\tB\x03\xe0A\x02B\n\n\x08scheduleB\n\n\x08evaluate"\xad\x01\n\x15EvaluationMissingData\x12\'\n#EVALUATION_MISSING_DATA_UNSPECIFIED\x10\x00\x12$\n EVALUATION_MISSING_DATA_INACTIVE\x10\x01\x12"\n\x1eEVALUATION_MISSING_DATA_ACTIVE\x10\x02\x12!\n\x1dEVALUATION_MISSING_DATA_NO_OP\x10\x03:\x97\x02\xeaA\x93\x02\n.monitoring.googleapis.com/AlertPolicyCondition\x12Fprojects/{project}/alertPolicies/{alert_policy}/conditions/{condition}\x12Porganizations/{organization}/alertPolicies/{alert_policy}/conditions/{condition}\x12Dfolders/{folder}/alertPolicies/{alert_policy}/conditions/{condition}\x12\x01*B\x0b\n\tcondition\x1a\x8c\x05\n\rAlertStrategy\x12f\n\x17notification_rate_limit\x18\x01 \x01(\x0b2E.google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationRateLimit\x12`\n\x14notification_prompts\x18\x02 \x03(\x0e2B.google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationPrompt\x12-\n\nauto_close\x18\x03 \x01(\x0b2\x19.google.protobuf.Duration\x12r\n\x1dnotification_channel_strategy\x18\x04 \x03(\x0b2K.google.monitoring.v3.AlertPolicy.AlertStrategy.NotificationChannelStrategy\x1aB\n\x15NotificationRateLimit\x12)\n\x06period\x18\x01 \x01(\x0b2\x19.google.protobuf.Duration\x1aw\n\x1bNotificationChannelStrategy\x12"\n\x1anotification_channel_names\x18\x01 \x03(\t\x124\n\x11renotify_interval\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"Q\n\x12NotificationPrompt\x12#\n\x1fNOTIFICATION_PROMPT_UNSPECIFIED\x10\x00\x12\n\n\x06OPENED\x10\x01\x12\n\n\x06CLOSED\x10\x03\x1a1\n\x0fUserLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"a\n\x15ConditionCombinerType\x12\x17\n\x13COMBINE_UNSPECIFIED\x10\x00\x12\x07\n\x03AND\x10\x01\x12\x06\n\x02OR\x10\x02\x12\x1e\n\x1aAND_WITH_MATCHING_RESOURCE\x10\x03"J\n\x08Severity\x12\x18\n\x14SEVERITY_UNSPECIFIED\x10\x00\x12\x0c\n\x08CRITICAL\x10\x01\x12\t\n\x05ERROR\x10\x02\x12\x0b\n\x07WARNING\x10\x03:\xc9\x01\xeaA\xc5\x01\n%monitoring.googleapis.com/AlertPolicy\x12/projects/{project}/alertPolicies/{alert_policy}\x129organizations/{organization}/alertPolicies/{alert_policy}\x12-folders/{folder}/alertPolicies/{alert_policy}\x12\x01*B\xc5\x01\n\x18com.google.monitoring.v3B\nAlertProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.monitoring.v3.alert_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x18com.google.monitoring.v3B\nAlertProtoP\x01ZAcloud.google.com/go/monitoring/apiv3/v2/monitoringpb;monitoringpb\xaa\x02\x1aGoogle.Cloud.Monitoring.V3\xca\x02\x1aGoogle\\Cloud\\Monitoring\\V3\xea\x02\x1dGoogle::Cloud::Monitoring::V3'
    _globals['_ALERTPOLICY_DOCUMENTATION'].fields_by_name['subject']._loaded_options = None
    _globals['_ALERTPOLICY_DOCUMENTATION'].fields_by_name['subject']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_DOCUMENTATION'].fields_by_name['links']._loaded_options = None
    _globals['_ALERTPOLICY_DOCUMENTATION'].fields_by_name['links']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD_FORECASTOPTIONS'].fields_by_name['forecast_horizon']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD_FORECASTOPTIONS'].fields_by_name['forecast_horizon']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD'].fields_by_name['filter']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_METRICABSENCE'].fields_by_name['filter']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_METRICABSENCE'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH_LABELEXTRACTORSENTRY']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH_LABELEXTRACTORSENTRY']._serialized_options = b'8\x01'
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH'].fields_by_name['filter']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH'].fields_by_name['filter']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION_LABELSENTRY']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['query']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['duration']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['duration']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['evaluation_interval']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['evaluation_interval']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['labels']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['rule_group']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['rule_group']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['alert_rule']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['alert_rule']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['disable_metric_validation']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION'].fields_by_name['disable_metric_validation']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_MINUTES'].fields_by_name['periodicity']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_MINUTES'].fields_by_name['periodicity']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY'].fields_by_name['periodicity']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY'].fields_by_name['periodicity']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY'].fields_by_name['minute_offset']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY'].fields_by_name['minute_offset']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY'].fields_by_name['periodicity']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY'].fields_by_name['periodicity']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY'].fields_by_name['execution_time']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY'].fields_by_name['execution_time']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST'].fields_by_name['comparison']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST'].fields_by_name['comparison']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST'].fields_by_name['threshold']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST'].fields_by_name['threshold']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_BOOLEANTEST'].fields_by_name['column']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_BOOLEANTEST'].fields_by_name['column']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION'].fields_by_name['query']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION'].fields_by_name['query']._serialized_options = b'\xe0A\x02'
    _globals['_ALERTPOLICY_CONDITION']._loaded_options = None
    _globals['_ALERTPOLICY_CONDITION']._serialized_options = b'\xeaA\x93\x02\n.monitoring.googleapis.com/AlertPolicyCondition\x12Fprojects/{project}/alertPolicies/{alert_policy}/conditions/{condition}\x12Porganizations/{organization}/alertPolicies/{alert_policy}/conditions/{condition}\x12Dfolders/{folder}/alertPolicies/{alert_policy}/conditions/{condition}\x12\x01*'
    _globals['_ALERTPOLICY_USERLABELSENTRY']._loaded_options = None
    _globals['_ALERTPOLICY_USERLABELSENTRY']._serialized_options = b'8\x01'
    _globals['_ALERTPOLICY'].fields_by_name['name']._loaded_options = None
    _globals['_ALERTPOLICY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ALERTPOLICY'].fields_by_name['severity']._loaded_options = None
    _globals['_ALERTPOLICY'].fields_by_name['severity']._serialized_options = b'\xe0A\x01'
    _globals['_ALERTPOLICY']._loaded_options = None
    _globals['_ALERTPOLICY']._serialized_options = b'\xeaA\xc5\x01\n%monitoring.googleapis.com/AlertPolicy\x12/projects/{project}/alertPolicies/{alert_policy}\x129organizations/{organization}/alertPolicies/{alert_policy}\x12-folders/{folder}/alertPolicies/{alert_policy}\x12\x01*'
    _globals['_ALERTPOLICY']._serialized_start = 316
    _globals['_ALERTPOLICY']._serialized_end = 6097
    _globals['_ALERTPOLICY_DOCUMENTATION']._serialized_start = 1037
    _globals['_ALERTPOLICY_DOCUMENTATION']._serialized_end = 1227
    _globals['_ALERTPOLICY_DOCUMENTATION_LINK']._serialized_start = 1186
    _globals['_ALERTPOLICY_DOCUMENTATION_LINK']._serialized_end = 1227
    _globals['_ALERTPOLICY_CONDITION']._serialized_start = 1230
    _globals['_ALERTPOLICY_CONDITION']._serialized_end = 5012
    _globals['_ALERTPOLICY_CONDITION_TRIGGER']._serialized_start = 1878
    _globals['_ALERTPOLICY_CONDITION_TRIGGER']._serialized_end = 1931
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD']._serialized_start = 1934
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD']._serialized_end = 2604
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD_FORECASTOPTIONS']._serialized_start = 2529
    _globals['_ALERTPOLICY_CONDITION_METRICTHRESHOLD_FORECASTOPTIONS']._serialized_end = 2604
    _globals['_ALERTPOLICY_CONDITION_METRICABSENCE']._serialized_start = 2607
    _globals['_ALERTPOLICY_CONDITION_METRICABSENCE']._serialized_end = 2815
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH']._serialized_start = 2818
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH']._serialized_end = 3006
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH_LABELEXTRACTORSENTRY']._serialized_start = 2952
    _globals['_ALERTPOLICY_CONDITION_LOGMATCH_LABELEXTRACTORSENTRY']._serialized_end = 3006
    _globals['_ALERTPOLICY_CONDITION_MONITORINGQUERYLANGUAGECONDITION']._serialized_start = 3009
    _globals['_ALERTPOLICY_CONDITION_MONITORINGQUERYLANGUAGECONDITION']._serialized_end = 3273
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION']._serialized_start = 3276
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION']._serialized_end = 3689
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION_LABELSENTRY']._serialized_start = 3644
    _globals['_ALERTPOLICY_CONDITION_PROMETHEUSQUERYLANGUAGECONDITION_LABELSENTRY']._serialized_end = 3689
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION']._serialized_start = 3692
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION']._serialized_end = 4541
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_MINUTES']._serialized_start = 4168
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_MINUTES']._serialized_end = 4203
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY']._serialized_start = 4205
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_HOURLY']._serialized_end = 4290
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY']._serialized_start = 4292
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_DAILY']._serialized_end = 4378
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST']._serialized_start = 4380
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_ROWCOUNTTEST']._serialized_end = 4481
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_BOOLEANTEST']._serialized_start = 4483
    _globals['_ALERTPOLICY_CONDITION_SQLCONDITION_BOOLEANTEST']._serialized_end = 4517
    _globals['_ALERTPOLICY_CONDITION_EVALUATIONMISSINGDATA']._serialized_start = 4544
    _globals['_ALERTPOLICY_CONDITION_EVALUATIONMISSINGDATA']._serialized_end = 4717
    _globals['_ALERTPOLICY_ALERTSTRATEGY']._serialized_start = 5015
    _globals['_ALERTPOLICY_ALERTSTRATEGY']._serialized_end = 5667
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONRATELIMIT']._serialized_start = 5397
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONRATELIMIT']._serialized_end = 5463
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONCHANNELSTRATEGY']._serialized_start = 5465
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONCHANNELSTRATEGY']._serialized_end = 5584
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONPROMPT']._serialized_start = 5586
    _globals['_ALERTPOLICY_ALERTSTRATEGY_NOTIFICATIONPROMPT']._serialized_end = 5667
    _globals['_ALERTPOLICY_USERLABELSENTRY']._serialized_start = 5669
    _globals['_ALERTPOLICY_USERLABELSENTRY']._serialized_end = 5718
    _globals['_ALERTPOLICY_CONDITIONCOMBINERTYPE']._serialized_start = 5720
    _globals['_ALERTPOLICY_CONDITIONCOMBINERTYPE']._serialized_end = 5817
    _globals['_ALERTPOLICY_SEVERITY']._serialized_start = 5819
    _globals['_ALERTPOLICY_SEVERITY']._serialized_end = 5893