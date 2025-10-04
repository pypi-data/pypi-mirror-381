"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/lfpproviders.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n;google/shopping/merchant/accounts/v1beta/lfpproviders.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1bgoogle/protobuf/empty.proto"\xf4\x01\n\x0bLfpProvider\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bregion_code\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x03 \x01(\t:\xa1\x01\xeaA\x9d\x01\n&merchantapi.googleapis.com/LfpProvider\x12Xaccounts/{account}/omnichannelSettings/{omnichannel_setting}/lfpProviders/{lfp_provider}*\x0clfpProviders2\x0blfpProvider"\x91\x01\n\x17FindLfpProvidersRequest\x12E\n\x06parent\x18\x01 \x01(\tB5\xe0A\x02\xfaA/\n-merchantapi.googleapis.com/OmnichannelSetting\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x81\x01\n\x18FindLfpProvidersResponse\x12L\n\rlfp_providers\x18\x01 \x03(\x0b25.google.shopping.merchant.accounts.v1beta.LfpProvider\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"x\n\x16LinkLfpProviderRequest\x12<\n\x04name\x18\x01 \x01(\tB.\xe0A\x02\xfaA(\n&merchantapi.googleapis.com/LfpProvider\x12 \n\x13external_account_id\x18\x02 \x01(\tB\x03\xe0A\x02"C\n\x17LinkLfpProviderResponse\x12(\n\x08response\x18\x01 \x01(\x0b2\x16.google.protobuf.Empty2\xdd\x04\n\x13LfpProvidersService\x12\xf8\x01\n\x10FindLfpProviders\x12A.google.shopping.merchant.accounts.v1beta.FindLfpProvidersRequest\x1aB.google.shopping.merchant.accounts.v1beta.FindLfpProvidersResponse"]\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/accounts/v1beta/{parent=accounts/*/omnichannelSettings/*}/lfpProviders:find\x12\x81\x02\n\x0fLinkLfpProvider\x12@.google.shopping.merchant.accounts.v1beta.LinkLfpProviderRequest\x1aA.google.shopping.merchant.accounts.v1beta.LinkLfpProviderResponse"i\xdaA\x04name\x82\xd3\xe4\x93\x02\\"W/accounts/v1beta/{name=accounts/*/omnichannelSettings/*/lfpProviders/*}:linkLfpProvider:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x93\x01\n,com.google.shopping.merchant.accounts.v1betaB\x11LfpProvidersProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.lfpproviders_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\x11LfpProvidersProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
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
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['FindLfpProviders']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02N\x12L/accounts/v1beta/{parent=accounts/*/omnichannelSettings/*}/lfpProviders:find'
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['LinkLfpProvider']._loaded_options = None
    _globals['_LFPPROVIDERSSERVICE'].methods_by_name['LinkLfpProvider']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\\"W/accounts/v1beta/{name=accounts/*/omnichannelSettings/*/lfpProviders/*}:linkLfpProvider:\x01*'
    _globals['_LFPPROVIDER']._serialized_start = 250
    _globals['_LFPPROVIDER']._serialized_end = 494
    _globals['_FINDLFPPROVIDERSREQUEST']._serialized_start = 497
    _globals['_FINDLFPPROVIDERSREQUEST']._serialized_end = 642
    _globals['_FINDLFPPROVIDERSRESPONSE']._serialized_start = 645
    _globals['_FINDLFPPROVIDERSRESPONSE']._serialized_end = 774
    _globals['_LINKLFPPROVIDERREQUEST']._serialized_start = 776
    _globals['_LINKLFPPROVIDERREQUEST']._serialized_end = 896
    _globals['_LINKLFPPROVIDERRESPONSE']._serialized_start = 898
    _globals['_LINKLFPPROVIDERRESPONSE']._serialized_end = 965
    _globals['_LFPPROVIDERSSERVICE']._serialized_start = 968
    _globals['_LFPPROVIDERSSERVICE']._serialized_end = 1573