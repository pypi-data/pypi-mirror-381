"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/programmatic_buyer_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/admanager/v1/programmatic_buyer_messages.proto\x12\x17google.ads.admanager.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xe4\x04\n\x11ProgrammaticBuyer\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12"\n\x10buyer_account_id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1e\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12#\n\x11parent_account_id\x18\x06 \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12#\n\x11partner_client_id\x18\x07 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x18\n\x06agency\x18\t \x01(\x08B\x03\xe0A\x03H\x04\x88\x01\x01\x12)\n\x17preferred_deals_enabled\x18\x0c \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01\x121\n\x1fprogrammatic_guaranteed_enabled\x18\r \x01(\x08B\x03\xe0A\x03H\x06\x88\x01\x01:\x98\x01\xeaA\x94\x01\n*admanager.googleapis.com/ProgrammaticBuyer\x12?networks/{network_code}/programmaticBuyers/{programmatic_buyer}*\x12programmaticBuyers2\x11programmaticBuyerB\x13\n\x11_buyer_account_idB\x0f\n\r_display_nameB\x14\n\x12_parent_account_idB\x14\n\x12_partner_client_idB\t\n\x07_agencyB\x1a\n\x18_preferred_deals_enabledB"\n _programmatic_guaranteed_enabledB\xd2\x01\n\x1bcom.google.ads.admanager.v1B\x1eProgrammaticBuyerMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.programmatic_buyer_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x1eProgrammaticBuyerMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['name']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['buyer_account_id']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['buyer_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['display_name']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['parent_account_id']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['parent_account_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['partner_client_id']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['partner_client_id']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['agency']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['agency']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['preferred_deals_enabled']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['preferred_deals_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER'].fields_by_name['programmatic_guaranteed_enabled']._loaded_options = None
    _globals['_PROGRAMMATICBUYER'].fields_by_name['programmatic_guaranteed_enabled']._serialized_options = b'\xe0A\x03'
    _globals['_PROGRAMMATICBUYER']._loaded_options = None
    _globals['_PROGRAMMATICBUYER']._serialized_options = b'\xeaA\x94\x01\n*admanager.googleapis.com/ProgrammaticBuyer\x12?networks/{network_code}/programmaticBuyers/{programmatic_buyer}*\x12programmaticBuyers2\x11programmaticBuyer'
    _globals['_PROGRAMMATICBUYER']._serialized_start = 147
    _globals['_PROGRAMMATICBUYER']._serialized_end = 759