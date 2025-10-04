"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/saasplatform/saasservicemgmt/v1beta1/rollouts_service.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.saasplatform.saasservicemgmt.v1beta1 import rollouts_resources_pb2 as google_dot_cloud_dot_saasplatform_dot_saasservicemgmt_dot_v1beta1_dot_rollouts__resources__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nHgoogle/cloud/saasplatform/saasservicemgmt/v1beta1/rollouts_service.proto\x121google.cloud.saasplatform.saasservicemgmt.v1beta1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1aJgoogle/cloud/saasplatform/saasservicemgmt/v1beta1/rollouts_resources.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xa3\x01\n\x13ListRolloutsRequest\x12?\n\x06parent\x18\x96N \x01(\tB.\xe0A\x02\xfaA(\x12&saasservicemgmt.googleapis.com/Rollout\x12\x12\n\tpage_size\x18\x89R \x01(\x05\x12\x13\n\npage_token\x18\x8aR \x01(\t\x12\x0f\n\x06filter\x18\x8bR \x01(\t\x12\x11\n\x08order_by\x18\x8cR \x01(\t"\x95\x01\n\x14ListRolloutsResponse\x12M\n\x08rollouts\x18\x8dR \x03(\x0b2:.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout\x12\x18\n\x0fnext_page_token\x18\x8eR \x01(\t\x12\x14\n\x0bunreachable\x18\x8fR \x03(\t"R\n\x11GetRolloutRequest\x12=\n\x04name\x18\x91N \x01(\tB.\xe0A\x02\xfaA(\n&saasservicemgmt.googleapis.com/Rollout"\xf1\x01\n\x14CreateRolloutRequest\x12?\n\x06parent\x18\x96N \x01(\tB.\xe0A\x02\xfaA(\x12&saasservicemgmt.googleapis.com/Rollout\x12\x18\n\nrollout_id\x18\x87R \x01(\tB\x03\xe0A\x02\x12Q\n\x07rollout\x18\x88R \x01(\x0b2:.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutB\x03\xe0A\x02\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t"\xc8\x01\n\x14UpdateRolloutRequest\x12Q\n\x07rollout\x18\x88R \x01(\x0b2:.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutB\x03\xe0A\x02\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t\x120\n\x0bupdate_mask\x18\x90R \x01(\x0b2\x1a.google.protobuf.FieldMask"\x91\x01\n\x14DeleteRolloutRequest\x12=\n\x04name\x18\x91N \x01(\tB.\xe0A\x02\xfaA(\n&saasservicemgmt.googleapis.com/Rollout\x12\r\n\x04etag\x18\xdaO \x01(\t\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t"\xab\x01\n\x17ListRolloutKindsRequest\x12C\n\x06parent\x18\x96N \x01(\tB2\xe0A\x02\xfaA,\x12*saasservicemgmt.googleapis.com/RolloutKind\x12\x12\n\tpage_size\x18\x89R \x01(\x05\x12\x13\n\npage_token\x18\x8aR \x01(\t\x12\x0f\n\x06filter\x18\x8bR \x01(\t\x12\x11\n\x08order_by\x18\x8cR \x01(\t"\xa2\x01\n\x18ListRolloutKindsResponse\x12V\n\rrollout_kinds\x18\x8dR \x03(\x0b2>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind\x12\x18\n\x0fnext_page_token\x18\x8eR \x01(\t\x12\x14\n\x0bunreachable\x18\x8fR \x03(\t"Z\n\x15GetRolloutKindRequest\x12A\n\x04name\x18\x91N \x01(\tB2\xe0A\x02\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind"\x87\x02\n\x18CreateRolloutKindRequest\x12C\n\x06parent\x18\x96N \x01(\tB2\xe0A\x02\xfaA,\x12*saasservicemgmt.googleapis.com/RolloutKind\x12\x1d\n\x0frollout_kind_id\x18\x87R \x01(\tB\x03\xe0A\x02\x12Z\n\x0crollout_kind\x18\x88R \x01(\x0b2>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKindB\x03\xe0A\x02\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t"\xd5\x01\n\x18UpdateRolloutKindRequest\x12Z\n\x0crollout_kind\x18\x88R \x01(\x0b2>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKindB\x03\xe0A\x02\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t\x120\n\x0bupdate_mask\x18\x90R \x01(\x0b2\x1a.google.protobuf.FieldMask"\x99\x01\n\x18DeleteRolloutKindRequest\x12A\n\x04name\x18\x91N \x01(\tB2\xe0A\x02\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind\x12\r\n\x04etag\x18\xdaO \x01(\t\x12\x16\n\rvalidate_only\x18\x85R \x01(\x08\x12\x13\n\nrequest_id\x18\x86R \x01(\t2\x88\x13\n\x0cSaasRollouts\x12\xe3\x01\n\x0cListRollouts\x12F.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsRequest\x1aG.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutsResponse"B\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta1/{parent=projects/*/locations/*}/rollouts\x12\xd0\x01\n\nGetRollout\x12D.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutRequest\x1a:.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout"@\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/locations/*/rollouts/*}\x12\xf4\x01\n\rCreateRollout\x12G.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutRequest\x1a:.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout"^\xdaA\x19parent,rollout,rollout_id\x82\xd3\xe4\x93\x02<"1/v1beta1/{parent=projects/*/locations/*}/rollouts:\x07rollout\x12\xf6\x01\n\rUpdateRollout\x12G.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutRequest\x1a:.google.cloud.saasplatform.saasservicemgmt.v1beta1.Rollout"`\xdaA\x13rollout,update_mask\x82\xd3\xe4\x93\x02D29/v1beta1/{rollout.name=projects/*/locations/*/rollouts/*}:\x07rollout\x12\xb2\x01\n\rDeleteRollout\x12G.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutRequest\x1a\x16.google.protobuf.Empty"@\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/locations/*/rollouts/*}\x12\xf3\x01\n\x10ListRolloutKinds\x12J.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsRequest\x1aK.google.cloud.saasplatform.saasservicemgmt.v1beta1.ListRolloutKindsResponse"F\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/rolloutKinds\x12\xe0\x01\n\x0eGetRolloutKind\x12H.google.cloud.saasplatform.saasservicemgmt.v1beta1.GetRolloutKindRequest\x1a>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind"D\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/rolloutKinds/*}\x12\x93\x02\n\x11CreateRolloutKind\x12K.google.cloud.saasplatform.saasservicemgmt.v1beta1.CreateRolloutKindRequest\x1a>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind"q\xdaA#parent,rollout_kind,rollout_kind_id\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/rolloutKinds:\x0crollout_kind\x12\x95\x02\n\x11UpdateRolloutKind\x12K.google.cloud.saasplatform.saasservicemgmt.v1beta1.UpdateRolloutKindRequest\x1a>.google.cloud.saasplatform.saasservicemgmt.v1beta1.RolloutKind"s\xdaA\x18rollout_kind,update_mask\x82\xd3\xe4\x93\x02R2B/v1beta1/{rollout_kind.name=projects/*/locations/*/rolloutKinds/*}:\x0crollout_kind\x12\xbe\x01\n\x11DeleteRolloutKind\x12K.google.cloud.saasplatform.saasservicemgmt.v1beta1.DeleteRolloutKindRequest\x1a\x16.google.protobuf.Empty"D\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/rolloutKinds/*}\x1aR\xcaA\x1esaasservicemgmt.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\xd4\x02\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x18SaasRolloutsServiceProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.saasplatform.saasservicemgmt.v1beta1.rollouts_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n5com.google.cloud.saasplatform.saasservicemgmt.v1beta1B\x18SaasRolloutsServiceProtoP\x01Z_cloud.google.com/go/saasplatform/saasservicemgmt/apiv1beta1/saasservicemgmtpb;saasservicemgmtpb\xaa\x021Google.Cloud.SaasPlatform.SaasServiceMgmt.V1Beta1\xca\x021Google\\Cloud\\SaasPlatform\\SaasServiceMgmt\\V1beta1\xea\x025Google::Cloud::SaasPlatform::SaasServiceMgmt::V1beta1'
    _globals['_LISTROLLOUTSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTROLLOUTSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&saasservicemgmt.googleapis.com/Rollout'
    _globals['_GETROLLOUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETROLLOUTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&saasservicemgmt.googleapis.com/Rollout'
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA(\x12&saasservicemgmt.googleapis.com/Rollout'
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['rollout_id']._loaded_options = None
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['rollout_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['rollout']._loaded_options = None
    _globals['_CREATEROLLOUTREQUEST'].fields_by_name['rollout']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROLLOUTREQUEST'].fields_by_name['rollout']._loaded_options = None
    _globals['_UPDATEROLLOUTREQUEST'].fields_by_name['rollout']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROLLOUTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEROLLOUTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA(\n&saasservicemgmt.googleapis.com/Rollout'
    _globals['_LISTROLLOUTKINDSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTROLLOUTKINDSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*saasservicemgmt.googleapis.com/RolloutKind'
    _globals['_GETROLLOUTKINDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETROLLOUTKINDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind'
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA,\x12*saasservicemgmt.googleapis.com/RolloutKind'
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind_id']._loaded_options = None
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind']._loaded_options = None
    _globals['_CREATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind']._loaded_options = None
    _globals['_UPDATEROLLOUTKINDREQUEST'].fields_by_name['rollout_kind']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEROLLOUTKINDREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEROLLOUTKINDREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA,\n*saasservicemgmt.googleapis.com/RolloutKind'
    _globals['_SAASROLLOUTS']._loaded_options = None
    _globals['_SAASROLLOUTS']._serialized_options = b'\xcaA\x1esaasservicemgmt.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_SAASROLLOUTS'].methods_by_name['ListRollouts']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['ListRollouts']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x023\x121/v1beta1/{parent=projects/*/locations/*}/rollouts'
    _globals['_SAASROLLOUTS'].methods_by_name['GetRollout']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['GetRollout']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023\x121/v1beta1/{name=projects/*/locations/*/rollouts/*}'
    _globals['_SAASROLLOUTS'].methods_by_name['CreateRollout']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['CreateRollout']._serialized_options = b'\xdaA\x19parent,rollout,rollout_id\x82\xd3\xe4\x93\x02<"1/v1beta1/{parent=projects/*/locations/*}/rollouts:\x07rollout'
    _globals['_SAASROLLOUTS'].methods_by_name['UpdateRollout']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['UpdateRollout']._serialized_options = b'\xdaA\x13rollout,update_mask\x82\xd3\xe4\x93\x02D29/v1beta1/{rollout.name=projects/*/locations/*/rollouts/*}:\x07rollout'
    _globals['_SAASROLLOUTS'].methods_by_name['DeleteRollout']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['DeleteRollout']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x023*1/v1beta1/{name=projects/*/locations/*/rollouts/*}'
    _globals['_SAASROLLOUTS'].methods_by_name['ListRolloutKinds']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['ListRolloutKinds']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x027\x125/v1beta1/{parent=projects/*/locations/*}/rolloutKinds'
    _globals['_SAASROLLOUTS'].methods_by_name['GetRolloutKind']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['GetRolloutKind']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027\x125/v1beta1/{name=projects/*/locations/*/rolloutKinds/*}'
    _globals['_SAASROLLOUTS'].methods_by_name['CreateRolloutKind']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['CreateRolloutKind']._serialized_options = b'\xdaA#parent,rollout_kind,rollout_kind_id\x82\xd3\xe4\x93\x02E"5/v1beta1/{parent=projects/*/locations/*}/rolloutKinds:\x0crollout_kind'
    _globals['_SAASROLLOUTS'].methods_by_name['UpdateRolloutKind']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['UpdateRolloutKind']._serialized_options = b'\xdaA\x18rollout_kind,update_mask\x82\xd3\xe4\x93\x02R2B/v1beta1/{rollout_kind.name=projects/*/locations/*/rolloutKinds/*}:\x0crollout_kind'
    _globals['_SAASROLLOUTS'].methods_by_name['DeleteRolloutKind']._loaded_options = None
    _globals['_SAASROLLOUTS'].methods_by_name['DeleteRolloutKind']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x027*5/v1beta1/{name=projects/*/locations/*/rolloutKinds/*}'
    _globals['_LISTROLLOUTSREQUEST']._serialized_start = 382
    _globals['_LISTROLLOUTSREQUEST']._serialized_end = 545
    _globals['_LISTROLLOUTSRESPONSE']._serialized_start = 548
    _globals['_LISTROLLOUTSRESPONSE']._serialized_end = 697
    _globals['_GETROLLOUTREQUEST']._serialized_start = 699
    _globals['_GETROLLOUTREQUEST']._serialized_end = 781
    _globals['_CREATEROLLOUTREQUEST']._serialized_start = 784
    _globals['_CREATEROLLOUTREQUEST']._serialized_end = 1025
    _globals['_UPDATEROLLOUTREQUEST']._serialized_start = 1028
    _globals['_UPDATEROLLOUTREQUEST']._serialized_end = 1228
    _globals['_DELETEROLLOUTREQUEST']._serialized_start = 1231
    _globals['_DELETEROLLOUTREQUEST']._serialized_end = 1376
    _globals['_LISTROLLOUTKINDSREQUEST']._serialized_start = 1379
    _globals['_LISTROLLOUTKINDSREQUEST']._serialized_end = 1550
    _globals['_LISTROLLOUTKINDSRESPONSE']._serialized_start = 1553
    _globals['_LISTROLLOUTKINDSRESPONSE']._serialized_end = 1715
    _globals['_GETROLLOUTKINDREQUEST']._serialized_start = 1717
    _globals['_GETROLLOUTKINDREQUEST']._serialized_end = 1807
    _globals['_CREATEROLLOUTKINDREQUEST']._serialized_start = 1810
    _globals['_CREATEROLLOUTKINDREQUEST']._serialized_end = 2073
    _globals['_UPDATEROLLOUTKINDREQUEST']._serialized_start = 2076
    _globals['_UPDATEROLLOUTKINDREQUEST']._serialized_end = 2289
    _globals['_DELETEROLLOUTKINDREQUEST']._serialized_start = 2292
    _globals['_DELETEROLLOUTKINDREQUEST']._serialized_end = 2445
    _globals['_SAASROLLOUTS']._serialized_start = 2448
    _globals['_SAASROLLOUTS']._serialized_end = 4888