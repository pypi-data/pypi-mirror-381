"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/identity_verification_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.enums import identity_verification_program_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_identity__verification__program__pb2
from ......google.ads.googleads.v20.enums import identity_verification_program_status_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_enums_dot_identity__verification__program__status__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nEgoogle/ads/googleads/v20/services/identity_verification_service.proto\x12!google.ads.googleads.v20.services\x1aBgoogle/ads/googleads/v20/enums/identity_verification_program.proto\x1aIgoogle/ads/googleads/v20/enums/identity_verification_program_status.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/protobuf/empty.proto"\xbc\x01\n StartIdentityVerificationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12~\n\x14verification_program\x18\x02 \x01(\x0e2[.google.ads.googleads.v20.enums.IdentityVerificationProgramEnum.IdentityVerificationProgramB\x03\xe0A\x02":\n\x1eGetIdentityVerificationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02"y\n\x1fGetIdentityVerificationResponse\x12V\n\x15identity_verification\x18\x01 \x03(\x0b27.google.ads.googleads.v20.services.IdentityVerification"\xaa\x03\n\x14IdentityVerification\x12y\n\x14verification_program\x18\x01 \x01(\x0e2[.google.ads.googleads.v20.enums.IdentityVerificationProgramEnum.IdentityVerificationProgram\x12r\n!identity_verification_requirement\x18\x02 \x01(\x0b2B.google.ads.googleads.v20.services.IdentityVerificationRequirementH\x00\x88\x01\x01\x12c\n\x15verification_progress\x18\x03 \x01(\x0b2?.google.ads.googleads.v20.services.IdentityVerificationProgressH\x01\x88\x01\x01B$\n"_identity_verification_requirementB\x18\n\x16_verification_progress"\xdc\x01\n\x1cIdentityVerificationProgress\x12\x7f\n\x0eprogram_status\x18\x01 \x01(\x0e2g.google.ads.googleads.v20.enums.IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus\x12\'\n\x1finvitation_link_expiration_time\x18\x02 \x01(\t\x12\x12\n\naction_url\x18\x03 \x01(\t"z\n\x1fIdentityVerificationRequirement\x12(\n verification_start_deadline_time\x18\x01 \x01(\t\x12-\n%verification_completion_deadline_time\x18\x02 \x01(\t2\xb8\x04\n\x1bIdentityVerificationService\x12\xe0\x01\n\x19StartIdentityVerification\x12C.google.ads.googleads.v20.services.StartIdentityVerificationRequest\x1a\x16.google.protobuf.Empty"f\xdaA customer_id,verification_program\x82\xd3\xe4\x93\x02="8/v20/customers/{customer_id=*}:startIdentityVerification:\x01*\x12\xee\x01\n\x17GetIdentityVerification\x12A.google.ads.googleads.v20.services.GetIdentityVerificationRequest\x1aB.google.ads.googleads.v20.services.GetIdentityVerificationResponse"L\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x028\x126/v20/customers/{customer_id=*}/getIdentityVerification\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x8c\x02\n%com.google.ads.googleads.v20.servicesB IdentityVerificationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.identity_verification_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB IdentityVerificationServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_STARTIDENTITYVERIFICATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_STARTIDENTITYVERIFICATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_STARTIDENTITYVERIFICATIONREQUEST'].fields_by_name['verification_program']._loaded_options = None
    _globals['_STARTIDENTITYVERIFICATIONREQUEST'].fields_by_name['verification_program']._serialized_options = b'\xe0A\x02'
    _globals['_GETIDENTITYVERIFICATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_GETIDENTITYVERIFICATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_IDENTITYVERIFICATIONSERVICE']._loaded_options = None
    _globals['_IDENTITYVERIFICATIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_IDENTITYVERIFICATIONSERVICE'].methods_by_name['StartIdentityVerification']._loaded_options = None
    _globals['_IDENTITYVERIFICATIONSERVICE'].methods_by_name['StartIdentityVerification']._serialized_options = b'\xdaA customer_id,verification_program\x82\xd3\xe4\x93\x02="8/v20/customers/{customer_id=*}:startIdentityVerification:\x01*'
    _globals['_IDENTITYVERIFICATIONSERVICE'].methods_by_name['GetIdentityVerification']._loaded_options = None
    _globals['_IDENTITYVERIFICATIONSERVICE'].methods_by_name['GetIdentityVerification']._serialized_options = b'\xdaA\x0bcustomer_id\x82\xd3\xe4\x93\x028\x126/v20/customers/{customer_id=*}/getIdentityVerification'
    _globals['_STARTIDENTITYVERIFICATIONREQUEST']._serialized_start = 369
    _globals['_STARTIDENTITYVERIFICATIONREQUEST']._serialized_end = 557
    _globals['_GETIDENTITYVERIFICATIONREQUEST']._serialized_start = 559
    _globals['_GETIDENTITYVERIFICATIONREQUEST']._serialized_end = 617
    _globals['_GETIDENTITYVERIFICATIONRESPONSE']._serialized_start = 619
    _globals['_GETIDENTITYVERIFICATIONRESPONSE']._serialized_end = 740
    _globals['_IDENTITYVERIFICATION']._serialized_start = 743
    _globals['_IDENTITYVERIFICATION']._serialized_end = 1169
    _globals['_IDENTITYVERIFICATIONPROGRESS']._serialized_start = 1172
    _globals['_IDENTITYVERIFICATIONPROGRESS']._serialized_end = 1392
    _globals['_IDENTITYVERIFICATIONREQUIREMENT']._serialized_start = 1394
    _globals['_IDENTITYVERIFICATIONREQUIREMENT']._serialized_end = 1516
    _globals['_IDENTITYVERIFICATIONSERVICE']._serialized_start = 1519
    _globals['_IDENTITYVERIFICATIONSERVICE']._serialized_end = 2087