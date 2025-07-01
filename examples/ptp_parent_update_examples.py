"""Examples for PtpParentUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.port_id_pb2 import PortId
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.ptp_parent_update_pb2 import PtpParentUpdate


def test_ptp_parent_child_relationship():
    # --8<-- [start:ptp_parent_child]
    child = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))
    parent = ClockId(ptp_clock_id=PtpClockId(id="222222.fffe.222222"))

    parent_port = PortId(clock_id=parent, port_number=1, ptp_domain=0)

    parent_update = PtpParentUpdate(clock_id=child, parent=parent_port)

    graph_update = GraphUpdate(ptp_parent_update=parent_update)
    # --8<-- [end:ptp_parent_child]
    return graph_update
