"""Utility functions for port IDs."""

from sync_tooling_msgs.clock_id import readable_clock_id
from sync_tooling_msgs.port_id_pb2 import PortId


def readable_port_id(port_id: PortId, include_domain: bool = True) -> str:
    """Return a human-readable string for the given port ID.

    See [`readable_clock_id`][sync_tooling_msgs.clock_id.readable_clock_id] for the format of
    clock IDs.

    Examples:
        * `PortId(SystemClockId("host"), port_number=1, ptp_domain=0)` ->
            `"0:host.sys-1"`

    Args:
        port_id: The port ID to convert to a string
        include_domain: Whether to include the PTP domain in the string. Defaults to True.

    Returns:
        The human-readable port ID

    """
    readable_id = f"{readable_clock_id(port_id.clock_id)}-{port_id.port_number}"
    if include_domain:
        readable_id = f"{port_id.ptp_domain}:{readable_id}"
    return readable_id
