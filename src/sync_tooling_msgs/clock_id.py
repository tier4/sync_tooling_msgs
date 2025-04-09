"""Utility functions for clock IDs"""

import re

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.interface_id_pb2 import InterfaceId
from sync_tooling_msgs.linux_clock_device_id_pb2 import LinuxClockDeviceId
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.sensor_id_pb2 import SensorId
from sync_tooling_msgs.system_clock_id_pb2 import SystemClockId


def readable_clock_id(clock_id: ClockId) -> str:
    """
    Convert a clock ID to a human-readable string.

    Outputs of this function are canonical and can be parsed back using
    [parse_clock_id][sync_tooling_msgs.clock_id.parse_clock_id].
    See that function for possible ambiguities.

    Examples:
        * `sensor_id`: `sensor_name@192.168.1.100`
        * `interface_id`: `hostname.eth0`
        * `linux_clock_device_id`: `hostname.ptp1`
        * `ptp_clock_id`: `123456.fffe.123456`
        * `system_clock_id`: `hostname.sys`

    Args:
        clock_id: The clock ID to convert.

    Raises:
        NotImplementedError: If the clock ID type is not supported (e.g. uninitialized IDs)

    Returns:
       The human-readable string
    """
    match clock_id.WhichOneof("id"):
        case "sensor_id":
            id = clock_id.sensor_id
            return f"{id.name}@{id.ip}"
        case "interface_id":
            id = clock_id.interface_id
            return f"{id.hostname}.{id.interface_name}"
        case "linux_clock_device_id":
            id = clock_id.linux_clock_device_id
            return f"{id.hostname}.ptp{id.clock_device_number}"
        case "ptp_clock_id":
            return clock_id.ptp_clock_id.id
        case "system_clock_id":
            id = clock_id.system_clock_id
            return f"{id.hostname}.sys"
        case other:
            raise NotImplementedError(f"Clock ID type '{other}' is not supported")


def parse_clock_id(string: str) -> ClockId:
    """
    Parses a string in the format produced by `readable_clock_id` into a clock ID.

    Possible ambiguities:
    * an interface name ending with @ followed by a valid IPv4 address will be interpreted as a sensor ID

    Args:
        string (str): The string to parse.

    Raises:
        ValueError: If the string could not be parsed into a valid clock ID

    Returns:
        ClockId: The parsed, valid clock ID
    """

    # see `man 7 hostname`
    re_hostname = r"(?P<hostname>[A-Za-z0-9][A-Za-z0-9\-]{,63})"
    re_sys = f"{re_hostname}.sys"
    re_clock_dev = f"{re_hostname}.ptp(?P<device_num>\\d+)"

    re_hex = r"[A-Fa-f0-9]"
    re_ptp = f"{re_hex}{{6}}.{re_hex}{{4}}.{re_hex}{{6}}"

    # interface name validation from: https://unix.stackexchange.com/a/532650
    re_iface = f"{re_hostname}.(?P<iface_name>[^/ ]+)"

    # from: https://stackoverflow.com/a/36760050
    re_ipv4 = r"((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?\b){4}"
    re_sensor = f"(?P<name>.+)@(?P<ip>{re_ipv4})"

    if m := re.fullmatch(re_sys, string):
        return ClockId(system_clock_id=SystemClockId(hostname=m["hostname"]))

    if m := re.fullmatch(re_clock_dev, string):
        return ClockId(
            linux_clock_device_id=LinuxClockDeviceId(
                hostname=m["hostname"], clock_device_number=int(m["device_num"])
            )
        )

    if m := re.fullmatch(re_ptp, string):
        return ClockId(ptp_clock_id=PtpClockId(id=string))

    if m := re.fullmatch(re_sensor, string):
        return ClockId(sensor_id=SensorId(name=m["name"], ip=m["ip"]))

    if m := re.fullmatch(re_iface, string):
        return ClockId(
            interface_id=InterfaceId(
                hostname=m["hostname"], interface_name=m["iface_name"]
            )
        )

    raise ValueError("Cannot parse clock id")


def readable_clock_type(clock_id: ClockId) -> str:
    """
    Return a human-readable clock type for the given clock ID.

    Args:
        clock_id: The clock ID to get the type of

    Returns:
        The human-readable clock type
    """
    type_names = {
        "sensor_id": "Sensor",
        "interface_id": "Network interface",
        "linux_clock_device_id": "Linux clock device",
        "ptp_clock_id": "PTP clock",
        "system_clock_id": "System clock",
        None: "Unset",
    }

    return type_names[clock_id.WhichOneof("id")]
