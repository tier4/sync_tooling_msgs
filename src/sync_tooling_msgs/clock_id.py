from sync_tooling_msgs.clock_id_pb2 import ClockId


def readable_clock_id(clock_id: ClockId) -> str | None:
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
        case None:
            return None
        case other:
            raise NotImplementedError(f"Clock ID type '{other}' is not supported")


def readable_clock_type(clock_id: ClockId):
    TYPE_NAMES = {
        "frame_id": "Sensor",
        "interface_id": "Network interface",
        "linux_clock_device_id": "Linux clock device",
        "ptp_clock_id": "PTP clock",
        "system_clock_id": "System clock",
        None: "Unset",
    }

    return TYPE_NAMES[clock_id.WhichOneof("id")]
