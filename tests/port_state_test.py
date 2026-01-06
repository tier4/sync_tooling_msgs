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

from sync_tooling_msgs.diag_tree import aggregate
from sync_tooling_msgs.port_state import diagnose_port_state
from sync_tooling_msgs.port_state_pb2 import PortState


def test_port_state_diagnostics():
    assertions = {
        # Fault/invalid states
        PortState.PS_UNKNOWN: "error",
        PortState.PS_FAULTY: "error",
        # Transient states
        PortState.PS_INITIALIZING: "error",
        PortState.PS_LISTENING: "error",
        PortState.PS_UNCALIBRATED: "error",
        PortState.PS_PRE_MASTER: "error",
        # Permitted inactive states
        PortState.PS_DISABLED: "ok",
        PortState.PS_PASSIVE: "ok",
        # Nominal operational states
        PortState.PS_SLAVE: "ok",
        PortState.PS_MASTER: "ok",
        PortState.PS_GRAND_MASTER: "ok",
    }

    assert all(v in assertions for v in PortState.values())

    for ps, expected_status in assertions.items():
        diag_tree = diagnose_port_state(ps)
        actual_status = aggregate(diag_tree).WhichOneof("status")
        assert actual_status == expected_status
