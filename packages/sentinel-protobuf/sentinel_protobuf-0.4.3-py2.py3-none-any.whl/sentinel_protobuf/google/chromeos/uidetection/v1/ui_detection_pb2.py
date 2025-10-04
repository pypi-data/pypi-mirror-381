"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chromeos/uidetection/v1/ui_detection.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n1google/chromeos/uidetection/v1/ui_detection.proto\x12\x1egoogle.chromeos.uidetection.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xc9\x02\n\x12UiDetectionRequest\x12\x16\n\timage_png\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12F\n\x07request\x18\x02 \x01(\x0b20.google.chromeos.uidetection.v1.DetectionRequestB\x03\xe0A\x02\x12\x19\n\x0cresize_image\x18\x03 \x01(\x08H\x00\x88\x01\x01\x12\x13\n\x07test_id\x18\x04 \x01(\tB\x02\x18\x01\x12H\n\rtest_metadata\x18\x05 \x01(\x0b2,.google.chromeos.uidetection.v1.TestMetadataB\x03\xe0A\x01\x12!\n\x14force_image_resizing\x18\x06 \x01(\x08B\x03\xe0A\x01\x12%\n\x18return_transformed_image\x18\x07 \x01(\x08B\x03\xe0A\x01B\x0f\n\r_resize_image"\xcc\x02\n\x10DetectionRequest\x12V\n\x16word_detection_request\x18\x01 \x01(\x0b24.google.chromeos.uidetection.v1.WordDetectionRequestH\x00\x12a\n\x1ctext_block_detection_request\x18\x02 \x01(\x0b29.google.chromeos.uidetection.v1.TextBlockDetectionRequestH\x00\x12c\n\x1dcustom_icon_detection_request\x18\x03 \x01(\x0b2:.google.chromeos.uidetection.v1.CustomIconDetectionRequestH\x00B\x18\n\x16detection_request_type"Q\n\x0cTestMetadata\x12\x0f\n\x07test_id\x18\x01 \x01(\t\x12\r\n\x05board\x18\x02 \x01(\t\x12\r\n\x05model\x18\x03 \x01(\t\x12\x12\n\ncros_build\x18\x04 \x01(\t"\x91\x01\n\x14WordDetectionRequest\x12\x11\n\x04word\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x12\n\nregex_mode\x18\x02 \x01(\x08\x12\x1c\n\x14disable_approx_match\x18\x03 \x01(\x08\x12\x1e\n\x11max_edit_distance\x18\x04 \x01(\x05H\x00\x88\x01\x01B\x14\n\x12_max_edit_distance"\xb5\x01\n\x19TextBlockDetectionRequest\x12\x12\n\x05words\x18\x01 \x03(\tB\x03\xe0A\x02\x12\x12\n\nregex_mode\x18\x02 \x01(\x08\x12\x1c\n\x14disable_approx_match\x18\x03 \x01(\x08\x12\x1e\n\x11max_edit_distance\x18\x04 \x01(\x05H\x00\x88\x01\x01\x12\x1c\n\x14specified_words_only\x18\x05 \x01(\x08B\x14\n\x12_max_edit_distance"j\n\x1aCustomIconDetectionRequest\x12\x15\n\x08icon_png\x18\x01 \x01(\x0cB\x03\xe0A\x02\x12\x13\n\x0bmatch_count\x18\x02 \x01(\x05\x12 \n\x18min_confidence_threshold\x18\x03 \x01(\x01"\x98\x01\n\x13UiDetectionResponse\x12C\n\x0ebounding_boxes\x18\x01 \x03(\x0b2+.google.chromeos.uidetection.v1.BoundingBox\x12\x1d\n\x15transformed_image_png\x18\x02 \x01(\x0c\x12\x1d\n\x15resizing_scale_factor\x18\x03 \x01(\x02"U\n\x0bBoundingBox\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03top\x18\x02 \x01(\x05\x12\x0c\n\x04left\x18\x03 \x01(\x05\x12\x0e\n\x06bottom\x18\x04 \x01(\x05\x12\r\n\x05right\x18\x05 \x01(\x052\xdf\x01\n\x12UiDetectionService\x12\xa1\x01\n\x10ExecuteDetection\x122.google.chromeos.uidetection.v1.UiDetectionRequest\x1a3.google.chromeos.uidetection.v1.UiDetectionResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/executeDetection:execute\x1a%\xcaA"chromeosuidetection.googleapis.comB\x83\x01\n"com.google.chromeos.uidetection.v1B\x10UiDetectionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/chromeos/uidetection/v1;uidetectionb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chromeos.uidetection.v1.ui_detection_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.chromeos.uidetection.v1B\x10UiDetectionProtoP\x01ZIgoogle.golang.org/genproto/googleapis/chromeos/uidetection/v1;uidetection'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['image_png']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['image_png']._serialized_options = b'\xe0A\x02'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['request']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['request']._serialized_options = b'\xe0A\x02'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['test_id']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['test_id']._serialized_options = b'\x18\x01'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['test_metadata']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['test_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['force_image_resizing']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['force_image_resizing']._serialized_options = b'\xe0A\x01'
    _globals['_UIDETECTIONREQUEST'].fields_by_name['return_transformed_image']._loaded_options = None
    _globals['_UIDETECTIONREQUEST'].fields_by_name['return_transformed_image']._serialized_options = b'\xe0A\x01'
    _globals['_WORDDETECTIONREQUEST'].fields_by_name['word']._loaded_options = None
    _globals['_WORDDETECTIONREQUEST'].fields_by_name['word']._serialized_options = b'\xe0A\x02'
    _globals['_TEXTBLOCKDETECTIONREQUEST'].fields_by_name['words']._loaded_options = None
    _globals['_TEXTBLOCKDETECTIONREQUEST'].fields_by_name['words']._serialized_options = b'\xe0A\x02'
    _globals['_CUSTOMICONDETECTIONREQUEST'].fields_by_name['icon_png']._loaded_options = None
    _globals['_CUSTOMICONDETECTIONREQUEST'].fields_by_name['icon_png']._serialized_options = b'\xe0A\x02'
    _globals['_UIDETECTIONSERVICE']._loaded_options = None
    _globals['_UIDETECTIONSERVICE']._serialized_options = b'\xcaA"chromeosuidetection.googleapis.com'
    _globals['_UIDETECTIONSERVICE'].methods_by_name['ExecuteDetection']._loaded_options = None
    _globals['_UIDETECTIONSERVICE'].methods_by_name['ExecuteDetection']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v1/executeDetection:execute'
    _globals['_UIDETECTIONREQUEST']._serialized_start = 174
    _globals['_UIDETECTIONREQUEST']._serialized_end = 503
    _globals['_DETECTIONREQUEST']._serialized_start = 506
    _globals['_DETECTIONREQUEST']._serialized_end = 838
    _globals['_TESTMETADATA']._serialized_start = 840
    _globals['_TESTMETADATA']._serialized_end = 921
    _globals['_WORDDETECTIONREQUEST']._serialized_start = 924
    _globals['_WORDDETECTIONREQUEST']._serialized_end = 1069
    _globals['_TEXTBLOCKDETECTIONREQUEST']._serialized_start = 1072
    _globals['_TEXTBLOCKDETECTIONREQUEST']._serialized_end = 1253
    _globals['_CUSTOMICONDETECTIONREQUEST']._serialized_start = 1255
    _globals['_CUSTOMICONDETECTIONREQUEST']._serialized_end = 1361
    _globals['_UIDETECTIONRESPONSE']._serialized_start = 1364
    _globals['_UIDETECTIONRESPONSE']._serialized_end = 1516
    _globals['_BOUNDINGBOX']._serialized_start = 1518
    _globals['_BOUNDINGBOX']._serialized_end = 1603
    _globals['_UIDETECTIONSERVICE']._serialized_start = 1606
    _globals['_UIDETECTIONSERVICE']._serialized_end = 1829