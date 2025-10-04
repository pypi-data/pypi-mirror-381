"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/storagebatchoperations/v1/storage_batch_operations_types.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import code_pb2 as google_dot_rpc_dot_code__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/cloud/storagebatchoperations/v1/storage_batch_operations_types.proto\x12&google.cloud.storagebatchoperations.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x15google/rpc/code.proto"\xfb\x08\n\x03Job\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x01\x12I\n\x0bbucket_list\x18\x13 \x01(\x0b22.google.cloud.storagebatchoperations.v1.BucketListH\x00\x12P\n\x0fput_object_hold\x18\x05 \x01(\x0b25.google.cloud.storagebatchoperations.v1.PutObjectHoldH\x01\x12M\n\rdelete_object\x18\x06 \x01(\x0b24.google.cloud.storagebatchoperations.v1.DeleteObjectH\x01\x12K\n\x0cput_metadata\x18\x08 \x01(\x0b23.google.cloud.storagebatchoperations.v1.PutMetadataH\x01\x12O\n\x0erewrite_object\x18\x14 \x01(\x0b25.google.cloud.storagebatchoperations.v1.RewriteObjectH\x01\x12R\n\x0elogging_config\x18\t \x01(\x0b25.google.cloud.storagebatchoperations.v1.LoggingConfigB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\n \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rschedule_time\x18\x0b \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rcomplete_time\x18\x0c \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x08counters\x18\r \x01(\x0b20.google.cloud.storagebatchoperations.v1.CountersB\x03\xe0A\x03\x12R\n\x0ferror_summaries\x18\x0e \x03(\x0b24.google.cloud.storagebatchoperations.v1.ErrorSummaryB\x03\xe0A\x03\x12E\n\x05state\x18\x0f \x01(\x0e21.google.cloud.storagebatchoperations.v1.Job.StateB\x03\xe0A\x03"T\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\r\n\tSUCCEEDED\x10\x02\x12\x0c\n\x08CANCELED\x10\x03\x12\n\n\x06FAILED\x10\x04:m\xeaAj\n)storagebatchoperations.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}*\x04jobs2\x03jobB\x08\n\x06sourceB\x10\n\x0etransformation"\xa6\x02\n\nBucketList\x12O\n\x07buckets\x18\x01 \x03(\x0b29.google.cloud.storagebatchoperations.v1.BucketList.BucketB\x03\xe0A\x02\x1a\xc6\x01\n\x06Bucket\x12\x13\n\x06bucket\x18\x01 \x01(\tB\x03\xe0A\x02\x12I\n\x0bprefix_list\x18\x02 \x01(\x0b22.google.cloud.storagebatchoperations.v1.PrefixListH\x00\x12D\n\x08manifest\x18\x03 \x01(\x0b20.google.cloud.storagebatchoperations.v1.ManifestH\x00B\x16\n\x14object_configuration"*\n\x08Manifest\x12\x1e\n\x11manifest_location\x18\x02 \x01(\tB\x03\xe0A\x02"3\n\nPrefixList\x12%\n\x18included_object_prefixes\x18\x02 \x03(\tB\x03\xe0A\x01"\x8e\x02\n\rPutObjectHold\x12]\n\x0etemporary_hold\x18\x01 \x01(\x0e2@.google.cloud.storagebatchoperations.v1.PutObjectHold.HoldStatusB\x03\xe0A\x02\x12_\n\x10event_based_hold\x18\x02 \x01(\x0e2@.google.cloud.storagebatchoperations.v1.PutObjectHold.HoldStatusB\x03\xe0A\x02"=\n\nHoldStatus\x12\x1b\n\x17HOLD_STATUS_UNSPECIFIED\x10\x00\x12\x07\n\x03SET\x10\x01\x12\t\n\x05UNSET\x10\x02">\n\x0cDeleteObject\x12.\n!permanent_object_deletion_enabled\x18\x01 \x01(\x08B\x03\xe0A\x02"\\\n\rRewriteObject\x12?\n\x07kms_key\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/CryptoKeyH\x00\x88\x01\x01B\n\n\x08_kms_key"\xef\x03\n\x0bPutMetadata\x12%\n\x13content_disposition\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x88\x01\x01\x12"\n\x10content_encoding\x18\x02 \x01(\tB\x03\xe0A\x01H\x01\x88\x01\x01\x12"\n\x10content_language\x18\x03 \x01(\tB\x03\xe0A\x01H\x02\x88\x01\x01\x12\x1e\n\x0ccontent_type\x18\x04 \x01(\tB\x03\xe0A\x01H\x03\x88\x01\x01\x12\x1f\n\rcache_control\x18\x05 \x01(\tB\x03\xe0A\x01H\x04\x88\x01\x01\x12\x1d\n\x0bcustom_time\x18\x06 \x01(\tB\x03\xe0A\x01H\x05\x88\x01\x01\x12e\n\x0fcustom_metadata\x18\x07 \x03(\x0b2G.google.cloud.storagebatchoperations.v1.PutMetadata.CustomMetadataEntryB\x03\xe0A\x01\x1a5\n\x13CustomMetadataEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01B\x16\n\x14_content_dispositionB\x13\n\x11_content_encodingB\x13\n\x11_content_languageB\x0f\n\r_content_typeB\x10\n\x0e_cache_controlB\x0e\n\x0c_custom_time"\xaa\x01\n\x0cErrorSummary\x12)\n\nerror_code\x18\x01 \x01(\x0e2\x10.google.rpc.CodeB\x03\xe0A\x02\x12\x18\n\x0berror_count\x18\x02 \x01(\x03B\x03\xe0A\x02\x12U\n\x11error_log_entries\x18\x03 \x03(\x0b25.google.cloud.storagebatchoperations.v1.ErrorLogEntryB\x03\xe0A\x02"J\n\rErrorLogEntry\x12\x1a\n\nobject_uri\x18\x01 \x01(\tB\x06\xe0A\x02\xe0A\x03\x12\x1d\n\rerror_details\x18\x03 \x03(\tB\x06\xe0A\x01\xe0A\x03"r\n\x08Counters\x12\x1f\n\x12total_object_count\x18\x01 \x01(\x03B\x03\xe0A\x03\x12#\n\x16succeeded_object_count\x18\x02 \x01(\x03B\x03\xe0A\x03\x12 \n\x13failed_object_count\x18\x03 \x01(\x03B\x03\xe0A\x03"\xf5\x02\n\rLoggingConfig\x12^\n\x0blog_actions\x18\x01 \x03(\x0e2D.google.cloud.storagebatchoperations.v1.LoggingConfig.LoggableActionB\x03\xe0A\x02\x12i\n\x11log_action_states\x18\x02 \x03(\x0e2I.google.cloud.storagebatchoperations.v1.LoggingConfig.LoggableActionStateB\x03\xe0A\x02"@\n\x0eLoggableAction\x12\x1f\n\x1bLOGGABLE_ACTION_UNSPECIFIED\x10\x00\x12\r\n\tTRANSFORM\x10\x06"W\n\x13LoggableActionState\x12%\n!LOGGABLE_ACTION_STATE_UNSPECIFIED\x10\x00\x12\r\n\tSUCCEEDED\x10\x01\x12\n\n\x06FAILED\x10\x02B\xad\x03\n*com.google.cloud.storagebatchoperations.v1B StorageBatchOperationsTypesProtoP\x01Zbcloud.google.com/go/storagebatchoperations/apiv1/storagebatchoperationspb;storagebatchoperationspb\xaa\x02&Google.Cloud.StorageBatchOperations.V1\xca\x02&Google\\Cloud\\StorageBatchOperations\\V1\xea\x02)Google::Cloud::StorageBatchOperations::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.storagebatchoperations.v1.storage_batch_operations_types_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n*com.google.cloud.storagebatchoperations.v1B StorageBatchOperationsTypesProtoP\x01Zbcloud.google.com/go/storagebatchoperations/apiv1/storagebatchoperationspb;storagebatchoperationspb\xaa\x02&Google.Cloud.StorageBatchOperations.V1\xca\x02&Google\\Cloud\\StorageBatchOperations\\V1\xea\x02)Google::Cloud::StorageBatchOperations::V1\xeaAx\n!cloudkms.googleapis.com/CryptoKey\x12Sprojects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}'
    _globals['_JOB'].fields_by_name['name']._loaded_options = None
    _globals['_JOB'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_JOB'].fields_by_name['description']._loaded_options = None
    _globals['_JOB'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_JOB'].fields_by_name['logging_config']._loaded_options = None
    _globals['_JOB'].fields_by_name['logging_config']._serialized_options = b'\xe0A\x01'
    _globals['_JOB'].fields_by_name['create_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['schedule_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['schedule_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['complete_time']._loaded_options = None
    _globals['_JOB'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['counters']._loaded_options = None
    _globals['_JOB'].fields_by_name['counters']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['error_summaries']._loaded_options = None
    _globals['_JOB'].fields_by_name['error_summaries']._serialized_options = b'\xe0A\x03'
    _globals['_JOB'].fields_by_name['state']._loaded_options = None
    _globals['_JOB'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_JOB']._loaded_options = None
    _globals['_JOB']._serialized_options = b'\xeaAj\n)storagebatchoperations.googleapis.com/Job\x122projects/{project}/locations/{location}/jobs/{job}*\x04jobs2\x03job'
    _globals['_BUCKETLIST_BUCKET'].fields_by_name['bucket']._loaded_options = None
    _globals['_BUCKETLIST_BUCKET'].fields_by_name['bucket']._serialized_options = b'\xe0A\x02'
    _globals['_BUCKETLIST'].fields_by_name['buckets']._loaded_options = None
    _globals['_BUCKETLIST'].fields_by_name['buckets']._serialized_options = b'\xe0A\x02'
    _globals['_MANIFEST'].fields_by_name['manifest_location']._loaded_options = None
    _globals['_MANIFEST'].fields_by_name['manifest_location']._serialized_options = b'\xe0A\x02'
    _globals['_PREFIXLIST'].fields_by_name['included_object_prefixes']._loaded_options = None
    _globals['_PREFIXLIST'].fields_by_name['included_object_prefixes']._serialized_options = b'\xe0A\x01'
    _globals['_PUTOBJECTHOLD'].fields_by_name['temporary_hold']._loaded_options = None
    _globals['_PUTOBJECTHOLD'].fields_by_name['temporary_hold']._serialized_options = b'\xe0A\x02'
    _globals['_PUTOBJECTHOLD'].fields_by_name['event_based_hold']._loaded_options = None
    _globals['_PUTOBJECTHOLD'].fields_by_name['event_based_hold']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEOBJECT'].fields_by_name['permanent_object_deletion_enabled']._loaded_options = None
    _globals['_DELETEOBJECT'].fields_by_name['permanent_object_deletion_enabled']._serialized_options = b'\xe0A\x02'
    _globals['_REWRITEOBJECT'].fields_by_name['kms_key']._loaded_options = None
    _globals['_REWRITEOBJECT'].fields_by_name['kms_key']._serialized_options = b'\xe0A\x02\xfaA#\n!cloudkms.googleapis.com/CryptoKey'
    _globals['_PUTMETADATA_CUSTOMMETADATAENTRY']._loaded_options = None
    _globals['_PUTMETADATA_CUSTOMMETADATAENTRY']._serialized_options = b'8\x01'
    _globals['_PUTMETADATA'].fields_by_name['content_disposition']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['content_disposition']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['content_encoding']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['content_encoding']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['content_language']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['content_language']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['content_type']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['content_type']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['cache_control']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['cache_control']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['custom_time']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['custom_time']._serialized_options = b'\xe0A\x01'
    _globals['_PUTMETADATA'].fields_by_name['custom_metadata']._loaded_options = None
    _globals['_PUTMETADATA'].fields_by_name['custom_metadata']._serialized_options = b'\xe0A\x01'
    _globals['_ERRORSUMMARY'].fields_by_name['error_code']._loaded_options = None
    _globals['_ERRORSUMMARY'].fields_by_name['error_code']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORSUMMARY'].fields_by_name['error_count']._loaded_options = None
    _globals['_ERRORSUMMARY'].fields_by_name['error_count']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORSUMMARY'].fields_by_name['error_log_entries']._loaded_options = None
    _globals['_ERRORSUMMARY'].fields_by_name['error_log_entries']._serialized_options = b'\xe0A\x02'
    _globals['_ERRORLOGENTRY'].fields_by_name['object_uri']._loaded_options = None
    _globals['_ERRORLOGENTRY'].fields_by_name['object_uri']._serialized_options = b'\xe0A\x02\xe0A\x03'
    _globals['_ERRORLOGENTRY'].fields_by_name['error_details']._loaded_options = None
    _globals['_ERRORLOGENTRY'].fields_by_name['error_details']._serialized_options = b'\xe0A\x01\xe0A\x03'
    _globals['_COUNTERS'].fields_by_name['total_object_count']._loaded_options = None
    _globals['_COUNTERS'].fields_by_name['total_object_count']._serialized_options = b'\xe0A\x03'
    _globals['_COUNTERS'].fields_by_name['succeeded_object_count']._loaded_options = None
    _globals['_COUNTERS'].fields_by_name['succeeded_object_count']._serialized_options = b'\xe0A\x03'
    _globals['_COUNTERS'].fields_by_name['failed_object_count']._loaded_options = None
    _globals['_COUNTERS'].fields_by_name['failed_object_count']._serialized_options = b'\xe0A\x03'
    _globals['_LOGGINGCONFIG'].fields_by_name['log_actions']._loaded_options = None
    _globals['_LOGGINGCONFIG'].fields_by_name['log_actions']._serialized_options = b'\xe0A\x02'
    _globals['_LOGGINGCONFIG'].fields_by_name['log_action_states']._loaded_options = None
    _globals['_LOGGINGCONFIG'].fields_by_name['log_action_states']._serialized_options = b'\xe0A\x02'
    _globals['_JOB']._serialized_start = 236
    _globals['_JOB']._serialized_end = 1383
    _globals['_JOB_STATE']._serialized_start = 1160
    _globals['_JOB_STATE']._serialized_end = 1244
    _globals['_BUCKETLIST']._serialized_start = 1386
    _globals['_BUCKETLIST']._serialized_end = 1680
    _globals['_BUCKETLIST_BUCKET']._serialized_start = 1482
    _globals['_BUCKETLIST_BUCKET']._serialized_end = 1680
    _globals['_MANIFEST']._serialized_start = 1682
    _globals['_MANIFEST']._serialized_end = 1724
    _globals['_PREFIXLIST']._serialized_start = 1726
    _globals['_PREFIXLIST']._serialized_end = 1777
    _globals['_PUTOBJECTHOLD']._serialized_start = 1780
    _globals['_PUTOBJECTHOLD']._serialized_end = 2050
    _globals['_PUTOBJECTHOLD_HOLDSTATUS']._serialized_start = 1989
    _globals['_PUTOBJECTHOLD_HOLDSTATUS']._serialized_end = 2050
    _globals['_DELETEOBJECT']._serialized_start = 2052
    _globals['_DELETEOBJECT']._serialized_end = 2114
    _globals['_REWRITEOBJECT']._serialized_start = 2116
    _globals['_REWRITEOBJECT']._serialized_end = 2208
    _globals['_PUTMETADATA']._serialized_start = 2211
    _globals['_PUTMETADATA']._serialized_end = 2706
    _globals['_PUTMETADATA_CUSTOMMETADATAENTRY']._serialized_start = 2536
    _globals['_PUTMETADATA_CUSTOMMETADATAENTRY']._serialized_end = 2589
    _globals['_ERRORSUMMARY']._serialized_start = 2709
    _globals['_ERRORSUMMARY']._serialized_end = 2879
    _globals['_ERRORLOGENTRY']._serialized_start = 2881
    _globals['_ERRORLOGENTRY']._serialized_end = 2955
    _globals['_COUNTERS']._serialized_start = 2957
    _globals['_COUNTERS']._serialized_end = 3071
    _globals['_LOGGINGCONFIG']._serialized_start = 3074
    _globals['_LOGGINGCONFIG']._serialized_end = 3447
    _globals['_LOGGINGCONFIG_LOGGABLEACTION']._serialized_start = 3294
    _globals['_LOGGINGCONFIG_LOGGABLEACTION']._serialized_end = 3358
    _globals['_LOGGINGCONFIG_LOGGABLEACTIONSTATE']._serialized_start = 3360
    _globals['_LOGGINGCONFIG_LOGGABLEACTIONSTATE']._serialized_end = 3447