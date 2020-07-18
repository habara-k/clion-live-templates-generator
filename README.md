# clion-live-templates-generator

![CI](https://github.com/habara-k/clion-live-templates-generator/workflows/CI/badge.svg)
[![PyPI version](https://badge.fury.io/py/clion-live-templates-generator.svg)](https://badge.fury.io/py/clion-live-templates-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# What is this?

This is a tool to generate CLion's Live templates from a library of competitive programming.

Only C++ is supported.

# How to use

## Install

```
$ pip install clion-live-templates-generator
```

## Generate Live templates

```
$ lt-generate -d <YOUR_LIBRARY_DIR>
```

### Where to place

Example

- Windows (not tested)

```
$ mv C_C__.xml C:\Users\JohnS\AppData\Local\JetBrains\CLion2020.1\templates
```

- macOS
```
$ mv C_C__.xml ~/Library/Caches/JetBrains/CLion2020.1/templates
```

- Linux (not tested)
```
$ mv C_C__.xml ~/.cache/JetBrains/CLion2020.1/templates
```

## Try Live templates

- restart CLion
- push `cmd + j`

![](https://user-images.githubusercontent.com/34413567/87849457-c9820080-c923-11ea-881f-6daabb676b2f.png)
