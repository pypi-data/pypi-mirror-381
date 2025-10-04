"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/discoveryengine/v1/identity_mapping_store_service.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.discoveryengine.v1 import identity_mapping_store_pb2 as google_dot_cloud_dot_discoveryengine_dot_v1_dot_identity__mapping__store__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from .....google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nDgoogle/cloud/discoveryengine/v1/identity_mapping_store_service.proto\x12\x1fgoogle.cloud.discoveryengine.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a<google/cloud/discoveryengine/v1/identity_mapping_store.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x17google/rpc/status.proto"\xdc\x02\n!CreateIdentityMappingStoreRequest\x12J\n\x10cmek_config_name\x18\x05 \x01(\tB.\xfaA+\n)discoveryengine.googleapis.com/CmekConfigH\x00\x12\x16\n\x0cdisable_cmek\x18\x06 \x01(\x08H\x00\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12&\n\x19identity_mapping_store_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12Z\n\x16identity_mapping_store\x18\x03 \x01(\x0b25.google.cloud.discoveryengine.v1.IdentityMappingStoreB\x03\xe0A\x02B\x0e\n\x0ccmek_options"k\n\x1eGetIdentityMappingStoreRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore"n\n!DeleteIdentityMappingStoreRequest\x12I\n\x04name\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore"\xd5\x02\n\x1dImportIdentityMappingsRequest\x12d\n\rinline_source\x18\x02 \x01(\x0b2K.google.cloud.discoveryengine.v1.ImportIdentityMappingsRequest.InlineSourceH\x00\x12[\n\x16identity_mapping_store\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore\x1ag\n\x0cInlineSource\x12W\n\x18identity_mapping_entries\x18\x01 \x03(\x0b25.google.cloud.discoveryengine.v1.IdentityMappingEntryB\x08\n\x06source"K\n\x1eImportIdentityMappingsResponse\x12)\n\rerror_samples\x18\x01 \x03(\x0b2\x12.google.rpc.Status"\x81\x03\n\x1cPurgeIdentityMappingsRequest\x12c\n\rinline_source\x18\x02 \x01(\x0b2J.google.cloud.discoveryengine.v1.PurgeIdentityMappingsRequest.InlineSourceH\x00\x12[\n\x16identity_mapping_store\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore\x12\x0e\n\x06filter\x18\x03 \x01(\t\x12\x12\n\x05force\x18\x04 \x01(\x08H\x01\x88\x01\x01\x1ag\n\x0cInlineSource\x12W\n\x18identity_mapping_entries\x18\x01 \x03(\x0b25.google.cloud.discoveryengine.v1.IdentityMappingEntryB\x08\n\x06sourceB\x08\n\x06_force"\xa1\x01\n\x1bListIdentityMappingsRequest\x12[\n\x16identity_mapping_store\x18\x01 \x01(\tB;\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x90\x01\n\x1cListIdentityMappingsResponse\x12W\n\x18identity_mapping_entries\x18\x01 \x03(\x0b25.google.cloud.discoveryengine.v1.IdentityMappingEntry\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"\x8a\x01\n ListIdentityMappingStoresRequest\x12?\n\x06parent\x18\x01 \x01(\tB/\xe0A\x02\xfaA)\n\'discoveryengine.googleapis.com/Location\x12\x11\n\tpage_size\x18\x02 \x01(\x05\x12\x12\n\npage_token\x18\x03 \x01(\t"\x94\x01\n!ListIdentityMappingStoresResponse\x12V\n\x17identity_mapping_stores\x18\x01 \x03(\x0b25.google.cloud.discoveryengine.v1.IdentityMappingStore\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t"j\n%IdentityMappingEntryOperationMetadata\x12\x15\n\rsuccess_count\x18\x01 \x01(\x03\x12\x15\n\rfailure_count\x18\x02 \x01(\x03\x12\x13\n\x0btotal_count\x18\x03 \x01(\x03"\x86\x01\n"DeleteIdentityMappingStoreMetadata\x12/\n\x0bcreate_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.Timestamp\x12/\n\x0bupdate_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.Timestamp2\xd8\x10\n\x1bIdentityMappingStoreService\x12\xad\x02\n\x1aCreateIdentityMappingStore\x12B.google.cloud.discoveryengine.v1.CreateIdentityMappingStoreRequest\x1a5.google.cloud.discoveryengine.v1.IdentityMappingStore"\x93\x01\xdaA7parent,identity_mapping_store,identity_mapping_store_id\x82\xd3\xe4\x93\x02S"9/v1/{parent=projects/*/locations/*}/identityMappingStores:\x16identity_mapping_store\x12\xdb\x01\n\x17GetIdentityMappingStore\x12?.google.cloud.discoveryengine.v1.GetIdentityMappingStoreRequest\x1a5.google.cloud.discoveryengine.v1.IdentityMappingStore"H\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/identityMappingStores/*}\x12\xa8\x02\n\x1aDeleteIdentityMappingStore\x12B.google.cloud.discoveryengine.v1.DeleteIdentityMappingStoreRequest\x1a\x1d.google.longrunning.Operation"\xa6\x01\xcaA[\n\x15google.protobuf.Empty\x12Bgoogle.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/identityMappingStores/*}\x12\xf2\x02\n\x16ImportIdentityMappings\x12>.google.cloud.discoveryengine.v1.ImportIdentityMappingsRequest\x1a\x1d.google.longrunning.Operation"\xf8\x01\xcaA\x87\x01\n>google.cloud.discoveryengine.v1.ImportIdentityMappingsResponse\x12Egoogle.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata\x82\xd3\xe4\x93\x02g"b/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:importIdentityMappings:\x01*\x12\xc5\x02\n\x15PurgeIdentityMappings\x12=.google.cloud.discoveryengine.v1.PurgeIdentityMappingsRequest\x1a\x1d.google.longrunning.Operation"\xcd\x01\xcaA^\n\x15google.protobuf.Empty\x12Egoogle.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata\x82\xd3\xe4\x93\x02f"a/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:purgeIdentityMappings:\x01*\x12\xfd\x01\n\x14ListIdentityMappings\x12<.google.cloud.discoveryengine.v1.ListIdentityMappingsRequest\x1a=.google.cloud.discoveryengine.v1.ListIdentityMappingsResponse"h\x82\xd3\xe4\x93\x02b\x12`/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:listIdentityMappings\x12\xee\x01\n\x19ListIdentityMappingStores\x12A.google.cloud.discoveryengine.v1.ListIdentityMappingStoresRequest\x1aB.google.cloud.discoveryengine.v1.ListIdentityMappingStoresResponse"J\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*}/identityMappingStores\x1aR\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformB\x93\x02\n#com.google.cloud.discoveryengine.v1B IdentityMappingStoreServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.discoveryengine.v1.identity_mapping_store_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.cloud.discoveryengine.v1B IdentityMappingStoreServiceProtoP\x01ZMcloud.google.com/go/discoveryengine/apiv1/discoveryenginepb;discoveryenginepb\xa2\x02\x0fDISCOVERYENGINE\xaa\x02\x1fGoogle.Cloud.DiscoveryEngine.V1\xca\x02\x1fGoogle\\Cloud\\DiscoveryEngine\\V1\xea\x02"Google::Cloud::DiscoveryEngine::V1'
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['cmek_config_name']._loaded_options = None
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['cmek_config_name']._serialized_options = b'\xfaA+\n)discoveryengine.googleapis.com/CmekConfig'
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['identity_mapping_store_id']._loaded_options = None
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['identity_mapping_store_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['identity_mapping_store']._loaded_options = None
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['identity_mapping_store']._serialized_options = b'\xe0A\x02'
    _globals['_GETIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_DELETEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEIDENTITYMAPPINGSTOREREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._loaded_options = None
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._serialized_options = b'\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_PURGEIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._loaded_options = None
    _globals['_PURGEIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._serialized_options = b'\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_LISTIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._loaded_options = None
    _globals['_LISTIDENTITYMAPPINGSREQUEST'].fields_by_name['identity_mapping_store']._serialized_options = b'\xe0A\x02\xfaA5\n3discoveryengine.googleapis.com/IdentityMappingStore'
    _globals['_LISTIDENTITYMAPPINGSTORESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTIDENTITYMAPPINGSTORESREQUEST'].fields_by_name['parent']._serialized_options = b"\xe0A\x02\xfaA)\n'discoveryengine.googleapis.com/Location"
    _globals['_IDENTITYMAPPINGSTORESERVICE']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE']._serialized_options = b'\xcaA\x1ediscoveryengine.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['CreateIdentityMappingStore']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['CreateIdentityMappingStore']._serialized_options = b'\xdaA7parent,identity_mapping_store,identity_mapping_store_id\x82\xd3\xe4\x93\x02S"9/v1/{parent=projects/*/locations/*}/identityMappingStores:\x16identity_mapping_store'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['GetIdentityMappingStore']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['GetIdentityMappingStore']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02;\x129/v1/{name=projects/*/locations/*/identityMappingStores/*}'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['DeleteIdentityMappingStore']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['DeleteIdentityMappingStore']._serialized_options = b'\xcaA[\n\x15google.protobuf.Empty\x12Bgoogle.cloud.discoveryengine.v1.DeleteIdentityMappingStoreMetadata\xdaA\x04name\x82\xd3\xe4\x93\x02;*9/v1/{name=projects/*/locations/*/identityMappingStores/*}'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ImportIdentityMappings']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ImportIdentityMappings']._serialized_options = b'\xcaA\x87\x01\n>google.cloud.discoveryengine.v1.ImportIdentityMappingsResponse\x12Egoogle.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata\x82\xd3\xe4\x93\x02g"b/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:importIdentityMappings:\x01*'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['PurgeIdentityMappings']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['PurgeIdentityMappings']._serialized_options = b'\xcaA^\n\x15google.protobuf.Empty\x12Egoogle.cloud.discoveryengine.v1.IdentityMappingEntryOperationMetadata\x82\xd3\xe4\x93\x02f"a/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:purgeIdentityMappings:\x01*'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ListIdentityMappings']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ListIdentityMappings']._serialized_options = b'\x82\xd3\xe4\x93\x02b\x12`/v1/{identity_mapping_store=projects/*/locations/*/identityMappingStores/*}:listIdentityMappings'
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ListIdentityMappingStores']._loaded_options = None
    _globals['_IDENTITYMAPPINGSTORESERVICE'].methods_by_name['ListIdentityMappingStores']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02;\x129/v1/{parent=projects/*/locations/*}/identityMappingStores'
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST']._serialized_start = 407
    _globals['_CREATEIDENTITYMAPPINGSTOREREQUEST']._serialized_end = 755
    _globals['_GETIDENTITYMAPPINGSTOREREQUEST']._serialized_start = 757
    _globals['_GETIDENTITYMAPPINGSTOREREQUEST']._serialized_end = 864
    _globals['_DELETEIDENTITYMAPPINGSTOREREQUEST']._serialized_start = 866
    _globals['_DELETEIDENTITYMAPPINGSTOREREQUEST']._serialized_end = 976
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST']._serialized_start = 979
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST']._serialized_end = 1320
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST_INLINESOURCE']._serialized_start = 1207
    _globals['_IMPORTIDENTITYMAPPINGSREQUEST_INLINESOURCE']._serialized_end = 1310
    _globals['_IMPORTIDENTITYMAPPINGSRESPONSE']._serialized_start = 1322
    _globals['_IMPORTIDENTITYMAPPINGSRESPONSE']._serialized_end = 1397
    _globals['_PURGEIDENTITYMAPPINGSREQUEST']._serialized_start = 1400
    _globals['_PURGEIDENTITYMAPPINGSREQUEST']._serialized_end = 1785
    _globals['_PURGEIDENTITYMAPPINGSREQUEST_INLINESOURCE']._serialized_start = 1207
    _globals['_PURGEIDENTITYMAPPINGSREQUEST_INLINESOURCE']._serialized_end = 1310
    _globals['_LISTIDENTITYMAPPINGSREQUEST']._serialized_start = 1788
    _globals['_LISTIDENTITYMAPPINGSREQUEST']._serialized_end = 1949
    _globals['_LISTIDENTITYMAPPINGSRESPONSE']._serialized_start = 1952
    _globals['_LISTIDENTITYMAPPINGSRESPONSE']._serialized_end = 2096
    _globals['_LISTIDENTITYMAPPINGSTORESREQUEST']._serialized_start = 2099
    _globals['_LISTIDENTITYMAPPINGSTORESREQUEST']._serialized_end = 2237
    _globals['_LISTIDENTITYMAPPINGSTORESRESPONSE']._serialized_start = 2240
    _globals['_LISTIDENTITYMAPPINGSTORESRESPONSE']._serialized_end = 2388
    _globals['_IDENTITYMAPPINGENTRYOPERATIONMETADATA']._serialized_start = 2390
    _globals['_IDENTITYMAPPINGENTRYOPERATIONMETADATA']._serialized_end = 2496
    _globals['_DELETEIDENTITYMAPPINGSTOREMETADATA']._serialized_start = 2499
    _globals['_DELETEIDENTITYMAPPINGSTOREMETADATA']._serialized_end = 2633
    _globals['_IDENTITYMAPPINGSTORESERVICE']._serialized_start = 2636
    _globals['_IDENTITYMAPPINGSTORESERVICE']._serialized_end = 4772