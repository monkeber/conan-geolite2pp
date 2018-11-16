### Description

Conan package for [GeoLite2++](https://www.ccoderun.ca/GeoLite2PP/api/index.html).
GeoLite2++ is C++ API for MaxMind's GeoLite2 Database.

### Dependencies

If you want to use this package in `Debug` mode, there are some implications:

If you on the OS which uses `apt` tool as package manager then you are good, during install you may be prompted to give sudo rights in order to install 2 packages:
 - libmaxminddb0
 - libmaxminddb-dev

If you on Arch Linux the you should install libmaxminddb library by yourself on your system, probably the same applies to Windows, building on windows is not tested at all.

### Package Status

| Bintray | Linux |
|:-----------:|:-------------------:|
| [ ![Download](https://api.bintray.com/packages/monkeber/monkeber/geolite2%2B%2B%3Amonkeber/images/download.svg) ](https://bintray.com/monkeber/monkeber/geolite2%2B%2B%3Amonkeber/_latestVersion) | [![Build Status](https://travis-ci.org/monkeber/conan-geolite2pp.svg?branch=master)](https://travis-ci.org/monkeber/conan-geolite2pp)

### Basic setup

```bash
$ conan install geolite2++/0.0.1-2561@monkeber/stable
```

### Project setup

```py
from conans import ConanFile, CMake

class AppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    requires = "geolite2++/0.0.1-2561@monkeber/stable"

    default_options = "geolite2++:shared=False"

    generators = "cmake"
```

Complete the installation of requirements for your project running:

```bash
conan install .
```

Project setup installs the libraries (with all needed dependencies) and generates
the files *conanbuildinfo.txt* and *conanbuildinfo.cmake*
with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io.

## Publish The Package

The example below shows the commands used to publish to conan repository.

### Add Remote

```bash
$ conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber 
```

### Build

Builds a binary package for recipe (conanfile.py) located in current dir. 
For more info please check [conan create](http://docs.conan.io/en/latest/reference/commands/creator/create.html#conan-create).

```bash
$ conan create . monkeber/stable
```

### Upload

Uploads a recipe and binary packages to a remote. 
For more info please check [conan upload](http://docs.conan.io/en/latest/reference/commands/creator/upload.html#conan-upload).

```bash
$ conan upload geolite2++/0.0.1-2561@monkeber/stable --all -r monkeber
```