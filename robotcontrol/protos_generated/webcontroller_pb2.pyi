from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ImageChunk(_message.Message):
    __slots__ = ["chunk"]
    CHUNK_FIELD_NUMBER: _ClassVar[int]
    chunk: bytes
    def __init__(self, chunk: _Optional[bytes] = ...) -> None: ...

class MoveInformationHasNewReply(_message.Message):
    __slots__ = ["hasNew"]
    HASNEW_FIELD_NUMBER: _ClassVar[int]
    hasNew: bool
    def __init__(self, hasNew: bool = ...) -> None: ...

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

class MoveInformationReplyWithStatus(_message.Message):
    __slots__ = ["direction", "name", "passedToRobot", "radius", "speed", "stop", "turn"]
    DIRECTION_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PASSEDTOROBOT_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    TURN_FIELD_NUMBER: _ClassVar[int]
    direction: str
    name: str
    passedToRobot: bool
    radius: float
    speed: int
    stop: bool
    turn: str
    def __init__(self, name: _Optional[str] = ..., stop: bool = ..., speed: _Optional[int] = ..., direction: _Optional[str] = ..., turn: _Optional[str] = ..., radius: _Optional[float] = ..., passedToRobot: bool = ...) -> None: ...

class MoveInformationRequest(_message.Message):
    __slots__ = ["name"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class MoveInformationSendBackward(_message.Message):
    __slots__ = ["name", "radius", "speed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    radius: float
    speed: int
    def __init__(self, name: _Optional[str] = ..., speed: _Optional[int] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationSendCenter(_message.Message):
    __slots__ = ["name", "radius", "speed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    radius: float
    speed: int
    def __init__(self, name: _Optional[str] = ..., speed: _Optional[int] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationSendForward(_message.Message):
    __slots__ = ["name", "radius", "speed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    radius: float
    speed: int
    def __init__(self, name: _Optional[str] = ..., speed: _Optional[int] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationSendLeft(_message.Message):
    __slots__ = ["name", "radius", "speed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    radius: float
    speed: int
    def __init__(self, name: _Optional[str] = ..., speed: _Optional[int] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationSendRight(_message.Message):
    __slots__ = ["name", "radius", "speed"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    RADIUS_FIELD_NUMBER: _ClassVar[int]
    SPEED_FIELD_NUMBER: _ClassVar[int]
    name: str
    radius: float
    speed: int
    def __init__(self, name: _Optional[str] = ..., speed: _Optional[int] = ..., radius: _Optional[float] = ...) -> None: ...

class MoveInformationSendStop(_message.Message):
    __slots__ = ["name", "stop"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    name: str
    stop: bool
    def __init__(self, name: _Optional[str] = ..., stop: bool = ...) -> None: ...
