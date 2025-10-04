from google.api import annotations_pb2 as _annotations_pb2
from google.api import client_pb2 as _client_pb2
from google.api import field_behavior_pb2 as _field_behavior_pb2
from google.api import resource_pb2 as _resource_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.shopping.merchant.productstudio.v1alpha import productstudio_common_pb2 as _productstudio_common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union
DESCRIPTOR: _descriptor.FileDescriptor

class GenerateProductImageBackgroundRequest(_message.Message):
    __slots__ = ('name', 'output_config', 'input_image', 'config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: OutputImageConfig
    input_image: _productstudio_common_pb2.InputImage
    config: GenerateImageBackgroundConfig

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[OutputImageConfig, _Mapping]]=..., input_image: _Optional[_Union[_productstudio_common_pb2.InputImage, _Mapping]]=..., config: _Optional[_Union[GenerateImageBackgroundConfig, _Mapping]]=...) -> None:
        ...

class GenerateProductImageBackgroundResponse(_message.Message):
    __slots__ = ('generated_image',)
    GENERATED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    generated_image: GeneratedImage

    def __init__(self, generated_image: _Optional[_Union[GeneratedImage, _Mapping]]=...) -> None:
        ...

class RemoveProductImageBackgroundRequest(_message.Message):
    __slots__ = ('name', 'output_config', 'input_image', 'config')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    CONFIG_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: OutputImageConfig
    input_image: _productstudio_common_pb2.InputImage
    config: RemoveImageBackgroundConfig

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[OutputImageConfig, _Mapping]]=..., input_image: _Optional[_Union[_productstudio_common_pb2.InputImage, _Mapping]]=..., config: _Optional[_Union[RemoveImageBackgroundConfig, _Mapping]]=...) -> None:
        ...

class RemoveProductImageBackgroundResponse(_message.Message):
    __slots__ = ('generated_image',)
    GENERATED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    generated_image: GeneratedImage

    def __init__(self, generated_image: _Optional[_Union[GeneratedImage, _Mapping]]=...) -> None:
        ...

class UpscaleProductImageRequest(_message.Message):
    __slots__ = ('name', 'output_config', 'input_image')
    NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUT_CONFIG_FIELD_NUMBER: _ClassVar[int]
    INPUT_IMAGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    output_config: OutputImageConfig
    input_image: _productstudio_common_pb2.InputImage

    def __init__(self, name: _Optional[str]=..., output_config: _Optional[_Union[OutputImageConfig, _Mapping]]=..., input_image: _Optional[_Union[_productstudio_common_pb2.InputImage, _Mapping]]=...) -> None:
        ...

class UpscaleProductImageResponse(_message.Message):
    __slots__ = ('generated_image',)
    GENERATED_IMAGE_FIELD_NUMBER: _ClassVar[int]
    generated_image: GeneratedImage

    def __init__(self, generated_image: _Optional[_Union[GeneratedImage, _Mapping]]=...) -> None:
        ...

class GeneratedImage(_message.Message):
    __slots__ = ('uri', 'image_bytes', 'name', 'generation_time')
    URI_FIELD_NUMBER: _ClassVar[int]
    IMAGE_BYTES_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GENERATION_TIME_FIELD_NUMBER: _ClassVar[int]
    uri: str
    image_bytes: bytes
    name: str
    generation_time: _timestamp_pb2.Timestamp

    def __init__(self, uri: _Optional[str]=..., image_bytes: _Optional[bytes]=..., name: _Optional[str]=..., generation_time: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]]=...) -> None:
        ...

class OutputImageConfig(_message.Message):
    __slots__ = ('return_image_uri',)
    RETURN_IMAGE_URI_FIELD_NUMBER: _ClassVar[int]
    return_image_uri: bool

    def __init__(self, return_image_uri: bool=...) -> None:
        ...

class GenerateImageBackgroundConfig(_message.Message):
    __slots__ = ('product_description', 'background_description')
    PRODUCT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    product_description: str
    background_description: str

    def __init__(self, product_description: _Optional[str]=..., background_description: _Optional[str]=...) -> None:
        ...

class RemoveImageBackgroundConfig(_message.Message):
    __slots__ = ('background_color',)
    BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
    background_color: RgbColor

    def __init__(self, background_color: _Optional[_Union[RgbColor, _Mapping]]=...) -> None:
        ...

class RgbColor(_message.Message):
    __slots__ = ('red', 'green', 'blue')
    RED_FIELD_NUMBER: _ClassVar[int]
    GREEN_FIELD_NUMBER: _ClassVar[int]
    BLUE_FIELD_NUMBER: _ClassVar[int]
    red: int
    green: int
    blue: int

    def __init__(self, red: _Optional[int]=..., green: _Optional[int]=..., blue: _Optional[int]=...) -> None:
        ...