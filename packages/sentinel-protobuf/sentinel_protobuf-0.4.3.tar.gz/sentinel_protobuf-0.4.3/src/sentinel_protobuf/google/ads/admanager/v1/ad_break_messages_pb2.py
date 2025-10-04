"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/ad_break_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import early_ad_break_notification_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_early__ad__break__notification__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/ads/admanager/v1/ad_break_messages.proto\x12\x17google.ads.admanager.v1\x1a?google/ads/admanager/v1/early_ad_break_notification_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xa8\x06\n\x07AdBreak\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12 \n\x0bad_break_id\x18\x02 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x00\x88\x01\x01\x12\x1e\n\tasset_key\x18\x03 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x01\x88\x01\x01\x12%\n\x10custom_asset_key\x18\x04 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x02\x88\x01\x01\x12A\n\x13expected_start_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x01H\x03\x88\x01\x01\x125\n\x08duration\x18\x06 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x02H\x04\x88\x01\x01\x12U\n\x0bbreak_state\x18\x07 \x01(\x0e26.google.ads.admanager.v1.AdBreakStateEnum.AdBreakStateB\x03\xe0A\x03H\x05\x88\x01\x01\x12 \n\x0ebreak_sequence\x18\x08 \x01(\x03B\x03\xe0A\x03H\x06\x88\x01\x01\x12#\n\x11pod_template_name\x18\t \x01(\tB\x03\xe0A\x01H\x07\x88\x01\x01\x12\x1f\n\rcustom_params\x18\n \x01(\tB\x03\xe0A\x01H\x08\x88\x01\x01\x12!\n\x0fscte_35_cue_out\x18\x0b \x01(\tB\x03\xe0A\x01H\t\x88\x01\x01:\x8d\x01\xeaA\x89\x01\n admanager.googleapis.com/AdBreak\x12Rnetworks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break}*\x08adBreaks2\x07adBreakB\x0e\n\x0c_ad_break_idB\x0c\n\n_asset_keyB\x13\n\x11_custom_asset_keyB\x16\n\x14_expected_start_timeB\x0b\n\t_durationB\x0e\n\x0c_break_stateB\x11\n\x0f_break_sequenceB\x14\n\x12_pod_template_nameB\x10\n\x0e_custom_paramsB\x12\n\x10_scte_35_cue_outB\xc8\x01\n\x1bcom.google.ads.admanager.v1B\x14AdBreakMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.ad_break_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x14AdBreakMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ADBREAK'].fields_by_name['name']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ADBREAK'].fields_by_name['ad_break_id']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['ad_break_id']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_ADBREAK'].fields_by_name['asset_key']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['asset_key']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_ADBREAK'].fields_by_name['custom_asset_key']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['custom_asset_key']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_ADBREAK'].fields_by_name['expected_start_time']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['expected_start_time']._serialized_options = b'\xe0A\x01'
    _globals['_ADBREAK'].fields_by_name['duration']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['duration']._serialized_options = b'\xe0A\x02'
    _globals['_ADBREAK'].fields_by_name['break_state']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['break_state']._serialized_options = b'\xe0A\x03'
    _globals['_ADBREAK'].fields_by_name['break_sequence']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['break_sequence']._serialized_options = b'\xe0A\x03'
    _globals['_ADBREAK'].fields_by_name['pod_template_name']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['pod_template_name']._serialized_options = b'\xe0A\x01'
    _globals['_ADBREAK'].fields_by_name['custom_params']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['custom_params']._serialized_options = b'\xe0A\x01'
    _globals['_ADBREAK'].fields_by_name['scte_35_cue_out']._loaded_options = None
    _globals['_ADBREAK'].fields_by_name['scte_35_cue_out']._serialized_options = b'\xe0A\x01'
    _globals['_ADBREAK']._loaded_options = None
    _globals['_ADBREAK']._serialized_options = b'\xeaA\x89\x01\n admanager.googleapis.com/AdBreak\x12Rnetworks/{network_code}/liveStreamEventsByAssetKey/{asset_key}/adBreaks/{ad_break}*\x08adBreaks2\x07adBreak'
    _globals['_ADBREAK']._serialized_start = 267
    _globals['_ADBREAK']._serialized_end = 1075