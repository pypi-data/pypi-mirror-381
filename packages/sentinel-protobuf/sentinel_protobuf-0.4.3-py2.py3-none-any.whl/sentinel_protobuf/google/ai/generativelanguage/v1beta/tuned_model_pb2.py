"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/ai/generativelanguage/v1beta/tuned_model.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5google/ai/generativelanguage/v1beta/tuned_model.proto\x12#google.ai.generativelanguage.v1beta\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"\xce\x06\n\nTunedModel\x12X\n\x12tuned_model_source\x18\x03 \x01(\x0b25.google.ai.generativelanguage.v1beta.TunedModelSourceB\x03\xe0A\x01H\x00\x12E\n\nbase_model\x18\x04 \x01(\tB/\xe0A\x05\xfaA)\n\'generativelanguage.googleapis.com/ModelH\x00\x12\x11\n\x04name\x18\x01 \x01(\tB\x03\xe0A\x03\x12\x19\n\x0cdisplay_name\x18\x05 \x01(\tB\x03\xe0A\x01\x12\x18\n\x0bdescription\x18\x06 \x01(\tB\x03\xe0A\x01\x12\x1d\n\x0btemperature\x18\x0b \x01(\x02B\x03\xe0A\x01H\x01\x88\x01\x01\x12\x17\n\x05top_p\x18\x0c \x01(\x02B\x03\xe0A\x01H\x02\x88\x01\x01\x12\x17\n\x05top_k\x18\r \x01(\x05B\x03\xe0A\x01H\x03\x88\x01\x01\x12I\n\x05state\x18\x07 \x01(\x0e25.google.ai.generativelanguage.v1beta.TunedModel.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x08 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bupdate_time\x18\t \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12I\n\x0btuning_task\x18\n \x01(\x0b2/.google.ai.generativelanguage.v1beta.TuningTaskB\x03\xe0A\x02\x12#\n\x16reader_project_numbers\x18\x0e \x03(\x03B\x03\xe0A\x01"D\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\x0c\n\x08CREATING\x10\x01\x12\n\n\x06ACTIVE\x10\x02\x12\n\n\x06FAILED\x10\x03:e\xeaAb\n,generativelanguage.googleapis.com/TunedModel\x12\x19tunedModels/{tuned_model}*\x0btunedModels2\ntunedModelB\x0e\n\x0csource_modelB\x0e\n\x0c_temperatureB\x08\n\x06_top_pB\x08\n\x06_top_k"\xa2\x01\n\x10TunedModelSource\x12I\n\x0btuned_model\x18\x01 \x01(\tB4\xe0A\x05\xfaA.\n,generativelanguage.googleapis.com/TunedModel\x12C\n\nbase_model\x18\x02 \x01(\tB/\xe0A\x03\xfaA)\n\'generativelanguage.googleapis.com/Model"\xea\x02\n\nTuningTask\x123\n\nstart_time\x18\x01 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x126\n\rcomplete_time\x18\x02 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x12K\n\tsnapshots\x18\x03 \x03(\x0b23.google.ai.generativelanguage.v1beta.TuningSnapshotB\x03\xe0A\x03\x12N\n\rtraining_data\x18\x04 \x01(\x0b2,.google.ai.generativelanguage.v1beta.DatasetB\t\xe0A\x04\xe0A\x02\xe0A\x05\x12R\n\x0fhyperparameters\x18\x05 \x01(\x0b24.google.ai.generativelanguage.v1beta.HyperparametersB\x03\xe0A\x05"\xd2\x01\n\x0fHyperparameters\x12\x1f\n\rlearning_rate\x18\x10 \x01(\x02B\x06\xe0A\x05\xe0A\x01H\x00\x12*\n\x18learning_rate_multiplier\x18\x11 \x01(\x02B\x06\xe0A\x05\xe0A\x01H\x00\x12\x1d\n\x0bepoch_count\x18\x0e \x01(\x05B\x03\xe0A\x05H\x01\x88\x01\x01\x12\x1c\n\nbatch_size\x18\x0f \x01(\x05B\x03\xe0A\x05H\x02\x88\x01\x01B\x16\n\x14learning_rate_optionB\x0e\n\x0c_epoch_countB\r\n\x0b_batch_size"b\n\x07Dataset\x12L\n\x08examples\x18\x01 \x01(\x0b23.google.ai.generativelanguage.v1beta.TuningExamplesB\x03\xe0A\x01H\x00B\t\n\x07dataset"V\n\x0eTuningExamples\x12D\n\x08examples\x18\x01 \x03(\x0b22.google.ai.generativelanguage.v1beta.TuningExample"N\n\rTuningExample\x12\x19\n\ntext_input\x18\x01 \x01(\tB\x03\xe0A\x01H\x00\x12\x13\n\x06output\x18\x03 \x01(\tB\x03\xe0A\x02B\r\n\x0bmodel_input"\x86\x01\n\x0eTuningSnapshot\x12\x11\n\x04step\x18\x01 \x01(\x05B\x03\xe0A\x03\x12\x12\n\x05epoch\x18\x02 \x01(\x05B\x03\xe0A\x03\x12\x16\n\tmean_loss\x18\x03 \x01(\x02B\x03\xe0A\x03\x125\n\x0ccompute_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03B\x9b\x01\n\'com.google.ai.generativelanguage.v1betaB\x0fTunedModelProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepbb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.ai.generativelanguage.v1beta.tuned_model_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b"\n'com.google.ai.generativelanguage.v1betaB\x0fTunedModelProtoP\x01Z]cloud.google.com/go/ai/generativelanguage/apiv1beta/generativelanguagepb;generativelanguagepb"
    _globals['_TUNEDMODEL'].fields_by_name['tuned_model_source']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['tuned_model_source']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['base_model']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['base_model']._serialized_options = b"\xe0A\x05\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_TUNEDMODEL'].fields_by_name['name']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['name']._serialized_options = b'\xe0A\x03'
    _globals['_TUNEDMODEL'].fields_by_name['display_name']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['display_name']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['description']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['description']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['temperature']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['temperature']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['top_p']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['top_p']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['top_k']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['top_k']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL'].fields_by_name['state']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['state']._serialized_options = b'\xe0A\x03'
    _globals['_TUNEDMODEL'].fields_by_name['create_time']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNEDMODEL'].fields_by_name['update_time']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['update_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNEDMODEL'].fields_by_name['tuning_task']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['tuning_task']._serialized_options = b'\xe0A\x02'
    _globals['_TUNEDMODEL'].fields_by_name['reader_project_numbers']._loaded_options = None
    _globals['_TUNEDMODEL'].fields_by_name['reader_project_numbers']._serialized_options = b'\xe0A\x01'
    _globals['_TUNEDMODEL']._loaded_options = None
    _globals['_TUNEDMODEL']._serialized_options = b'\xeaAb\n,generativelanguage.googleapis.com/TunedModel\x12\x19tunedModels/{tuned_model}*\x0btunedModels2\ntunedModel'
    _globals['_TUNEDMODELSOURCE'].fields_by_name['tuned_model']._loaded_options = None
    _globals['_TUNEDMODELSOURCE'].fields_by_name['tuned_model']._serialized_options = b'\xe0A\x05\xfaA.\n,generativelanguage.googleapis.com/TunedModel'
    _globals['_TUNEDMODELSOURCE'].fields_by_name['base_model']._loaded_options = None
    _globals['_TUNEDMODELSOURCE'].fields_by_name['base_model']._serialized_options = b"\xe0A\x03\xfaA)\n'generativelanguage.googleapis.com/Model"
    _globals['_TUNINGTASK'].fields_by_name['start_time']._loaded_options = None
    _globals['_TUNINGTASK'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGTASK'].fields_by_name['complete_time']._loaded_options = None
    _globals['_TUNINGTASK'].fields_by_name['complete_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGTASK'].fields_by_name['snapshots']._loaded_options = None
    _globals['_TUNINGTASK'].fields_by_name['snapshots']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGTASK'].fields_by_name['training_data']._loaded_options = None
    _globals['_TUNINGTASK'].fields_by_name['training_data']._serialized_options = b'\xe0A\x04\xe0A\x02\xe0A\x05'
    _globals['_TUNINGTASK'].fields_by_name['hyperparameters']._loaded_options = None
    _globals['_TUNINGTASK'].fields_by_name['hyperparameters']._serialized_options = b'\xe0A\x05'
    _globals['_HYPERPARAMETERS'].fields_by_name['learning_rate']._loaded_options = None
    _globals['_HYPERPARAMETERS'].fields_by_name['learning_rate']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_HYPERPARAMETERS'].fields_by_name['learning_rate_multiplier']._loaded_options = None
    _globals['_HYPERPARAMETERS'].fields_by_name['learning_rate_multiplier']._serialized_options = b'\xe0A\x05\xe0A\x01'
    _globals['_HYPERPARAMETERS'].fields_by_name['epoch_count']._loaded_options = None
    _globals['_HYPERPARAMETERS'].fields_by_name['epoch_count']._serialized_options = b'\xe0A\x05'
    _globals['_HYPERPARAMETERS'].fields_by_name['batch_size']._loaded_options = None
    _globals['_HYPERPARAMETERS'].fields_by_name['batch_size']._serialized_options = b'\xe0A\x05'
    _globals['_DATASET'].fields_by_name['examples']._loaded_options = None
    _globals['_DATASET'].fields_by_name['examples']._serialized_options = b'\xe0A\x01'
    _globals['_TUNINGEXAMPLE'].fields_by_name['text_input']._loaded_options = None
    _globals['_TUNINGEXAMPLE'].fields_by_name['text_input']._serialized_options = b'\xe0A\x01'
    _globals['_TUNINGEXAMPLE'].fields_by_name['output']._loaded_options = None
    _globals['_TUNINGEXAMPLE'].fields_by_name['output']._serialized_options = b'\xe0A\x02'
    _globals['_TUNINGSNAPSHOT'].fields_by_name['step']._loaded_options = None
    _globals['_TUNINGSNAPSHOT'].fields_by_name['step']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGSNAPSHOT'].fields_by_name['epoch']._loaded_options = None
    _globals['_TUNINGSNAPSHOT'].fields_by_name['epoch']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGSNAPSHOT'].fields_by_name['mean_loss']._loaded_options = None
    _globals['_TUNINGSNAPSHOT'].fields_by_name['mean_loss']._serialized_options = b'\xe0A\x03'
    _globals['_TUNINGSNAPSHOT'].fields_by_name['compute_time']._loaded_options = None
    _globals['_TUNINGSNAPSHOT'].fields_by_name['compute_time']._serialized_options = b'\xe0A\x03'
    _globals['_TUNEDMODEL']._serialized_start = 188
    _globals['_TUNEDMODEL']._serialized_end = 1034
    _globals['_TUNEDMODEL_STATE']._serialized_start = 811
    _globals['_TUNEDMODEL_STATE']._serialized_end = 879
    _globals['_TUNEDMODELSOURCE']._serialized_start = 1037
    _globals['_TUNEDMODELSOURCE']._serialized_end = 1199
    _globals['_TUNINGTASK']._serialized_start = 1202
    _globals['_TUNINGTASK']._serialized_end = 1564
    _globals['_HYPERPARAMETERS']._serialized_start = 1567
    _globals['_HYPERPARAMETERS']._serialized_end = 1777
    _globals['_DATASET']._serialized_start = 1779
    _globals['_DATASET']._serialized_end = 1877
    _globals['_TUNINGEXAMPLES']._serialized_start = 1879
    _globals['_TUNINGEXAMPLES']._serialized_end = 1965
    _globals['_TUNINGEXAMPLE']._serialized_start = 1967
    _globals['_TUNINGEXAMPLE']._serialized_end = 2045
    _globals['_TUNINGSNAPSHOT']._serialized_start = 2048
    _globals['_TUNINGSNAPSHOT']._serialized_end = 2182