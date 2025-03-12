cmake_minimum_required(VERSION 3.10.0)
project(CMakeOpenGLTest VERSION 0.1.0 LANGUAGES C CXX)

# finds the OpenGL package.
find_package(OpenGL REQUIRED)

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

# finds the library path and includes it in the CMake project.
set(LIBRARY_PATH "${PROJECT_SOURCE_DIR}/lib")
target_include_directories(CMakeOpenGLTest PUBLIC ${LIBRARY_PATH})

# includes OpenGL.
include_directories(${OPENGL_INCLUDE_DIRS})

# includes the GLFW library.
target_link_libraries(CMakeOpenGLTest ${OPENGL_LIBRARIES} ${LIBRARY_PATH}/libglfw3dll.a)
