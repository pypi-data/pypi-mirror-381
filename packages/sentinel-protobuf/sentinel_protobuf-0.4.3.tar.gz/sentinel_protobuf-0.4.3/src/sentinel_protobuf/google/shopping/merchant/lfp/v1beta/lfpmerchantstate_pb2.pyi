from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class LfpMerchantState(_message.Message):
    __slots__ = ('name', 'linked_gbps', 'store_states', 'inventory_stats', 'country_settings')

    class LfpStoreState(_message.Message):
        __slots__ = ('store_code', 'matching_state', 'matching_state_hint')

        class StoreMatchingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STORE_MATCHING_STATE_UNSPECIFIED: _ClassVar[LfpMerchantState.LfpStoreState.StoreMatchingState]
            STORE_MATCHING_STATE_MATCHED: _ClassVar[LfpMerchantState.LfpStoreState.StoreMatchingState]
            STORE_MATCHING_STATE_FAILED: _ClassVar[LfpMerchantState.LfpStoreState.StoreMatchingState]
        STORE_MATCHING_STATE_UNSPECIFIED: LfpMerchantState.LfpStoreState.StoreMatchingState
        STORE_MATCHING_STATE_MATCHED: LfpMerchantState.LfpStoreState.StoreMatchingState
        STORE_MATCHING_STATE_FAILED: LfpMerchantState.LfpStoreState.StoreMatchingState
        STORE_CODE_FIELD_NUMBER: _ClassVar[int]
        MATCHING_STATE_FIELD_NUMBER: _ClassVar[int]
        MATCHING_STATE_HINT_FIELD_NUMBER: _ClassVar[int]
        store_code: str
        matching_state: LfpMerchantState.LfpStoreState.StoreMatchingState
        matching_state_hint: str

        def __init__(self, store_code: _Optional[str]=..., matching_state: _Optional[_Union[LfpMerchantState.LfpStoreState.StoreMatchingState, str]]=..., matching_state_hint: _Optional[str]=...) -> None:
            ...

    class InventoryStats(_message.Message):
        __slots__ = ('submitted_entries', 'submitted_in_stock_entries', 'unsubmitted_entries', 'submitted_products')
        SUBMITTED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_IN_STOCK_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        UNSUBMITTED_ENTRIES_FIELD_NUMBER: _ClassVar[int]
        SUBMITTED_PRODUCTS_FIELD_NUMBER: _ClassVar[int]
        submitted_entries: int
        submitted_in_stock_entries: int
        unsubmitted_entries: int
        submitted_products: int

        def __init__(self, submitted_entries: _Optional[int]=..., submitted_in_stock_entries: _Optional[int]=..., unsubmitted_entries: _Optional[int]=..., submitted_products: _Optional[int]=...) -> None:
            ...

    class CountrySettings(_message.Message):
        __slots__ = ('region_code', 'free_local_listings_enabled', 'local_inventory_ads_enabled', 'inventory_verification_state', 'product_page_type', 'instock_serving_verification_state', 'pickup_serving_verification_state')

        class VerificationState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VERIFICATION_STATE_UNSPECIFIED: _ClassVar[LfpMerchantState.CountrySettings.VerificationState]
            VERIFICATION_STATE_NOT_APPROVED: _ClassVar[LfpMerchantState.CountrySettings.VerificationState]
            VERIFICATION_STATE_IN_PROGRESS: _ClassVar[LfpMerchantState.CountrySettings.VerificationState]
            VERIFICATION_STATE_APPROVED: _ClassVar[LfpMerchantState.CountrySettings.VerificationState]
        VERIFICATION_STATE_UNSPECIFIED: LfpMerchantState.CountrySettings.VerificationState
        VERIFICATION_STATE_NOT_APPROVED: LfpMerchantState.CountrySettings.VerificationState
        VERIFICATION_STATE_IN_PROGRESS: LfpMerchantState.CountrySettings.VerificationState
        VERIFICATION_STATE_APPROVED: LfpMerchantState.CountrySettings.VerificationState

        class ProductPageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRODUCT_PAGE_TYPE_UNSPECIFIED: _ClassVar[LfpMerchantState.CountrySettings.ProductPageType]
            GOOGLE_HOSTED: _ClassVar[LfpMerchantState.CountrySettings.ProductPageType]
            MERCHANT_HOSTED: _ClassVar[LfpMerchantState.CountrySettings.ProductPageType]
            MERCHANT_HOSTED_STORE_SPECIFIC: _ClassVar[LfpMerchantState.CountrySettings.ProductPageType]
        PRODUCT_PAGE_TYPE_UNSPECIFIED: LfpMerchantState.CountrySettings.ProductPageType
        GOOGLE_HOSTED: LfpMerchantState.CountrySettings.ProductPageType
        MERCHANT_HOSTED: LfpMerchantState.CountrySettings.ProductPageType
        MERCHANT_HOSTED_STORE_SPECIFIC: LfpMerchantState.CountrySettings.ProductPageType
        REGION_CODE_FIELD_NUMBER: _ClassVar[int]
        FREE_LOCAL_LISTINGS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        LOCAL_INVENTORY_ADS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        INVENTORY_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        PRODUCT_PAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        INSTOCK_SERVING_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        PICKUP_SERVING_VERIFICATION_STATE_FIELD_NUMBER: _ClassVar[int]
        region_code: str
        free_local_listings_enabled: bool
        local_inventory_ads_enabled: bool
        inventory_verification_state: LfpMerchantState.CountrySettings.VerificationState
        product_page_type: LfpMerchantState.CountrySettings.ProductPageType
        instock_serving_verification_state: LfpMerchantState.CountrySettings.VerificationState
        pickup_serving_verification_state: LfpMerchantState.CountrySettings.VerificationState

        def __init__(self, region_code: _Optional[str]=..., free_local_listings_enabled: bool=..., local_inventory_ads_enabled: bool=..., inventory_verification_state: _Optional[_Union[LfpMerchantState.CountrySettings.VerificationState, str]]=..., product_page_type: _Optional[_Union[LfpMerchantState.CountrySettings.ProductPageType, str]]=..., instock_serving_verification_state: _Optional[_Union[LfpMerchantState.CountrySettings.VerificationState, str]]=..., pickup_serving_verification_state: _Optional[_Union[LfpMerchantState.CountrySettings.VerificationState, str]]=...) -> None:
            ...
    NAME_FIELD_NUMBER: _ClassVar[int]
    LINKED_GBPS_FIELD_NUMBER: _ClassVar[int]
    STORE_STATES_FIELD_NUMBER: _ClassVar[int]
    INVENTORY_STATS_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    name: str
    linked_gbps: int
    store_states: _containers.RepeatedCompositeFieldContainer[LfpMerchantState.LfpStoreState]
    inventory_stats: LfpMerchantState.InventoryStats
    country_settings: _containers.RepeatedCompositeFieldContainer[LfpMerchantState.CountrySettings]

    def __init__(self, name: _Optional[str]=..., linked_gbps: _Optional[int]=..., store_states: _Optional[_Iterable[_Union[LfpMerchantState.LfpStoreState, _Mapping]]]=..., inventory_stats: _Optional[_Union[LfpMerchantState.InventoryStats, _Mapping]]=..., country_settings: _Optional[_Iterable[_Union[LfpMerchantState.CountrySettings, _Mapping]]]=...) -> None:
        ...

class GetLfpMerchantStateRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...