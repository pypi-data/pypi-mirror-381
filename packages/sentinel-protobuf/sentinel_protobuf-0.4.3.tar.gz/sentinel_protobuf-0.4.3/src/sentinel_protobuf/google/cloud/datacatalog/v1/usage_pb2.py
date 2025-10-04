"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/datacatalog/v1/usage.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\'google/cloud/datacatalog/v1/usage.proto\x12\x1bgoogle.cloud.datacatalog.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x91\x01\n\nUsageStats\x12\x19\n\x11total_completions\x18\x01 \x01(\x02\x12\x16\n\x0etotal_failures\x18\x02 \x01(\x02\x12\x1b\n\x13total_cancellations\x18\x03 \x01(\x02\x123\n+total_execution_time_for_completions_millis\x18\x04 \x01(\x02":\n\x10CommonUsageStats\x12\x17\n\nview_count\x18\x01 \x01(\x03H\x00\x88\x01\x01B\r\n\x0b_view_count"\xa2\x04\n\x0bUsageSignal\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12h\n\x17usage_within_time_range\x18\x02 \x03(\x0b2B.google.cloud.datacatalog.v1.UsageSignal.UsageWithinTimeRangeEntryB\x03\xe0A\x03\x12p\n\x1ecommon_usage_within_time_range\x18\x03 \x03(\x0b2H.google.cloud.datacatalog.v1.UsageSignal.CommonUsageWithinTimeRangeEntry\x12\x1b\n\x0efavorite_count\x18\x04 \x01(\x03H\x00\x88\x01\x01\x1ad\n\x19UsageWithinTimeRangeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.datacatalog.v1.UsageStats:\x028\x01\x1ap\n\x1fCommonUsageWithinTimeRangeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12<\n\x05value\x18\x02 \x01(\x0b2-.google.cloud.datacatalog.v1.CommonUsageStats:\x028\x01B\x11\n\x0f_favorite_countB\xc3\x01\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1.usage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1fcom.google.cloud.datacatalog.v1P\x01ZAcloud.google.com/go/datacatalog/apiv1/datacatalogpb;datacatalogpb\xaa\x02\x1bGoogle.Cloud.DataCatalog.V1\xca\x02\x1bGoogle\\Cloud\\DataCatalog\\V1\xea\x02\x1eGoogle::Cloud::DataCatalog::V1'
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._loaded_options = None
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_options = b'8\x01'
    _globals['_USAGESIGNAL_COMMONUSAGEWITHINTIMERANGEENTRY']._loaded_options = None
    _globals['_USAGESIGNAL_COMMONUSAGEWITHINTIMERANGEENTRY']._serialized_options = b'8\x01'
    _globals['_USAGESIGNAL'].fields_by_name['usage_within_time_range']._loaded_options = None
    _globals['_USAGESIGNAL'].fields_by_name['usage_within_time_range']._serialized_options = b'\xe0A\x03'
    _globals['_USAGESTATS']._serialized_start = 139
    _globals['_USAGESTATS']._serialized_end = 284
    _globals['_COMMONUSAGESTATS']._serialized_start = 286
    _globals['_COMMONUSAGESTATS']._serialized_end = 344
    _globals['_USAGESIGNAL']._serialized_start = 347
    _globals['_USAGESIGNAL']._serialized_end = 893
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_start = 660
    _globals['_USAGESIGNAL_USAGEWITHINTIMERANGEENTRY']._serialized_end = 760
    _globals['_USAGESIGNAL_COMMONUSAGEWITHINTIMERANGEENTRY']._serialized_start = 762
    _globals['_USAGESIGNAL_COMMONUSAGEWITHINTIMERANGEENTRY']._serialized_end = 874