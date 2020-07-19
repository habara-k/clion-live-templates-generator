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

**If you have already set up a live templates, please make a backup before you overwrite it.**

- macOS
```
$ cp -i C_C__.xml ~/Library/Application\ Support/JetBrains/CLion2020.1/templates/C_C__.xml
```
For Linux and Windows, please refer to the following links

https://pleiades.io/help/clion/tuning-the-ide.html#config-directory

## Try Live templates

- restart CLion
- push `cmd + j`

![](https://user-images.githubusercontent.com/34413567/87849457-c9820080-c923-11ea-881f-6daabb676b2f.png)
