from sync_tooling_msgs.clock_id_pb2 import ClockId


ClockKey = str
def readable_clock_id(clock_id: ClockId) -> ClockKey:
    match clock_id.WhichOneof("id"):
        case "frame_id":
            return clock_id.frame_id.frame
        case "interface_id":
            id = clock_id.interface_id
            return f"{id.hostname}.{id.interface_name}"
        case "linux_clock_device_id":
            id = clock_id.linux_clock_device_id
            return f"{id.hostname}.ptp{id.clock_device_number}"
        case "ptp_clock_id":
            return clock_id.ptp_clock_id.id
        case "system_clock_id":
            id = clock_id.system_clock_id
            return f"{id.hostname}.sys"
    raise ValueError()
