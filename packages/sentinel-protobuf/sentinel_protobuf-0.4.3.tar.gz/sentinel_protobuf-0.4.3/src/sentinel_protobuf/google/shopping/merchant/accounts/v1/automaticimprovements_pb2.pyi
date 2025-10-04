from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class AutomaticImprovements(_message.Message):
    __slots__ = ('name', 'item_updates', 'image_improvements', 'shipping_improvements')
    NAME_FIELD_NUMBER: _ClassVar[int]
    ITEM_UPDATES_FIELD_NUMBER: _ClassVar[int]
    IMAGE_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
    SHIPPING_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
    name: str
    item_updates: AutomaticItemUpdates
    image_improvements: AutomaticImageImprovements
    shipping_improvements: AutomaticShippingImprovements

    def __init__(self, name: _Optional[str]=..., item_updates: _Optional[_Union[AutomaticItemUpdates, _Mapping]]=..., image_improvements: _Optional[_Union[AutomaticImageImprovements, _Mapping]]=..., shipping_improvements: _Optional[_Union[AutomaticShippingImprovements, _Mapping]]=...) -> None:
        ...

class AutomaticItemUpdates(_message.Message):
    __slots__ = ('account_item_updates_settings', 'effective_allow_price_updates', 'effective_allow_availability_updates', 'effective_allow_strict_availability_updates', 'effective_allow_condition_updates')

    class ItemUpdatesAccountLevelSettings(_message.Message):
        __slots__ = ('allow_price_updates', 'allow_availability_updates', 'allow_strict_availability_updates', 'allow_condition_updates')
        ALLOW_PRICE_UPDATES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_AVAILABILITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_STRICT_AVAILABILITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
        ALLOW_CONDITION_UPDATES_FIELD_NUMBER: _ClassVar[int]
        allow_price_updates: bool
        allow_availability_updates: bool
        allow_strict_availability_updates: bool
        allow_condition_updates: bool

        def __init__(self, allow_price_updates: bool=..., allow_availability_updates: bool=..., allow_strict_availability_updates: bool=..., allow_condition_updates: bool=...) -> None:
            ...
    ACCOUNT_ITEM_UPDATES_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ALLOW_PRICE_UPDATES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ALLOW_AVAILABILITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ALLOW_STRICT_AVAILABILITY_UPDATES_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ALLOW_CONDITION_UPDATES_FIELD_NUMBER: _ClassVar[int]
    account_item_updates_settings: AutomaticItemUpdates.ItemUpdatesAccountLevelSettings
    effective_allow_price_updates: bool
    effective_allow_availability_updates: bool
    effective_allow_strict_availability_updates: bool
    effective_allow_condition_updates: bool

    def __init__(self, account_item_updates_settings: _Optional[_Union[AutomaticItemUpdates.ItemUpdatesAccountLevelSettings, _Mapping]]=..., effective_allow_price_updates: bool=..., effective_allow_availability_updates: bool=..., effective_allow_strict_availability_updates: bool=..., effective_allow_condition_updates: bool=...) -> None:
        ...

class AutomaticImageImprovements(_message.Message):
    __slots__ = ('account_image_improvements_settings', 'effective_allow_automatic_image_improvements')

    class ImageImprovementsAccountLevelSettings(_message.Message):
        __slots__ = ('allow_automatic_image_improvements',)
        ALLOW_AUTOMATIC_IMAGE_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
        allow_automatic_image_improvements: bool

        def __init__(self, allow_automatic_image_improvements: bool=...) -> None:
            ...
    ACCOUNT_IMAGE_IMPROVEMENTS_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ALLOW_AUTOMATIC_IMAGE_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
    account_image_improvements_settings: AutomaticImageImprovements.ImageImprovementsAccountLevelSettings
    effective_allow_automatic_image_improvements: bool

    def __init__(self, account_image_improvements_settings: _Optional[_Union[AutomaticImageImprovements.ImageImprovementsAccountLevelSettings, _Mapping]]=..., effective_allow_automatic_image_improvements: bool=...) -> None:
        ...

class AutomaticShippingImprovements(_message.Message):
    __slots__ = ('allow_shipping_improvements',)
    ALLOW_SHIPPING_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
    allow_shipping_improvements: bool

    def __init__(self, allow_shipping_improvements: bool=...) -> None:
        ...

class GetAutomaticImprovementsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class UpdateAutomaticImprovementsRequest(_message.Message):
    __slots__ = ('automatic_improvements', 'update_mask')
    AUTOMATIC_IMPROVEMENTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    automatic_improvements: AutomaticImprovements
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, automatic_improvements: _Optional[_Union[AutomaticImprovements, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...