"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/customer_client.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import customer_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_customer__status__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v19/resources/customer_client.proto\x12"google.ads.googleads.v19.resources\x1a4google/ads/googleads/v19/enums/customer_status.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x8d\x06\n\x0eCustomerClient\x12F\n\rresource_name\x18\x01 \x01(\tB/\xe0A\x03\xfaA)\n\'googleads.googleapis.com/CustomerClient\x12G\n\x0fclient_customer\x18\x0c \x01(\tB)\xe0A\x03\xfaA#\n!googleads.googleapis.com/CustomerH\x00\x88\x01\x01\x12\x18\n\x06hidden\x18\r \x01(\x08B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x17\n\x05level\x18\x0e \x01(\x03B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1b\n\ttime_zone\x18\x0f \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1e\n\x0ctest_account\x18\x10 \x01(\x08B\x03\xe0A\x03H\x04\x88\x01\x01\x12\x19\n\x07manager\x18\x11 \x01(\x08B\x03\xe0A\x03H\x05\x88\x01\x01\x12"\n\x10descriptive_name\x18\x12 \x01(\tB\x03\xe0A\x03H\x06\x88\x01\x01\x12\x1f\n\rcurrency_code\x18\x13 \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01\x12\x14\n\x02id\x18\x14 \x01(\x03B\x03\xe0A\x03H\x08\x88\x01\x01\x12>\n\x0eapplied_labels\x18\x15 \x03(\tB&\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Label\x12V\n\x06status\x18\x16 \x01(\x0e2A.google.ads.googleads.v19.enums.CustomerStatusEnum.CustomerStatusB\x03\xe0A\x03:j\xeaAg\n\'googleads.googleapis.com/CustomerClient\x12<customers/{customer_id}/customerClients/{client_customer_id}B\x12\n\x10_client_customerB\t\n\x07_hiddenB\x08\n\x06_levelB\x0c\n\n_time_zoneB\x0f\n\r_test_accountB\n\n\x08_managerB\x13\n\x11_descriptive_nameB\x10\n\x0e_currency_codeB\x05\n\x03_idB\x85\x02\n&com.google.ads.googleads.v19.resourcesB\x13CustomerClientProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.customer_client_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x13CustomerClientProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_CUSTOMERCLIENT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['resource_name']._serialized_options = b"\xe0A\x03\xfaA)\n'googleads.googleapis.com/CustomerClient"
    _globals['_CUSTOMERCLIENT'].fields_by_name['client_customer']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['client_customer']._serialized_options = b'\xe0A\x03\xfaA#\n!googleads.googleapis.com/Customer'
    _globals['_CUSTOMERCLIENT'].fields_by_name['hidden']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['hidden']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['level']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['level']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['time_zone']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['time_zone']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['test_account']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['test_account']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['manager']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['manager']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['descriptive_name']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['descriptive_name']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['currency_code']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['currency_code']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['id']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT'].fields_by_name['applied_labels']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['applied_labels']._serialized_options = b'\xe0A\x03\xfaA \n\x1egoogleads.googleapis.com/Label'
    _globals['_CUSTOMERCLIENT'].fields_by_name['status']._loaded_options = None
    _globals['_CUSTOMERCLIENT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERCLIENT']._loaded_options = None
    _globals['_CUSTOMERCLIENT']._serialized_options = b"\xeaAg\n'googleads.googleapis.com/CustomerClient\x12<customers/{customer_id}/customerClients/{client_customer_id}"
    _globals['_CUSTOMERCLIENT']._serialized_start = 211
    _globals['_CUSTOMERCLIENT']._serialized_end = 992