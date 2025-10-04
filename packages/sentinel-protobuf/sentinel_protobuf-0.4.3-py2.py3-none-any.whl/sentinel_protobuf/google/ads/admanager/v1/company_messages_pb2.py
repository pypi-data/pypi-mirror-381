"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/admanager/v1/company_messages.proto')
_sym_db = _symbol_database.Default()
from .....google.ads.admanager.v1 import applied_label_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_applied__label__pb2
from .....google.ads.admanager.v1 import company_enums_pb2 as google_dot_ads_dot_admanager_dot_v1_dot_company__enums__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/ads/admanager/v1/company_messages.proto\x12\x17google.ads.admanager.v1\x1a+google/ads/admanager/v1/applied_label.proto\x1a+google/ads/admanager/v1/company_enums.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x9c\x06\n\x07Company\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x17\n\ncompany_id\x18\x02 \x01(\x03B\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x02\x12G\n\x04type\x18\x04 \x01(\x0e24.google.ads.admanager.v1.CompanyTypeEnum.CompanyTypeB\x03\xe0A\x02\x12\x14\n\x07address\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05email\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x10\n\x03fax\x18\x07 \x01(\tB\x03\xe0A\x01\x12\x12\n\x05phone\x18\x08 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bexternal_id\x18\t \x01(\tB\x03\xe0A\x01\x12\x14\n\x07comment\x18\n \x01(\tB\x03\xe0A\x01\x12`\n\rcredit_status\x18\x0b \x01(\x0e2D.google.ads.admanager.v1.CompanyCreditStatusEnum.CompanyCreditStatusB\x03\xe0A\x01\x12B\n\x0eapplied_labels\x18\x0c \x03(\x0b2%.google.ads.admanager.v1.AppliedLabelB\x03\xe0A\x01\x12F\n\x0fprimary_contact\x18\r \x01(\tB(\xe0A\x01\xfaA"\n admanager.googleapis.com/ContactH\x00\x88\x01\x01\x12<\n\rapplied_teams\x18\x0e \x03(\tB%\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team\x12#\n\x16third_party_company_id\x18\x10 \x01(\x03B\x03\xe0A\x01\x124\n\x0bupdate_time\x18\x0f \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03:f\xeaAc\n admanager.googleapis.com/Company\x12+networks/{network_code}/companies/{company}*\tcompanies2\x07companyB\x12\n\x10_primary_contactB\xc8\x01\n\x1bcom.google.ads.admanager.v1B\x14CompanyMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.admanager.v1.company_messages_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1bcom.google.ads.admanager.v1B\x14CompanyMessagesProtoP\x01Z@google.golang.org/genproto/googleapis/ads/admanager/v1;admanager\xaa\x02\x17Google.Ads.AdManager.V1\xca\x02\x17Google\\Ads\\AdManager\\V1\xea\x02\x1aGoogle::Ads::AdManager::V1'
    _globals['_COMPANY'].fields_by_name['name']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_COMPANY'].fields_by_name['company_id']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['company_id']._serialized_options = b'\xe0A\x03'
    _globals['_COMPANY'].fields_by_name['display_name']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_COMPANY'].fields_by_name['type']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_COMPANY'].fields_by_name['address']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['address']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['email']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['email']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['fax']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['fax']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['phone']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['phone']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['external_id']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['external_id']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['comment']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['comment']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['credit_status']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['credit_status']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['applied_labels']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['applied_labels']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['primary_contact']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['primary_contact']._serialized_options = b'\xe0A\x01\xfaA"\n admanager.googleapis.com/Contact'
    _globals['_COMPANY'].fields_by_name['applied_teams']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['applied_teams']._serialized_options = b'\xe0A\x01\xfaA\x1f\n\x1dadmanager.googleapis.com/Team'
    _globals['_COMPANY'].fields_by_name['third_party_company_id']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['third_party_company_id']._serialized_options = b'\xe0A\x01'
    _globals['_COMPANY'].fields_by_name['update_time']._loaded_options = None
    _globals['_COMPANY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_COMPANY']._loaded_options = None
    _globals['_COMPANY']._serialized_options = b'\xeaAc\n admanager.googleapis.com/Company\x12+networks/{network_code}/companies/{company}*\tcompanies2\x07company'
    _globals['_COMPANY']._serialized_start = 259
    _globals['_COMPANY']._serialized_end = 1055