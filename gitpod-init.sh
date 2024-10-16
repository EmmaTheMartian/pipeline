#!/usr/bin/env sh

git clone https://github.com/vlang/v
git clone https://github.com/emmathemartian/clockwork

cd v
make
sudo ./v symlink
cd ..

cd clockwork
v install EmmaTheMartian.Maple
v run . install
cd ..
