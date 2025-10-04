"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(_runtime_version.Domain.PUBLIC, 5, 29, 0, '', 'ibc/applications/fee/v1/genesis.proto')
_sym_db = _symbol_database.Default()
from .....gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from .....ibc.applications.fee.v1 import fee_pb2 as ibc_dot_applications_dot_fee_dot_v1_dot_fee__pb2
from .....ibc.core.channel.v1 import channel_pb2 as ibc_dot_core_dot_channel_dot_v1_dot_channel__pb2
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%ibc/applications/fee/v1/genesis.proto\x12\x17ibc.applications.fee.v1\x1a\x14gogoproto/gogo.proto\x1a!ibc/applications/fee/v1/fee.proto\x1a!ibc/core/channel/v1/channel.proto"\xc5\x04\n\x0cGenesisState\x12f\n\x0fidentified_fees\x18\x01 \x03(\x0b2-.ibc.applications.fee.v1.IdentifiedPacketFeesB\x1e\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"identified_fees"\x12m\n\x14fee_enabled_channels\x18\x02 \x03(\x0b2*.ibc.applications.fee.v1.FeeEnabledChannelB#\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"fee_enabled_channels"\x12e\n\x11registered_payees\x18\x03 \x03(\x0b2(.ibc.applications.fee.v1.RegisteredPayeeB \xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"registered_payees"\x12\x8b\x01\n\x1eregistered_counterparty_payees\x18\x04 \x03(\x0b24.ibc.applications.fee.v1.RegisteredCounterpartyPayeeB-\xc8\xde\x1f\x00\xf2\xde\x1f%yaml:"registered_counterparty_payees"\x12i\n\x10forward_relayers\x18\x05 \x03(\x0b2..ibc.applications.fee.v1.ForwardRelayerAddressB\x1f\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"forward_relayers""c\n\x11FeeEnabledChannel\x12#\n\x07port_id\x18\x01 \x01(\tB\x12\xf2\xde\x1f\x0eyaml:"port_id"\x12)\n\nchannel_id\x18\x02 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id""\\\n\x0fRegisteredPayee\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x12\r\n\x05payee\x18\x03 \x01(\t"\x94\x01\n\x1bRegisteredCounterpartyPayee\x12)\n\nchannel_id\x18\x01 \x01(\tB\x15\xf2\xde\x1f\x11yaml:"channel_id"\x12\x0f\n\x07relayer\x18\x02 \x01(\t\x129\n\x12counterparty_payee\x18\x03 \x01(\tB\x1d\xf2\xde\x1f\x19yaml:"counterparty_payee""t\n\x15ForwardRelayerAddress\x12\x0f\n\x07address\x18\x01 \x01(\t\x12J\n\tpacket_id\x18\x02 \x01(\x0b2\x1d.ibc.core.channel.v1.PacketIdB\x18\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"B7Z5github.com/cosmos/ibc-go/v7/modules/apps/29-fee/typesb\x06proto3')
_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ibc.applications.fee.v1.genesis_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    _globals['DESCRIPTOR']._loaded_options = None
    _globals['DESCRIPTOR']._serialized_options = b'Z5github.com/cosmos/ibc-go/v7/modules/apps/29-fee/types'
    _globals['_GENESISSTATE'].fields_by_name['identified_fees']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['identified_fees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x16yaml:"identified_fees"'
    _globals['_GENESISSTATE'].fields_by_name['fee_enabled_channels']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['fee_enabled_channels']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x1byaml:"fee_enabled_channels"'
    _globals['_GENESISSTATE'].fields_by_name['registered_payees']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['registered_payees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x18yaml:"registered_payees"'
    _globals['_GENESISSTATE'].fields_by_name['registered_counterparty_payees']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['registered_counterparty_payees']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f%yaml:"registered_counterparty_payees"'
    _globals['_GENESISSTATE'].fields_by_name['forward_relayers']._loaded_options = None
    _globals['_GENESISSTATE'].fields_by_name['forward_relayers']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x17yaml:"forward_relayers"'
    _globals['_FEEENABLEDCHANNEL'].fields_by_name['port_id']._loaded_options = None
    _globals['_FEEENABLEDCHANNEL'].fields_by_name['port_id']._serialized_options = b'\xf2\xde\x1f\x0eyaml:"port_id"'
    _globals['_FEEENABLEDCHANNEL'].fields_by_name['channel_id']._loaded_options = None
    _globals['_FEEENABLEDCHANNEL'].fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _globals['_REGISTEREDPAYEE'].fields_by_name['channel_id']._loaded_options = None
    _globals['_REGISTEREDPAYEE'].fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _globals['_REGISTEREDCOUNTERPARTYPAYEE'].fields_by_name['channel_id']._loaded_options = None
    _globals['_REGISTEREDCOUNTERPARTYPAYEE'].fields_by_name['channel_id']._serialized_options = b'\xf2\xde\x1f\x11yaml:"channel_id"'
    _globals['_REGISTEREDCOUNTERPARTYPAYEE'].fields_by_name['counterparty_payee']._loaded_options = None
    _globals['_REGISTEREDCOUNTERPARTYPAYEE'].fields_by_name['counterparty_payee']._serialized_options = b'\xf2\xde\x1f\x19yaml:"counterparty_payee"'
    _globals['_FORWARDRELAYERADDRESS'].fields_by_name['packet_id']._loaded_options = None
    _globals['_FORWARDRELAYERADDRESS'].fields_by_name['packet_id']._serialized_options = b'\xc8\xde\x1f\x00\xf2\xde\x1f\x10yaml:"packet_id"'
    _globals['_GENESISSTATE']._serialized_start = 159
    _globals['_GENESISSTATE']._serialized_end = 740
    _globals['_FEEENABLEDCHANNEL']._serialized_start = 742
    _globals['_FEEENABLEDCHANNEL']._serialized_end = 841
    _globals['_REGISTEREDPAYEE']._serialized_start = 843
    _globals['_REGISTEREDPAYEE']._serialized_end = 935
    _globals['_REGISTEREDCOUNTERPARTYPAYEE']._serialized_start = 938
    _globals['_REGISTEREDCOUNTERPARTYPAYEE']._serialized_end = 1086
    _globals['_FORWARDRELAYERADDRESS']._serialized_start = 1088
    _globals['_FORWARDRELAYERADDRESS']._serialized_end = 1204