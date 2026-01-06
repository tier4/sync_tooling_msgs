# Copyright 2025 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
