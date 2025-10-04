"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/resources/local_services_lead.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.enums import local_services_lead_credit_state_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__lead__credit__state__pb2
from ......google.ads.googleads.v21.enums import local_services_lead_status_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__lead__status__pb2
from ......google.ads.googleads.v21.enums import local_services_lead_type_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_enums_dot_local__services__lead__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n<google/ads/googleads/v21/resources/local_services_lead.proto\x12"google.ads.googleads.v21.resources\x1aEgoogle/ads/googleads/v21/enums/local_services_lead_credit_state.proto\x1a?google/ads/googleads/v21/enums/local_services_lead_status.proto\x1a=google/ads/googleads/v21/enums/local_services_lead_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xd2\x06\n\x11LocalServicesLead\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x03\xfaA,\n*googleads.googleapis.com/LocalServicesLead\x12\x0f\n\x02id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x18\n\x0bcategory_id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x17\n\nservice_id\x18\x04 \x01(\tB\x03\xe0A\x03\x12P\n\x0fcontact_details\x18\x05 \x01(\x0b22.google.ads.googleads.v21.resources.ContactDetailsB\x03\xe0A\x03\x12Z\n\tlead_type\x18\x06 \x01(\x0e2B.google.ads.googleads.v21.enums.LocalServicesLeadTypeEnum.LeadTypeB\x03\xe0A\x03\x12`\n\x0blead_status\x18\x07 \x01(\x0e2F.google.ads.googleads.v21.enums.LocalServicesLeadStatusEnum.LeadStatusB\x03\xe0A\x03\x12\x1f\n\x12creation_date_time\x18\x08 \x01(\tB\x03\xe0A\x03\x12\x13\n\x06locale\x18\t \x01(\tB\x03\xe0A\x03\x12@\n\x04note\x18\n \x01(\x0b2(.google.ads.googleads.v21.resources.NoteB\x03\xe0A\x03H\x00\x88\x01\x01\x12\x19\n\x0clead_charged\x18\x0b \x01(\x08B\x03\xe0A\x03\x12S\n\x0ecredit_details\x18\x0c \x01(\x0b21.google.ads.googleads.v21.resources.CreditDetailsB\x03\xe0A\x03H\x01\x88\x01\x01\x12$\n\x17lead_feedback_submitted\x18\r \x01(\x08B\x03\xe0A\x03:t\xeaAq\n*googleads.googleapis.com/LocalServicesLead\x12Ccustomers/{customer_id}/localServicesLeads/{local_services_lead_id}B\x07\n\x05_noteB\x11\n\x0f_credit_details"[\n\x0eContactDetails\x12\x19\n\x0cphone_number\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x12\n\x05email\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x1a\n\rconsumer_name\x18\x03 \x01(\tB\x03\xe0A\x03"=\n\x04Note\x12\x1b\n\x0eedit_date_time\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03"\xa5\x01\n\rCreditDetails\x12c\n\x0ccredit_state\x18\x01 \x01(\x0e2H.google.ads.googleads.v21.enums.LocalServicesCreditStateEnum.CreditStateB\x03\xe0A\x03\x12/\n"credit_state_last_update_date_time\x18\x02 \x01(\tB\x03\xe0A\x03B\x88\x02\n&com.google.ads.googleads.v21.resourcesB\x16LocalServicesLeadProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.resources.local_services_lead_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v21.resourcesB\x16LocalServicesLeadProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v21/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V21.Resources\xca\x02"Google\\Ads\\GoogleAds\\V21\\Resources\xea\x02&Google::Ads::GoogleAds::V21::Resources'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA,\n*googleads.googleapis.com/LocalServicesLead'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['id']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['category_id']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['category_id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['service_id']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['service_id']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['contact_details']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['contact_details']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_type']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_type']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_status']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_status']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['locale']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['locale']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['note']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['note']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_charged']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_charged']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['credit_details']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['credit_details']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_feedback_submitted']._loaded_options = None
    _globals['_LOCALSERVICESLEAD'].fields_by_name['lead_feedback_submitted']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD']._loaded_options = None
    _globals['_LOCALSERVICESLEAD']._serialized_options = b'\xeaAq\n*googleads.googleapis.com/LocalServicesLead\x12Ccustomers/{customer_id}/localServicesLeads/{local_services_lead_id}'
    _globals['_CONTACTDETAILS'].fields_by_name['phone_number']._loaded_options = None
    _globals['_CONTACTDETAILS'].fields_by_name['phone_number']._serialized_options = b'\xe0A\x03'
    _globals['_CONTACTDETAILS'].fields_by_name['email']._loaded_options = None
    _globals['_CONTACTDETAILS'].fields_by_name['email']._serialized_options = b'\xe0A\x03'
    _globals['_CONTACTDETAILS'].fields_by_name['consumer_name']._loaded_options = None
    _globals['_CONTACTDETAILS'].fields_by_name['consumer_name']._serialized_options = b'\xe0A\x03'
    _globals['_NOTE'].fields_by_name['edit_date_time']._loaded_options = None
    _globals['_NOTE'].fields_by_name['edit_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_NOTE'].fields_by_name['description']._loaded_options = None
    _globals['_NOTE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_CREDITDETAILS'].fields_by_name['credit_state']._loaded_options = None
    _globals['_CREDITDETAILS'].fields_by_name['credit_state']._serialized_options = b'\xe0A\x03'
    _globals['_CREDITDETAILS'].fields_by_name['credit_state_last_update_date_time']._loaded_options = None
    _globals['_CREDITDETAILS'].fields_by_name['credit_state_last_update_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_LOCALSERVICESLEAD']._serialized_start = 360
    _globals['_LOCALSERVICESLEAD']._serialized_end = 1210
    _globals['_CONTACTDETAILS']._serialized_start = 1212
    _globals['_CONTACTDETAILS']._serialized_end = 1303
    _globals['_NOTE']._serialized_start = 1305
    _globals['_NOTE']._serialized_end = 1366
    _globals['_CREDITDETAILS']._serialized_start = 1369
    _globals['_CREDITDETAILS']._serialized_end = 1534