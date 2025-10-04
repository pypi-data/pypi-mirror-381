"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/lustre/v1/transfer.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/cloud/lustre/v1/transfer.proto\x12\x16google.cloud.lustre.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\xb7\x02\n\x11ImportDataRequest\x123\n\x08gcs_path\x18\x02 \x01(\x0b2\x1f.google.cloud.lustre.v1.GcsPathH\x00\x129\n\x0blustre_path\x18\x03 \x01(\x0b2".google.cloud.lustre.v1.LustrePathH\x01\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12B\n\x0fservice_account\x18\x05 \x01(\tB)\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccountB\x08\n\x06sourceB\r\n\x0bdestination"\xb7\x02\n\x11ExportDataRequest\x129\n\x0blustre_path\x18\x02 \x01(\x0b2".google.cloud.lustre.v1.LustrePathH\x00\x123\n\x08gcs_path\x18\x03 \x01(\x0b2\x1f.google.cloud.lustre.v1.GcsPathH\x01\x124\n\x04name\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance\x12\x1f\n\nrequest_id\x18\x04 \x01(\tB\x0b\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12B\n\x0fservice_account\x18\x05 \x01(\tB)\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccountB\x08\n\x06sourceB\r\n\x0bdestination"\x14\n\x12ExportDataResponse"\x14\n\x12ImportDataResponse"\xd0\x02\n\x12ExportDataMetadata\x12M\n\x12operation_metadata\x18\x01 \x01(\x0b21.google.cloud.lustre.v1.TransferOperationMetadata\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04verb\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x06 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x08 \x01(\tB\x03\xe0A\x03"\xbd\x02\n\x12ImportDataMetadata\x12M\n\x12operation_metadata\x18\x01 \x01(\x0b21.google.cloud.lustre.v1.TransferOperationMetadata\x124\n\x0bcreate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x121\n\x08end_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12\x13\n\x06target\x18\x04 \x01(\tB\x03\xe0A\x03\x12\x1b\n\x0estatus_message\x18\x06 \x01(\tB\x03\xe0A\x03\x12#\n\x16requested_cancellation\x18\x07 \x01(\x08B\x03\xe0A\x03\x12\x18\n\x0bapi_version\x18\x08 \x01(\tB\x03\xe0A\x03"\x1b\n\x07GcsPath\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02"\x1f\n\nLustrePath\x12\x11\n\x04path\x18\x01 \x01(\tB\x03\xe0A\x01"\x84\x02\n\x10TransferCounters\x12\x1b\n\x13found_objects_count\x18\x01 \x01(\x03\x12\x19\n\x11bytes_found_count\x18\x02 \x01(\x03\x12\x1d\n\x15objects_skipped_count\x18\x03 \x01(\x03\x12\x1b\n\x13bytes_skipped_count\x18\x04 \x01(\x03\x12\x1c\n\x14objects_copied_count\x18\x05 \x01(\x03\x12\x1a\n\x12bytes_copied_count\x18\x06 \x01(\x03\x12!\n\x14objects_failed_count\x18\x07 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12bytes_failed_count\x18\x08 \x01(\x03B\x03\xe0A\x03"8\n\rErrorLogEntry\x12\x10\n\x03uri\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x15\n\rerror_details\x18\x02 \x03(\t"\x95\x01\n\x0cErrorSummary\x12)\n\nerror_code\x18\x01 \x01(\x0e2\x10.google.rpc.CodeB\x03\xe0A\x02\x12\x18\n\x0berror_count\x18\x02 \x01(\x03B\x03\xe0A\x02\x12@\n\x11error_log_entries\x18\x03 \x03(\x0b2%.google.cloud.lustre.v1.ErrorLogEntry"\x95\x04\n\x19TransferOperationMetadata\x12E\n\x12source_lustre_path\x18\x03 \x01(\x0b2".google.cloud.lustre.v1.LustrePathB\x03\xe0A\x03H\x00\x12?\n\x0fsource_gcs_path\x18\x04 \x01(\x0b2\x1f.google.cloud.lustre.v1.GcsPathB\x03\xe0A\x03H\x00\x12D\n\x14destination_gcs_path\x18\x05 \x01(\x0b2\x1f.google.cloud.lustre.v1.GcsPathB\x03\xe0A\x03H\x01\x12J\n\x17destination_lustre_path\x18\x06 \x01(\x0b2".google.cloud.lustre.v1.LustrePathB\x03\xe0A\x03H\x01\x12?\n\x08counters\x18\x01 \x01(\x0b2(.google.cloud.lustre.v1.TransferCountersB\x03\xe0A\x03\x12@\n\rtransfer_type\x18\x02 \x01(\x0e2$.google.cloud.lustre.v1.TransferTypeB\x03\xe0A\x03\x12B\n\x0ferror_summaries\x18\x07 \x03(\x0b2$.google.cloud.lustre.v1.ErrorSummaryB\x03\xe0A\x03B\x08\n\x06sourceB\r\n\x0bdestination*E\n\x0cTransferType\x12\x1d\n\x19TRANSFER_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06IMPORT\x10\x01\x12\n\n\x06EXPORT\x10\x02Ba\n\x1acom.google.cloud.lustre.v1B\rTransferProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.lustre.v1.transfer_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1acom.google.cloud.lustre.v1B\rTransferProtoP\x01Z2cloud.google.com/go/lustre/apiv1/lustrepb;lustrepb'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_IMPORTDATAREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_IMPORTDATAREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA \n\x1elustre.googleapis.com/Instance'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['request_id']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['request_id']._serialized_options = b'\xe0A\x01\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_EXPORTDATAREQUEST'].fields_by_name['service_account']._loaded_options = None
    _globals['_EXPORTDATAREQUEST'].fields_by_name['service_account']._serialized_options = b'\xe0A\x01\xfaA#\n!iam.googleapis.com/ServiceAccount'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['verb']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['verb']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_EXPORTDATAMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_EXPORTDATAMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['create_time']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['end_time']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['target']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['target']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['status_message']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['status_message']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['requested_cancellation']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['requested_cancellation']._serialized_options = b'\xe0A\x03'
    _globals['_IMPORTDATAMETADATA'].fields_by_name['api_version']._loaded_options = None
    _globals['_IMPORTDATAMETADATA'].fields_by_name['api_version']._serialized_options = b'\xe0A\x03'
    _globals['_GCSPATH'].fields_by_name['uri']._loaded_options = None
    _globals['_GCSPATH'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_LUSTREPATH'].fields_by_name['path']._loaded_options = None
    _globals['_LUSTREPATH'].fields_by_name['path']._serialized_options = b'\xe0A\x01'
    _globals['_TRANSFERCOUNTERS'].fields_by_name['objects_failed_count']._loaded_options = None
    _globals['_TRANSFERCOUNTERS'].fields_by_name['objects_failed_count']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERCOUNTERS'].fields_by_name['bytes_failed_count']._loaded_options = None
    _globals['_TRANSFERCOUNTERS'].fields_by_name['bytes_failed_count']._serialized_options = b'\xe0A\x03'
    _globals['_ERRORLOGENTRY'].fields_by_name['uri']._loaded_options = None
    _globals['_ERRORLOGENTRY'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORSUMMARY'].fields_by_name['error_code']._loaded_options = None
    _globals['_ERRORSUMMARY'].fields_by_name['error_code']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORSUMMARY'].fields_by_name['error_count']._loaded_options = None
    _globals['_ERRORSUMMARY'].fields_by_name['error_count']._serialized_options = b'\xe0A\x02'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_lustre_path']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_lustre_path']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_gcs_path']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['source_gcs_path']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_gcs_path']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_gcs_path']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_lustre_path']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['destination_lustre_path']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['counters']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['counters']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['transfer_type']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['transfer_type']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['error_summaries']._loaded_options = None
    _globals['_TRANSFEROPERATIONMETADATA'].fields_by_name['error_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_TRANSFERTYPE']._serialized_start = 2612
    _globals['_TRANSFERTYPE']._serialized_end = 2681
    _globals['_IMPORTDATAREQUEST']._serialized_start = 211
    _globals['_IMPORTDATAREQUEST']._serialized_end = 522
    _globals['_EXPORTDATAREQUEST']._serialized_start = 525
    _globals['_EXPORTDATAREQUEST']._serialized_end = 836
    _globals['_EXPORTDATARESPONSE']._serialized_start = 838
    _globals['_EXPORTDATARESPONSE']._serialized_end = 858
    _globals['_IMPORTDATARESPONSE']._serialized_start = 860
    _globals['_IMPORTDATARESPONSE']._serialized_end = 880
    _globals['_EXPORTDATAMETADATA']._serialized_start = 883
    _globals['_EXPORTDATAMETADATA']._serialized_end = 1219
    _globals['_IMPORTDATAMETADATA']._serialized_start = 1222
    _globals['_IMPORTDATAMETADATA']._serialized_end = 1539
    _globals['_GCSPATH']._serialized_start = 1541
    _globals['_GCSPATH']._serialized_end = 1568
    _globals['_LUSTREPATH']._serialized_start = 1570
    _globals['_LUSTREPATH']._serialized_end = 1601
    _globals['_TRANSFERCOUNTERS']._serialized_start = 1604
    _globals['_TRANSFERCOUNTERS']._serialized_end = 1864
    _globals['_ERRORLOGENTRY']._serialized_start = 1866
    _globals['_ERRORLOGENTRY']._serialized_end = 1922
    _globals['_ERRORSUMMARY']._serialized_start = 1925
    _globals['_ERRORSUMMARY']._serialized_end = 2074
    _globals['_TRANSFEROPERATIONMETADATA']._serialized_start = 2077
    _globals['_TRANSFEROPERATIONMETADATA']._serialized_end = 2610