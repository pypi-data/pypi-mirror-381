from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.cloud.universalledger.v1 import accounts_pb2 as _accounts_pb2
from google.cloud.universalledger.v1 import common_pb2 as _common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class FeePayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    FEE_PAYER_UNSPECIFIED: _ClassVar[FeePayer]
    FEE_PAYER_SENDER: _ClassVar[FeePayer]
    FEE_PAYER_RECEIVER: _ClassVar[FeePayer]
    FEE_PAYER_OTHER: _ClassVar[FeePayer]

class SettlementMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SETTLEMENT_MODE_UNSPECIFIED: _ClassVar[SettlementMode]
    SETTLEMENT_MODE_DEFERRED: _ClassVar[SettlementMode]
    SETTLEMENT_MODE_INSTANT: _ClassVar[SettlementMode]
FEE_PAYER_UNSPECIFIED: FeePayer
FEE_PAYER_SENDER: FeePayer
FEE_PAYER_RECEIVER: FeePayer
FEE_PAYER_OTHER: FeePayer
SETTLEMENT_MODE_UNSPECIFIED: SettlementMode
SETTLEMENT_MODE_DEFERRED: SettlementMode
SETTLEMENT_MODE_INSTANT: SettlementMode

class FractionalFee(_message.Message):
    __slots__ = ('amount', 'fee_payer', 'fee_account')
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FEE_PAYER_FIELD_NUMBER: _ClassVar[int]
    FEE_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    amount: int
    fee_payer: FeePayer
    fee_account: _common_pb2.Entity

    def __init__(self, amount: _Optional[int]=..., fee_payer: _Optional[_Union[FeePayer, str]]=..., fee_account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class SettlementRequest(_message.Message):
    __slots__ = ('payer', 'beneficiary', 'balance', 'round_id')
    PAYER_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    ROUND_ID_FIELD_NUMBER: _ClassVar[int]
    payer: _common_pb2.Entity
    beneficiary: _common_pb2.Entity
    balance: _common_pb2.CurrencyValue
    round_id: int

    def __init__(self, payer: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., beneficiary: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., balance: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=..., round_id: _Optional[int]=...) -> None:
        ...

class CreateAccount(_message.Message):
    __slots__ = ('public_key', 'roles', 'account_status', 'account_comment', 'token_manager')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_STATUS_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    TOKEN_MANAGER_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    roles: _containers.RepeatedScalarFieldContainer[_accounts_pb2.Role]
    account_status: _accounts_pb2.AccountStatus
    account_comment: str
    token_manager: _common_pb2.Entity

    def __init__(self, public_key: _Optional[bytes]=..., roles: _Optional[_Iterable[_Union[_accounts_pb2.Role, str]]]=..., account_status: _Optional[_Union[_accounts_pb2.AccountStatus, str]]=..., account_comment: _Optional[str]=..., token_manager: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class DeactivateAccount(_message.Message):
    __slots__ = ('account',)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _common_pb2.Entity

    def __init__(self, account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class ActivateAccount(_message.Message):
    __slots__ = ('account',)
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    account: _common_pb2.Entity

    def __init__(self, account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class AddRoles(_message.Message):
    __slots__ = ('account', 'roles')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    account: _common_pb2.Entity
    roles: _containers.RepeatedScalarFieldContainer[_accounts_pb2.Role]

    def __init__(self, account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., roles: _Optional[_Iterable[_Union[_accounts_pb2.Role, str]]]=...) -> None:
        ...

class RemoveRoles(_message.Message):
    __slots__ = ('account', 'roles')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ROLES_FIELD_NUMBER: _ClassVar[int]
    account: _common_pb2.Entity
    roles: _containers.RepeatedScalarFieldContainer[_accounts_pb2.Role]

    def __init__(self, account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., roles: _Optional[_Iterable[_Union[_accounts_pb2.Role, str]]]=...) -> None:
        ...

class ChangeAccountManager(_message.Message):
    __slots__ = ('account', 'next_manager')
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    NEXT_MANAGER_FIELD_NUMBER: _ClassVar[int]
    account: _common_pb2.Entity
    next_manager: _common_pb2.Entity

    def __init__(self, account: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., next_manager: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class IncreaseTokenIssuanceLimit(_message.Message):
    __slots__ = ('token_manager', 'amount')
    TOKEN_MANAGER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_manager: _common_pb2.Entity
    amount: _common_pb2.CurrencyValue

    def __init__(self, token_manager: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., amount: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=...) -> None:
        ...

class DecreaseTokenIssuanceLimit(_message.Message):
    __slots__ = ('token_manager', 'amount')
    TOKEN_MANAGER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    token_manager: _common_pb2.Entity
    amount: _common_pb2.CurrencyValue

    def __init__(self, token_manager: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., amount: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=...) -> None:
        ...

class Mint(_message.Message):
    __slots__ = ('mint_amount', 'beneficiary')
    MINT_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BENEFICIARY_FIELD_NUMBER: _ClassVar[int]
    mint_amount: _common_pb2.CurrencyValue
    beneficiary: _common_pb2.Entity

    def __init__(self, mint_amount: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=..., beneficiary: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class Burn(_message.Message):
    __slots__ = ('burn_amount', 'payer')
    BURN_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    PAYER_FIELD_NUMBER: _ClassVar[int]
    burn_amount: _common_pb2.CurrencyValue
    payer: _common_pb2.Entity

    def __init__(self, burn_amount: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=..., payer: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class Transfer(_message.Message):
    __slots__ = ('beneficiary', 'amount', 'fractional_fee')
    BENEFICIARY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    FRACTIONAL_FEE_FIELD_NUMBER: _ClassVar[int]
    beneficiary: _common_pb2.Entity
    amount: _common_pb2.CurrencyValue
    fractional_fee: FractionalFee

    def __init__(self, beneficiary: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., amount: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=..., fractional_fee: _Optional[_Union[FractionalFee, _Mapping]]=...) -> None:
        ...

class CreateTokenManager(_message.Message):
    __slots__ = ('public_key', 'account_comment')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    account_comment: str

    def __init__(self, public_key: _Optional[bytes]=..., account_comment: _Optional[str]=...) -> None:
        ...

class CreateAccountManager(_message.Message):
    __slots__ = ('public_key', 'default_token_manager', 'account_comment')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_TOKEN_MANAGER_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    default_token_manager: _common_pb2.Entity
    account_comment: str

    def __init__(self, public_key: _Optional[bytes]=..., default_token_manager: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., account_comment: _Optional[str]=...) -> None:
        ...

class CreateClearinghouse(_message.Message):
    __slots__ = ('public_key', 'account_comment', 'settlement_mode')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    SETTLEMENT_MODE_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    account_comment: str
    settlement_mode: SettlementMode

    def __init__(self, public_key: _Optional[bytes]=..., account_comment: _Optional[str]=..., settlement_mode: _Optional[_Union[SettlementMode, str]]=...) -> None:
        ...

class TransferPlatformOperator(_message.Message):
    __slots__ = ('public_key', 'account_comment')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    account_comment: str

    def __init__(self, public_key: _Optional[bytes]=..., account_comment: _Optional[str]=...) -> None:
        ...

class CreateCurrencyOperator(_message.Message):
    __slots__ = ('public_key', 'account_comment', 'currency')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    account_comment: str
    currency: str

    def __init__(self, public_key: _Optional[bytes]=..., account_comment: _Optional[str]=..., currency: _Optional[str]=...) -> None:
        ...

class TransferCurrencyOperator(_message.Message):
    __slots__ = ('public_key', 'account_comment', 'currency_operator')
    PUBLIC_KEY_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_OPERATOR_FIELD_NUMBER: _ClassVar[int]
    public_key: bytes
    account_comment: str
    currency_operator: _common_pb2.Entity

    def __init__(self, public_key: _Optional[bytes]=..., account_comment: _Optional[str]=..., currency_operator: _Optional[_Union[_common_pb2.Entity, _Mapping]]=...) -> None:
        ...

class CreateSnapshot(_message.Message):
    __slots__ = ()

    def __init__(self) -> None:
        ...

class CreateContract(_message.Message):
    __slots__ = ('contract_bytes', 'arguments', 'contract_comment')

    class ArgumentsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_common_pb2.Value, _Mapping]]=...) -> None:
            ...
    CONTRACT_BYTES_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    CONTRACT_COMMENT_FIELD_NUMBER: _ClassVar[int]
    contract_bytes: bytes
    arguments: _containers.MessageMap[str, _common_pb2.Value]
    contract_comment: str

    def __init__(self, contract_bytes: _Optional[bytes]=..., arguments: _Optional[_Mapping[str, _common_pb2.Value]]=..., contract_comment: _Optional[str]=...) -> None:
        ...

class GrantContractPermissions(_message.Message):
    __slots__ = ('contract', 'permissions')
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2.Entity
    permissions: _containers.RepeatedScalarFieldContainer[_accounts_pb2.ContractPermission]

    def __init__(self, contract: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., permissions: _Optional[_Iterable[_Union[_accounts_pb2.ContractPermission, str]]]=...) -> None:
        ...

class InvokeContractMethod(_message.Message):
    __slots__ = ('contract', 'method_name', 'arguments', 'payment')

    class ArgumentsEntry(_message.Message):
        __slots__ = ('key', 'value')
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: _common_pb2.Value

        def __init__(self, key: _Optional[str]=..., value: _Optional[_Union[_common_pb2.Value, _Mapping]]=...) -> None:
            ...
    CONTRACT_FIELD_NUMBER: _ClassVar[int]
    METHOD_NAME_FIELD_NUMBER: _ClassVar[int]
    ARGUMENTS_FIELD_NUMBER: _ClassVar[int]
    PAYMENT_FIELD_NUMBER: _ClassVar[int]
    contract: _common_pb2.Entity
    method_name: str
    arguments: _containers.MessageMap[str, _common_pb2.Value]
    payment: _common_pb2.CurrencyValue

    def __init__(self, contract: _Optional[_Union[_common_pb2.Entity, _Mapping]]=..., method_name: _Optional[str]=..., arguments: _Optional[_Mapping[str, _common_pb2.Value]]=..., payment: _Optional[_Union[_common_pb2.CurrencyValue, _Mapping]]=...) -> None:
        ...