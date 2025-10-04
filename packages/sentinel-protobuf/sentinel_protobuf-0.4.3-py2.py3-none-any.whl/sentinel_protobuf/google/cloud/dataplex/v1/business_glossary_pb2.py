"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/dataplex/v1/business_glossary.proto')
_sym_db = _symbol_database.Default()
from .....google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from .....google.api import client_pb2 as google_dot_api_dot_client__pb2
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import field_info_pb2 as google_dot_api_dot_field__info__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from .....google.cloud.dataplex.v1 import service_pb2 as google_dot_cloud_dot_dataplex_dot_v1_dot_service__pb2
from .....google.longrunning import operations_pb2 as google_dot_longrunning_dot_operations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n0google/cloud/dataplex/v1/business_glossary.proto\x12\x18google.cloud.dataplex.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x17google/api/client.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1bgoogle/api/field_info.proto\x1a\x19google/api/resource.proto\x1a&google/cloud/dataplex/v1/service.proto\x1a#google/longrunning/operations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x94\x04\n\x08Glossary\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12C\n\x06labels\x18\x07 \x03(\x0b2..google.cloud.dataplex.v1.Glossary.LabelsEntryB\x03\xe0A\x01\x12\x17\n\nterm_count\x18\x08 \x01(\x05B\x03\xe0A\x03\x12\x1b\n\x0ecategory_count\x18\t \x01(\x05B\x03\xe0A\x03\x12\x11\n\x04etag\x18\n \x01(\tB\x03\xe0A\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:z\xeaAw\n dataplex.googleapis.com/Glossary\x12=projects/{project}/locations/{location}/glossaries/{glossary}*\nglossaries2\x08glossary"\x99\x04\n\x10GlossaryCategory\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\x06labels\x18\x07 \x03(\x0b26.google.cloud.dataplex.v1.GlossaryCategory.LabelsEntryB\x03\xe0A\x01\x12\x13\n\x06parent\x18\x08 \x01(\tB\x03\xe0A\x02\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\xa2\x01\xeaA\x9e\x01\n(dataplex.googleapis.com/GlossaryCategory\x12\\projects/{project}/locations/{location}/glossaries/{glossary}/categories/{glossary_category}*\ncategories2\x08category"\xa0\x04\n\x0cGlossaryTerm\x12\x14\n\x04name\x18\x01 \x01(\tB\x06\xe0A\x03\xe0A\x08\x12\x18\n\x03uid\x18\x02 \x01(\tB\x0b\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01\x12\x19\n\x0cdisplay_name\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x04 \x01(\tB\x03\xe0A\x01\x124\n\x0bcreate_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\x06 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12G\n\x06labels\x18\x07 \x03(\x0b22.google.cloud.dataplex.v1.GlossaryTerm.LabelsEntryB\x03\xe0A\x01\x128\n\x06parent\x18\x08 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x028\x01:\x8c\x01\xeaA\x88\x01\n$dataplex.googleapis.com/GlossaryTerm\x12Sprojects/{project}/locations/{location}/glossaries/{glossary}/terms/{glossary_term}*\x05terms2\x04term"\xc3\x01\n\x15CreateGlossaryRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x18\n\x0bglossary_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x08glossary\x18\x03 \x01(\x0b2".google.cloud.dataplex.v1.GlossaryB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x04 \x01(\x08B\x03\xe0A\x01"\xa4\x01\n\x15UpdateGlossaryRequest\x129\n\x08glossary\x18\x01 \x01(\x0b2".google.cloud.dataplex.v1.GlossaryB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02\x12\x1a\n\rvalidate_only\x18\x03 \x01(\x08B\x03\xe0A\x01"b\n\x15DeleteGlossaryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x12\x11\n\x04etag\x18\x02 \x01(\tB\x03\xe0A\x01"L\n\x12GetGlossaryRequest\x126\n\x04name\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary"\xaf\x01\n\x15ListGlossariesRequest\x129\n\x06parent\x18\x01 \x01(\tB)\xe0A\x02\xfaA#\n!locations.googleapis.com/Location\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x88\x01\n\x16ListGlossariesResponse\x126\n\nglossaries\x18\x01 \x03(\x0b2".google.cloud.dataplex.v1.Glossary\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1d\n\x15unreachable_locations\x18\x03 \x03(\t"\xb6\x01\n\x1dCreateGlossaryCategoryRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x12\x18\n\x0bcategory_id\x18\x02 \x01(\tB\x03\xe0A\x02\x12A\n\x08category\x18\x03 \x01(\x0b2*.google.cloud.dataplex.v1.GlossaryCategoryB\x03\xe0A\x02"\x98\x01\n\x1dUpdateGlossaryCategoryRequest\x12A\n\x08category\x18\x01 \x01(\x0b2*.google.cloud.dataplex.v1.GlossaryCategoryB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"_\n\x1dDeleteGlossaryCategoryRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dataplex.googleapis.com/GlossaryCategory"\\\n\x1aGetGlossaryCategoryRequest\x12>\n\x04name\x18\x01 \x01(\tB0\xe0A\x02\xfaA*\n(dataplex.googleapis.com/GlossaryCategory"\xb6\x01\n\x1dListGlossaryCategoriesRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x98\x01\n\x1eListGlossaryCategoriesResponse\x12>\n\ncategories\x18\x01 \x03(\x0b2*.google.cloud.dataplex.v1.GlossaryCategory\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1d\n\x15unreachable_locations\x18\x03 \x03(\t"\xa6\x01\n\x19CreateGlossaryTermRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x12\x14\n\x07term_id\x18\x02 \x01(\tB\x03\xe0A\x02\x129\n\x04term\x18\x03 \x01(\x0b2&.google.cloud.dataplex.v1.GlossaryTermB\x03\xe0A\x02"\x8c\x01\n\x19UpdateGlossaryTermRequest\x129\n\x04term\x18\x01 \x01(\x0b2&.google.cloud.dataplex.v1.GlossaryTermB\x03\xe0A\x02\x124\n\x0bupdate_mask\x18\x02 \x01(\x0b2\x1a.google.protobuf.FieldMaskB\x03\xe0A\x02"W\n\x19DeleteGlossaryTermRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dataplex.googleapis.com/GlossaryTerm"T\n\x16GetGlossaryTermRequest\x12:\n\x04name\x18\x01 \x01(\tB,\xe0A\x02\xfaA&\n$dataplex.googleapis.com/GlossaryTerm"\xb1\x01\n\x18ListGlossaryTermsRequest\x128\n\x06parent\x18\x01 \x01(\tB(\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary\x12\x16\n\tpage_size\x18\x02 \x01(\x05B\x03\xe0A\x01\x12\x17\n\npage_token\x18\x03 \x01(\tB\x03\xe0A\x01\x12\x13\n\x06filter\x18\x04 \x01(\tB\x03\xe0A\x01\x12\x15\n\x08order_by\x18\x05 \x01(\tB\x03\xe0A\x01"\x8a\x01\n\x19ListGlossaryTermsResponse\x125\n\x05terms\x18\x01 \x03(\x0b2&.google.cloud.dataplex.v1.GlossaryTerm\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\x12\x1d\n\x15unreachable_locations\x18\x03 \x03(\t2\xd6\x18\n\x17BusinessGlossaryService\x12\xe0\x01\n\x0eCreateGlossary\x12/.google.cloud.dataplex.v1.CreateGlossaryRequest\x1a\x1d.google.longrunning.Operation"~\xcaA\x1d\n\x08Glossary\x12\x11OperationMetadata\xdaA\x1bparent,glossary,glossary_id\x82\xd3\xe4\x93\x02:"./v1/{parent=projects/*/locations/*}/glossaries:\x08glossary\x12\xe3\x01\n\x0eUpdateGlossary\x12/.google.cloud.dataplex.v1.UpdateGlossaryRequest\x1a\x1d.google.longrunning.Operation"\x80\x01\xcaA\x1d\n\x08Glossary\x12\x11OperationMetadata\xdaA\x14glossary,update_mask\x82\xd3\xe4\x93\x02C27/v1/{glossary.name=projects/*/locations/*/glossaries/*}:\x08glossary\x12\xcc\x01\n\x0eDeleteGlossary\x12/.google.cloud.dataplex.v1.DeleteGlossaryRequest\x1a\x1d.google.longrunning.Operation"j\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/glossaries/*}\x12\x9e\x01\n\x0bGetGlossary\x12,.google.cloud.dataplex.v1.GetGlossaryRequest\x1a".google.cloud.dataplex.v1.Glossary"=\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/glossaries/*}\x12\xb4\x01\n\x0eListGlossaries\x12/.google.cloud.dataplex.v1.ListGlossariesRequest\x1a0.google.cloud.dataplex.v1.ListGlossariesResponse"?\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/glossaries\x12\xea\x01\n\x16CreateGlossaryCategory\x127.google.cloud.dataplex.v1.CreateGlossaryCategoryRequest\x1a*.google.cloud.dataplex.v1.GlossaryCategory"k\xdaA\x1bparent,category,category_id\x82\xd3\xe4\x93\x02G";/v1/{parent=projects/*/locations/*/glossaries/*}/categories:\x08category\x12\xec\x01\n\x16UpdateGlossaryCategory\x127.google.cloud.dataplex.v1.UpdateGlossaryCategoryRequest\x1a*.google.cloud.dataplex.v1.GlossaryCategory"m\xdaA\x14category,update_mask\x82\xd3\xe4\x93\x02P2D/v1/{category.name=projects/*/locations/*/glossaries/*/categories/*}:\x08category\x12\xb5\x01\n\x16DeleteGlossaryCategory\x127.google.cloud.dataplex.v1.DeleteGlossaryCategoryRequest\x1a\x16.google.protobuf.Empty"J\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/glossaries/*/categories/*}\x12\xc3\x01\n\x13GetGlossaryCategory\x124.google.cloud.dataplex.v1.GetGlossaryCategoryRequest\x1a*.google.cloud.dataplex.v1.GlossaryCategory"J\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/glossaries/*/categories/*}\x12\xd9\x01\n\x16ListGlossaryCategories\x127.google.cloud.dataplex.v1.ListGlossaryCategoriesRequest\x1a8.google.cloud.dataplex.v1.ListGlossaryCategoriesResponse"L\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/glossaries/*}/categories\x12\xcd\x01\n\x12CreateGlossaryTerm\x123.google.cloud.dataplex.v1.CreateGlossaryTermRequest\x1a&.google.cloud.dataplex.v1.GlossaryTerm"Z\xdaA\x13parent,term,term_id\x82\xd3\xe4\x93\x02>"6/v1/{parent=projects/*/locations/*/glossaries/*}/terms:\x04term\x12\xcf\x01\n\x12UpdateGlossaryTerm\x123.google.cloud.dataplex.v1.UpdateGlossaryTermRequest\x1a&.google.cloud.dataplex.v1.GlossaryTerm"\\\xdaA\x10term,update_mask\x82\xd3\xe4\x93\x02C2;/v1/{term.name=projects/*/locations/*/glossaries/*/terms/*}:\x04term\x12\xa8\x01\n\x12DeleteGlossaryTerm\x123.google.cloud.dataplex.v1.DeleteGlossaryTermRequest\x1a\x16.google.protobuf.Empty"E\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=projects/*/locations/*/glossaries/*/terms/*}\x12\xb2\x01\n\x0fGetGlossaryTerm\x120.google.cloud.dataplex.v1.GetGlossaryTermRequest\x1a&.google.cloud.dataplex.v1.GlossaryTerm"E\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/glossaries/*/terms/*}\x12\xc5\x01\n\x11ListGlossaryTerms\x122.google.cloud.dataplex.v1.ListGlossaryTermsRequest\x1a3.google.cloud.dataplex.v1.ListGlossaryTermsResponse"G\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*/glossaries/*}/terms\x1aK\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platformBq\n\x1ccom.google.cloud.dataplex.v1B\x15BusinessGlossaryProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.dataplex.v1.business_glossary_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ccom.google.cloud.dataplex.v1B\x15BusinessGlossaryProtoP\x01Z8cloud.google.com/go/dataplex/apiv1/dataplexpb;dataplexpb'
    _globals['_GLOSSARY_LABELSENTRY']._loaded_options = None
    _globals['_GLOSSARY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GLOSSARY'].fields_by_name['name']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_GLOSSARY'].fields_by_name['uid']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GLOSSARY'].fields_by_name['display_name']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARY'].fields_by_name['description']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARY'].fields_by_name['create_time']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARY'].fields_by_name['update_time']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARY'].fields_by_name['labels']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARY'].fields_by_name['term_count']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['term_count']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARY'].fields_by_name['category_count']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['category_count']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARY'].fields_by_name['etag']._loaded_options = None
    _globals['_GLOSSARY'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARY']._loaded_options = None
    _globals['_GLOSSARY']._serialized_options = b'\xeaAw\n dataplex.googleapis.com/Glossary\x12=projects/{project}/locations/{location}/glossaries/{glossary}*\nglossaries2\x08glossary'
    _globals['_GLOSSARYCATEGORY_LABELSENTRY']._loaded_options = None
    _globals['_GLOSSARYCATEGORY_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['name']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['uid']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['display_name']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['description']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['create_time']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['update_time']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['labels']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYCATEGORY'].fields_by_name['parent']._loaded_options = None
    _globals['_GLOSSARYCATEGORY'].fields_by_name['parent']._serialized_options = b'\xe0A\x02'
    _globals['_GLOSSARYCATEGORY']._loaded_options = None
    _globals['_GLOSSARYCATEGORY']._serialized_options = b'\xeaA\x9e\x01\n(dataplex.googleapis.com/GlossaryCategory\x12\\projects/{project}/locations/{location}/glossaries/{glossary}/categories/{glossary_category}*\ncategories2\x08category'
    _globals['_GLOSSARYTERM_LABELSENTRY']._loaded_options = None
    _globals['_GLOSSARYTERM_LABELSENTRY']._serialized_options = b'8\x01'
    _globals['_GLOSSARYTERM'].fields_by_name['name']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['name']._serialized_options = b'\xe0A\x03\xe0A\x08'
    _globals['_GLOSSARYTERM'].fields_by_name['uid']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['uid']._serialized_options = b'\xe0A\x03\xe2\x8c\xcf\xd7\x08\x02\x08\x01'
    _globals['_GLOSSARYTERM'].fields_by_name['display_name']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYTERM'].fields_by_name['description']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYTERM'].fields_by_name['create_time']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARYTERM'].fields_by_name['update_time']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_GLOSSARYTERM'].fields_by_name['labels']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['labels']._serialized_options = b'\xe0A\x01'
    _globals['_GLOSSARYTERM'].fields_by_name['parent']._loaded_options = None
    _globals['_GLOSSARYTERM'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_GLOSSARYTERM']._loaded_options = None
    _globals['_GLOSSARYTERM']._serialized_options = b'\xeaA\x88\x01\n$dataplex.googleapis.com/GlossaryTerm\x12Sprojects/{project}/locations/{location}/glossaries/{glossary}/terms/{glossary_term}*\x05terms2\x04term'
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['glossary_id']._loaded_options = None
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['glossary_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['glossary']._loaded_options = None
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['glossary']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_CREATEGLOSSARYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['glossary']._loaded_options = None
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['glossary']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['validate_only']._loaded_options = None
    _globals['_UPDATEGLOSSARYREQUEST'].fields_by_name['validate_only']._serialized_options = b'\xe0A\x01'
    _globals['_DELETEGLOSSARYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGLOSSARYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_DELETEGLOSSARYREQUEST'].fields_by_name['etag']._loaded_options = None
    _globals['_DELETEGLOSSARYREQUEST'].fields_by_name['etag']._serialized_options = b'\xe0A\x01'
    _globals['_GETGLOSSARYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGLOSSARYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA#\n!locations.googleapis.com/Location'
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTGLOSSARIESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category_id']._loaded_options = None
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category']._loaded_options = None
    _globals['_CREATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category']._loaded_options = None
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST'].fields_by_name['category']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGLOSSARYCATEGORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGLOSSARYCATEGORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dataplex.googleapis.com/GlossaryCategory'
    _globals['_GETGLOSSARYCATEGORYREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGLOSSARYCATEGORYREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA*\n(dataplex.googleapis.com/GlossaryCategory'
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTGLOSSARYCATEGORIESREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['term_id']._loaded_options = None
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['term_id']._serialized_options = b'\xe0A\x02'
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['term']._loaded_options = None
    _globals['_CREATEGLOSSARYTERMREQUEST'].fields_by_name['term']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYTERMREQUEST'].fields_by_name['term']._loaded_options = None
    _globals['_UPDATEGLOSSARYTERMREQUEST'].fields_by_name['term']._serialized_options = b'\xe0A\x02'
    _globals['_UPDATEGLOSSARYTERMREQUEST'].fields_by_name['update_mask']._loaded_options = None
    _globals['_UPDATEGLOSSARYTERMREQUEST'].fields_by_name['update_mask']._serialized_options = b'\xe0A\x02'
    _globals['_DELETEGLOSSARYTERMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_DELETEGLOSSARYTERMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dataplex.googleapis.com/GlossaryTerm'
    _globals['_GETGLOSSARYTERMREQUEST'].fields_by_name['name']._loaded_options = None
    _globals['_GETGLOSSARYTERMREQUEST'].fields_by_name['name']._serialized_options = b'\xe0A\x02\xfaA&\n$dataplex.googleapis.com/GlossaryTerm'
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['parent']._loaded_options = None
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['parent']._serialized_options = b'\xe0A\x02\xfaA"\n dataplex.googleapis.com/Glossary'
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['page_size']._loaded_options = None
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['page_size']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['page_token']._loaded_options = None
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['page_token']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['filter']._loaded_options = None
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['filter']._serialized_options = b'\xe0A\x01'
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['order_by']._loaded_options = None
    _globals['_LISTGLOSSARYTERMSREQUEST'].fields_by_name['order_by']._serialized_options = b'\xe0A\x01'
    _globals['_BUSINESSGLOSSARYSERVICE']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE']._serialized_options = b'\xcaA\x17dataplex.googleapis.com\xd2A.https://www.googleapis.com/auth/cloud-platform'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossary']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossary']._serialized_options = b'\xcaA\x1d\n\x08Glossary\x12\x11OperationMetadata\xdaA\x1bparent,glossary,glossary_id\x82\xd3\xe4\x93\x02:"./v1/{parent=projects/*/locations/*}/glossaries:\x08glossary'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossary']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossary']._serialized_options = b'\xcaA\x1d\n\x08Glossary\x12\x11OperationMetadata\xdaA\x14glossary,update_mask\x82\xd3\xe4\x93\x02C27/v1/{glossary.name=projects/*/locations/*/glossaries/*}:\x08glossary'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossary']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossary']._serialized_options = b'\xcaA*\n\x15google.protobuf.Empty\x12\x11OperationMetadata\xdaA\x04name\x82\xd3\xe4\x93\x020*./v1/{name=projects/*/locations/*/glossaries/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossary']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossary']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x020\x12./v1/{name=projects/*/locations/*/glossaries/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaries']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaries']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x020\x12./v1/{parent=projects/*/locations/*}/glossaries'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossaryCategory']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossaryCategory']._serialized_options = b'\xdaA\x1bparent,category,category_id\x82\xd3\xe4\x93\x02G";/v1/{parent=projects/*/locations/*/glossaries/*}/categories:\x08category'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossaryCategory']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossaryCategory']._serialized_options = b'\xdaA\x14category,update_mask\x82\xd3\xe4\x93\x02P2D/v1/{category.name=projects/*/locations/*/glossaries/*/categories/*}:\x08category'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossaryCategory']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossaryCategory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=*;/v1/{name=projects/*/locations/*/glossaries/*/categories/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossaryCategory']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossaryCategory']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x02=\x12;/v1/{name=projects/*/locations/*/glossaries/*/categories/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaryCategories']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaryCategories']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x02=\x12;/v1/{parent=projects/*/locations/*/glossaries/*}/categories'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossaryTerm']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['CreateGlossaryTerm']._serialized_options = b'\xdaA\x13parent,term,term_id\x82\xd3\xe4\x93\x02>"6/v1/{parent=projects/*/locations/*/glossaries/*}/terms:\x04term'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossaryTerm']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['UpdateGlossaryTerm']._serialized_options = b'\xdaA\x10term,update_mask\x82\xd3\xe4\x93\x02C2;/v1/{term.name=projects/*/locations/*/glossaries/*/terms/*}:\x04term'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossaryTerm']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['DeleteGlossaryTerm']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028*6/v1/{name=projects/*/locations/*/glossaries/*/terms/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossaryTerm']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['GetGlossaryTerm']._serialized_options = b'\xdaA\x04name\x82\xd3\xe4\x93\x028\x126/v1/{name=projects/*/locations/*/glossaries/*/terms/*}'
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaryTerms']._loaded_options = None
    _globals['_BUSINESSGLOSSARYSERVICE'].methods_by_name['ListGlossaryTerms']._serialized_options = b'\xdaA\x06parent\x82\xd3\xe4\x93\x028\x126/v1/{parent=projects/*/locations/*/glossaries/*}/terms'
    _globals['_GLOSSARY']._serialized_start = 396
    _globals['_GLOSSARY']._serialized_end = 928
    _globals['_GLOSSARY_LABELSENTRY']._serialized_start = 759
    _globals['_GLOSSARY_LABELSENTRY']._serialized_end = 804
    _globals['_GLOSSARYCATEGORY']._serialized_start = 931
    _globals['_GLOSSARYCATEGORY']._serialized_end = 1468
    _globals['_GLOSSARYCATEGORY_LABELSENTRY']._serialized_start = 759
    _globals['_GLOSSARYCATEGORY_LABELSENTRY']._serialized_end = 804
    _globals['_GLOSSARYTERM']._serialized_start = 1471
    _globals['_GLOSSARYTERM']._serialized_end = 2015
    _globals['_GLOSSARYTERM_LABELSENTRY']._serialized_start = 759
    _globals['_GLOSSARYTERM_LABELSENTRY']._serialized_end = 804
    _globals['_CREATEGLOSSARYREQUEST']._serialized_start = 2018
    _globals['_CREATEGLOSSARYREQUEST']._serialized_end = 2213
    _globals['_UPDATEGLOSSARYREQUEST']._serialized_start = 2216
    _globals['_UPDATEGLOSSARYREQUEST']._serialized_end = 2380
    _globals['_DELETEGLOSSARYREQUEST']._serialized_start = 2382
    _globals['_DELETEGLOSSARYREQUEST']._serialized_end = 2480
    _globals['_GETGLOSSARYREQUEST']._serialized_start = 2482
    _globals['_GETGLOSSARYREQUEST']._serialized_end = 2558
    _globals['_LISTGLOSSARIESREQUEST']._serialized_start = 2561
    _globals['_LISTGLOSSARIESREQUEST']._serialized_end = 2736
    _globals['_LISTGLOSSARIESRESPONSE']._serialized_start = 2739
    _globals['_LISTGLOSSARIESRESPONSE']._serialized_end = 2875
    _globals['_CREATEGLOSSARYCATEGORYREQUEST']._serialized_start = 2878
    _globals['_CREATEGLOSSARYCATEGORYREQUEST']._serialized_end = 3060
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST']._serialized_start = 3063
    _globals['_UPDATEGLOSSARYCATEGORYREQUEST']._serialized_end = 3215
    _globals['_DELETEGLOSSARYCATEGORYREQUEST']._serialized_start = 3217
    _globals['_DELETEGLOSSARYCATEGORYREQUEST']._serialized_end = 3312
    _globals['_GETGLOSSARYCATEGORYREQUEST']._serialized_start = 3314
    _globals['_GETGLOSSARYCATEGORYREQUEST']._serialized_end = 3406
    _globals['_LISTGLOSSARYCATEGORIESREQUEST']._serialized_start = 3409
    _globals['_LISTGLOSSARYCATEGORIESREQUEST']._serialized_end = 3591
    _globals['_LISTGLOSSARYCATEGORIESRESPONSE']._serialized_start = 3594
    _globals['_LISTGLOSSARYCATEGORIESRESPONSE']._serialized_end = 3746
    _globals['_CREATEGLOSSARYTERMREQUEST']._serialized_start = 3749
    _globals['_CREATEGLOSSARYTERMREQUEST']._serialized_end = 3915
    _globals['_UPDATEGLOSSARYTERMREQUEST']._serialized_start = 3918
    _globals['_UPDATEGLOSSARYTERMREQUEST']._serialized_end = 4058
    _globals['_DELETEGLOSSARYTERMREQUEST']._serialized_start = 4060
    _globals['_DELETEGLOSSARYTERMREQUEST']._serialized_end = 4147
    _globals['_GETGLOSSARYTERMREQUEST']._serialized_start = 4149
    _globals['_GETGLOSSARYTERMREQUEST']._serialized_end = 4233
    _globals['_LISTGLOSSARYTERMSREQUEST']._serialized_start = 4236
    _globals['_LISTGLOSSARYTERMSREQUEST']._serialized_end = 4413
    _globals['_LISTGLOSSARYTERMSRESPONSE']._serialized_start = 4416
    _globals['_LISTGLOSSARYTERMSRESPONSE']._serialized_end = 4554
    _globals['_BUSINESSGLOSSARYSERVICE']._serialized_start = 4557
    _globals['_BUSINESSGLOSSARYSERVICE']._serialized_end = 7715