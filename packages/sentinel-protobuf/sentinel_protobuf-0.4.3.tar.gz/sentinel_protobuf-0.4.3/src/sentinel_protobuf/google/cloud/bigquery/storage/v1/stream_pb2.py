"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/storage/v1/stream.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1 import arrow_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_arrow__pb2
from ......google.cloud.bigquery.storage.v1 import avro_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_avro__pb2
from ......google.cloud.bigquery.storage.v1 import table_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1_dot_table__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-google/cloud/bigquery/storage/v1/stream.proto\x12 google.cloud.bigquery.storage.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a,google/cloud/bigquery/storage/v1/arrow.proto\x1a+google/cloud/bigquery/storage/v1/avro.proto\x1a,google/cloud/bigquery/storage/v1/table.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xc3\x0c\n\x0bReadSession\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x124\n\x0bexpire_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12F\n\x0bdata_format\x18\x03 \x01(\x0e2,.google.cloud.bigquery.storage.v1.DataFormatB\x03\xe0A\x05\x12H\n\x0bavro_schema\x18\x04 \x01(\x0b2,.google.cloud.bigquery.storage.v1.AvroSchemaB\x03\xe0A\x03H\x00\x12J\n\x0carrow_schema\x18\x05 \x01(\x0b2-.google.cloud.bigquery.storage.v1.ArrowSchemaB\x03\xe0A\x03H\x00\x124\n\x05table\x18\x06 \x01(\tB%\xe0A\x05\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12Z\n\x0ftable_modifiers\x18\x07 \x01(\x0b2<.google.cloud.bigquery.storage.v1.ReadSession.TableModifiersB\x03\xe0A\x01\x12Y\n\x0cread_options\x18\x08 \x01(\x0b2>.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptionsB\x03\xe0A\x01\x12B\n\x07streams\x18\n \x03(\x0b2,.google.cloud.bigquery.storage.v1.ReadStreamB\x03\xe0A\x03\x12*\n\x1destimated_total_bytes_scanned\x18\x0c \x01(\x03B\x03\xe0A\x03\x12/\n"estimated_total_physical_file_size\x18\x0f \x01(\x03B\x03\xe0A\x03\x12 \n\x13estimated_row_count\x18\x0e \x01(\x03B\x03\xe0A\x03\x12\x15\n\x08trace_id\x18\r \x01(\tB\x03\xe0A\x01\x1aC\n\x0eTableModifiers\x121\n\rsnapshot_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a\x89\x05\n\x10TableReadOptions\x12\x17\n\x0fselected_fields\x18\x01 \x03(\t\x12\x17\n\x0frow_restriction\x18\x02 \x01(\t\x12g\n\x1barrow_serialization_options\x18\x03 \x01(\x0b2;.google.cloud.bigquery.storage.v1.ArrowSerializationOptionsB\x03\xe0A\x01H\x00\x12e\n\x1aavro_serialization_options\x18\x04 \x01(\x0b2:.google.cloud.bigquery.storage.v1.AvroSerializationOptionsB\x03\xe0A\x01H\x00\x12#\n\x11sample_percentage\x18\x05 \x01(\x01B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x85\x01\n\x1aresponse_compression_codec\x18\x06 \x01(\x0e2W.google.cloud.bigquery.storage.v1.ReadSession.TableReadOptions.ResponseCompressionCodecB\x03\xe0A\x01H\x02\x88\x01\x01"j\n\x18ResponseCompressionCodec\x12*\n&RESPONSE_COMPRESSION_CODEC_UNSPECIFIED\x10\x00\x12"\n\x1eRESPONSE_COMPRESSION_CODEC_LZ4\x10\x02B%\n#output_format_serialization_optionsB\x14\n\x12_sample_percentageB\x1d\n\x1b_response_compression_codec:k\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}B\x08\n\x06schema"\x9c\x01\n\nReadStream\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03:{\xeaAx\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}"\xfb\x04\n\x0bWriteStream\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12E\n\x04type\x18\x02 \x01(\x0e22.google.cloud.bigquery.storage.v1.WriteStream.TypeB\x03\xe0A\x05\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bcommit_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12H\n\x0ctable_schema\x18\x05 \x01(\x0b2-.google.cloud.bigquery.storage.v1.TableSchemaB\x03\xe0A\x03\x12P\n\nwrite_mode\x18\x07 \x01(\x0e27.google.cloud.bigquery.storage.v1.WriteStream.WriteModeB\x03\xe0A\x05\x12\x15\n\x08location\x18\x08 \x01(\tB\x03\xe0A\x05"F\n\x04Type\x12\x14\n\x10TYPE_UNSPECIFIED\x10\x00\x12\r\n\tCOMMITTED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0c\n\x08BUFFERED\x10\x03"3\n\tWriteMode\x12\x1a\n\x16WRITE_MODE_UNSPECIFIED\x10\x00\x12\n\n\x06INSERT\x10\x01:v\xeaAs\n*bigquerystorage.googleapis.com/WriteStream\x12Eprojects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}*>\n\nDataFormat\x12\x1b\n\x17DATA_FORMAT_UNSPECIFIED\x10\x00\x12\x08\n\x04AVRO\x10\x01\x12\t\n\x05ARROW\x10\x02*I\n\x0fWriteStreamView\x12!\n\x1dWRITE_STREAM_VIEW_UNSPECIFIED\x10\x00\x12\t\n\x05BASIC\x10\x01\x12\x08\n\x04FULL\x10\x02B\xbb\x01\n$com.google.cloud.bigquery.storage.v1B\x0bStreamProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1.stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.bigquery.storage.v1B\x0bStreamProtoP\x01Z>cloud.google.com/go/bigquery/storage/apiv1/storagepb;storagepb\xaa\x02 Google.Cloud.BigQuery.Storage.V1\xca\x02 Google\\Cloud\\BigQuery\\Storage\\V1'
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['arrow_serialization_options']._loaded_options = None
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['arrow_serialization_options']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['avro_serialization_options']._loaded_options = None
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['avro_serialization_options']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['sample_percentage']._loaded_options = None
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['sample_percentage']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['response_compression_codec']._loaded_options = None
    _globals['_READSESSION_TABLEREADOPTIONS'].fields_by_name['response_compression_codec']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['name']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['expire_time']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['expire_time']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['data_format']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['data_format']._serialized_options = b'\xe0A\x05'
    _globals['_READSESSION'].fields_by_name['avro_schema']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['avro_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['arrow_schema']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['arrow_schema']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['table']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['table']._serialized_options = b'\xe0A\x05\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_READSESSION'].fields_by_name['table_modifiers']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['table_modifiers']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['read_options']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['read_options']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION'].fields_by_name['streams']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['streams']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['estimated_total_bytes_scanned']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['estimated_total_bytes_scanned']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['estimated_total_physical_file_size']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['estimated_total_physical_file_size']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['estimated_row_count']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['estimated_row_count']._serialized_options = b'\xe0A\x03'
    _globals['_READSESSION'].fields_by_name['trace_id']._loaded_options = None
    _globals['_READSESSION'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x01'
    _globals['_READSESSION']._loaded_options = None
    _globals['_READSESSION']._serialized_options = b'\xeaAh\n*bigquerystorage.googleapis.com/ReadSession\x12:projects/{project}/locations/{location}/sessions/{session}'
    _globals['_READSTREAM'].fields_by_name['name']._loaded_options = None
    _globals['_READSTREAM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_READSTREAM']._loaded_options = None
    _globals['_READSTREAM']._serialized_options = b'\xeaAx\n)bigquerystorage.googleapis.com/ReadStream\x12Kprojects/{project}/locations/{location}/sessions/{session}/streams/{stream}'
    _globals['_WRITESTREAM'].fields_by_name['name']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['type']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['type']._serialized_options = b'\xe0A\x05'
    _globals['_WRITESTREAM'].fields_by_name['create_time']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['commit_time']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['commit_time']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['table_schema']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['table_schema']._serialized_options = b'\xe0A\x03'
    _globals['_WRITESTREAM'].fields_by_name['write_mode']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['write_mode']._serialized_options = b'\xe0A\x05'
    _globals['_WRITESTREAM'].fields_by_name['location']._loaded_options = None
    _globals['_WRITESTREAM'].fields_by_name['location']._serialized_options = b'\xe0A\x05'
    _globals['_WRITESTREAM']._loaded_options = None
    _globals['_WRITESTREAM']._serialized_options = b'\xeaAs\n*bigquerystorage.googleapis.com/WriteStream\x12Eprojects/{project}/datasets/{dataset}/tables/{table}/streams/{stream}'
    _globals['_DATAFORMAT']._serialized_start = 2716
    _globals['_DATAFORMAT']._serialized_end = 2778
    _globals['_WRITESTREAMVIEW']._serialized_start = 2780
    _globals['_WRITESTREAMVIEW']._serialized_end = 2853
    _globals['_READSESSION']._serialized_start = 314
    _globals['_READSESSION']._serialized_end = 1917
    _globals['_READSESSION_TABLEMODIFIERS']._serialized_start = 1079
    _globals['_READSESSION_TABLEMODIFIERS']._serialized_end = 1146
    _globals['_READSESSION_TABLEREADOPTIONS']._serialized_start = 1149
    _globals['_READSESSION_TABLEREADOPTIONS']._serialized_end = 1798
    _globals['_READSESSION_TABLEREADOPTIONS_RESPONSECOMPRESSIONCODEC']._serialized_start = 1600
    _globals['_READSESSION_TABLEREADOPTIONS_RESPONSECOMPRESSIONCODEC']._serialized_end = 1706
    _globals['_READSTREAM']._serialized_start = 1920
    _globals['_READSTREAM']._serialized_end = 2076
    _globals['_WRITESTREAM']._serialized_start = 2079
    _globals['_WRITESTREAM']._serialized_end = 2714
    _globals['_WRITESTREAM_TYPE']._serialized_start = 2471
    _globals['_WRITESTREAM_TYPE']._serialized_end = 2541
    _globals['_WRITESTREAM_WRITEMODE']._serialized_start = 2543
    _globals['_WRITESTREAM_WRITEMODE']._serialized_end = 2594