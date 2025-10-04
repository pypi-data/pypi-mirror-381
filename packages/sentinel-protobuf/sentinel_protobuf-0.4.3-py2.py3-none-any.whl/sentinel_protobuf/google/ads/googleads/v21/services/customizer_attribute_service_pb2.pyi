from google.ads.googleads.v21.enums import response_content_type_pb2 as _response_content_type_pb2
from google.ads.googleads.v21.resources import customizer_attribute_pb2 as _customizer_attribute_pb2
from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import field_mask_pb2 as _field_mask_pb2
from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class MutateCustomizerAttributesRequest(_message.Message):
    __slots__ = ('customer_id', 'operations', 'partial_failure', 'validate_only', 'response_content_type')
    CUSTOMER_ID_FIELD_NUMBER: _ClassVar[int]
    OPERATIONS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ONLY_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
    customer_id: str
    operations: _containers.RepeatedCompositeFieldContainer[CustomizerAttributeOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: _response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType

    def __init__(self, customer_id: _Optional[str]=..., operations: _Optional[_Iterable[_Union[CustomizerAttributeOperation, _Mapping]]]=..., partial_failure: bool=..., validate_only: bool=..., response_content_type: _Optional[_Union[_response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType, str]]=...) -> None:
        ...

class CustomizerAttributeOperation(_message.Message):
    __slots__ = ('update_mask', 'create', 'remove')
    UPDATE_MASK_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    REMOVE_FIELD_NUMBER: _ClassVar[int]
    update_mask: _field_mask_pb2.FieldMask
    create: _customizer_attribute_pb2.CustomizerAttribute
    remove: str

    def __init__(self, update_mask: _Optional[_Union[_field_mask_pb2.FieldMask, _Mapping]]=..., create: _Optional[_Union[_customizer_attribute_pb2.CustomizerAttribute, _Mapping]]=..., remove: _Optional[str]=...) -> None:
        ...

class MutateCustomizerAttributesResponse(_message.Message):
    __slots__ = ('results', 'partial_failure_error')
    RESULTS_FIELD_NUMBER: _ClassVar[int]
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: _ClassVar[int]
    results: _containers.RepeatedCompositeFieldContainer[MutateCustomizerAttributeResult]
    partial_failure_error: _status_pb2.Status

    def __init__(self, results: _Optional[_Iterable[_Union[MutateCustomizerAttributeResult, _Mapping]]]=..., partial_failure_error: _Optional[_Union[_status_pb2.Status, _Mapping]]=...) -> None:
        ...

class MutateCustomizerAttributeResult(_message.Message):
    __slots__ = ('resource_name', 'customizer_attribute')
    RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
    CUSTOMIZER_ATTRIBUTE_FIELD_NUMBER: _ClassVar[int]
    resource_name: str
    customizer_attribute: _customizer_attribute_pb2.CustomizerAttribute

    def __init__(self, resource_name: _Optional[str]=..., customizer_attribute: _Optional[_Union[_customizer_attribute_pb2.CustomizerAttribute, _Mapping]]=...) -> None:
        ...