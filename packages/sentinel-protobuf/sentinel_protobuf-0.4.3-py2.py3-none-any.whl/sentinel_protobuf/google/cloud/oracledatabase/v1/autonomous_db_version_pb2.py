"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/oracledatabase/v1/autonomous_db_version.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.oracledatabase.v1 import autonomous_database_pb2 as google_dot_cloud_dot_oracledatabase_dot_v1_dot_autonomous__database__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/cloud/oracledatabase/v1/autonomous_db_version.proto\x12\x1egoogle.cloud.oracledatabase.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a8google/cloud/oracledatabase/v1/autonomous_database.proto"\xda\x02\n\x13AutonomousDbVersion\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x07version\x18\x02 \x01(\tB\x03\xe0A\x03\x12D\n\x0bdb_workload\x18\x04 \x01(\x0e2*.google.cloud.oracledatabase.v1.DBWorkloadB\x03\xe0A\x03\x12\x19\n\x0cworkload_uri\x18\x05 \x01(\tB\x03\xe0A\x03:\xb8\x01\xeaA\xb4\x01\n1oracledatabase.googleapis.com/AutonomousDbVersion\x12Tprojects/{project}/locations/{location}/autonomousDbVersions/{autonomous_db_version}*\x14autonomousDbVersions2\x13autonomousDbVersionB\xf2\x01\n"com.google.cloud.oracledatabase.v1B\x18AutonomousDbVersionProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.oracledatabase.v1.autonomous_db_version_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.cloud.oracledatabase.v1B\x18AutonomousDbVersionProtoP\x01ZJcloud.google.com/go/oracledatabase/apiv1/oracledatabasepb;oracledatabasepb\xaa\x02\x1eGoogle.Cloud.OracleDatabase.V1\xca\x02\x1eGoogle\\Cloud\\OracleDatabase\\V1\xea\x02!Google::Cloud::OracleDatabase::V1'
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['name']._loaded_options = None
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['version']._loaded_options = None
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['version']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['db_workload']._loaded_options = None
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['db_workload']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['workload_uri']._loaded_options = None
    _globals['_AUTONOMOUSDBVERSION'].fields_by_name['workload_uri']._serialized_options = b'\xe0A\x03'
    _globals['_AUTONOMOUSDBVERSION']._loaded_options = None
    _globals['_AUTONOMOUSDBVERSION']._serialized_options = b'\xeaA\xb4\x01\n1oracledatabase.googleapis.com/AutonomousDbVersion\x12Tprojects/{project}/locations/{location}/autonomousDbVersions/{autonomous_db_version}*\x14autonomousDbVersions2\x13autonomousDbVersion'
    _globals['_AUTONOMOUSDBVERSION']._serialized_start = 213
    _globals['_AUTONOMOUSDBVERSION']._serialized_end = 559