"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/invoice_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import month_of_year_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_month__of__year__pb2
from ......google.ads.googleads.v19.resources import invoice_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_resources_dot_invoice__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/services/invoice_service.proto\x12!google.ads.googleads.v19.services\x1a2google/ads/googleads/v19/enums/month_of_year.proto\x1a0google/ads/googleads/v19/resources/invoice.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto"\xbb\x01\n\x13ListInvoicesRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x1a\n\rbilling_setup\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\nissue_year\x18\x03 \x01(\tB\x03\xe0A\x02\x12U\n\x0bissue_month\x18\x04 \x01(\x0e2;.google.ads.googleads.v19.enums.MonthOfYearEnum.MonthOfYearB\x03\xe0A\x02"U\n\x14ListInvoicesResponse\x12=\n\x08invoices\x18\x01 \x03(\x0b2+.google.ads.googleads.v19.resources.Invoice2\xbd\x02\n\x0eInvoiceService\x12\xe3\x01\n\x0cListInvoices\x126.google.ads.googleads.v19.services.ListInvoicesRequest\x1a7.google.ads.googleads.v19.services.ListInvoicesResponse"b\xdaA0customer_id,billing_setup,issue_year,issue_month\x82\xd3\xe4\x93\x02)\x12\'/v19/customers/{customer_id=*}/invoices\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\xff\x01\n%com.google.ads.googleads.v19.servicesB\x13InvoiceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.invoice_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x13InvoiceServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_LISTINVOICESREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_LISTINVOICESREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINVOICESREQUEST'].fields_by_name['billing_setup']._loaded_options = None
    _globals['_LISTINVOICESREQUEST'].fields_by_name['billing_setup']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINVOICESREQUEST'].fields_by_name['issue_year']._loaded_options = None
    _globals['_LISTINVOICESREQUEST'].fields_by_name['issue_year']._serialized_options = b'\xe0A\x02'
    _globals['_LISTINVOICESREQUEST'].fields_by_name['issue_month']._loaded_options = None
    _globals['_LISTINVOICESREQUEST'].fields_by_name['issue_month']._serialized_options = b'\xe0A\x02'
    _globals['_INVOICESERVICE']._loaded_options = None
    _globals['_INVOICESERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_INVOICESERVICE'].methods_by_name['ListInvoices']._loaded_options = None
    _globals['_INVOICESERVICE'].methods_by_name['ListInvoices']._serialized_options = b"\xdaA0customer_id,billing_setup,issue_year,issue_month\x82\xd3\xe4\x93\x02)\x12'/v19/customers/{customer_id=*}/invoices"
    _globals['_LISTINVOICESREQUEST']._serialized_start = 285
    _globals['_LISTINVOICESREQUEST']._serialized_end = 472
    _globals['_LISTINVOICESRESPONSE']._serialized_start = 474
    _globals['_LISTINVOICESRESPONSE']._serialized_end = 559
    _globals['_INVOICESERVICE']._serialized_start = 562
    _globals['_INVOICESERVICE']._serialized_end = 879