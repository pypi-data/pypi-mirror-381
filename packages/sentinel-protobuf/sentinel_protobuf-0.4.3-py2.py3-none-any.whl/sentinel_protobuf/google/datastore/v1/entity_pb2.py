"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/datastore/v1/entity.proto')
_sym_db = _symbol_database.Default()
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from ....google.type import latlng_pb2 as google_dot_type_dot_latlng__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n google/datastore/v1/entity.proto\x12\x13google.datastore.v1\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x18google/type/latlng.proto"L\n\x0bPartitionId\x12\x12\n\nproject_id\x18\x02 \x01(\t\x12\x13\n\x0bdatabase_id\x18\x03 \x01(\t\x12\x14\n\x0cnamespace_id\x18\x04 \x01(\t"\xb7\x01\n\x03Key\x126\n\x0cpartition_id\x18\x01 \x01(\x0b2 .google.datastore.v1.PartitionId\x122\n\x04path\x18\x02 \x03(\x0b2$.google.datastore.v1.Key.PathElement\x1aD\n\x0bPathElement\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\x0c\n\x02id\x18\x02 \x01(\x03H\x00\x12\x0e\n\x04name\x18\x03 \x01(\tH\x00B\t\n\x07id_type"8\n\nArrayValue\x12*\n\x06values\x18\x01 \x03(\x0b2\x1a.google.datastore.v1.Value"\xf1\x03\n\x05Value\x120\n\nnull_value\x18\x0b \x01(\x0e2\x1a.google.protobuf.NullValueH\x00\x12\x17\n\rboolean_value\x18\x01 \x01(\x08H\x00\x12\x17\n\rinteger_value\x18\x02 \x01(\x03H\x00\x12\x16\n\x0cdouble_value\x18\x03 \x01(\x01H\x00\x125\n\x0ftimestamp_value\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12-\n\tkey_value\x18\x05 \x01(\x0b2\x18.google.datastore.v1.KeyH\x00\x12\x16\n\x0cstring_value\x18\x11 \x01(\tH\x00\x12\x14\n\nblob_value\x18\x12 \x01(\x0cH\x00\x12.\n\x0fgeo_point_value\x18\x08 \x01(\x0b2\x13.google.type.LatLngH\x00\x123\n\x0centity_value\x18\x06 \x01(\x0b2\x1b.google.datastore.v1.EntityH\x00\x126\n\x0barray_value\x18\t \x01(\x0b2\x1f.google.datastore.v1.ArrayValueH\x00\x12\x0f\n\x07meaning\x18\x0e \x01(\x05\x12\x1c\n\x14exclude_from_indexes\x18\x13 \x01(\x08B\x0c\n\nvalue_type"\xbf\x01\n\x06Entity\x12%\n\x03key\x18\x01 \x01(\x0b2\x18.google.datastore.v1.Key\x12?\n\nproperties\x18\x03 \x03(\x0b2+.google.datastore.v1.Entity.PropertiesEntry\x1aM\n\x0fPropertiesEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12)\n\x05value\x18\x02 \x01(\x0b2\x1a.google.datastore.v1.Value:\x028\x01B\xbc\x01\n\x17com.google.datastore.v1B\x0bEntityProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.datastore.v1.entity_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.datastore.v1B\x0bEntityProtoP\x01Z;cloud.google.com/go/datastore/apiv1/datastorepb;datastorepb\xaa\x02\x19Google.Cloud.Datastore.V1\xca\x02\x19Google\\Cloud\\Datastore\\V1\xea\x02\x1cGoogle::Cloud::Datastore::V1'
    _globals['_ENTITY_PROPERTIESENTRY']._loaded_options = None
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_options = b'8\x01'
    _globals['_PARTITIONID']._serialized_start = 146
    _globals['_PARTITIONID']._serialized_end = 222
    _globals['_KEY']._serialized_start = 225
    _globals['_KEY']._serialized_end = 408
    _globals['_KEY_PATHELEMENT']._serialized_start = 340
    _globals['_KEY_PATHELEMENT']._serialized_end = 408
    _globals['_ARRAYVALUE']._serialized_start = 410
    _globals['_ARRAYVALUE']._serialized_end = 466
    _globals['_VALUE']._serialized_start = 469
    _globals['_VALUE']._serialized_end = 966
    _globals['_ENTITY']._serialized_start = 969
    _globals['_ENTITY']._serialized_end = 1160
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_start = 1083
    _globals['_ENTITY_PROPERTIESENTRY']._serialized_end = 1160