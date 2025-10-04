from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class OmnichannelSetting(_message.Message):
    __slots__ = ('name', 'region_code', 'lsf_type', 'in_stock', 'pickup', 'lfp_link', 'odo', 'about', 'inventory_verification')

    class LsfType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LSF_TYPE_UNSPECIFIED: _ClassVar[OmnichannelSetting.LsfType]
        GHLSF: _ClassVar[OmnichannelSetting.LsfType]
        MHLSF_BASIC: _ClassVar[OmnichannelSetting.LsfType]
        MHLSF_FULL: _ClassVar[OmnichannelSetting.LsfType]
    LSF_TYPE_UNSPECIFIED: OmnichannelSetting.LsfType
    GHLSF: OmnichannelSetting.LsfType
    MHLSF_BASIC: OmnichannelSetting.LsfType
    MHLSF_FULL: OmnichannelSetting.LsfType
    NAME_FIELD_NUMBER: _ClassVar[int]
    REGION_CODE_FIELD_NUMBER: _ClassVar[int]
    LSF_TYPE_FIELD_NUMBER: _ClassVar[int]
    IN_STOCK_FIELD_NUMBER: _ClassVar[int]
    PICKUP_FIELD_NUMBER: _ClassVar[int]
    LFP_LINK_FIELD_NUMBER: _ClassVar[int]
    ODO_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_VERIFICATION_FIELD_NUMBER: _ClassVar[int]
    name: str
    region_code: str
    lsf_type: OmnichannelSetting.LsfType
    in_stock: InStock
    pickup: Pickup
    lfp_link: LfpLink
    odo: OnDisplayToOrder
    about: About
    inventory_verification: InventoryVerification

    def __init__(self, name: _Optional[str]=..., region_code: _Optional[str]=..., lsf_type: _Optional[_Union[OmnichannelSetting.LsfType, str]]=..., in_stock: _Optional[_Union[InStock, _Mapping]]=..., pickup: _Optional[_Union[Pickup, _Mapping]]=..., lfp_link: _Optional[_Union[LfpLink, _Mapping]]=..., odo: _Optional[_Union[OnDisplayToOrder, _Mapping]]=..., about: _Optional[_Union[About, _Mapping]]=..., inventory_verification: _Optional[_Union[InventoryVerification, _Mapping]]=...) -> None:
        ...

class ReviewState(_message.Message):
    __slots__ = ()

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[ReviewState.State]
        ACTIVE: _ClassVar[ReviewState.State]
        FAILED: _ClassVar[ReviewState.State]
        RUNNING: _ClassVar[ReviewState.State]
        ACTION_REQUIRED: _ClassVar[ReviewState.State]
    STATE_UNSPECIFIED: ReviewState.State
    ACTIVE: ReviewState.State
    FAILED: ReviewState.State
    RUNNING: ReviewState.State
    ACTION_REQUIRED: ReviewState.State

    def __init__(self) -> None:
        ...

class InStock(_message.Message):
    __slots__ = ('uri', 'state')
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    state: ReviewState.State

    def __init__(self, uri: _Optional[str]=..., state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class Pickup(_message.Message):
    __slots__ = ('uri', 'state')
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    state: ReviewState.State

    def __init__(self, uri: _Optional[str]=..., state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class LfpLink(_message.Message):
    __slots__ = ('lfp_provider', 'external_account_id', 'state')
    LFP_PROVIDER_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_ACCOUNT_ID_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    lfp_provider: str
    external_account_id: str
    state: ReviewState.State

    def __init__(self, lfp_provider: _Optional[str]=..., external_account_id: _Optional[str]=..., state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class OnDisplayToOrder(_message.Message):
    __slots__ = ('uri', 'state')
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    state: ReviewState.State

    def __init__(self, uri: _Optional[str]=..., state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class About(_message.Message):
    __slots__ = ('uri', 'state')
    URI_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    uri: str
    state: ReviewState.State

    def __init__(self, uri: _Optional[str]=..., state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class InventoryVerification(_message.Message):
    __slots__ = ('state', 'contact', 'contact_email', 'contact_state')

    class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        STATE_UNSPECIFIED: _ClassVar[InventoryVerification.State]
        ACTION_REQUIRED: _ClassVar[InventoryVerification.State]
        INACTIVE: _ClassVar[InventoryVerification.State]
        RUNNING: _ClassVar[InventoryVerification.State]
        SUCCEEDED: _ClassVar[InventoryVerification.State]
        SUSPENDED: _ClassVar[InventoryVerification.State]
    STATE_UNSPECIFIED: InventoryVerification.State
    ACTION_REQUIRED: InventoryVerification.State
    INACTIVE: InventoryVerification.State
    RUNNING: InventoryVerification.State
    SUCCEEDED: InventoryVerification.State
    SUSPENDED: InventoryVerification.State
    STATE_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CONTACT_EMAIL_FIELD_NUMBER: _ClassVar[int]
    CONTACT_STATE_FIELD_NUMBER: _ClassVar[int]
    state: InventoryVerification.State
    contact: str
    contact_email: str
    contact_state: ReviewState.State

    def __init__(self, state: _Optional[_Union[InventoryVerification.State, str]]=..., contact: _Optional[str]=..., contact_email: _Optional[str]=..., contact_state: _Optional[_Union[ReviewState.State, str]]=...) -> None:
        ...

class GetOmnichannelSettingRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class ListOmnichannelSettingsRequest(_message.Message):
    __slots__ = ('parent', 'page_size', 'page_token')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PAGE_SIZE_FIELD_NUMBER: _ClassVar[int]
    PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    parent: str
    page_size: int
    page_token: str

    def __init__(self, parent: _Optional[str]=..., page_size: _Optional[int]=..., page_token: _Optional[str]=...) -> None:
        ...

class ListOmnichannelSettingsResponse(_message.Message):
    __slots__ = ('omnichannel_settings', 'next_page_token')
    OMNICHANNEL_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    NEXT_PAGE_TOKEN_FIELD_NUMBER: _ClassVar[int]
    omnichannel_settings: _containers.RepeatedCompositeFieldContainer[OmnichannelSetting]
    next_page_token: str

    def __init__(self, omnichannel_settings: _Optional[_Iterable[_Union[OmnichannelSetting, _Mapping]]]=..., next_page_token: _Optional[str]=...) -> None:
        ...

class CreateOmnichannelSettingRequest(_message.Message):
    __slots__ = ('parent', 'omnichannel_setting')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    OMNICHANNEL_SETTING_FIELD_NUMBER: _ClassVar[int]
    parent: str
    omnichannel_setting: OmnichannelSetting

    def __init__(self, parent: _Optional[str]=..., omnichannel_setting: _Optional[_Union[OmnichannelSetting, _Mapping]]=...) -> None:
        ...

class UpdateOmnichannelSettingRequest(_message.Message):
    __slots__ = ('omnichannel_setting', 'update_mask')
    OMNICHANNEL_SETTING_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    omnichannel_setting: OmnichannelSetting
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, omnichannel_setting: _Optional[_Union[OmnichannelSetting, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class RequestInventoryVerificationRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class RequestInventoryVerificationResponse(_message.Message):
    __slots__ = ('omnichannel_setting',)
    OMNICHANNEL_SETTING_FIELD_NUMBER: _ClassVar[int]
    omnichannel_setting: OmnichannelSetting

    def __init__(self, omnichannel_setting: _Optional[_Union[OmnichannelSetting, _Mapping]]=...) -> None:
        ...