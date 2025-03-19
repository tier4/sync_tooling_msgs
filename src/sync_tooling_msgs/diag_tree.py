from sync_tooling_msgs.diag_status_pb2 import DiagStatus
from sync_tooling_msgs.diag_tree_pb2 import DiagTree
from sync_tooling_msgs.error_pb2 import Error
from sync_tooling_msgs.ok_pb2 import Ok
from sync_tooling_msgs.unknown_pb2 import Unknown
from sync_tooling_msgs.warning_pb2 import Warning


def precedence(status: DiagStatus) -> int:
    match status.WhichOneof("status"):
        case "ok":
            return 0
        case "unknown":
            return 1
        case "warning":
            return 2
        case "error":
            return 3
    raise ValueError()


def to_diag_tree(
    proto: DiagStatus | Ok | Warning | Error | Unknown | list | dict,
) -> DiagTree:
    match proto:
        case DiagTree():
            return proto
        case DiagStatus():
            return DiagTree(status=proto)
        case [*ls]:
            return DiagTree(
                list=DiagTree.DiagList(list=[to_diag_tree(elem) for elem in ls])
            )
        case {**kv}:
            return DiagTree(
                map=DiagTree.DiagMap(map={k: to_diag_tree(v) for k, v in kv.items()})
            )
        case Ok():
            return to_diag_tree(DiagStatus(ok=proto))
        case Warning():
            return to_diag_tree(DiagStatus(warning=proto))
        case Error():
            return to_diag_tree(DiagStatus(error=proto))
        case Unknown():
            return to_diag_tree(DiagStatus(unknown=proto))
    raise ValueError(f"Could not convert {type(proto)} to DiagTree")


def prettify(diag_tree: DiagTree, indent=0) -> str:
    lpad = "  " * indent

    match diag_tree.WhichOneof("tree"):
        case "status":
            status = diag_tree.status
            field = status.WhichOneof("status")
            if field is None:
                raise ValueError("No status set")

            status_value: Ok | Warning | Error | Unknown = getattr(status, field)
            text = status_value.__class__.__name__
            if status_value.msg is not None:
                text += f"({status_value.msg})"
            return lpad + text
        case "list":
            subtrees = diag_tree.list.list
            if not subtrees:
                return lpad + "[]"

            lf = "\n"
            return f"{lpad}[\n{lf.join([prettify(t, indent + 1) for t in subtrees])}\n{lpad}]"
        case "map":
            subtrees = diag_tree.map.map
            if not subtrees:
                return lpad + "{}"

            lf = "\n"
            return f"{lpad}{{\n{lf.join([f'{k}: {prettify(t, indent + 1)}' for k, t in subtrees.items()])}\n{lpad}}}"
    raise AssertionError()


def aggregate(diag_tree: DiagTree) -> DiagStatus:
    match diag_tree.WhichOneof("tree"):
        case "status":
            return diag_tree.status
        case "list":
            subtrees = diag_tree.list.list
            if not subtrees:
                return DiagStatus(ok=Ok())

            max_status = max(map(aggregate, subtrees), key=precedence)
            return max_status
        case "map":
            subtrees = diag_tree.map.map
            if not subtrees:
                return DiagStatus(ok=Ok())

            max_status = max(map(aggregate, subtrees.values()), key=precedence)
            return max_status
    raise AssertionError()


def flatten(diag_tree: DiagTree) -> dict[str, DiagStatus]:
    def concat_labels(a: str, b: str | None):
        return a if b is None else f"{a}.{b}"

    def internal_flatten(diag_tree: DiagTree) -> dict[str | None, DiagStatus]:
        match diag_tree.WhichOneof("tree"):
            case "status":
                return {None: diag_tree.status}
            case "list":
                subtrees = diag_tree.list.list
                subtrees = {
                    str(i): flatten(subtree) for i, subtree in enumerate(subtrees)
                }
                return {
                    concat_labels(label, sub_label): item
                    for label, subtree in subtrees.items()
                    for sub_label, item in subtree.items()
                }
            case "map":
                subtrees = diag_tree.map.map
                subtrees = {
                    label: flatten(subtree) for label, subtree in subtrees.items()
                }
                return {
                    concat_labels(label, sub_label): item
                    for label, subtree in subtrees.items()
                    for sub_label, item in subtree.items()
                }
        raise AssertionError()

    flattened = internal_flatten(diag_tree)
    if None in flattened:
        flattened["status"] = flattened[None]
        del flattened[None]

    return flattened  # type: ignore
