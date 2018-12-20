from conans import ConanFile, CMake, tools


class SocketcancppConan(ConanFile):
    name = "socketcancpp"
    version = "1.0.0"
    license = "MIT"
    author = "Smart-Ag"
    url = "https://github.com/Smart-Ag/socketcan-cpp"
    description = "<Description of Socketcancpp here>"
    topics = ("socketcan", "can")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"
    exports_sources = ("src/*.cpp",
                       "include/socketcan_cpp/*",
                       "CMakeLists.txt",
                       "cmake/*",
                       "examples/*")

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["socketcan_cpp"]
