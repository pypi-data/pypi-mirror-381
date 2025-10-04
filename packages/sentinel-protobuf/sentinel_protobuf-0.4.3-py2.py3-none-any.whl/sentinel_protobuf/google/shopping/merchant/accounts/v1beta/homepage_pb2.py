"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/shopping/merchant/accounts/v1beta/homepage.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/shopping/merchant/accounts/v1beta/homepage.proto\x12(google.shopping.merchant.accounts.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto"\xae\x01\n\x08Homepage\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x15\n\x03uri\x18\x02 \x01(\tB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x14\n\x07claimed\x18\x03 \x01(\x08B\x03\xe0A\x03:Z\xeaAW\n#merchantapi.googleapis.com/Homepage\x12\x1baccounts/{account}/homepage*\thomepages2\x08homepageB\x06\n\x04_uri"O\n\x12GetHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage"\x98\x01\n\x15UpdateHomepageRequest\x12I\n\x08homepage\x18\x01 \x01(\x0b22.google.shopping.merchant.accounts.v1beta.HomepageB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"Q\n\x14ClaimHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage"S\n\x16UnclaimHomepageRequest\x129\n\x04name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage2\x8d\x07\n\x0fHomepageService\x12\xbb\x01\n\x0bGetHomepage\x12<.google.shopping.merchant.accounts.v1beta.GetHomepageRequest\x1a2.google.shopping.merchant.accounts.v1beta.Homepage":\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/accounts/v1beta/{name=accounts/*/homepage}\x12\xe4\x01\n\x0eUpdateHomepage\x12?.google.shopping.merchant.accounts.v1beta.UpdateHomepageRequest\x1a2.google.shopping.merchant.accounts.v1beta.Homepage"]\xdaA\x14homepage,update_mask\x82\xd3\xe4\x93\x02@24/accounts/v1beta/{homepage.name=accounts/*/homepage}:\x08homepage\x12\xc1\x01\n\rClaimHomepage\x12>.google.shopping.merchant.accounts.v1beta.ClaimHomepageRequest\x1a2.google.shopping.merchant.accounts.v1beta.Homepage"<\x82\xd3\xe4\x93\x026"1/accounts/v1beta/{name=accounts/*/homepage}:claim:\x01*\x12\xc7\x01\n\x0fUnclaimHomepage\x12@.google.shopping.merchant.accounts.v1beta.UnclaimHomepageRequest\x1a2.google.shopping.merchant.accounts.v1beta.Homepage">\x82\xd3\xe4\x93\x028"3/accounts/v1beta/{name=accounts/*/homepage}:unclaim:\x01*\x1aG\xcaA\x1amerchantapi.googleapis.com\xd2A\'https://www.googleapis.com/auth/contentB\x8f\x01\n,com.google.shopping.merchant.accounts.v1betaB\rHomepageProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.shopping.merchant.accounts.v1beta.homepage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n,com.google.shopping.merchant.accounts.v1betaB\rHomepageProtoP\x01ZNcloud.google.com/go/shopping/merchant/accounts/apiv1beta/accountspb;accountspb'
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
    _globals['_UPDATEHOMEPAGEREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_CLAIMHOMEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage'
    _globals['_UNCLAIMHOMEPAGEREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_UNCLAIMHOMEPAGEREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA%\n#merchantapi.googleapis.com/Homepage'
    _globals['_HOMEPAGESERVICE']._loaded_options = None
    _globals['_HOMEPAGESERVICE']._serialized_options = b"\xcaA\x1amerchantapi.googleapis.com\xd2A'https://www.googleapis.com/auth/content"
    _globals['_HOMEPAGESERVICE'].methods_by_name['GetHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['GetHomepage']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02-\x12+/accounts/v1beta/{name=accounts/*/homepage}'
    _globals['_HOMEPAGESERVICE'].methods_by_name['UpdateHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['UpdateHomepage']._serialized_options = b'\xdaA\x14homepage,update_mask\x82\xd3\xe4\x93\x02@24/accounts/v1beta/{homepage.name=accounts/*/homepage}:\x08homepage'
    _globals['_HOMEPAGESERVICE'].methods_by_name['ClaimHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['ClaimHomepage']._serialized_options = b'\x82\xd3\xe4\x93\x026"1/accounts/v1beta/{name=accounts/*/homepage}:claim:\x01*'
    _globals['_HOMEPAGESERVICE'].methods_by_name['UnclaimHomepage']._loaded_options = None
    _globals['_HOMEPAGESERVICE'].methods_by_name['UnclaimHomepage']._serialized_options = b'\x82\xd3\xe4\x93\x028"3/accounts/v1beta/{name=accounts/*/homepage}:unclaim:\x01*'
    _globals['_HOMEPAGE']._serialized_start = 251
    _globals['_HOMEPAGE']._serialized_end = 425
    _globals['_GETHOMEPAGEREQUEST']._serialized_start = 427
    _globals['_GETHOMEPAGEREQUEST']._serialized_end = 506
    _globals['_UPDATEHOMEPAGEREQUEST']._serialized_start = 509
    _globals['_UPDATEHOMEPAGEREQUEST']._serialized_end = 661
    _globals['_CLAIMHOMEPAGEREQUEST']._serialized_start = 663
    _globals['_CLAIMHOMEPAGEREQUEST']._serialized_end = 744
    _globals['_UNCLAIMHOMEPAGEREQUEST']._serialized_start = 746
    _globals['_UNCLAIMHOMEPAGEREQUEST']._serialized_end = 829
    _globals['_HOMEPAGESERVICE']._serialized_start = 832
    _globals['_HOMEPAGESERVICE']._serialized_end = 1741