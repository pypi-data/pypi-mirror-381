"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v20/services/experiment_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v20.resources import experiment_pb2 as google_dot_ads_dot_googleads_dot_v20_dot_resources_dot_experiment__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n:google/ads/googleads/v20/services/experiment_service.proto\x12!google.ads.googleads.v20.services\x1a3google/ads/googleads/v20/resources/experiment.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xb5\x01\n\x18MutateExperimentsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12O\n\noperations\x18\x02 \x03(\x0b26.google.ads.googleads.v20.services.ExperimentOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\x93\x02\n\x13ExperimentOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12@\n\x06create\x18\x01 \x01(\x0b2..google.ads.googleads.v20.resources.ExperimentH\x00\x12@\n\x06update\x18\x02 \x01(\x0b2..google.ads.googleads.v20.resources.ExperimentH\x00\x12:\n\x06remove\x18\x03 \x01(\tB(\xfaA%\n#googleads.googleapis.com/ExperimentH\x00B\x0b\n\toperation"\x9a\x01\n\x19MutateExperimentsResponse\x121\n\x15partial_failure_error\x18\x01 \x01(\x0b2\x12.google.rpc.Status\x12J\n\x07results\x18\x02 \x03(\x0b29.google.ads.googleads.v20.services.MutateExperimentResult"Y\n\x16MutateExperimentResult\x12?\n\rresource_name\x18\x01 \x01(\tB(\xfaA%\n#googleads.googleapis.com/Experiment"n\n\x14EndExperimentRequest\x12?\n\nexperiment\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08"\x8d\x01\n ListExperimentAsyncErrorsRequest\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment\x12\x12\n\npage_token\x18\x02 \x01(\t\x12\x11\n\tpage_size\x18\x03 \x01(\x05"`\n!ListExperimentAsyncErrorsResponse\x12"\n\x06errors\x18\x01 \x03(\x0b2\x12.google.rpc.Status\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\xd4\x01\n\x19GraduateExperimentRequest\x12?\n\nexperiment\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment\x12_\n\x18campaign_budget_mappings\x18\x02 \x03(\x0b28.google.ads.googleads.v20.services.CampaignBudgetMappingB\x03\xe0A\x02\x12\x15\n\rvalidate_only\x18\x03 \x01(\x08"\xa9\x01\n\x15CampaignBudgetMapping\x12F\n\x13experiment_campaign\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!googleads.googleapis.com/Campaign\x12H\n\x0fcampaign_budget\x18\x02 \x01(\tB/\xe0A\x02\xfaA)\n\'googleads.googleapis.com/CampaignBudget"v\n\x19ScheduleExperimentRequest\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08"]\n\x1aScheduleExperimentMetadata\x12?\n\nexperiment\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment"u\n\x18PromoteExperimentRequest\x12B\n\rresource_name\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment\x12\x15\n\rvalidate_only\x18\x02 \x01(\x08"\\\n\x19PromoteExperimentMetadata\x12?\n\nexperiment\x18\x01 \x01(\tB+\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment2\xb3\x0c\n\x11ExperimentService\x12\xe5\x01\n\x11MutateExperiments\x12;.google.ads.googleads.v20.services.MutateExperimentsRequest\x1a<.google.ads.googleads.v20.services.MutateExperimentsResponse"U\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x026"1/v20/customers/{customer_id=*}/experiments:mutate:\x01*\x12\xb3\x01\n\rEndExperiment\x127.google.ads.googleads.v20.services.EndExperimentRequest\x1a\x16.google.protobuf.Empty"Q\xdaA\nexperiment\x82\xd3\xe4\x93\x02>"9/v20/{experiment=customers/*/experiments/*}:endExperiment:\x01*\x12\x88\x02\n\x19ListExperimentAsyncErrors\x12C.google.ads.googleads.v20.services.ListExperimentAsyncErrorsRequest\x1aD.google.ads.googleads.v20.services.ListExperimentAsyncErrorsResponse"`\xdaA\rresource_name\x82\xd3\xe4\x93\x02J\x12H/v20/{resource_name=customers/*/experiments/*}:listExperimentAsyncErrors\x12\xdb\x01\n\x12GraduateExperiment\x12<.google.ads.googleads.v20.services.GraduateExperimentRequest\x1a\x16.google.protobuf.Empty"o\xdaA#experiment,campaign_budget_mappings\x82\xd3\xe4\x93\x02C">/v20/{experiment=customers/*/experiments/*}:graduateExperiment:\x01*\x12\xa8\x02\n\x12ScheduleExperiment\x12<.google.ads.googleads.v20.services.ScheduleExperimentRequest\x1a\x1d.google.longrunning.Operation"\xb4\x01\xcaAU\n\x15google.protobuf.Empty\x12<google.ads.googleads.v20.services.ScheduleExperimentMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02F"A/v20/{resource_name=customers/*/experiments/*}:scheduleExperiment:\x01*\x12\xa4\x02\n\x11PromoteExperiment\x12;.google.ads.googleads.v20.services.PromoteExperimentRequest\x1a\x1d.google.longrunning.Operation"\xb2\x01\xcaAT\n\x15google.protobuf.Empty\x12;google.ads.googleads.v20.services.PromoteExperimentMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02E"@/v20/{resource_name=customers/*/experiments/*}:promoteExperiment:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x82\x02\n%com.google.ads.googleads.v20.servicesB\x16ExperimentServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v20.services.experiment_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v20.servicesB\x16ExperimentServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v20/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V20.Services\xca\x02!Google\\Ads\\GoogleAds\\V20\\Services\xea\x02%Google::Ads::GoogleAds::V20::Services'
    _globals['_MUTATEEXPERIMENTSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEEXPERIMENTSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEEXPERIMENTSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEEXPERIMENTSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_EXPERIMENTOPERATION'].fields_by_name['remove']._loaded_options = None
    _globals['_EXPERIMENTOPERATION'].fields_by_name['remove']._serialized_options = b'\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_MUTATEEXPERIMENTRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEEXPERIMENTRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_ENDEXPERIMENTREQUEST'].fields_by_name['experiment']._loaded_options = None
    _globals['_ENDEXPERIMENTREQUEST'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_LISTEXPERIMENTASYNCERRORSREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_LISTEXPERIMENTASYNCERRORSREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_GRADUATEEXPERIMENTREQUEST'].fields_by_name['experiment']._loaded_options = None
    _globals['_GRADUATEEXPERIMENTREQUEST'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_GRADUATEEXPERIMENTREQUEST'].fields_by_name['campaign_budget_mappings']._loaded_options = None
    _globals['_GRADUATEEXPERIMENTREQUEST'].fields_by_name['campaign_budget_mappings']._serialized_options = b'\xe0A\x02'
    _globals['_CAMPAIGNBUDGETMAPPING'].fields_by_name['experiment_campaign']._loaded_options = None
    _globals['_CAMPAIGNBUDGETMAPPING'].fields_by_name['experiment_campaign']._serialized_options = b'\xe0A\x02\xfaA#\n!googleads.googleapis.com/Campaign'
    _globals['_CAMPAIGNBUDGETMAPPING'].fields_by_name['campaign_budget']._loaded_options = None
    _globals['_CAMPAIGNBUDGETMAPPING'].fields_by_name['campaign_budget']._serialized_options = b"\xe0A\x02\xfaA)\n'googleads.googleapis.com/CampaignBudget"
    _globals['_SCHEDULEEXPERIMENTREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_SCHEDULEEXPERIMENTREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_SCHEDULEEXPERIMENTMETADATA'].fields_by_name['experiment']._loaded_options = None
    _globals['_SCHEDULEEXPERIMENTMETADATA'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_PROMOTEEXPERIMENTREQUEST'].fields_by_name['resource_name']._loaded_options = None
    _globals['_PROMOTEEXPERIMENTREQUEST'].fields_by_name['resource_name']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_PROMOTEEXPERIMENTMETADATA'].fields_by_name['experiment']._loaded_options = None
    _globals['_PROMOTEEXPERIMENTMETADATA'].fields_by_name['experiment']._serialized_options = b'\xe0A\x02\xfaA%\n#googleads.googleapis.com/Experiment'
    _globals['_EXPERIMENTSERVICE']._loaded_options = None
    _globals['_EXPERIMENTSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_EXPERIMENTSERVICE'].methods_by_name['MutateExperiments']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['MutateExperiments']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x026"1/v20/customers/{customer_id=*}/experiments:mutate:\x01*'
    _globals['_EXPERIMENTSERVICE'].methods_by_name['EndExperiment']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['EndExperiment']._serialized_options = b'\xdaA\nexperiment\x82\xd3\xe4\x93\x02>"9/v20/{experiment=customers/*/experiments/*}:endExperiment:\x01*'
    _globals['_EXPERIMENTSERVICE'].methods_by_name['ListExperimentAsyncErrors']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['ListExperimentAsyncErrors']._serialized_options = b'\xdaA\rresource_name\x82\xd3\xe4\x93\x02J\x12H/v20/{resource_name=customers/*/experiments/*}:listExperimentAsyncErrors'
    _globals['_EXPERIMENTSERVICE'].methods_by_name['GraduateExperiment']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['GraduateExperiment']._serialized_options = b'\xdaA#experiment,campaign_budget_mappings\x82\xd3\xe4\x93\x02C">/v20/{experiment=customers/*/experiments/*}:graduateExperiment:\x01*'
    _globals['_EXPERIMENTSERVICE'].methods_by_name['ScheduleExperiment']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['ScheduleExperiment']._serialized_options = b'\xcaAU\n\x15google.protobuf.Empty\x12<google.ads.googleads.v20.services.ScheduleExperimentMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02F"A/v20/{resource_name=customers/*/experiments/*}:scheduleExperiment:\x01*'
    _globals['_EXPERIMENTSERVICE'].methods_by_name['PromoteExperiment']._loaded_options = None
    _globals['_EXPERIMENTSERVICE'].methods_by_name['PromoteExperiment']._serialized_options = b'\xcaAT\n\x15google.protobuf.Empty\x12;google.ads.googleads.v20.services.PromoteExperimentMetadata\xdaA\rresource_name\x82\xd3\xe4\x93\x02E"@/v20/{resource_name=customers/*/experiments/*}:promoteExperiment:\x01*'
    _globals['_MUTATEEXPERIMENTSREQUEST']._serialized_start = 391
    _globals['_MUTATEEXPERIMENTSREQUEST']._serialized_end = 572
    _globals['_EXPERIMENTOPERATION']._serialized_start = 575
    _globals['_EXPERIMENTOPERATION']._serialized_end = 850
    _globals['_MUTATEEXPERIMENTSRESPONSE']._serialized_start = 853
    _globals['_MUTATEEXPERIMENTSRESPONSE']._serialized_end = 1007
    _globals['_MUTATEEXPERIMENTRESULT']._serialized_start = 1009
    _globals['_MUTATEEXPERIMENTRESULT']._serialized_end = 1098
    _globals['_ENDEXPERIMENTREQUEST']._serialized_start = 1100
    _globals['_ENDEXPERIMENTREQUEST']._serialized_end = 1210
    _globals['_LISTEXPERIMENTASYNCERRORSREQUEST']._serialized_start = 1213
    _globals['_LISTEXPERIMENTASYNCERRORSREQUEST']._serialized_end = 1354
    _globals['_LISTEXPERIMENTASYNCERRORSRESPONSE']._serialized_start = 1356
    _globals['_LISTEXPERIMENTASYNCERRORSRESPONSE']._serialized_end = 1452
    _globals['_GRADUATEEXPERIMENTREQUEST']._serialized_start = 1455
    _globals['_GRADUATEEXPERIMENTREQUEST']._serialized_end = 1667
    _globals['_CAMPAIGNBUDGETMAPPING']._serialized_start = 1670
    _globals['_CAMPAIGNBUDGETMAPPING']._serialized_end = 1839
    _globals['_SCHEDULEEXPERIMENTREQUEST']._serialized_start = 1841
    _globals['_SCHEDULEEXPERIMENTREQUEST']._serialized_end = 1959
    _globals['_SCHEDULEEXPERIMENTMETADATA']._serialized_start = 1961
    _globals['_SCHEDULEEXPERIMENTMETADATA']._serialized_end = 2054
    _globals['_PROMOTEEXPERIMENTREQUEST']._serialized_start = 2056
    _globals['_PROMOTEEXPERIMENTREQUEST']._serialized_end = 2173
    _globals['_PROMOTEEXPERIMENTMETADATA']._serialized_start = 2175
    _globals['_PROMOTEEXPERIMENTMETADATA']._serialized_end = 2267
    _globals['_EXPERIMENTSERVICE']._serialized_start = 2270
    _globals['_EXPERIMENTSERVICE']._serialized_end = 3857