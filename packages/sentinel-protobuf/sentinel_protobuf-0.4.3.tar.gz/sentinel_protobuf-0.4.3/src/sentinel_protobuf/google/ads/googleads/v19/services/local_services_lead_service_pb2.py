"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/services/local_services_lead_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import local_services_lead_credit_issuance_decision_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_local__services__lead__credit__issuance__decision__pb2
from ......google.ads.googleads.v19.enums import local_services_lead_survey_answer_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_local__services__lead__survey__answer__pb2
from ......google.ads.googleads.v19.enums import local_services_lead_survey_dissatisfied_reason_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_local__services__lead__survey__dissatisfied__reason__pb2
from ......google.ads.googleads.v19.enums import local_services_lead_survey_satisfied_reason_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_local__services__lead__survey__satisfied__reason__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nCgoogle/ads/googleads/v19/services/local_services_lead_service.proto\x12!google.ads.googleads.v19.services\x1aQgoogle/ads/googleads/v19/enums/local_services_lead_credit_issuance_decision.proto\x1aFgoogle/ads/googleads/v19/enums/local_services_lead_survey_answer.proto\x1aSgoogle/ads/googleads/v19/enums/local_services_lead_survey_dissatisfied_reason.proto\x1aPgoogle/ads/googleads/v19/enums/local_services_lead_survey_satisfied_reason.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x17google/rpc/status.proto"\x86\x01\n\x1dAppendLeadConversationRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12K\n\rconversations\x18\x02 \x03(\x0b2/.google.ads.googleads.v19.services.ConversationB\x03\xe0A\x02"p\n\x1eAppendLeadConversationResponse\x12N\n\tresponses\x18\x01 \x03(\x0b26.google.ads.googleads.v19.services.ConversationOrErrorB\x03\xe0A\x02"r\n\x0cConversation\x12O\n\x13local_services_lead\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead\x12\x11\n\x04text\x18\x02 \x01(\tB\x03\xe0A\x02"\x9b\x01\n\x13ConversationOrError\x12*\n local_services_lead_conversation\x18\x01 \x01(\tH\x00\x123\n\x15partial_failure_error\x18\x02 \x01(\x0b2\x12.google.rpc.StatusH\x00B#\n!append_lead_conversation_response"\xbd\x01\n\x0fSurveySatisfied\x12\x86\x01\n\x17survey_satisfied_reason\x18\x01 \x01(\x0e2`.google.ads.googleads.v19.enums.LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReasonB\x03\xe0A\x02\x12!\n\x14other_reason_comment\x18\x02 \x01(\tB\x03\xe0A\x01"\xc9\x01\n\x12SurveyDissatisfied\x12\x8f\x01\n\x1asurvey_dissatisfied_reason\x18\x01 \x01(\x0e2f.google.ads.googleads.v19.enums.LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReasonB\x03\xe0A\x02\x12!\n\x14other_reason_comment\x18\x02 \x01(\tB\x03\xe0A\x01"\x8b\x03\n\x1aProvideLeadFeedbackRequest\x12I\n\rresource_name\x18\x01 \x01(\tB2\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead\x12j\n\rsurvey_answer\x18\x02 \x01(\x0e2N.google.ads.googleads.v19.enums.LocalServicesLeadSurveyAnswerEnum.SurveyAnswerB\x03\xe0A\x02\x12N\n\x10survey_satisfied\x18\x03 \x01(\x0b22.google.ads.googleads.v19.services.SurveySatisfiedH\x00\x12T\n\x13survey_dissatisfied\x18\x04 \x01(\x0b25.google.ads.googleads.v19.services.SurveyDissatisfiedH\x00B\x10\n\x0esurvey_details"\xa9\x01\n\x1bProvideLeadFeedbackResponse\x12\x89\x01\n\x18credit_issuance_decision\x18\x01 \x01(\x0e2b.google.ads.googleads.v19.enums.LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecisionB\x03\xe0A\x022\xda\x04\n\x18LocalServicesLeadService\x12\x89\x02\n\x16AppendLeadConversation\x12@.google.ads.googleads.v19.services.AppendLeadConversationRequest\x1aA.google.ads.googleads.v19.services.AppendLeadConversationResponse"j\xdaA\x19customer_id,conversations\x82\xd3\xe4\x93\x02H"C/v19/customers/{customer_id=*}/localServices:appendLeadConversation:\x01*\x12\xea\x01\n\x13ProvideLeadFeedback\x12=.google.ads.googleads.v19.services.ProvideLeadFeedbackRequest\x1a>.google.ads.googleads.v19.services.ProvideLeadFeedbackResponse"T\x82\xd3\xe4\x93\x02N"I/v19/{resource_name=customers/*/localServicesLeads/*}:provideLeadFeedback:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x89\x02\n%com.google.ads.googleads.v19.servicesB\x1dLocalServicesLeadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.services.local_services_lead_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v19.servicesB\x1dLocalServicesLeadServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v19/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V19.Services\xca\x02!Google\\Ads\\GoogleAds\\V19\\Services\xea\x02%Google::Ads::GoogleAds::V19::Services'
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['conversations']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONREQUEST'].fields_by_name['conversations']._serialized_options = b'\xe0A\x02'
    _globals['_APPENDLEADCONVERSATIONRESPONSE'].fields_by_name['responses']._loaded_options = None
    _globals['_APPENDLEADCONVERSATIONRESPONSE'].fields_by_name['responses']._serialized_options = b'\xe0A\x02'
    _globals['_CONVERSATION'].fields_by_name['local_services_lead']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['local_services_lead']._serialized_options = b'\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead'
    _globals['_CONVERSATION'].fields_by_name['text']._loaded_options = None
    _globals['_CONVERSATION'].fields_by_name['text']._serialized_options = b'\xe0A\x02'
    _globals['_SURVEYSATISFIED'].fields_by_name['survey_satisfied_reason']._loaded_options = None
    _globals['_SURVEYSATISFIED'].fields_by_name['survey_satisfied_reason']._serialized_options = b'\xe0A\x02'
    _globals['_SURVEYSATISFIED'].fields_by_name['other_reason_comment']._loaded_options = None
    _globals['_SURVEYSATISFIED'].fields_by_name['other_reason_comment']._serialized_options = b'\xe0A\x01'
    _globals['_SURVEYDISSATISFIED'].fields_by_name['survey_dissatisfied_reason']._loaded_options = None
    _globals['_SURVEYDISSATISFIED'].fields_by_name['survey_dissatisfied_reason']._serialized_options = b'\xe0A\x02'
    _globals['_SURVEYDISSATISFIED'].fields_by_name['other_reason_comment']._loaded_options = None
    _globals['_SURVEYDISSATISFIED'].fields_by_name['other_reason_comment']._serialized_options = b'\xe0A\x01'
    _globals['_PROVIDELEADFEEDBACKREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PROVIDELEADFEEDBACKREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA,\n*googleads.googleapis.com/LocalServicesLead'
    _globals['_PROVIDELEADFEEDBACKREQUEST'].fields_by_name['survey_answer']._loaded_options = None
    _globals['_PROVIDELEADFEEDBACKREQUEST'].fields_by_name['survey_answer']._serialized_options = b'\xe0A\x02'
    _globals['_PROVIDELEADFEEDBACKRESPONSE'].fields_by_name['credit_issuance_decision']._loaded_options = None
    _globals['_PROVIDELEADFEEDBACKRESPONSE'].fields_by_name['credit_issuance_decision']._serialized_options = b'\xe0A\x02'
    _globals['_LOCALSERVICESLEADSERVICE']._loaded_options = None
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['AppendLeadConversation']._loaded_options = None
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['AppendLeadConversation']._serialized_options = b'\xdaA\x19customer_id,conversations\x82\xd3\xe4\x93\x02H"C/v19/customers/{customer_id=*}/localServices:appendLeadConversation:\x01*'
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['ProvideLeadFeedback']._loaded_options = None
    _globals['_LOCALSERVICESLEADSERVICE'].methods_by_name['ProvideLeadFeedback']._serialized_options = b'\x82\xd3\xe4\x93\x02N"I/v19/{resource_name=customers/*/localServicesLeads/*}:provideLeadFeedback:\x01*'
    _globals['_APPENDLEADCONVERSATIONREQUEST']._serialized_start = 569
    _globals['_APPENDLEADCONVERSATIONREQUEST']._serialized_end = 703
    _globals['_APPENDLEADCONVERSATIONRESPONSE']._serialized_start = 705
    _globals['_APPENDLEADCONVERSATIONRESPONSE']._serialized_end = 817
    _globals['_CONVERSATION']._serialized_start = 819
    _globals['_CONVERSATION']._serialized_end = 933
    _globals['_CONVERSATIONORERROR']._serialized_start = 936
    _globals['_CONVERSATIONORERROR']._serialized_end = 1091
    _globals['_SURVEYSATISFIED']._serialized_start = 1094
    _globals['_SURVEYSATISFIED']._serialized_end = 1283
    _globals['_SURVEYDISSATISFIED']._serialized_start = 1286
    _globals['_SURVEYDISSATISFIED']._serialized_end = 1487
    _globals['_PROVIDELEADFEEDBACKREQUEST']._serialized_start = 1490
    _globals['_PROVIDELEADFEEDBACKREQUEST']._serialized_end = 1885
    _globals['_PROVIDELEADFEEDBACKRESPONSE']._serialized_start = 1888
    _globals['_PROVIDELEADFEEDBACKRESPONSE']._serialized_end = 2057
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_start = 2060
    _globals['_LOCALSERVICESLEADSERVICE']._serialized_end = 2662