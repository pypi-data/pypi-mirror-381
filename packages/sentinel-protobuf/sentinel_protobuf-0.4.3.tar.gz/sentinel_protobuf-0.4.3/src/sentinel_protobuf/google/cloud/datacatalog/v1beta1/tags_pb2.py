"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/datacatalog/v1beta1/tags.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n+google/cloud/datacatalog/v1beta1/tags.proto\x12 google.cloud.datacatalog.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\x95\x03\n\x03Tag\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x15\n\x08template\x18\x02 \x01(\tB\x03\xe0A\x02\x12"\n\x15template_display_name\x18\x05 \x01(\tB\x03\xe0A\x03\x12\x10\n\x06column\x18\x04 \x01(\tH\x00\x12F\n\x06fields\x18\x03 \x03(\x0b21.google.cloud.datacatalog.v1beta1.Tag.FieldsEntryB\x03\xe0A\x02\x1aY\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x129\n\x05value\x18\x02 \x01(\x0b2*.google.cloud.datacatalog.v1beta1.TagField:\x028\x01:\x81\x01\xeaA~\n\x1edatacatalog.googleapis.com/Tag\x12\\projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}B\x07\n\x05scope"\xad\x02\n\x08TagField\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x16\n\x0cdouble_value\x18\x02 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x03 \x01(\tH\x00\x12\x14\n\nbool_value\x18\x04 \x01(\x08H\x00\x125\n\x0ftimestamp_value\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampH\x00\x12J\n\nenum_value\x18\x06 \x01(\x0b24.google.cloud.datacatalog.v1beta1.TagField.EnumValueH\x00\x12\x12\n\x05order\x18\x07 \x01(\x05B\x03\xe0A\x03\x1a!\n\tEnumValue\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\tB\x06\n\x04kind"\x9e\x04\n\x0bTagTemplate\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12\x14\n\x0cdisplay_name\x18\x02 \x01(\t\x12N\n\x06fields\x18\x03 \x03(\x0b29.google.cloud.datacatalog.v1beta1.TagTemplate.FieldsEntryB\x03\xe0A\x02\x12k\n\x18dataplex_transfer_status\x18\x07 \x01(\x0e2D.google.cloud.datacatalog.v1beta1.TagTemplate.DataplexTransferStatusB\x03\xe0A\x03\x1aa\n\x0bFieldsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12A\n\x05value\x18\x02 \x01(\x0b22.google.cloud.datacatalog.v1beta1.TagTemplateField:\x028\x01"T\n\x16DataplexTransferStatus\x12(\n$DATAPLEX_TRANSFER_STATUS_UNSPECIFIED\x10\x00\x12\x10\n\x08MIGRATED\x10\x01\x1a\x02\x08\x01:p\xeaAm\n&datacatalog.googleapis.com/TagTemplate\x12Cprojects/{project}/locations/{location}/tagTemplates/{tag_template}"\xbf\x02\n\x10TagTemplateField\x12\x14\n\x04name\x18\x06 \x01(\tB\x06\xe0A\x08\xe0A\x03\x12\x14\n\x0cdisplay_name\x18\x01 \x01(\t\x12>\n\x04type\x18\x02 \x01(\x0b2+.google.cloud.datacatalog.v1beta1.FieldTypeB\x03\xe0A\x02\x12\x13\n\x0bis_required\x18\x03 \x01(\x08\x12\x13\n\x0bdescription\x18\x04 \x01(\t\x12\r\n\x05order\x18\x05 \x01(\x05:\x85\x01\xeaA\x81\x01\n+datacatalog.googleapis.com/TagTemplateField\x12Rprojects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}"\xa7\x03\n\tFieldType\x12S\n\x0eprimitive_type\x18\x01 \x01(\x0e29.google.cloud.datacatalog.v1beta1.FieldType.PrimitiveTypeH\x00\x12I\n\tenum_type\x18\x02 \x01(\x0b24.google.cloud.datacatalog.v1beta1.FieldType.EnumTypeH\x00\x1a\x8a\x01\n\x08EnumType\x12V\n\x0eallowed_values\x18\x01 \x03(\x0b2>.google.cloud.datacatalog.v1beta1.FieldType.EnumType.EnumValue\x1a&\n\tEnumValue\x12\x19\n\x0cdisplay_name\x18\x01 \x01(\tB\x03\xe0A\x02"`\n\rPrimitiveType\x12\x1e\n\x1aPRIMITIVE_TYPE_UNSPECIFIED\x10\x00\x12\n\n\x06DOUBLE\x10\x01\x12\n\n\x06STRING\x10\x02\x12\x08\n\x04BOOL\x10\x03\x12\r\n\tTIMESTAMP\x10\x04B\x0b\n\ttype_declB\xdc\x01\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.datacatalog.v1beta1.tags_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n$com.google.cloud.datacatalog.v1beta1P\x01ZFcloud.google.com/go/datacatalog/apiv1beta1/datacatalogpb;datacatalogpb\xaa\x02 Google.Cloud.DataCatalog.V1Beta1\xca\x02 Google\\Cloud\\DataCatalog\\V1beta1\xea\x02#Google::Cloud::DataCatalog::V1beta1'
    _globals['_TAG_FIELDSENTRY']._loaded_options = None
    _globals['_TAG_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_TAG'].fields_by_name['name']._loaded_options = None
    _globals['_TAG'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TAG'].fields_by_name['template']._loaded_options = None
    _globals['_TAG'].fields_by_name['template']._serialized_options = b'\xe0A\x02'
    _globals['_TAG'].fields_by_name['template_display_name']._loaded_options = None
    _globals['_TAG'].fields_by_name['template_display_name']._serialized_options = b'\xe0A\x03'
    _globals['_TAG'].fields_by_name['fields']._loaded_options = None
    _globals['_TAG'].fields_by_name['fields']._serialized_options = b'\xe0A\x02'
    _globals['_TAG']._loaded_options = None
    _globals['_TAG']._serialized_options = b'\xeaA~\n\x1edatacatalog.googleapis.com/Tag\x12\\projects/{project}/locations/{location}/entryGroups/{entry_group}/entries/{entry}/tags/{tag}'
    _globals['_TAGFIELD'].fields_by_name['display_name']._loaded_options = None
    _globals['_TAGFIELD'].fields_by_name['display_name']._serialized_options = b'\xe0A\x03'
    _globals['_TAGFIELD'].fields_by_name['order']._loaded_options = None
    _globals['_TAGFIELD'].fields_by_name['order']._serialized_options = b'\xe0A\x03'
    _globals['_TAGTEMPLATE_FIELDSENTRY']._loaded_options = None
    _globals['_TAGTEMPLATE_FIELDSENTRY']._serialized_options = b'8\x01'
    _globals['_TAGTEMPLATE_DATAPLEXTRANSFERSTATUS'].values_by_name['MIGRATED']._loaded_options = None
    _globals['_TAGTEMPLATE_DATAPLEXTRANSFERSTATUS'].values_by_name['MIGRATED']._serialized_options = b'\x08\x01'
    _globals['_TAGTEMPLATE'].fields_by_name['name']._loaded_options = None
    _globals['_TAGTEMPLATE'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_TAGTEMPLATE'].fields_by_name['fields']._loaded_options = None
    _globals['_TAGTEMPLATE'].fields_by_name['fields']._serialized_options = b'\xe0A\x02'
    _globals['_TAGTEMPLATE'].fields_by_name['dataplex_transfer_status']._loaded_options = None
    _globals['_TAGTEMPLATE'].fields_by_name['dataplex_transfer_status']._serialized_options = b'\xe0A\x03'
    _globals['_TAGTEMPLATE']._loaded_options = None
    _globals['_TAGTEMPLATE']._serialized_options = b'\xeaAm\n&datacatalog.googleapis.com/TagTemplate\x12Cprojects/{project}/locations/{location}/tagTemplates/{tag_template}'
    _globals['_TAGTEMPLATEFIELD'].fields_by_name['name']._loaded_options = None
    _globals['_TAGTEMPLATEFIELD'].fields_by_name['name']._serialized_options = b'\xe0A\x08\xe0A\x03'
    _globals['_TAGTEMPLATEFIELD'].fields_by_name['type']._loaded_options = None
    _globals['_TAGTEMPLATEFIELD'].fields_by_name['type']._serialized_options = b'\xe0A\x02'
    _globals['_TAGTEMPLATEFIELD']._loaded_options = None
    _globals['_TAGTEMPLATEFIELD']._serialized_options = b'\xeaA\x81\x01\n+datacatalog.googleapis.com/TagTemplateField\x12Rprojects/{project}/locations/{location}/tagTemplates/{tag_template}/fields/{field}'
    _globals['_FIELDTYPE_ENUMTYPE_ENUMVALUE'].fields_by_name['display_name']._loaded_options = None
    _globals['_FIELDTYPE_ENUMTYPE_ENUMVALUE'].fields_by_name['display_name']._serialized_options = b'\xe0A\x02'
    _globals['_TAG']._serialized_start = 175
    _globals['_TAG']._serialized_end = 580
    _globals['_TAG_FIELDSENTRY']._serialized_start = 350
    _globals['_TAG_FIELDSENTRY']._serialized_end = 439
    _globals['_TAGFIELD']._serialized_start = 583
    _globals['_TAGFIELD']._serialized_end = 884
    _globals['_TAGFIELD_ENUMVALUE']._serialized_start = 843
    _globals['_TAGFIELD_ENUMVALUE']._serialized_end = 876
    _globals['_TAGTEMPLATE']._serialized_start = 887
    _globals['_TAGTEMPLATE']._serialized_end = 1429
    _globals['_TAGTEMPLATE_FIELDSENTRY']._serialized_start = 1132
    _globals['_TAGTEMPLATE_FIELDSENTRY']._serialized_end = 1229
    _globals['_TAGTEMPLATE_DATAPLEXTRANSFERSTATUS']._serialized_start = 1231
    _globals['_TAGTEMPLATE_DATAPLEXTRANSFERSTATUS']._serialized_end = 1315
    _globals['_TAGTEMPLATEFIELD']._serialized_start = 1432
    _globals['_TAGTEMPLATEFIELD']._serialized_end = 1751
    _globals['_FIELDTYPE']._serialized_start = 1754
    _globals['_FIELDTYPE']._serialized_end = 2177
    _globals['_FIELDTYPE_ENUMTYPE']._serialized_start = 1928
    _globals['_FIELDTYPE_ENUMTYPE']._serialized_end = 2066
    _globals['_FIELDTYPE_ENUMTYPE_ENUMVALUE']._serialized_start = 2028
    _globals['_FIELDTYPE_ENUMTYPE_ENUMVALUE']._serialized_end = 2066
    _globals['_FIELDTYPE_PRIMITIVETYPE']._serialized_start = 2068
    _globals['_FIELDTYPE_PRIMITIVETYPE']._serialized_end = 2164