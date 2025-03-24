from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.port_id_pb2 import PortId
from sync_tooling_msgs.sensor_id_pb2 import SensorId

clock_id_test1 = ClockId(sensor_id=SensorId(name="test", ip="192.168.1.201"))
clock_id_test2 = ClockId(sensor_id=SensorId(name="test", ip="192.168.1.201"))
clock_id_other = ClockId(sensor_id=SensorId(name="other", ip="192.168.1.202"))
clock_id_empty = ClockId()

port_id_domain0 = PortId(clock_id=clock_id_test1, port_number=1, ptp_domain=0)
port_id_domain1 = PortId(clock_id=clock_id_test1, port_number=1, ptp_domain=1)


def test_clock_id_hash_basics():
    assert clock_id_test1 == clock_id_test2
    assert clock_id_test1 != clock_id_other
    assert clock_id_test1 != clock_id_empty
    assert hash(clock_id_test1) == hash(clock_id_test2)

    # Not true for all possible clock IDs (hashes can clash), but likely (and deterministic).
    assert hash(clock_id_test1) != hash(clock_id_other)


def test_port_id_hash_basics():
    assert port_id_domain0 != port_id_domain1
    assert hash(port_id_domain0) != hash(port_id_domain1)


def test_clock_id_collections():
    mapping = {clock_id_test1: "a", clock_id_other: "b", clock_id_empty: "c"}

    assert len(mapping) == 3
    assert mapping[clock_id_test1] == "a"
    assert mapping[clock_id_test2] == "a"


def test_port_id_collection():
    mapping = {port_id_domain0: "a", port_id_domain1: "b"}

    assert len(mapping) == 2
    assert mapping[port_id_domain0] == "a"
