"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1/homepage.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3google/shopping/merchant/accounts/v1/homepage.proto\x12$google.shopping.merchant.accounts.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xae\x01\n\x08Homepage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x15\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x14\n\x07claimed\x18\x03 \x01(\x08B\x03\xe0A\x03:Z\xeaAW\n#merchantapi.googleapis.com/Homepage\x12\x1baccounts/{account}/homepage*\thomepages2\x08homepageB\x06\n\x04_uri"O\n\x12GetHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage"\x94\x01\n\x15UpdateHomepageRequest\x12E\n\x08homepage\x18\x01 \x01(\x0b2..google.shopping.merchant.accounts.v1.HomepageB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"i\n\x14ClaimHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage\x12\x16\n\toverwrite\x18\x02 \x01(\x08B\x03\xe0A\x01"S\n\x16UnclaimHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage2\xdd\x06\n\x0fHomepageService\x12\xaf\x01\n\x0bGetHomepage\x128.google.shopping.merchant.accounts.v1.GetHomepageRequest\x1a..google.shopping.merchant.accounts.v1.Homepage"6\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12\'/accounts/v1/{name=accounts/*/homepage}\x12\xd8\x01\n\x0eUpdateHomepage\x12;.google.shopping.merchant.accounts.v1.UpdateHomepageRequest\x1a..google.shopping.merchant.accounts.v1.Homepage"Y\xdaA\x14homepage,update_mask\x82\xd3\xe4\x93\x02<20/accounts/v1/{homepage.name=accounts/*/homepage}:\x08homepage\x12\xb5\x01\n\rClaimHomepage\x12:.google.shopping.merchant.accounts.v1.ClaimHomepageRequest\x1a..google.shopping.merchant.accounts.v1.Homepage"8\x82\xd3\xe4\x93\x022"-/accounts/v1/{name=accounts/*/homepage}:claim:\x01*\x12\xbb\x01\n\x0fUnclaimHomepage\x12<.google.shopping.merchant.accounts.v1.UnclaimHomepageRequest\x1a..google.shopping.merchant.accounts.v1.Homepage":\x82\xd3\xe4\x93\x024"//accounts/v1/{name=accounts/*/homepage}:unclaim:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x80\x02\n(com.google.shopping.merchant.accounts.v1B\rHomepageProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1.homepage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.shopping.merchant.accounts.v1B\rHomepageProtoP\x01ZJcloud.google.com/go/shopping/merchant/accounts/apiv1/accountspb;accountspb\xaa\x02$Google.Shopping.Merchant.Accounts.V1\xca\x02$Google\\Shopping\\Merchant\\Accounts\\V1\xea\x02(Google::Shopping::Merchant::Accounts::V1'
    _globals['_HOMEPAGE'].fields_by_name['name']._loaded_options = None
    _globals['_HOMEPAGE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_HOMEPAGE'].fields_by_name['uri']._loaded_options = None
    _globals['_HOMEPAGE'].fields_by_name['uri']._serialized_options = b'\xe0A\x02'
    _globals['_HOMEPAGE'].fields_by_name['claimed']._loaded_options = None
    _globals['_HOMEPAGE'].fields_by_name['claimed']._serialized_options = b'\xe0A\x03'
    _globals['_HOMEPAGE']._loaded_options = None
    _globals['_HOMEPAGE']._serialized_options = b'\xeaAW\n#merchantapi.googleapis.com/Homepage\x12\x1baccounts/{account}/homepage*\thomepages2\x08homepage'
    _globals['_GETHOMEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHOMEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage'
    _globals['_UPDATEHOMEPAGEREQUEST'].fields_by_name['homepage']._loaded_options = None
    _globals['_UPDATEHOMEPAGEREQUEST'].fields_by_name['homepage']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEHOMEPAGEREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEHOMEPAGEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage'
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['overwrite']._loaded_options = None
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['overwrite']._serialized_options = b'\xe0A\x01'
    _globals['_UNCLAIMHOMEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNCLAIMHOMEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage'
    _globals['_HOMEPAGESERVICE']._loaded_options = None
    _globals['_HOMEPAGESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_HOMEPAGESERVICE'].methods_by_name['GetHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['GetHomepage']._serialized_options = b"\xdaA\x04name\x82\xd3\xe4\x93\x02)\x12'/accounts/v1/{name=accounts/*/homepage}"
    _globals['_HOMEPAGESERVICE'].methods_by_name['UpdateHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['UpdateHomepage']._serialized_options = b'\xdaA\x14homepage,update_mask\x82\xd3\xe4\x93\x02<20/accounts/v1/{homepage.name=accounts/*/homepage}:\x08homepage'
    _globals['_HOMEPAGESERVICE'].methods_by_name['ClaimHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['ClaimHomepage']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/accounts/v1/{name=accounts/*/homepage}:claim:\x01*'
    _globals['_HOMEPAGESERVICE'].methods_by_name['UnclaimHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['UnclaimHomepage']._serialized_options = b'\x82\xd3\xe4\x93\x024"//accounts/v1/{name=accounts/*/homepage}:unclaim:\x01*'
    _globals['_HOMEPAGE']._serialized_start = 243
    _globals['_HOMEPAGE']._serialized_end = 417
    _globals['_GETHOMEPAGEREQUEST']._serialized_start = 419
    _globals['_GETHOMEPAGEREQUEST']._serialized_end = 498
    _globals['_UPDATEHOMEPAGEREQUEST']._serialized_start = 501
    _globals['_UPDATEHOMEPAGEREQUEST']._serialized_end = 649
    _globals['_CLAIMHOMEPAGEREQUEST']._serialized_start = 651
    _globals['_CLAIMHOMEPAGEREQUEST']._serialized_end = 756
    _globals['_UNCLAIMHOMEPAGEREQUEST']._serialized_start = 758
    _globals['_UNCLAIMHOMEPAGEREQUEST']._serialized_end = 841
    _globals['_HOMEPAGESERVICE']._serialized_start = 844
    _globals['_HOMEPAGESERVICE']._serialized_end = 1705