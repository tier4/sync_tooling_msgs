cmake_minimum_required(VERSION 3.14)
project(sync_tooling_msgs)

find_package(Protobuf 3.12 REQUIRED)

set(PROTO_DIR proto)
set(PYTHON_OUT_DIR python_out)
set(CPP_OUT_DIR cpp_out)

set(PROTO_FILES
  proto/unknown.proto
  proto/ok.proto
  proto/warning.proto
  proto/error.proto
  proto/diag_status.proto
  proto/diag_tree.proto
)

set(CPP_SRCS "")
set(CPP_HDRS "")
set(PY_SRCS "")

foreach(PROTO_FILE ${PROTO_FILES})
  get_filename_component(PROTO_NAME ${PROTO_FILE} NAME_WE)
  list(APPEND CPP_SRCS ${CPP_OUT_DIR}/${PROTO_NAME}.pb.cc)
  list(APPEND CPP_HDRS ${CPP_OUT_DIR}/${PROTO_NAME}.pb.h)
  list(APPEND PY_SRCS ${PYTHON_OUT_DIR}/${PROTO_NAME}_pb2.py)
endforeach()

list(TRANSFORM PROTO_FILES PREPEND ${CMAKE_CURRENT_SOURCE_DIR}/)

make_directory(${CPP_OUT_DIR})
make_directory(${PYTHON_OUT_DIR})

add_custom_command(
  OUTPUT ${CPP_SRCS} ${CPP_HDRS} ${PY_SRCS}
  COMMAND ${Protobuf_PROTOC_EXECUTABLE}
  ARGS --python_out=${PYTHON_OUT_DIR} --cpp_out=${CPP_OUT_DIR} --experimental_allow_proto3_optional -I${CMAKE_SOURCE_DIR}/proto ${PROTO_FILES}
  DEPENDS ${PROTO_FILES}
)

add_library(sync_tooling_msgs_cpp ${CPP_SRCS} SHARED)
file(TOUCH ${CMAKE_CURRENT_BINARY_DIR}/${PYTHON_OUT_DIR}/__init__.py)