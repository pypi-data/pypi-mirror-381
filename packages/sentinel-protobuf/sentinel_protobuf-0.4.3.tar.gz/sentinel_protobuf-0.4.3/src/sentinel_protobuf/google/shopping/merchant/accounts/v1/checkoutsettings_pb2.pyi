from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.shopping.type import types_pb2 as _types_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GetCheckoutSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CreateCheckoutSettingsRequest(_message.Message):
    __slots__ = ('parent', 'checkout_settings')
    PARENT_FIELD_NUMBER: _ClassVar[int]
    CHECKOUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    parent: str
    checkout_settings: CheckoutSettings

    def __init__(self, parent: _Optional[str]=..., checkout_settings: _Optional[_Union[CheckoutSettings, _Mapping]]=...) -> None:
        ...

class UpdateCheckoutSettingsRequest(_message.Message):
    __slots__ = ('checkout_settings', 'update_mask')
    CHECKOUT_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    checkout_settings: CheckoutSettings
    update_mask: _field_mask_pb2.FieldMask

    def __init__(self, checkout_settings: _Optional[_Union[CheckoutSettings, _Mapping]]=..., update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=...) -> None:
        ...

class DeleteCheckoutSettingsRequest(_message.Message):
    __slots__ = ('name',)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str

    def __init__(self, name: _Optional[str]=...) -> None:
        ...

class CheckoutSettings(_message.Message):
    __slots__ = ('name', 'uri_settings', 'eligible_destinations', 'enrollment_state', 'review_state', 'effective_uri_settings', 'effective_enrollment_state', 'effective_review_state')

    class CheckoutEnrollmentState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED: _ClassVar[CheckoutSettings.CheckoutEnrollmentState]
        INACTIVE: _ClassVar[CheckoutSettings.CheckoutEnrollmentState]
        ENROLLED: _ClassVar[CheckoutSettings.CheckoutEnrollmentState]
        OPTED_OUT: _ClassVar[CheckoutSettings.CheckoutEnrollmentState]
    CHECKOUT_ENROLLMENT_STATE_UNSPECIFIED: CheckoutSettings.CheckoutEnrollmentState
    INACTIVE: CheckoutSettings.CheckoutEnrollmentState
    ENROLLED: CheckoutSettings.CheckoutEnrollmentState
    OPTED_OUT: CheckoutSettings.CheckoutEnrollmentState

    class CheckoutReviewState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CHECKOUT_REVIEW_STATE_UNSPECIFIED: _ClassVar[CheckoutSettings.CheckoutReviewState]
        IN_REVIEW: _ClassVar[CheckoutSettings.CheckoutReviewState]
        APPROVED: _ClassVar[CheckoutSettings.CheckoutReviewState]
        DISAPPROVED: _ClassVar[CheckoutSettings.CheckoutReviewState]
    CHECKOUT_REVIEW_STATE_UNSPECIFIED: CheckoutSettings.CheckoutReviewState
    IN_REVIEW: CheckoutSettings.CheckoutReviewState
    APPROVED: CheckoutSettings.CheckoutReviewState
    DISAPPROVED: CheckoutSettings.CheckoutReviewState
    NAME_FIELD_NUMBER: _ClassVar[int]
    URI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    ELIGIBLE_DESTINATIONS_FIELD_NUMBER: _ClassVar[int]
    ENROLLMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    REVIEW_STATE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_URI_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_ENROLLMENT_STATE_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_REVIEW_STATE_FIELD_NUMBER: _ClassVar[int]
    name: str
    uri_settings: UriSettings
    eligible_destinations: _containers.RepeatedScalarFieldContainer[_types_pb2.Destination.DestinationEnum]
    enrollment_state: CheckoutSettings.CheckoutEnrollmentState
    review_state: CheckoutSettings.CheckoutReviewState
    effective_uri_settings: UriSettings
    effective_enrollment_state: CheckoutSettings.CheckoutEnrollmentState
    effective_review_state: CheckoutSettings.CheckoutReviewState

    def __init__(self, name: _Optional[str]=..., uri_settings: _Optional[_Union[UriSettings, _Mapping]]=..., eligible_destinations: _Optional[_Iterable[_Union[_types_pb2.Destination.DestinationEnum, str]]]=..., enrollment_state: _Optional[_Union[CheckoutSettings.CheckoutEnrollmentState, str]]=..., review_state: _Optional[_Union[CheckoutSettings.CheckoutReviewState, str]]=..., effective_uri_settings: _Optional[_Union[UriSettings, _Mapping]]=..., effective_enrollment_state: _Optional[_Union[CheckoutSettings.CheckoutEnrollmentState, str]]=..., effective_review_state: _Optional[_Union[CheckoutSettings.CheckoutReviewState, str]]=...) -> None:
        ...

class UriSettings(_message.Message):
    __slots__ = ('checkout_uri_template', 'cart_uri_template')
    CHECKOUT_URI_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    CART_URI_TEMPLATE_FIELD_NUMBER: _ClassVar[int]
    checkout_uri_template: str
    cart_uri_template: str

    def __init__(self, checkout_uri_template: _Optional[str]=..., cart_uri_template: _Optional[str]=...) -> None:
        ...