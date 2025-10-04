from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional
DESCRIPTOR: _descriptor.FileDescriptor

class LoggedBackupPlanMetadata(_message.Message):
    __slots__ = ('backup_channel', 'rpo_risk_level', 'rpo_risk_reason')
    BACKUP_CHANNEL_FIELD_NUMBER: _ClassVar[int]
    RPO_RISK_LEVEL_FIELD_NUMBER: _ClassVar[int]
    RPO_RISK_REASON_FIELD_NUMBER: _ClassVar[int]
    backup_channel: str
    rpo_risk_level: int
    rpo_risk_reason: str

    def __init__(self, backup_channel: _Optional[str]=..., rpo_risk_level: _Optional[int]=..., rpo_risk_reason: _Optional[str]=...) -> None:
        ...