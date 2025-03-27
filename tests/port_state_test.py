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
