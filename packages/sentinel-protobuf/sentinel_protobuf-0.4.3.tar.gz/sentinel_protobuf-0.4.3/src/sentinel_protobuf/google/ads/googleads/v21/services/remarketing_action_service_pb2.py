"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ads/googleads/v21/services/remarketing_action_service.proto')
_sym_db = _symbol_database.Default()
from ......google.ads.googleads.v21.resources import remarketing_action_pb2 as google_dot_ads_dot_googleads_dot_v21_dot_resources_dot_remarketing__action__pb2
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from ......google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nBgoogle/ads/googleads/v21/services/remarketing_action_service.proto\x12!google.ads.googleads.v21.services\x1a;google/ads/googleads/v21/resources/remarketing_action.proto\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a google/protobuf/field_mask.proto\x1a\x17google/rpc/status.proto"\xc3\x01\n\x1fMutateRemarketingActionsRequest\x12\x18\n\x0bcustomer_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12V\n\noperations\x18\x02 \x03(\x0b2=.google.ads.googleads.v21.services.RemarketingActionOperationB\x03\xe0A\x02\x12\x17\n\x0fpartial_failure\x18\x03 \x01(\x08\x12\x15\n\rvalidate_only\x18\x04 \x01(\x08"\xec\x01\n\x1aRemarketingActionOperation\x12/\n\x0bupdate_mask\x18\x04 \x01(\x0b2\x1a.google.protobuf.FieldMask\x12G\n\x06create\x18\x01 \x01(\x0b25.google.ads.googleads.v21.resources.RemarketingActionH\x00\x12G\n\x06update\x18\x02 \x01(\x0b25.google.ads.googleads.v21.resources.RemarketingActionH\x00B\x0b\n\toperation"\xa8\x01\n MutateRemarketingActionsResponse\x121\n\x15partial_failure_error\x18\x03 \x01(\x0b2\x12.google.rpc.Status\x12Q\n\x07results\x18\x02 \x03(\x0b2@.google.ads.googleads.v21.services.MutateRemarketingActionResult"g\n\x1dMutateRemarketingActionResult\x12F\n\rresource_name\x18\x01 \x01(\tB/\xfaA,\n*googleads.googleapis.com/RemarketingAction2\xe5\x02\n\x18RemarketingActionService\x12\x81\x02\n\x18MutateRemarketingActions\x12B.google.ads.googleads.v21.services.MutateRemarketingActionsRequest\x1aC.google.ads.googleads.v21.services.MutateRemarketingActionsResponse"\\\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02="8/v21/customers/{customer_id=*}/remarketingActions:mutate:\x01*\x1aE\xcaA\x18googleads.googleapis.com\xd2A\'https://www.googleapis.com/auth/adwordsB\x89\x02\n%com.google.ads.googleads.v21.servicesB\x1dRemarketingActionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Servicesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ads.googleads.v21.services.remarketing_action_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n%com.google.ads.googleads.v21.servicesB\x1dRemarketingActionServiceProtoP\x01ZIgoogle.golang.org/genproto/googleapis/ads/googleads/v21/services;services\xa2\x02\x03GAA\xaa\x02!Google.Ads.GoogleAds.V21.Services\xca\x02!Google\\Ads\\GoogleAds\\V21\\Services\xea\x02%Google::Ads::GoogleAds::V21::Services'
    _globals['_MUTATEREMARKETINGACTIONSREQUEST'].fields_by_name['customer_id']._loaded_options = None
    _globals['_MUTATEREMARKETINGACTIONSREQUEST'].fields_by_name['customer_id']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEREMARKETINGACTIONSREQUEST'].fields_by_name['operations']._loaded_options = None
    _globals['_MUTATEREMARKETINGACTIONSREQUEST'].fields_by_name['operations']._serialized_options = b'\xe0A\x02'
    _globals['_MUTATEREMARKETINGACTIONRESULT'].fields_by_name['resource_name']._loaded_options = None
    _globals['_MUTATEREMARKETINGACTIONRESULT'].fields_by_name['resource_name']._serialized_options = b'\xfaA,\n*googleads.googleapis.com/RemarketingAction'
    _globals['_REMARKETINGACTIONSERVICE']._loaded_options = None
    _globals['_REMARKETINGACTIONSERVICE']._serialized_options = b"\xcaA\x18googleads.googleapis.com\xd2A'https://www.googleapis.com/auth/adwords"
    _globals['_REMARKETINGACTIONSERVICE'].methods_by_name['MutateRemarketingActions']._loaded_options = None
    _globals['_REMARKETINGACTIONSERVICE'].methods_by_name['MutateRemarketingActions']._serialized_options = b'\xdaA\x16customer_id,operations\x82\xd3\xe4\x93\x02="8/v21/customers/{customer_id=*}/remarketingActions:mutate:\x01*'
    _globals['_MUTATEREMARKETINGACTIONSREQUEST']._serialized_start = 341
    _globals['_MUTATEREMARKETINGACTIONSREQUEST']._serialized_end = 536
    _globals['_REMARKETINGACTIONOPERATION']._serialized_start = 539
    _globals['_REMARKETINGACTIONOPERATION']._serialized_end = 775
    _globals['_MUTATEREMARKETINGACTIONSRESPONSE']._serialized_start = 778
    _globals['_MUTATEREMARKETINGACTIONSRESPONSE']._serialized_end = 946
    _globals['_MUTATEREMARKETINGACTIONRESULT']._serialized_start = 948
    _globals['_MUTATEREMARKETINGACTIONRESULT']._serialized_end = 1051
    _globals['_REMARKETINGACTIONSERVICE']._serialized_start = 1054
    _globals['_REMARKETINGACTIONSERVICE']._serialized_end = 1411