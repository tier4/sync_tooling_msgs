import bidict
from sync_tooling_msgs.port_state_pb2 import PortState as ps

PORT_STATE_NAMES = bidict.bidict({
  ps.PS_UNKNOWN: "NONE",
	ps.PS_INITIALIZING: "INITIALIZING",
	ps.PS_FAULTY: "FAULTY",
	ps.PS_DISABLED: "DISABLED",
	ps.PS_LISTENING: "LISTENING",
	ps.PS_PRE_MASTER: "PRE_MASTER",
	ps.PS_MASTER: "MASTER",
	ps.PS_PASSIVE: "PASSIVE",
	ps.PS_UNCALIBRATED: "UNCALIBRATED",
	ps.PS_SLAVE: "SLAVE",
	ps.PS_GRAND_MASTER: "GRAND_MASTER",
})

def port_state_name(state: ps.ValueType) -> str:
  return PORT_STATE_NAMES[state]

def port_state_value(name: str) -> ps.ValueType:
  return PORT_STATE_NAMES.inverse[name]