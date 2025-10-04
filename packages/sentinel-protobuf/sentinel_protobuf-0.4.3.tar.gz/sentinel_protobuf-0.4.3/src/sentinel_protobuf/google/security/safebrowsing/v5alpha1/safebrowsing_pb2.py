"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/security/safebrowsing/v5alpha1/safebrowsing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n8google/security/safebrowsing/v5alpha1/safebrowsing.proto\x12%google.security.safebrowsing.v5alpha1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto"F\n\x13SearchHashesRequest\x12\x1a\n\rhash_prefixes\x18\x01 \x03(\x0cB\x03\xe0A\x02\x12\x13\n\x06filter\x18\x02 \x01(\tB\x03\xe0A\x01"\x94\x01\n\x14SearchHashesResponse\x12I\n\x0bfull_hashes\x18\x01 \x03(\x0b2/.google.security.safebrowsing.v5alpha1.FullHashB\x03\xe0A\x06\x121\n\x0ecache_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\xa9\x02\n\x08FullHash\x12\x11\n\tfull_hash\x18\x01 \x01(\x0c\x12^\n\x11full_hash_details\x18\x02 \x03(\x0b2>.google.security.safebrowsing.v5alpha1.FullHash.FullHashDetailB\x03\xe0A\x06\x1a\xa9\x01\n\x0eFullHashDetail\x12F\n\x0bthreat_type\x18\x01 \x01(\x0e21.google.security.safebrowsing.v5alpha1.ThreatType\x12O\n\nattributes\x18\x02 \x03(\x0e26.google.security.safebrowsing.v5alpha1.ThreatAttributeB\x03\xe0A\x06"\xb3\x01\n\x12GetHashListRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12P\n\x10size_constraints\x18\x04 \x01(\x0b26.google.security.safebrowsing.v5alpha1.SizeConstraints"K\n\x0fSizeConstraints\x12\x1a\n\x12max_update_entries\x18\x01 \x01(\x05\x12\x1c\n\x14max_database_entries\x18\x02 \x01(\x05"q\n\x15RiceDeltaEncoded32Bit\x12\x13\n\x0bfirst_value\x18\x01 \x01(\r\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x15\n\rentries_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c"q\n\x15RiceDeltaEncoded64Bit\x12\x13\n\x0bfirst_value\x18\x01 \x01(\x04\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x15\n\rentries_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c"\x8d\x01\n\x16RiceDeltaEncoded128Bit\x12\x16\n\x0efirst_value_hi\x18\x01 \x01(\x04\x12\x16\n\x0efirst_value_lo\x18\x02 \x01(\x06\x12\x16\n\x0erice_parameter\x18\x03 \x01(\x05\x12\x15\n\rentries_count\x18\x04 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x05 \x01(\x0c"\xdf\x01\n\x16RiceDeltaEncoded256Bit\x12\x1e\n\x16first_value_first_part\x18\x01 \x01(\x04\x12\x1f\n\x17first_value_second_part\x18\x02 \x01(\x06\x12\x1e\n\x16first_value_third_part\x18\x03 \x01(\x06\x12\x1f\n\x17first_value_fourth_part\x18\x04 \x01(\x06\x12\x16\n\x0erice_parameter\x18\x05 \x01(\x05\x12\x15\n\rentries_count\x18\x06 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x07 \x01(\x0c"\x9a\x03\n\x10HashListMetadata\x12L\n\x0cthreat_types\x18\x01 \x03(\x0e21.google.security.safebrowsing.v5alpha1.ThreatTypeB\x03\xe0A\x06\x12U\n\x11likely_safe_types\x18\x02 \x03(\x0e25.google.security.safebrowsing.v5alpha1.LikelySafeTypeB\x03\xe0A\x06\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12W\n\x0bhash_length\x18\x06 \x01(\x0e2B.google.security.safebrowsing.v5alpha1.HashListMetadata.HashLength"s\n\nHashLength\x12\x1b\n\x17HASH_LENGTH_UNSPECIFIED\x10\x00\x12\x0e\n\nFOUR_BYTES\x10\x02\x12\x0f\n\x0bEIGHT_BYTES\x10\x03\x12\x11\n\rSIXTEEN_BYTES\x10\x04\x12\x14\n\x10THIRTY_TWO_BYTES\x10\x05"\x98\x06\n\x08HashList\x12\\\n\x14additions_four_bytes\x18\x04 \x01(\x0b2<.google.security.safebrowsing.v5alpha1.RiceDeltaEncoded32BitH\x00\x12]\n\x15additions_eight_bytes\x18\t \x01(\x0b2<.google.security.safebrowsing.v5alpha1.RiceDeltaEncoded64BitH\x00\x12`\n\x17additions_sixteen_bytes\x18\n \x01(\x0b2=.google.security.safebrowsing.v5alpha1.RiceDeltaEncoded128BitH\x00\x12c\n\x1aadditions_thirty_two_bytes\x18\x0b \x01(\x0b2=.google.security.safebrowsing.v5alpha1.RiceDeltaEncoded256BitH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12\x16\n\x0epartial_update\x18\x03 \x01(\x08\x12Y\n\x13compressed_removals\x18\x05 \x01(\x0b2<.google.security.safebrowsing.v5alpha1.RiceDeltaEncoded32Bit\x128\n\x15minimum_wait_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x17\n\x0fsha256_checksum\x18\x07 \x01(\x0c\x12I\n\x08metadata\x18\x08 \x01(\x0b27.google.security.safebrowsing.v5alpha1.HashListMetadata:@\xeaA=\n$safebrowsing.googleapis.com/HashList\x12\x15hashLists/{hash_list}B\x16\n\x14compressed_additions"\xba\x01\n\x18BatchGetHashListsRequest\x12;\n\x05names\x18\x01 \x03(\tB,\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList\x12\x0f\n\x07version\x18\x02 \x03(\x0c\x12P\n\x10size_constraints\x18\x04 \x01(\x0b26.google.security.safebrowsing.v5alpha1.SizeConstraints"`\n\x19BatchGetHashListsResponse\x12C\n\nhash_lists\x18\x01 \x03(\x0b2/.google.security.safebrowsing.v5alpha1.HashList"=\n\x14ListHashListsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"u\n\x15ListHashListsResponse\x12C\n\nhash_lists\x18\x01 \x03(\x0b2/.google.security.safebrowsing.v5alpha1.HashList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x8a\x01\n\nThreatType\x12\x1b\n\x17THREAT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MALWARE\x10\x01\x12\x16\n\x12SOCIAL_ENGINEERING\x10\x02\x12\x15\n\x11UNWANTED_SOFTWARE\x10\x03\x12#\n\x1fPOTENTIALLY_HARMFUL_APPLICATION\x10\x04*_\n\x0eLikelySafeType\x12 \n\x1cLIKELY_SAFE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10GENERAL_BROWSING\x10\x01\x12\x07\n\x03CSD\x10\x02\x12\x0c\n\x08DOWNLOAD\x10\x03*O\n\x0fThreatAttribute\x12 \n\x1cTHREAT_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\n\n\x06CANARY\x10\x01\x12\x0e\n\nFRAME_ONLY\x10\x022\xeb\x05\n\x0cSafeBrowsing\x12\xa8\x01\n\x0cSearchHashes\x12:.google.security.safebrowsing.v5alpha1.SearchHashesRequest\x1a;.google.security.safebrowsing.v5alpha1.SearchHashesResponse"\x1f\x82\xd3\xe4\x93\x02\x19\x12\x17/v5alpha1/hashes:search\x12\xa3\x01\n\x0bGetHashList\x129.google.security.safebrowsing.v5alpha1.GetHashListRequest\x1a/.google.security.safebrowsing.v5alpha1.HashList"(\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v5alpha1/hashList/{name}\x12\xaa\x01\n\rListHashLists\x12;.google.security.safebrowsing.v5alpha1.ListHashListsRequest\x1a<.google.security.safebrowsing.v5alpha1.ListHashListsResponse"\x1e\xdaA\x00\x82\xd3\xe4\x93\x02\x15\x12\x13/v5alpha1/hashLists\x12\xbc\x01\n\x11BatchGetHashLists\x12?.google.security.safebrowsing.v5alpha1.BatchGetHashListsRequest\x1a@.google.security.safebrowsing.v5alpha1.BatchGetHashListsResponse"$\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v5alpha1/hashLists:batchGet\x1a\x1e\xcaA\x1bsafebrowsing.googleapis.comB\x93\x01\n)com.google.security.safebrowsing.v5alpha1B\x11SafeBrowsingProtoP\x01ZQgoogle.golang.org/genproto/googleapis/security/safebrowsing/v5alpha1;safebrowsingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.security.safebrowsing.v5alpha1.safebrowsing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n)com.google.security.safebrowsing.v5alpha1B\x11SafeBrowsingProtoP\x01ZQgoogle.golang.org/genproto/googleapis/security/safebrowsing/v5alpha1;safebrowsing'
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['hash_prefixes']._loaded_options = None
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['hash_prefixes']._serialized_options = b'\xe0A\x02'
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_SEARCHHASHESRESPONSE'].fields_by_name['full_hashes']._loaded_options = None
    _globals['_SEARCHHASHESRESPONSE'].fields_by_name['full_hashes']._serialized_options = b'\xe0A\x06'
    _globals['_FULLHASH_FULLHASHDETAIL'].fields_by_name['attributes']._loaded_options = None
    _globals['_FULLHASH_FULLHASHDETAIL'].fields_by_name['attributes']._serialized_options = b'\xe0A\x06'
    _globals['_FULLHASH'].fields_by_name['full_hash_details']._loaded_options = None
    _globals['_FULLHASH'].fields_by_name['full_hash_details']._serialized_options = b'\xe0A\x06'
    _globals['_GETHASHLISTREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETHASHLISTREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList'
    _globals['_HASHLISTMETADATA'].fields_by_name['threat_types']._loaded_options = None
    _globals['_HASHLISTMETADATA'].fields_by_name['threat_types']._serialized_options = b'\xe0A\x06'
    _globals['_HASHLISTMETADATA'].fields_by_name['likely_safe_types']._loaded_options = None
    _globals['_HASHLISTMETADATA'].fields_by_name['likely_safe_types']._serialized_options = b'\xe0A\x06'
    _globals['_HASHLIST']._loaded_options = None
    _globals['_HASHLIST']._serialized_options = b'\xeaA=\n$safebrowsing.googleapis.com/HashList\x12\x15hashLists/{hash_list}'
    _globals['_BATCHGETHASHLISTSREQUEST'].fields_by_name['names']._loaded_options = None
    _globals['_BATCHGETHASHLISTSREQUEST'].fields_by_name['names']._serialized_options = b'\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList'
    _globals['_SAFEBROWSING']._loaded_options = None
    _globals['_SAFEBROWSING']._serialized_options = b'\xcaA\x1bsafebrowsing.googleapis.com'
    _globals['_SAFEBROWSING'].methods_by_name['SearchHashes']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['SearchHashes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x19\x12\x17/v5alpha1/hashes:search'
    _globals['_SAFEBROWSING'].methods_by_name['GetHashList']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['GetHashList']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x1b\x12\x19/v5alpha1/hashList/{name}'
    _globals['_SAFEBROWSING'].methods_by_name['ListHashLists']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['ListHashLists']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02\x15\x12\x13/v5alpha1/hashLists'
    _globals['_SAFEBROWSING'].methods_by_name['BatchGetHashLists']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['BatchGetHashLists']._serialized_options = b'\x82\xd3\xe4\x93\x02\x1e\x12\x1c/v5alpha1/hashLists:batchGet'
    _globals['_THREATTYPE']._serialized_start = 3306
    _globals['_THREATTYPE']._serialized_end = 3444
    _globals['_LIKELYSAFETYPE']._serialized_start = 3446
    _globals['_LIKELYSAFETYPE']._serialized_end = 3541
    _globals['_THREATATTRIBUTE']._serialized_start = 3543
    _globals['_THREATATTRIBUTE']._serialized_end = 3622
    _globals['_SEARCHHASHESREQUEST']._serialized_start = 246
    _globals['_SEARCHHASHESREQUEST']._serialized_end = 316
    _globals['_SEARCHHASHESRESPONSE']._serialized_start = 319
    _globals['_SEARCHHASHESRESPONSE']._serialized_end = 467
    _globals['_FULLHASH']._serialized_start = 470
    _globals['_FULLHASH']._serialized_end = 767
    _globals['_FULLHASH_FULLHASHDETAIL']._serialized_start = 598
    _globals['_FULLHASH_FULLHASHDETAIL']._serialized_end = 767
    _globals['_GETHASHLISTREQUEST']._serialized_start = 770
    _globals['_GETHASHLISTREQUEST']._serialized_end = 949
    _globals['_SIZECONSTRAINTS']._serialized_start = 951
    _globals['_SIZECONSTRAINTS']._serialized_end = 1026
    _globals['_RICEDELTAENCODED32BIT']._serialized_start = 1028
    _globals['_RICEDELTAENCODED32BIT']._serialized_end = 1141
    _globals['_RICEDELTAENCODED64BIT']._serialized_start = 1143
    _globals['_RICEDELTAENCODED64BIT']._serialized_end = 1256
    _globals['_RICEDELTAENCODED128BIT']._serialized_start = 1259
    _globals['_RICEDELTAENCODED128BIT']._serialized_end = 1400
    _globals['_RICEDELTAENCODED256BIT']._serialized_start = 1403
    _globals['_RICEDELTAENCODED256BIT']._serialized_end = 1626
    _globals['_HASHLISTMETADATA']._serialized_start = 1629
    _globals['_HASHLISTMETADATA']._serialized_end = 2039
    _globals['_HASHLISTMETADATA_HASHLENGTH']._serialized_start = 1924
    _globals['_HASHLISTMETADATA_HASHLENGTH']._serialized_end = 2039
    _globals['_HASHLIST']._serialized_start = 2042
    _globals['_HASHLIST']._serialized_end = 2834
    _globals['_BATCHGETHASHLISTSREQUEST']._serialized_start = 2837
    _globals['_BATCHGETHASHLISTSREQUEST']._serialized_end = 3023
    _globals['_BATCHGETHASHLISTSRESPONSE']._serialized_start = 3025
    _globals['_BATCHGETHASHLISTSRESPONSE']._serialized_end = 3121
    _globals['_LISTHASHLISTSREQUEST']._serialized_start = 3123
    _globals['_LISTHASHLISTSREQUEST']._serialized_end = 3184
    _globals['_LISTHASHLISTSRESPONSE']._serialized_start = 3186
    _globals['_LISTHASHLISTSRESPONSE']._serialized_end = 3303
    _globals['_SAFEBROWSING']._serialized_start = 3625
    _globals['_SAFEBROWSING']._serialized_end = 4372