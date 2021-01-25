#!/bin/sh
# clang-tidy needs a 'compile_commands.json' in the root direcotry,
# which can be genereated in Qt Creator: Build → Generate Compilation Database
find . -regex './src/.*\(cpp\|h\)' -exec clang-tidy --fix {} \;
