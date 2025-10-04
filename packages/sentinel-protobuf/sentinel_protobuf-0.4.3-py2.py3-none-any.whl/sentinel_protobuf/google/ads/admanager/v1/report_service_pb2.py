"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/report_service.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import report_messages_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_report__messages__pb2
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ads/admanager/v1/report_service.proto\x12\x17google.ads.admanager.v1\x1a-google/ads/admanager/v1/report_messages.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"I\n\x10RunReportRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/Report"c\n\x11RunReportMetadata\x12\x18\n\x10percent_complete\x18\x02 \x01(\x05\x124\n\x06report\x18\x04 \x01(\tB$\xfaA!\n\x1fadmanager.googleapis.com/Report"*\n\x11RunReportResponse\x12\x15\n\rreport_result\x18\x01 \x01(\t"I\n\x10GetReportRequest\x125\n\x04name\x18\x01 \x01(\tB\'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/Report"\xbe\x01\n\x12ListReportsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x11\n\x04skip\x18\x06 \x01(\x05B\x03\xe0A\x01"t\n\x13ListReportsResponse\x120\n\x07reports\x18\x01 \x03(\x0b2\x1f.google.ads.admanager.v1.Report\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x12\n\ntotal_size\x18\x03 \x01(\x05"\x85\x01\n\x13CreateReportRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/Network\x124\n\x06report\x18\x02 \x01(\x0b2\x1f.google.ads.admanager.v1.ReportB\x03\xe0A\x02"\x81\x01\n\x13UpdateReportRequest\x124\n\x06report\x18\x01 \x01(\x0b2\x1f.google.ads.admanager.v1.ReportB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"]\n\x1cFetchReportResultRowsRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xe5\x02\n\x1dFetchReportResultRowsResponse\x12;\n\x04rows\x18\x01 \x03(\x0b2-.google.ads.admanager.v1.Report.DataTable.Row\x12,\n\x08run_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12M\n\x0bdate_ranges\x18\x03 \x03(\x0b28.google.ads.admanager.v1.Report.DateRange.FixedDateRange\x12X\n\x16comparison_date_ranges\x18\x04 \x03(\x0b28.google.ads.admanager.v1.Report.DateRange.FixedDateRange\x12\x17\n\x0ftotal_row_count\x18\x05 \x01(\x05\x12\x17\n\x0fnext_page_token\x18\x06 \x01(\t2\xd2\x08\n\rReportService\x12\x87\x01\n\tGetReport\x12).google.ads.admanager.v1.GetReportRequest\x1a\x1f.google.ads.admanager.v1.Report".\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=networks/*/reports/*}\x12\x9a\x01\n\x0bListReports\x12+.google.ads.admanager.v1.ListReportsRequest\x1a,.google.ads.admanager.v1.ListReportsResponse"0\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=networks/*}/reports\x12\x9e\x01\n\x0cCreateReport\x12,.google.ads.admanager.v1.CreateReportRequest\x1a\x1f.google.ads.admanager.v1.Report"?\xdaA\rparent,report\x82\xd3\xe4\x93\x02)"\x1f/v1/{parent=networks/*}/reports:\x06report\x12\xaa\x01\n\x0cUpdateReport\x12,.google.ads.admanager.v1.UpdateReportRequest\x1a\x1f.google.ads.admanager.v1.Report"K\xdaA\x12report,update_mask\x82\xd3\xe4\x93\x0202&/v1/{report.name=networks/*/reports/*}:\x06report\x12\xb5\x01\n\tRunReport\x12).google.ads.admanager.v1.RunReportRequest\x1a\x1d.google.longrunning.Operation"^\xcaA&\n\x11RunReportResponse\x12\x11RunReportMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02("#/v1/{name=networks/*/reports/*}:run:\x01*\x12\xca\x01\n\x15FetchReportResultRows\x125.google.ads.admanager.v1.FetchReportResultRowsRequest\x1a6.google.ads.admanager.v1.FetchReportResultRowsResponse"B\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=networks/*/reports/*/results/*}:fetchRows\x1aG\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanagerB\xc6\x01\n\x1bcom.google.ads.admanager.v1B\x12ReportServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.report_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x12ReportServiceProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_RUNREPORTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_RUNREPORTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/Report'
    _globals['_RUNREPORTMETADATA'].fields_by_name['report']._loaded_options = None
    _globals['_RUNREPORTMETADATA'].fields_by_name['report']._serialized_options = b'\xfaA!\n\x1fadmanager.googleapis.com/Report'
    _globals['_GETREPORTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETREPORTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA!\n\x1fadmanager.googleapis.com/Report'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_LISTREPORTSREQUEST'].fields_by_name['skip']._loaded_options = None
    _globals['_LISTREPORTSREQUEST'].fields_by_name['skip']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEREPORTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREPORTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Network'
    _globals['_CREATEREPORTREQUEST'].fields_by_name['report']._loaded_options = None
    _globals['_CREATEREPORTREQUEST'].fields_by_name['report']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREPORTREQUEST'].fields_by_name['report']._loaded_options = None
    _globals['_UPDATEREPORTREQUEST'].fields_by_name['report']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEREPORTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEREPORTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_FETCHREPORTRESULTROWSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_FETCHREPORTRESULTROWSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_FETCHREPORTRESULTROWSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_FETCHREPORTRESULTROWSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_REPORTSERVICE']._loaded_options = None
    _globals['_REPORTSERVICE']._serialized_options = b'\xcaA\x18admanager.googleapis.com\xd2A)https://www.googleapis.com/auth/admanager'
    _globals['_REPORTSERVICE'].methods_by_name['GetReport']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['GetReport']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{name=networks/*/reports/*}'
    _globals['_REPORTSERVICE'].methods_by_name['ListReports']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['ListReports']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02!\x12\x1f/v1/{parent=networks/*}/reports'
    _globals['_REPORTSERVICE'].methods_by_name['CreateReport']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['CreateReport']._serialized_options = b'\xdaA\rparent,report\x82\xd3\xe4\x93\x02)"\x1f/v1/{parent=networks/*}/reports:\x06report'
    _globals['_REPORTSERVICE'].methods_by_name['UpdateReport']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['UpdateReport']._serialized_options = b'\xdaA\x12report,update_mask\x82\xd3\xe4\x93\x0202&/v1/{report.name=networks/*/reports/*}:\x06report'
    _globals['_REPORTSERVICE'].methods_by_name['RunReport']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['RunReport']._serialized_options = b'\xcaA&\n\x11RunReportResponse\x12\x11RunReportMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02("#/v1/{name=networks/*/reports/*}:run:\x01*'
    _globals['_REPORTSERVICE'].methods_by_name['FetchReportResultRows']._loaded_options = None
    _globals['_REPORTSERVICE'].methods_by_name['FetchReportResultRows']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x025\x123/v1/{name=networks/*/reports/*/results/*}:fetchRows'
    _globals['_RUNREPORTREQUEST']._serialized_start = 339
    _globals['_RUNREPORTREQUEST']._serialized_end = 412
    _globals['_RUNREPORTMETADATA']._serialized_start = 414
    _globals['_RUNREPORTMETADATA']._serialized_end = 513
    _globals['_RUNREPORTRESPONSE']._serialized_start = 515
    _globals['_RUNREPORTRESPONSE']._serialized_end = 557
    _globals['_GETREPORTREQUEST']._serialized_start = 559
    _globals['_GETREPORTREQUEST']._serialized_end = 632
    _globals['_LISTREPORTSREQUEST']._serialized_start = 635
    _globals['_LISTREPORTSREQUEST']._serialized_end = 825
    _globals['_LISTREPORTSRESPONSE']._serialized_start = 827
    _globals['_LISTREPORTSRESPONSE']._serialized_end = 943
    _globals['_CREATEREPORTREQUEST']._serialized_start = 946
    _globals['_CREATEREPORTREQUEST']._serialized_end = 1079
    _globals['_UPDATEREPORTREQUEST']._serialized_start = 1082
    _globals['_UPDATEREPORTREQUEST']._serialized_end = 1211
    _globals['_FETCHREPORTRESULTROWSREQUEST']._serialized_start = 1213
    _globals['_FETCHREPORTRESULTROWSREQUEST']._serialized_end = 1306
    _globals['_FETCHREPORTRESULTROWSRESPONSE']._serialized_start = 1309
    _globals['_FETCHREPORTRESULTROWSRESPONSE']._serialized_end = 1666
    _globals['_REPORTSERVICE']._serialized_start = 1669
    _globals['_REPORTSERVICE']._serialized_end = 2775