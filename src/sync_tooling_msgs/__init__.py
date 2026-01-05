"""Sync tooling message types and utilities.

This module provides protobuf message types and helper functions for clock
synchronization diagnostics.
"""

from google.protobuf.message import Message

from sync_tooling_msgs.clock_id import readable_clock_id

from .clock_id_pb2 import ClockId
from .graph_update_pb2 import GraphUpdate
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


GraphUpdate.__hash__ = _proto_hash  # type: ignore
ClockId.__hash__ = _proto_hash  # type: ignore
ClockId.__str__ = readable_clock_id # type: ignore
PortId.__hash__ = _proto_hash  # type: ignore
