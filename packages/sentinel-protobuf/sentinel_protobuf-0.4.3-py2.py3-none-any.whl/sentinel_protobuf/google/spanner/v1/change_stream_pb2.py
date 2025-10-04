"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/spanner/v1/change_stream.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.spanner.v1 import type_pb2 as google_dot_spanner_dot_v1_dot_type__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%google/spanner/v1/change_stream.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/spanner/v1/type.proto"\x96\x14\n\x12ChangeStreamRecord\x12T\n\x12data_change_record\x18\x01 \x01(\x0b26.google.spanner.v1.ChangeStreamRecord.DataChangeRecordH\x00\x12Q\n\x10heartbeat_record\x18\x02 \x01(\x0b25.google.spanner.v1.ChangeStreamRecord.HeartbeatRecordH\x00\x12\\\n\x16partition_start_record\x18\x03 \x01(\x0b2:.google.spanner.v1.ChangeStreamRecord.PartitionStartRecordH\x00\x12X\n\x14partition_end_record\x18\x04 \x01(\x0b28.google.spanner.v1.ChangeStreamRecord.PartitionEndRecordH\x00\x12\\\n\x16partition_event_record\x18\x05 \x01(\x0b2:.google.spanner.v1.ChangeStreamRecord.PartitionEventRecordH\x00\x1a\xd2\n\n\x10DataChangeRecord\x124\n\x10commit_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0frecord_sequence\x18\x02 \x01(\t\x12\x1d\n\x15server_transaction_id\x18\x03 \x01(\t\x122\n*is_last_record_in_transaction_in_partition\x18\x04 \x01(\x08\x12\r\n\x05table\x18\x05 \x01(\t\x12^\n\x0fcolumn_metadata\x18\x06 \x03(\x0b2E.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ColumnMetadata\x12H\n\x04mods\x18\x07 \x03(\x0b2:.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.Mod\x12P\n\x08mod_type\x18\x08 \x01(\x0e2>.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModType\x12c\n\x12value_capture_type\x18\t \x01(\x0e2G.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ValueCaptureType\x12(\n number_of_records_in_transaction\x18\n \x01(\x05\x12+\n#number_of_partitions_in_transaction\x18\x0b \x01(\x05\x12\x17\n\x0ftransaction_tag\x18\x0c \x01(\t\x12\x1d\n\x15is_system_transaction\x18\r \x01(\x08\x1aw\n\x0eColumnMetadata\x12\x0c\n\x04name\x18\x01 \x01(\t\x12%\n\x04type\x18\x02 \x01(\x0b2\x17.google.spanner.v1.Type\x12\x16\n\x0eis_primary_key\x18\x03 \x01(\x08\x12\x18\n\x10ordinal_position\x18\x04 \x01(\x03\x1aP\n\x08ModValue\x12\x1d\n\x15column_metadata_index\x18\x01 \x01(\x05\x12%\n\x05value\x18\x02 \x01(\x0b2\x16.google.protobuf.Value\x1a\xfe\x01\n\x03Mod\x12M\n\x04keys\x18\x01 \x03(\x0b2?.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModValue\x12S\n\nold_values\x18\x02 \x03(\x0b2?.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModValue\x12S\n\nnew_values\x18\x03 \x03(\x0b2?.google.spanner.v1.ChangeStreamRecord.DataChangeRecord.ModValue"G\n\x07ModType\x12\x18\n\x14MOD_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06INSERT\x10\n\x12\n\n\x06UPDATE\x10\x14\x12\n\n\x06DELETE\x10\x1e"\x87\x01\n\x10ValueCaptureType\x12"\n\x1eVALUE_CAPTURE_TYPE_UNSPECIFIED\x10\x00\x12\x16\n\x12OLD_AND_NEW_VALUES\x10\n\x12\x0e\n\nNEW_VALUES\x10\x14\x12\x0b\n\x07NEW_ROW\x10\x1e\x12\x1a\n\x16NEW_ROW_AND_OLD_VALUES\x10(\x1a@\n\x0fHeartbeatRecord\x12-\n\ttimestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x1a~\n\x14PartitionStartRecord\x123\n\x0fstart_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0frecord_sequence\x18\x02 \x01(\t\x12\x18\n\x10partition_tokens\x18\x03 \x03(\t\x1ay\n\x12PartitionEndRecord\x121\n\rend_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0frecord_sequence\x18\x02 \x01(\t\x12\x17\n\x0fpartition_token\x18\x03 \x01(\t\x1a\xa4\x03\n\x14PartitionEventRecord\x124\n\x10commit_timestamp\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x17\n\x0frecord_sequence\x18\x02 \x01(\t\x12\x17\n\x0fpartition_token\x18\x03 \x01(\t\x12^\n\x0emove_in_events\x18\x04 \x03(\x0b2F.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveInEvent\x12`\n\x0fmove_out_events\x18\x05 \x03(\x0b2G.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent\x1a-\n\x0bMoveInEvent\x12\x1e\n\x16source_partition_token\x18\x01 \x01(\t\x1a3\n\x0cMoveOutEvent\x12#\n\x1bdestination_partition_token\x18\x01 \x01(\tB\x08\n\x06recordB\xb4\x01\n\x15com.google.spanner.v1B\x11ChangeStreamProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.spanner.v1.change_stream_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x15com.google.spanner.v1B\x11ChangeStreamProtoP\x01Z5cloud.google.com/go/spanner/apiv1/spannerpb;spannerpb\xaa\x02\x17Google.Cloud.Spanner.V1\xca\x02\x17Google\\Cloud\\Spanner\\V1\xea\x02\x1aGoogle::Cloud::Spanner::V1'
    _globals['_CHANGESTREAMRECORD']._serialized_start = 154
    _globals['_CHANGESTREAMRECORD']._serialized_end = 2736
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD']._serialized_start = 624
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD']._serialized_end = 1986
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_COLUMNMETADATA']._serialized_start = 1317
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_COLUMNMETADATA']._serialized_end = 1436
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MODVALUE']._serialized_start = 1438
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MODVALUE']._serialized_end = 1518
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MOD']._serialized_start = 1521
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MOD']._serialized_end = 1775
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MODTYPE']._serialized_start = 1777
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_MODTYPE']._serialized_end = 1848
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_VALUECAPTURETYPE']._serialized_start = 1851
    _globals['_CHANGESTREAMRECORD_DATACHANGERECORD_VALUECAPTURETYPE']._serialized_end = 1986
    _globals['_CHANGESTREAMRECORD_HEARTBEATRECORD']._serialized_start = 1988
    _globals['_CHANGESTREAMRECORD_HEARTBEATRECORD']._serialized_end = 2052
    _globals['_CHANGESTREAMRECORD_PARTITIONSTARTRECORD']._serialized_start = 2054
    _globals['_CHANGESTREAMRECORD_PARTITIONSTARTRECORD']._serialized_end = 2180
    _globals['_CHANGESTREAMRECORD_PARTITIONENDRECORD']._serialized_start = 2182
    _globals['_CHANGESTREAMRECORD_PARTITIONENDRECORD']._serialized_end = 2303
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD']._serialized_start = 2306
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD']._serialized_end = 2726
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD_MOVEINEVENT']._serialized_start = 2628
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD_MOVEINEVENT']._serialized_end = 2673
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD_MOVEOUTEVENT']._serialized_start = 2675
    _globals['_CHANGESTREAMRECORD_PARTITIONEVENTRECORD_MOVEOUTEVENT']._serialized_end = 2726