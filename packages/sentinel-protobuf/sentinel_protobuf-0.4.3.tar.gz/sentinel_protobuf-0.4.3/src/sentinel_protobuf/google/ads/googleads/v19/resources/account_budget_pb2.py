"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/account_budget.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import account_budget_proposal_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_account__budget__proposal__type__pb2
from ......google.ads.googleads.v19.enums import account_budget_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_account__budget__status__pb2
from ......google.ads.googleads.v19.enums import spending_limit_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_spending__limit__type__pb2
from ......google.ads.googleads.v19.enums import time_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_time__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7google/ads/googleads/v19/resources/account_budget.proto\x12"google.ads.googleads.v19.resources\x1aAgoogle/ads/googleads/v19/enums/account_budget_proposal_type.proto\x1a:google/ads/googleads/v19/enums/account_budget_status.proto\x1a8google/ads/googleads/v19/enums/spending_limit_type.proto\x1a.google/ads/googleads/v19/enums/time_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x90\x14\n\rAccountBudget\x12E\n\rresource_name\x18\x01 \x01(\tB.\xe0A\x03\xfaA(\n&googleads.googleapis.com/AccountBudget\x12\x14\n\x02id\x18\x17 \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12I\n\rbilling_setup\x18\x18 \x01(\tB-\xe0A\x03\xfaA\'\n%googleads.googleapis.com/BillingSetupH\x06\x88\x01\x01\x12`\n\x06status\x18\x04 \x01(\x0e2K.google.ads.googleads.v19.enums.AccountBudgetStatusEnum.AccountBudgetStatusB\x03\xe0A\x03\x12\x16\n\x04name\x18\x19 \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01\x12*\n\x18proposed_start_date_time\x18\x1a \x01(\tB\x03\xe0A\x03H\x08\x88\x01\x01\x12*\n\x18approved_start_date_time\x18\x1b \x01(\tB\x03\xe0A\x03H\t\x88\x01\x01\x12%\n\x18total_adjustments_micros\x18! \x01(\x03B\x03\xe0A\x03\x12!\n\x14amount_served_micros\x18" \x01(\x03B\x03\xe0A\x03\x12\'\n\x15purchase_order_number\x18# \x01(\tB\x03\xe0A\x03H\n\x88\x01\x01\x12\x17\n\x05notes\x18$ \x01(\tB\x03\xe0A\x03H\x0b\x88\x01\x01\x12m\n\x10pending_proposal\x18\x16 \x01(\x0b2N.google.ads.googleads.v19.resources.AccountBudget.PendingAccountBudgetProposalB\x03\xe0A\x03\x12%\n\x16proposed_end_date_time\x18\x1c \x01(\tB\x03\xe0A\x03H\x00\x12\\\n\x16proposed_end_time_type\x18\t \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x03H\x00\x12%\n\x16approved_end_date_time\x18\x1d \x01(\tB\x03\xe0A\x03H\x01\x12\\\n\x16approved_end_time_type\x18\x0b \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x03H\x01\x12-\n\x1eproposed_spending_limit_micros\x18\x1e \x01(\x03B\x03\xe0A\x03H\x02\x12t\n\x1cproposed_spending_limit_type\x18\r \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x03H\x02\x12-\n\x1eapproved_spending_limit_micros\x18\x1f \x01(\x03B\x03\xe0A\x03H\x03\x12t\n\x1capproved_spending_limit_type\x18\x0f \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x03H\x03\x12-\n\x1eadjusted_spending_limit_micros\x18  \x01(\x03B\x03\xe0A\x03H\x04\x12t\n\x1cadjusted_spending_limit_type\x18\x11 \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x03H\x04\x1a\xac\x06\n\x1cPendingAccountBudgetProposal\x12\\\n\x17account_budget_proposal\x18\x0c \x01(\tB6\xe0A\x03\xfaA0\n.googleads.googleapis.com/AccountBudgetProposalH\x02\x88\x01\x01\x12s\n\rproposal_type\x18\x02 \x01(\x0e2W.google.ads.googleads.v19.enums.AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeB\x03\xe0A\x03\x12\x16\n\x04name\x18\r \x01(\tB\x03\xe0A\x03H\x03\x88\x01\x01\x12!\n\x0fstart_date_time\x18\x0e \x01(\tB\x03\xe0A\x03H\x04\x88\x01\x01\x12\'\n\x15purchase_order_number\x18\x11 \x01(\tB\x03\xe0A\x03H\x05\x88\x01\x01\x12\x17\n\x05notes\x18\x12 \x01(\tB\x03\xe0A\x03H\x06\x88\x01\x01\x12$\n\x12creation_date_time\x18\x13 \x01(\tB\x03\xe0A\x03H\x07\x88\x01\x01\x12\x1c\n\rend_date_time\x18\x0f \x01(\tB\x03\xe0A\x03H\x00\x12S\n\rend_time_type\x18\x06 \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x03H\x00\x12$\n\x15spending_limit_micros\x18\x10 \x01(\x03B\x03\xe0A\x03H\x01\x12k\n\x13spending_limit_type\x18\x08 \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x03H\x01B\n\n\x08end_timeB\x10\n\x0espending_limitB\x1a\n\x18_account_budget_proposalB\x07\n\x05_nameB\x12\n\x10_start_date_timeB\x18\n\x16_purchase_order_numberB\x08\n\x06_notesB\x15\n\x13_creation_date_time:g\xeaAd\n&googleads.googleapis.com/AccountBudget\x12:customers/{customer_id}/accountBudgets/{account_budget_id}B\x13\n\x11proposed_end_timeB\x13\n\x11approved_end_timeB\x19\n\x17proposed_spending_limitB\x19\n\x17approved_spending_limitB\x19\n\x17adjusted_spending_limitB\x05\n\x03_idB\x10\n\x0e_billing_setupB\x07\n\x05_nameB\x1b\n\x19_proposed_start_date_timeB\x1b\n\x19_approved_start_date_timeB\x18\n\x16_purchase_order_numberB\x08\n\x06_notesB\x84\x02\n&com.google.ads.googleads.v19.resourcesB\x12AccountBudgetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.account_budget_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x12AccountBudgetProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['account_budget_proposal']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['account_budget_proposal']._serialized_options = b'\xe0A\x03\xfaA0\n.googleads.googleapis.com/AccountBudgetProposal'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['proposal_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['proposal_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['start_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['start_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['purchase_order_number']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['purchase_order_number']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['notes']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['notes']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['end_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['end_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['end_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['end_time_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['spending_limit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL'].fields_by_name['spending_limit_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x03\xfaA(\n&googleads.googleapis.com/AccountBudget'
    _globals['_ACCOUNTBUDGET'].fields_by_name['id']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['billing_setup']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['billing_setup']._serialized_options = b"\xe0A\x03\xfaA'\n%googleads.googleapis.com/BillingSetup"
    _globals['_ACCOUNTBUDGET'].fields_by_name['status']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['name']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_start_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_start_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_start_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_start_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['total_adjustments_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['total_adjustments_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['amount_served_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['amount_served_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['purchase_order_number']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['purchase_order_number']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['notes']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['notes']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['pending_proposal']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['pending_proposal']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_end_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_end_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_end_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_end_time_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_end_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_end_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_end_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_end_time_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_spending_limit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['proposed_spending_limit_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_spending_limit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['approved_spending_limit_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['adjusted_spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['adjusted_spending_limit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET'].fields_by_name['adjusted_spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGET'].fields_by_name['adjusted_spending_limit_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGET']._loaded_options = None
    _globals['_ACCOUNTBUDGET']._serialized_options = b'\xeaAd\n&googleads.googleapis.com/AccountBudget\x12:customers/{customer_id}/accountBudgets/{account_budget_id}'
    _globals['_ACCOUNTBUDGET']._serialized_start = 389
    _globals['_ACCOUNTBUDGET']._serialized_end = 2965
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL']._serialized_start = 1797
    _globals['_ACCOUNTBUDGET_PENDINGACCOUNTBUDGETPROPOSAL']._serialized_end = 2609