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
    assert graph_update.WhichOneof("update")
