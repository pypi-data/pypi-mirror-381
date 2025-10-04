"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/resources/customer_user_access.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import access_role_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_access__role__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v20/resources/customer_user_access.proto\x12"google.ads.googleads.v20.resources\x1a0google/ads/googleads/v20/enums/access_role.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfb\x03\n\x12CustomerUserAccess\x12J\n\rresource_name\x18\x01 \x01(\tB3\xe0A\x05\xfaA-\n+googleads.googleapis.com/CustomerUserAccess\x12\x14\n\x07user_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x1f\n\remail_address\x18\x03 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12N\n\x0baccess_role\x18\x04 \x01(\x0e29.google.ads.googleads.v20.enums.AccessRoleEnum.AccessRole\x12+\n\x19access_creation_date_time\x18\x06 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12,\n\x1ainviter_user_email_address\x18\x07 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01:h\xeaAe\n+googleads.googleapis.com/CustomerUserAccess\x126customers/{customer_id}/customerUserAccesses/{user_id}B\x10\n\x0e_email_addressB\x1c\n\x1a_access_creation_date_timeB\x1d\n\x1b_inviter_user_email_addressB\x89\x02\n&com.google.ads.googleads.v20.resourcesB\x17CustomerUserAccessProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.resources.customer_user_access_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v20.resourcesB\x17CustomerUserAccessProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v20/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V20.Resources\xca\x02"Google\\Ads\\GoogleAds\\V20\\Resources\xea\x02&Google::Ads::GoogleAds::V20::Resources'
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA-\n+googleads.googleapis.com/CustomerUserAccess'
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['user_id']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['user_id']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['email_address']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['email_address']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['access_creation_date_time']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['access_creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['inviter_user_email_address']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS'].fields_by_name['inviter_user_email_address']._serialized_options = b'\xe0A\x03'
    _globals['_CUSTOMERUSERACCESS']._loaded_options = None
    _globals['_CUSTOMERUSERACCESS']._serialized_options = b'\xeaAe\n+googleads.googleapis.com/CustomerUserAccess\x126customers/{customer_id}/customerUserAccesses/{user_id}'
    _globals['_CUSTOMERUSERACCESS']._serialized_start = 212
    _globals['_CUSTOMERUSERACCESS']._serialized_end = 719