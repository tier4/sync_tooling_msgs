# Synchronization Tooling Messages

This project aims to serve as a bridge between the Python-based [Synchronization Tooling](https://github.com/tier4/sync_tooling) and ROS-based C++ packages such as [Nebula](https://github.com/tier4/nebula).

ROS2 message transport has been evaluated for this use case but has ultimately not fulfilled requirements:
* it does not support self-similar data structures such as JSON-like nested objects
* the different Ubuntu/Python versions used on different ECUs make it hard to use ROS2 in combination with Python 3.10

## Prerequisites

- Protobuf >= 3.12 (`sudo apt install libprotoc-dev libprotoc23`)

When building for Python (ROS2-less):
- Python >= 3.10
- uv (`pip install uv`)

When building for C++/ROS2:
- CMake >= 3.14
- ROS2 Humble

## Building

### For Python (without ROS2)


```shell
uv sync && uv build
```

### For C++ (ROS2)

```shell
colcon build
```