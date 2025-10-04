"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/ad_unit_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import ad_unit_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_ad__unit__enums__pb2
from .....google.ads.admanager.v1 import applied_label_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_applied__label__pb2
from .....google.ads.admanager.v1 import environment_type_enum_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_environment__type__enum__pb2
from .....google.ads.admanager.v1 import frequency_cap_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_frequency__cap__pb2
from .....google.ads.admanager.v1 import size_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_size__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/admanager/v1/ad_unit_messages.proto\x12\x17google.ads.admanager.v1\x1a+google/ads/admanager/v1/ad_unit_enums.proto\x1a+google/ads/admanager/v1/applied_label.proto\x1a3google/ads/admanager/v1/environment_type_enum.proto\x1a+google/ads/admanager/v1/frequency_cap.proto\x1a"google/ads/admanager/v1/size.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x80\x0f\n\x06AdUnit\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x17\n\nad_unit_id\x18\x0f \x01(\x03B\x03\xe0A\x03\x12G\n\x0eparent_ad_unit\x18\n \x01(\tB*\xe0A\x02\xe0A\x05\xfaA!\n\x1fadmanager.googleapis.com/AdUnitH\x00\x88\x01\x01\x12?\n\x0bparent_path\x18\x0b \x03(\x0b2%.google.ads.admanager.v1.AdUnitParentB\x03\xe0A\x03\x12\x1e\n\x0cdisplay_name\x18\t \x01(\tB\x03\xe0A\x02H\x01\x88\x01\x01\x12!\n\x0cad_unit_code\x18\x02 \x01(\tB\x06\xe0A\x01\xe0A\x05H\x02\x88\x01\x01\x12P\n\x06status\x18\r \x01(\x0e26.google.ads.admanager.v1.AdUnitStatusEnum.AdUnitStatusB\x03\xe0A\x03H\x03\x88\x01\x01\x12_\n\x15applied_target_window\x18, \x01(\x0e26.google.ads.admanager.v1.TargetWindowEnum.TargetWindowB\x03\xe0A\x01H\x04\x88\x01\x01\x12d\n\x17effective_target_window\x18- \x01(\x0e26.google.ads.admanager.v1.TargetWindowEnum.TargetWindowB\x06\xe0A\x07\xe0A\x03H\x05\x88\x01\x01\x12<\n\rapplied_teams\x18\x03 \x03(\tB%\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team\x124\n\x05teams\x18\x04 \x03(\tB%\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/Team\x12\x1d\n\x0bdescription\x18\x05 \x01(\tB\x03\xe0A\x01H\x06\x88\x01\x01\x12%\n\x13explicitly_targeted\x18\x06 \x01(\x08B\x03\xe0A\x01H\x07\x88\x01\x01\x12\x1e\n\x0chas_children\x18\x07 \x01(\x08B\x03\xe0A\x03H\x08\x88\x01\x01\x129\n\x0bupdate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\t\x88\x01\x01\x12?\n\rad_unit_sizes\x18\x0e \x03(\x0b2#.google.ads.admanager.v1.AdUnitSizeB\x03\xe0A\x01\x123\n\x1fexternal_set_top_box_channel_id\x18\x11 \x01(\tB\x05\x18\x01\xe0A\x01H\n\x88\x01\x01\x12:\n\rrefresh_delay\x18\x13 \x01(\x0b2\x19.google.protobuf.DurationB\x03\xe0A\x01H\x0b\x88\x01\x01\x12B\n\x0eapplied_labels\x18\x15 \x03(\x0b2%.google.ads.admanager.v1.AppliedLabelB\x03\xe0A\x01\x12L\n\x18effective_applied_labels\x18\x16 \x03(\x0b2%.google.ads.admanager.v1.AppliedLabelB\x03\xe0A\x03\x12U\n\x1capplied_label_frequency_caps\x18\x17 \x03(\x0b2*.google.ads.admanager.v1.LabelFrequencyCapB\x03\xe0A\x01\x12W\n\x1eeffective_label_frequency_caps\x18\x18 \x03(\x0b2*.google.ads.admanager.v1.LabelFrequencyCapB\x03\xe0A\x03\x12^\n\x0fsmart_size_mode\x18\x19 \x01(\x0e28.google.ads.admanager.v1.SmartSizeModeEnum.SmartSizeModeB\x06\xe0A\x01\xe0A\x07H\x0c\x88\x01\x01\x12)\n\x17applied_adsense_enabled\x18\x1a \x01(\x08B\x03\xe0A\x01H\r\x88\x01\x01\x12+\n\x19effective_adsense_enabled\x18\x1b \x01(\x08B\x03\xe0A\x03H\x0e\x88\x01\x01:`\xeaA]\n\x1fadmanager.googleapis.com/AdUnit\x12)networks/{network_code}/adUnits/{ad_unit}*\x07adUnits2\x06adUnitB\x11\n\x0f_parent_ad_unitB\x0f\n\r_display_nameB\x0f\n\r_ad_unit_codeB\t\n\x07_statusB\x18\n\x16_applied_target_windowB\x1a\n\x18_effective_target_windowB\x0e\n\x0c_descriptionB\x16\n\x14_explicitly_targetedB\x0f\n\r_has_childrenB\x0e\n\x0c_update_timeB"\n _external_set_top_box_channel_idB\x10\n\x0e_refresh_delayB\x12\n\x10_smart_size_modeB\x1a\n\x18_applied_adsense_enabledB\x1c\n\x1a_effective_adsense_enabled"\xce\x01\n\nAdUnitSize\x120\n\x04size\x18\x01 \x01(\x0b2\x1d.google.ads.admanager.v1.SizeB\x03\xe0A\x02\x12[\n\x10environment_type\x18\x02 \x01(\x0e2<.google.ads.admanager.v1.EnvironmentTypeEnum.EnvironmentTypeB\x03\xe0A\x02\x121\n\ncompanions\x18\x03 \x03(\x0b2\x1d.google.ads.admanager.v1.Size"\x85\x01\n\x0cAdUnitParent\x12?\n\x0eparent_ad_unit\x18\x01 \x01(\tB\'\xe0A\x03\xfaA!\n\x1fadmanager.googleapis.com/AdUnit\x12\x19\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cad_unit_code\x18\x03 \x01(\tB\x03\xe0A\x03"\x88\x01\n\x11LabelFrequencyCap\x125\n\x05label\x18\x01 \x01(\tB&\xe0A\x02\xfaA \n\x1eadmanager.googleapis.com/Label\x12<\n\rfrequency_cap\x18\x02 \x01(\x0b2%.google.ads.admanager.v1.FrequencyCapB\xc7\x01\n\x1bcom.google.ads.admanager.v1B\x13AdUnitMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.ad_unit_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x13AdUnitMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ADUNIT'].fields_by_name['name']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ADUNIT'].fields_by_name['ad_unit_id']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['ad_unit_id']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['parent_ad_unit']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['parent_ad_unit']._serialized_options = b'\xe0A\x02\xe0A\x05\xfaA!\n\x1fadmanager.googleapis.com/AdUnit'
    _globals['_ADUNIT'].fields_by_name['parent_path']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['parent_path']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['display_name']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ADUNIT'].fields_by_name['ad_unit_code']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['ad_unit_code']._serialized_options = b'\xe0A\x01\xe0A\x05'
    _globals['_ADUNIT'].fields_by_name['status']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['applied_target_window']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['applied_target_window']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['effective_target_window']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['effective_target_window']._serialized_options = b'\xe0A\x07\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['applied_teams']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['applied_teams']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team'
    _globals['_ADUNIT'].fields_by_name['teams']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['teams']._serialized_options = b'\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/Team'
    _globals['_ADUNIT'].fields_by_name['description']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['explicitly_targeted']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['explicitly_targeted']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['has_children']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['has_children']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['update_time']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['ad_unit_sizes']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['ad_unit_sizes']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['external_set_top_box_channel_id']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['external_set_top_box_channel_id']._serialized_options = b'\x18\x01\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['refresh_delay']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['refresh_delay']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['applied_labels']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['applied_labels']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['effective_applied_labels']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['effective_applied_labels']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['applied_label_frequency_caps']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['applied_label_frequency_caps']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['effective_label_frequency_caps']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['effective_label_frequency_caps']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT'].fields_by_name['smart_size_mode']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['smart_size_mode']._serialized_options = b'\xe0A\x01\xe0A\x07'
    _globals['_ADUNIT'].fields_by_name['applied_adsense_enabled']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['applied_adsense_enabled']._serialized_options = b'\xe0A\x01'
    _globals['_ADUNIT'].fields_by_name['effective_adsense_enabled']._loaded_options = None
    _globals['_ADUNIT'].fields_by_name['effective_adsense_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNIT']._loaded_options = None
    _globals['_ADUNIT']._serialized_options = b'\xeaA]\n\x1fadmanager.googleapis.com/AdUnit\x12)networks/{network_code}/adUnits/{ad_unit}*\x07adUnits2\x06adUnit'
    _globals['_ADUNITSIZE'].fields_by_name['size']._loaded_options = None
    _globals['_ADUNITSIZE'].fields_by_name['size']._serialized_options = b'\xe0A\x02'
    _globals['_ADUNITSIZE'].fields_by_name['environment_type']._loaded_options = None
    _globals['_ADUNITSIZE'].fields_by_name['environment_type']._serialized_options = b'\xe0A\x02'
    _globals['_ADUNITPARENT'].fields_by_name['parent_ad_unit']._loaded_options = None
    _globals['_ADUNITPARENT'].fields_by_name['parent_ad_unit']._serialized_options = b'\xe0A\x03\xfaA!\n\x1fadmanager.googleapis.com/AdUnit'
    _globals['_ADUNITPARENT'].fields_by_name['display_name']._loaded_options = None
    _globals['_ADUNITPARENT'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_ADUNITPARENT'].fields_by_name['ad_unit_code']._loaded_options = None
    _globals['_ADUNITPARENT'].fields_by_name['ad_unit_code']._serialized_options = b'\xe0A\x03'
    _globals['_LABELFREQUENCYCAP'].fields_by_name['label']._loaded_options = None
    _globals['_LABELFREQUENCYCAP'].fields_by_name['label']._serialized_options = b'\xe0A\x02\xfaA \n\x1eadmanager.googleapis.com/Label'
    _globals['_ADUNIT']._serialized_start = 425
    _globals['_ADUNIT']._serialized_end = 2345
    _globals['_ADUNITSIZE']._serialized_start = 2348
    _globals['_ADUNITSIZE']._serialized_end = 2554
    _globals['_ADUNITPARENT']._serialized_start = 2557
    _globals['_ADUNITPARENT']._serialized_end = 2690
    _globals['_LABELFREQUENCYCAP']._serialized_start = 2693
    _globals['_LABELFREQUENCYCAP']._serialized_end = 2829