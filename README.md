# Getting Started

## Prerequisites

- Protobuf >= 3.12 (`sudo apt install libprotoc-dev libprotoc23`)
- Python >= 3.10
- CMake >= 3.14
- uv (`pip install uv`)

## Building

```shell
mkdir -p build && \
cd build && \
cmake .. && \
make && \
cd .. && \
uv build
```