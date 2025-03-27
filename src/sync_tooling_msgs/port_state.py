import bidict

from sync_tooling_msgs.diag_tree import to_diag_tree
from sync_tooling_msgs.error_pb2 import Error
from sync_tooling_msgs.ok_pb2 import Ok
from sync_tooling_msgs.port_state_pb2 import PortState as PS

PORT_STATE_NAMES = bidict.bidict(
    {
        PS.PS_UNKNOWN: "NONE",
        PS.PS_INITIALIZING: "INITIALIZING",
        PS.PS_FAULTY: "FAULTY",
        PS.PS_DISABLED: "DISABLED",
        PS.PS_LISTENING: "LISTENING",
        PS.PS_PRE_MASTER: "PRE_MASTER",
        PS.PS_MASTER: "MASTER",
        PS.PS_PASSIVE: "PASSIVE",
        PS.PS_UNCALIBRATED: "UNCALIBRATED",
        PS.PS_SLAVE: "SLAVE",
        PS.PS_GRAND_MASTER: "GRAND_MASTER",
    }
)


def port_state_name(state: PS.ValueType) -> str:
    return PORT_STATE_NAMES[state]


def port_state_value(name: str) -> PS.ValueType:
    return PORT_STATE_NAMES.inverse[name]


def diagnose_port_state(state: PS.ValueType):
    match state:
        case PS.PS_UNKNOWN:
            return to_diag_tree(Error(msg="Invalid port state"))
        case PS.PS_MASTER | PS.PS_SLAVE | PS.PS_GRAND_MASTER:
            return to_diag_tree(
                Ok(msg=f"Port is operating nominally ({port_state_name(state)})")
            )
        case (
            PS.PS_LISTENING | PS.PS_INITIALIZING | PS.PS_PRE_MASTER | PS.PS_UNCALIBRATED
        ):
            return to_diag_tree(
                Error(msg=f"Port is in a transient state ({port_state_name(state)})")
            )
        case PS.PS_DISABLED | PS.PS_PASSIVE:
            return to_diag_tree(
                Ok(msg=f"Port exists but is not being used ({port_state_name(state)})")
            )
        case _:
            return to_diag_tree(
                Error(msg=f"Port is not working correctly ({port_state_name(state)})")
            )
