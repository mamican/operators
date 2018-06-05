from conans import ConanFile, CMake
import os

class TAOCPPOperatorsConan(ConanFile):
    name = "taocpp-operators"
    description = "C++11 single-header library that provides highly efficient, move aware operators for arithmetic data types"
    homepage = "https://github.com/taocpp/operators"
    url = homepage
    license = "MIT"
    author = "taocpp@icemx.net"
    exports_sources = "include*", "LICENSE", "CMakeLists.txt"

    def package(self):
        cmake = CMake(self)

        cmake.definitions["TAOCPP_OPERATORS_BUILD_TESTS"] = "OFF"
        cmake.definitions["TAOCPP_OPERATORS_BUILD_EXAMPLES"] = "OFF"
        cmake.definitions["TAOCPP_OPERATORS_INSTALL_DOC_DIR"] = "licenses"

        cmake.configure()
        cmake.install()

    def package_id(self):
        self.info.header_only()