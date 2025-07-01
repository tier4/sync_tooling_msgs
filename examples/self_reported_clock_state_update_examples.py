"""Examples for SelfReportedClockStateUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.self_reported_clock_state_update_pb2 import (
    SelfReportedClockStateUpdate,
)
from sync_tooling_msgs.sensor_id_pb2 import SensorId


def test_self_reported_clock_state():
    # --8<-- [start:self_reported_clock_state]
    sensor = ClockId(sensor_id=SensorId(frame_id="lidar/top"))

    clock_state_update = SelfReportedClockStateUpdate(
        clock_id=sensor, state=SelfReportedClockStateUpdate.State.LOCKED
    )

    graph_update = GraphUpdate(self_reported_clock_state_update=clock_state_update)
    # --8<-- [end:self_reported_clock_state]
    assert graph_update.WhichOneof("update")
