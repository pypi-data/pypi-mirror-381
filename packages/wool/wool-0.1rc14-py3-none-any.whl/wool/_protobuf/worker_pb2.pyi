import task_pb2 as _task_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("ack", "nack", "result", "exception")
    ACK_FIELD_NUMBER: _ClassVar[int]
    NACK_FIELD_NUMBER: _ClassVar[int]
    RESULT_FIELD_NUMBER: _ClassVar[int]
    EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    ack: Ack
    nack: Nack
    result: _task_pb2.Result
    exception: _task_pb2.Exception
    def __init__(self, ack: _Optional[_Union[Ack, _Mapping]] = ..., nack: _Optional[_Union[Nack, _Mapping]] = ..., result: _Optional[_Union[_task_pb2.Result, _Mapping]] = ..., exception: _Optional[_Union[_task_pb2.Exception, _Mapping]] = ...) -> None: ...

class Ack(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class Nack(_message.Message):
    __slots__ = ("reason",)
    REASON_FIELD_NUMBER: _ClassVar[int]
    reason: str
    def __init__(self, reason: _Optional[str] = ...) -> None: ...

class StopRequest(_message.Message):
    __slots__ = ("wait",)
    WAIT_FIELD_NUMBER: _ClassVar[int]
    wait: int
    def __init__(self, wait: _Optional[int] = ...) -> None: ...

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
