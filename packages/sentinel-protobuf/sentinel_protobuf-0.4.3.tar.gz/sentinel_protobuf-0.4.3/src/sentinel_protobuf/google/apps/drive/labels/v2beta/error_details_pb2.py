"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/apps/drive/labels/v2beta/error_details.proto')
_sym_db = _symbol_database.Default()
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/apps/drive/labels/v2beta/error_details.proto\x12\x1fgoogle.apps.drive.labels.v2beta"\xc1\x03\n\x0fInvalidArgument\x12Y\n\x10field_violations\x18\x01 \x03(\x0b2?.google.apps.drive.labels.v2beta.InvalidArgument.FieldViolation\x1a\xd2\x02\n\x0eFieldViolation\x12\r\n\x05field\x18\x01 \x01(\t\x12V\n\x06reason\x18\x02 \x01(\x0e2F.google.apps.drive.labels.v2beta.InvalidArgument.FieldViolation.Reason\x12\x17\n\x0fdisplay_message\x18\x03 \x01(\t"\xbf\x01\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eFIELD_REQUIRED\x10\x01\x12\x11\n\rINVALID_VALUE\x10\x02\x12\x16\n\x12VALUE_OUT_OF_RANGE\x10\x03\x12\x19\n\x15STRING_VALUE_TOO_LONG\x10\x04\x12\x18\n\x14MAX_ENTRIES_EXCEEDED\x10\x05\x12\x13\n\x0fFIELD_NOT_FOUND\x10\x06\x12\x14\n\x10CHOICE_NOT_FOUND\x10\x07"\xc9\x04\n\x13PreconditionFailure\x12Q\n\tviolation\x18\x01 \x03(\x0b2>.google.apps.drive.labels.v2beta.PreconditionFailure.Violation\x1a\xde\x03\n\tViolation\x12\r\n\x05field\x18\x01 \x01(\t\x12U\n\x06reason\x18\x02 \x01(\x0e2E.google.apps.drive.labels.v2beta.PreconditionFailure.Violation.Reason\x12\x17\n\x0fdisplay_message\x18\x03 \x01(\t"\xd1\x02\n\x06Reason\x12\x16\n\x12REASON_UNSPECIFIED\x10\x00\x12\x12\n\x0eCANNOT_DISABLE\x10\x01\x12\x11\n\rCANNOT_ENABLE\x10\x02\x12\x12\n\x0eCANNOT_PUBLISH\x10\x03\x12\x14\n\x10CANNOT_UNPUBLISH\x10\x04\x12\x11\n\rCANNOT_DELETE\x10\x05\x12\x19\n\x15CANNOT_RESTRICT_RANGE\x10\x06\x12!\n\x1dCANNOT_CHANGE_PUBLISHED_FIELD\x10\x07\x12\x1d\n\x19CANNOT_CREATE_MORE_LABELS\x10\x08\x12&\n"CANNOT_CHANGE_PUBLISHED_FIELD_TYPE\x10\t\x12"\n\x1eCANNOT_MODIFY_LOCKED_COMPONENT\x10\n\x12"\n\x1eUNSUPPORT_ENABLED_APP_SETTINGS\x10\x0bB\x81\x01\n#com.google.apps.drive.labels.v2betaB\x11ErrorDetailsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labelsb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.apps.drive.labels.v2beta.error_details_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.apps.drive.labels.v2betaB\x11ErrorDetailsProtoP\x01ZEgoogle.golang.org/genproto/googleapis/apps/drive/labels/v2beta;labels'
    _globals['_INVALIDARGUMENT']._serialized_start = 89
    _globals['_INVALIDARGUMENT']._serialized_end = 538
    _globals['_INVALIDARGUMENT_FIELDVIOLATION']._serialized_start = 200
    _globals['_INVALIDARGUMENT_FIELDVIOLATION']._serialized_end = 538
    _globals['_INVALIDARGUMENT_FIELDVIOLATION_REASON']._serialized_start = 347
    _globals['_INVALIDARGUMENT_FIELDVIOLATION_REASON']._serialized_end = 538
    _globals['_PRECONDITIONFAILURE']._serialized_start = 541
    _globals['_PRECONDITIONFAILURE']._serialized_end = 1126
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_start = 648
    _globals['_PRECONDITIONFAILURE_VIOLATION']._serialized_end = 1126
    _globals['_PRECONDITIONFAILURE_VIOLATION_REASON']._serialized_start = 789
    _globals['_PRECONDITIONFAILURE_VIOLATION_REASON']._serialized_end = 1126