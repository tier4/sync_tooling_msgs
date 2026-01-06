# SYNC.TOOLING Messages

This project aims to serve as a bridge between the Python-based [SYNC.TOOLING](https://github.com/tier4/sync_tooling) and ROS2-based C++ packages such as [Nebula](https://github.com/tier4/nebula).

The message definitions are Protobuf, but can be used over ROS2 pub/sub as a transport layer.

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
rosdep install -yqi --from-paths .
colcon build
```