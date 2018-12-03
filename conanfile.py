
from conans import ConanFile, CMake, tools
from conans.tools import os_info, SystemPackageTool
from pathlib import Path
import os
import shutil


class uwebsocketConan(ConanFile):
    name = "uwebsocket"
    version = "0.0.1"
    license = "LGPL"
    author = "kaiyin keezhong@qq.com"
    url = "https://github.com/kindlychung/conan_uwebsocket"
    description = "change_your_description"
    topics = ("cpp", )
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    requires = ("docopt/0.6.2@conan/stable",)
    generators = "cmake"
    exports_sources = "src/%s/*" % name, "src/CMakeLists.txt", "src/*.cmake"

    def system_requirements(self):
        pack_list = None
        if os_info.linux_distro == "ubuntu":
            pack_list = []
        if pack_list:
            for p in pack_list:
                installer = SystemPackageTool()
                installer.install(p)

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="src")
        cmake.build()

    def package(self):
        self.copy("conan_uwebsocket/*.hpp", dst="include", src="src")
        self.copy("conan_uwebsocket/*.h", dst="include", src="src")
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.dylib*", dst="lib", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def imports(self):
        self.copy("*", dst="include", src="include")
        self.copy("*", dst="bin", src="lib")

    def package_info(self):
        self.cpp_info.libs = ["conan_uwebsocket"]
