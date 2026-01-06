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

"""Examples for ClockAliasUpdate message type."""

from sync_tooling_msgs.clock_alias_update_pb2 import ClockAliasUpdate
from sync_tooling_msgs.clock_id_pb2 import ClockId
from sync_tooling_msgs.graph_update_pb2 import GraphUpdate
from sync_tooling_msgs.ptp_clock_id_pb2 import PtpClockId
from sync_tooling_msgs.system_clock_id_pb2 import SystemClockId


def test_basic_clock_alias_update():
    # --8<-- [start:basic_alias]
    ptp_clock_id = ClockId(ptp_clock_id=PtpClockId(id="123456.fffe.654321"))
    system_clock_id = ClockId(system_clock_id=SystemClockId(hostname="my_host"))

    alias_update = ClockAliasUpdate(aliases=[ptp_clock_id, system_clock_id])
    graph_update = GraphUpdate(clock_alias_update=alias_update)
    # --8<-- [end:basic_alias]
    assert graph_update.WhichOneof("update")
