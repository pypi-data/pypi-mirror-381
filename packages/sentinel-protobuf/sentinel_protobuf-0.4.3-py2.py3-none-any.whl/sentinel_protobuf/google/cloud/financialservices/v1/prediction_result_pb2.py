"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/financialservices/v1/prediction_result.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.financialservices.v1 import bigquery_destination_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_bigquery__destination__pb2
from .....google.cloud.financialservices.v1 import line_of_business_pb2 as google_dot_cloud_dot_financialservices_dot_v1_dot_line__of__business__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/financialservices/v1/prediction_result.proto\x12!google.cloud.financialservices.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/financialservices/v1/bigquery_destination.proto\x1a8google/cloud/financialservices/v1/line_of_business.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x93\t\n\x10PredictionResult\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12O\n\x06labels\x18\x04 \x03(\x0b2?.google.cloud.financialservices.v1.PredictionResult.LabelsEntry\x12M\n\x05state\x18\x05 \x01(\x0e29.google.cloud.financialservices.v1.PredictionResult.StateB\x03\xe0A\x03\x12A\n\x07dataset\x18\x06 \x01(\tB0\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset\x12=\n\x05model\x18\x07 \x01(\tB.\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model\x121\n\x08end_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02\x12\x1a\n\x12prediction_periods\x18\n \x01(\x05\x12Q\n\x07outputs\x18\x0b \x01(\x0b2;.google.cloud.financialservices.v1.PredictionResult.OutputsB\x03\xe0A\x02\x12P\n\x10line_of_business\x18\x0c \x01(\x0e21.google.cloud.financialservices.v1.LineOfBusinessB\x03\xe0A\x03\x1a\xc2\x01\n\x07Outputs\x12[\n\x16prediction_destination\x18\x01 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02\x12Z\n\x1aexplainability_destination\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestination\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\x0c\n\x08UPDATING\x10\x03\x12\x0c\n\x08DELETING\x10\x04:\x9f\x01\xeaA\x9b\x01\n1financialservices.googleapis.com/PredictionResult\x12fprojects/{project_num}/locations/{location}/instances/{instance}/predictionResults/{prediction_result}"\xaa\x01\n\x1cListPredictionResultsRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0e\n\x06filter\x18\x04 \x01(\t\x12\x10\n\x08order_by\x18\x05 \x01(\t"\x9e\x01\n\x1dListPredictionResultsResponse\x12O\n\x12prediction_results\x18\x01 \x03(\x0b23.google.cloud.financialservices.v1.PredictionResult\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x13\n\x0bunreachable\x18\x03 \x03(\t"e\n\x1aGetPredictionResultRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult"\xf3\x01\n\x1dCreatePredictionResultRequest\x12A\n\x06parent\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance\x12!\n\x14prediction_result_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12S\n\x11prediction_result\x18\x03 \x01(\x0b23.google.cloud.financialservices.v1.PredictionResultB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xc3\x01\n\x1dUpdatePredictionResultRequest\x124\n\x0bupdate_mask\x18\x01 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01\x12S\n\x11prediction_result\x18\x02 \x01(\x0b23.google.cloud.financialservices.v1.PredictionResultB\x03\xe0A\x02\x12\x17\n\nrequest_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x1dDeletePredictionResultRequest\x12G\n\x04name\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult\x12\x17\n\nrequest_id\x18\x02 \x01(\tB\x03\xe0A\x01"\xe3\x01\n%ExportPredictionResultMetadataRequest\x12T\n\x11prediction_result\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult\x12d\n\x1fstructured_metadata_destination\x18\x02 \x01(\x0b26.google.cloud.financialservices.v1.BigQueryDestinationB\x03\xe0A\x02"(\n&ExportPredictionResultMetadataResponseB\x84\x02\n%com.google.cloud.financialservices.v1B\x15PredictionResultProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.financialservices.v1.prediction_result_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.cloud.financialservices.v1B\x15PredictionResultProtoP\x01ZScloud.google.com/go/financialservices/apiv1/financialservicespb;financialservicespb\xaa\x02!Google.Cloud.FinancialServices.V1\xca\x02!Google\\Cloud\\FinancialServices\\V1\xea\x02$Google::Cloud::FinancialServices::V1'
    _globals['_PREDICTIONRESULT_OUTPUTS'].fields_by_name['prediction_destination']._loaded_options = None
    _globals['_PREDICTIONRESULT_OUTPUTS'].fields_by_name['prediction_destination']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTIONRESULT_LABELSENTRY']._loaded_options = None
    _globals['_PREDICTIONRESULT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_PREDICTIONRESULT'].fields_by_name['name']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONRESULT'].fields_by_name['create_time']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONRESULT'].fields_by_name['update_time']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONRESULT'].fields_by_name['state']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONRESULT'].fields_by_name['dataset']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02\xfaA*\n(financialservices.googleapis.com/Dataset'
    _globals['_PREDICTIONRESULT'].fields_by_name['model']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['model']._serialized_options = b'\xe0A\x02\xfaA(\n&financialservices.googleapis.com/Model'
    _globals['_PREDICTIONRESULT'].fields_by_name['end_time']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['end_time']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTIONRESULT'].fields_by_name['outputs']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['outputs']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTIONRESULT'].fields_by_name['line_of_business']._loaded_options = None
    _globals['_PREDICTIONRESULT'].fields_by_name['line_of_business']._serialized_options = b'\xe0A\x03'
    _globals['_PREDICTIONRESULT']._loaded_options = None
    _globals['_PREDICTIONRESULT']._serialized_options = b'\xeaA\x9b\x01\n1financialservices.googleapis.com/PredictionResult\x12fprojects/{project_num}/locations/{location}/instances/{instance}/predictionResults/{prediction_result}'
    _globals['_LISTPREDICTIONRESULTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTPREDICTIONRESULTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_GETPREDICTIONRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETPREDICTIONRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult'
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA+\n)financialservices.googleapis.com/Instance'
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result_id']._loaded_options = None
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result']._loaded_options = None
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_CREATEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result']._loaded_options = None
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['prediction_result']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_UPDATEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEPREDICTIONRESULTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEPREDICTIONRESULTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult'
    _globals['_DELETEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_DELETEPREDICTIONRESULTREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01'
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST'].fields_by_name['prediction_result']._loaded_options = None
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST'].fields_by_name['prediction_result']._serialized_options = b'\xe0A\x02\xfaA3\n1financialservices.googleapis.com/PredictionResult'
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._loaded_options = None
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST'].fields_by_name['structured_metadata_destination']._serialized_options = b'\xe0A\x02'
    _globals['_PREDICTIONRESULT']._serialized_start = 344
    _globals['_PREDICTIONRESULT']._serialized_end = 1515
    _globals['_PREDICTIONRESULT_OUTPUTS']._serialized_start = 1026
    _globals['_PREDICTIONRESULT_OUTPUTS']._serialized_end = 1220
    _globals['_PREDICTIONRESULT_LABELSENTRY']._serialized_start = 1222
    _globals['_PREDICTIONRESULT_LABELSENTRY']._serialized_end = 1267
    _globals['_PREDICTIONRESULT_STATE']._serialized_start = 1269
    _globals['_PREDICTIONRESULT_STATE']._serialized_end = 1353
    _globals['_LISTPREDICTIONRESULTSREQUEST']._serialized_start = 1518
    _globals['_LISTPREDICTIONRESULTSREQUEST']._serialized_end = 1688
    _globals['_LISTPREDICTIONRESULTSRESPONSE']._serialized_start = 1691
    _globals['_LISTPREDICTIONRESULTSRESPONSE']._serialized_end = 1849
    _globals['_GETPREDICTIONRESULTREQUEST']._serialized_start = 1851
    _globals['_GETPREDICTIONRESULTREQUEST']._serialized_end = 1952
    _globals['_CREATEPREDICTIONRESULTREQUEST']._serialized_start = 1955
    _globals['_CREATEPREDICTIONRESULTREQUEST']._serialized_end = 2198
    _globals['_UPDATEPREDICTIONRESULTREQUEST']._serialized_start = 2201
    _globals['_UPDATEPREDICTIONRESULTREQUEST']._serialized_end = 2396
    _globals['_DELETEPREDICTIONRESULTREQUEST']._serialized_start = 2399
    _globals['_DELETEPREDICTIONRESULTREQUEST']._serialized_end = 2528
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST']._serialized_start = 2531
    _globals['_EXPORTPREDICTIONRESULTMETADATAREQUEST']._serialized_end = 2758
    _globals['_EXPORTPREDICTIONRESULTMETADATARESPONSE']._serialized_start = 2760
    _globals['_EXPORTPREDICTIONRESULTMETADATARESPONSE']._serialized_end = 2800