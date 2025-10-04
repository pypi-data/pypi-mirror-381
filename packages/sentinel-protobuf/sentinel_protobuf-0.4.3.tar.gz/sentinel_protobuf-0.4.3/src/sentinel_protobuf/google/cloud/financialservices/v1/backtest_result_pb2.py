"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/backtest_result.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import bigquery_destination_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_bigquery__destination__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/cloud/financialservices/v1/backtest_result.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/financialservices/v1/bigquery_destination.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9b\x08\n\x0eBacktestResult\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12M\n\x06labels\x18\x04 \x03(\x0b2=.google.cloud.financialservices.v1.BacktestResult.LabelsEntry\x12K\n\x05state\x18\x05 \x01(\x0e27.google.cloud.financialservices.v1.BacktestResult.StateB\x03\xe0A\x03\x12A\n\x07dataset\x18\x06 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset\x12=\n\x05model\x18\x07 \x01(\tB.\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model\x121\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x18\n\x10backtest_periods\x18\n \x01(\x05\x12d\n\x12performance_target\x18\x0b \x01(\x0b2C.google.cloud.financialservices.v1.BacktestResult.PerformanceTargetB\x03\xe0A\x02\x12P\n\x10line_of_business\x18\x0c \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x03\x1aF\n\x11PerformanceTarget\x121\n$party_investigations_per_period_hint\x18\x01 \x01(\x03B\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:\x99\x01\xeaA\x95\x01\n/financialservices.googleapis.com/BacktestResult\x12bprojects/{project_num}/locations/{location}/instances/{instance}/backtestResults/{backtest_result}"\xa8\x01\n\x1aListBacktestResultsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x98\x01\n\x1bListBacktestResultsResponse\x12K\n\x10backtest_results\x18\x01 \x03(\x0b21.google.cloud.financialservices.v1.BacktestResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"a\n\x18GetBacktestResultRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult"\xeb\x01\n\x1bCreateBacktestResultRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x1f\n\x12backtest_result_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12O\n\x0fbacktest_result\x18\x03 \x01(\x0b21.google.cloud.financialservices.v1.BacktestResultB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xbd\x01\n\x1bUpdateBacktestResultRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12O\n\x0fbacktest_result\x18\x02 \x01(\x0b21.google.cloud.financialservices.v1.BacktestResultB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"}\n\x1bDeleteBacktestResultRequest\x12E\n\x04name\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xdd\x01\n#ExportBacktestResultMetadataRequest\x12P\n\x0fbacktest_result\x18\x01 \x01(\tB7\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult\x12d\n\x1fstructured_metadata_destination\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02"&\n$ExportBacktestResultMetadataResponseB\x82\x02\n%com.google.cloud.financialservices.v1B\x13BacktestResultProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.backtest_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x13BacktestResultProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_BACKTESTRESULT_PERFORMANCETARGET'].fields_by_name['party_investigations_per_period_hint']._loaded_options = None
    _globals['_BACKTESTRESULT_PERFORMANCETARGET'].fields_by_name['party_investigations_per_period_hint']._serialized_options = b'\xe0A\x02'
    _globals['_BACKTESTRESULT_LABELSENTRY']._loaded_options = None
    _globals['_BACKTESTRESULT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_BACKTESTRESULT'].fields_by_name['name']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_BACKTESTRESULT'].fields_by_name['create_time']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKTESTRESULT'].fields_by_name['update_time']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_BACKTESTRESULT'].fields_by_name['state']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_BACKTESTRESULT'].fields_by_name['dataset']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_BACKTESTRESULT'].fields_by_name['model']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model'
    _globals['_BACKTESTRESULT'].fields_by_name['end_time']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_BACKTESTRESULT'].fields_by_name['performance_target']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['performance_target']._serialized_options = b'\xe0A\x02'
    _globals['_BACKTESTRESULT'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_BACKTESTRESULT'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x03'
    _globals['_BACKTESTRESULT']._loaded_options = None
    _globals['_BACKTESTRESULT']._serialized_options = b'\xeaA\x95\x01\n/financialservices.googleapis.com/BacktestResult\x12bprojects/{project_num}/locations/{location}/instances/{instance}/backtestResults/{backtest_result}'
    _globals['_LISTBACKTESTRESULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTBACKTESTRESULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_GETBACKTESTRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETBACKTESTRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult'
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result_id']._loaded_options = None
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result']._loaded_options = None
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result']._loaded_options = None
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['backtest_result']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEBACKTESTRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEBACKTESTRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult'
    _globals['_DELETEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEBACKTESTRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST'].fields_by_name['backtest_result']._loaded_options = None
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST'].fields_by_name['backtest_result']._serialized_options = b'\xe0A\x02\xfaA1\n/financialservices.googleapis.com/BacktestResult'
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._loaded_options = None
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._serialized_options = b'\xe0A\x02'
    _globals['_BACKTESTRESULT']._serialized_start = 342
    _globals['_BACKTESTRESULT']._serialized_end = 1393
    _globals['_BACKTESTRESULT_PERFORMANCETARGET']._serialized_start = 1034
    _globals['_BACKTESTRESULT_PERFORMANCETARGET']._serialized_end = 1104
    _globals['_BACKTESTRESULT_LABELSENTRY']._serialized_start = 1106
    _globals['_BACKTESTRESULT_LABELSENTRY']._serialized_end = 1151
    _globals['_BACKTESTRESULT_STATE']._serialized_start = 1153
    _globals['_BACKTESTRESULT_STATE']._serialized_end = 1237
    _globals['_LISTBACKTESTRESULTSREQUEST']._serialized_start = 1396
    _globals['_LISTBACKTESTRESULTSREQUEST']._serialized_end = 1564
    _globals['_LISTBACKTESTRESULTSRESPONSE']._serialized_start = 1567
    _globals['_LISTBACKTESTRESULTSRESPONSE']._serialized_end = 1719
    _globals['_GETBACKTESTRESULTREQUEST']._serialized_start = 1721
    _globals['_GETBACKTESTRESULTREQUEST']._serialized_end = 1818
    _globals['_CREATEBACKTESTRESULTREQUEST']._serialized_start = 1821
    _globals['_CREATEBACKTESTRESULTREQUEST']._serialized_end = 2056
    _globals['_UPDATEBACKTESTRESULTREQUEST']._serialized_start = 2059
    _globals['_UPDATEBACKTESTRESULTREQUEST']._serialized_end = 2248
    _globals['_DELETEBACKTESTRESULTREQUEST']._serialized_start = 2250
    _globals['_DELETEBACKTESTRESULTREQUEST']._serialized_end = 2375
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST']._serialized_start = 2378
    _globals['_EXPORTBACKTESTRESULTMETADATAREQUEST']._serialized_end = 2599
    _globals['_EXPORTBACKTESTRESULTMETADATARESPONSE']._serialized_start = 2601
    _globals['_EXPORTBACKTESTRESULTMETADATARESPONSE']._serialized_end = 2639