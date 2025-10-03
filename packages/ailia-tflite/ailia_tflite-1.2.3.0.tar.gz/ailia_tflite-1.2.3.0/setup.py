import os
import sys
import platform
import glob
import shutil
import platform

from setuptools import setup, Extension
from setuptools import find_packages

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

scripts = []
for f in glob.glob("ailia_tflite/*.py"):
    scripts.append(f)

def find_libraries():
    dll_names = []
    platforms = ["win32", "darwin", "linux_armv7l", "linux_aarch64", "linux_x86_64"]

    for platform in platforms:
        if platform == "win32" :
            dll_platform = "windows/x64"
            dll_type = ".dll"
        elif platform == "darwin" :
            dll_platform = "mac"
            dll_type = ".dylib"
        else:
            if platform == "linux_armv7l":
                dll_platform = "linux/armeabi-v7a"
            elif platform == "linux_aarch64":
                dll_platform = "linux/arm64-v8a"
            else :
                dll_platform = "linux/x64"
            dll_type = ".so"
    
        dll_path = "./ailia_tflite/" + dll_platform + "/"

        for f in glob.glob(dll_path+"*"+dll_type):
            f = f.replace("\\", "/")
            f = f.replace("./ailia_tflite/", "./")
            dll_names.append(f)

    dll_names.append("./LICENSE_AILIA_EN.pdf")
    dll_names.append("./LICENSE_AILIA_JA.pdf")
    dll_names.append("./oss/LICENSE_TENSORFLOW.txt")
    dll_names.append("./oss/LICENSE_INTELMKL.txt")
 
    return dll_names
    
if __name__ == "__main__":
    setup(
        name="ailia_tflite",
        scripts=scripts,
        version="1.2.3.0",
        description="ailia TFLite Runtime",
        long_description=long_description,
        long_description_content_type="text/markdown",
        author="ax Inc.",
        author_email="contact@axinc.jp",
        url="https://ailia.jp/",
        license="https://ailia.ai/license/en/",
        packages=find_packages(),
        package_data={"ailia_tflite":find_libraries()},
        include_package_data=True,
        python_requires=">3.6",
    )