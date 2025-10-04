"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/bigquery/storage/v1beta/metastore_partition.proto')
_sym_db = _symbol_database.Default()
from ......google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from ......google.api import client_pb2 as google_dot_api_dot_client__pb2
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from ......google.cloud.bigquery.storage.v1beta import partition_pb2 as google_dot_cloud_dot_bigquery_dot_storage_dot_v1beta_dot_partition__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n>google/cloud/bigquery/storage/v1beta/metastore_partition.proto\x12$google.cloud.bigquery.storage.v1beta\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a4google/cloud/bigquery/storage/v1beta/partition.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto"\xb4\x01\n\x1fCreateMetastorePartitionRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12Z\n\x13metastore_partition\x18\x02 \x01(\x0b28.google.cloud.bigquery.storage.v1beta.MetastorePartitionB\x03\xe0A\x02"\xfa\x01\n%BatchCreateMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\\\n\x08requests\x18\x02 \x03(\x0b2E.google.cloud.bigquery.storage.v1beta.CreateMetastorePartitionRequestB\x03\xe0A\x02\x12%\n\x18skip_existing_partitions\x18\x03 \x01(\x08B\x03\xe0A\x01\x12\x15\n\x08trace_id\x18\x04 \x01(\tB\x03\xe0A\x01"v\n&BatchCreateMetastorePartitionsResponse\x12L\n\npartitions\x18\x01 \x03(\x0b28.google.cloud.bigquery.storage.v1beta.MetastorePartition"\xd4\x01\n%BatchDeleteMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12]\n\x10partition_values\x18\x02 \x03(\x0b2>.google.cloud.bigquery.storage.v1beta.MetastorePartitionValuesB\x03\xe0A\x02\x12\x15\n\x08trace_id\x18\x04 \x01(\tB\x03\xe0A\x01"\xb3\x01\n\x1fUpdateMetastorePartitionRequest\x12Z\n\x13metastore_partition\x18\x01 \x01(\x0b28.google.cloud.bigquery.storage.v1beta.MetastorePartitionB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x01"\xd3\x01\n%BatchUpdateMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\\\n\x08requests\x18\x02 \x03(\x0b2E.google.cloud.bigquery.storage.v1beta.UpdateMetastorePartitionRequestB\x03\xe0A\x02\x12\x15\n\x08trace_id\x18\x04 \x01(\tB\x03\xe0A\x01"v\n&BatchUpdateMetastorePartitionsResponse\x12L\n\npartitions\x18\x01 \x03(\x0b28.google.cloud.bigquery.storage.v1beta.MetastorePartition"\x83\x01\n\x1eListMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08trace_id\x18\x03 \x01(\tB\x03\xe0A\x01"\xc6\x01\n\x1fListMetastorePartitionsResponse\x12R\n\npartitions\x18\x01 \x01(\x0b2<.google.cloud.bigquery.storage.v1beta.MetastorePartitionListH\x00\x12C\n\x07streams\x18\x02 \x01(\x0b20.google.cloud.bigquery.storage.v1beta.StreamListH\x00B\n\n\x08response"\xdd\x01\n StreamMetastorePartitionsRequest\x125\n\x06parent\x18\x01 \x01(\tB%\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table\x12[\n\x14metastore_partitions\x18\x02 \x03(\x0b28.google.cloud.bigquery.storage.v1beta.MetastorePartitionB\x03\xe0A\x01\x12%\n\x18skip_existing_partitions\x18\x03 \x01(\x08B\x03\xe0A\x01"u\n!StreamMetastorePartitionsResponse\x12\'\n\x1ftotal_partitions_streamed_count\x18\x02 \x01(\x03\x12\'\n\x1ftotal_partitions_inserted_count\x18\x03 \x01(\x03"L\n\x16BatchSizeTooLargeError\x12\x16\n\x0emax_batch_size\x18\x01 \x01(\x03\x12\x1a\n\rerror_message\x18\x02 \x01(\tB\x03\xe0A\x012\xd1\n\n\x19MetastorePartitionService\x12\x8e\x02\n\x1eBatchCreateMetastorePartitions\x12K.google.cloud.bigquery.storage.v1beta.BatchCreateMetastorePartitionsRequest\x1aL.google.cloud.bigquery.storage.v1beta.BatchCreateMetastorePartitionsResponse"Q\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchCreate:\x01*\x12\xd8\x01\n\x1eBatchDeleteMetastorePartitions\x12K.google.cloud.bigquery.storage.v1beta.BatchDeleteMetastorePartitionsRequest\x1a\x16.google.protobuf.Empty"Q\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchDelete:\x01*\x12\x8e\x02\n\x1eBatchUpdateMetastorePartitions\x12K.google.cloud.bigquery.storage.v1beta.BatchUpdateMetastorePartitionsRequest\x1aL.google.cloud.bigquery.storage.v1beta.BatchUpdateMetastorePartitionsResponse"Q\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchUpdate:\x01*\x12\x84\x02\n\x17ListMetastorePartitions\x12D.google.cloud.bigquery.storage.v1beta.ListMetastorePartitionsRequest\x1aE.google.cloud.bigquery.storage.v1beta.ListMetastorePartitionsResponse"\\\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:list\x12\xb2\x01\n\x19StreamMetastorePartitions\x12F.google.cloud.bigquery.storage.v1beta.StreamMetastorePartitionsRequest\x1aG.google.cloud.bigquery.storage.v1beta.StreamMetastorePartitionsResponse"\x00(\x010\x01\x1a{\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platformB\xb6\x02\n(com.google.cloud.bigquery.storage.v1betaB\x1eMetastorePartitionServiceProtoP\x01ZBcloud.google.com/go/bigquery/storage/apiv1beta/storagepb;storagepb\xaa\x02$Google.Cloud.BigQuery.Storage.V1Beta\xca\x02$Google\\Cloud\\BigQuery\\Storage\\V1beta\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.bigquery.storage.v1beta.metastore_partition_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n(com.google.cloud.bigquery.storage.v1betaB\x1eMetastorePartitionServiceProtoP\x01ZBcloud.google.com/go/bigquery/storage/apiv1beta/storagepb;storagepb\xaa\x02$Google.Cloud.BigQuery.Storage.V1Beta\xca\x02$Google\\Cloud\\BigQuery\\Storage\\V1beta\xeaAU\n\x1dbigquery.googleapis.com/Table\x124projects/{project}/datasets/{dataset}/tables/{table}'
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._loaded_options = None
    _globals['_CREATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._loaded_options = None
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['partition_values']._loaded_options = None
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['partition_values']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._loaded_options = None
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._loaded_options = None
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['metastore_partition']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEMETASTOREPARTITIONREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._loaded_options = None
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['requests']._serialized_options = b'\xe0A\x02'
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._loaded_options = None
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._loaded_options = None
    _globals['_LISTMETASTOREPARTITIONSREQUEST'].fields_by_name['trace_id']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA\x1f\n\x1dbigquery.googleapis.com/Table'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['metastore_partitions']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['metastore_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._loaded_options = None
    _globals['_STREAMMETASTOREPARTITIONSREQUEST'].fields_by_name['skip_existing_partitions']._serialized_options = b'\xe0A\x01'
    _globals['_BATCHSIZETOOLARGEERROR'].fields_by_name['error_message']._loaded_options = None
    _globals['_BATCHSIZETOOLARGEERROR'].fields_by_name['error_message']._serialized_options = b'\xe0A\x01'
    _globals['_METASTOREPARTITIONSERVICE']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE']._serialized_options = b'\xcaA\x1ebigquerystorage.googleapis.com\xd2AWhttps://www.googleapis.com/auth/bigquery,https://www.googleapis.com/auth/cloud-platform'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchCreateMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchCreateMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchCreate:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchDeleteMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchDeleteMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchDelete:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchUpdateMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['BatchUpdateMetastorePartitions']._serialized_options = b'\x82\xd3\xe4\x93\x02K"F/v1beta/{parent=projects/*/datasets/*/tables/*}/partitions:batchUpdate:\x01*'
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['ListMetastorePartitions']._loaded_options = None
    _globals['_METASTOREPARTITIONSERVICE'].methods_by_name['ListMetastorePartitions']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02M\x12K/v1beta/{parent=projects/*/locations/*/datasets/*/tables/*}/partitions:list'
    _globals['_CREATEMETASTOREPARTITIONREQUEST']._serialized_start = 337
    _globals['_CREATEMETASTOREPARTITIONREQUEST']._serialized_end = 517
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST']._serialized_start = 520
    _globals['_BATCHCREATEMETASTOREPARTITIONSREQUEST']._serialized_end = 770
    _globals['_BATCHCREATEMETASTOREPARTITIONSRESPONSE']._serialized_start = 772
    _globals['_BATCHCREATEMETASTOREPARTITIONSRESPONSE']._serialized_end = 890
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST']._serialized_start = 893
    _globals['_BATCHDELETEMETASTOREPARTITIONSREQUEST']._serialized_end = 1105
    _globals['_UPDATEMETASTOREPARTITIONREQUEST']._serialized_start = 1108
    _globals['_UPDATEMETASTOREPARTITIONREQUEST']._serialized_end = 1287
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST']._serialized_start = 1290
    _globals['_BATCHUPDATEMETASTOREPARTITIONSREQUEST']._serialized_end = 1501
    _globals['_BATCHUPDATEMETASTOREPARTITIONSRESPONSE']._serialized_start = 1503
    _globals['_BATCHUPDATEMETASTOREPARTITIONSRESPONSE']._serialized_end = 1621
    _globals['_LISTMETASTOREPARTITIONSREQUEST']._serialized_start = 1624
    _globals['_LISTMETASTOREPARTITIONSREQUEST']._serialized_end = 1755
    _globals['_LISTMETASTOREPARTITIONSRESPONSE']._serialized_start = 1758
    _globals['_LISTMETASTOREPARTITIONSRESPONSE']._serialized_end = 1956
    _globals['_STREAMMETASTOREPARTITIONSREQUEST']._serialized_start = 1959
    _globals['_STREAMMETASTOREPARTITIONSREQUEST']._serialized_end = 2180
    _globals['_STREAMMETASTOREPARTITIONSRESPONSE']._serialized_start = 2182
    _globals['_STREAMMETASTOREPARTITIONSRESPONSE']._serialized_end = 2299
    _globals['_BATCHSIZETOOLARGEERROR']._serialized_start = 2301
    _globals['_BATCHSIZETOOLARGEERROR']._serialized_end = 2377
    _globals['_METASTOREPARTITIONSERVICE']._serialized_start = 2380
    _globals['_METASTOREPARTITIONSERVICE']._serialized_end = 3741