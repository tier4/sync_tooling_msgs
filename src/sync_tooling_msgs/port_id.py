from sync_tooling_msgs.clock_id import readable_clock_id
from sync_tooling_msgs.port_id_pb2 import PortId


PortKey = str
def readable_port_id(port_id: PortId) -> str:
    return f"{port_id.ptp_domain}:{readable_clock_id(port_id.clock_id)}-{port_id.port_number}"
