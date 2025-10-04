"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/lfpproviders.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1/lfpproviders.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xf4\x01\n\x0bLfpProvider\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bregion_code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t:\xa1\x01\xeaA\x9d\x01\n&merchantapi.googleapis.com/LfpProvider\x12Xaccounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}*\x0clfpProviders2\x0blfpProvider"\x91\x01\n\x17FindLfpProvidersRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"}\n\x18FindLfpProvidersResponse\x12H\n\rlfp_providers\x18\x01 \x03(\x0b21.google.shopping.merchant.accounts.v1.LfpProvider\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"x\n\x16LinkLfpProviderRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&merchantapi.googleapis.com/LfpProvider\x12 \n\x13external_account_id\x18\x02 \x01(\tB\x03\xe0A\x02"C\n\x17LinkLfpProviderResponse\x12(\n\x08response\x18\x01 \x01(\x0b2\x16.google.protobuf.Empty2\xc5\x04\n\x13LfpProvidersService\x12\xec\x01\n\x10FindLfpProviders\x12=.google.shopping.merchant.accounts.v1.FindLfpProvidersRequest\x1a>.google.shopping.merchant.accounts.v1.FindLfpProvidersResponse"Y\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/accounts/v1/{parent=accounts/*/omnichannelSettings/*}/lfpProviders:find\x12\xf5\x01\n\x0fLinkLfpProvider\x12<.google.shopping.merchant.accounts.v1.LinkLfpProviderRequest\x1a=.google.shopping.merchant.accounts.v1.LinkLfpProviderResponse"e\xdaA\x04name\x82\xd3\xe4\x93\x02X"S/accounts/v1/{name=accounts/*/omnichannelSettings/*/lfpProviders/*}:linkLfpProvider:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x84\x02\n(com.google.shopping.merchant.accounts.v1B\x11LfpProvidersProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.lfpproviders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\x11LfpProvidersProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_LFPPROVIDER'].fields_by_name['name']._loaded_options = None
    _globals['_LFPPROVIDER'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_LFPPROVIDER'].fields_by_name['region_code']._loaded_options = None
    _globals['_LFPPROVIDER'].fields_by_name['region_code']._serialized_options = b'\xe0A\x03'
    _globals['_LFPPROVIDER']._loaded_options = None
    _globals['_LFPPROVIDER']._serialized_options = b'\xeaA\x9d\x01\n&merchantapi.googleapis.com/LfpProvider\x12Xaccounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}*\x0clfpProviders2\x0blfpProvider'
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting'
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_FINDLFPPROVIDERSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LINKLFPPROVIDERREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_LINKLFPPROVIDERREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&merchantapi.googleapis.com/LfpProvider'
    _globals['_LINKLFPPROVIDERREQUEST'].fields_by_name['external_account_id']._loaded_options = None
    _globals['_LINKLFPPROVIDERREQUEST'].fields_by_name['external_account_id']._serialized_options = b'\xe0A\x02'
    _globals['_LFPPROVIDERSSERVICE']._loaded_options = None
    _globals['_LFPPROVIDERSSERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['FindLfpProviders']._loaded_options = None
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['FindLfpProviders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02J\x12H/accounts/v1/{parent=accounts/*/omnichannelSettings/*}/lfpProviders:find'
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['LinkLfpProvider']._loaded_options = None
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['LinkLfpProvider']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02X"S/accounts/v1/{name=accounts/*/omnichannelSettings/*/lfpProviders/*}:linkLfpProvider:\x01*'
    _globals['_LFPPROVIDER']._serialized_start = 242
    _globals['_LFPPROVIDER']._serialized_end = 486
    _globals['_FINDLFPPROVIDERSREQUEST']._serialized_start = 489
    _globals['_FINDLFPPROVIDERSREQUEST']._serialized_end = 634
    _globals['_FINDLFPPROVIDERSRESPONSE']._serialized_start = 636
    _globals['_FINDLFPPROVIDERSRESPONSE']._serialized_end = 761
    _globals['_LINKLFPPROVIDERREQUEST']._serialized_start = 763
    _globals['_LINKLFPPROVIDERREQUEST']._serialized_end = 883
    _globals['_LINKLFPPROVIDERRESPONSE']._serialized_start = 885
    _globals['_LINKLFPPROVIDERRESPONSE']._serialized_end = 952
    _globals['_LFPPROVIDERSSERVICE']._serialized_start = 955
    _globals['_LFPPROVIDERSSERVICE']._serialized_end = 1536