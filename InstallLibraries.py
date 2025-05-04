import shutil
import os

# get's the directory of this script.
user_dir = os.path.abspath(os.path.dirname(__file__))

update_GLFW = input("do you want to update GLFW? (y/n): ").lower()

if update_GLFW == "y":
    # asks user for their vcpkg directory.
    vcpkg_dir = input("path to VCPKG installation: ")

    # exits the program if the vcpkg directory is invalid.
    if not os.path.exists(os.path.join(vcpkg_dir, "vcpkg.exe")):
        print("please specify a valid vcpkg directory")
        input("press enter to exit...")
        exit()

    # creates the "lib" folder if it doesn't exist.
    if not os.path.exists(os.path.join(user_dir, "lib")):
        print("creating lib folder")
        os.mkdir(os.path.join(user_dir, "lib"))
    
    # REINSTALLS GLFW3 PACKAGE FROM VCPKG #

    # removes the GLFW3 package.
    print("removing GLFW3 vcpkg package")
    os.system("vcpkg remove glfw3 --triplet=x64-mingw-dynamic --host-triplet=x64-mingw-dynamic")

    # installs the GLFW3 vcpkg package if it's not already installed.
    print("installing GLFW3 vcpkg package")
    os.system("vcpkg install glfw3 --triplet=x64-mingw-dynamic --host-triplet=x64-mingw-dynamic")
    
    # UPDATES GLFW #

    # contains the path to the GLFW package.
    glfw_path = os.path.join(vcpkg_dir, "packages/glfw3_x64-mingw-dynamic")
    
    # copies the "glfw3.dll" file into the "lib" folder if it's not already in that folder.
    print("getting glfw3.dll")
    shutil.copy(os.path.join(glfw_path, "bin/glfw3.dll"), os.path.join(user_dir, "lib/"))

    # copies the "libglfw3dll.a" file into the "lib" folder if it's not already in that folder.
    print("getting libglfw3dll.a")
    shutil.copy(os.path.join(glfw_path, "lib/libglfw3dll.a"), os.path.join(user_dir, "lib/"))

    # copies the GLFW source code into the include folder if it's not alreadt in that folder.
    print("getting GLFW source files")
    if not os.path.exists(os.path.join(user_dir, "include/GLFW")):
        os.mkdir(os.path.join(user_dir, "include/GLFW"))
    glfw_source_path = os.path.join(glfw_path, "include/GLFW")
    for filename in os.listdir(glfw_source_path):
        shutil.copy(os.path.join(glfw_source_path, filename), os.path.join(user_dir, "include/GLFW/"))

# exists the program if the build output folder doesn't exist.
if not os.path.exists(os.path.join(user_dir, "build/")):
    print("failed to find the build output folder. please run this script again once the build output folder has been created so it can copy the glfw3.dll file into the build output folder")
    exit()

# copies the "glfw3.dll" file into the build output folder if it isn't already in that folder or GLFW was updated.
if not os.path.exists(os.path.join(user_dir, "build/glfw3.dll")) or update_GLFW == "y":
    print("copying the glfw3.dll file to the build output folder")
    shutil.copy(os.path.join(user_dir, "lib/glfw3.dll"), os.path.join(user_dir, "build/"))

print("installed all libraries")

input("press enter to exit...")
