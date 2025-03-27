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
