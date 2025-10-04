"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/managedkafka/schemaregistry/v1/schema_registry_resources.proto')
_sym_db = _symbol_database.Default()
from ......google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from ......google.api import resource_pb2 as google_dot_api_dot_resource__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nKgoogle/cloud/managedkafka/schemaregistry/v1/schema_registry_resources.proto\x12+google.cloud.managedkafka.schemaregistry.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto"\x89\x02\n\x0eSchemaRegistry\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12C\n\x08contexts\x18\x02 \x03(\tB1\xe0A\x03\xfaA+\n)managedkafka.googleapis.com/SchemaContext:\x9e\x01\xeaA\x9a\x01\n*managedkafka.googleapis.com/SchemaRegistry\x12Jprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}*\x10schemaRegistries2\x0eschemaRegistry"\x85\x02\n\x07Context\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12C\n\x08subjects\x18\x02 \x03(\tB1\xe0A\x01\xfaA+\n)managedkafka.googleapis.com/SchemaSubject:\xa1\x01\xeaA\x9d\x01\n)managedkafka.googleapis.com/SchemaContext\x12]projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}*\x08contexts2\x07context"\x90\x05\n\x06Schema\x12X\n\x0bschema_type\x18\x01 \x01(\x0e2>.google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaTypeB\x03\xe0A\x01\x12\x1e\n\x0eschema_payload\x18\x02 \x01(\tR\x06schema\x12\\\n\nreferences\x18\x03 \x03(\x0b2C.google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaReferenceB\x03\xe0A\x01\x1aP\n\x0fSchemaReference\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07subject\x18\x02 \x01(\tB\x03\xe0A\x02\x12\x14\n\x07version\x18\x03 \x01(\x05B\x03\xe0A\x02"K\n\nSchemaType\x12\x1b\n\x17SCHEMA_TYPE_UNSPECIFIED\x10\x00\x12\x08\n\x04AVRO\x10\x01\x12\x08\n\x04JSON\x10\x02\x12\x0c\n\x08PROTOBUF\x10\x03:\x8e\x02\xeaA\x8a\x02\n"managedkafka.googleapis.com/Schema\x12_projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}\x12rprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}*\x07schemas2\x06schema"\xfd\x02\n\rSchemaSubject\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x08\x12C\n\x08versions\x18\x03 \x03(\tB1\xe0A\x01\xfaA+\n)managedkafka.googleapis.com/SchemaVersion:\x93\x02\xeaA\x8f\x02\n)managedkafka.googleapis.com/SchemaSubject\x12]projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}\x12pprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}*\x08subjects2\x07subject"\x91\t\n\rSchemaVersion\x12\x14\n\x07subject\x18\x01 \x01(\tB\x03\xe0A\x02\x12 \n\nversion_id\x18\x02 \x01(\x05B\x03\xe0A\x02R\x07version\x12\x1a\n\tschema_id\x18\x03 \x01(\x05B\x03\xe0A\x02R\x02id\x12X\n\x0bschema_type\x18\x04 \x01(\x0e2>.google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaTypeB\x03\xe0A\x01\x12#\n\x0eschema_payload\x18\x05 \x01(\tB\x03\xe0A\x02R\x06schema\x12\\\n\nreferences\x18\x06 \x03(\x0b2C.google.cloud.managedkafka.schemaregistry.v1.Schema.SchemaReferenceB\x03\xe0A\x01:\xce\x06\xeaA\xca\x06\n)managedkafka.googleapis.com/SchemaVersion\x12pprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}\x12\x83\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}\x12tprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions\x12\x87\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/compatibility/subjects/{subject}/versions\x12~projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions/{version}\x12\x91\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/compatibility/subjects/{subject}/versions/{version}*\x08versions2\x07version"\xa0\x06\n\x0cSchemaConfig\x12l\n\rcompatibility\x18\x01 \x01(\x0e2K.google.cloud.managedkafka.schemaregistry.v1.SchemaConfig.CompatibilityTypeB\x03\xe0A\x02H\x00\x88\x01\x01\x12\x1b\n\tnormalize\x18\x02 \x01(\x08B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x12\n\x05alias\x18\x03 \x01(\tB\x03\xe0A\x01"\x88\x01\n\x11CompatibilityType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08BACKWARD\x10\x01\x12\x17\n\x13BACKWARD_TRANSITIVE\x10\x02\x12\x0b\n\x07FORWARD\x10\x03\x12\x16\n\x12FORWARD_TRANSITIVE\x10\x04\x12\x08\n\x04FULL\x10\x05\x12\x13\n\x0fFULL_TRANSITIVE\x10\x06:\xc5\x03\xeaA\xc1\x03\n(managedkafka.googleapis.com/SchemaConfig\x12Qprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config\x12[projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}\x12dprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/config\x12nprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/config/{subject}*\x07configs2\x06configB\x10\n\x0e_compatibilityB\x0c\n\n_normalize"\xda\x04\n\nSchemaMode\x12S\n\x04mode\x18\x01 \x01(\x0e2@.google.cloud.managedkafka.schemaregistry.v1.SchemaMode.ModeTypeB\x03\xe0A\x02"=\n\x08ModeType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08READONLY\x10\x01\x12\r\n\tREADWRITE\x10\x02\x12\n\n\x06IMPORT\x10\x03:\xb7\x03\xeaA\xb3\x03\n&managedkafka.googleapis.com/SchemaMode\x12Oprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode\x12Yprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}\x12bprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode\x12lprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}*\x05modes2\x04modeB\xb8\x02\n/com.google.cloud.managedkafka.schemaregistry.v1B\x1cSchemaRegistryResourcesProtoP\x01ZWcloud.google.com/go/managedkafka/schemaregistry/apiv1/schemaregistrypb;schemaregistrypb\xaa\x02+Google.Cloud.ManagedKafka.SchemaRegistry.V1\xca\x02+Google\\Cloud\\ManagedKafka\\SchemaRegistry\\V1\xea\x02/Google::Cloud::ManagedKafka::SchemaRegistry::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.managedkafka.schemaregistry.v1.schema_registry_resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n/com.google.cloud.managedkafka.schemaregistry.v1B\x1cSchemaRegistryResourcesProtoP\x01ZWcloud.google.com/go/managedkafka/schemaregistry/apiv1/schemaregistrypb;schemaregistrypb\xaa\x02+Google.Cloud.ManagedKafka.SchemaRegistry.V1\xca\x02+Google\\Cloud\\ManagedKafka\\SchemaRegistry\\V1\xea\x02/Google::Cloud::ManagedKafka::SchemaRegistry::V1'
    _globals['_SCHEMAREGISTRY'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMAREGISTRY'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SCHEMAREGISTRY'].fields_by_name['contexts']._loaded_options = None
    _globals['_SCHEMAREGISTRY'].fields_by_name['contexts']._serialized_options = b'\xe0A\x03\xfaA+\n)managedkafka.googleapis.com/SchemaContext'
    _globals['_SCHEMAREGISTRY']._loaded_options = None
    _globals['_SCHEMAREGISTRY']._serialized_options = b'\xeaA\x9a\x01\n*managedkafka.googleapis.com/SchemaRegistry\x12Jprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}*\x10schemaRegistries2\x0eschemaRegistry'
    _globals['_CONTEXT'].fields_by_name['name']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_CONTEXT'].fields_by_name['subjects']._loaded_options = None
    _globals['_CONTEXT'].fields_by_name['subjects']._serialized_options = b'\xe0A\x01\xfaA+\n)managedkafka.googleapis.com/SchemaSubject'
    _globals['_CONTEXT']._loaded_options = None
    _globals['_CONTEXT']._serialized_options = b'\xeaA\x9d\x01\n)managedkafka.googleapis.com/SchemaContext\x12]projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}*\x08contexts2\x07context'
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['name']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['subject']._loaded_options = None
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['subject']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['version']._loaded_options = None
    _globals['_SCHEMA_SCHEMAREFERENCE'].fields_by_name['version']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMA'].fields_by_name['schema_type']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['schema_type']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA'].fields_by_name['references']._loaded_options = None
    _globals['_SCHEMA'].fields_by_name['references']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMA']._loaded_options = None
    _globals['_SCHEMA']._serialized_options = b'\xeaA\x8a\x02\n"managedkafka.googleapis.com/Schema\x12_projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/schemas/ids/{schema}\x12rprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/schemas/ids/{schema}*\x07schemas2\x06schema'
    _globals['_SCHEMASUBJECT'].fields_by_name['name']._loaded_options = None
    _globals['_SCHEMASUBJECT'].fields_by_name['name']._serialized_options = b'\xe0A\x08'
    _globals['_SCHEMASUBJECT'].fields_by_name['versions']._loaded_options = None
    _globals['_SCHEMASUBJECT'].fields_by_name['versions']._serialized_options = b'\xe0A\x01\xfaA+\n)managedkafka.googleapis.com/SchemaVersion'
    _globals['_SCHEMASUBJECT']._loaded_options = None
    _globals['_SCHEMASUBJECT']._serialized_options = b'\xeaA\x8f\x02\n)managedkafka.googleapis.com/SchemaSubject\x12]projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}\x12pprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}*\x08subjects2\x07subject'
    _globals['_SCHEMAVERSION'].fields_by_name['subject']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['subject']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMAVERSION'].fields_by_name['version_id']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['version_id']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMAVERSION'].fields_by_name['schema_id']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['schema_id']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMAVERSION'].fields_by_name['schema_type']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['schema_type']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMAVERSION'].fields_by_name['schema_payload']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['schema_payload']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMAVERSION'].fields_by_name['references']._loaded_options = None
    _globals['_SCHEMAVERSION'].fields_by_name['references']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMAVERSION']._loaded_options = None
    _globals['_SCHEMAVERSION']._serialized_options = b'\xeaA\xca\x06\n)managedkafka.googleapis.com/SchemaVersion\x12pprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/subjects/{subject}/versions/{version}\x12\x83\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/subjects/{subject}/versions/{version}\x12tprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions\x12\x87\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/compatibility/subjects/{subject}/versions\x12~projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/compatibility/subjects/{subject}/versions/{version}\x12\x91\x01projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/compatibility/subjects/{subject}/versions/{version}*\x08versions2\x07version'
    _globals['_SCHEMACONFIG'].fields_by_name['compatibility']._loaded_options = None
    _globals['_SCHEMACONFIG'].fields_by_name['compatibility']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMACONFIG'].fields_by_name['normalize']._loaded_options = None
    _globals['_SCHEMACONFIG'].fields_by_name['normalize']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMACONFIG'].fields_by_name['alias']._loaded_options = None
    _globals['_SCHEMACONFIG'].fields_by_name['alias']._serialized_options = b'\xe0A\x01'
    _globals['_SCHEMACONFIG']._loaded_options = None
    _globals['_SCHEMACONFIG']._serialized_options = b'\xeaA\xc1\x03\n(managedkafka.googleapis.com/SchemaConfig\x12Qprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config\x12[projects/{project}/locations/{location}/schemaRegistries/{schema_registry}/config/{subject}\x12dprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/config\x12nprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/config/{subject}*\x07configs2\x06config'
    _globals['_SCHEMAMODE'].fields_by_name['mode']._loaded_options = None
    _globals['_SCHEMAMODE'].fields_by_name['mode']._serialized_options = b'\xe0A\x02'
    _globals['_SCHEMAMODE']._loaded_options = None
    _globals['_SCHEMAMODE']._serialized_options = b'\xeaA\xb3\x03\n&managedkafka.googleapis.com/SchemaMode\x12Oprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode\x12Yprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/mode/{subject}\x12bprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode\x12lprojects/{project}/locations/{location}/schemaRegistries/{schema_registry}/contexts/{context}/mode/{subject}*\x05modes2\x04mode'
    _globals['_SCHEMAREGISTRY']._serialized_start = 185
    _globals['_SCHEMAREGISTRY']._serialized_end = 450
    _globals['_CONTEXT']._serialized_start = 453
    _globals['_CONTEXT']._serialized_end = 714
    _globals['_SCHEMA']._serialized_start = 717
    _globals['_SCHEMA']._serialized_end = 1373
    _globals['_SCHEMA_SCHEMAREFERENCE']._serialized_start = 943
    _globals['_SCHEMA_SCHEMAREFERENCE']._serialized_end = 1023
    _globals['_SCHEMA_SCHEMATYPE']._serialized_start = 1025
    _globals['_SCHEMA_SCHEMATYPE']._serialized_end = 1100
    _globals['_SCHEMASUBJECT']._serialized_start = 1376
    _globals['_SCHEMASUBJECT']._serialized_end = 1757
    _globals['_SCHEMAVERSION']._serialized_start = 1760
    _globals['_SCHEMAVERSION']._serialized_end = 2929
    _globals['_SCHEMACONFIG']._serialized_start = 2932
    _globals['_SCHEMACONFIG']._serialized_end = 3732
    _globals['_SCHEMACONFIG_COMPATIBILITYTYPE']._serialized_start = 3108
    _globals['_SCHEMACONFIG_COMPATIBILITYTYPE']._serialized_end = 3244
    _globals['_SCHEMAMODE']._serialized_start = 3735
    _globals['_SCHEMAMODE']._serialized_end = 4337
    _globals['_SCHEMAMODE_MODETYPE']._serialized_start = 3834
    _globals['_SCHEMAMODE_MODETYPE']._serialized_end = 3895