"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataplex/v1/datascans_common.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/dataplex/v1/datascans_common.proto\x12\x18google.cloud.dataplex.v1\x1a\x1fgoogle/api/field_behavior.proto"\xb1\x01\n\x1fDataScanCatalogPublishingStatus\x12S\n\x05state\x18\x01 \x01(\x0e2?.google.cloud.dataplex.v1.DataScanCatalogPublishingStatus.StateB\x03\xe0A\x03"9\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02Bp\n\x1ccom.google.cloud.dataplex.v1B\x14DataScansCommonProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.datascans_common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x14DataScansCommonProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS'].fields_by_name['state']._loaded_options = None
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS']._serialized_start = 111
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS']._serialized_end = 288
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS_STATE']._serialized_start = 231
    _globals['_DATASCANCATALOGPUBLISHINGSTATUS_STATE']._serialized_end = 288