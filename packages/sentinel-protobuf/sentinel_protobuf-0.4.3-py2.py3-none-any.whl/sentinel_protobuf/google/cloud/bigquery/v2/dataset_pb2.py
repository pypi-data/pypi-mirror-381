"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/v2/dataset.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.bigquery.v2 import dataset_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_dataset__reference__pb2
from .....google.cloud.bigquery.v2 import encryption_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_encryption__config__pb2
from .....google.cloud.bigquery.v2 import external_catalog_dataset_options_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_external__catalog__dataset__options__pb2
from .....google.cloud.bigquery.v2 import external_dataset_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_external__dataset__reference__pb2
from .....google.cloud.bigquery.v2 import restriction_config_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_restriction__config__pb2
from .....google.cloud.bigquery.v2 import routine_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_routine__reference__pb2
from .....google.cloud.bigquery.v2 import table_reference_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__reference__pb2
from .....google.cloud.bigquery.v2 import table_schema_pb2 as google_dot_cloud_dot_bigquery_dot_v2_dot_table__schema__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from .....google.type import expr_pb2 as google_dot_type_dot_expr__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n&google/cloud/bigquery/v2/dataset.proto\x12\x18google.cloud.bigquery.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a0google/cloud/bigquery/v2/dataset_reference.proto\x1a0google/cloud/bigquery/v2/encryption_config.proto\x1a?google/cloud/bigquery/v2/external_catalog_dataset_options.proto\x1a9google/cloud/bigquery/v2/external_dataset_reference.proto\x1a1google/cloud/bigquery/v2/restriction_config.proto\x1a0google/cloud/bigquery/v2/routine_reference.proto\x1a.google/cloud/bigquery/v2/table_reference.proto\x1a+google/cloud/bigquery/v2/table_schema.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x16google/type/expr.proto"\xe4\x01\n\x12DatasetAccessEntry\x12;\n\x07dataset\x18\x01 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReference\x12M\n\x0ctarget_types\x18\x02 \x03(\x0e27.google.cloud.bigquery.v2.DatasetAccessEntry.TargetType"B\n\nTargetType\x12\x1b\n\x17TARGET_TYPE_UNSPECIFIED\x10\x00\x12\t\n\x05VIEWS\x10\x01\x12\x0c\n\x08ROUTINES\x10\x02"\xdf\x02\n\x06Access\x12\x0c\n\x04role\x18\x01 \x01(\t\x12\x15\n\ruser_by_email\x18\x02 \x01(\t\x12\x16\n\x0egroup_by_email\x18\x03 \x01(\t\x12\x0e\n\x06domain\x18\x04 \x01(\t\x12\x15\n\rspecial_group\x18\x05 \x01(\t\x12\x12\n\niam_member\x18\x07 \x01(\t\x126\n\x04view\x18\x06 \x01(\x0b2(.google.cloud.bigquery.v2.TableReference\x12;\n\x07routine\x18\x08 \x01(\x0b2*.google.cloud.bigquery.v2.RoutineReference\x12=\n\x07dataset\x18\t \x01(\x0b2,.google.cloud.bigquery.v2.DatasetAccessEntry\x12)\n\tcondition\x18\n \x01(\x0b2\x11.google.type.ExprB\x03\xe0A\x01"\xbc\x0f\n\x07Dataset\x12\x11\n\x04kind\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x0f\n\x02id\x18\x03 \x01(\tB\x03\xe0A\x03\x12\x16\n\tself_link\x18\x04 \x01(\tB\x03\xe0A\x03\x12J\n\x11dataset_reference\x18\x05 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReferenceB\x03\xe0A\x02\x128\n\rfriendly_name\x18\x06 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x126\n\x0bdescription\x18\x07 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12E\n\x1bdefault_table_expiration_ms\x18\x08 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x12D\n\x1fdefault_partition_expiration_ms\x18\x0e \x01(\x0b2\x1b.google.protobuf.Int64Value\x12=\n\x06labels\x18\t \x03(\x0b2-.google.cloud.bigquery.v2.Dataset.LabelsEntry\x125\n\x06access\x18\n \x03(\x0b2 .google.cloud.bigquery.v2.AccessB\x03\xe0A\x01\x12\x1a\n\rcreation_time\x18\x0b \x01(\x03B\x03\xe0A\x03\x12\x1f\n\x12last_modified_time\x18\x0c \x01(\x03B\x03\xe0A\x03\x12\x10\n\x08location\x18\r \x01(\t\x12[\n default_encryption_configuration\x18\x10 \x01(\x0b21.google.cloud.bigquery.v2.EncryptionConfiguration\x126\n\rsatisfies_pzs\x18\x11 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x126\n\rsatisfies_pzi\x18\x1f \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x03\x12\x11\n\x04type\x18\x12 \x01(\tB\x03\xe0A\x03\x12Q\n\x15linked_dataset_source\x18\x13 \x01(\x0b2-.google.cloud.bigquery.v2.LinkedDatasetSourceB\x03\xe0A\x01\x12U\n\x17linked_dataset_metadata\x18\x1d \x01(\x0b2/.google.cloud.bigquery.v2.LinkedDatasetMetadataB\x03\xe0A\x03\x12[\n\x1aexternal_dataset_reference\x18\x14 \x01(\x0b22.google.cloud.bigquery.v2.ExternalDatasetReferenceB\x03\xe0A\x01\x12f\n external_catalog_dataset_options\x18  \x01(\x0b27.google.cloud.bigquery.v2.ExternalCatalogDatasetOptionsB\x03\xe0A\x01\x12<\n\x13is_case_insensitive\x18\x15 \x01(\x0b2\x1a.google.protobuf.BoolValueB\x03\xe0A\x01\x12<\n\x11default_collation\x18\x16 \x01(\x0b2\x1c.google.protobuf.StringValueB\x03\xe0A\x01\x12[\n\x15default_rounding_mode\x18\x1a \x01(\x0e27.google.cloud.bigquery.v2.TableFieldSchema.RoundingModeB\x03\xe0A\x01\x12?\n\x15max_time_travel_hours\x18\x17 \x01(\x0b2\x1b.google.protobuf.Int64ValueB\x03\xe0A\x01\x125\n\x04tags\x18\x18 \x03(\x0b2 .google.cloud.bigquery.v2.GcpTagB\x05\x18\x01\xe0A\x03\x12Y\n\x15storage_billing_model\x18\x19 \x01(\x0e25.google.cloud.bigquery.v2.Dataset.StorageBillingModelB\x03\xe0A\x01\x12I\n\x0crestrictions\x18\x1b \x01(\x0b2+.google.cloud.bigquery.v2.RestrictionConfigB\x06\xe0A\x01\xe0A\x03\x12O\n\rresource_tags\x18\x1e \x03(\x0b23.google.cloud.bigquery.v2.Dataset.ResourceTagsEntryB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01\x1a3\n\x11ResourceTagsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"W\n\x13StorageBillingModel\x12%\n!STORAGE_BILLING_MODEL_UNSPECIFIED\x10\x00\x12\x0b\n\x07LOGICAL\x10\x01\x12\x0c\n\x08PHYSICAL\x10\x02"6\n\x06GcpTag\x12\x14\n\x07tag_key\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x16\n\ttag_value\x18\x02 \x01(\tB\x03\xe0A\x02"Y\n\x13LinkedDatasetSource\x12B\n\x0esource_dataset\x18\x01 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReference"\xae\x01\n\x15LinkedDatasetMetadata\x12R\n\nlink_state\x18\x01 \x01(\x0e29.google.cloud.bigquery.v2.LinkedDatasetMetadata.LinkStateB\x03\xe0A\x03"A\n\tLinkState\x12\x1a\n\x16LINK_STATE_UNSPECIFIED\x10\x00\x12\n\n\x06LINKED\x10\x01\x12\x0c\n\x08UNLINKED\x10\x02"\x8b\x02\n\x11GetDatasetRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12R\n\x0cdataset_view\x18\x03 \x01(\x0e27.google.cloud.bigquery.v2.GetDatasetRequest.DatasetViewB\x03\xe0A\x01\x12"\n\x15access_policy_version\x18\x04 \x01(\x05B\x03\xe0A\x01"L\n\x0bDatasetView\x12\x1c\n\x18DATASET_VIEW_UNSPECIFIED\x10\x00\x12\x0c\n\x08METADATA\x10\x01\x12\x07\n\x03ACL\x10\x02\x12\x08\n\x04FULL\x10\x03"\x8c\x01\n\x14InsertDatasetRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x127\n\x07dataset\x18\x02 \x01(\x0b2!.google.cloud.bigquery.v2.DatasetB\x03\xe0A\x02\x12"\n\x15access_policy_version\x18\x04 \x01(\x05B\x03\xe0A\x01"\xe9\x02\n\x1bUpdateOrPatchDatasetRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x127\n\x07dataset\x18\x03 \x01(\x0b2!.google.cloud.bigquery.v2.DatasetB\x03\xe0A\x02\x12Z\n\x0bupdate_mode\x18\x04 \x01(\x0e2@.google.cloud.bigquery.v2.UpdateOrPatchDatasetRequest.UpdateModeB\x03\xe0A\x01\x12"\n\x15access_policy_version\x18\x05 \x01(\x05B\x03\xe0A\x01"_\n\nUpdateMode\x12\x1b\n\x17UPDATE_MODE_UNSPECIFIED\x10\x00\x12\x13\n\x0fUPDATE_METADATA\x10\x01\x12\x0e\n\nUPDATE_ACL\x10\x02\x12\x0f\n\x0bUPDATE_FULL\x10\x03"a\n\x14DeleteDatasetRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x17\n\x0fdelete_contents\x18\x03 \x01(\x08"\x92\x01\n\x13ListDatasetsRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x121\n\x0bmax_results\x18\x02 \x01(\x0b2\x1c.google.protobuf.UInt32Value\x12\x12\n\npage_token\x18\x03 \x01(\t\x12\x0b\n\x03all\x18\x04 \x01(\x08\x12\x0e\n\x06filter\x18\x05 \x01(\t"\x90\x03\n\x11ListFormatDataset\x12\x0c\n\x04kind\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12E\n\x11dataset_reference\x18\x03 \x01(\x0b2*.google.cloud.bigquery.v2.DatasetReference\x12G\n\x06labels\x18\x04 \x03(\x0b27.google.cloud.bigquery.v2.ListFormatDataset.LabelsEntry\x123\n\rfriendly_name\x18\x05 \x01(\x0b2\x1c.google.protobuf.StringValue\x12\x10\n\x08location\x18\x06 \x01(\t\x12[\n\x1aexternal_dataset_reference\x18\x0b \x01(\x0b22.google.cloud.bigquery.v2.ExternalDatasetReferenceB\x03\xe0A\x03\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01"\xa0\x01\n\x0bDatasetList\x12\x11\n\x04kind\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x03\x12\x17\n\x0fnext_page_token\x18\x03 \x01(\t\x12=\n\x08datasets\x18\x04 \x03(\x0b2+.google.cloud.bigquery.v2.ListFormatDataset\x12\x13\n\x0bunreachable\x18\x05 \x03(\t"\x82\x01\n\x16UndeleteDatasetRequest\x12\x17\n\nproject_id\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x17\n\ndataset_id\x18\x02 \x01(\tB\x03\xe0A\x02\x126\n\rdeletion_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x012\xf9\n\n\x0eDatasetService\x12\xa2\x01\n\nGetDataset\x12+.google.cloud.bigquery.v2.GetDatasetRequest\x1a!.google.cloud.bigquery.v2.Dataset"D\x82\xd3\xe4\x93\x02>\x12</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}\x12\xa2\x01\n\rInsertDataset\x12..google.cloud.bigquery.v2.InsertDatasetRequest\x1a!.google.cloud.bigquery.v2.Dataset">\x82\xd3\xe4\x93\x028"-/bigquery/v2/projects/{project_id=*}/datasets:\x07dataset\x12\xb7\x01\n\x0cPatchDataset\x125.google.cloud.bigquery.v2.UpdateOrPatchDatasetRequest\x1a!.google.cloud.bigquery.v2.Dataset"M\x82\xd3\xe4\x93\x02G2</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:\x07dataset\x12\xb8\x01\n\rUpdateDataset\x125.google.cloud.bigquery.v2.UpdateOrPatchDatasetRequest\x1a!.google.cloud.bigquery.v2.Dataset"M\x82\xd3\xe4\x93\x02G\x1a</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:\x07dataset\x12\x9d\x01\n\rDeleteDataset\x12..google.cloud.bigquery.v2.DeleteDatasetRequest\x1a\x16.google.protobuf.Empty"D\x82\xd3\xe4\x93\x02>*</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}\x12\x9b\x01\n\x0cListDatasets\x12-.google.cloud.bigquery.v2.ListDatasetsRequest\x1a%.google.cloud.bigquery.v2.DatasetList"5\x82\xd3\xe4\x93\x02/\x12-/bigquery/v2/projects/{project_id=*}/datasets\x12\xb8\x01\n\x0fUndeleteDataset\x120.google.cloud.bigquery.v2.UndeleteDatasetRequest\x1a!.google.cloud.bigquery.v2.Dataset"P\x82\xd3\xe4\x93\x02J"E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:undelete:\x01*\x1a\xae\x01\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-onlyBi\n\x1ccom.google.cloud.bigquery.v2B\x0cDatasetProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.v2.dataset_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.bigquery.v2B\x0cDatasetProtoZ;cloud.google.com/go/bigquery/v2/apiv2/bigquerypb;bigquerypb'
    _globals['_ACCESS'].fields_by_name['condition']._loaded_options = None
    _globals['_ACCESS'].fields_by_name['condition']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET_LABELSENTRY']._loaded_options = None
    _globals['_DATASET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET_RESOURCETAGSENTRY']._loaded_options = None
    _globals['_DATASET_RESOURCETAGSENTRY']._serialized_options = b'8\x01'
    _globals['_DATASET'].fields_by_name['kind']._loaded_options = None
    _globals['_DATASET'].fields_by_name['kind']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['etag']._loaded_options = None
    _globals['_DATASET'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['id']._loaded_options = None
    _globals['_DATASET'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['self_link']._loaded_options = None
    _globals['_DATASET'].fields_by_name['self_link']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['dataset_reference']._loaded_options = None
    _globals['_DATASET'].fields_by_name['dataset_reference']._serialized_options = b'\xe0A\x02'
    _globals['_DATASET'].fields_by_name['friendly_name']._loaded_options = None
    _globals['_DATASET'].fields_by_name['friendly_name']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['description']._loaded_options = None
    _globals['_DATASET'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['default_table_expiration_ms']._loaded_options = None
    _globals['_DATASET'].fields_by_name['default_table_expiration_ms']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['access']._loaded_options = None
    _globals['_DATASET'].fields_by_name['access']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['creation_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['creation_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['last_modified_time']._loaded_options = None
    _globals['_DATASET'].fields_by_name['last_modified_time']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzs']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._loaded_options = None
    _globals['_DATASET'].fields_by_name['satisfies_pzi']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['type']._loaded_options = None
    _globals['_DATASET'].fields_by_name['type']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['linked_dataset_source']._loaded_options = None
    _globals['_DATASET'].fields_by_name['linked_dataset_source']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['linked_dataset_metadata']._loaded_options = None
    _globals['_DATASET'].fields_by_name['linked_dataset_metadata']._serialized_options = b'\xe0A\x03'
    _globals['_DATASET'].fields_by_name['external_dataset_reference']._loaded_options = None
    _globals['_DATASET'].fields_by_name['external_dataset_reference']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['external_catalog_dataset_options']._loaded_options = None
    _globals['_DATASET'].fields_by_name['external_catalog_dataset_options']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['is_case_insensitive']._loaded_options = None
    _globals['_DATASET'].fields_by_name['is_case_insensitive']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['default_collation']._loaded_options = None
    _globals['_DATASET'].fields_by_name['default_collation']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['default_rounding_mode']._loaded_options = None
    _globals['_DATASET'].fields_by_name['default_rounding_mode']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['max_time_travel_hours']._loaded_options = None
    _globals['_DATASET'].fields_by_name['max_time_travel_hours']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['tags']._loaded_options = None
    _globals['_DATASET'].fields_by_name['tags']._serialized_options = b'\x18\x01\xe0A\x03'
    _globals['_DATASET'].fields_by_name['storage_billing_model']._loaded_options = None
    _globals['_DATASET'].fields_by_name['storage_billing_model']._serialized_options = b'\xe0A\x01'
    _globals['_DATASET'].fields_by_name['restrictions']._loaded_options = None
    _globals['_DATASET'].fields_by_name['restrictions']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_DATASET'].fields_by_name['resource_tags']._loaded_options = None
    _globals['_DATASET'].fields_by_name['resource_tags']._serialized_options = b'\xe0A\x01'
    _globals['_GCPTAG'].fields_by_name['tag_key']._loaded_options = None
    _globals['_GCPTAG'].fields_by_name['tag_key']._serialized_options = b'\xe0A\x02'
    _globals['_GCPTAG'].fields_by_name['tag_value']._loaded_options = None
    _globals['_GCPTAG'].fields_by_name['tag_value']._serialized_options = b'\xe0A\x02'
    _globals['_LINKEDDATASETMETADATA'].fields_by_name['link_state']._loaded_options = None
    _globals['_LINKEDDATASETMETADATA'].fields_by_name['link_state']._serialized_options = b'\xe0A\x03'
    _globals['_GETDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_GETDATASETREQUEST'].fields_by_name['dataset_view']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['dataset_view']._serialized_options = b'\xe0A\x01'
    _globals['_GETDATASETREQUEST'].fields_by_name['access_policy_version']._loaded_options = None
    _globals['_GETDATASETREQUEST'].fields_by_name['access_policy_version']._serialized_options = b'\xe0A\x01'
    _globals['_INSERTDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_INSERTDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_INSERTDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_INSERTDATASETREQUEST'].fields_by_name['access_policy_version']._loaded_options = None
    _globals['_INSERTDATASETREQUEST'].fields_by_name['access_policy_version']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['dataset']._loaded_options = None
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['dataset']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['update_mode']._loaded_options = None
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['update_mode']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['access_policy_version']._loaded_options = None
    _globals['_UPDATEORPATCHDATASETREQUEST'].fields_by_name['access_policy_version']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_DELETEDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTDATASETSREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_LISTDATASETSREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_LISTFORMATDATASET_LABELSENTRY']._loaded_options = None
    _globals['_LISTFORMATDATASET_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_LISTFORMATDATASET'].fields_by_name['external_dataset_reference']._loaded_options = None
    _globals['_LISTFORMATDATASET'].fields_by_name['external_dataset_reference']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETLIST'].fields_by_name['kind']._loaded_options = None
    _globals['_DATASETLIST'].fields_by_name['kind']._serialized_options = b'\xe0A\x03'
    _globals['_DATASETLIST'].fields_by_name['etag']._loaded_options = None
    _globals['_DATASETLIST'].fields_by_name['etag']._serialized_options = b'\xe0A\x03'
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['project_id']._loaded_options = None
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['project_id']._serialized_options = b'\xe0A\x02'
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['dataset_id']._loaded_options = None
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['dataset_id']._serialized_options = b'\xe0A\x02'
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['deletion_time']._loaded_options = None
    _globals['_UNDELETEDATASETREQUEST'].fields_by_name['deletion_time']._serialized_options = b'\xe0A\x01'
    _globals['_DATASETSERVICE']._loaded_options = None
    _globals['_DATASETSERVICE']._serialized_options = b'\xcaA\x17bigquery.googleapis.com\xd2A\x90\x01https://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform,https://www.googleapis.com/auth/cloud-platform.read-only'
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['GetDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02>\x12</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}'
    _globals['_DATASETSERVICE'].methods_by_name['InsertDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['InsertDataset']._serialized_options = b'\x82\xd3\xe4\x93\x028"-/bigquery/v2/projects/{project_id=*}/datasets:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['PatchDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['PatchDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02G2</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UpdateDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02G\x1a</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:\x07dataset'
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['DeleteDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02>*</bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}'
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['ListDatasets']._serialized_options = b'\x82\xd3\xe4\x93\x02/\x12-/bigquery/v2/projects/{project_id=*}/datasets'
    _globals['_DATASETSERVICE'].methods_by_name['UndeleteDataset']._loaded_options = None
    _globals['_DATASETSERVICE'].methods_by_name['UndeleteDataset']._serialized_options = b'\x82\xd3\xe4\x93\x02J"E/bigquery/v2/projects/{project_id=*}/datasets/{dataset_id=*}:undelete:\x01*'
    _globals['_DATASETACCESSENTRY']._serialized_start = 693
    _globals['_DATASETACCESSENTRY']._serialized_end = 921
    _globals['_DATASETACCESSENTRY_TARGETTYPE']._serialized_start = 855
    _globals['_DATASETACCESSENTRY_TARGETTYPE']._serialized_end = 921
    _globals['_ACCESS']._serialized_start = 924
    _globals['_ACCESS']._serialized_end = 1275
    _globals['_DATASET']._serialized_start = 1278
    _globals['_DATASET']._serialized_end = 3258
    _globals['_DATASET_LABELSENTRY']._serialized_start = 3071
    _globals['_DATASET_LABELSENTRY']._serialized_end = 3116
    _globals['_DATASET_RESOURCETAGSENTRY']._serialized_start = 3118
    _globals['_DATASET_RESOURCETAGSENTRY']._serialized_end = 3169
    _globals['_DATASET_STORAGEBILLINGMODEL']._serialized_start = 3171
    _globals['_DATASET_STORAGEBILLINGMODEL']._serialized_end = 3258
    _globals['_GCPTAG']._serialized_start = 3260
    _globals['_GCPTAG']._serialized_end = 3314
    _globals['_LINKEDDATASETSOURCE']._serialized_start = 3316
    _globals['_LINKEDDATASETSOURCE']._serialized_end = 3405
    _globals['_LINKEDDATASETMETADATA']._serialized_start = 3408
    _globals['_LINKEDDATASETMETADATA']._serialized_end = 3582
    _globals['_LINKEDDATASETMETADATA_LINKSTATE']._serialized_start = 3517
    _globals['_LINKEDDATASETMETADATA_LINKSTATE']._serialized_end = 3582
    _globals['_GETDATASETREQUEST']._serialized_start = 3585
    _globals['_GETDATASETREQUEST']._serialized_end = 3852
    _globals['_GETDATASETREQUEST_DATASETVIEW']._serialized_start = 3776
    _globals['_GETDATASETREQUEST_DATASETVIEW']._serialized_end = 3852
    _globals['_INSERTDATASETREQUEST']._serialized_start = 3855
    _globals['_INSERTDATASETREQUEST']._serialized_end = 3995
    _globals['_UPDATEORPATCHDATASETREQUEST']._serialized_start = 3998
    _globals['_UPDATEORPATCHDATASETREQUEST']._serialized_end = 4359
    _globals['_UPDATEORPATCHDATASETREQUEST_UPDATEMODE']._serialized_start = 4264
    _globals['_UPDATEORPATCHDATASETREQUEST_UPDATEMODE']._serialized_end = 4359
    _globals['_DELETEDATASETREQUEST']._serialized_start = 4361
    _globals['_DELETEDATASETREQUEST']._serialized_end = 4458
    _globals['_LISTDATASETSREQUEST']._serialized_start = 4461
    _globals['_LISTDATASETSREQUEST']._serialized_end = 4607
    _globals['_LISTFORMATDATASET']._serialized_start = 4610
    _globals['_LISTFORMATDATASET']._serialized_end = 5010
    _globals['_LISTFORMATDATASET_LABELSENTRY']._serialized_start = 3071
    _globals['_LISTFORMATDATASET_LABELSENTRY']._serialized_end = 3116
    _globals['_DATASETLIST']._serialized_start = 5013
    _globals['_DATASETLIST']._serialized_end = 5173
    _globals['_UNDELETEDATASETREQUEST']._serialized_start = 5176
    _globals['_UNDELETEDATASETREQUEST']._serialized_end = 5306
    _globals['_DATASETSERVICE']._serialized_start = 5309
    _globals['_DATASETSERVICE']._serialized_end = 6710