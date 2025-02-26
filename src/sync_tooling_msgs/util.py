from typing import Any, Callable, Generic, TypeVar
from google.protobuf.message import Message


def hash_proto(message: Message):
    """Hash a given proto message stably. The hash is only valid during runtime.

    See https://protobuf.dev/programming-guides/serialization-not-canonical/#deterministic-is-not-canonical
    for details on why hashes cannot reliably be persisted across executions.

    Args:
        message (Message): The message to hash

    Returns:
        int: The hash value
    """
    return hash(message.SerializePartialToString(deterministic=True))
