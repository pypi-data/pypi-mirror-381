"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v19/resources/account_budget_proposal.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v19.enums import account_budget_proposal_status_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_account__budget__proposal__status__pb2
from ......google.ads.googleads.v19.enums import account_budget_proposal_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_account__budget__proposal__type__pb2
from ......google.ads.googleads.v19.enums import spending_limit_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_spending__limit__type__pb2
from ......google.ads.googleads.v19.enums import time_type_pb2 as google_dot_ads_dot_googleads_dot_v19_dot_enums_dot_time__type__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@google/ads/googleads/v19/resources/account_budget_proposal.proto\x12"google.ads.googleads.v19.resources\x1aCgoogle/ads/googleads/v19/enums/account_budget_proposal_status.proto\x1aAgoogle/ads/googleads/v19/enums/account_budget_proposal_type.proto\x1a8google/ads/googleads/v19/enums/spending_limit_type.proto\x1a.google/ads/googleads/v19/enums/time_type.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\xfe\x0e\n\x15AccountBudgetProposal\x12M\n\rresource_name\x18\x01 \x01(\tB6\xe0A\x05\xfaA0\n.googleads.googleapis.com/AccountBudgetProposal\x12\x14\n\x02id\x18\x19 \x01(\x03B\x03\xe0A\x03H\x05\x88\x01\x01\x12I\n\rbilling_setup\x18\x1a \x01(\tB-\xe0A\x05\xfaA\'\n%googleads.googleapis.com/BillingSetupH\x06\x88\x01\x01\x12K\n\x0eaccount_budget\x18\x1b \x01(\tB.\xe0A\x05\xfaA(\n&googleads.googleapis.com/AccountBudgetH\x07\x88\x01\x01\x12s\n\rproposal_type\x18\x04 \x01(\x0e2W.google.ads.googleads.v19.enums.AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeB\x03\xe0A\x05\x12p\n\x06status\x18\x0f \x01(\x0e2[.google.ads.googleads.v19.enums.AccountBudgetProposalStatusEnum.AccountBudgetProposalStatusB\x03\xe0A\x03\x12\x1f\n\rproposed_name\x18\x1c \x01(\tB\x03\xe0A\x05H\x08\x88\x01\x01\x12*\n\x18approved_start_date_time\x18\x1e \x01(\tB\x03\xe0A\x03H\t\x88\x01\x01\x120\n\x1eproposed_purchase_order_number\x18# \x01(\tB\x03\xe0A\x05H\n\x88\x01\x01\x12 \n\x0eproposed_notes\x18$ \x01(\tB\x03\xe0A\x05H\x0b\x88\x01\x01\x12$\n\x12creation_date_time\x18% \x01(\tB\x03\xe0A\x03H\x0c\x88\x01\x01\x12$\n\x12approval_date_time\x18& \x01(\tB\x03\xe0A\x03H\r\x88\x01\x01\x12\'\n\x18proposed_start_date_time\x18\x1d \x01(\tB\x03\xe0A\x05H\x00\x12^\n\x18proposed_start_time_type\x18\x07 \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x05H\x00\x12%\n\x16proposed_end_date_time\x18\x1f \x01(\tB\x03\xe0A\x05H\x01\x12\\\n\x16proposed_end_time_type\x18\t \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x05H\x01\x12%\n\x16approved_end_date_time\x18  \x01(\tB\x03\xe0A\x03H\x02\x12\\\n\x16approved_end_time_type\x18\x16 \x01(\x0e25.google.ads.googleads.v19.enums.TimeTypeEnum.TimeTypeB\x03\xe0A\x03H\x02\x12-\n\x1eproposed_spending_limit_micros\x18! \x01(\x03B\x03\xe0A\x05H\x03\x12t\n\x1cproposed_spending_limit_type\x18\x0b \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x05H\x03\x12-\n\x1eapproved_spending_limit_micros\x18" \x01(\x03B\x03\xe0A\x03H\x04\x12t\n\x1capproved_spending_limit_type\x18\x18 \x01(\x0e2G.google.ads.googleads.v19.enums.SpendingLimitTypeEnum.SpendingLimitTypeB\x03\xe0A\x03H\x04:\x80\x01\xeaA}\n.googleads.googleapis.com/AccountBudgetProposal\x12Kcustomers/{customer_id}/accountBudgetProposals/{account_budget_proposal_id}B\x15\n\x13proposed_start_timeB\x13\n\x11proposed_end_timeB\x13\n\x11approved_end_timeB\x19\n\x17proposed_spending_limitB\x19\n\x17approved_spending_limitB\x05\n\x03_idB\x10\n\x0e_billing_setupB\x11\n\x0f_account_budgetB\x10\n\x0e_proposed_nameB\x1b\n\x19_approved_start_date_timeB!\n\x1f_proposed_purchase_order_numberB\x11\n\x0f_proposed_notesB\x15\n\x13_creation_date_timeB\x15\n\x13_approval_date_timeB\x8c\x02\n&com.google.ads.googleads.v19.resourcesB\x1aAccountBudgetProposalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resourcesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v19.resources.account_budget_proposal_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n&com.google.ads.googleads.v19.resourcesB\x1aAccountBudgetProposalProtoP\x01ZKgoogle.golang.org/genproto/googleapis/ads/googleads/v19/resources;resources\xa2\x02\x03GAA\xaa\x02"Google.Ads.GoogleAds.V19.Resources\xca\x02"Google\\Ads\\GoogleAds\\V19\\Resources\xea\x02&Google::Ads::GoogleAds::V19::Resources'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['resource_name']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x05\xfaA0\n.googleads.googleapis.com/AccountBudgetProposal'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['id']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['billing_setup']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['billing_setup']._serialized_options = b"\xe0A\x05\xfaA'\n%googleads.googleapis.com/BillingSetup"
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['account_budget']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['account_budget']._serialized_options = b'\xe0A\x05\xfaA(\n&googleads.googleapis.com/AccountBudget'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposal_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposal_type']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['status']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_name']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_name']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_start_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_start_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_purchase_order_number']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_purchase_order_number']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_notes']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_notes']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['creation_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['creation_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approval_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approval_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_start_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_start_date_time']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_start_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_start_time_type']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_end_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_end_date_time']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_end_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_end_time_type']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_end_date_time']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_end_date_time']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_end_time_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_end_time_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_spending_limit_micros']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['proposed_spending_limit_type']._serialized_options = b'\xe0A\x05'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_spending_limit_micros']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_spending_limit_micros']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_spending_limit_type']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL'].fields_by_name['approved_spending_limit_type']._serialized_options = b'\xe0A\x03'
    _globals['_ACCOUNTBUDGETPROPOSAL']._loaded_options = None
    _globals['_ACCOUNTBUDGETPROPOSAL']._serialized_options = b'\xeaA}\n.googleads.googleapis.com/AccountBudgetProposal\x12Kcustomers/{customer_id}/accountBudgetProposals/{account_budget_proposal_id}'
    _globals['_ACCOUNTBUDGETPROPOSAL']._serialized_start = 407
    _globals['_ACCOUNTBUDGETPROPOSAL']._serialized_end = 2325