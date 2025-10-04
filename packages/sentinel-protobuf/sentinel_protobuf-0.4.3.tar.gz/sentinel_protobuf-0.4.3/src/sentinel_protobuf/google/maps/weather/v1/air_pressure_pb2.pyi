from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class AirPressure(_message.Message):
    __slots__ = ('mean_sea_level_millibars',)
    MEAN_SEA_LEVEL_MILLIBARS_FIELD_NUMBER: _ClassVar[int]
    mean_sea_level_millibars: float

    def __init__(self, mean_sea_level_millibars: _Optional[float]=...) -> None:
        ...