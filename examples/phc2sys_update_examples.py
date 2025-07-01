"""Examples for Phc2SysUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.phc2sys_update_pb2 import Phc2SysUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.servo_state_pb2 import ServoState
from sync_tooling_msgs.slave_clock_state_pb2 import SlaveClockState
from sync_tooling_msgs.system_clock_id_pb2 import SystemClockId


def test_phc2sys_synchronization():
    # --8<-- [start:phc2sys_sync]
    src_hw_clock = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))
    dst_sys_clock = ClockId(system_clock_id=SystemClockId(hostname="my_host"))

    clock_state = SlaveClockState(offset_ns=1, servo_state=ServoState.SERVO_LOCKED)

    phc2sys_update = Phc2SysUpdate(
        src=src_hw_clock, dst=dst_sys_clock, clock_state=clock_state
    )

    graph_update = GraphUpdate(phc2sys_update=phc2sys_update)
    # --8<-- [end:phc2sys_sync]
    assert graph_update.WhichOneof("update")
