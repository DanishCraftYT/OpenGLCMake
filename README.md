# Overview
uses CMake to build OpenGL, GLFW, Glad, and ImGUI. it's been tested using the GCC compiler, vcpkg and Visual Studio Code. feel free to use my code or CMakelists.txt file in your project.<br>

# Requirements
* GCC compiler.<br>
* Python 3.13.<br>

## OPTIONAL
* vcpkg glfw3 package. by default the glfw3 package files are included in this project however if you want to update them. you can follow [this guide](https://github.com/DanishCraftYT/OpenGLCMake?tab=readme-ov-file#updating-glfw).<br>

# Building The Project
once you have met all the requirements listed above. clone the repo and run "WinBuild.py". then run the "InstallLibraries.py" file.<br>

# updating GLFW
to update GLFW. first update the glfw3 package. then delete the "lib" and "include/GLFW" folders in this project.

## Windows
delete the "glfw3.dll" file in the build output folder in this project. run the "InstallLibraries.py" script to install the glfw3 package and copy it's files into this project. then build the project and run it.<br>
