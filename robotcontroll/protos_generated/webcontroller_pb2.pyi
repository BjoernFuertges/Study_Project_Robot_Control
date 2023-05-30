from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class MoveInformationReply(_message.Message):
    __slots__ = ["direction", "name", "radius", "speed", "stop", "turn"]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    TURN_FIELD_NUMBER: _ClassVar[int]
    direction: str
    name: str
    radius: float
    speed: int
    stop: bool
    turn: str
    def __init__(self, name: _Optional[str] = ..., stop: bool = ..., speed: _Optional[int] = ..., direction: _Optional[str] = ..., turn: _Optional[str] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...
