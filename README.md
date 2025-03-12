# Overview
uses CMake to build OpenGL, GLFW, Glad, and ImGUI. it's been tested using the GCC compiler, vcpkg and Visual Studio Code. feel free to use my code or CMakelists.txt file in your project.<br>

# Requirements
* GCC compiler.<br>
* vcpkg glfw3 package. by default the glfw3 package files are included in this project however if you want to update them. you can follow [this guide](https://github.com/DanishCraftYT/OpenGLCMake?tab=readme-ov-file#updating-glfw).<br>
* Visual Studio Code.<br>
* Visual Studio Code Extensions: C/C++ and CMake Tools.<br>

# Building The Project
once you have met all the requirements listed above. clone the repo and open it in Visual Studio Code. then in the CMake tab you can build the project.<br>

## IMPORTANT
if the "glfw3.dll" file is missing from the build output directory. please run the "InstallLibraries.py" script which will copy the "glfw3.dll" file into the build output directory or copy and paste the "glfw3.dll" file into the build output directory. the "glfw3.dll" file can be found in the "lib" folder.<br>

# updating GLFW
to update GLFW. first update or install the glfw3 package. then delete the "lib" and "include/GLFW" folders in this project. then delete the "glfw3.dll" file in the build output folder in this project. then run the "InstallLibraries.py" script to install the glfw3 package and copy it's files into this project. then build the project and run it.<br>
