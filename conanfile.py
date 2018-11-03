from conans import ConanFile, CMake, tools
import os


class Geolite2Conan(ConanFile):
    name = "geolite2++"
    version = "0.0.1-2561"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Geolite2 here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    requires = "maxminddb/1.3.2@monkeber/stable"
    generators = "cmake"

    def source(self):
        tools.download("https://www.ccoderun.ca/GeoLite2PP/download" \
            "/geolite2++-{}-Source.tar.gz".format(self.version), "geolite2++.tar.gz")
        tools.unzip("geolite2++.tar.gz")
        os.unlink("geolite2++.tar.gz")
        self.run("mv geolite2++-{}-Source geolite2++".format(self.version))

    def build(self):
        cmake = CMake(self)
        self.run("ls")
        cmake.configure(source_folder="geolite2++")
        cmake.build()

    def package(self):
        self.run("cd geolite2++/scripts && ./geolite2pp_get_database.sh")
        self.copy("*.mmdb", dst="bin", src="geolite2++/scripts")
        self.copy("*.h*", dst="include", src="geolite2++/src-lib")
        self.copy("*geolite2++.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["geolite2++"]

