"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/audience_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import response_content_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_response__content__type__pb2
from ......google.ads.googleads.v21.resources import audience_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_audience__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/ads/googleads/v21/services/audience_service.proto\x12!google.ads.googleads.v21.services\x1a:google/ads/googleads/v21/enums/response_content_type.proto\x1a1google/ads/googleads/v21/resources/audience.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\x9d\x02\n\x16MutateAudiencesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12M\n\noperations\x18\x02 \x03(\x0b24.google.ads.googleads.v21.services.AudienceOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08\x12j\n\x15response_content_type\x18\x05 \x01(\x0e2K.google.ads.googleads.v21.enums.ResponseContentTypeEnum.ResponseContentType"\x96\x01\n\x17MutateAudiencesResponse\x12H\n\x07results\x18\x01 \x03(\x0b27.google.ads.googleads.v21.services.MutateAudienceResult\x121\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.Status"\xd1\x01\n\x11AudienceOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12>\n\x06create\x18\x01 \x01(\x0b2,.google.ads.googleads.v21.resources.AudienceH\x00\x12>\n\x06update\x18\x02 \x01(\x0b2,.google.ads.googleads.v21.resources.AudienceH\x00B\x0b\n\toperation"\x95\x01\n\x14MutateAudienceResult\x12=\n\rresource_name\x18\x01 \x01(\tB&\xfaA#\n!googleads.googleapis.com/Audience\x12>\n\x08audience\x18\x02 \x01(\x0b2,.google.ads.googleads.v21.resources.Audience2\xb8\x02\n\x0fAudienceService\x12\xdd\x01\n\x0fMutateAudiences\x129.google.ads.googleads.v21.services.MutateAudiencesRequest\x1a:.google.ads.googleads.v21.services.MutateAudiencesResponse"S\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x024"//v21/customers/{customer_id=*}/audiences:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x80\x02\n%com.google.ads.googleads.v21.servicesB\x14AudienceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.audience_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x14AudienceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEAUDIENCESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEAUDIENCESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEAUDIENCESREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEAUDIENCESREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEAUDIENCERESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEAUDIENCERESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA#\n!googleads.googleapis.com/Audience'
    _globals['_AUDIENCESERVICE']._loaded_options = None
    _globals['_AUDIENCESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_AUDIENCESERVICE'].methods_by_name['MutateAudiences']._loaded_options = None
    _globals['_AUDIENCESERVICE'].methods_by_name['MutateAudiences']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x024"//v21/customers/{customer_id=*}/audiences:mutate:\x01*'
    _globals['_MUTATEAUDIENCESREQUEST']._serialized_start = 381
    _globals['_MUTATEAUDIENCESREQUEST']._serialized_end = 666
    _globals['_MUTATEAUDIENCESRESPONSE']._serialized_start = 669
    _globals['_MUTATEAUDIENCESRESPONSE']._serialized_end = 819
    _globals['_AUDIENCEOPERATION']._serialized_start = 822
    _globals['_AUDIENCEOPERATION']._serialized_end = 1031
    _globals['_MUTATEAUDIENCERESULT']._serialized_start = 1034
    _globals['_MUTATEAUDIENCERESULT']._serialized_end = 1183
    _globals['_AUDIENCESERVICE']._serialized_start = 1186
    _globals['_AUDIENCESERVICE']._serialized_end = 1498