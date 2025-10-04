"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/cloud/aiplatform/v1/notebook_software_config.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.cloud.aiplatform.v1 import env_var_pb2 as google_dot_cloud_dot_aiplatform_dot_v1_dot_env__var__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n9google/cloud/aiplatform/v1/notebook_software_config.proto\x12\x1agoogle.cloud.aiplatform.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a(google/cloud/aiplatform/v1/env_var.proto"\xec\x02\n\x17PostStartupScriptConfig\x12 \n\x13post_startup_script\x18\x01 \x01(\tB\x03\xe0A\x01\x12$\n\x17post_startup_script_url\x18\x02 \x01(\tB\x03\xe0A\x01\x12x\n\x1cpost_startup_script_behavior\x18\x03 \x01(\x0e2M.google.cloud.aiplatform.v1.PostStartupScriptConfig.PostStartupScriptBehaviorB\x03\xe0A\x01"\x8e\x01\n\x19PostStartupScriptBehavior\x12,\n(POST_STARTUP_SCRIPT_BEHAVIOR_UNSPECIFIED\x10\x00\x12\x0c\n\x08RUN_ONCE\x10\x01\x12\x13\n\x0fRUN_EVERY_START\x10\x02\x12 \n\x1cDOWNLOAD_AND_RUN_EVERY_START\x10\x03"A\n\nColabImage\x12\x19\n\x0crelease_name\x18\x01 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x02 \x01(\tB\x03\xe0A\x03"\x81\x02\n\x16NotebookSoftwareConfig\x12B\n\x0bcolab_image\x18\x05 \x01(\x0b2&.google.cloud.aiplatform.v1.ColabImageB\x03\xe0A\x01H\x00\x124\n\x03env\x18\x01 \x03(\x0b2".google.cloud.aiplatform.v1.EnvVarB\x03\xe0A\x01\x12\\\n\x1apost_startup_script_config\x18\x02 \x01(\x0b23.google.cloud.aiplatform.v1.PostStartupScriptConfigB\x03\xe0A\x01B\x0f\n\rruntime_imageB\xd9\x01\n\x1ecom.google.cloud.aiplatform.v1B\x1bNotebookSoftwareConfigProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.cloud.aiplatform.v1.notebook_software_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n\x1ecom.google.cloud.aiplatform.v1B\x1bNotebookSoftwareConfigProtoP\x01Z>cloud.google.com/go/aiplatform/apiv1/aiplatformpb;aiplatformpb\xaa\x02\x1aGoogle.Cloud.AIPlatform.V1\xca\x02\x1aGoogle\\Cloud\\AIPlatform\\V1\xea\x02\x1dGoogle::Cloud::AIPlatform::V1'
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script']._loaded_options = None
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script']._serialized_options = b'\xe0A\x01'
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script_url']._loaded_options = None
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script_url']._serialized_options = b'\xe0A\x01'
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script_behavior']._loaded_options = None
    _globals['_POSTSTARTUPSCRIPTCONFIG'].fields_by_name['post_startup_script_behavior']._serialized_options = b'\xe0A\x01'
    _globals['_COLABIMAGE'].fields_by_name['release_name']._loaded_options = None
    _globals['_COLABIMAGE'].fields_by_name['release_name']._serialized_options = b'\xe0A\x01'
    _globals['_COLABIMAGE'].fields_by_name['description']._loaded_options = None
    _globals['_COLABIMAGE'].fields_by_name['description']._serialized_options = b'\xe0A\x03'
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['colab_image']._loaded_options = None
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['colab_image']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['env']._loaded_options = None
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['env']._serialized_options = b'\xe0A\x01'
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['post_startup_script_config']._loaded_options = None
    _globals['_NOTEBOOKSOFTWARECONFIG'].fields_by_name['post_startup_script_config']._serialized_options = b'\xe0A\x01'
    _globals['_POSTSTARTUPSCRIPTCONFIG']._serialized_start = 165
    _globals['_POSTSTARTUPSCRIPTCONFIG']._serialized_end = 529
    _globals['_POSTSTARTUPSCRIPTCONFIG_POSTSTARTUPSCRIPTBEHAVIOR']._serialized_start = 387
    _globals['_POSTSTARTUPSCRIPTCONFIG_POSTSTARTUPSCRIPTBEHAVIOR']._serialized_end = 529
    _globals['_COLABIMAGE']._serialized_start = 531
    _globals['_COLABIMAGE']._serialized_end = 596
    _globals['_NOTEBOOKSOFTWARECONFIG']._serialized_start = 599
    _globals['_NOTEBOOKSOFTWARECONFIG']._serialized_end = 856