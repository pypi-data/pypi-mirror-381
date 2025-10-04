import os
import subprocess
import sys
import shutil # Import shutil for directory operations
from setuptools import setup, find_packages
from setuptools.command.build_ext import build_ext

# A custom build extension for CMake
class CMakeBuild(build_ext):
    def run(self):
        # Create a temporary build directory for CMake
        # self.build_temp is the standard temp directory for setuptools
        build_directory = os.path.abspath(self.build_temp)
        if not os.path.exists(build_directory):
            os.makedirs(build_directory)

        # --- Build SLEEF ---
        # SLEEF source is in vendor/sleef
        sleef_source_dir = os.path.abspath(os.path.join("vendor", "sleef"))
        # SLEEF will be built in a subdirectory of our main build temp
        sleef_build_dir = os.path.join(build_directory, "sleef_build")
        if not os.path.exists(sleef_build_dir):
            os.makedirs(sleef_build_dir)

        print("Configuring and building SLEEF...")
        # Configure SLEEF for static library output
        sleef_cmake_args = [
            "-DCMAKE_BUILD_TYPE=Release",
            "-DSLEEF_STATIC_LIBS=ON",  # Ensure static library is built
            "-DSLEEF_TEST=OFF",        # Don't build tests
            "-DSLEEF_SMP=OFF",         # Disable SMP if not needed, simplifies build
            "-DSLEEF_OPENMP=OFF",      # Disable OpenMP if not needed
            # Add more options as per SLEEF's CMakeLists.txt if you want to fine-tune
        ]
        subprocess.check_call(["cmake", sleef_source_dir, *sleef_cmake_args], cwd=sleef_build_dir)
        subprocess.check_call(["cmake", "--build", ".", "--config", "Release"], cwd=sleef_build_dir)
        print("SLEEF built successfully.")

        # Determine SLEEF's static library path (it might be in sleef_build_dir/lib or directly in sleef_build_dir)
        # We'll make a best guess and then verify
        sleef_static_lib_name = "libsleef.a" # Unix-like
        if sys.platform == "win32":
            sleef_static_lib_name = "sleef.lib" # Windows

        sleef_library_path = None
        # Common places for static libs after CMake build
        potential_sleef_lib_paths = [
            os.path.join(sleef_build_dir, sleef_static_lib_name),
            os.path.join(sleef_build_dir, "lib", sleef_static_lib_name),
            os.path.join(sleef_build_dir, "Release", sleef_static_lib_name), # Visual Studio might put it here
            os.path.join(sleef_build_dir, "src", "lib", sleef_static_lib_name), # Another potential
        ]

        for p in potential_sleef_lib_paths:
            if os.path.exists(p):
                sleef_library_path = p
                break
        
        if not sleef_library_path:
            raise FileNotFoundError(f"Could not find SLEEF static library ('{sleef_static_lib_name}') in expected locations: {potential_sleef_lib_paths}. Check SLEEF build output.")

        # Include directory for SLEEF headers
        sleef_include_dir = os.path.join(sleef_source_dir, "include") # SLEEF headers are typically in its source's include folder

        # --- Build Axon (our main project) ---
        print("Configuring and building Axon...")
        axon_cmake_args = [
            "-DCMAKE_BUILD_TYPE=Release",  # Or Debug
            # Output the shared library directly into our main build_directory
            f"-DCMAKE_LIBRARY_OUTPUT_DIRECTORY={build_directory}",
            f"-DSLEEF_INCLUDE_DIR={sleef_include_dir}",
            f"-DSLEEF_LIBRARY={sleef_library_path}", # Link against the found static SLEEF library
        ]
        
        # Add platform-specific arguments if needed by your Axon CMakeLists.txt
        # e.g., if you need to set specific compiler flags for Windows/macOS/Linux
        if sys.platform == "win32":
             axon_cmake_args.append("-GVisual Studio 17 2022") # Example for Visual Studio generator
             # Make sure to adjust for your Visual Studio version or use Ninja if installed

        subprocess.check_call(["cmake", os.path.abspath("."), *axon_cmake_args], cwd=build_directory)
        subprocess.check_call(["cmake", "--build", ".", "--config", "Release"], cwd=build_directory)
        print("Axon built successfully.")

        # Determine the correct library name based on the platform
        if sys.platform == "linux":
            lib_name = "libaxon.so"
        elif sys.platform == "darwin":
            lib_name = "libaxon.dylib"
        elif sys.platform == "win32":
            lib_name = "axon.dll"
        else:
            raise NotImplementedError(f"Unsupported platform: {sys.platform}")

        built_lib_path = os.path.join(build_directory, lib_name)
        
        # Verify the built library exists
        if not os.path.exists(built_lib_path):
            raise FileNotFoundError(f"Built library not found at: {built_lib_path}. Check Axon build output.")

        # Copy the built library to the axon package directory
        # This assumes the axon package is directly under the project root
        package_dir = os.path.join(os.path.abspath("."), "axon")
        if not os.path.exists(package_dir):
            os.makedirs(package_dir)
        
        destination_lib_path = os.path.join(package_dir, lib_name)
        print(f"Copying {built_lib_path} to {destination_lib_path}")
        shutil.copyfile(built_lib_path, destination_lib_path)
        print("Library copied successfully.")

# Function to dynamically determine package_data for the current platform
def get_platform_package_data():
    if sys.platform == "linux":
        return ['libaxon.so']
    elif sys.platform == "darwin":
        return ['libaxon.dylib']
    elif sys.platform == "win32":
        return ['axon.dll']
    else:
        return [] # Fallback, should ideally not happen due to CMakeBuild check

setup(
    name='axon',
    version='0.1.0',
    packages=find_packages(),
    cmdclass={
        'build_ext': CMakeBuild,
    },
    # Dynamically set package_data to include only the relevant library for the current platform
    # When building a wheel, this will ensure only the correct library is bundled.
    package_data={
        'axon': get_platform_package_data(),
    },
    # Ensure the package is not treated as zip_safe, as it contains compiled extensions
    zip_safe=False,
)
