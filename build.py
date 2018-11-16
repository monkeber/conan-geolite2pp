from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber"
    builder = ConanMultiPackager(docker_entry_script=command)
    builder.add_common_builds()
    builder.run()