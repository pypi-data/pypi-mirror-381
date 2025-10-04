"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/billing_setup_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.resources import billing_setup_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_billing__setup__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n=google/ads/googleads/v21/services/billing_setup_service.proto\x12!google.ads.googleads.v21.services\x1a6google/ads/googleads/v21/resources/billing_setup.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x87\x01\n\x19MutateBillingSetupRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12P\n\toperation\x18\x02 \x01(\x0b28.google.ads.googleads.v21.services.BillingSetupOperationB\x03\xe0A\x02"\xa6\x01\n\x15BillingSetupOperation\x12B\n\x06create\x18\x02 \x01(\x0b20.google.ads.googleads.v21.resources.BillingSetupH\x00\x12<\n\x06remove\x18\x01 \x01(\tB*\xfaA\'\n%googleads.googleapis.com/BillingSetupH\x00B\x0b\n\toperation"i\n\x1aMutateBillingSetupResponse\x12K\n\x06result\x18\x01 \x01(\x0b2;.google.ads.googleads.v21.services.MutateBillingSetupResult"]\n\x18MutateBillingSetupResult\x12A\n\rresource_name\x18\x01 \x01(\tB*\xfaA\'\n%googleads.googleapis.com/BillingSetup2\xc8\x02\n\x13BillingSetupService\x12\xe9\x01\n\x12MutateBillingSetup\x12<.google.ads.googleads.v21.services.MutateBillingSetupRequest\x1a=.google.ads.googleads.v21.services.MutateBillingSetupResponse"V\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x028"3/v21/customers/{customer_id=*}/billingSetups:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x84\x02\n%com.google.ads.googleads.v21.servicesB\x18BillingSetupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.billing_setup_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x18BillingSetupServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEBILLINGSETUPREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEBILLINGSETUPREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEBILLINGSETUPREQUEST'].fields_by_name['operation']._loaded_options = None
    _globals['_MUTATEBILLINGSETUPREQUEST'].fields_by_name['operation']._serialized_options = b'\xe0A\x02'
    _globals['_BILLINGSETUPOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_BILLINGSETUPOPERATION'].fields_by_name['remove']._serialized_options = b"\xfaA'\n%googleads.googleapis.com/BillingSetup"
    _globals['_MUTATEBILLINGSETUPRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEBILLINGSETUPRESULT'].fields_by_name['resource_name']._serialized_options = b"\xfaA'\n%googleads.googleapis.com/BillingSetup"
    _globals['_BILLINGSETUPSERVICE']._loaded_options = None
    _globals['_BILLINGSETUPSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_BILLINGSETUPSERVICE'].methods_by_name['MutateBillingSetup']._loaded_options = None
    _globals['_BILLINGSETUPSERVICE'].methods_by_name['MutateBillingSetup']._serialized_options = b'\xdaA\x15customer_id,operation\x82\xd3\xe4\x93\x028"3/v21/customers/{customer_id=*}/billingSetups:mutate:\x01*'
    _globals['_MUTATEBILLINGSETUPREQUEST']._serialized_start = 272
    _globals['_MUTATEBILLINGSETUPREQUEST']._serialized_end = 407
    _globals['_BILLINGSETUPOPERATION']._serialized_start = 410
    _globals['_BILLINGSETUPOPERATION']._serialized_end = 576
    _globals['_MUTATEBILLINGSETUPRESPONSE']._serialized_start = 578
    _globals['_MUTATEBILLINGSETUPRESPONSE']._serialized_end = 683
    _globals['_MUTATEBILLINGSETUPRESULT']._serialized_start = 685
    _globals['_MUTATEBILLINGSETUPRESULT']._serialized_end = 778
    _globals['_BILLINGSETUPSERVICE']._serialized_start = 781
    _globals['_BILLINGSETUPSERVICE']._serialized_end = 1109