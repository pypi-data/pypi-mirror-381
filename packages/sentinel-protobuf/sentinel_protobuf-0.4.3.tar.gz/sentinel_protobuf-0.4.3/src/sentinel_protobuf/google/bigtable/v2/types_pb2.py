"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/bigtable/v2/types.proto')
_sym_db = _symbol_database.Default()
from ....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1egoogle/bigtable/v2/types.proto\x12\x12google.bigtable.v2\x1a\x1fgoogle/api/field_behavior.proto"\x87\x18\n\x04Type\x124\n\nbytes_type\x18\x01 \x01(\x0b2\x1e.google.bigtable.v2.Type.BytesH\x00\x126\n\x0bstring_type\x18\x02 \x01(\x0b2\x1f.google.bigtable.v2.Type.StringH\x00\x124\n\nint64_type\x18\x05 \x01(\x0b2\x1e.google.bigtable.v2.Type.Int64H\x00\x128\n\x0cfloat32_type\x18\x0c \x01(\x0b2 .google.bigtable.v2.Type.Float32H\x00\x128\n\x0cfloat64_type\x18\t \x01(\x0b2 .google.bigtable.v2.Type.Float64H\x00\x122\n\tbool_type\x18\x08 \x01(\x0b2\x1d.google.bigtable.v2.Type.BoolH\x00\x12<\n\x0etimestamp_type\x18\n \x01(\x0b2".google.bigtable.v2.Type.TimestampH\x00\x122\n\tdate_type\x18\x0b \x01(\x0b2\x1d.google.bigtable.v2.Type.DateH\x00\x12<\n\x0eaggregate_type\x18\x06 \x01(\x0b2".google.bigtable.v2.Type.AggregateH\x00\x126\n\x0bstruct_type\x18\x07 \x01(\x0b2\x1f.google.bigtable.v2.Type.StructH\x00\x124\n\narray_type\x18\x03 \x01(\x0b2\x1e.google.bigtable.v2.Type.ArrayH\x00\x120\n\x08map_type\x18\x04 \x01(\x0b2\x1c.google.bigtable.v2.Type.MapH\x00\x124\n\nproto_type\x18\r \x01(\x0b2\x1e.google.bigtable.v2.Type.ProtoH\x00\x122\n\tenum_type\x18\x0e \x01(\x0b2\x1d.google.bigtable.v2.Type.EnumH\x00\x1a\xb3\x01\n\x05Bytes\x129\n\x08encoding\x18\x01 \x01(\x0b2\'.google.bigtable.v2.Type.Bytes.Encoding\x1ao\n\x08Encoding\x12:\n\x03raw\x18\x01 \x01(\x0b2+.google.bigtable.v2.Type.Bytes.Encoding.RawH\x00\x1a\x1b\n\x03Raw\x12\x14\n\x0cescape_nulls\x18\x01 \x01(\x08B\n\n\x08encoding\x1a\xa7\x02\n\x06String\x12:\n\x08encoding\x18\x01 \x01(\x0b2(.google.bigtable.v2.Type.String.Encoding\x1a\xe0\x01\n\x08Encoding\x12H\n\x08utf8_raw\x18\x01 \x01(\x0b20.google.bigtable.v2.Type.String.Encoding.Utf8RawB\x02\x18\x01H\x00\x12H\n\nutf8_bytes\x18\x02 \x01(\x0b22.google.bigtable.v2.Type.String.Encoding.Utf8BytesH\x00\x1a\r\n\x07Utf8Raw:\x02\x18\x01\x1a%\n\tUtf8Bytes\x12\x18\n\x10null_escape_char\x18\x01 \x01(\tB\n\n\x08encoding\x1a\xe5\x02\n\x05Int64\x129\n\x08encoding\x18\x01 \x01(\x0b2\'.google.bigtable.v2.Type.Int64.Encoding\x1a\xa0\x02\n\x08Encoding\x12R\n\x10big_endian_bytes\x18\x01 \x01(\x0b26.google.bigtable.v2.Type.Int64.Encoding.BigEndianBytesH\x00\x12V\n\x12ordered_code_bytes\x18\x02 \x01(\x0b28.google.bigtable.v2.Type.Int64.Encoding.OrderedCodeBytesH\x00\x1aH\n\x0eBigEndianBytes\x126\n\nbytes_type\x18\x01 \x01(\x0b2\x1e.google.bigtable.v2.Type.BytesB\x02\x18\x01\x1a\x12\n\x10OrderedCodeBytesB\n\n\x08encoding\x1a\x06\n\x04Bool\x1a\t\n\x07Float32\x1a\t\n\x07Float64\x1a\xa8\x01\n\tTimestamp\x12=\n\x08encoding\x18\x01 \x01(\x0b2+.google.bigtable.v2.Type.Timestamp.Encoding\x1a\\\n\x08Encoding\x12D\n\x11unix_micros_int64\x18\x01 \x01(\x0b2\'.google.bigtable.v2.Type.Int64.EncodingH\x00B\n\n\x08encoding\x1a\x06\n\x04Date\x1a\x95\x04\n\x06Struct\x125\n\x06fields\x18\x01 \x03(\x0b2%.google.bigtable.v2.Type.Struct.Field\x12:\n\x08encoding\x18\x02 \x01(\x0b2(.google.bigtable.v2.Type.Struct.Encoding\x1aC\n\x05Field\x12\x12\n\nfield_name\x18\x01 \x01(\t\x12&\n\x04type\x18\x02 \x01(\x0b2\x18.google.bigtable.v2.Type\x1a\xd2\x02\n\x08Encoding\x12G\n\tsingleton\x18\x01 \x01(\x0b22.google.bigtable.v2.Type.Struct.Encoding.SingletonH\x00\x12R\n\x0fdelimited_bytes\x18\x02 \x01(\x0b27.google.bigtable.v2.Type.Struct.Encoding.DelimitedBytesH\x00\x12W\n\x12ordered_code_bytes\x18\x03 \x01(\x0b29.google.bigtable.v2.Type.Struct.Encoding.OrderedCodeBytesH\x00\x1a\x0b\n\tSingleton\x1a#\n\x0eDelimitedBytes\x12\x11\n\tdelimiter\x18\x01 \x01(\x0c\x1a\x12\n\x10OrderedCodeBytesB\n\n\x08encoding\x1a7\n\x05Proto\x12\x18\n\x10schema_bundle_id\x18\x01 \x01(\t\x12\x14\n\x0cmessage_name\x18\x02 \x01(\t\x1a3\n\x04Enum\x12\x18\n\x10schema_bundle_id\x18\x01 \x01(\t\x12\x11\n\tenum_name\x18\x02 \x01(\t\x1a7\n\x05Array\x12.\n\x0celement_type\x18\x01 \x01(\x0b2\x18.google.bigtable.v2.Type\x1a_\n\x03Map\x12*\n\x08key_type\x18\x01 \x01(\x0b2\x18.google.bigtable.v2.Type\x12,\n\nvalue_type\x18\x02 \x01(\x0b2\x18.google.bigtable.v2.Type\x1a\xb7\x03\n\tAggregate\x12,\n\ninput_type\x18\x01 \x01(\x0b2\x18.google.bigtable.v2.Type\x121\n\nstate_type\x18\x02 \x01(\x0b2\x18.google.bigtable.v2.TypeB\x03\xe0A\x03\x125\n\x03sum\x18\x04 \x01(\x0b2&.google.bigtable.v2.Type.Aggregate.SumH\x00\x12_\n\x12hllpp_unique_count\x18\x05 \x01(\x0b2A.google.bigtable.v2.Type.Aggregate.HyperLogLogPlusPlusUniqueCountH\x00\x125\n\x03max\x18\x06 \x01(\x0b2&.google.bigtable.v2.Type.Aggregate.MaxH\x00\x125\n\x03min\x18\x07 \x01(\x0b2&.google.bigtable.v2.Type.Aggregate.MinH\x00\x1a\x05\n\x03Sum\x1a\x05\n\x03Max\x1a\x05\n\x03Min\x1a \n\x1eHyperLogLogPlusPlusUniqueCountB\x0c\n\naggregatorB\x06\n\x04kindB\xb4\x01\n\x16com.google.bigtable.v2B\nTypesProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.bigtable.v2.types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x16com.google.bigtable.v2B\nTypesProtoP\x01Z8cloud.google.com/go/bigtable/apiv2/bigtablepb;bigtablepb\xaa\x02\x18Google.Cloud.Bigtable.V2\xca\x02\x18Google\\Cloud\\Bigtable\\V2\xea\x02\x1bGoogle::Cloud::Bigtable::V2'
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._loaded_options = None
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_options = b'\x18\x01'
    _globals['_TYPE_STRING_ENCODING'].fields_by_name['utf8_raw']._loaded_options = None
    _globals['_TYPE_STRING_ENCODING'].fields_by_name['utf8_raw']._serialized_options = b'\x18\x01'
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES'].fields_by_name['bytes_type']._loaded_options = None
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES'].fields_by_name['bytes_type']._serialized_options = b'\x18\x01'
    _globals['_TYPE_AGGREGATE'].fields_by_name['state_type']._loaded_options = None
    _globals['_TYPE_AGGREGATE'].fields_by_name['state_type']._serialized_options = b'\xe0A\x03'
    _globals['_TYPE']._serialized_start = 88
    _globals['_TYPE']._serialized_end = 3167
    _globals['_TYPE_BYTES']._serialized_start = 871
    _globals['_TYPE_BYTES']._serialized_end = 1050
    _globals['_TYPE_BYTES_ENCODING']._serialized_start = 939
    _globals['_TYPE_BYTES_ENCODING']._serialized_end = 1050
    _globals['_TYPE_BYTES_ENCODING_RAW']._serialized_start = 1011
    _globals['_TYPE_BYTES_ENCODING_RAW']._serialized_end = 1038
    _globals['_TYPE_STRING']._serialized_start = 1053
    _globals['_TYPE_STRING']._serialized_end = 1348
    _globals['_TYPE_STRING_ENCODING']._serialized_start = 1124
    _globals['_TYPE_STRING_ENCODING']._serialized_end = 1348
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_start = 1284
    _globals['_TYPE_STRING_ENCODING_UTF8RAW']._serialized_end = 1297
    _globals['_TYPE_STRING_ENCODING_UTF8BYTES']._serialized_start = 1299
    _globals['_TYPE_STRING_ENCODING_UTF8BYTES']._serialized_end = 1336
    _globals['_TYPE_INT64']._serialized_start = 1351
    _globals['_TYPE_INT64']._serialized_end = 1708
    _globals['_TYPE_INT64_ENCODING']._serialized_start = 1420
    _globals['_TYPE_INT64_ENCODING']._serialized_end = 1708
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES']._serialized_start = 1604
    _globals['_TYPE_INT64_ENCODING_BIGENDIANBYTES']._serialized_end = 1676
    _globals['_TYPE_INT64_ENCODING_ORDEREDCODEBYTES']._serialized_start = 1678
    _globals['_TYPE_INT64_ENCODING_ORDEREDCODEBYTES']._serialized_end = 1696
    _globals['_TYPE_BOOL']._serialized_start = 1710
    _globals['_TYPE_BOOL']._serialized_end = 1716
    _globals['_TYPE_FLOAT32']._serialized_start = 1718
    _globals['_TYPE_FLOAT32']._serialized_end = 1727
    _globals['_TYPE_FLOAT64']._serialized_start = 1729
    _globals['_TYPE_FLOAT64']._serialized_end = 1738
    _globals['_TYPE_TIMESTAMP']._serialized_start = 1741
    _globals['_TYPE_TIMESTAMP']._serialized_end = 1909
    _globals['_TYPE_TIMESTAMP_ENCODING']._serialized_start = 1817
    _globals['_TYPE_TIMESTAMP_ENCODING']._serialized_end = 1909
    _globals['_TYPE_DATE']._serialized_start = 1911
    _globals['_TYPE_DATE']._serialized_end = 1917
    _globals['_TYPE_STRUCT']._serialized_start = 1920
    _globals['_TYPE_STRUCT']._serialized_end = 2453
    _globals['_TYPE_STRUCT_FIELD']._serialized_start = 2045
    _globals['_TYPE_STRUCT_FIELD']._serialized_end = 2112
    _globals['_TYPE_STRUCT_ENCODING']._serialized_start = 2115
    _globals['_TYPE_STRUCT_ENCODING']._serialized_end = 2453
    _globals['_TYPE_STRUCT_ENCODING_SINGLETON']._serialized_start = 2373
    _globals['_TYPE_STRUCT_ENCODING_SINGLETON']._serialized_end = 2384
    _globals['_TYPE_STRUCT_ENCODING_DELIMITEDBYTES']._serialized_start = 2386
    _globals['_TYPE_STRUCT_ENCODING_DELIMITEDBYTES']._serialized_end = 2421
    _globals['_TYPE_STRUCT_ENCODING_ORDEREDCODEBYTES']._serialized_start = 1678
    _globals['_TYPE_STRUCT_ENCODING_ORDEREDCODEBYTES']._serialized_end = 1696
    _globals['_TYPE_PROTO']._serialized_start = 2455
    _globals['_TYPE_PROTO']._serialized_end = 2510
    _globals['_TYPE_ENUM']._serialized_start = 2512
    _globals['_TYPE_ENUM']._serialized_end = 2563
    _globals['_TYPE_ARRAY']._serialized_start = 2565
    _globals['_TYPE_ARRAY']._serialized_end = 2620
    _globals['_TYPE_MAP']._serialized_start = 2622
    _globals['_TYPE_MAP']._serialized_end = 2717
    _globals['_TYPE_AGGREGATE']._serialized_start = 2720
    _globals['_TYPE_AGGREGATE']._serialized_end = 3159
    _globals['_TYPE_AGGREGATE_SUM']._serialized_start = 3092
    _globals['_TYPE_AGGREGATE_SUM']._serialized_end = 3097
    _globals['_TYPE_AGGREGATE_MAX']._serialized_start = 3099
    _globals['_TYPE_AGGREGATE_MAX']._serialized_end = 3104
    _globals['_TYPE_AGGREGATE_MIN']._serialized_start = 3106
    _globals['_TYPE_AGGREGATE_MIN']._serialized_end = 3111
    _globals['_TYPE_AGGREGATE_HYPERLOGLOGPLUSPLUSUNIQUECOUNT']._serialized_start = 3113
    _globals['_TYPE_AGGREGATE_HYPERLOGLOGPLUSPLUSUNIQUECOUNT']._serialized_end = 3145