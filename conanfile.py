from conans import ConanFile, CMake, tools
import os

class Geolite2Conan(ConanFile):
    name = "geolite2pp"
    version = "0.0.1-2561"
    url = "https://github.com/monkeber/conan-geolite2pp"
    description = "C++ API for MaxMind's GeoLite2 Database"
    settings = "os", "compiler", "build_type", "arch"
    requires = "maxminddb/1.3.2@monkeber/testing"
    generators = "cmake"
    build_policy = "missing"
    options = { "shared": [True, False] }
    default_options = "shared=False"

    def source(self):
        self.run("git clone git@gitlab.instacoins.com:instacoins/geolite2pp.git", "master")

    def build(self):
        args = list()
        args.append("-DCMAKE_LIBRARY_PATH=%s" % self.deps_cpp_info["maxminddb"].lib_paths[0])
        args.append("-DCMAKE_CXX_FLAGS=-I%s"
            % self.deps_cpp_info["maxminddb"].include_paths[0])
        args.append("-DCMAKE_CXX_STANDARD=11")

        cmake = CMake(self)
        cmake.configure(source_folder="geolite2pp", args=args)
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include", src="geolite2pp/src-lib")
        if self.options.shared:
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so", dst="lib", src="src-lib", keep_path=False)
            self.copy("*.so.0", dst="lib", src="src-lib", keep_path=False)
            self.copy("*.dylib", dst="lib", src="src-lib", keep_path=False)
        else:
            self.copy("*geolite2++.lib", dst="lib", keep_path=False)
            self.copy("*.a", dst="lib", src="src-lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geolite2++", "maxminddb"]
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.includedirs = ["include"]
        if self.settings.os == "Linux":
            self.cpp_info.libs.append("pthread")

