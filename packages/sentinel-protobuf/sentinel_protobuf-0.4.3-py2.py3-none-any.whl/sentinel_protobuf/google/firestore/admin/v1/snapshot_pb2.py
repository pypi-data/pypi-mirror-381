"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/firestore/admin/v1/snapshot.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(google/firestore/admin/v1/snapshot.proto\x12\x19google.firestore.admin.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9e\x01\n\x0cPitrSnapshot\x12;\n\x08database\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database\x12\x19\n\x0cdatabase_uid\x18\x02 \x01(\x0cB\x03\xe0A\x03\x126\n\rsnapshot_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x02B\xe0\x01\n\x1dcom.google.firestore.admin.v1B\x11PitrSnapshotProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.firestore.admin.v1.snapshot_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1dcom.google.firestore.admin.v1B\x11PitrSnapshotProtoP\x01Z9cloud.google.com/go/firestore/apiv1/admin/adminpb;adminpb\xa2\x02\x04GCFS\xaa\x02\x1fGoogle.Cloud.Firestore.Admin.V1\xca\x02\x1fGoogle\\Cloud\\Firestore\\Admin\\V1\xea\x02#Google::Cloud::Firestore::Admin::V1'
    _globals['_PITRSNAPSHOT'].fields_by_name['database']._loaded_options = None
    _globals['_PITRSNAPSHOT'].fields_by_name['database']._serialized_options = b'\xe0A\x02\xfaA#\n!firestore.googleapis.com/Database'
    _globals['_PITRSNAPSHOT'].fields_by_name['database_uid']._loaded_options = None
    _globals['_PITRSNAPSHOT'].fields_by_name['database_uid']._serialized_options = b'\xe0A\x03'
    _globals['_PITRSNAPSHOT'].fields_by_name['snapshot_time']._loaded_options = None
    _globals['_PITRSNAPSHOT'].fields_by_name['snapshot_time']._serialized_options = b'\xe0A\x02'
    _globals['_PITRSNAPSHOT']._serialized_start = 165
    _globals['_PITRSNAPSHOT']._serialized_end = 323