"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/firestore/v1/write.proto')
_sym_db = _symbol_database.Default()
from ....google.firestore.v1 import bloom_filter_pb2 as google_dot_firestore_dot_v1_dot_bloom__filter__pb2
from ....google.firestore.v1 import common_pb2 as google_dot_firestore_dot_v1_dot_common__pb2
from ....google.firestore.v1 import document_pb2 as google_dot_firestore_dot_v1_dot_document__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fgoogle/firestore/v1/write.proto\x12\x13google.firestore.v1\x1a&google/firestore/v1/bloom_filter.proto\x1a google/firestore/v1/common.proto\x1a"google/firestore/v1/document.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xdb\x02\n\x05Write\x12/\n\x06update\x18\x01 \x01(\x0b2\x1d.google.firestore.v1.DocumentH\x00\x12\x10\n\x06delete\x18\x02 \x01(\tH\x00\x12;\n\ttransform\x18\x06 \x01(\x0b2&.google.firestore.v1.DocumentTransformH\x00\x126\n\x0bupdate_mask\x18\x03 \x01(\x0b2!.google.firestore.v1.DocumentMask\x12P\n\x11update_transforms\x18\x07 \x03(\x0b25.google.firestore.v1.DocumentTransform.FieldTransform\x12;\n\x10current_document\x18\x04 \x01(\x0b2!.google.firestore.v1.PreconditionB\x0b\n\toperation"\xe5\x04\n\x11DocumentTransform\x12\x10\n\x08document\x18\x01 \x01(\t\x12O\n\x10field_transforms\x18\x02 \x03(\x0b25.google.firestore.v1.DocumentTransform.FieldTransform\x1a\xec\x03\n\x0eFieldTransform\x12\x12\n\nfield_path\x18\x01 \x01(\t\x12`\n\x13set_to_server_value\x18\x02 \x01(\x0e2A.google.firestore.v1.DocumentTransform.FieldTransform.ServerValueH\x00\x12/\n\tincrement\x18\x03 \x01(\x0b2\x1a.google.firestore.v1.ValueH\x00\x12-\n\x07maximum\x18\x04 \x01(\x0b2\x1a.google.firestore.v1.ValueH\x00\x12-\n\x07minimum\x18\x05 \x01(\x0b2\x1a.google.firestore.v1.ValueH\x00\x12B\n\x17append_missing_elements\x18\x06 \x01(\x0b2\x1f.google.firestore.v1.ArrayValueH\x00\x12@\n\x15remove_all_from_array\x18\x07 \x01(\x0b2\x1f.google.firestore.v1.ArrayValueH\x00"=\n\x0bServerValue\x12\x1c\n\x18SERVER_VALUE_UNSPECIFIED\x10\x00\x12\x10\n\x0cREQUEST_TIME\x10\x01B\x10\n\x0etransform_type"u\n\x0bWriteResult\x12/\n\x0bupdate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x125\n\x11transform_results\x18\x02 \x03(\x0b2\x1a.google.firestore.v1.Value"q\n\x0eDocumentChange\x12/\n\x08document\x18\x01 \x01(\x0b2\x1d.google.firestore.v1.Document\x12\x12\n\ntarget_ids\x18\x05 \x03(\x05\x12\x1a\n\x12removed_target_ids\x18\x06 \x03(\x05"m\n\x0eDocumentDelete\x12\x10\n\x08document\x18\x01 \x01(\t\x12\x1a\n\x12removed_target_ids\x18\x06 \x03(\x05\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"m\n\x0eDocumentRemove\x12\x10\n\x08document\x18\x01 \x01(\t\x12\x1a\n\x12removed_target_ids\x18\x02 \x03(\x05\x12-\n\tread_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.Timestamp"n\n\x0fExistenceFilter\x12\x11\n\ttarget_id\x18\x01 \x01(\x05\x12\r\n\x05count\x18\x02 \x01(\x05\x129\n\x0funchanged_names\x18\x03 \x01(\x0b2 .google.firestore.v1.BloomFilterB\xc2\x01\n\x17com.google.firestore.v1B\nWriteProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.v1.write_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x17com.google.firestore.v1B\nWriteProtoP\x01Z;cloud.google.com/go/firestore/apiv1/firestorepb;firestorepb\xa2\x02\x04GCFS\xaa\x02\x19Google.Cloud.Firestore.V1\xca\x02\x19Google\\Cloud\\Firestore\\V1\xea\x02\x1cGoogle::Cloud::Firestore::V1'
    _globals['_WRITE']._serialized_start = 200
    _globals['_WRITE']._serialized_end = 547
    _globals['_DOCUMENTTRANSFORM']._serialized_start = 550
    _globals['_DOCUMENTTRANSFORM']._serialized_end = 1163
    _globals['_DOCUMENTTRANSFORM_FIELDTRANSFORM']._serialized_start = 671
    _globals['_DOCUMENTTRANSFORM_FIELDTRANSFORM']._serialized_end = 1163
    _globals['_DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE']._serialized_start = 1084
    _globals['_DOCUMENTTRANSFORM_FIELDTRANSFORM_SERVERVALUE']._serialized_end = 1145
    _globals['_WRITERESULT']._serialized_start = 1165
    _globals['_WRITERESULT']._serialized_end = 1282
    _globals['_DOCUMENTCHANGE']._serialized_start = 1284
    _globals['_DOCUMENTCHANGE']._serialized_end = 1397
    _globals['_DOCUMENTDELETE']._serialized_start = 1399
    _globals['_DOCUMENTDELETE']._serialized_end = 1508
    _globals['_DOCUMENTREMOVE']._serialized_start = 1510
    _globals['_DOCUMENTREMOVE']._serialized_end = 1619
    _globals['_EXISTENCEFILTER']._serialized_start = 1621
    _globals['_EXISTENCEFILTER']._serialized_end = 1731