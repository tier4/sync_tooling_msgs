from sync_tooling_msgs.clock_id import readable_clock_id
from sync_tooling_msgs.port_id_pb2 import PortId


def readable_port_id(port_id: PortId, include_domain = True) -> str:
    readable_id = f"{readable_clock_id(port_id.clock_id)}-{port_id.port_number}"
    if (include_domain):
        readable_id = f"{port_id.ptp_domain}:{readable_id}"
    return readable_id
