"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/local_services_verification_artifact.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.common import local_services_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_common_dot_local__services__pb2
from ......google.ads.googleads.v21.enums import local_services_business_registration_check_rejection_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__business__registration__check__rejection__reason__pb2
from ......google.ads.googleads.v21.enums import local_services_business_registration_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__business__registration__type__pb2
from ......google.ads.googleads.v21.enums import local_services_insurance_rejection_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__insurance__rejection__reason__pb2
from ......google.ads.googleads.v21.enums import local_services_license_rejection_reason_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__license__rejection__reason__pb2
from ......google.ads.googleads.v21.enums import local_services_verification_artifact_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__verification__artifact__status__pb2
from ......google.ads.googleads.v21.enums import local_services_verification_artifact_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__verification__artifact__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nMgoogle/ads/googleads/v21/resources/local_services_verification_artifact.proto\x12"google.ads.googleads.v21.resources\x1a4google/ads/googleads/v21/common/local_services.proto\x1a`google/ads/googleads/v21/enums/local_services_business_registration_check_rejection_reason.proto\x1aNgoogle/ads/googleads/v21/enums/local_services_business_registration_type.proto\x1aNgoogle/ads/googleads/v21/enums/local_services_insurance_rejection_reason.proto\x1aLgoogle/ads/googleads/v21/enums/local_services_license_rejection_reason.proto\x1aPgoogle/ads/googleads/v21/enums/local_services_verification_artifact_status.proto\x1aNgoogle/ads/googleads/v21/enums/local_services_verification_artifact_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfc\x08\n!LocalServicesVerificationArtifact\x12Y\n\rresource_name\x18\x01 \x01(\tBB\xe0A\x05\xfaA<\n:googleads.googleapis.com/LocalServicesVerificationArtifact\x12\x14\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1f\n\x12creation_date_time\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x88\x01\n\x06status\x18\x04 \x01(\x0e2s.google.ads.googleads.v21.enums.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatusB\x03\xe0A\x03\x12\x8b\x01\n\rartifact_type\x18\x05 \x01(\x0e2o.google.ads.googleads.v21.enums.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactTypeB\x03\xe0A\x03\x12~\n&background_check_verification_artifact\x18\x06 \x01(\x0b2G.google.ads.googleads.v21.resources.BackgroundCheckVerificationArtifactB\x03\xe0A\x03H\x00\x12q\n\x1finsurance_verification_artifact\x18\x07 \x01(\x0b2A.google.ads.googleads.v21.resources.InsuranceVerificationArtifactB\x03\xe0A\x03H\x00\x12m\n\x1dlicense_verification_artifact\x18\x08 \x01(\x0b2?.google.ads.googleads.v21.resources.LicenseVerificationArtifactB\x03\xe0A\x03H\x00\x12\x93\x01\n1business_registration_check_verification_artifact\x18\t \x01(\x0b2Q.google.ads.googleads.v21.resources.BusinessRegistrationCheckVerificationArtifactB\x03\xe0A\x03H\x00:\x9b\x01\xeaA\x97\x01\n:googleads.googleapis.com/LocalServicesVerificationArtifact\x12Ycustomers/{customer_id}/localServicesVerificationArtifacts/{gls_verification_artifact_id}B\x0f\n\rartifact_dataB\x05\n\x03_id"\x9f\x01\n#BackgroundCheckVerificationArtifact\x12\x1a\n\x08case_url\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12.\n\x1cfinal_adjudication_date_time\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01B\x0b\n\t_case_urlB\x1f\n\x1d_final_adjudication_date_time"\xcd\x03\n\x1dInsuranceVerificationArtifact\x12\x1f\n\ramount_micros\x18\x01 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x93\x01\n\x10rejection_reason\x18\x02 \x01(\x0e2o.google.ads.googleads.v21.enums.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReasonB\x03\xe0A\x03H\x01\x88\x01\x01\x12m\n\x1binsurance_document_readonly\x18\x03 \x01(\x0b2>.google.ads.googleads.v21.common.LocalServicesDocumentReadOnlyB\x03\xe0A\x03H\x02\x88\x01\x01\x12&\n\x14expiration_date_time\x18\x04 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01B\x10\n\x0e_amount_microsB\x13\n\x11_rejection_reasonB\x1e\n\x1c_insurance_document_readonlyB\x17\n\x15_expiration_date_time"\xf2\x04\n\x1bLicenseVerificationArtifact\x12\x1e\n\x0clicense_type\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12 \n\x0elicense_number\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12%\n\x13licensee_first_name\x18\x03 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12$\n\x12licensee_last_name\x18\x04 \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x8f\x01\n\x10rejection_reason\x18\x05 \x01(\x0e2k.google.ads.googleads.v21.enums.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReasonB\x03\xe0A\x03H\x04\x88\x01\x01\x12k\n\x19license_document_readonly\x18\x06 \x01(\x0b2>.google.ads.googleads.v21.common.LocalServicesDocumentReadOnlyB\x03\xe0A\x03H\x05\x88\x01\x01\x12&\n\x14expiration_date_time\x18\x07 \x01(\tB\x03\xe0A\x03H\x06\x88\x01\x01B\x0f\n\r_license_typeB\x11\n\x0f_license_numberB\x16\n\x14_licensee_first_nameB\x15\n\x13_licensee_last_nameB\x13\n\x11_rejection_reasonB\x1c\n\x1a_license_document_readonlyB\x17\n\x15_expiration_date_time"\xb6\x05\n-BusinessRegistrationCheckVerificationArtifact\x12\x94\x01\n\x11registration_type\x18\x03 \x01(\x0e2o.google.ads.googleads.v21.enums.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationTypeB\x03\xe0A\x03H\x01\x88\x01\x01\x12\x1a\n\x08check_id\x18\x04 \x01(\tB\x03\xe0A\x03H\x02\x88\x01\x01\x12\xb4\x01\n\x10rejection_reason\x18\x05 \x01(\x0e2\x8f\x01.google.ads.googleads.v21.enums.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReasonB\x03\xe0A\x03H\x03\x88\x01\x01\x12b\n\x13registration_number\x18\x01 \x01(\x0b2>.google.ads.googleads.v21.resources.BusinessRegistrationNumberB\x03\xe0A\x03H\x00\x12f\n\x15registration_document\x18\x02 \x01(\x0b2@.google.ads.googleads.v21.resources.BusinessRegistrationDocumentB\x03\xe0A\x03H\x00B\x17\n\x15business_registrationB\x14\n\x12_registration_typeB\x0b\n\t_check_idB\x13\n\x11_rejection_reason"A\n\x1aBusinessRegistrationNumber\x12\x18\n\x06number\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01B\t\n\x07_number"\x99\x01\n\x1cBusinessRegistrationDocument\x12c\n\x11document_readonly\x18\x01 \x01(\x0b2>.google.ads.googleads.v21.common.LocalServicesDocumentReadOnlyB\x03\xe0A\x03H\x00\x88\x01\x01B\x14\n\x12_document_readonlyB\x98\x02\n&com.google.ads.googleads.v21.resourcesB&LocalServicesVerificationArtifactProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.local_services_verification_artifact_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB&LocalServicesVerificationArtifactProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA<\n:googleads.googleapis.com/LocalServicesVerificationArtifact'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['id']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['status']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['artifact_type']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['artifact_type']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['background_check_verification_artifact']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['background_check_verification_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['insurance_verification_artifact']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['insurance_verification_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['license_verification_artifact']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['license_verification_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['business_registration_check_verification_artifact']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT'].fields_by_name['business_registration_check_verification_artifact']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT']._loaded_options = None
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT']._serialized_options = b'\xeaA\x97\x01\n:googleads.googleapis.com/LocalServicesVerificationArtifact\x12Ycustomers/{customer_id}/localServicesVerificationArtifacts/{gls_verification_artifact_id}'
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT'].fields_by_name['case_url']._loaded_options = None
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT'].fields_by_name['case_url']._serialized_options = b'\xe0A\x03'
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT'].fields_by_name['final_adjudication_date_time']._loaded_options = None
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT'].fields_by_name['final_adjudication_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['amount_micros']._loaded_options = None
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['amount_micros']._serialized_options = b'\xe0A\x03'
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._loaded_options = None
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._serialized_options = b'\xe0A\x03'
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['insurance_document_readonly']._loaded_options = None
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['insurance_document_readonly']._serialized_options = b'\xe0A\x03'
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['expiration_date_time']._loaded_options = None
    _globals['_INSURANCEVERIFICATIONARTIFACT'].fields_by_name['expiration_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_type']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_type']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_number']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_number']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['licensee_first_name']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['licensee_first_name']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['licensee_last_name']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['licensee_last_name']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_document_readonly']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['license_document_readonly']._serialized_options = b'\xe0A\x03'
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['expiration_date_time']._loaded_options = None
    _globals['_LICENSEVERIFICATIONARTIFACT'].fields_by_name['expiration_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_type']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_type']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['check_id']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['check_id']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['rejection_reason']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_number']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_number']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_document']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT'].fields_by_name['registration_document']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONNUMBER'].fields_by_name['number']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONNUMBER'].fields_by_name['number']._serialized_options = b'\xe0A\x03'
    _globals['_BUSINESSREGISTRATIONDOCUMENT'].fields_by_name['document_readonly']._loaded_options = None
    _globals['_BUSINESSREGISTRATIONDOCUMENT'].fields_by_name['document_readonly']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT']._serialized_start = 730
    _globals['_LOCALSERVICESVERIFICATIONARTIFACT']._serialized_end = 1878
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT']._serialized_start = 1881
    _globals['_BACKGROUNDCHECKVERIFICATIONARTIFACT']._serialized_end = 2040
    _globals['_INSURANCEVERIFICATIONARTIFACT']._serialized_start = 2043
    _globals['_INSURANCEVERIFICATIONARTIFACT']._serialized_end = 2504
    _globals['_LICENSEVERIFICATIONARTIFACT']._serialized_start = 2507
    _globals['_LICENSEVERIFICATIONARTIFACT']._serialized_end = 3133
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT']._serialized_start = 3136
    _globals['_BUSINESSREGISTRATIONCHECKVERIFICATIONARTIFACT']._serialized_end = 3830
    _globals['_BUSINESSREGISTRATIONNUMBER']._serialized_start = 3832
    _globals['_BUSINESSREGISTRATIONNUMBER']._serialized_end = 3897
    _globals['_BUSINESSREGISTRATIONDOCUMENT']._serialized_start = 3900
    _globals['_BUSINESSREGISTRATIONDOCUMENT']._serialized_end = 4053