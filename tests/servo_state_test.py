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
from sync_tooling_msgs.servo_state import diagnose_servo_state
from sync_tooling_msgs.servo_state_pb2 import ServoState


def test_sero_state_diagnostics():
    assertions = {
        ServoState.SERVO_UNLOCKED: "error",
        ServoState.SERVO_JUMP: "error",
        ServoState.SERVO_LOCKED: "ok",
        ServoState.SERVO_LOCKED_STABLE: "ok",
    }

    assert all(v in assertions for v in ServoState.values())

    for ss, expected_status in assertions.items():
        diag_tree = diagnose_servo_state(ss)
        actual_status = aggregate(diag_tree).WhichOneof("status")
        assert actual_status == expected_status
