"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/provider/v3/msg.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.provider.v3 import params_pb2 as sentinel_dot_provider_dot_v3_dot_params__pb2
from ....sentinel.types.v1 import status_pb2 as sentinel_dot_types_dot_v1_dot_status__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/provider/v3/msg.proto\x12\x14sentinel.provider.v3\x1a\x14gogoproto/gogo.proto\x1a!sentinel/provider/v3/params.proto\x1a\x1esentinel/types/v1/status.proto"o\n\x1aMsgRegisterProviderRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"t\n\x1fMsgUpdateProviderDetailsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x10\n\x08identity\x18\x03 \x01(\t\x12\x0f\n\x07website\x18\x04 \x01(\t\x12\x13\n\x0bdescription\x18\x05 \x01(\t"X\n\x1eMsgUpdateProviderStatusRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x12)\n\x06status\x18\x02 \x01(\x0e2\x19.sentinel.types.v1.Status"Y\n\x16MsgUpdateParamsRequest\x12\x0b\n\x03frm\x18\x01 \x01(\t\x122\n\x06params\x18\x02 \x01(\x0b2\x1c.sentinel.provider.v3.ParamsB\x04\xc8\xde\x1f\x00"\x1d\n\x1bMsgRegisterProviderResponse""\n MsgUpdateProviderDetailsResponse"!\n\x1fMsgUpdateProviderStatusResponse"\x19\n\x17MsgUpdateParamsResponse2\x8d\x04\n\nMsgService\x12z\n\x13MsgRegisterProvider\x120.sentinel.provider.v3.MsgRegisterProviderRequest\x1a1.sentinel.provider.v3.MsgRegisterProviderResponse\x12\x89\x01\n\x18MsgUpdateProviderDetails\x125.sentinel.provider.v3.MsgUpdateProviderDetailsRequest\x1a6.sentinel.provider.v3.MsgUpdateProviderDetailsResponse\x12\x86\x01\n\x17MsgUpdateProviderStatus\x124.sentinel.provider.v3.MsgUpdateProviderStatusRequest\x1a5.sentinel.provider.v3.MsgUpdateProviderStatusResponse\x12n\n\x0fMsgUpdateParams\x12,.sentinel.provider.v3.MsgUpdateParamsRequest\x1a-.sentinel.provider.v3.MsgUpdateParamsResponseBJZ@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.provider.v3.msg_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z@github.com/sentinel-official/sentinelhub/v12/x/provider/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._loaded_options = None
    _globals['_MSGUPDATEPARAMSREQUEST'].fields_by_name['params']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_MSGREGISTERPROVIDERREQUEST']._serialized_start = 145
    _globals['_MSGREGISTERPROVIDERREQUEST']._serialized_end = 256
    _globals['_MSGUPDATEPROVIDERDETAILSREQUEST']._serialized_start = 258
    _globals['_MSGUPDATEPROVIDERDETAILSREQUEST']._serialized_end = 374
    _globals['_MSGUPDATEPROVIDERSTATUSREQUEST']._serialized_start = 376
    _globals['_MSGUPDATEPROVIDERSTATUSREQUEST']._serialized_end = 464
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_start = 466
    _globals['_MSGUPDATEPARAMSREQUEST']._serialized_end = 555
    _globals['_MSGREGISTERPROVIDERRESPONSE']._serialized_start = 557
    _globals['_MSGREGISTERPROVIDERRESPONSE']._serialized_end = 586
    _globals['_MSGUPDATEPROVIDERDETAILSRESPONSE']._serialized_start = 588
    _globals['_MSGUPDATEPROVIDERDETAILSRESPONSE']._serialized_end = 622
    _globals['_MSGUPDATEPROVIDERSTATUSRESPONSE']._serialized_start = 624
    _globals['_MSGUPDATEPROVIDERSTATUSRESPONSE']._serialized_end = 657
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_start = 659
    _globals['_MSGUPDATEPARAMSRESPONSE']._serialized_end = 684
    _globals['_MSGSERVICE']._serialized_start = 687
    _globals['_MSGSERVICE']._serialized_end = 1212