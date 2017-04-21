#!/bin/bash
VER=25.1
WORK=/tmp/work

mv /usr/local/src/emacs-$VER $WORK

cd emacs-$VER
./configure --without-x
make
make install
cd ..
cd /usr/local
tar -zcf ../emacs-${VER}.tar.gz .
