"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'google/chromeos/moblab/v1beta1/resources.proto')
_sym_db = _symbol_database.Default()
from .....google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from .....google.api import resource_pb2 as google_dot_api_dot_resource__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n.google/chromeos/moblab/v1beta1/resources.proto\x12\x1egoogle.chromeos.moblab.v1beta1\x1a\x1fgoogle/api/field_behavior.proto\x1a\x19google/api/resource.proto\x1a\x1fgoogle/protobuf/timestamp.proto"h\n\x0bBuildTarget\x12\x0c\n\x04name\x18\x01 \x01(\t:K\xeaAH\n)chromeosmoblab.googleapis.com/BuildTarget\x12\x1bbuildTargets/{build_target}"k\n\x05Model\x12\x0c\n\x04name\x18\x01 \x01(\t:T\xeaAQ\n#chromeosmoblab.googleapis.com/Model\x12*buildTargets/{build_target}/models/{model}"_\n\tMilestone\x12\x0c\n\x04name\x18\x01 \x01(\t:D\xeaAA\n\'chromeosmoblab.googleapis.com/Milestone\x12\x16milestones/{milestone}"\xb0\x04\n\x05Build\x12\x0c\n\x04name\x18\x01 \x01(\t\x12?\n\tmilestone\x18\x02 \x01(\tB,\xfaA)\n\'chromeosmoblab.googleapis.com/Milestone\x12\x15\n\rbuild_version\x18\x03 \x01(\t\x12A\n\x06status\x18\x04 \x01(\x0e21.google.chromeos.moblab.v1beta1.Build.BuildStatus\x12=\n\x04type\x18\x05 \x01(\x0e2/.google.chromeos.moblab.v1beta1.Build.BuildType\x12\x0e\n\x06branch\x18\x06 \x01(\t\x12\x1b\n\x13rw_firmware_version\x18\x07 \x01(\t\x12\x0e\n\x06labels\x18\x08 \x03(\t"Y\n\x0bBuildStatus\x12\x1c\n\x18BUILD_STATUS_UNSPECIFIED\x10\x00\x12\x08\n\x04PASS\x10\x01\x12\x08\n\x04FAIL\x10\x02\x12\x0b\n\x07RUNNING\x10\x03\x12\x0b\n\x07ABORTED\x10\x04"B\n\tBuildType\x12\x1a\n\x16BUILD_TYPE_UNSPECIFIED\x10\x00\x12\x0b\n\x07RELEASE\x10\x01\x12\x0c\n\x08FIRMWARE\x10\x02:c\xeaA`\n#chromeosmoblab.googleapis.com/Build\x129buildTargets/{build_target}/models/{model}/builds/{build}"\x8d\x02\n\rBuildArtifact\x12\x0c\n\x04name\x18\x01 \x01(\t\x127\n\x05build\x18\x02 \x01(\tB(\xfaA%\n#chromeosmoblab.googleapis.com/Build\x12\x0e\n\x06bucket\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x14\n\x0cobject_count\x18\x05 \x01(\r:\x80\x01\xeaA}\n+chromeosmoblab.googleapis.com/BuildArtifact\x12NbuildTargets/{build_target}/models/{model}/builds/{build}/artifacts/{artifact}"\xa4\x03\n\nCloudBuild\x12\x0f\n\x02id\x18\x01 \x01(\tB\x03\xe0A\x03\x12E\n\x06status\x18\x02 \x01(\x0e20.google.chromeos.moblab.v1beta1.CloudBuild.StateB\x03\xe0A\x03\x124\n\x0bcreate_time\x18\x03 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x123\n\nstart_time\x18\x04 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03\x124\n\x0bfinish_time\x18\x05 \x01(\x0b2\x1a.google.protobuf.TimestampB\x03\xe0A\x03"\x9c\x01\n\x05State\x12\x15\n\x11STATE_UNSPECIFIED\x10\x00\x12\n\n\x06QUEUED\x10\x01\x12\x0b\n\x07PENDING\x10\x02\x12\x0b\n\x07WORKING\x10\x03\x12\r\n\tSUCCEEDED\x10\x04\x12\n\n\x06FAILED\x10\x05\x12\x12\n\x0eINTERNAL_ERROR\x10\x06\x12\x0b\n\x07TIMEOUT\x10\x07\x12\r\n\tCANCELLED\x10\x08\x12\x0b\n\x07EXPIRED\x10\tB~\n"com.google.chromeos.moblab.v1beta1B\x0eResourcesProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblabb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'google.chromeos.moblab.v1beta1.resources_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'\n"com.google.chromeos.moblab.v1beta1B\x0eResourcesProtoH\x01P\x01ZDgoogle.golang.org/genproto/googleapis/chromeos/moblab/v1beta1;moblab'
    _globals['_BUILDTARGET']._loaded_options = None
    _globals['_BUILDTARGET']._serialized_options = b'\xeaAH\n)chromeosmoblab.googleapis.com/BuildTarget\x12\x1bbuildTargets/{build_target}'
    _globals['_MODEL']._loaded_options = None
    _globals['_MODEL']._serialized_options = b'\xeaAQ\n#chromeosmoblab.googleapis.com/Model\x12*buildTargets/{build_target}/models/{model}'
    _globals['_MILESTONE']._loaded_options = None
    _globals['_MILESTONE']._serialized_options = b"\xeaAA\n'chromeosmoblab.googleapis.com/Milestone\x12\x16milestones/{milestone}"
    _globals['_BUILD'].fields_by_name['milestone']._loaded_options = None
    _globals['_BUILD'].fields_by_name['milestone']._serialized_options = b"\xfaA)\n'chromeosmoblab.googleapis.com/Milestone"
    _globals['_BUILD']._loaded_options = None
    _globals['_BUILD']._serialized_options = b'\xeaA`\n#chromeosmoblab.googleapis.com/Build\x129buildTargets/{build_target}/models/{model}/builds/{build}'
    _globals['_BUILDARTIFACT'].fields_by_name['build']._loaded_options = None
    _globals['_BUILDARTIFACT'].fields_by_name['build']._serialized_options = b'\xfaA%\n#chromeosmoblab.googleapis.com/Build'
    _globals['_BUILDARTIFACT']._loaded_options = None
    _globals['_BUILDARTIFACT']._serialized_options = b'\xeaA}\n+chromeosmoblab.googleapis.com/BuildArtifact\x12NbuildTargets/{build_target}/models/{model}/builds/{build}/artifacts/{artifact}'
    _globals['_CLOUDBUILD'].fields_by_name['id']._loaded_options = None
    _globals['_CLOUDBUILD'].fields_by_name['id']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDBUILD'].fields_by_name['status']._loaded_options = None
    _globals['_CLOUDBUILD'].fields_by_name['status']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDBUILD'].fields_by_name['create_time']._loaded_options = None
    _globals['_CLOUDBUILD'].fields_by_name['create_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDBUILD'].fields_by_name['start_time']._loaded_options = None
    _globals['_CLOUDBUILD'].fields_by_name['start_time']._serialized_options = b'\xe0A\x03'
    _globals['_CLOUDBUILD'].fields_by_name['finish_time']._loaded_options = None
    _globals['_CLOUDBUILD'].fields_by_name['finish_time']._serialized_options = b'\xe0A\x03'
    _globals['_BUILDTARGET']._serialized_start = 175
    _globals['_BUILDTARGET']._serialized_end = 279
    _globals['_MODEL']._serialized_start = 281
    _globals['_MODEL']._serialized_end = 388
    _globals['_MILESTONE']._serialized_start = 390
    _globals['_MILESTONE']._serialized_end = 485
    _globals['_BUILD']._serialized_start = 488
    _globals['_BUILD']._serialized_end = 1048
    _globals['_BUILD_BUILDSTATUS']._serialized_start = 790
    _globals['_BUILD_BUILDSTATUS']._serialized_end = 879
    _globals['_BUILD_BUILDTYPE']._serialized_start = 881
    _globals['_BUILD_BUILDTYPE']._serialized_end = 947
    _globals['_BUILDARTIFACT']._serialized_start = 1051
    _globals['_BUILDARTIFACT']._serialized_end = 1320
    _globals['_CLOUDBUILD']._serialized_start = 1323
    _globals['_CLOUDBUILD']._serialized_end = 1743
    _globals['_CLOUDBUILD_STATE']._serialized_start = 1587
    _globals['_CLOUDBUILD_STATE']._serialized_end = 1743