"""Examples for PortStateUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.port_id_pb2 import PortId
from sync_tooling_msgs.port_state_pb2 import PortState
from sync_tooling_msgs.port_state_update_pb2 import PortStateUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId


def test_port_state_update():
    # --8<-- [start:port_state_update]
    clock = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))

    port = PortId(clock_id=clock, port_number=1, ptp_domain=0)

    port_state_update = PortStateUpdate(port_id=port, port_state=PortState.PS_SLAVE)

    graph_update = GraphUpdate(port_state_update=port_state_update)
    # --8<-- [end:port_state_update]
    return graph_update
