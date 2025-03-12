from google.protobuf.message import Message

from .clock_id_pb2 import ClockId
from .port_id_pb2 import PortId


def _proto_hash(message: Message):
    """Hash a given proto message stably. The hash is only valid during runtime.

    See https://protobuf.dev/programming-guides/serialization-not-canonical/#deterministic-is-not-canonical
    for details on why hashes cannot reliably be persisted across executions.

    Args:
        message (Message): The message to hash

    Returns:
        int: The hash value
    """
    return hash(message.SerializePartialToString(deterministic=True))


ClockId.__hash__ = _proto_hash  # type: ignore
PortId.__hash__ = _proto_hash  # type: ignore
