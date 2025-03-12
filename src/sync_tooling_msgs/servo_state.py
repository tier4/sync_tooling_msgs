import bidict

from sync_tooling_msgs.diag_tree import to_diag_tree
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
    return SERVO_STATE_NAMES[state]


def servo_state_value(name: str) -> ServoState.ValueType:
    return SERVO_STATE_NAMES.inverse[name]


def diagnose_servo_state(state: ServoState.ValueType):
    match state:
        case ServoState.SERVO_LOCKED | ServoState.SERVO_LOCKED_STABLE:
            return to_diag_tree(Ok(msg=f"Servo locked ({servo_state_name(state)})"))
        case _:
            return to_diag_tree(Error(msg=f"Servo not locked ({servo_state_name(state)})"))
