from google.ads.datamanager.v1 import cart_data_pb2 as _cart_data_pb2
from google.ads.datamanager.v1 import consent_pb2 as _consent_pb2
from google.ads.datamanager.v1 import device_info_pb2 as _device_info_pb2
from google.ads.datamanager.v1 import experimental_field_pb2 as _experimental_field_pb2
from google.ads.datamanager.v1 import user_data_pb2 as _user_data_pb2
from google.ads.datamanager.v1 import user_properties_pb2 as _user_properties_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class EventSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EVENT_SOURCE_UNSPECIFIED: _ClassVar[EventSource]
    WEB: _ClassVar[EventSource]
    APP: _ClassVar[EventSource]
    IN_STORE: _ClassVar[EventSource]
    PHONE: _ClassVar[EventSource]
    OTHER: _ClassVar[EventSource]
EVENT_SOURCE_UNSPECIFIED: EventSource
WEB: EventSource
APP: EventSource
IN_STORE: EventSource
PHONE: EventSource
OTHER: EventSource

class Event(_message.Message):
    __slots__ = ('destination_references', 'transaction_id', 'event_timestamp', 'last_updated_timestamp', 'user_data', 'consent', 'ad_identifiers', 'currency', 'conversion_value', 'event_source', 'event_device_info', 'cart_data', 'custom_variables', 'experimental_fields', 'user_properties')
    DESTINATION_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    TRANSACTION_ID_FIELD_NUMBER: _ClassVar[int]
    EVENT_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    LAST_UPDATED_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    USER_DATA_FIELD_NUMBER: _ClassVar[int]
    CONSENT_FIELD_NUMBER: _ClassVar[int]
    AD_IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    CONVERSION_VALUE_FIELD_NUMBER: _ClassVar[int]
    EVENT_SOURCE_FIELD_NUMBER: _ClassVar[int]
    EVENT_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    CART_DATA_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_VARIABLES_FIELD_NUMBER: _ClassVar[int]
    EXPERIMENTAL_FIELDS_FIELD_NUMBER: _ClassVar[int]
    USER_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    destination_references: _containers.RepeatedScalarFieldContainer[str]
    transaction_id: str
    event_timestamp: _timestamp_pb2.Timestamp
    last_updated_timestamp: _timestamp_pb2.Timestamp
    user_data: _user_data_pb2.UserData
    consent: _consent_pb2.Consent
    ad_identifiers: AdIdentifiers
    currency: str
    conversion_value: float
    event_source: EventSource
    event_device_info: _device_info_pb2.DeviceInfo
    cart_data: _cart_data_pb2.CartData
    custom_variables: _containers.RepeatedCompositeFieldContainer[CustomVariable]
    experimental_fields: _containers.RepeatedCompositeFieldContainer[_experimental_field_pb2.ExperimentalField]
    user_properties: _user_properties_pb2.UserProperties

    def __init__(self, destination_references: _Optional[_Iterable[str]]=..., transaction_id: _Optional[str]=..., event_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., last_updated_timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=..., user_data: _Optional[_Union[_user_data_pb2.UserData, _Mapping]]=..., consent: _Optional[_Union[_consent_pb2.Consent, _Mapping]]=..., ad_identifiers: _Optional[_Union[AdIdentifiers, _Mapping]]=..., currency: _Optional[str]=..., conversion_value: _Optional[float]=..., event_source: _Optional[_Union[EventSource, str]]=..., event_device_info: _Optional[_Union[_device_info_pb2.DeviceInfo, _Mapping]]=..., cart_data: _Optional[_Union[_cart_data_pb2.CartData, _Mapping]]=..., custom_variables: _Optional[_Iterable[_Union[CustomVariable, _Mapping]]]=..., experimental_fields: _Optional[_Iterable[_Union[_experimental_field_pb2.ExperimentalField, _Mapping]]]=..., user_properties: _Optional[_Union[_user_properties_pb2.UserProperties, _Mapping]]=...) -> None:
        ...

class AdIdentifiers(_message.Message):
    __slots__ = ('session_attributes', 'gclid', 'gbraid', 'wbraid', 'landing_page_device_info')
    SESSION_ATTRIBUTES_FIELD_NUMBER: _ClassVar[int]
    GCLID_FIELD_NUMBER: _ClassVar[int]
    GBRAID_FIELD_NUMBER: _ClassVar[int]
    WBRAID_FIELD_NUMBER: _ClassVar[int]
    LANDING_PAGE_DEVICE_INFO_FIELD_NUMBER: _ClassVar[int]
    session_attributes: str
    gclid: str
    gbraid: str
    wbraid: str
    landing_page_device_info: _device_info_pb2.DeviceInfo

    def __init__(self, session_attributes: _Optional[str]=..., gclid: _Optional[str]=..., gbraid: _Optional[str]=..., wbraid: _Optional[str]=..., landing_page_device_info: _Optional[_Union[_device_info_pb2.DeviceInfo, _Mapping]]=...) -> None:
        ...

class CustomVariable(_message.Message):
    __slots__ = ('variable', 'value', 'destination_references')
    VARIABLE_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_REFERENCES_FIELD_NUMBER: _ClassVar[int]
    variable: str
    value: str
    destination_references: _containers.RepeatedScalarFieldContainer[str]

    def __init__(self, variable: _Optional[str]=..., value: _Optional[str]=..., destination_references: _Optional[_Iterable[str]]=...) -> None:
        ...