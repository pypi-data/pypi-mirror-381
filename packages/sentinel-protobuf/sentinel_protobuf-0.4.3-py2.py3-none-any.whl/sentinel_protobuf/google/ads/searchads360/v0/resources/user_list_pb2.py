"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/searchads360/v0/resources/user_list.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.searchads360.v0.enums import user_list_type_pb2 as google_dot_ads_dot_searchads360_dot_v0_dot_enums_dot_user__list__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n4google/ads/searchads360/v0/resources/user_list.proto\x12$google.ads.searchads360.v0.resources\x1a5google/ads/searchads360/v0/enums/user_list_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xb9\x02\n\x08UserList\x12C\n\rresource_name\x18\x01 \x01(\tB,\xe0A\x05\xfaA&\n$searchads360.googleapis.com/UserList\x12\x14\n\x02id\x18\x19 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x11\n\x04name\x18\x1b \x01(\tH\x01\x88\x01\x01\x12R\n\x04type\x18\r \x01(\x0e2?.google.ads.searchads360.v0.enums.UserListTypeEnum.UserListTypeB\x03\xe0A\x03:[\xeaAX\n$searchads360.googleapis.com/UserList\x120customers/{customer_id}/userLists/{user_list_id}B\x05\n\x03_idB\x07\n\x05_nameB\x8d\x02\n(com.google.ads.searchads360.v0.resourcesB\rUserListProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.searchads360.v0.resources.user_list_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.ads.searchads360.v0.resourcesB\rUserListProtoP\x01ZMgoogle.golang.org/genproto/googleapis/ads/searchads360/v0/resources;resources\xa2\x02\x07GASA360\xaa\x02$Google.Ads.SearchAds360.V0.Resources\xca\x02$Google\\Ads\\SearchAds360\\V0\\Resources\xea\x02(Google::Ads::SearchAds360::V0::Resources'
    _globals['_USERLIST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA&\n$searchads360.googleapis.com/UserList'
    _globals['_USERLIST'].fields_by_name['id']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST'].fields_by_name['type']._loaded_options = None
    _globals['_USERLIST'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_USERLIST']._loaded_options = None
    _globals['_USERLIST']._serialized_options = b'\xeaAX\n$searchads360.googleapis.com/UserList\x120customers/{customer_id}/userLists/{user_list_id}'
    _globals['_USERLIST']._serialized_start = 210
    _globals['_USERLIST']._serialized_end = 523