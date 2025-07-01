"""Examples for ClockDiffMeasurement message type."""

from sync_tooling_msgs.clock_diff_measurement_pb2 import ClockDiffMeasurement
from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.sensor_id_pb2 import SensorId


def test_clock_diff_measurement():
    # --8<-- [start:clock_diff_measurement]
    src = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))
    dst = ClockId(sensor_id=SensorId(frame_id="lidar/top"))

    diff_measurement = ClockDiffMeasurement(src=src, dst=dst, diff_ns=20000)

    graph_update = GraphUpdate(clock_diff_measurement=diff_measurement)
    # --8<-- [end:clock_diff_measurement]
    return graph_update
