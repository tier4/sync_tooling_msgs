import pytest

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.port_id_pb2 import PortId
from sync_tooling_msgs.sensor_id_pb2 import SensorId


@pytest.fixture
def clock_id_test1():
  return ClockId(sensor_id=SensorId(frame_id="test"))
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
