"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/asset/v1/assets.proto')
_sym_db = _symbol_database.Default()
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.asset.v1 import asset_enrichment_resourceowners_pb2 as google_dot_cloud_dot_asset_dot_v1_dot_asset__enrichment__resourceowners__pb2
from .....google.cloud.orgpolicy.v1 import orgpolicy_pb2 as google_dot_cloud_dot_orgpolicy_dot_v1_dot_orgpolicy__pb2
from .....google.cloud.osconfig.v1 import inventory_pb2 as google_dot_cloud_dot_osconfig_dot_v1_dot_inventory__pb2
from .....google.iam.v1 import policy_pb2 as google_dot_iam_dot_v1_dot_policy__pb2
from .....google.identity.accesscontextmanager.v1 import access_level_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__level__pb2
from .....google.identity.accesscontextmanager.v1 import access_policy_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_access__policy__pb2
from .....google.identity.accesscontextmanager.v1 import service_perimeter_pb2 as google_dot_identity_dot_accesscontextmanager_dot_v1_dot_service__perimeter__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n"google/cloud/asset/v1/assets.proto\x12\x15google.cloud.asset.v1\x1a\x19google/api/resource.proto\x1a;google/cloud/asset/v1/asset_enrichment_resourceowners.proto\x1a)google/cloud/orgpolicy/v1/orgpolicy.proto\x1a(google/cloud/osconfig/v1/inventory.proto\x1a\x1agoogle/iam/v1/policy.proto\x1a:google/identity/accesscontextmanager/v1/access_level.proto\x1a;google/identity/accesscontextmanager/v1/access_policy.proto\x1a?google/identity/accesscontextmanager/v1/service_perimeter.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\xf5\x02\n\rTemporalAsset\x121\n\x06window\x18\x01 \x01(\x0b2!.google.cloud.asset.v1.TimeWindow\x12\x0f\n\x07deleted\x18\x02 \x01(\x08\x12+\n\x05asset\x18\x03 \x01(\x0b2\x1c.google.cloud.asset.v1.Asset\x12O\n\x11prior_asset_state\x18\x04 \x01(\x0e24.google.cloud.asset.v1.TemporalAsset.PriorAssetState\x121\n\x0bprior_asset\x18\x05 \x01(\x0b2\x1c.google.cloud.asset.v1.Asset"o\n\x0fPriorAssetState\x12!\n\x1dPRIOR_ASSET_STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07PRESENT\x10\x01\x12\x0b\n\x07INVALID\x10\x02\x12\x12\n\x0eDOES_NOT_EXIST\x10\x03\x12\x0b\n\x07DELETED\x10\x04"j\n\nTimeWindow\x12.\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12,\n\x08end_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp"e\n\x0fAssetEnrichment\x12@\n\x0fresource_owners\x18\x07 \x01(\x0b2%.google.cloud.asset.v1.ResourceOwnersH\x00B\x10\n\x0eEnrichmentData"\xf3\x05\n\x05Asset\x12/\n\x0bupdate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x121\n\x08resource\x18\x03 \x01(\x0b2\x1f.google.cloud.asset.v1.Resource\x12)\n\niam_policy\x18\x04 \x01(\x0b2\x15.google.iam.v1.Policy\x125\n\norg_policy\x18\x06 \x03(\x0b2!.google.cloud.orgpolicy.v1.Policy\x12N\n\raccess_policy\x18\x07 \x01(\x0b25.google.identity.accesscontextmanager.v1.AccessPolicyH\x00\x12L\n\x0caccess_level\x18\x08 \x01(\x0b24.google.identity.accesscontextmanager.v1.AccessLevelH\x00\x12V\n\x11service_perimeter\x18\t \x01(\x0b29.google.identity.accesscontextmanager.v1.ServicePerimeterH\x00\x129\n\x0cos_inventory\x18\x0c \x01(\x0b2#.google.cloud.osconfig.v1.Inventory\x12@\n\x0erelated_assets\x18\r \x01(\x0b2$.google.cloud.asset.v1.RelatedAssetsB\x02\x18\x01\x12:\n\rrelated_asset\x18\x0f \x01(\x0b2#.google.cloud.asset.v1.RelatedAsset\x12\x11\n\tancestors\x18\n \x03(\t:\'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*B\x17\n\x15access_context_policy"\xb2\x01\n\x08Resource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x1e\n\x16discovery_document_uri\x18\x02 \x01(\t\x12\x16\n\x0ediscovery_name\x18\x03 \x01(\t\x12\x14\n\x0cresource_url\x18\x04 \x01(\t\x12\x0e\n\x06parent\x18\x05 \x01(\t\x12%\n\x04data\x18\x06 \x01(\x0b2\x17.google.protobuf.Struct\x12\x10\n\x08location\x18\x08 \x01(\t"\x98\x01\n\rRelatedAssets\x12N\n\x17relationship_attributes\x18\x01 \x01(\x0b2-.google.cloud.asset.v1.RelationshipAttributes\x123\n\x06assets\x18\x02 \x03(\x0b2#.google.cloud.asset.v1.RelatedAsset:\x02\x18\x01"v\n\x16RelationshipAttributes\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x1c\n\x14source_resource_type\x18\x01 \x01(\t\x12\x1c\n\x14target_resource_type\x18\x02 \x01(\t\x12\x0e\n\x06action\x18\x03 \x01(\t:\x02\x18\x01"\x85\x01\n\x0cRelatedAsset\x123\n\x05asset\x18\x01 \x01(\tB$\xfaA!\n\x1fcloudasset.googleapis.com/Asset\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x11\n\tancestors\x18\x03 \x03(\t\x12\x19\n\x11relationship_type\x18\x04 \x01(\t"\xa1\x01\n\x03Tag\x12\x14\n\x07tag_key\x18\x01 \x01(\tH\x00\x88\x01\x01\x12\x17\n\ntag_key_id\x18\x02 \x01(\tH\x01\x88\x01\x01\x12\x16\n\ttag_value\x18\x03 \x01(\tH\x02\x88\x01\x01\x12\x19\n\x0ctag_value_id\x18\x04 \x01(\tH\x03\x88\x01\x01B\n\n\x08_tag_keyB\r\n\x0b_tag_key_idB\x0c\n\n_tag_valueB\x0f\n\r_tag_value_id"\x7f\n\x13EffectiveTagDetails\x12\x1e\n\x11attached_resource\x18\x01 \x01(\tH\x00\x88\x01\x01\x122\n\x0eeffective_tags\x18\x02 \x03(\x0b2\x1a.google.cloud.asset.v1.TagB\x14\n\x12_attached_resource"\x97\n\n\x14ResourceSearchResult\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x02 \x01(\t\x12\x0f\n\x07project\x18\x03 \x01(\t\x12\x0f\n\x07folders\x18\x11 \x03(\t\x12\x14\n\x0corganization\x18\x12 \x01(\t\x12\x14\n\x0cdisplay_name\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12G\n\x06labels\x18\x07 \x03(\x0b27.google.cloud.asset.v1.ResourceSearchResult.LabelsEntry\x12\x14\n\x0cnetwork_tags\x18\x08 \x03(\t\x12\x13\n\x07kms_key\x18\n \x01(\tB\x02\x18\x01\x12\x10\n\x08kms_keys\x18\x1c \x03(\t\x12/\n\x0bcreate_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.Timestamp\x12\r\n\x05state\x18\r \x01(\t\x126\n\x15additional_attributes\x18\t \x01(\x0b2\x17.google.protobuf.Struct\x12!\n\x19parent_full_resource_name\x18\x13 \x01(\t\x12E\n\x13versioned_resources\x18\x10 \x03(\x0b2(.google.cloud.asset.v1.VersionedResource\x12C\n\x12attached_resources\x18\x14 \x03(\x0b2\'.google.cloud.asset.v1.AttachedResource\x12U\n\rrelationships\x18\x15 \x03(\x0b2>.google.cloud.asset.v1.ResourceSearchResult.RelationshipsEntry\x12\x14\n\x08tag_keys\x18\x17 \x03(\tB\x02\x18\x01\x12\x16\n\ntag_values\x18\x19 \x03(\tB\x02\x18\x01\x12\x19\n\rtag_value_ids\x18\x1a \x03(\tB\x02\x18\x01\x12(\n\x04tags\x18\x1d \x03(\x0b2\x1a.google.cloud.asset.v1.Tag\x12B\n\x0eeffective_tags\x18\x1e \x03(\x0b2*.google.cloud.asset.v1.EffectiveTagDetails\x12;\n\x0benrichments\x18\x1f \x03(\x0b2&.google.cloud.asset.v1.AssetEnrichment\x12\x19\n\x11parent_asset_type\x18g \x01(\t\x12]\n\x12scc_security_marks\x18  \x03(\x0b2A.google.cloud.asset.v1.ResourceSearchResult.SccSecurityMarksEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a]\n\x12RelationshipsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x126\n\x05value\x18\x02 \x01(\x0b2\'.google.cloud.asset.v1.RelatedResources:\x028\x01\x1a7\n\x15SccSecurityMarksEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"O\n\x11VersionedResource\x12\x0f\n\x07version\x18\x01 \x01(\t\x12)\n\x08resource\x18\x02 \x01(\x0b2\x17.google.protobuf.Struct"m\n\x10AttachedResource\x12\x12\n\nasset_type\x18\x01 \x01(\t\x12E\n\x13versioned_resources\x18\x03 \x03(\x0b2(.google.cloud.asset.v1.VersionedResource"U\n\x10RelatedResources\x12A\n\x11related_resources\x18\x01 \x03(\x0b2&.google.cloud.asset.v1.RelatedResource"A\n\x0fRelatedResource\x12\x12\n\nasset_type\x18\x01 \x01(\t\x12\x1a\n\x12full_resource_name\x18\x02 \x01(\t"\x8f\x04\n\x15IamPolicySearchResult\x12\x10\n\x08resource\x18\x01 \x01(\t\x12\x12\n\nasset_type\x18\x05 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0f\n\x07folders\x18\x06 \x03(\t\x12\x14\n\x0corganization\x18\x07 \x01(\t\x12%\n\x06policy\x18\x03 \x01(\x0b2\x15.google.iam.v1.Policy\x12M\n\x0bexplanation\x18\x04 \x01(\x0b28.google.cloud.asset.v1.IamPolicySearchResult.Explanation\x1a\xa1\x02\n\x0bExplanation\x12m\n\x13matched_permissions\x18\x01 \x03(\x0b2P.google.cloud.asset.v1.IamPolicySearchResult.Explanation.MatchedPermissionsEntry\x1a"\n\x0bPermissions\x12\x13\n\x0bpermissions\x18\x01 \x03(\t\x1a\x7f\n\x17MatchedPermissionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12S\n\x05value\x18\x02 \x01(\x0b2D.google.cloud.asset.v1.IamPolicySearchResult.Explanation.Permissions:\x028\x01"G\n\x16IamPolicyAnalysisState\x12\x1e\n\x04code\x18\x01 \x01(\x0e2\x10.google.rpc.Code\x12\r\n\x05cause\x18\x02 \x01(\t"\xc6\x01\n\x13ConditionEvaluation\x12T\n\x10evaluation_value\x18\x01 \x01(\x0e2:.google.cloud.asset.v1.ConditionEvaluation.EvaluationValue"Y\n\x0fEvaluationValue\x12 \n\x1cEVALUATION_VALUE_UNSPECIFIED\x10\x00\x12\x08\n\x04TRUE\x10\x01\x12\t\n\x05FALSE\x10\x02\x12\x0f\n\x0bCONDITIONAL\x10\x03"\xab\t\n\x17IamPolicyAnalysisResult\x12#\n\x1battached_resource_full_name\x18\x01 \x01(\t\x12+\n\x0biam_binding\x18\x02 \x01(\x0b2\x16.google.iam.v1.Binding\x12^\n\x14access_control_lists\x18\x03 \x03(\x0b2@.google.cloud.asset.v1.IamPolicyAnalysisResult.AccessControlList\x12R\n\ridentity_list\x18\x04 \x01(\x0b2;.google.cloud.asset.v1.IamPolicyAnalysisResult.IdentityList\x12\x16\n\x0efully_explored\x18\x05 \x01(\x08\x1am\n\x08Resource\x12\x1a\n\x12full_resource_name\x18\x01 \x01(\t\x12E\n\x0eanalysis_state\x18\x02 \x01(\x0b2-.google.cloud.asset.v1.IamPolicyAnalysisState\x1a\x85\x01\n\x06Access\x12\x0e\n\x04role\x18\x01 \x01(\tH\x00\x12\x14\n\npermission\x18\x02 \x01(\tH\x00\x12E\n\x0eanalysis_state\x18\x03 \x01(\x0b2-.google.cloud.asset.v1.IamPolicyAnalysisStateB\x0e\n\x0coneof_access\x1a_\n\x08Identity\x12\x0c\n\x04name\x18\x01 \x01(\t\x12E\n\x0eanalysis_state\x18\x02 \x01(\x0b2-.google.cloud.asset.v1.IamPolicyAnalysisState\x1a0\n\x04Edge\x12\x13\n\x0bsource_node\x18\x01 \x01(\t\x12\x13\n\x0btarget_node\x18\x02 \x01(\t\x1a\xbf\x02\n\x11AccessControlList\x12J\n\tresources\x18\x01 \x03(\x0b27.google.cloud.asset.v1.IamPolicyAnalysisResult.Resource\x12G\n\x08accesses\x18\x02 \x03(\x0b25.google.cloud.asset.v1.IamPolicyAnalysisResult.Access\x12K\n\x0eresource_edges\x18\x03 \x03(\x0b23.google.cloud.asset.v1.IamPolicyAnalysisResult.Edge\x12H\n\x14condition_evaluation\x18\x04 \x01(\x0b2*.google.cloud.asset.v1.ConditionEvaluation\x1a\xa5\x01\n\x0cIdentityList\x12K\n\nidentities\x18\x01 \x03(\x0b27.google.cloud.asset.v1.IamPolicyAnalysisResult.Identity\x12H\n\x0bgroup_edges\x18\x02 \x03(\x0b23.google.cloud.asset.v1.IamPolicyAnalysisResult.EdgeB\x8a\x01\n\x19com.google.cloud.asset.v1B\nAssetProtoP\x01Z/cloud.google.com/go/asset/apiv1/assetpb;assetpb\xaa\x02\x15Google.Cloud.Asset.V1\xca\x02\x15Google\\Cloud\\Asset\\V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.asset.v1.assets_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x19com.google.cloud.asset.v1B\nAssetProtoP\x01Z/cloud.google.com/go/asset/apiv1/assetpb;assetpb\xaa\x02\x15Google.Cloud.Asset.V1\xca\x02\x15Google\\Cloud\\Asset\\V1'
    _globals['_ASSET'].fields_by_name['related_assets']._loaded_options = None
    _globals['_ASSET'].fields_by_name['related_assets']._serialized_options = b'\x18\x01'
    _globals['_ASSET']._loaded_options = None
    _globals['_ASSET']._serialized_options = b'\xeaA$\n\x1fcloudasset.googleapis.com/Asset\x12\x01*'
    _globals['_RELATEDASSETS']._loaded_options = None
    _globals['_RELATEDASSETS']._serialized_options = b'\x18\x01'
    _globals['_RELATIONSHIPATTRIBUTES']._loaded_options = None
    _globals['_RELATIONSHIPATTRIBUTES']._serialized_options = b'\x18\x01'
    _globals['_RELATEDASSET'].fields_by_name['asset']._loaded_options = None
    _globals['_RELATEDASSET'].fields_by_name['asset']._serialized_options = b'\xfaA!\n\x1fcloudasset.googleapis.com/Asset'
    _globals['_RESOURCESEARCHRESULT_LABELSENTRY']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCESEARCHRESULT_RELATIONSHIPSENTRY']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT_RELATIONSHIPSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCESEARCHRESULT_SCCSECURITYMARKSENTRY']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT_SCCSECURITYMARKSENTRY']._serialized_options = b'8\x01'
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['kms_key']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['kms_key']._serialized_options = b'\x18\x01'
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_keys']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_keys']._serialized_options = b'\x18\x01'
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_values']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_values']._serialized_options = b'\x18\x01'
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_value_ids']._loaded_options = None
    _globals['_RESOURCESEARCHRESULT'].fields_by_name['tag_value_ids']._serialized_options = b'\x18\x01'
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY']._loaded_options = None
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY']._serialized_options = b'8\x01'
    _globals['_TEMPORALASSET']._serialized_start = 535
    _globals['_TEMPORALASSET']._serialized_end = 908
    _globals['_TEMPORALASSET_PRIORASSETSTATE']._serialized_start = 797
    _globals['_TEMPORALASSET_PRIORASSETSTATE']._serialized_end = 908
    _globals['_TIMEWINDOW']._serialized_start = 910
    _globals['_TIMEWINDOW']._serialized_end = 1016
    _globals['_ASSETENRICHMENT']._serialized_start = 1018
    _globals['_ASSETENRICHMENT']._serialized_end = 1119
    _globals['_ASSET']._serialized_start = 1122
    _globals['_ASSET']._serialized_end = 1877
    _globals['_RESOURCE']._serialized_start = 1880
    _globals['_RESOURCE']._serialized_end = 2058
    _globals['_RELATEDASSETS']._serialized_start = 2061
    _globals['_RELATEDASSETS']._serialized_end = 2213
    _globals['_RELATIONSHIPATTRIBUTES']._serialized_start = 2215
    _globals['_RELATIONSHIPATTRIBUTES']._serialized_end = 2333
    _globals['_RELATEDASSET']._serialized_start = 2336
    _globals['_RELATEDASSET']._serialized_end = 2469
    _globals['_TAG']._serialized_start = 2472
    _globals['_TAG']._serialized_end = 2633
    _globals['_EFFECTIVETAGDETAILS']._serialized_start = 2635
    _globals['_EFFECTIVETAGDETAILS']._serialized_end = 2762
    _globals['_RESOURCESEARCHRESULT']._serialized_start = 2765
    _globals['_RESOURCESEARCHRESULT']._serialized_end = 4068
    _globals['_RESOURCESEARCHRESULT_LABELSENTRY']._serialized_start = 3871
    _globals['_RESOURCESEARCHRESULT_LABELSENTRY']._serialized_end = 3916
    _globals['_RESOURCESEARCHRESULT_RELATIONSHIPSENTRY']._serialized_start = 3918
    _globals['_RESOURCESEARCHRESULT_RELATIONSHIPSENTRY']._serialized_end = 4011
    _globals['_RESOURCESEARCHRESULT_SCCSECURITYMARKSENTRY']._serialized_start = 4013
    _globals['_RESOURCESEARCHRESULT_SCCSECURITYMARKSENTRY']._serialized_end = 4068
    _globals['_VERSIONEDRESOURCE']._serialized_start = 4070
    _globals['_VERSIONEDRESOURCE']._serialized_end = 4149
    _globals['_ATTACHEDRESOURCE']._serialized_start = 4151
    _globals['_ATTACHEDRESOURCE']._serialized_end = 4260
    _globals['_RELATEDRESOURCES']._serialized_start = 4262
    _globals['_RELATEDRESOURCES']._serialized_end = 4347
    _globals['_RELATEDRESOURCE']._serialized_start = 4349
    _globals['_RELATEDRESOURCE']._serialized_end = 4414
    _globals['_IAMPOLICYSEARCHRESULT']._serialized_start = 4417
    _globals['_IAMPOLICYSEARCHRESULT']._serialized_end = 4944
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION']._serialized_start = 4655
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION']._serialized_end = 4944
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_PERMISSIONS']._serialized_start = 4781
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_PERMISSIONS']._serialized_end = 4815
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY']._serialized_start = 4817
    _globals['_IAMPOLICYSEARCHRESULT_EXPLANATION_MATCHEDPERMISSIONSENTRY']._serialized_end = 4944
    _globals['_IAMPOLICYANALYSISSTATE']._serialized_start = 4946
    _globals['_IAMPOLICYANALYSISSTATE']._serialized_end = 5017
    _globals['_CONDITIONEVALUATION']._serialized_start = 5020
    _globals['_CONDITIONEVALUATION']._serialized_end = 5218
    _globals['_CONDITIONEVALUATION_EVALUATIONVALUE']._serialized_start = 5129
    _globals['_CONDITIONEVALUATION_EVALUATIONVALUE']._serialized_end = 5218
    _globals['_IAMPOLICYANALYSISRESULT']._serialized_start = 5221
    _globals['_IAMPOLICYANALYSISRESULT']._serialized_end = 6416
    _globals['_IAMPOLICYANALYSISRESULT_RESOURCE']._serialized_start = 5534
    _globals['_IAMPOLICYANALYSISRESULT_RESOURCE']._serialized_end = 5643
    _globals['_IAMPOLICYANALYSISRESULT_ACCESS']._serialized_start = 5646
    _globals['_IAMPOLICYANALYSISRESULT_ACCESS']._serialized_end = 5779
    _globals['_IAMPOLICYANALYSISRESULT_IDENTITY']._serialized_start = 5781
    _globals['_IAMPOLICYANALYSISRESULT_IDENTITY']._serialized_end = 5876
    _globals['_IAMPOLICYANALYSISRESULT_EDGE']._serialized_start = 5878
    _globals['_IAMPOLICYANALYSISRESULT_EDGE']._serialized_end = 5926
    _globals['_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST']._serialized_start = 5929
    _globals['_IAMPOLICYANALYSISRESULT_ACCESSCONTROLLIST']._serialized_end = 6248
    _globals['_IAMPOLICYANALYSISRESULT_IDENTITYLIST']._serialized_start = 6251
    _globals['_IAMPOLICYANALYSISRESULT_IDENTITYLIST']._serialized_end = 6416