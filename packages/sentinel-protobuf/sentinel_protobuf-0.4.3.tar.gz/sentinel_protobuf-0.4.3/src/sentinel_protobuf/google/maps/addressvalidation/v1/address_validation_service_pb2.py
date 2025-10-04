"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/maps/addressvalidation/v1/address_validation_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.maps.addressvalidation.v1 import address_pb2 as google_dot_maps_dot_addressvalidation_dot_v1_dot_address__pb2
from .....google.maps.addressvalidation.v1 import geocode_pb2 as google_dot_maps_dot_addressvalidation_dot_v1_dot_geocode__pb2
from .....google.maps.addressvalidation.v1 import metadata_pb2 as google_dot_maps_dot_addressvalidation_dot_v1_dot_metadata__pb2
from .....google.maps.addressvalidation.v1 import usps_data_pb2 as google_dot_maps_dot_addressvalidation_dot_v1_dot_usps__data__pb2
from .....google.type import postal_address_pb2 as google_dot_type_dot_postal__address__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nAgoogle/maps/addressvalidation/v1/address_validation_service.proto\x12 google.maps.addressvalidation.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a.google/maps/addressvalidation/v1/address.proto\x1a.google/maps/addressvalidation/v1/geocode.proto\x1a/google/maps/addressvalidation/v1/metadata.proto\x1a0google/maps/addressvalidation/v1/usps_data.proto\x1a google/type/postal_address.proto"\x9e\x01\n\x16ValidateAddressRequest\x120\n\x07address\x18\x01 \x01(\x0b2\x1a.google.type.PostalAddressB\x03\xe0A\x02\x12\x1c\n\x14previous_response_id\x18\x02 \x01(\t\x12\x18\n\x10enable_usps_cass\x18\x03 \x01(\x08\x12\x1a\n\rsession_token\x18\x05 \x01(\tB\x03\xe0A\x01"r\n\x17ValidateAddressResponse\x12B\n\x06result\x18\x01 \x01(\x0b22.google.maps.addressvalidation.v1.ValidationResult\x12\x13\n\x0bresponse_id\x18\x02 \x01(\t"\xcb\x02\n ProvideValidationFeedbackRequest\x12p\n\nconclusion\x18\x01 \x01(\x0e2W.google.maps.addressvalidation.v1.ProvideValidationFeedbackRequest.ValidationConclusionB\x03\xe0A\x02\x12\x18\n\x0bresponse_id\x18\x02 \x01(\tB\x03\xe0A\x02"\x9a\x01\n\x14ValidationConclusion\x12%\n!VALIDATION_CONCLUSION_UNSPECIFIED\x10\x00\x12\x1a\n\x16VALIDATED_VERSION_USED\x10\x01\x12\x15\n\x11USER_VERSION_USED\x10\x02\x12\x1c\n\x18UNVALIDATED_VERSION_USED\x10\x03\x12\n\n\x06UNUSED\x10\x04"#\n!ProvideValidationFeedbackResponse"\xca\x02\n\x10ValidationResult\x12:\n\x07verdict\x18\x01 \x01(\x0b2).google.maps.addressvalidation.v1.Verdict\x12:\n\x07address\x18\x02 \x01(\x0b2).google.maps.addressvalidation.v1.Address\x12:\n\x07geocode\x18\x03 \x01(\x0b2).google.maps.addressvalidation.v1.Geocode\x12C\n\x08metadata\x18\x04 \x01(\x0b21.google.maps.addressvalidation.v1.AddressMetadata\x12=\n\tusps_data\x18\x05 \x01(\x0b2*.google.maps.addressvalidation.v1.UspsData"\xb1\x04\n\x07Verdict\x12P\n\x11input_granularity\x18\x01 \x01(\x0e25.google.maps.addressvalidation.v1.Verdict.Granularity\x12U\n\x16validation_granularity\x18\x02 \x01(\x0e25.google.maps.addressvalidation.v1.Verdict.Granularity\x12R\n\x13geocode_granularity\x18\x03 \x01(\x0e25.google.maps.addressvalidation.v1.Verdict.Granularity\x12\x18\n\x10address_complete\x18\x04 \x01(\x08\x12"\n\x1ahas_unconfirmed_components\x18\x05 \x01(\x08\x12\x1f\n\x17has_inferred_components\x18\x06 \x01(\x08\x12\x1f\n\x17has_replaced_components\x18\x07 \x01(\x08\x12&\n\x1ehas_spell_corrected_components\x18\t \x01(\x08"\x80\x01\n\x0bGranularity\x12\x1b\n\x17GRANULARITY_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSUB_PREMISE\x10\x01\x12\x0b\n\x07PREMISE\x10\x02\x12\x15\n\x11PREMISE_PROXIMITY\x10\x03\x12\t\n\x05BLOCK\x10\x04\x12\t\n\x05ROUTE\x10\x05\x12\t\n\x05OTHER\x10\x062\xb2\x03\n\x11AddressValidation\x12\xa6\x01\n\x0fValidateAddress\x128.google.maps.addressvalidation.v1.ValidateAddressRequest\x1a9.google.maps.addressvalidation.v1.ValidateAddressResponse"\x1e\x82\xd3\xe4\x93\x02\x18"\x13/v1:validateAddress:\x01*\x12\xce\x01\n\x19ProvideValidationFeedback\x12B.google.maps.addressvalidation.v1.ProvideValidationFeedbackRequest\x1aC.google.maps.addressvalidation.v1.ProvideValidationFeedbackResponse"(\x82\xd3\xe4\x93\x02""\x1d/v1:provideValidationFeedback:\x01*\x1a#\xcaA addressvalidation.googleapis.comB\x97\x02\n$com.google.maps.addressvalidation.v1B\x1dAddressValidationServiceProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.maps.addressvalidation.v1.address_validation_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.maps.addressvalidation.v1B\x1dAddressValidationServiceProtoP\x01ZXcloud.google.com/go/maps/addressvalidation/apiv1/addressvalidationpb;addressvalidationpb\xa2\x02\x07GMPAVV1\xaa\x02 Google.Maps.AddressValidation.V1\xca\x02 Google\\Maps\\AddressValidation\\V1\xea\x02#Google::Maps::AddressValidation::V1'
    _globals['_VALIDATEADDRESSREQUEST'].fields_by_name['address']._loaded_options = None
    _globals['_VALIDATEADDRESSREQUEST'].fields_by_name['address']._serialized_options = b'\xe0A\x02'
    _globals['_VALIDATEADDRESSREQUEST'].fields_by_name['session_token']._loaded_options = None
    _globals['_VALIDATEADDRESSREQUEST'].fields_by_name['session_token']._serialized_options = b'\xe0A\x01'
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST'].fields_by_name['conclusion']._loaded_options = None
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST'].fields_by_name['conclusion']._serialized_options = b'\xe0A\x02'
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST'].fields_by_name['response_id']._loaded_options = None
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST'].fields_by_name['response_id']._serialized_options = b'\xe0A\x02'
    _globals['_ADDRESSVALIDATION']._loaded_options = None
    _globals['_ADDRESSVALIDATION']._serialized_options = b'\xcaA addressvalidation.googleapis.com'
    _globals['_ADDRESSVALIDATION'].methods_by_name['ValidateAddress']._loaded_options = None
    _globals['_ADDRESSVALIDATION'].methods_by_name['ValidateAddress']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18"\x13/v1:validateAddress:\x01*'
    _globals['_ADDRESSVALIDATION'].methods_by_name['ProvideValidationFeedback']._loaded_options = None
    _globals['_ADDRESSVALIDATION'].methods_by_name['ProvideValidationFeedback']._serialized_options = b'\x82\xd3\xe4\x93\x02""\x1d/v1:provideValidationFeedback:\x01*'
    _globals['_VALIDATEADDRESSREQUEST']._serialized_start = 421
    _globals['_VALIDATEADDRESSREQUEST']._serialized_end = 579
    _globals['_VALIDATEADDRESSRESPONSE']._serialized_start = 581
    _globals['_VALIDATEADDRESSRESPONSE']._serialized_end = 695
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST']._serialized_start = 698
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST']._serialized_end = 1029
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST_VALIDATIONCONCLUSION']._serialized_start = 875
    _globals['_PROVIDEVALIDATIONFEEDBACKREQUEST_VALIDATIONCONCLUSION']._serialized_end = 1029
    _globals['_PROVIDEVALIDATIONFEEDBACKRESPONSE']._serialized_start = 1031
    _globals['_PROVIDEVALIDATIONFEEDBACKRESPONSE']._serialized_end = 1066
    _globals['_VALIDATIONRESULT']._serialized_start = 1069
    _globals['_VALIDATIONRESULT']._serialized_end = 1399
    _globals['_VERDICT']._serialized_start = 1402
    _globals['_VERDICT']._serialized_end = 1963
    _globals['_VERDICT_GRANULARITY']._serialized_start = 1835
    _globals['_VERDICT_GRANULARITY']._serialized_end = 1963
    _globals['_ADDRESSVALIDATION']._serialized_start = 1966
    _globals['_ADDRESSVALIDATION']._serialized_end = 2400