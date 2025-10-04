"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'sentinel/node/v3/session.proto')
_sym_db = _symbol_database.Default()
from ....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from ....sentinel.session.v3 import session_pb2 as sentinel_dot_session_dot_v3_dot_session__pb2
from ....sentinel.types.v1 import price_pb2 as sentinel_dot_types_dot_v1_dot_price__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1esentinel/node/v3/session.proto\x12\x10sentinel.node.v3\x1a\x14gogoproto/gogo.proto\x1a!sentinel/session/v3/session.proto\x1a\x1dsentinel/types/v1/price.proto"v\n\x07Session\x12<\n\x0cbase_session\x18\x01 \x01(\x0b2 .sentinel.session.v3.BaseSessionB\x04\xd0\xde\x1f\x01\x12-\n\x05price\x18\x02 \x01(\x0b2\x18.sentinel.types.v1.PriceB\x04\xc8\xde\x1f\x00BFZ<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00b\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'sentinel.node.v3.session_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z<github.com/sentinel-official/sentinelhub/v12/x/node/types/v3\xc8\xe1\x1e\x00\xa8\xe2\x1e\x00'
    _globals['_SESSION'].fields_by_name['base_session']._loaded_options = None
    _globals['_SESSION'].fields_by_name['base_session']._serialized_options = b'\xd0\xde\x1f\x01'
    _globals['_SESSION'].fields_by_name['price']._loaded_options = None
    _globals['_SESSION'].fields_by_name['price']._serialized_options = b'\xc8\xde\x1f\x00'
    _globals['_SESSION']._serialized_start = 140
    _globals['_SESSION']._serialized_end = 258