# Copyright 2025 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Examples for ClockMasterUpdate message type."""

from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.clock_master_update_pb2 import ClockMasterUpdate
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId


def test_master_slave_relationship():
    # --8<-- [start:master_slave_relationship]
    slave = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))
    master = ClockId(ptp_clock_id=PtpClockId(id="222222.fffe.222222"))

    master_update = ClockMasterUpdate(clock_id=slave, master=master, master_offset_ns=3)

    graph_update = GraphUpdate(clock_master_update=master_update)
    # --8<-- [end:master_slave_relationship]
    assert graph_update.WhichOneof("update")


def test_no_master_update():
    # --8<-- [start:no_master]
    standalone_clock = ClockId(ptp_clock_id=PtpClockId(id="111111.fffe.111111"))

    master_update = ClockMasterUpdate(clock_id=standalone_clock)

    graph_update = GraphUpdate(clock_master_update=master_update)
    # --8<-- [end:no_master]
    assert graph_update.WhichOneof("update")
