cmake_minimum_required(VERSION 3.10.0)
project(CMakeOpenGLTest VERSION 0.1.0 LANGUAGES C CXX)

find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

file(GLOB_RECURSE SOURCES
    "include/*.h"
    "include/*.cpp"
    "glad.c"
)

add_executable(CMakeOpenGLTest main.cpp ${SOURCES})

target_include_directories(CMakeOpenGLTest PRIVATE "include/")

include_directories(${OPENGL_INCLUDE_DIRS})
target_link_libraries(CMakeOpenGLTest ${OPENGL_LIBRARIES})

target_link_libraries(CMakeOpenGLTest glfw)

include(CTest)
enable_testing()
