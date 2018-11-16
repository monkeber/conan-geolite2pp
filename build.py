from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber" \
        "&& sudo apt-get -qq update && sudo apt-get -qq install -y libmaxminddb-dev"
    builder = ConanMultiPackager(docker_entry_script=command)
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86',
        'arch_build': 'x86', 'build_type': 'Release', 'compiler': 'gcc'})
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86',
        'arch_build': 'x86', 'build_type': 'Debug', 'compiler': 'gcc'})
    builder.run()