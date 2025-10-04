"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/batch/v1alpha/resource_allowance.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.batch.v1alpha import notification_pb2 as google_dot_cloud_dot_batch_dot_v1alpha_dot_notification__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.type import interval_pb2 as google_dot_type_dot_interval__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/cloud/batch/v1alpha/resource_allowance.proto\x12\x1agoogle.cloud.batch.v1alpha\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a-google/cloud/batch/v1alpha/notification.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1agoogle/type/interval.proto"\xd0\x04\n\x11ResourceAllowance\x12V\n\x18usage_resource_allowance\x18\x04 \x01(\x0b22.google.cloud.batch.v1alpha.UsageResourceAllowanceH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12N\n\x06labels\x18\x05 \x03(\x0b29.google.cloud.batch.v1alpha.ResourceAllowance.LabelsEntryB\x03\xe0A\x01\x12D\n\rnotifications\x18\x06 \x03(\x0b2(.google.cloud.batch.v1alpha.NotificationB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xa4\x01\xeaA\xa0\x01\n&batch.googleapis.com/ResourceAllowance\x12Oprojects/{project}/locations/{location}/resourceAllowances/{resource_allowance}*\x12resourceAllowances2\x11resourceAllowanceB\x14\n\x12resource_allowance"\xb2\x01\n\x16UsageResourceAllowance\x12I\n\x04spec\x18\x01 \x01(\x0b26.google.cloud.batch.v1alpha.UsageResourceAllowanceSpecB\x03\xe0A\x02\x12M\n\x06status\x18\x02 \x01(\x0b28.google.cloud.batch.v1alpha.UsageResourceAllowanceStatusB\x03\xe0A\x03"\x86\x02\n\x1aUsageResourceAllowanceSpec\x12\x11\n\x04type\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\x05limit\x18\x02 \x01(\x0b2<.google.cloud.batch.v1alpha.UsageResourceAllowanceSpec.LimitB\x03\xe0A\x02\x1a\x82\x01\n\x05Limit\x12J\n\x0fcalendar_period\x18\x01 \x01(\x0e2*.google.cloud.batch.v1alpha.CalendarPeriodB\x03\xe0A\x01H\x00\x12\x17\n\x05limit\x18\x02 \x01(\x01B\x03\xe0A\x02H\x01\x88\x01\x01B\n\n\x08durationB\x08\n\x06_limit"\xee\x06\n\x1cUsageResourceAllowanceStatus\x12F\n\x05state\x18\x01 \x01(\x0e22.google.cloud.batch.v1alpha.ResourceAllowanceStateB\x03\xe0A\x03\x12_\n\x0climit_status\x18\x02 \x01(\x0b2D.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.LimitStatusB\x03\xe0A\x03\x12_\n\x06report\x18\x03 \x01(\x0b2J.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReportB\x03\xe0A\x03\x1a\x93\x01\n\x0bLimitStatus\x128\n\x14consumption_interval\x18\x01 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x03\x12\x17\n\x05limit\x18\x02 \x01(\x01B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1a\n\x08consumed\x18\x03 \x01(\x01B\x03\xe0A\x03H\x01\x88\x01\x01B\x08\n\x06_limitB\x0b\n\t_consumed\x1av\n\x11PeriodConsumption\x128\n\x14consumption_interval\x18\x01 \x01(\x0b2\x15.google.type.IntervalB\x03\xe0A\x03\x12\x1a\n\x08consumed\x18\x02 \x01(\x01B\x03\xe0A\x03H\x00\x88\x01\x01B\x0b\n\t_consumed\x1a\xb5\x02\n\x11ConsumptionReport\x12\x91\x01\n\x1alatest_period_consumptions\x18\x01 \x03(\x0b2h.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.ConsumptionReport.LatestPeriodConsumptionsEntryB\x03\xe0A\x03\x1a\x8b\x01\n\x1dLatestPeriodConsumptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12Y\n\x05value\x18\x02 \x01(\x0b2J.google.cloud.batch.v1alpha.UsageResourceAllowanceStatus.PeriodConsumption:\x028\x01*f\n\x0eCalendarPeriod\x12\x1f\n\x1bCALENDAR_PERIOD_UNSPECIFIED\x10\x00\x12\t\n\x05MONTH\x10\x01\x12\x0b\n\x07QUARTER\x10\x02\x12\x08\n\x04YEAR\x10\x03\x12\x08\n\x04WEEK\x10\x04\x12\x07\n\x03DAY\x10\x05*\x82\x01\n\x16ResourceAllowanceState\x12(\n$RESOURCE_ALLOWANCE_STATE_UNSPECIFIED\x10\x00\x12\x1d\n\x19RESOURCE_ALLOWANCE_ACTIVE\x10\x01\x12\x1f\n\x1bRESOURCE_ALLOWANCE_DEPLETED\x10\x02B\xd0\x01\n\x1ecom.google.cloud.batch.v1alphaB\x16ResourceAllowanceProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alphab\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.batch.v1alpha.resource_allowance_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.batch.v1alphaB\x16ResourceAllowanceProtoP\x01Z4cloud.google.com/go/batch/apiv1alpha/batchpb;batchpb\xa2\x02\x03GCB\xaa\x02\x1aGoogle.Cloud.Batch.V1Alpha\xca\x02\x1aGoogle\\Cloud\\Batch\\V1alpha\xea\x02\x1dGoogle::Cloud::Batch::V1alpha'
    _globals['_RESOURCEALLOWANCE_LABELSENTRY']._loaded_options = None
    _globals['_RESOURCEALLOWANCE_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCEALLOWANCE'].fields_by_name['name']._loaded_options = None
    _globals['_RESOURCEALLOWANCE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_RESOURCEALLOWANCE'].fields_by_name['uid']._loaded_options = None
    _globals['_RESOURCEALLOWANCE'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_RESOURCEALLOWANCE'].fields_by_name['create_time']._loaded_options = None
    _globals['_RESOURCEALLOWANCE'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_RESOURCEALLOWANCE'].fields_by_name['labels']._loaded_options = None
    _globals['_RESOURCEALLOWANCE'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEALLOWANCE'].fields_by_name['notifications']._loaded_options = None
    _globals['_RESOURCEALLOWANCE'].fields_by_name['notifications']._serialized_options = b'\xe0A\x01'
    _globals['_RESOURCEALLOWANCE']._loaded_options = None
    _globals['_RESOURCEALLOWANCE']._serialized_options = b'\xeaA\xa0\x01\n&batch.googleapis.com/ResourceAllowance\x12Oprojects/{project}/locations/{location}/resourceAllowances/{resource_allowance}*\x12resourceAllowances2\x11resourceAllowance'
    _globals['_USAGERESOURCEALLOWANCE'].fields_by_name['spec']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCE'].fields_by_name['spec']._serialized_options = b'\xe0A\x02'
    _globals['_USAGERESOURCEALLOWANCE'].fields_by_name['status']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT'].fields_by_name['calendar_period']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT'].fields_by_name['calendar_period']._serialized_options = b'\xe0A\x01'
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT'].fields_by_name['limit']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT'].fields_by_name['limit']._serialized_options = b'\xe0A\x02'
    _globals['_USAGERESOURCEALLOWANCESPEC'].fields_by_name['type']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESPEC'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_USAGERESOURCEALLOWANCESPEC'].fields_by_name['limit']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESPEC'].fields_by_name['limit']._serialized_options = b'\xe0A\x02'
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['consumption_interval']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['consumption_interval']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['limit']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['limit']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['consumed']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS'].fields_by_name['consumed']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION'].fields_by_name['consumption_interval']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION'].fields_by_name['consumption_interval']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION'].fields_by_name['consumed']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION'].fields_by_name['consumed']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT_LATESTPERIODCONSUMPTIONSENTRY']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT_LATESTPERIODCONSUMPTIONSENTRY']._serialized_options = b'8\x01'
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT'].fields_by_name['latest_period_consumptions']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT'].fields_by_name['latest_period_consumptions']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['limit_status']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['limit_status']._serialized_options = b'\xe0A\x03'
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['report']._loaded_options = None
    _globals['_USAGERESOURCEALLOWANCESTATUS'].fields_by_name['report']._serialized_options = b'\xe0A\x03'
    _globals['_CALENDARPERIOD']._serialized_start = 2202
    _globals['_CALENDARPERIOD']._serialized_end = 2304
    _globals['_RESOURCEALLOWANCESTATE']._serialized_start = 2307
    _globals['_RESOURCEALLOWANCESTATE']._serialized_end = 2437
    _globals['_RESOURCEALLOWANCE']._serialized_start = 281
    _globals['_RESOURCEALLOWANCE']._serialized_end = 873
    _globals['_RESOURCEALLOWANCE_LABELSENTRY']._serialized_start = 639
    _globals['_RESOURCEALLOWANCE_LABELSENTRY']._serialized_end = 684
    _globals['_USAGERESOURCEALLOWANCE']._serialized_start = 876
    _globals['_USAGERESOURCEALLOWANCE']._serialized_end = 1054
    _globals['_USAGERESOURCEALLOWANCESPEC']._serialized_start = 1057
    _globals['_USAGERESOURCEALLOWANCESPEC']._serialized_end = 1319
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT']._serialized_start = 1189
    _globals['_USAGERESOURCEALLOWANCESPEC_LIMIT']._serialized_end = 1319
    _globals['_USAGERESOURCEALLOWANCESTATUS']._serialized_start = 1322
    _globals['_USAGERESOURCEALLOWANCESTATUS']._serialized_end = 2200
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS']._serialized_start = 1621
    _globals['_USAGERESOURCEALLOWANCESTATUS_LIMITSTATUS']._serialized_end = 1768
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION']._serialized_start = 1770
    _globals['_USAGERESOURCEALLOWANCESTATUS_PERIODCONSUMPTION']._serialized_end = 1888
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT']._serialized_start = 1891
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT']._serialized_end = 2200
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT_LATESTPERIODCONSUMPTIONSENTRY']._serialized_start = 2061
    _globals['_USAGERESOURCEALLOWANCESTATUS_CONSUMPTIONREPORT_LATESTPERIODCONSUMPTIONSENTRY']._serialized_end = 2200