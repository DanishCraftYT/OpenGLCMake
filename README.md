# Overview
uses CMake to build OpenGL, GLFW, Glad, ImGUI, and VCPKG (package manager). it's been tested using the GCC compiler. feel free to use my code or CMakelists.txt file in your project.<br>

# Requirements
* GCC compiler.<br>
* Make.<br>
* Python 3.13.<br>
* (optional) vcpkg. by default the vcpkg packages files are included in this project however if you want to update them. you can follow [this guide](https://github.com/DanishCraftYT/OpenGLCMake?tab=readme-ov-file#updating-glfw).<br>

# Install Guide (Windows)
download msys2 from [msys2.org](https://www.msys2.org/). once installed. open `msys2.exe` and type `pacman -S mingw-w64-x86_64-toolchain` to install the GCC compiler and Make. you can download Python from [python.org](https://www.python.org/) and optionally you can download VCPKG from the [vcpkg github repo](https://github.com/microsoft/vcpkg/releases) if you want to update the VCPKG packages this project uses.<br>

# Building The Project
once you have met all the requirements listed above. clone the repo and run "WinBuild.py". then run the "InstallLibraries.py" file.<br>

# updating VCPKG packages
to update the vcpkg packages. run the "InstallLibraries.py" script and type "y" to update the vcpkg packages. then specify a path to the vcpkg root directory and wait for it to reinstall the vcpkg packages and copy over the new files into the project.<br>
