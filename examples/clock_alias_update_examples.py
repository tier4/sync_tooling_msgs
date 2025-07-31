"""Examples for ClockAliasUpdate message type."""

from sync_tooling_msgs.clock_alias_update_pb2 import ClockAliasUpdate
from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.system_clock_id_pb2 import SystemClockId


def test_basic_clock_alias_update():
    # --8<-- [start:basic_alias]
    ptp_clock_id = ClockId(ptp_clock_id=PtpClockId(id="123456.fffe.654321", domain=0))
    system_clock_id = ClockId(system_clock_id=SystemClockId(hostname="my_host"))

    alias_update = ClockAliasUpdate(aliases=[ptp_clock_id, system_clock_id])
    graph_update = GraphUpdate(clock_alias_update=alias_update)
    # --8<-- [end:basic_alias]
    assert graph_update.WhichOneof("update")
