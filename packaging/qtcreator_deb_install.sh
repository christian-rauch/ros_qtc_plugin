#!/usr/bin/env bash

VER="14.0.1"
DEBNAME="qtcreator-opensource-linux-$(uname --machine)-${VER}.deb"

wget https://download.qt.io/official_releases/qtcreator/14.0/${VER}/cpack_experimental/${DEBNAME}

sudo apt install ./${DEBNAME}
