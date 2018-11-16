from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber"
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.run()