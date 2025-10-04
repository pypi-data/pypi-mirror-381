"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/storage/v1/storage.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1 import arrow_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_arrow__pb2
from ......google.cloud.bigquery.storage.v1 import avro_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_avro__pb2
from ......google.cloud.bigquery.storage.v1 import protobuf_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_protobuf__pb2
from ......google.cloud.bigquery.storage.v1 import stream_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_stream__pb2
from ......google.cloud.bigquery.storage.v1 import table_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_table__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/cloud/bigquery/storage/v1/storage.proto\x12 google.cloud.bigquery.storage.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/bigquery/storage/v1/arrow.proto\x1a+google/cloud/bigquery/storage/v1/avro.proto\x1a/google/cloud/bigquery/storage/v1/protobuf.proto\x1a-google/cloud/bigquery/storage/v1/stream.proto\x1a,google/cloud/bigquery/storage/v1/table.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x17google/rpc/status.proto"\xe7\x01\n\x18CreateReadSessionRequest\x12C\n\x06parent\x18\x01 \x01(\tB3\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project\x12H\n\x0cread_session\x18\x02 \x01(\x0b2-.google.cloud.bigquery.storage.v1.ReadSessionB\x03\xe0A\x02\x12\x18\n\x10max_stream_count\x18\x03 \x01(\x05\x12"\n\x1apreferred_min_stream_count\x18\x04 \x01(\x05"i\n\x0fReadRowsRequest\x12F\n\x0bread_stream\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream\x12\x0e\n\x06offset\x18\x02 \x01(\x03")\n\rThrottleState\x12\x18\n\x10throttle_percent\x18\x01 \x01(\x05"\x97\x01\n\x0bStreamStats\x12H\n\x08progress\x18\x02 \x01(\x0b26.google.cloud.bigquery.storage.v1.StreamStats.Progress\x1a>\n\x08Progress\x12\x19\n\x11at_response_start\x18\x01 \x01(\x01\x12\x17\n\x0fat_response_end\x18\x02 \x01(\x01"\xac\x04\n\x10ReadRowsResponse\x12?\n\tavro_rows\x18\x03 \x01(\x0b2*.google.cloud.bigquery.storage.v1.AvroRowsH\x00\x12P\n\x12arrow_record_batch\x18\x04 \x01(\x0b22.google.cloud.bigquery.storage.v1.ArrowRecordBatchH\x00\x12\x11\n\trow_count\x18\x06 \x01(\x03\x12<\n\x05stats\x18\x02 \x01(\x0b2-.google.cloud.bigquery.storage.v1.StreamStats\x12G\n\x0ethrottle_state\x18\x05 \x01(\x0b2/.google.cloud.bigquery.storage.v1.ThrottleState\x12H\n\x0bavro_schema\x18\x07 \x01(\x0b2,.google.cloud.bigquery.storage.v1.AvroSchemaB\x03\xe0A\x03H\x01\x12J\n\x0carrow_schema\x18\x08 \x01(\x0b2-.google.cloud.bigquery.storage.v1.ArrowSchemaB\x03\xe0A\x03H\x01\x12(\n\x16uncompressed_byte_size\x18\t \x01(\x03B\x03\xe0A\x01H\x02\x88\x01\x01B\x06\n\x04rowsB\x08\n\x06schemaB\x19\n\x17_uncompressed_byte_size"k\n\x16SplitReadStreamRequest\x12?\n\x04name\x18\x01 \x01(\tB1\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream\x12\x10\n\x08fraction\x18\x02 \x01(\x01"\xa7\x01\n\x17SplitReadStreamResponse\x12D\n\x0eprimary_stream\x18\x01 \x01(\x0b2,.google.cloud.bigquery.storage.v1.ReadStream\x12F\n\x10remainder_stream\x18\x02 \x01(\x0b2,.google.cloud.bigquery.storage.v1.ReadStream"\x9b\x01\n\x18CreateWriteStreamRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12H\n\x0cwrite_stream\x18\x02 \x01(\x0b2-.google.cloud.bigquery.storage.v1.WriteStreamB\x03\xe0A\x02"\xf8\x08\n\x11AppendRowsRequest\x12H\n\x0cwrite_stream\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream\x12+\n\x06offset\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64Value\x12S\n\nproto_rows\x18\x04 \x01(\x0b2=.google.cloud.bigquery.storage.v1.AppendRowsRequest.ProtoDataH\x00\x12S\n\narrow_rows\x18\x05 \x01(\x0b2=.google.cloud.bigquery.storage.v1.AppendRowsRequest.ArrowDataH\x00\x12\x10\n\x08trace_id\x18\x06 \x01(\t\x12{\n\x1dmissing_value_interpretations\x18\x07 \x03(\x0b2T.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretationsEntry\x12\x81\x01\n$default_missing_value_interpretation\x18\x08 \x01(\x0e2N.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretationB\x03\xe0A\x01\x1a\x93\x01\n\tArrowData\x12D\n\rwriter_schema\x18\x01 \x01(\x0b2-.google.cloud.bigquery.storage.v1.ArrowSchema\x12@\n\x04rows\x18\x02 \x01(\x0b22.google.cloud.bigquery.storage.v1.ArrowRecordBatch\x1a\x8c\x01\n\tProtoData\x12D\n\rwriter_schema\x18\x01 \x01(\x0b2-.google.cloud.bigquery.storage.v1.ProtoSchema\x129\n\x04rows\x18\x02 \x01(\x0b2+.google.cloud.bigquery.storage.v1.ProtoRows\x1a\x92\x01\n MissingValueInterpretationsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12]\n\x05value\x18\x02 \x01(\x0e2N.google.cloud.bigquery.storage.v1.AppendRowsRequest.MissingValueInterpretation:\x028\x01"m\n\x1aMissingValueInterpretation\x12,\n(MISSING_VALUE_INTERPRETATION_UNSPECIFIED\x10\x00\x12\x0e\n\nNULL_VALUE\x10\x01\x12\x11\n\rDEFAULT_VALUE\x10\x02B\x06\n\x04rows"\xfb\x02\n\x12AppendRowsResponse\x12Z\n\rappend_result\x18\x01 \x01(\x0b2A.google.cloud.bigquery.storage.v1.AppendRowsResponse.AppendResultH\x00\x12#\n\x05error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00\x12E\n\x0eupdated_schema\x18\x03 \x01(\x0b2-.google.cloud.bigquery.storage.v1.TableSchema\x12>\n\nrow_errors\x18\x04 \x03(\x0b2*.google.cloud.bigquery.storage.v1.RowError\x12\x14\n\x0cwrite_stream\x18\x05 \x01(\t\x1a;\n\x0cAppendResult\x12+\n\x06offset\x18\x01 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\n\n\x08response"\x9a\x01\n\x15GetWriteStreamRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream\x12?\n\x04view\x18\x03 \x01(\x0e21.google.cloud.bigquery.storage.v1.WriteStreamView"s\n\x1eBatchCommitWriteStreamsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\x1a\n\rwrite_streams\x18\x02 \x03(\tB\x03\xe0A\x02"\x99\x01\n\x1fBatchCommitWriteStreamsResponse\x12/\n\x0bcommit_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12E\n\rstream_errors\x18\x02 \x03(\x0b2..google.cloud.bigquery.storage.v1.StorageError"^\n\x1aFinalizeWriteStreamRequest\x12@\n\x04name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream"0\n\x1bFinalizeWriteStreamResponse\x12\x11\n\trow_count\x18\x01 \x01(\x03"\x89\x01\n\x10FlushRowsRequest\x12H\n\x0cwrite_stream\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream\x12+\n\x06offset\x18\x02 \x01(\x0b2\x1b.google.protobuf.Int64Value"#\n\x11FlushRowsResponse\x12\x0e\n\x06offset\x18\x01 \x01(\x03"\xa4\x04\n\x0cStorageError\x12M\n\x04code\x18\x01 \x01(\x0e2?.google.cloud.bigquery.storage.v1.StorageError.StorageErrorCode\x12\x0e\n\x06entity\x18\x02 \x01(\t\x12\x15\n\rerror_message\x18\x03 \x01(\t"\x9d\x03\n\x10StorageErrorCode\x12"\n\x1eSTORAGE_ERROR_CODE_UNSPECIFIED\x10\x00\x12\x13\n\x0fTABLE_NOT_FOUND\x10\x01\x12\x1c\n\x18STREAM_ALREADY_COMMITTED\x10\x02\x12\x14\n\x10STREAM_NOT_FOUND\x10\x03\x12\x17\n\x13INVALID_STREAM_TYPE\x10\x04\x12\x18\n\x14INVALID_STREAM_STATE\x10\x05\x12\x14\n\x10STREAM_FINALIZED\x10\x06\x12 \n\x1cSCHEMA_MISMATCH_EXTRA_FIELDS\x10\x07\x12\x19\n\x15OFFSET_ALREADY_EXISTS\x10\x08\x12\x17\n\x13OFFSET_OUT_OF_RANGE\x10\t\x12\x15\n\x11CMEK_NOT_PROVIDED\x10\n\x12\x19\n\x15INVALID_CMEK_PROVIDED\x10\x0b\x12\x19\n\x15CMEK_ENCRYPTION_ERROR\x10\x0c\x12\x15\n\x11KMS_SERVICE_ERROR\x10\r\x12\x19\n\x15KMS_PERMISSION_DENIED\x10\x0e"\xb3\x01\n\x08RowError\x12\r\n\x05index\x18\x01 \x01(\x03\x12E\n\x04code\x18\x02 \x01(\x0e27.google.cloud.bigquery.storage.v1.RowError.RowErrorCode\x12\x0f\n\x07message\x18\x03 \x01(\t"@\n\x0cRowErrorCode\x12\x1e\n\x1aROW_ERROR_CODE_UNSPECIFIED\x10\x00\x12\x10\n\x0cFIELDS_ERROR\x10\x012\x92\x06\n\x0cBigQueryRead\x12\xe9\x01\n\x11CreateReadSession\x12:.google.cloud.bigquery.storage.v1.CreateReadSessionRequest\x1a-.google.cloud.bigquery.storage.v1.ReadSession"i\xdaA$parent,read_session,max_stream_count\x82\xd3\xe4\x93\x02<"7/v1/{read_session.table=projects/*/datasets/*/tables/*}:\x01*\x12\xcf\x01\n\x08ReadRows\x121.google.cloud.bigquery.storage.v1.ReadRowsRequest\x1a2.google.cloud.bigquery.storage.v1.ReadRowsResponse"Z\xdaA\x12read_stream,offset\x82\xd3\xe4\x93\x02?\x12=/v1/{read_stream=projects/*/locations/*/sessions/*/streams/*}0\x01\x12\xc6\x01\n\x0fSplitReadStream\x128.google.cloud.bigquery.storage.v1.SplitReadStreamRequest\x1a9.google.cloud.bigquery.storage.v1.SplitReadStreamResponse">\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/sessions/*/streams/*}\x1a{\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform2\xbc\x0b\n\rBigQueryWrite\x12\xd7\x01\n\x11CreateWriteStream\x12:.google.cloud.bigquery.storage.v1.CreateWriteStreamRequest\x1a-.google.cloud.bigquery.storage.v1.WriteStream"W\xdaA\x13parent,write_stream\x82\xd3\xe4\x93\x02;"+/v1/{parent=projects/*/datasets/*/tables/*}:\x0cwrite_stream\x12\xd2\x01\n\nAppendRows\x123.google.cloud.bigquery.storage.v1.AppendRowsRequest\x1a4.google.cloud.bigquery.storage.v1.AppendRowsResponse"U\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02@";/v1/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*(\x010\x01\x12\xbf\x01\n\x0eGetWriteStream\x127.google.cloud.bigquery.storage.v1.GetWriteStreamRequest\x1a-.google.cloud.bigquery.storage.v1.WriteStream"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*\x12\xd9\x01\n\x13FinalizeWriteStream\x12<.google.cloud.bigquery.storage.v1.FinalizeWriteStreamRequest\x1a=.google.cloud.bigquery.storage.v1.FinalizeWriteStreamResponse"E\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*\x12\xdc\x01\n\x17BatchCommitWriteStreams\x12@.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsRequest\x1aA.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponse"<\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/datasets/*/tables/*}\x12\xcb\x01\n\tFlushRows\x122.google.cloud.bigquery.storage.v1.FlushRowsRequest\x1a3.google.cloud.bigquery.storage.v1.FlushRowsResponse"U\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02@";/v1/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*\x1a\xb0\x01\xcaA\x1ebigquerystorage.googleapis.com\xd2A\x8b\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/bigquery.insertdata,https://www.googleapis.com/auth/cloud-platformB\x94\x02\n$com.google.cloud.bigquery.storage.v1B\x0cStorageProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1.storage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.storage.v1B\x0cStorageProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA-\n+cloudresourcemanager.googleapis.com/Project'
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['read_session']._loaded_options = None
    _globals['_CREATEREADSESSIONREQUEST'].fields_by_name['read_session']._serialized_options = b'\xe0A\x02'
    _globals['_READROWSREQUEST'].fields_by_name['read_stream']._loaded_options = None
    _globals['_READROWSREQUEST'].fields_by_name['read_stream']._serialized_options = b'\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream'
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['avro_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['arrow_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READROWSRESPONSE'].fields_by_name['uncompressed_byte_size']._loaded_options = None
    _globals['_READROWSRESPONSE'].fields_by_name['uncompressed_byte_size']._serialized_options = b'\xe0A\x01'
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_SPLITREADSTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA+\n)bigquerystorage.googleapis.com/ReadStream'
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_CREATEWRITESTREAMREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATIONSENTRY']._loaded_options = None
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATIONSENTRY']._serialized_options = b'8\x01'
    _globals['_APPENDROWSREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_APPENDROWSREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_APPENDROWSREQUEST'].fields_by_name['default_missing_value_interpretation']._loaded_options = None
    _globals['_APPENDROWSREQUEST'].fields_by_name['default_missing_value_interpretation']._serialized_options = b'\xe0A\x01'
    _globals['_GETWRITESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETWRITESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['write_streams']._loaded_options = None
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST'].fields_by_name['write_streams']._serialized_options = b'\xe0A\x02'
    _globals['_FINALIZEWRITESTREAMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_FINALIZEWRITESTREAMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_FLUSHROWSREQUEST'].fields_by_name['write_stream']._loaded_options = None
    _globals['_FLUSHROWSREQUEST'].fields_by_name['write_stream']._serialized_options = b'\xe0A\x02\xfaA,\n*bigquerystorage.googleapis.com/WriteStream'
    _globals['_BIGQUERYREAD']._loaded_options = None
    _globals['_BIGQUERYREAD']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BIGQUERYREAD'].methods_by_name['CreateReadSession']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['CreateReadSession']._serialized_options = b'\xdaA$parent,read_session,max_stream_count\x82\xd3\xe4\x93\x02<"7/v1/{read_session.table=projects/*/datasets/*/tables/*}:\x01*'
    _globals['_BIGQUERYREAD'].methods_by_name['ReadRows']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['ReadRows']._serialized_options = b'\xdaA\x12read_stream,offset\x82\xd3\xe4\x93\x02?\x12=/v1/{read_stream=projects/*/locations/*/sessions/*/streams/*}'
    _globals['_BIGQUERYREAD'].methods_by_name['SplitReadStream']._loaded_options = None
    _globals['_BIGQUERYREAD'].methods_by_name['SplitReadStream']._serialized_options = b'\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/sessions/*/streams/*}'
    _globals['_BIGQUERYWRITE']._loaded_options = None
    _globals['_BIGQUERYWRITE']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2A\x8b\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/bigquery.insertdata,https://www.googleapis.com/auth/cloud-platform'
    _globals['_BIGQUERYWRITE'].methods_by_name['CreateWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['CreateWriteStream']._serialized_options = b'\xdaA\x13parent,write_stream\x82\xd3\xe4\x93\x02;"+/v1/{parent=projects/*/datasets/*/tables/*}:\x0cwrite_stream'
    _globals['_BIGQUERYWRITE'].methods_by_name['AppendRows']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['AppendRows']._serialized_options = b'\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02@";/v1/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['GetWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['GetWriteStream']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['FinalizeWriteStream']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['FinalizeWriteStream']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028"3/v1/{name=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_BIGQUERYWRITE'].methods_by_name['BatchCommitWriteStreams']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['BatchCommitWriteStreams']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02-\x12+/v1/{parent=projects/*/datasets/*/tables/*}'
    _globals['_BIGQUERYWRITE'].methods_by_name['FlushRows']._loaded_options = None
    _globals['_BIGQUERYWRITE'].methods_by_name['FlushRows']._serialized_options = b'\xdaA\x0cwrite_stream\x82\xd3\xe4\x93\x02@";/v1/{write_stream=projects/*/datasets/*/tables/*/streams/*}:\x01*'
    _globals['_CREATEREADSESSIONREQUEST']._serialized_start = 523
    _globals['_CREATEREADSESSIONREQUEST']._serialized_end = 754
    _globals['_READROWSREQUEST']._serialized_start = 756
    _globals['_READROWSREQUEST']._serialized_end = 861
    _globals['_THROTTLESTATE']._serialized_start = 863
    _globals['_THROTTLESTATE']._serialized_end = 904
    _globals['_STREAMSTATS']._serialized_start = 907
    _globals['_STREAMSTATS']._serialized_end = 1058
    _globals['_STREAMSTATS_PROGRESS']._serialized_start = 996
    _globals['_STREAMSTATS_PROGRESS']._serialized_end = 1058
    _globals['_READROWSRESPONSE']._serialized_start = 1061
    _globals['_READROWSRESPONSE']._serialized_end = 1617
    _globals['_SPLITREADSTREAMREQUEST']._serialized_start = 1619
    _globals['_SPLITREADSTREAMREQUEST']._serialized_end = 1726
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_start = 1729
    _globals['_SPLITREADSTREAMRESPONSE']._serialized_end = 1896
    _globals['_CREATEWRITESTREAMREQUEST']._serialized_start = 1899
    _globals['_CREATEWRITESTREAMREQUEST']._serialized_end = 2054
    _globals['_APPENDROWSREQUEST']._serialized_start = 2057
    _globals['_APPENDROWSREQUEST']._serialized_end = 3201
    _globals['_APPENDROWSREQUEST_ARROWDATA']._serialized_start = 2643
    _globals['_APPENDROWSREQUEST_ARROWDATA']._serialized_end = 2790
    _globals['_APPENDROWSREQUEST_PROTODATA']._serialized_start = 2793
    _globals['_APPENDROWSREQUEST_PROTODATA']._serialized_end = 2933
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATIONSENTRY']._serialized_start = 2936
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATIONSENTRY']._serialized_end = 3082
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATION']._serialized_start = 3084
    _globals['_APPENDROWSREQUEST_MISSINGVALUEINTERPRETATION']._serialized_end = 3193
    _globals['_APPENDROWSRESPONSE']._serialized_start = 3204
    _globals['_APPENDROWSRESPONSE']._serialized_end = 3583
    _globals['_APPENDROWSRESPONSE_APPENDRESULT']._serialized_start = 3512
    _globals['_APPENDROWSRESPONSE_APPENDRESULT']._serialized_end = 3571
    _globals['_GETWRITESTREAMREQUEST']._serialized_start = 3586
    _globals['_GETWRITESTREAMREQUEST']._serialized_end = 3740
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST']._serialized_start = 3742
    _globals['_BATCHCOMMITWRITESTREAMSREQUEST']._serialized_end = 3857
    _globals['_BATCHCOMMITWRITESTREAMSRESPONSE']._serialized_start = 3860
    _globals['_BATCHCOMMITWRITESTREAMSRESPONSE']._serialized_end = 4013
    _globals['_FINALIZEWRITESTREAMREQUEST']._serialized_start = 4015
    _globals['_FINALIZEWRITESTREAMREQUEST']._serialized_end = 4109
    _globals['_FINALIZEWRITESTREAMRESPONSE']._serialized_start = 4111
    _globals['_FINALIZEWRITESTREAMRESPONSE']._serialized_end = 4159
    _globals['_FLUSHROWSREQUEST']._serialized_start = 4162
    _globals['_FLUSHROWSREQUEST']._serialized_end = 4299
    _globals['_FLUSHROWSRESPONSE']._serialized_start = 4301
    _globals['_FLUSHROWSRESPONSE']._serialized_end = 4336
    _globals['_STORAGEERROR']._serialized_start = 4339
    _globals['_STORAGEERROR']._serialized_end = 4887
    _globals['_STORAGEERROR_STORAGEERRORCODE']._serialized_start = 4474
    _globals['_STORAGEERROR_STORAGEERRORCODE']._serialized_end = 4887
    _globals['_ROWERROR']._serialized_start = 4890
    _globals['_ROWERROR']._serialized_end = 5069
    _globals['_ROWERROR_ROWERRORCODE']._serialized_start = 5005
    _globals['_ROWERROR_ROWERRORCODE']._serialized_end = 5069
    _globals['_BIGQUERYREAD']._serialized_start = 5072
    _globals['_BIGQUERYREAD']._serialized_end = 5858
    _globals['_BIGQUERYWRITE']._serialized_start = 5861
    _globals['_BIGQUERYWRITE']._serialized_end = 7329