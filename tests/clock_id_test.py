
import pytest

from sync_tooling_msgs.clock_id import parse_clock_id, readable_clock_id
from sync_tooling_msgs.clock_id_pb2 import ClockId


@pytest.mark.parametrize("clock_name", [
    "sensor_clock_id",
    "sensor_clock_id_namespaced",
    "system_clock_id",
    "linux_clock_id",
    "ptp_clock_id",
    "interface_clock_id",
])
def test_print_and_parse(clock_name, request):
    clock_id: ClockId = request.getfixturevalue(clock_name)
    assert clock_id == parse_clock_id(readable_clock_id(clock_id))
