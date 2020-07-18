# clion-live-templates-generator

![](https://github.com/habara-k/clion-live-templates-generator/workflows/CI/badge.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

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
$ lt-generate -d <YOUR_LIBRARY>
```

- macOS
```
$ mv C_C__.xml ~/Library/Application\ Support/JetBrains/CLion{{YOUR_VERSION}}/templates/
```

## Use Live templates

- start CLion
- push `cmd + j`

![](https://user-images.githubusercontent.com/34413567/87849457-c9820080-c923-11ea-881f-6daabb676b2f.png)
