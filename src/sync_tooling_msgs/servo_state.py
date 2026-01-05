"""Utility functions for servo states"""

import bidict

from sync_tooling_msgs.diag_tree import to_diag_tree
from sync_tooling_msgs.diag_tree_pb2 import DiagTree
from sync_tooling_msgs.error_pb2 import Error
from sync_tooling_msgs.ok_pb2 import Ok
from sync_tooling_msgs.servo_state_pb2 import ServoState

SERVO_STATE_NAMES = bidict.bidict(
    {
        ServoState.SERVO_UNLOCKED: "SERVO_UNLOCKED",
        ServoState.SERVO_JUMP: "SERVO_JUMP",
        ServoState.SERVO_LOCKED: "SERVO_LOCKED",
        ServoState.SERVO_LOCKED_STABLE: "SERVO_LOCKED_STABLE",
    }
)


def servo_state_name(state: ServoState.ValueType) -> str:
    """Return the canonical name for the given servo state enum value"""
    return SERVO_STATE_NAMES[state]


def servo_state_value(name: str) -> ServoState.ValueType:
    """Return the enum value for the given canonical servo state name"""
    return SERVO_STATE_NAMES.inverse[name]


def diagnose_servo_state(state: ServoState.ValueType) -> DiagTree:
    """Diagnose a given servo state enum value.

    For valid operational states, the diagnostic tree is of type `Ok`. For transient states
    and invalid states, the diagnostic tree is of type `Error`.

    Specifically, the state is only `Ok` if the servo state is `SERVO_LOCKED` or
    `SERVO_LOCKED_STABLE`.

    Args:
        state: The servo state enum value to diagnose

    Returns:
        The diagnostic tree for the given servo state. This is always a tree of type `Ok` or
        `Error`.

    """
    match state:
        case ServoState.SERVO_LOCKED | ServoState.SERVO_LOCKED_STABLE:
            return to_diag_tree(Ok(msg=f"Servo locked ({servo_state_name(state)})"))
        case _:
            return to_diag_tree(Error(msg=f"Servo not locked ({servo_state_name(state)})"))
