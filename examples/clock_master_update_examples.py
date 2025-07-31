"""Examples for ClockMasterUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.clock_master_update_pb2 import ClockMasterUpdate
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId


def test_master_slave_relationship():
    # --8<-- [start:master_slave_relationship]
    slave = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111", domain=1))
    master = ClockId(ptp_clock_id=PtpClockId(id="222222.fffe.222222", domain=1))

    master_update = ClockMasterUpdate(clock_id=slave, master=master, master_offset_ns=3)

    graph_update = GraphUpdate(clock_master_update=master_update)
    # --8<-- [end:master_slave_relationship]
    assert graph_update.WhichOneof("update")


def test_no_master_update():
    # --8<-- [start:no_master]
    standalone_clock = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111", domain=2))

    master_update = ClockMasterUpdate(clock_id=standalone_clock)

    graph_update = GraphUpdate(clock_master_update=master_update)
    # --8<-- [end:no_master]
    assert graph_update.WhichOneof("update")
