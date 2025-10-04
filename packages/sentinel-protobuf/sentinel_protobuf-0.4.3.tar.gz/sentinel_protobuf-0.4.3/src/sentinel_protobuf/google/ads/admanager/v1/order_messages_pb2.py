"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/order_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import applied_label_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_applied__label__pb2
from .....google.ads.admanager.v1 import custom_field_value_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_custom__field__value__pb2
from .....google.ads.admanager.v1 import order_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_order__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n,google/ads/admanager/v1/order_messages.proto\x12\x17google.ads.admanager.v1\x1a+google/ads/admanager/v1/applied_label.proto\x1a0google/ads/admanager/v1/custom_field_value.proto\x1a)google/ads/admanager/v1/order_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x96\x0f\n\x05Order\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x1a\n\x08order_id\x18\x04 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0cdisplay_name\x18\x02 \x01(\tB\x03\xe0A\x02H\x01\x88\x01\x01\x12\x1e\n\x0cprogrammatic\x18\x03 \x01(\x08B\x03\xe0A\x01H\x02\x88\x01\x01\x12>\n\ntrafficker\x18\x17 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/UserH\x03\x88\x01\x01\x12E\n\x13advertiser_contacts\x18\x05 \x03(\tB(\xe0A\x01\xfaA"\n admanager.googleapis.com/Contact\x12A\n\nadvertiser\x18\x06 \x01(\tB(\xe0A\x02\xfaA"\n admanager.googleapis.com/CompanyH\x04\x88\x01\x01\x12A\n\x0fagency_contacts\x18\x07 \x03(\tB(\xe0A\x01\xfaA"\n admanager.googleapis.com/Contact\x12=\n\x06agency\x18\x08 \x01(\tB(\xe0A\x01\xfaA"\n admanager.googleapis.com/CompanyH\x05\x88\x01\x01\x12<\n\rapplied_teams\x18\t \x03(\tB%\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team\x12>\n\x0feffective_teams\x18\x1c \x03(\tB%\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/Team\x12;\n\x07creator\x18\n \x01(\tB%\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/UserH\x06\x88\x01\x01\x12\x1f\n\rcurrency_code\x18\x0b \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01\x128\n\nstart_time\x18\x13 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x08\x88\x01\x01\x126\n\x08end_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\t\x88\x01\x01\x12$\n\x12unlimited_end_time\x18- \x01(\x08B\x03\xe0A\x03H\n\x88\x01\x01\x12#\n\x11external_order_id\x18\r \x01(\x05B\x03\xe0A\x01H\x0b\x88\x01\x01\x12\x1a\n\x08archived\x18\x0e \x01(\x08B\x03\xe0A\x03H\x0c\x88\x01\x01\x12&\n\x14last_modified_by_app\x18\x0f \x01(\tB\x03\xe0A\x03H\r\x88\x01\x01\x129\n\x0bupdate_time\x18\x10 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03H\x0e\x88\x01\x01\x12\x17\n\x05notes\x18\x11 \x01(\tB\x03\xe0A\x01H\x0f\x88\x01\x01\x12\x1b\n\tpo_number\x18\x12 \x01(\tB\x03\xe0A\x01H\x10\x88\x01\x01\x12N\n\x06status\x18\x14 \x01(\x0e24.google.ads.admanager.v1.OrderStatusEnum.OrderStatusB\x03\xe0A\x03H\x11\x88\x01\x01\x12?\n\x0bsalesperson\x18\x15 \x01(\tB%\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/UserH\x12\x88\x01\x01\x12G\n\x15secondary_salespeople\x18\x16 \x03(\tB(\xe0A\x01\xe0A\x06\xfaA\x1f\n\x1dadmanager.googleapis.com/User\x12G\n\x15secondary_traffickers\x18\x18 \x03(\tB(\xe0A\x01\xe0A\x06\xfaA\x1f\n\x1dadmanager.googleapis.com/User\x12B\n\x0eapplied_labels\x18\x19 \x03(\x0b2%.google.ads.admanager.v1.AppliedLabelB\x03\xe0A\x01\x12L\n\x18effective_applied_labels\x18\x1a \x03(\x0b2%.google.ads.admanager.v1.AppliedLabelB\x03\xe0A\x03\x12K\n\x13custom_field_values\x18& \x03(\x0b2).google.ads.admanager.v1.CustomFieldValueB\x03\xe0A\x01:Z\xeaAW\n\x1eadmanager.googleapis.com/Order\x12&networks/{network_code}/orders/{order}*\x06orders2\x05orderB\x0b\n\t_order_idB\x0f\n\r_display_nameB\x0f\n\r_programmaticB\r\n\x0b_traffickerB\r\n\x0b_advertiserB\t\n\x07_agencyB\n\n\x08_creatorB\x10\n\x0e_currency_codeB\r\n\x0b_start_timeB\x0b\n\t_end_timeB\x15\n\x13_unlimited_end_timeB\x14\n\x12_external_order_idB\x0b\n\t_archivedB\x17\n\x15_last_modified_by_appB\x0e\n\x0c_update_timeB\x08\n\x06_notesB\x0c\n\n_po_numberB\t\n\x07_statusB\x0e\n\x0c_salespersonB\xc6\x01\n\x1bcom.google.ads.admanager.v1B\x12OrderMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.order_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x12OrderMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_ORDER'].fields_by_name['name']._loaded_options = None
    _globals['_ORDER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_ORDER'].fields_by_name['order_id']._loaded_options = None
    _globals['_ORDER'].fields_by_name['order_id']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['display_name']._loaded_options = None
    _globals['_ORDER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_ORDER'].fields_by_name['programmatic']._loaded_options = None
    _globals['_ORDER'].fields_by_name['programmatic']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER'].fields_by_name['trafficker']._loaded_options = None
    _globals['_ORDER'].fields_by_name['trafficker']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_ORDER'].fields_by_name['advertiser_contacts']._loaded_options = None
    _globals['_ORDER'].fields_by_name['advertiser_contacts']._serialized_options = b'\xe0A\x01\xfaA"\n admanager.googleapis.com/Contact'
    _globals['_ORDER'].fields_by_name['advertiser']._loaded_options = None
    _globals['_ORDER'].fields_by_name['advertiser']._serialized_options = b'\xe0A\x02\xfaA"\n admanager.googleapis.com/Company'
    _globals['_ORDER'].fields_by_name['agency_contacts']._loaded_options = None
    _globals['_ORDER'].fields_by_name['agency_contacts']._serialized_options = b'\xe0A\x01\xfaA"\n admanager.googleapis.com/Contact'
    _globals['_ORDER'].fields_by_name['agency']._loaded_options = None
    _globals['_ORDER'].fields_by_name['agency']._serialized_options = b'\xe0A\x01\xfaA"\n admanager.googleapis.com/Company'
    _globals['_ORDER'].fields_by_name['applied_teams']._loaded_options = None
    _globals['_ORDER'].fields_by_name['applied_teams']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team'
    _globals['_ORDER'].fields_by_name['effective_teams']._loaded_options = None
    _globals['_ORDER'].fields_by_name['effective_teams']._serialized_options = b'\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/Team'
    _globals['_ORDER'].fields_by_name['creator']._loaded_options = None
    _globals['_ORDER'].fields_by_name['creator']._serialized_options = b'\xe0A\x03\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_ORDER'].fields_by_name['currency_code']._loaded_options = None
    _globals['_ORDER'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['start_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['end_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['end_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['unlimited_end_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['unlimited_end_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['external_order_id']._loaded_options = None
    _globals['_ORDER'].fields_by_name['external_order_id']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER'].fields_by_name['archived']._loaded_options = None
    _globals['_ORDER'].fields_by_name['archived']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['last_modified_by_app']._loaded_options = None
    _globals['_ORDER'].fields_by_name['last_modified_by_app']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['update_time']._loaded_options = None
    _globals['_ORDER'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['notes']._loaded_options = None
    _globals['_ORDER'].fields_by_name['notes']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER'].fields_by_name['po_number']._loaded_options = None
    _globals['_ORDER'].fields_by_name['po_number']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER'].fields_by_name['status']._loaded_options = None
    _globals['_ORDER'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['salesperson']._loaded_options = None
    _globals['_ORDER'].fields_by_name['salesperson']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_ORDER'].fields_by_name['secondary_salespeople']._loaded_options = None
    _globals['_ORDER'].fields_by_name['secondary_salespeople']._serialized_options = b'\xe0A\x01\xe0A\x06\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_ORDER'].fields_by_name['secondary_traffickers']._loaded_options = None
    _globals['_ORDER'].fields_by_name['secondary_traffickers']._serialized_options = b'\xe0A\x01\xe0A\x06\xfaA\x1f\n\x1dadmanager.googleapis.com/User'
    _globals['_ORDER'].fields_by_name['applied_labels']._loaded_options = None
    _globals['_ORDER'].fields_by_name['applied_labels']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER'].fields_by_name['effective_applied_labels']._loaded_options = None
    _globals['_ORDER'].fields_by_name['effective_applied_labels']._serialized_options = b'\xe0A\x03'
    _globals['_ORDER'].fields_by_name['custom_field_values']._loaded_options = None
    _globals['_ORDER'].fields_by_name['custom_field_values']._serialized_options = b'\xe0A\x01'
    _globals['_ORDER']._loaded_options = None
    _globals['_ORDER']._serialized_options = b'\xeaAW\n\x1eadmanager.googleapis.com/Order\x12&networks/{network_code}/orders/{order}*\x06orders2\x05order'
    _globals['_ORDER']._serialized_start = 305
    _globals['_ORDER']._serialized_end = 2247