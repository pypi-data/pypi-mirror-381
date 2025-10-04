"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/policysimulator/v1/orgpolicy.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.orgpolicy.v2 import constraint_pb2 as google_dot_cloud_dot_orgpolicy_dot_v2_dot_constraint__pb2
from .....google.cloud.orgpolicy.v2 import orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v2_dot_orgpolicy__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n/google/cloud/policysimulator/v1/orgpolicy.proto\x12\x1fgoogle.cloud.policysimulator.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a*google/cloud/orgpolicy/v2/constraint.proto\x1a)google/cloud/orgpolicy/v2/orgpolicy.proto\x1a#google/longrunning/operations.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xbd\x06\n\x1aOrgPolicyViolationsPreview\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12A\n\x05state\x18\x02 \x01(\x0e2-.google.cloud.policysimulator.v1.PreviewStateB\x03\xe0A\x03\x12G\n\x07overlay\x18\x03 \x01(\x0b21.google.cloud.policysimulator.v1.OrgPolicyOverlayB\x03\xe0A\x02\x12\x1d\n\x10violations_count\x18\x04 \x01(\x05B\x03\xe0A\x03\x12h\n\x0fresource_counts\x18\x05 \x01(\x0b2J.google.cloud.policysimulator.v1.OrgPolicyViolationsPreview.ResourceCountsB\x03\xe0A\x03\x12M\n\x12custom_constraints\x18\x06 \x03(\tB1\xe0A\x03\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint\x124\n\x0bcreate_time\x18\x07 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x1a\x87\x01\n\x0eResourceCounts\x12\x14\n\x07scanned\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x19\n\x0cnoncompliant\x18\x02 \x01(\x05B\x03\xe0A\x03\x12\x16\n\tcompliant\x18\x03 \x01(\x05B\x03\xe0A\x03\x12\x17\n\nunenforced\x18\x04 \x01(\x05B\x03\xe0A\x03\x12\x13\n\x06errors\x18\x05 \x01(\x05B\x03\xe0A\x03:\xe7\x01\xeaA\xe3\x01\n9policysimulator.googleapis.com/OrgPolicyViolationsPreview\x12morganizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{org_policy_violations_preview}*\x1borgPolicyViolationsPreviews2\x1aorgPolicyViolationsPreview"\xcf\x03\n\x12OrgPolicyViolation\x12\x0c\n\x04name\x18\x01 \x01(\t\x12B\n\x08resource\x18\x02 \x01(\x0b20.google.cloud.policysimulator.v1.ResourceContext\x12F\n\x11custom_constraint\x18\x03 \x01(\x0b2+.google.cloud.orgpolicy.v2.CustomConstraint\x12!\n\x05error\x18\x04 \x01(\x0b2\x12.google.rpc.Status:\xfb\x01\xeaA\xf7\x01\n1policysimulator.googleapis.com/OrgPolicyViolation\x12\x98\x01organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{org_policy_violations_preview}/orgPolicyViolations/{org_policy_violation}*\x13orgPolicyViolations2\x12orgPolicyViolation"J\n\x0fResourceContext\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x11\n\tancestors\x18\x03 \x03(\t"\xcb\x03\n\x10OrgPolicyOverlay\x12V\n\x08policies\x18\x01 \x03(\x0b2?.google.cloud.policysimulator.v1.OrgPolicyOverlay.PolicyOverlayB\x03\xe0A\x01\x12j\n\x12custom_constraints\x18\x02 \x03(\x0b2I.google.cloud.policysimulator.v1.OrgPolicyOverlay.CustomConstraintOverlayB\x03\xe0A\x01\x1ac\n\rPolicyOverlay\x12\x1a\n\rpolicy_parent\x18\x01 \x01(\tB\x03\xe0A\x01\x126\n\x06policy\x18\x02 \x01(\x0b2!.google.cloud.orgpolicy.v2.PolicyB\x03\xe0A\x01\x1a\x8d\x01\n\x17CustomConstraintOverlay\x12%\n\x18custom_constraint_parent\x18\x01 \x01(\tB\x03\xe0A\x01\x12K\n\x11custom_constraint\x18\x02 \x01(\x0b2+.google.cloud.orgpolicy.v2.CustomConstraintB\x03\xe0A\x01"\xa7\x02\n1CreateOrgPolicyViolationsPreviewOperationMetadata\x120\n\x0crequest_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12.\n\nstart_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12A\n\x05state\x18\x03 \x01(\x0e2-.google.cloud.policysimulator.v1.PreviewStateB\x03\xe0A\x03\x12\x17\n\x0fresources_found\x18\x04 \x01(\x05\x12\x19\n\x11resources_scanned\x18\x05 \x01(\x05\x12\x19\n\x11resources_pending\x18\x06 \x01(\x05"\xac\x01\n&ListOrgPolicyViolationsPreviewsRequest\x12Q\n\x06parent\x18\x01 \x01(\tBA\xe0A\x02\xfaA;\x129policysimulator.googleapis.com/OrgPolicyViolationsPreview\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\xa7\x01\n\'ListOrgPolicyViolationsPreviewsResponse\x12c\n\x1eorg_policy_violations_previews\x18\x01 \x03(\x0b2;.google.cloud.policysimulator.v1.OrgPolicyViolationsPreview\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"w\n$GetOrgPolicyViolationsPreviewRequest\x12O\n\x04name\x18\x01 \x01(\tBA\xe0A\x02\xfaA;\n9policysimulator.googleapis.com/OrgPolicyViolationsPreview"\x94\x02\n\'CreateOrgPolicyViolationsPreviewRequest\x12Q\n\x06parent\x18\x01 \x01(\tBA\xe0A\x02\xfaA;\x129policysimulator.googleapis.com/OrgPolicyViolationsPreview\x12g\n\x1dorg_policy_violations_preview\x18\x02 \x01(\x0b2;.google.cloud.policysimulator.v1.OrgPolicyViolationsPreviewB\x03\xe0A\x02\x12-\n org_policy_violations_preview_id\x18\x03 \x01(\tB\x03\xe0A\x01"\x9c\x01\n\x1eListOrgPolicyViolationsRequest\x12I\n\x06parent\x18\x01 \x01(\tB9\xe0A\x02\xfaA3\x121policysimulator.googleapis.com/OrgPolicyViolation\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01"\x8e\x01\n\x1fListOrgPolicyViolationsResponse\x12R\n\x15org_policy_violations\x18\x01 \x03(\x0b23.google.cloud.policysimulator.v1.OrgPolicyViolation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x82\x01\n\x0cPreviewState\x12\x1d\n\x19PREVIEW_STATE_UNSPECIFIED\x10\x00\x12\x13\n\x0fPREVIEW_PENDING\x10\x01\x12\x13\n\x0fPREVIEW_RUNNING\x10\x02\x12\x15\n\x11PREVIEW_SUCCEEDED\x10\x03\x12\x12\n\x0ePREVIEW_FAILED\x10\x042\xa2\n\n!OrgPolicyViolationsPreviewService\x12\x8b\x02\n\x1fListOrgPolicyViolationsPreviews\x12G.google.cloud.policysimulator.v1.ListOrgPolicyViolationsPreviewsRequest\x1aH.google.cloud.policysimulator.v1.ListOrgPolicyViolationsPreviewsResponse"U\xdaA\x06parent\x82\xd3\xe4\x93\x02F\x12D/v1/{parent=organizations/*/locations/*}/orgPolicyViolationsPreviews\x12\xf8\x01\n\x1dGetOrgPolicyViolationsPreview\x12E.google.cloud.policysimulator.v1.GetOrgPolicyViolationsPreviewRequest\x1a;.google.cloud.policysimulator.v1.OrgPolicyViolationsPreview"S\xdaA\x04name\x82\xd3\xe4\x93\x02F\x12D/v1/{name=organizations/*/locations/*/orgPolicyViolationsPreviews/*}\x12\x93\x03\n CreateOrgPolicyViolationsPreview\x12H.google.cloud.policysimulator.v1.CreateOrgPolicyViolationsPreviewRequest\x1a\x1d.google.longrunning.Operation"\x85\x02\xcaAO\n\x1aOrgPolicyViolationsPreview\x121CreateOrgPolicyViolationsPreviewOperationMetadata\xdaAEparent,org_policy_violations_preview,org_policy_violations_preview_id\x82\xd3\xe4\x93\x02e"D/v1/{parent=organizations/*/locations/*}/orgPolicyViolationsPreviews:\x1dorg_policy_violations_preview\x12\x89\x02\n\x17ListOrgPolicyViolations\x12?.google.cloud.policysimulator.v1.ListOrgPolicyViolationsRequest\x1a@.google.cloud.policysimulator.v1.ListOrgPolicyViolationsResponse"k\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x12Z/v1/{parent=organizations/*/locations/*/orgPolicyViolationsPreviews/*}/orgPolicyViolations\x1aR\xcaA\x1epolicysimulator.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x9b\x03\n#com.google.cloud.policysimulator.v1B\x0eOrgpolicyProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1\xeaA\\\n\'iam.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}\xeaAJ\n!iam.googleapis.com/FolderLocation\x12%folders/{folder}/locations/{location}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.policysimulator.v1.orgpolicy_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.policysimulator.v1B\x0eOrgpolicyProtoP\x01ZMcloud.google.com/go/policysimulator/apiv1/policysimulatorpb;policysimulatorpb\xaa\x02\x1fGoogle.Cloud.PolicySimulator.V1\xca\x02\x1fGoogle\\Cloud\\PolicySimulator\\V1\xea\x02"Google::Cloud::PolicySimulator::V1\xeaA\\\n\'iam.googleapis.com/OrganizationLocation\x121organizations/{organization}/locations/{location}\xeaAJ\n!iam.googleapis.com/FolderLocation\x12%folders/{folder}/locations/{location}'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['scanned']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['scanned']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['noncompliant']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['noncompliant']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['compliant']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['compliant']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['unenforced']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['unenforced']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['errors']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS'].fields_by_name['errors']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['name']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['state']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['overlay']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['overlay']._serialized_options = b'\xe0A\x02'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['violations_count']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['violations_count']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['resource_counts']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['resource_counts']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['custom_constraints']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['custom_constraints']._serialized_options = b'\xe0A\x03\xfaA+\n)orgpolicy.googleapis.com/CustomConstraint'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['create_time']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_ORGPOLICYVIOLATIONSPREVIEW']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEW']._serialized_options = b'\xeaA\xe3\x01\n9policysimulator.googleapis.com/OrgPolicyViolationsPreview\x12morganizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{org_policy_violations_preview}*\x1borgPolicyViolationsPreviews2\x1aorgPolicyViolationsPreview'
    _globals['_ORGPOLICYVIOLATION']._loaded_options = None
    _globals['_ORGPOLICYVIOLATION']._serialized_options = b'\xeaA\xf7\x01\n1policysimulator.googleapis.com/OrgPolicyViolation\x12\x98\x01organizations/{organization}/locations/{location}/orgPolicyViolationsPreviews/{org_policy_violations_preview}/orgPolicyViolations/{org_policy_violation}*\x13orgPolicyViolations2\x12orgPolicyViolation'
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY'].fields_by_name['policy_parent']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY'].fields_by_name['policy_parent']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY'].fields_by_name['policy']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY'].fields_by_name['policy']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY'].fields_by_name['custom_constraint_parent']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY'].fields_by_name['custom_constraint_parent']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY'].fields_by_name['custom_constraint']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY'].fields_by_name['custom_constraint']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYOVERLAY'].fields_by_name['policies']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY'].fields_by_name['policies']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYOVERLAY'].fields_by_name['custom_constraints']._loaded_options = None
    _globals['_ORGPOLICYOVERLAY'].fields_by_name['custom_constraints']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWOPERATIONMETADATA'].fields_by_name['state']._loaded_options = None
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWOPERATIONMETADATA'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA;\x129policysimulator.googleapis.com/OrgPolicyViolationsPreview'
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_GETORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA;\n9policysimulator.googleapis.com/OrgPolicyViolationsPreview'
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA;\x129policysimulator.googleapis.com/OrgPolicyViolationsPreview'
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['org_policy_violations_preview']._loaded_options = None
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['org_policy_violations_preview']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['org_policy_violations_preview_id']._loaded_options = None
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST'].fields_by_name['org_policy_violations_preview_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA3\x121policysimulator.googleapis.com/OrgPolicyViolation'
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE']._serialized_options = b'\xcaA\x1epolicysimulator.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['ListOrgPolicyViolationsPreviews']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['ListOrgPolicyViolationsPreviews']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02F\x12D/v1/{parent=organizations/*/locations/*}/orgPolicyViolationsPreviews'
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['GetOrgPolicyViolationsPreview']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['GetOrgPolicyViolationsPreview']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02F\x12D/v1/{name=organizations/*/locations/*/orgPolicyViolationsPreviews/*}'
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['CreateOrgPolicyViolationsPreview']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['CreateOrgPolicyViolationsPreview']._serialized_options = b'\xcaAO\n\x1aOrgPolicyViolationsPreview\x121CreateOrgPolicyViolationsPreviewOperationMetadata\xdaAEparent,org_policy_violations_preview,org_policy_violations_preview_id\x82\xd3\xe4\x93\x02e"D/v1/{parent=organizations/*/locations/*}/orgPolicyViolationsPreviews:\x1dorg_policy_violations_preview'
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['ListOrgPolicyViolations']._loaded_options = None
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE'].methods_by_name['ListOrgPolicyViolations']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02\\\x12Z/v1/{parent=organizations/*/locations/*/orgPolicyViolationsPreviews/*}/orgPolicyViolations'
    _globals['_PREVIEWSTATE']._serialized_start = 3565
    _globals['_PREVIEWSTATE']._serialized_end = 3695
    _globals['_ORGPOLICYVIOLATIONSPREVIEW']._serialized_start = 382
    _globals['_ORGPOLICYVIOLATIONSPREVIEW']._serialized_end = 1211
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS']._serialized_start = 842
    _globals['_ORGPOLICYVIOLATIONSPREVIEW_RESOURCECOUNTS']._serialized_end = 977
    _globals['_ORGPOLICYVIOLATION']._serialized_start = 1214
    _globals['_ORGPOLICYVIOLATION']._serialized_end = 1677
    _globals['_RESOURCECONTEXT']._serialized_start = 1679
    _globals['_RESOURCECONTEXT']._serialized_end = 1753
    _globals['_ORGPOLICYOVERLAY']._serialized_start = 1756
    _globals['_ORGPOLICYOVERLAY']._serialized_end = 2215
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY']._serialized_start = 1972
    _globals['_ORGPOLICYOVERLAY_POLICYOVERLAY']._serialized_end = 2071
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY']._serialized_start = 2074
    _globals['_ORGPOLICYOVERLAY_CUSTOMCONSTRAINTOVERLAY']._serialized_end = 2215
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWOPERATIONMETADATA']._serialized_start = 2218
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWOPERATIONMETADATA']._serialized_end = 2513
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST']._serialized_start = 2516
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSREQUEST']._serialized_end = 2688
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSRESPONSE']._serialized_start = 2691
    _globals['_LISTORGPOLICYVIOLATIONSPREVIEWSRESPONSE']._serialized_end = 2858
    _globals['_GETORGPOLICYVIOLATIONSPREVIEWREQUEST']._serialized_start = 2860
    _globals['_GETORGPOLICYVIOLATIONSPREVIEWREQUEST']._serialized_end = 2979
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST']._serialized_start = 2982
    _globals['_CREATEORGPOLICYVIOLATIONSPREVIEWREQUEST']._serialized_end = 3258
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST']._serialized_start = 3261
    _globals['_LISTORGPOLICYVIOLATIONSREQUEST']._serialized_end = 3417
    _globals['_LISTORGPOLICYVIOLATIONSRESPONSE']._serialized_start = 3420
    _globals['_LISTORGPOLICYVIOLATIONSRESPONSE']._serialized_end = 3562
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE']._serialized_start = 3698
    _globals['_ORGPOLICYVIOLATIONSPREVIEWSERVICE']._serialized_end = 5012