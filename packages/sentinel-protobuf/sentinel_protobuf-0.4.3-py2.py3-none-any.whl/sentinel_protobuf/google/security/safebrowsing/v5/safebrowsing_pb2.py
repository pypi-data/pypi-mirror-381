"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/security/safebrowsing/v5/safebrowsing.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2google/security/safebrowsing/v5/safebrowsing.proto\x12\x1fgoogle.security.safebrowsing.v5\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1egoogle/protobuf/duration.proto"1\n\x13SearchHashesRequest\x12\x1a\n\rhash_prefixes\x18\x01 \x03(\x0cB\x03\xe0A\x02"\x8e\x01\n\x14SearchHashesResponse\x12C\n\x0bfull_hashes\x18\x01 \x03(\x0b2).google.security.safebrowsing.v5.FullHashB\x03\xe0A\x06\x121\n\x0ecache_duration\x18\x02 \x01(\x0b2\x19.google.protobuf.Duration"\x97\x02\n\x08FullHash\x12\x11\n\tfull_hash\x18\x01 \x01(\x0c\x12X\n\x11full_hash_details\x18\x02 \x03(\x0b28.google.security.safebrowsing.v5.FullHash.FullHashDetailB\x03\xe0A\x06\x1a\x9d\x01\n\x0eFullHashDetail\x12@\n\x0bthreat_type\x18\x01 \x01(\x0e2+.google.security.safebrowsing.v5.ThreatType\x12I\n\nattributes\x18\x02 \x03(\x0e20.google.security.safebrowsing.v5.ThreatAttributeB\x03\xe0A\x06"\xad\x01\n\x12GetHashListRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12J\n\x10size_constraints\x18\x04 \x01(\x0b20.google.security.safebrowsing.v5.SizeConstraints"K\n\x0fSizeConstraints\x12\x1a\n\x12max_update_entries\x18\x01 \x01(\x05\x12\x1c\n\x14max_database_entries\x18\x02 \x01(\x05"q\n\x15RiceDeltaEncoded32Bit\x12\x13\n\x0bfirst_value\x18\x01 \x01(\r\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x15\n\rentries_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c"q\n\x15RiceDeltaEncoded64Bit\x12\x13\n\x0bfirst_value\x18\x01 \x01(\x04\x12\x16\n\x0erice_parameter\x18\x02 \x01(\x05\x12\x15\n\rentries_count\x18\x03 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x04 \x01(\x0c"\x8d\x01\n\x16RiceDeltaEncoded128Bit\x12\x16\n\x0efirst_value_hi\x18\x01 \x01(\x04\x12\x16\n\x0efirst_value_lo\x18\x02 \x01(\x06\x12\x16\n\x0erice_parameter\x18\x03 \x01(\x05\x12\x15\n\rentries_count\x18\x04 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x05 \x01(\x0c"\xdf\x01\n\x16RiceDeltaEncoded256Bit\x12\x1e\n\x16first_value_first_part\x18\x01 \x01(\x04\x12\x1f\n\x17first_value_second_part\x18\x02 \x01(\x06\x12\x1e\n\x16first_value_third_part\x18\x03 \x01(\x06\x12\x1f\n\x17first_value_fourth_part\x18\x04 \x01(\x06\x12\x16\n\x0erice_parameter\x18\x05 \x01(\x05\x12\x15\n\rentries_count\x18\x06 \x01(\x05\x12\x14\n\x0cencoded_data\x18\x07 \x01(\x0c"\x88\x03\n\x10HashListMetadata\x12F\n\x0cthreat_types\x18\x01 \x03(\x0e2+.google.security.safebrowsing.v5.ThreatTypeB\x03\xe0A\x06\x12O\n\x11likely_safe_types\x18\x02 \x03(\x0e2/.google.security.safebrowsing.v5.LikelySafeTypeB\x03\xe0A\x06\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12Q\n\x0bhash_length\x18\x06 \x01(\x0e2<.google.security.safebrowsing.v5.HashListMetadata.HashLength"s\n\nHashLength\x12\x1b\n\x17HASH_LENGTH_UNSPECIFIED\x10\x00\x12\x0e\n\nFOUR_BYTES\x10\x02\x12\x0f\n\x0bEIGHT_BYTES\x10\x03\x12\x11\n\rSIXTEEN_BYTES\x10\x04\x12\x14\n\x10THIRTY_TWO_BYTES\x10\x05"\xf4\x05\n\x08HashList\x12V\n\x14additions_four_bytes\x18\x04 \x01(\x0b26.google.security.safebrowsing.v5.RiceDeltaEncoded32BitH\x00\x12W\n\x15additions_eight_bytes\x18\t \x01(\x0b26.google.security.safebrowsing.v5.RiceDeltaEncoded64BitH\x00\x12Z\n\x17additions_sixteen_bytes\x18\n \x01(\x0b27.google.security.safebrowsing.v5.RiceDeltaEncoded128BitH\x00\x12]\n\x1aadditions_thirty_two_bytes\x18\x0b \x01(\x0b27.google.security.safebrowsing.v5.RiceDeltaEncoded256BitH\x00\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x0c\x12\x16\n\x0epartial_update\x18\x03 \x01(\x08\x12S\n\x13compressed_removals\x18\x05 \x01(\x0b26.google.security.safebrowsing.v5.RiceDeltaEncoded32Bit\x128\n\x15minimum_wait_duration\x18\x06 \x01(\x0b2\x19.google.protobuf.Duration\x12\x17\n\x0fsha256_checksum\x18\x07 \x01(\x0c\x12C\n\x08metadata\x18\x08 \x01(\x0b21.google.security.safebrowsing.v5.HashListMetadata:@\xeaA=\n$safebrowsing.googleapis.com/HashList\x12\x15hashLists/{hash_list}B\x16\n\x14compressed_additions"\xb4\x01\n\x18BatchGetHashListsRequest\x12;\n\x05names\x18\x01 \x03(\tB,\xe0A\x02\xfaA&\n$safebrowsing.googleapis.com/HashList\x12\x0f\n\x07version\x18\x02 \x03(\x0c\x12J\n\x10size_constraints\x18\x04 \x01(\x0b20.google.security.safebrowsing.v5.SizeConstraints"Z\n\x19BatchGetHashListsResponse\x12=\n\nhash_lists\x18\x01 \x03(\x0b2).google.security.safebrowsing.v5.HashList"=\n\x14ListHashListsRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x12\n\npage_token\x18\x02 \x01(\t"o\n\x15ListHashListsResponse\x12=\n\nhash_lists\x18\x01 \x03(\x0b2).google.security.safebrowsing.v5.HashList\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*\x8a\x01\n\nThreatType\x12\x1b\n\x17THREAT_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07MALWARE\x10\x01\x12\x16\n\x12SOCIAL_ENGINEERING\x10\x02\x12\x15\n\x11UNWANTED_SOFTWARE\x10\x03\x12#\n\x1fPOTENTIALLY_HARMFUL_APPLICATION\x10\x04*_\n\x0eLikelySafeType\x12 \n\x1cLIKELY_SAFE_TYPE_UNSPECIFIED\x10\x00\x12\x14\n\x10GENERAL_BROWSING\x10\x01\x12\x07\n\x03CSD\x10\x02\x12\x0c\n\x08DOWNLOAD\x10\x03*O\n\x0fThreatAttribute\x12 \n\x1cTHREAT_ATTRIBUTE_UNSPECIFIED\x10\x00\x12\n\n\x06CANARY\x10\x01\x12\x0e\n\nFRAME_ONLY\x10\x022\xa3\x05\n\x0cSafeBrowsing\x12\x96\x01\n\x0cSearchHashes\x124.google.security.safebrowsing.v5.SearchHashesRequest\x1a5.google.security.safebrowsing.v5.SearchHashesResponse"\x19\x82\xd3\xe4\x93\x02\x13\x12\x11/v5/hashes:search\x12\x91\x01\n\x0bGetHashList\x123.google.security.safebrowsing.v5.GetHashListRequest\x1a).google.security.safebrowsing.v5.HashList""\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v5/hashList/{name}\x12\x98\x01\n\rListHashLists\x125.google.security.safebrowsing.v5.ListHashListsRequest\x1a6.google.security.safebrowsing.v5.ListHashListsResponse"\x18\xdaA\x00\x82\xd3\xe4\x93\x02\x0f\x12\r/v5/hashLists\x12\xaa\x01\n\x11BatchGetHashLists\x129.google.security.safebrowsing.v5.BatchGetHashListsRequest\x1a:.google.security.safebrowsing.v5.BatchGetHashListsResponse"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v5/hashLists:batchGet\x1a\x1e\xcaA\x1bsafebrowsing.googleapis.comB\x87\x01\n#com.google.security.safebrowsing.v5B\x11SafeBrowsingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/security/safebrowsing/v5;safebrowsingb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.security.safebrowsing.v5.safebrowsing_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n#com.google.security.safebrowsing.v5B\x11SafeBrowsingProtoP\x01ZKgoogle.golang.org/genproto/googleapis/security/safebrowsing/v5;safebrowsing'
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['hash_prefixes']._loaded_options = None
    _globals['_SEARCHHASHESREQUEST'].fields_by_name['hash_prefixes']._serialized_options = b'\xe0A\x02'
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
    _globals['_SAFEBROWSING'].methods_by_name['SearchHashes']._serialized_options = b'\x82\xd3\xe4\x93\x02\x13\x12\x11/v5/hashes:search'
    _globals['_SAFEBROWSING'].methods_by_name['GetHashList']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['GetHashList']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02\x15\x12\x13/v5/hashList/{name}'
    _globals['_SAFEBROWSING'].methods_by_name['ListHashLists']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['ListHashLists']._serialized_options = b'\xdaA\x00\x82\xd3\xe4\x93\x02\x0f\x12\r/v5/hashLists'
    _globals['_SAFEBROWSING'].methods_by_name['BatchGetHashLists']._loaded_options = None
    _globals['_SAFEBROWSING'].methods_by_name['BatchGetHashLists']._serialized_options = b'\x82\xd3\xe4\x93\x02\x18\x12\x16/v5/hashLists:batchGet'
    _globals['_THREATTYPE']._serialized_start = 3171
    _globals['_THREATTYPE']._serialized_end = 3309
    _globals['_LIKELYSAFETYPE']._serialized_start = 3311
    _globals['_LIKELYSAFETYPE']._serialized_end = 3406
    _globals['_THREATATTRIBUTE']._serialized_start = 3408
    _globals['_THREATATTRIBUTE']._serialized_end = 3487
    _globals['_SEARCHHASHESREQUEST']._serialized_start = 234
    _globals['_SEARCHHASHESREQUEST']._serialized_end = 283
    _globals['_SEARCHHASHESRESPONSE']._serialized_start = 286
    _globals['_SEARCHHASHESRESPONSE']._serialized_end = 428
    _globals['_FULLHASH']._serialized_start = 431
    _globals['_FULLHASH']._serialized_end = 710
    _globals['_FULLHASH_FULLHASHDETAIL']._serialized_start = 553
    _globals['_FULLHASH_FULLHASHDETAIL']._serialized_end = 710
    _globals['_GETHASHLISTREQUEST']._serialized_start = 713
    _globals['_GETHASHLISTREQUEST']._serialized_end = 886
    _globals['_SIZECONSTRAINTS']._serialized_start = 888
    _globals['_SIZECONSTRAINTS']._serialized_end = 963
    _globals['_RICEDELTAENCODED32BIT']._serialized_start = 965
    _globals['_RICEDELTAENCODED32BIT']._serialized_end = 1078
    _globals['_RICEDELTAENCODED64BIT']._serialized_start = 1080
    _globals['_RICEDELTAENCODED64BIT']._serialized_end = 1193
    _globals['_RICEDELTAENCODED128BIT']._serialized_start = 1196
    _globals['_RICEDELTAENCODED128BIT']._serialized_end = 1337
    _globals['_RICEDELTAENCODED256BIT']._serialized_start = 1340
    _globals['_RICEDELTAENCODED256BIT']._serialized_end = 1563
    _globals['_HASHLISTMETADATA']._serialized_start = 1566
    _globals['_HASHLISTMETADATA']._serialized_end = 1958
    _globals['_HASHLISTMETADATA_HASHLENGTH']._serialized_start = 1843
    _globals['_HASHLISTMETADATA_HASHLENGTH']._serialized_end = 1958
    _globals['_HASHLIST']._serialized_start = 1961
    _globals['_HASHLIST']._serialized_end = 2717
    _globals['_BATCHGETHASHLISTSREQUEST']._serialized_start = 2720
    _globals['_BATCHGETHASHLISTSREQUEST']._serialized_end = 2900
    _globals['_BATCHGETHASHLISTSRESPONSE']._serialized_start = 2902
    _globals['_BATCHGETHASHLISTSRESPONSE']._serialized_end = 2992
    _globals['_LISTHASHLISTSREQUEST']._serialized_start = 2994
    _globals['_LISTHASHLISTSREQUEST']._serialized_end = 3055
    _globals['_LISTHASHLISTSRESPONSE']._serialized_start = 3057
    _globals['_LISTHASHLISTSRESPONSE']._serialized_end = 3168
    _globals['_SAFEBROWSING']._serialized_start = 3490
    _globals['_SAFEBROWSING']._serialized_end = 4165