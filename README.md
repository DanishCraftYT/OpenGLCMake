# Overview
uses CMake to build OpenGL, GLFW, Glad, ImGUI, and VCPKG (package manager). it's been tested using the GCC compiler. feel free to use my code or CMakelists.txt file in your project.<br>

# Requirements
* GCC compiler.<br>
* CMake.<br>
* Make.<br>
* Python 3.13.<br>
* (optional) vcpkg. by default the vcpkg packages files are included in this project however if you want to update them. you can follow [this guide](https://github.com/DanishCraftYT/OpenGLCMake/tree/main?tab=readme-ov-file#updating-vcpkg-packages).<br>

# Install Guide (Windows)
### GCC Compiler and Make
download msys2 from [msys2.org](https://www.msys2.org/). once installed. open `msys2.exe` and type `pacman -S mingw-w64-x86_64-toolchain` to install the GCC compiler and Make. make sure you also add the `mingw64/bin` folder to PATH.

### Python
you can download Python from [python.org](https://www.python.org/) and make sure you also add Python to PATH.<br>

### CMake
you will also need CMake to build the project. you can donwload it from [cmake.org](https://cmake.org/download/).<br>

### VCPKG (optional)
you can also install VCPKG if you want to update the VCPKG packages this project uses. you can download VCPKG from the [vcpkg github repo](https://github.com/microsoft/vcpkg/releases). once installed. open the root folder of the VCPKG installation and run the `bootstrap-vcpkg.bat` script to create the `vcpkg.exe` executable. make sure you also add the root directory of your VCPKG installation to PATH.<br>

# Building The Project
once you have met all the requirements listed above. clone the repo and run "WinBuild.py". then run the "InstallLibraries.py" file.<br>

# updating VCPKG packages
to update the vcpkg packages. run the "InstallLibraries.py" script and type "y" to update the vcpkg packages. then specify a path to the vcpkg root directory and wait for it to reinstall the vcpkg packages and copy over the new files into the project.<br>
