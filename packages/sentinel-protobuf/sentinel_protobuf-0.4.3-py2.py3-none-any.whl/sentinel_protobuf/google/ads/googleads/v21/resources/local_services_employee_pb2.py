"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/local_services_employee.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import local_services_employee_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__employee__status__pb2
from ......google.ads.googleads.v21.enums import local_services_employee_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__employee__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v21/resources/local_services_employee.proto\x12"google.ads.googleads.v21.resources\x1aCgoogle/ads/googleads/v21/enums/local_services_employee_status.proto\x1aAgoogle/ads/googleads/v21/enums/local_services_employee_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x98\t\n\x15LocalServicesEmployee\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/LocalServicesEmployee\x12\x14\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03H\x00\x88\x01\x01\x12\x1f\n\x12creation_date_time\x18\x03 \x01(\tB\x03\xe0A\x03\x12p\n\x06status\x18\x04 \x01(\x0e2[.google.ads.googleads.v21.enums.LocalServicesEmployeeStatusEnum.LocalServicesEmployeeStatusB\x03\xe0A\x03\x12j\n\x04type\x18\x05 \x01(\x0e2W.google.ads.googleads.v21.enums.LocalServicesEmployeeTypeEnum.LocalServicesEmployeeTypeB\x03\xe0A\x03\x12U\n\x12university_degrees\x18\x06 \x03(\x0b24.google.ads.googleads.v21.resources.UniversityDegreeB\x03\xe0A\x03\x12G\n\x0bresidencies\x18\x07 \x03(\x0b2-.google.ads.googleads.v21.resources.ResidencyB\x03\xe0A\x03\x12H\n\x0bfellowships\x18\x08 \x03(\x0b2..google.ads.googleads.v21.resources.FellowshipB\x03\xe0A\x03\x12\x1b\n\tjob_title\x18\t \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12)\n\x17year_started_practicing\x18\n \x01(\x05B\x03\xe0A\x03H\x02\x88\x01\x01\x12\x1d\n\x10languages_spoken\x18\x0b \x03(\tB\x03\xe0A\x03\x12\x19\n\x0ccategory_ids\x18\x0c \x03(\tB\x03\xe0A\x03\x12-\n\x1bnational_provider_id_number\x18\r \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12\x1f\n\remail_address\x18\x0e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12\x1c\n\nfirst_name\x18\x0f \x01(\tB\x03\xe0A\x03H\x05\x88\x01\x01\x12\x1d\n\x0bmiddle_name\x18\x10 \x01(\tB\x03\xe0A\x03H\x06\x88\x01\x01\x12\x1b\n\tlast_name\x18\x11 \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01:u\xeaAr\n.googleads.googleapis.com/LocalServicesEmployee\x12@customers/{customer_id}/localServicesEmployees/{gls_employee_id}B\x05\n\x03_idB\x0c\n\n_job_titleB\x1a\n\x18_year_started_practicingB\x1e\n\x1c_national_provider_id_numberB\x10\n\x0e_email_addressB\r\n\x0b_first_nameB\x0e\n\x0c_middle_nameB\x0c\n\n_last_name"\xa7\x01\n\x10UniversityDegree\x12"\n\x10institution_name\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x18\n\x06degree\x18\x02 \x01(\tB\x03\xe0A\x03H\x01\x88\x01\x01\x12!\n\x0fgraduation_year\x18\x03 \x01(\x05B\x03\xe0A\x03H\x02\x88\x01\x01B\x13\n\x11_institution_nameB\t\n\x07_degreeB\x12\n\x10_graduation_year"{\n\tResidency\x12"\n\x10institution_name\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12!\n\x0fcompletion_year\x18\x02 \x01(\x05B\x03\xe0A\x03H\x01\x88\x01\x01B\x13\n\x11_institution_nameB\x12\n\x10_completion_year"|\n\nFellowship\x12"\n\x10institution_name\x18\x01 \x01(\tB\x03\xe0A\x03H\x00\x88\x01\x01\x12!\n\x0fcompletion_year\x18\x02 \x01(\x05B\x03\xe0A\x03H\x01\x88\x01\x01B\x13\n\x11_institution_nameB\x12\n\x10_completion_yearB\x8c\x02\n&com.google.ads.googleads.v21.resourcesB\x1aLocalServicesEmployeeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.local_services_employee_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x1aLocalServicesEmployeeProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/LocalServicesEmployee'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['id']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['status']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['type']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['university_degrees']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['university_degrees']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['residencies']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['residencies']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['fellowships']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['fellowships']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['job_title']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['job_title']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['year_started_practicing']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['year_started_practicing']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['languages_spoken']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['languages_spoken']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['category_ids']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['category_ids']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['national_provider_id_number']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['national_provider_id_number']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['email_address']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['email_address']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['first_name']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['first_name']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['middle_name']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['middle_name']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['last_name']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE'].fields_by_name['last_name']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE']._loaded_options = None
    _globals['_LOCALSERVICESEMPLOYEE']._serialized_options = b'\xeaAr\n.googleads.googleapis.com/LocalServicesEmployee\x12@customers/{customer_id}/localServicesEmployees/{gls_employee_id}'
    _globals['_UNIVERSITYDEGREE'].fields_by_name['institution_name']._loaded_options = None
    _globals['_UNIVERSITYDEGREE'].fields_by_name['institution_name']._serialized_options = b'\xe0A\x03'
    _globals['_UNIVERSITYDEGREE'].fields_by_name['degree']._loaded_options = None
    _globals['_UNIVERSITYDEGREE'].fields_by_name['degree']._serialized_options = b'\xe0A\x03'
    _globals['_UNIVERSITYDEGREE'].fields_by_name['graduation_year']._loaded_options = None
    _globals['_UNIVERSITYDEGREE'].fields_by_name['graduation_year']._serialized_options = b'\xe0A\x03'
    _globals['_RESIDENCY'].fields_by_name['institution_name']._loaded_options = None
    _globals['_RESIDENCY'].fields_by_name['institution_name']._serialized_options = b'\xe0A\x03'
    _globals['_RESIDENCY'].fields_by_name['completion_year']._loaded_options = None
    _globals['_RESIDENCY'].fields_by_name['completion_year']._serialized_options = b'\xe0A\x03'
    _globals['_FELLOWSHIP'].fields_by_name['institution_name']._loaded_options = None
    _globals['_FELLOWSHIP'].fields_by_name['institution_name']._serialized_options = b'\xe0A\x03'
    _globals['_FELLOWSHIP'].fields_by_name['completion_year']._loaded_options = None
    _globals['_FELLOWSHIP'].fields_by_name['completion_year']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESEMPLOYEE']._serialized_start = 301
    _globals['_LOCALSERVICESEMPLOYEE']._serialized_end = 1477
    _globals['_UNIVERSITYDEGREE']._serialized_start = 1480
    _globals['_UNIVERSITYDEGREE']._serialized_end = 1647
    _globals['_RESIDENCY']._serialized_start = 1649
    _globals['_RESIDENCY']._serialized_end = 1772
    _globals['_FELLOWSHIP']._serialized_start = 1774
    _globals['_FELLOWSHIP']._serialized_end = 1898