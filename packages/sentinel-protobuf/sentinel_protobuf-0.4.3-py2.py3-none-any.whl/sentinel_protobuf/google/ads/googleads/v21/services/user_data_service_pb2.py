"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/user_data_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import offline_user_data_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_offline__user__data__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v21/services/user_data_service.proto\x12!google.ads.googleads.v21.services\x1a7google/ads/googleads/v21/common/offline_user_data.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xf9\x01\n\x15UploadUserDataRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12M\n\noperations\x18\x03 \x03(\x0b24.google.ads.googleads.v21.services.UserDataOperationB\x03\xe0A\x02\x12k\n!customer_match_user_list_metadata\x18\x02 \x01(\x0b2>.google.ads.googleads.v21.common.CustomerMatchUserListMetadataH\x00B\n\n\x08metadata"\x9a\x01\n\x11UserDataOperation\x12;\n\x06create\x18\x01 \x01(\x0b2).google.ads.googleads.v21.common.UserDataH\x00\x12;\n\x06remove\x18\x02 \x01(\x0b2).google.ads.googleads.v21.common.UserDataH\x00B\x0b\n\toperation"\x92\x01\n\x16UploadUserDataResponse\x12\x1d\n\x10upload_date_time\x18\x03 \x01(\tH\x00\x88\x01\x01\x12&\n\x19received_operations_count\x18\x04 \x01(\x05H\x01\x88\x01\x01B\x13\n\x11_upload_date_timeB\x1c\n\x1a_received_operations_count2\x9a\x02\n\x0fUserDataService\x12\xbf\x01\n\x0eUploadUserData\x128.google.ads.googleads.v21.services.UploadUserDataRequest\x1a9.google.ads.googleads.v21.services.UploadUserDataResponse"8\x82\xd3\xe4\x93\x022"-/v21/customers/{customer_id=*}:uploadUserData:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v21.servicesB\x14UserDataServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.user_data_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x14UserDataServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_UPLOADUSERDATAREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPLOADUSERDATAREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPLOADUSERDATAREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_UPLOADUSERDATAREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_USERDATASERVICE']._loaded_options = None
    _globals['_USERDATASERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_USERDATASERVICE'].methods_by_name['UploadUserData']._loaded_options = None
    _globals['_USERDATASERVICE'].methods_by_name['UploadUserData']._serialized_options = b'\x82\xd3\xe4\x93\x022"-/v21/customers/{customer_id=*}:uploadUserData:\x01*'
    _globals['_UPLOADUSERDATAREQUEST']._serialized_start = 242
    _globals['_UPLOADUSERDATAREQUEST']._serialized_end = 491
    _globals['_USERDATAOPERATION']._serialized_start = 494
    _globals['_USERDATAOPERATION']._serialized_end = 648
    _globals['_UPLOADUSERDATARESPONSE']._serialized_start = 651
    _globals['_UPLOADUSERDATARESPONSE']._serialized_end = 797
    _globals['_USERDATASERVICE']._serialized_start = 800
    _globals['_USERDATASERVICE']._serialized_end = 1082