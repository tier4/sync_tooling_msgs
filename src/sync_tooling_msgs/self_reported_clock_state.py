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

"""Utility functions for self-reported clock states."""

import bidict

from sync_tooling_msgs.diag_tree import to_diag_tree
from sync_tooling_msgs.diag_tree_pb2 import DiagTree
from sync_tooling_msgs.error_pb2 import Error
from sync_tooling_msgs.ok_pb2 import Ok
from sync_tooling_msgs.self_reported_clock_state_update_pb2 import (
    SelfReportedClockStateUpdate,
)
from sync_tooling_msgs.warning_pb2 import Warning

CLOCK_STATE_NAMES = bidict.bidict(
    {
        SelfReportedClockStateUpdate.State.INVALID: "INVALID",
        SelfReportedClockStateUpdate.State.UNSYNCHRONIZED: "UNSYNCHRONIZED",
        SelfReportedClockStateUpdate.State.TRACKING: "TRACKING",
        SelfReportedClockStateUpdate.State.LOCKED: "LOCKED",
        SelfReportedClockStateUpdate.State.LOST: "LOST",
    }
)


def clock_state_name(
    state: SelfReportedClockStateUpdate.State.ValueType,
) -> str:
    """Return the canonical name for the given clock state enum value."""
    return CLOCK_STATE_NAMES[state]


def clock_state_value(
    name: str,
) -> SelfReportedClockStateUpdate.State.ValueType:
    """Return the enum value for the given canonical clock state name."""
    return CLOCK_STATE_NAMES.inverse[name]


def diagnose_clock_state(
    state: SelfReportedClockStateUpdate.State.ValueType,
) -> DiagTree:
    """Diagnose a given clock state enum value.

    For valid states, the diagnostic tree is of type `Ok`. For transient states
    and invalid states, the diagnostic tree is of type `Error`.

    Specifically, the state is only `Ok` if the clock state is `LOCKED` and `Warning` if the
    clock state is `TRACKING`. Otherwise, the state is `Error`.

    Args:
        state: The clock state enum value to diagnose

    Returns:
        The diagnostic tree for the given clock state. This is always a tree of type `Ok` or
        `Error`.

    """
    match state:
        case SelfReportedClockStateUpdate.State.INVALID:
            return to_diag_tree(Error(msg="Clock reports an invalid state"))
        case SelfReportedClockStateUpdate.State.UNSYNCHRONIZED:
            return to_diag_tree(Error(msg="Clock reports to be unsynchronized"))
        case SelfReportedClockStateUpdate.State.TRACKING:
            return to_diag_tree(Warning(msg="Clock reports to be tracking"))
        case SelfReportedClockStateUpdate.State.LOCKED:
            return to_diag_tree(Ok(msg="Clock reports to be locked"))
        case SelfReportedClockStateUpdate.State.LOST:
            return to_diag_tree(Error(msg="Clock reports to have lost synchronization"))
        case _:
            raise AssertionError(f"Unknown clock state: {state}")
