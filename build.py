from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    # These commands will be executed before installing conan packages in docker.
    command = "conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber" \
        "&& sudo apt-get -qq update && sudo apt-get -qq install -y libmaxminddb-dev"
    builder = ConanMultiPackager(docker_entry_script=command)

    # For some reason x86 arch will not work, so build is only for x86_64.
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86_64',
        'arch_build': 'x86_64', 'build_type': 'Release', 'compiler': 'gcc'})
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86_64',
        'arch_build': 'x86_64', 'build_type': 'Debug', 'compiler': 'gcc'})

    builder.run()