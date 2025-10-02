from messages.order import common_pb2 as _common_pb2
from messages.common import pagination_pb2 as _pagination_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetOrdersByShopResponse(_message.Message):
    __slots__ = ("result", "length")
    RESULT_FIELD_NUMBER: _ClassVar[int]
    LENGTH_FIELD_NUMBER: _ClassVar[int]
    result: _containers.RepeatedCompositeFieldContainer[_common_pb2.Order]
    length: str
    def __init__(self, result: _Optional[_Iterable[_Union[_common_pb2.Order, _Mapping]]] = ..., length: _Optional[str] = ...) -> None: ...
