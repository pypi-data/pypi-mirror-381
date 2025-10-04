"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/analytics/data/v1beta/analytics_data_api.proto')
_sym_db = _symbol_database.Default()
from .....google.analytics.data.v1beta import data_pb2 as google_dot_analytics_dot_data_dot_v1beta_dot_data__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/analytics/data/v1beta/analytics_data_api.proto\x12\x1cgoogle.analytics.data.v1beta\x1a\'google/analytics/data/v1beta/data.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xfd\x02\n\x19CheckCompatibilityRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12;\n\ndimensions\x18\x02 \x03(\x0b2\'.google.analytics.data.v1beta.Dimension\x125\n\x07metrics\x18\x03 \x03(\x0b2$.google.analytics.data.v1beta.Metric\x12H\n\x10dimension_filter\x18\x04 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12E\n\rmetric_filter\x18\x05 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12I\n\x14compatibility_filter\x18\x06 \x01(\x0e2+.google.analytics.data.v1beta.Compatibility"\xc8\x01\n\x1aCheckCompatibilityResponse\x12W\n\x19dimension_compatibilities\x18\x01 \x03(\x0b24.google.analytics.data.v1beta.DimensionCompatibility\x12Q\n\x16metric_compatibilities\x18\x02 \x03(\x0b21.google.analytics.data.v1beta.MetricCompatibility"\xaf\x02\n\x08Metadata\x12\x0c\n\x04name\x18\x03 \x01(\t\x12C\n\ndimensions\x18\x01 \x03(\x0b2/.google.analytics.data.v1beta.DimensionMetadata\x12=\n\x07metrics\x18\x02 \x03(\x0b2,.google.analytics.data.v1beta.MetricMetadata\x12E\n\x0bcomparisons\x18\x04 \x03(\x0b20.google.analytics.data.v1beta.ComparisonMetadata:J\xeaAG\n%analyticsdata.googleapis.com/Metadata\x12\x1eproperties/{property}/metadata"\xe0\x05\n\x10RunReportRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12;\n\ndimensions\x18\x02 \x03(\x0b2\'.google.analytics.data.v1beta.Dimension\x125\n\x07metrics\x18\x03 \x03(\x0b2$.google.analytics.data.v1beta.Metric\x12<\n\x0bdate_ranges\x18\x04 \x03(\x0b2\'.google.analytics.data.v1beta.DateRange\x12H\n\x10dimension_filter\x18\x05 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12E\n\rmetric_filter\x18\x06 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12\x0e\n\x06offset\x18\x07 \x01(\x03\x12\r\n\x05limit\x18\x08 \x01(\x03\x12L\n\x13metric_aggregations\x18\t \x03(\x0e2/.google.analytics.data.v1beta.MetricAggregation\x128\n\torder_bys\x18\n \x03(\x0b2%.google.analytics.data.v1beta.OrderBy\x12\x15\n\rcurrency_code\x18\x0b \x01(\t\x12=\n\x0bcohort_spec\x18\x0c \x01(\x0b2(.google.analytics.data.v1beta.CohortSpec\x12\x17\n\x0fkeep_empty_rows\x18\r \x01(\x08\x12\x1d\n\x15return_property_quota\x18\x0e \x01(\x08\x12B\n\x0bcomparisons\x18\x0f \x03(\x0b2(.google.analytics.data.v1beta.ComparisonB\x03\xe0A\x01"\x97\x04\n\x11RunReportResponse\x12H\n\x11dimension_headers\x18\x01 \x03(\x0b2-.google.analytics.data.v1beta.DimensionHeader\x12B\n\x0emetric_headers\x18\x02 \x03(\x0b2*.google.analytics.data.v1beta.MetricHeader\x12/\n\x04rows\x18\x03 \x03(\x0b2!.google.analytics.data.v1beta.Row\x121\n\x06totals\x18\x04 \x03(\x0b2!.google.analytics.data.v1beta.Row\x123\n\x08maximums\x18\x05 \x03(\x0b2!.google.analytics.data.v1beta.Row\x123\n\x08minimums\x18\x06 \x03(\x0b2!.google.analytics.data.v1beta.Row\x12\x11\n\trow_count\x18\x07 \x01(\x05\x12@\n\x08metadata\x18\x08 \x01(\x0b2..google.analytics.data.v1beta.ResponseMetaData\x12C\n\x0eproperty_quota\x18\t \x01(\x0b2+.google.analytics.data.v1beta.PropertyQuota\x12\x0c\n\x04kind\x18\n \x01(\t"\xf3\x04\n\x15RunPivotReportRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12;\n\ndimensions\x18\x02 \x03(\x0b2\'.google.analytics.data.v1beta.Dimension\x125\n\x07metrics\x18\x03 \x03(\x0b2$.google.analytics.data.v1beta.Metric\x12<\n\x0bdate_ranges\x18\x04 \x03(\x0b2\'.google.analytics.data.v1beta.DateRange\x123\n\x06pivots\x18\x05 \x03(\x0b2#.google.analytics.data.v1beta.Pivot\x12H\n\x10dimension_filter\x18\x06 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12E\n\rmetric_filter\x18\x07 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12\x15\n\rcurrency_code\x18\x08 \x01(\t\x12=\n\x0bcohort_spec\x18\t \x01(\x0b2(.google.analytics.data.v1beta.CohortSpec\x12\x17\n\x0fkeep_empty_rows\x18\n \x01(\x08\x12\x1d\n\x15return_property_quota\x18\x0b \x01(\x08\x12B\n\x0bcomparisons\x18\x0c \x03(\x0b2(.google.analytics.data.v1beta.ComparisonB\x03\xe0A\x01"\xe5\x03\n\x16RunPivotReportResponse\x12@\n\rpivot_headers\x18\x01 \x03(\x0b2).google.analytics.data.v1beta.PivotHeader\x12H\n\x11dimension_headers\x18\x02 \x03(\x0b2-.google.analytics.data.v1beta.DimensionHeader\x12B\n\x0emetric_headers\x18\x03 \x03(\x0b2*.google.analytics.data.v1beta.MetricHeader\x12/\n\x04rows\x18\x04 \x03(\x0b2!.google.analytics.data.v1beta.Row\x125\n\naggregates\x18\x05 \x03(\x0b2!.google.analytics.data.v1beta.Row\x12@\n\x08metadata\x18\x06 \x01(\x0b2..google.analytics.data.v1beta.ResponseMetaData\x12C\n\x0eproperty_quota\x18\x07 \x01(\x0b2+.google.analytics.data.v1beta.PropertyQuota\x12\x0c\n\x04kind\x18\x08 \x01(\t"l\n\x16BatchRunReportsRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12@\n\x08requests\x18\x02 \x03(\x0b2..google.analytics.data.v1beta.RunReportRequest"i\n\x17BatchRunReportsResponse\x12@\n\x07reports\x18\x01 \x03(\x0b2/.google.analytics.data.v1beta.RunReportResponse\x12\x0c\n\x04kind\x18\x02 \x01(\t"v\n\x1bBatchRunPivotReportsRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12E\n\x08requests\x18\x02 \x03(\x0b23.google.analytics.data.v1beta.RunPivotReportRequest"y\n\x1cBatchRunPivotReportsResponse\x12K\n\rpivot_reports\x18\x01 \x03(\x0b24.google.analytics.data.v1beta.RunPivotReportResponse\x12\x0c\n\x04kind\x18\x02 \x01(\t"Q\n\x12GetMetadataRequest\x12;\n\x04name\x18\x01 \x01(\tB-\xe0A\x02\xfaA\'\n%analyticsdata.googleapis.com/Metadata"\xa9\x04\n\x18RunRealtimeReportRequest\x12\x10\n\x08property\x18\x01 \x01(\t\x12;\n\ndimensions\x18\x02 \x03(\x0b2\'.google.analytics.data.v1beta.Dimension\x125\n\x07metrics\x18\x03 \x03(\x0b2$.google.analytics.data.v1beta.Metric\x12H\n\x10dimension_filter\x18\x04 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12E\n\rmetric_filter\x18\x05 \x01(\x0b2..google.analytics.data.v1beta.FilterExpression\x12\r\n\x05limit\x18\x06 \x01(\x03\x12L\n\x13metric_aggregations\x18\x07 \x03(\x0e2/.google.analytics.data.v1beta.MetricAggregation\x128\n\torder_bys\x18\x08 \x03(\x0b2%.google.analytics.data.v1beta.OrderBy\x12\x1d\n\x15return_property_quota\x18\t \x01(\x08\x12@\n\rminute_ranges\x18\n \x03(\x0b2).google.analytics.data.v1beta.MinuteRange"\xdd\x03\n\x19RunRealtimeReportResponse\x12H\n\x11dimension_headers\x18\x01 \x03(\x0b2-.google.analytics.data.v1beta.DimensionHeader\x12B\n\x0emetric_headers\x18\x02 \x03(\x0b2*.google.analytics.data.v1beta.MetricHeader\x12/\n\x04rows\x18\x03 \x03(\x0b2!.google.analytics.data.v1beta.Row\x121\n\x06totals\x18\x04 \x03(\x0b2!.google.analytics.data.v1beta.Row\x123\n\x08maximums\x18\x05 \x03(\x0b2!.google.analytics.data.v1beta.Row\x123\n\x08minimums\x18\x06 \x03(\x0b2!.google.analytics.data.v1beta.Row\x12\x11\n\trow_count\x18\x07 \x01(\x05\x12C\n\x0eproperty_quota\x18\x08 \x01(\x0b2+.google.analytics.data.v1beta.PropertyQuota\x12\x0c\n\x04kind\x18\t \x01(\t"]\n\x18GetAudienceExportRequest\x12A\n\x04name\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+analyticsdata.googleapis.com/AudienceExport"\x92\x01\n\x1aListAudienceExportsRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+analyticsdata.googleapis.com/AudienceExport\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x97\x01\n\x1bListAudienceExportsResponse\x12F\n\x10audience_exports\x18\x01 \x03(\x0b2,.google.analytics.data.v1beta.AudienceExport\x12\x1c\n\x0fnext_page_token\x18\x02 \x01(\tH\x00\x88\x01\x01B\x12\n\x10_next_page_token"\xae\x01\n\x1bCreateAudienceExportRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\x12+analyticsdata.googleapis.com/AudienceExport\x12J\n\x0faudience_export\x18\x02 \x01(\x0b2,.google.analytics.data.v1beta.AudienceExportB\x03\xe0A\x02"\xfc\x05\n\x0eAudienceExport\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x08\xe0A\x03\x12\x15\n\x08audience\x18\x02 \x01(\tB\x03\xe0A\x02\x12"\n\x15audience_display_name\x18\x03 \x01(\tB\x03\xe0A\x03\x12H\n\ndimensions\x18\x04 \x03(\x0b2/.google.analytics.data.v1beta.AudienceDimensionB\x03\xe0A\x02\x12K\n\x05state\x18\x05 \x01(\x0e22.google.analytics.data.v1beta.AudienceExport.StateB\x03\xe0A\x03H\x00\x88\x01\x01\x12A\n\x13begin_creating_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x01\x88\x01\x01\x12*\n\x1dcreation_quota_tokens_charged\x18\x07 \x01(\x05B\x03\xe0A\x03\x12\x1b\n\trow_count\x18\x08 \x01(\x05B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1f\n\rerror_message\x18\t \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12&\n\x14percentage_completed\x18\n \x01(\x01B\x03\xe0A\x03H\x04\x88\x01\x01"D\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\x03:\x8b\x01\xeaA\x87\x01\n+analyticsdata.googleapis.com/AudienceExport\x127properties/{property}/audienceExports/{audience_export}*\x0faudienceExports2\x0eaudienceExportB\x08\n\x06_stateB\x16\n\x14_begin_creating_timeB\x0c\n\n_row_countB\x10\n\x0e_error_messageB\x17\n\x15_percentage_completed"\x18\n\x16AudienceExportMetadata"X\n\x1aQueryAudienceExportRequest\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x13\n\x06offset\x18\x02 \x01(\x03B\x03\xe0A\x01\x12\x12\n\x05limit\x18\x03 \x01(\x03B\x03\xe0A\x01"\xe5\x01\n\x1bQueryAudienceExportResponse\x12J\n\x0faudience_export\x18\x01 \x01(\x0b2,.google.analytics.data.v1beta.AudienceExportH\x00\x88\x01\x01\x12@\n\raudience_rows\x18\x02 \x03(\x0b2).google.analytics.data.v1beta.AudienceRow\x12\x16\n\trow_count\x18\x03 \x01(\x05H\x01\x88\x01\x01B\x12\n\x10_audience_exportB\x0c\n\n_row_count"]\n\x0bAudienceRow\x12N\n\x10dimension_values\x18\x01 \x03(\x0b24.google.analytics.data.v1beta.AudienceDimensionValue"0\n\x11AudienceDimension\x12\x1b\n\x0edimension_name\x18\x01 \x01(\tB\x03\xe0A\x01"6\n\x16AudienceDimensionValue\x12\x0f\n\x05value\x18\x01 \x01(\tH\x00B\x0b\n\tone_value2\x87\x12\n\x11BetaAnalyticsData\x12\xa2\x01\n\tRunReport\x12..google.analytics.data.v1beta.RunReportRequest\x1a/.google.analytics.data.v1beta.RunReportResponse"4\x82\xd3\xe4\x93\x02.")/v1beta/{property=properties/*}:runReport:\x01*\x12\xb6\x01\n\x0eRunPivotReport\x123.google.analytics.data.v1beta.RunPivotReportRequest\x1a4.google.analytics.data.v1beta.RunPivotReportResponse"9\x82\xd3\xe4\x93\x023"./v1beta/{property=properties/*}:runPivotReport:\x01*\x12\xba\x01\n\x0fBatchRunReports\x124.google.analytics.data.v1beta.BatchRunReportsRequest\x1a5.google.analytics.data.v1beta.BatchRunReportsResponse":\x82\xd3\xe4\x93\x024"//v1beta/{property=properties/*}:batchRunReports:\x01*\x12\xce\x01\n\x14BatchRunPivotReports\x129.google.analytics.data.v1beta.BatchRunPivotReportsRequest\x1a:.google.analytics.data.v1beta.BatchRunPivotReportsResponse"?\x82\xd3\xe4\x93\x029"4/v1beta/{property=properties/*}:batchRunPivotReports:\x01*\x12\x9c\x01\n\x0bGetMetadata\x120.google.analytics.data.v1beta.GetMetadataRequest\x1a&.google.analytics.data.v1beta.Metadata"3\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1beta/{name=properties/*/metadata}\x12\xc2\x01\n\x11RunRealtimeReport\x126.google.analytics.data.v1beta.RunRealtimeReportRequest\x1a7.google.analytics.data.v1beta.RunRealtimeReportResponse"<\x82\xd3\xe4\x93\x026"1/v1beta/{property=properties/*}:runRealtimeReport:\x01*\x12\xc6\x01\n\x12CheckCompatibility\x127.google.analytics.data.v1beta.CheckCompatibilityRequest\x1a8.google.analytics.data.v1beta.CheckCompatibilityResponse"=\x82\xd3\xe4\x93\x027"2/v1beta/{property=properties/*}:checkCompatibility:\x01*\x12\xfd\x01\n\x14CreateAudienceExport\x129.google.analytics.data.v1beta.CreateAudienceExportRequest\x1a\x1d.google.longrunning.Operation"\x8a\x01\xcaA(\n\x0eAudienceExport\x12\x16AudienceExportMetadata\xdaA\x16parent,audience_export\x82\xd3\xe4\x93\x02@"-/v1beta/{parent=properties/*}/audienceExports:\x0faudience_export\x12\xd1\x01\n\x13QueryAudienceExport\x128.google.analytics.data.v1beta.QueryAudienceExportRequest\x1a9.google.analytics.data.v1beta.QueryAudienceExportResponse"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta/{name=properties/*/audienceExports/*}:query:\x01*\x12\xb7\x01\n\x11GetAudienceExport\x126.google.analytics.data.v1beta.GetAudienceExportRequest\x1a,.google.analytics.data.v1beta.AudienceExport"<\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1beta/{name=properties/*/audienceExports/*}\x12\xca\x01\n\x13ListAudienceExports\x128.google.analytics.data.v1beta.ListAudienceExportsRequest\x1a9.google.analytics.data.v1beta.ListAudienceExportsResponse">\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1beta/{parent=properties/*}/audienceExports\x1a~\xcaA\x1canalyticsdata.googleapis.com\xd2A\\https://www.googleapis.com/auth/analytics,https://www.googleapis.com/auth/analytics.readonlyB\xbf\x01\n com.google.analytics.data.v1betaB\x15AnalyticsDataApiProtoP\x01Z@google.golang.org/genproto/googleapis/analytics/data/v1beta;data\xeaA?\n&analyticsadmin.googleapis.com/Property\x12\x15properties/{property}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.analytics.data.v1beta.analytics_data_api_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n com.google.analytics.data.v1betaB\x15AnalyticsDataApiProtoP\x01Z@google.golang.org/genproto/googleapis/analytics/data/v1beta;data\xeaA?\n&analyticsadmin.googleapis.com/Property\x12\x15properties/{property}'
    _globals['_METADATA']._loaded_options = None
    _globals['_METADATA']._serialized_options = b'\xeaAG\n%analyticsdata.googleapis.com/Metadata\x12\x1eproperties/{property}/metadata'
    _globals['_RUNREPORTREQUEST'].fields_by_name['comparisons']._loaded_options = None
    _globals['_RUNREPORTREQUEST'].fields_by_name['comparisons']._serialized_options = b'\xe0A\x01'
    _globals['_RUNPIVOTREPORTREQUEST'].fields_by_name['comparisons']._loaded_options = None
    _globals['_RUNPIVOTREPORTREQUEST'].fields_by_name['comparisons']._serialized_options = b'\xe0A\x01'
    _globals['_GETMETADATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETMETADATAREQUEST'].fields_by_name['name']._serialized_options = b"\xe0A\x02\xfaA'\n%analyticsdata.googleapis.com/Metadata"
    _globals['_GETAUDIENCEEXPORTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETAUDIENCEEXPORTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA-\n+analyticsdata.googleapis.com/AudienceExport'
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+analyticsdata.googleapis.com/AudienceExport'
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTAUDIENCEEXPORTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEAUDIENCEEXPORTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEAUDIENCEEXPORTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\x12+analyticsdata.googleapis.com/AudienceExport'
    _globals['_CREATEAUDIENCEEXPORTREQUEST'].fields_by_name['audience_export']._loaded_options = None
    _globals['_CREATEAUDIENCEEXPORTREQUEST'].fields_by_name['audience_export']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEEXPORT'].fields_by_name['name']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['audience']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['audience']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEEXPORT'].fields_by_name['audience_display_name']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['audience_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['dimensions']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['dimensions']._serialized_options = b'\xe0A\x02'
    _globals['_AUDIENCEEXPORT'].fields_by_name['state']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['begin_creating_time']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['begin_creating_time']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['creation_quota_tokens_charged']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['creation_quota_tokens_charged']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['row_count']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['row_count']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['error_message']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['error_message']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT'].fields_by_name['percentage_completed']._loaded_options = None
    _globals['_AUDIENCEEXPORT'].fields_by_name['percentage_completed']._serialized_options = b'\xe0A\x03'
    _globals['_AUDIENCEEXPORT']._loaded_options = None
    _globals['_AUDIENCEEXPORT']._serialized_options = b'\xeaA\x87\x01\n+analyticsdata.googleapis.com/AudienceExport\x127properties/{property}/audienceExports/{audience_export}*\x0faudienceExports2\x0eaudienceExport'
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['offset']._loaded_options = None
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['offset']._serialized_options = b'\xe0A\x01'
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['limit']._loaded_options = None
    _globals['_QUERYAUDIENCEEXPORTREQUEST'].fields_by_name['limit']._serialized_options = b'\xe0A\x01'
    _globals['_AUDIENCEDIMENSION'].fields_by_name['dimension_name']._loaded_options = None
    _globals['_AUDIENCEDIMENSION'].fields_by_name['dimension_name']._serialized_options = b'\xe0A\x01'
    _globals['_BETAANALYTICSDATA']._loaded_options = None
    _globals['_BETAANALYTICSDATA']._serialized_options = b'\xcaA\x1canalyticsdata.googleapis.com\xd2A\\https://www.googleapis.com/auth/analytics,https://www.googleapis.com/auth/analytics.readonly'
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunReport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunReport']._serialized_options = b'\x82\xd3\xe4\x93\x02.")/v1beta/{property=properties/*}:runReport:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunPivotReport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunPivotReport']._serialized_options = b'\x82\xd3\xe4\x93\x023"./v1beta/{property=properties/*}:runPivotReport:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['BatchRunReports']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['BatchRunReports']._serialized_options = b'\x82\xd3\xe4\x93\x024"//v1beta/{property=properties/*}:batchRunReports:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['BatchRunPivotReports']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['BatchRunPivotReports']._serialized_options = b'\x82\xd3\xe4\x93\x029"4/v1beta/{property=properties/*}:batchRunPivotReports:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['GetMetadata']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['GetMetadata']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02&\x12$/v1beta/{name=properties/*/metadata}'
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunRealtimeReport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['RunRealtimeReport']._serialized_options = b'\x82\xd3\xe4\x93\x026"1/v1beta/{property=properties/*}:runRealtimeReport:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['CheckCompatibility']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['CheckCompatibility']._serialized_options = b'\x82\xd3\xe4\x93\x027"2/v1beta/{property=properties/*}:checkCompatibility:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['CreateAudienceExport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['CreateAudienceExport']._serialized_options = b'\xcaA(\n\x0eAudienceExport\x12\x16AudienceExportMetadata\xdaA\x16parent,audience_export\x82\xd3\xe4\x93\x02@"-/v1beta/{parent=properties/*}/audienceExports:\x0faudience_export'
    _globals['_BETAANALYTICSDATA'].methods_by_name['QueryAudienceExport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['QueryAudienceExport']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1beta/{name=properties/*/audienceExports/*}:query:\x01*'
    _globals['_BETAANALYTICSDATA'].methods_by_name['GetAudienceExport']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['GetAudienceExport']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02/\x12-/v1beta/{name=properties/*/audienceExports/*}'
    _globals['_BETAANALYTICSDATA'].methods_by_name['ListAudienceExports']._loaded_options = None
    _globals['_BETAANALYTICSDATA'].methods_by_name['ListAudienceExports']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02/\x12-/v1beta/{parent=properties/*}/audienceExports'
    _globals['_CHECKCOMPATIBILITYREQUEST']._serialized_start = 314
    _globals['_CHECKCOMPATIBILITYREQUEST']._serialized_end = 695
    _globals['_CHECKCOMPATIBILITYRESPONSE']._serialized_start = 698
    _globals['_CHECKCOMPATIBILITYRESPONSE']._serialized_end = 898
    _globals['_METADATA']._serialized_start = 901
    _globals['_METADATA']._serialized_end = 1204
    _globals['_RUNREPORTREQUEST']._serialized_start = 1207
    _globals['_RUNREPORTREQUEST']._serialized_end = 1943
    _globals['_RUNREPORTRESPONSE']._serialized_start = 1946
    _globals['_RUNREPORTRESPONSE']._serialized_end = 2481
    _globals['_RUNPIVOTREPORTREQUEST']._serialized_start = 2484
    _globals['_RUNPIVOTREPORTREQUEST']._serialized_end = 3111
    _globals['_RUNPIVOTREPORTRESPONSE']._serialized_start = 3114
    _globals['_RUNPIVOTREPORTRESPONSE']._serialized_end = 3599
    _globals['_BATCHRUNREPORTSREQUEST']._serialized_start = 3601
    _globals['_BATCHRUNREPORTSREQUEST']._serialized_end = 3709
    _globals['_BATCHRUNREPORTSRESPONSE']._serialized_start = 3711
    _globals['_BATCHRUNREPORTSRESPONSE']._serialized_end = 3816
    _globals['_BATCHRUNPIVOTREPORTSREQUEST']._serialized_start = 3818
    _globals['_BATCHRUNPIVOTREPORTSREQUEST']._serialized_end = 3936
    _globals['_BATCHRUNPIVOTREPORTSRESPONSE']._serialized_start = 3938
    _globals['_BATCHRUNPIVOTREPORTSRESPONSE']._serialized_end = 4059
    _globals['_GETMETADATAREQUEST']._serialized_start = 4061
    _globals['_GETMETADATAREQUEST']._serialized_end = 4142
    _globals['_RUNREALTIMEREPORTREQUEST']._serialized_start = 4145
    _globals['_RUNREALTIMEREPORTREQUEST']._serialized_end = 4698
    _globals['_RUNREALTIMEREPORTRESPONSE']._serialized_start = 4701
    _globals['_RUNREALTIMEREPORTRESPONSE']._serialized_end = 5178
    _globals['_GETAUDIENCEEXPORTREQUEST']._serialized_start = 5180
    _globals['_GETAUDIENCEEXPORTREQUEST']._serialized_end = 5273
    _globals['_LISTAUDIENCEEXPORTSREQUEST']._serialized_start = 5276
    _globals['_LISTAUDIENCEEXPORTSREQUEST']._serialized_end = 5422
    _globals['_LISTAUDIENCEEXPORTSRESPONSE']._serialized_start = 5425
    _globals['_LISTAUDIENCEEXPORTSRESPONSE']._serialized_end = 5576
    _globals['_CREATEAUDIENCEEXPORTREQUEST']._serialized_start = 5579
    _globals['_CREATEAUDIENCEEXPORTREQUEST']._serialized_end = 5753
    _globals['_AUDIENCEEXPORT']._serialized_start = 5756
    _globals['_AUDIENCEEXPORT']._serialized_end = 6520
    _globals['_AUDIENCEEXPORT_STATE']._serialized_start = 6219
    _globals['_AUDIENCEEXPORT_STATE']._serialized_end = 6287
    _globals['_AUDIENCEEXPORTMETADATA']._serialized_start = 6522
    _globals['_AUDIENCEEXPORTMETADATA']._serialized_end = 6546
    _globals['_QUERYAUDIENCEEXPORTREQUEST']._serialized_start = 6548
    _globals['_QUERYAUDIENCEEXPORTREQUEST']._serialized_end = 6636
    _globals['_QUERYAUDIENCEEXPORTRESPONSE']._serialized_start = 6639
    _globals['_QUERYAUDIENCEEXPORTRESPONSE']._serialized_end = 6868
    _globals['_AUDIENCEROW']._serialized_start = 6870
    _globals['_AUDIENCEROW']._serialized_end = 6963
    _globals['_AUDIENCEDIMENSION']._serialized_start = 6965
    _globals['_AUDIENCEDIMENSION']._serialized_end = 7013
    _globals['_AUDIENCEDIMENSIONVALUE']._serialized_start = 7015
    _globals['_AUDIENCEDIMENSIONVALUE']._serialized_end = 7069
    _globals['_BETAANALYTICSDATA']._serialized_start = 7072
    _globals['_BETAANALYTICSDATA']._serialized_end = 9383