cmake_minimum_required(VERSION 3.15...4.0)

project(
  ${SKBUILD_PROJECT_NAME}
  VERSION ${SKBUILD_PROJECT_VERSION}
  LANGUAGES CXX)

find_package(pybind11 CONFIG REQUIRED)

python_add_library(_core MODULE cpp/main.cpp WITH_SOABI)
target_link_libraries(_core PRIVATE pybind11::headers)
target_compile_definitions(_core PRIVATE VERSION_INFO=${PROJECT_VERSION})


# The install directory is the output (wheel) directory
install(TARGETS _core DESTINATION rosia)
