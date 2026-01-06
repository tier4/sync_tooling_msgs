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
