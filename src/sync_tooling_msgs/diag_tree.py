"""Utility functions for diagnostic trees."""

from sync_tooling_msgs.diag_status_pb2 import DiagStatus
from sync_tooling_msgs.diag_tree_pb2 import DiagTree
from sync_tooling_msgs.error_pb2 import Error
from sync_tooling_msgs.ok_pb2 import Ok
from sync_tooling_msgs.unknown_pb2 import Unknown
from sync_tooling_msgs.warning_pb2 import Warning


def precedence(status: DiagStatus) -> int:
    """Return the precedence (= severity) of a diagnostic status.

    Args:
        status: The diagnostic status to get the precedence of

    Raises:
        ValueError: If the status is invalid (e.g. uninitialized)

    Returns:
        0 for `Ok`, 1 for `Unknown`, 2 for `Warning`, 3 for `Error`

    """
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
    proto: DiagTree | DiagStatus | Ok | Warning | Error | Unknown | list | dict | str,
) -> DiagTree:
    """Convert a diagnostic status, list or dictionary to a diagnostic tree.

    If performed on a list or dictionary, the conversion is performed recursively and the items
    have to be convertible themselves.

    Args:
        proto: The diagnostic status, list or dictionary to convert

    Raises:
        ValueError: If the input is not convertible

    Returns:
        The converted diagnostic tree

    """
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
        case str():
            return DiagTree(comment=proto)
    raise ValueError(f"Could not convert {type(proto)} to DiagTree")


def prettify(diag_tree: DiagTree, indent: int = 0) -> str:
    """Stringify a diagnostic tree in a human-readable format.

    Examples:
        * `Ok()` -> `Ok`
        * `Error(msg="my message")` -> `Error(my message)`
        * `[]` -> `[]`
        * `[Ok(), Error(msg="my message")]` ->

            ```
            [
                Ok,
                Error(my message)
            ]
            ```
        * `{"a": Ok(), "b": Error(msg="my message")}` ->

            ```
            {
                a: Ok,
                b: Error(my message)
            }
            ```

    Args:
        diag_tree: The diagnostic tree to stringify
        indent: The number of spaces to indent per level. Defaults to 0.

    Raises:
        ValueError: If the tree is invalid (e.g. uninitialized)

    Returns:
        The stringified diagnostic tree

    """
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
        case "comment":
            return lpad + diag_tree.comment
    raise ValueError("Invalid diagnostic tree")


def aggregate(diag_tree: DiagTree, default: DiagStatus | None = None) -> DiagStatus:
    """
    Aggregate a diagnostic tree into a single status, keeping the highest severity status.

    The final diagnostic message is the one of the highest severity status. If there are
    multiple statuses with the same severity, the message of one of them is used.

    Args:
        diag_tree: The diagnostic tree to aggregate
        default: The default status to return if the tree is empty, or if none of the statuses
            in the tree have a higher severity than the default.

    Raises:
        ValueError: If the tree is invalid (e.g. uninitialized)

    Returns:
        The aggregated diagnostic status

    """
    if default is None:
        default = DiagStatus(ok=Ok())

    match diag_tree.WhichOneof("tree"):
        case "status":
            return diag_tree.status
        case "list":
            subtrees = diag_tree.list.list
            if not subtrees:
                return default

            max_status = max(map(aggregate, subtrees), key=precedence)
            if precedence(default) >= precedence(max_status):
                return default
            return max_status
        case "map":
            subtrees = diag_tree.map.map
            if not subtrees:
                return default

            max_status = max(map(aggregate, subtrees.values()), key=precedence)
            if precedence(default) >= precedence(max_status):
                return default
            return max_status
        case "comment":
            return default
    raise ValueError("Invalid diagnostic tree")


def _concat_labels(a: str, b: str | None):
    if b is None:
        return a

    if b.startswith("["):
        return f"{a}{b}"

    return f"{a} › {b}"  # noqa: RUF001


def _internal_flatten(diag_tree: DiagTree) -> dict[str | None, DiagStatus | str]:
    match diag_tree.WhichOneof("tree"):
        case "status":
            return {None: diag_tree.status}
        case "list":
            subtrees = diag_tree.list.list
            subtrees = {
                f"[{i}]": _internal_flatten(subtree)
                for i, subtree in enumerate(subtrees)
            }
            return {
                _concat_labels(label, sub_label): item
                for label, subtree in subtrees.items()
                for sub_label, item in subtree.items()
            }
        case "map":
            subtrees = diag_tree.map.map
            subtrees = {
                label: _internal_flatten(subtree) for label, subtree in subtrees.items()
            }
            return {
                _concat_labels(label, sub_label): item
                for label, subtree in subtrees.items()
                for sub_label, item in subtree.items()
            }
        case "comment":
            return {None: diag_tree.comment}
    raise AssertionError()


def flatten(diag_tree: DiagTree) -> dict[str, DiagStatus | str]:
    """Flatten a diagnostic tree into a dictionary of path -> status.

    The components of the path are separated by dots.

    Examples:
        * `Ok()` -> `{"status": Ok()}`
        * `[Ok(), Error(msg="my message")]` ->

            ```
            {
                "0.status": Ok(),
                "1.status": Error(my message)
            }
            ```

    Args:
        diag_tree: The diagnostic tree to flatten

    Returns:
        The flattened diagnostic tree

    """
    flattened = _internal_flatten(diag_tree)
    if None in flattened:
        match flattened[None]:
            case DiagStatus():
                flattened["status"] = flattened[None]
            case str():
                flattened["comment"] = flattened[None]
        del flattened[None]

    return flattened  # type: ignore
