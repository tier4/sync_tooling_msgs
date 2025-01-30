cmake_minimum_required(VERSION 3.14)
project(sync_tooling_msgs)

find_package(Protobuf 3.12 REQUIRED)
find_package(ament_cmake)

set(PROTO_DIR proto)
set(CPP_OUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/cpp_out)

set(PROTO_FILES
  proto/unknown.proto
  proto/ok.proto
  proto/warning.proto
  proto/error.proto
  proto/diag_status.proto
  proto/diag_tree.proto
  proto/graph_update.proto
)

set(CPP_SRCS "")
set(CPP_HDRS "")

foreach(PROTO_FILE ${PROTO_FILES})
  get_filename_component(PROTO_NAME ${PROTO_FILE} NAME_WE)
  list(APPEND CPP_SRCS ${CPP_OUT_DIR}/${PROTO_NAME}.pb.cc)
  list(APPEND CPP_HDRS ${CPP_OUT_DIR}/${PROTO_NAME}.pb.h)
endforeach()

list(TRANSFORM PROTO_FILES PREPEND ${CMAKE_CURRENT_SOURCE_DIR}/)

make_directory(${CPP_OUT_DIR})

add_custom_command(
  OUTPUT ${CPP_SRCS} ${CPP_HDRS} ${PY_SRCS}
  COMMAND ${Protobuf_PROTOC_EXECUTABLE}
  ARGS --cpp_out=${CPP_OUT_DIR} --experimental_allow_proto3_optional -I${CMAKE_SOURCE_DIR}/proto ${PROTO_FILES}
  DEPENDS ${PROTO_FILES}
)

add_library(sync_tooling_msgs SHARED ${CPP_SRCS})
target_link_libraries(sync_tooling_msgs PUBLIC ${Protobuf_LIBRARIES})
target_include_directories(sync_tooling_msgs PUBLIC ${CPP_OUT_DIR})

install(TARGETS sync_tooling_msgs EXPORT export_sync_tooling_msgs)
install(DIRECTORY proto DESTINATION share/${PROJECT_NAME})
install(FILES ${CPP_HDRS} DESTINATION include/${PROJECT_NAME})

ament_package()