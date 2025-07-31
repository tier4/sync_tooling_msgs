import pytest

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.interface_id_pb2 import InterfaceId
from sync_tooling_msgs.linux_clock_device_id_pb2 import LinuxClockDeviceId
from sync_tooling_msgs.port_id_pb2 import PortId
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.sensor_id_pb2 import SensorId
from sync_tooling_msgs.system_clock_id_pb2 import SystemClockId


@pytest.fixture
def sensor_clock_id():
    return ClockId(sensor_id=SensorId(frame_id="test"))


@pytest.fixture
def sensor_clock_id_namespaced():
    return ClockId(sensor_id=SensorId(frame_id="/my/sensor/frame"))


@pytest.fixture
def system_clock_id():
    return ClockId(system_clock_id=SystemClockId(hostname="test"))


@pytest.fixture
def linux_clock_id():
    return ClockId(
        linux_clock_device_id=LinuxClockDeviceId(hostname="test", clock_device_number=0)
    )


@pytest.fixture
def ptp_clock_id():
    return ClockId(ptp_clock_id=PtpClockId(id="12af56.fffe.65EC21", domain=0))


@pytest.fixture
def interface_clock_id():
    return ClockId(interface_id=InterfaceId(hostname="test", interface_name="enp7s0f0"))


@pytest.fixture
def clock_id_test1(sensor_clock_id):
    return sensor_clock_id


@pytest.fixture
def clock_id_test2():
    return ClockId(sensor_id=SensorId(frame_id="test"))


@pytest.fixture
def clock_id_other():
    return ClockId(sensor_id=SensorId(frame_id="other"))


@pytest.fixture
def clock_id_empty():
    return ClockId()


@pytest.fixture
def port_id_domain0(clock_id_test1):
    return PortId(clock_id=clock_id_test1, port_number=1, ptp_domain=0)


@pytest.fixture
def port_id_domain1(clock_id_test1):
    return PortId(clock_id=clock_id_test1, port_number=1, ptp_domain=1)
