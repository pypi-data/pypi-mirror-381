"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/data_link_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import data_link_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_data__link__status__pb2
from ......google.ads.googleads.v19.resources import data_link_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_data__link__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/ads/googleads/v19/services/data_link_service.proto\x12!google.ads.googleads.v19.services\x1a5google/ads/googleads/v19/enums/data_link_status.proto\x1a2google/ads/googleads/v19/resources/data_link.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"w\n\x15CreateDataLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12D\n\tdata_link\x18\x02 \x01(\x0b2,.google.ads.googleads.v19.resources.DataLinkB\x03\xe0A\x02"W\n\x16CreateDataLinkResponse\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/DataLink"s\n\x15RemoveDataLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12@\n\rresource_name\x18\x02 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/DataLink"W\n\x16RemoveDataLinkResponse\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/DataLink"\xd5\x01\n\x15UpdateDataLinkRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12`\n\x10data_link_status\x18\x02 \x01(\x0e2A.google.ads.googleads.v19.enums.DataLinkStatusEnum.DataLinkStatusB\x03\xe0A\x02\x12@\n\rresource_name\x18\x03 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/DataLink"W\n\x16UpdateDataLinkResponse\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/DataLink2\x85\x06\n\x0fDataLinkService\x12\xd9\x01\n\x0eCreateDataLink\x128.google.ads.googleads.v19.services.CreateDataLinkRequest\x1a9.google.ads.googleads.v19.services.CreateDataLinkResponse"R\xdaA\x15customer_id,data_link\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:create:\x01*\x12\xdd\x01\n\x0eRemoveDataLink\x128.google.ads.googleads.v19.services.RemoveDataLinkRequest\x1a9.google.ads.googleads.v19.services.RemoveDataLinkResponse"V\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:remove:\x01*\x12\xee\x01\n\x0eUpdateDataLink\x128.google.ads.googleads.v19.services.UpdateDataLinkRequest\x1a9.google.ads.googleads.v19.services.UpdateDataLinkResponse"g\xdaA*customer_id,data_link_status,resource_name\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:update:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v19.servicesB\x14DataLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.data_link_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x14DataLinkServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_CREATEDATALINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_CREATEDATALINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATALINKREQUEST'].fields_by_name['data_link']._loaded_options = None
    _globals['_CREATEDATALINKREQUEST'].fields_by_name['data_link']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEDATALINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_CREATEDATALINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_REMOVEDATALINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_REMOVEDATALINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_REMOVEDATALINKREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEDATALINKREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_REMOVEDATALINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_REMOVEDATALINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['data_link_status']._loaded_options = None
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['data_link_status']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_UPDATEDATALINKREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_UPDATEDATALINKRESPONSE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_UPDATEDATALINKRESPONSE'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/DataLink'
    _globals['_DATALINKSERVICE']._loaded_options = None
    _globals['_DATALINKSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_DATALINKSERVICE'].methods_by_name['CreateDataLink']._loaded_options = None
    _globals['_DATALINKSERVICE'].methods_by_name['CreateDataLink']._serialized_options = b'\xdaA\x15customer_id,data_link\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:create:\x01*'
    _globals['_DATALINKSERVICE'].methods_by_name['RemoveDataLink']._loaded_options = None
    _globals['_DATALINKSERVICE'].methods_by_name['RemoveDataLink']._serialized_options = b'\xdaA\x19customer_id,resource_name\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:remove:\x01*'
    _globals['_DATALINKSERVICE'].methods_by_name['UpdateDataLink']._loaded_options = None
    _globals['_DATALINKSERVICE'].methods_by_name['UpdateDataLink']._serialized_options = b'\xdaA*customer_id,data_link_status,resource_name\x82\xd3\xe4\x93\x024"//v19/customers/{customer_id=*}/dataLinks:update:\x01*'
    _globals['_CREATEDATALINKREQUEST']._serialized_start = 318
    _globals['_CREATEDATALINKREQUEST']._serialized_end = 437
    _globals['_CREATEDATALINKRESPONSE']._serialized_start = 439
    _globals['_CREATEDATALINKRESPONSE']._serialized_end = 526
    _globals['_REMOVEDATALINKREQUEST']._serialized_start = 528
    _globals['_REMOVEDATALINKREQUEST']._serialized_end = 643
    _globals['_REMOVEDATALINKRESPONSE']._serialized_start = 645
    _globals['_REMOVEDATALINKRESPONSE']._serialized_end = 732
    _globals['_UPDATEDATALINKREQUEST']._serialized_start = 735
    _globals['_UPDATEDATALINKREQUEST']._serialized_end = 948
    _globals['_UPDATEDATALINKRESPONSE']._serialized_start = 950
    _globals['_UPDATEDATALINKRESPONSE']._serialized_end = 1037
    _globals['_DATALINKSERVICE']._serialized_start = 1040
    _globals['_DATALINKSERVICE']._serialized_end = 1813