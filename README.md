# SYNC.TOOLING Messages

This repository contains interfaces for [SYNC.TOOLING](https://github.com/tier4/sync_tooling), a
real-time PTP synchronization monitoring and diagnostics framework for distributed systems.

The interface definitions are in Protobuf 3, and have Python and C++ bindings.
The Python bindings are packaged using uv, while the C++ bindings are packaged for ROS 2.

## Prerequisites

- Protobuf >= 3.12 (`sudo apt install libprotoc-dev libprotoc23`)

When building for Python (ROS 2 independent):
- Python >= 3.10
- uv (`pip install uv`)

When building for C++/ROS 2:
- CMake >= 3.14
- ROS 2 Humble, Jazzy, or Rolling

## Building

### For Python (without ROS2)

```shell
uv sync --all-packages && uv build
```

### For C++ (ROS2)

```shell
rosdep install -yqi --from-paths .
colcon build
```