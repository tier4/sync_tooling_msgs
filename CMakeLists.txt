cmake_minimum_required(VERSION 3.14)
project(sync_tooling_msgs)

find_package(Protobuf 3.12 REQUIRED)
find_package(ament_cmake)

set(PROTO_DIR proto)
set(PROTO_NAMESPACE ${PROJECT_NAME})
set(CPP_OUT_DIR ${CMAKE_CURRENT_BINARY_DIR}/cpp_out)

set(PROTO_FILES
  clock_alias_update.proto
  clock_diff_measurement.proto
  clock_id.proto
  clock_master_update.proto
  diag_status.proto
  diag_tree.proto
  error.proto
  frame_id.proto
  graph_update.proto
  interface_id.proto
  linux_clock_device_id.proto
  ok.proto
  phc2sys_status_message.proto
  phc2sys_update.proto
  port_id.proto
  port_state.proto
  port_state_update.proto
  ptp4l_port_status_message.proto
  ptp4l_status_message.proto
  ptp_clock_id.proto
  ptp_parent_update.proto
  system_clock_id.proto
  unknown.proto
  warning.proto
)

set(CPP_SRCS "")
set(CPP_HDRS "")

foreach(PROTO_FILE ${PROTO_FILES})
  get_filename_component(PROTO_NAME ${PROTO_FILE} NAME_WE)
  list(APPEND CPP_SRCS ${CPP_OUT_DIR}/${PROTO_NAMESPACE}/${PROTO_NAME}.pb.cc)
  list(APPEND CPP_HDRS ${CPP_OUT_DIR}/${PROTO_NAMESPACE}/${PROTO_NAME}.pb.h)
endforeach()

list(TRANSFORM PROTO_FILES PREPEND ${CMAKE_CURRENT_SOURCE_DIR}/proto/${PROTO_NAMESPACE}/)

make_directory(${CPP_OUT_DIR})

add_custom_command(
  OUTPUT ${CPP_SRCS} ${CPP_HDRS} ${PY_SRCS}
  COMMAND ${Protobuf_PROTOC_EXECUTABLE}
  ARGS --cpp_out=${CPP_OUT_DIR} --experimental_allow_proto3_optional -I${CMAKE_SOURCE_DIR}/proto ${PROTO_FILES}
  DEPENDS ${PROTO_FILES}
)

add_library(sync_tooling_msgs SHARED ${CPP_SRCS} ${CPP_HDRS})
target_include_directories(sync_tooling_msgs PUBLIC
    $<BUILD_INTERFACE:${CPP_OUT_DIR}>
    $<INSTALL_INTERFACE:include>
)
target_link_libraries(sync_tooling_msgs PUBLIC ${Protobuf_LIBRARIES})

install(TARGETS sync_tooling_msgs EXPORT export_sync_tooling_msgs)
install(DIRECTORY proto DESTINATION share/${PROJECT_NAME})
install(FILES ${CPP_HDRS} DESTINATION include/${PROJECT_NAME})

ament_export_include_directories(include)
ament_export_targets(export_sync_tooling_msgs)
ament_package()