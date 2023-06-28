from google.protobuf import wrappers_pb2 as _wrappers_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LcuAnnounce(_message.Message):
    __slots__ = ["description", "id"]
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    description: _wrappers_pb2.StringValue
    id: _wrappers_pb2.StringValue
    def __init__(self, id: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ..., description: _Optional[_Union[_wrappers_pb2.StringValue, _Mapping]] = ...) -> None: ...

class LcuClientMessage(_message.Message):
    __slots__ = ["lcu_announce"]
    LCU_ANNOUNCE_FIELD_NUMBER: _ClassVar[int]
    lcu_announce: LcuAnnounce
    def __init__(self, lcu_announce: _Optional[_Union[LcuAnnounce, _Mapping]] = ...) -> None: ...

class LcuResponseMessage(_message.Message):
    __slots__ = ["success"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: Success
    def __init__(self, success: _Optional[_Union[Success, _Mapping]] = ...) -> None: ...

class Success(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...
