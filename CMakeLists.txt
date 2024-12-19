cmake_minimum_required(VERSION 3.10.0)
project(CMakeOpenGLTest VERSION 0.1.0 LANGUAGES C CXX)

# finds the OpenGL & GLFW packages.
find_package(OpenGL REQUIRED)
find_package(glfw3 REQUIRED)

# finds all .h and .cpp files. also compiles "glad.c".
file(GLOB_RECURSE SOURCES
    "include/*.h"
    "include/*.cpp"
    "glad.c"
)

# tells CMake to create a .exe file using the specified source files.
add_executable(CMakeOpenGLTest main.cpp ${SOURCES})

# handles include directories and libraries.
target_include_directories(CMakeOpenGLTest PRIVATE "include/")

include_directories(${OPENGL_INCLUDE_DIRS})
target_link_libraries(CMakeOpenGLTest ${OPENGL_LIBRARIES} glfw)

include(CTest)
enable_testing()
