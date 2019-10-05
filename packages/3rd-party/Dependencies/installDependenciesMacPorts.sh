#!/bin/sh

mkdir -p /opt/mports
cd /opt/mports
git clone https://github.com/macports/macports-base.git
cd /opt/mports/macports-base
./configure --enable-readline
make
make install
make distclean

port -f install cmake +x86_64 +Debug -d
port -f install sqlite3-tcl +x86_64 +Debug -d
port -f install boost  +x86_64 -d
port -f install wxWidgets-3.2 wxWidgets_select wxWidgets-common wxMaxima py27-wxpython-3.0 py27-wxpython-2.8 
port -f install wxWidgets-3.0 wxWidgets-3.2 wxWidgets-2.8
port -f install aquaterm  +x86_64 -d
port -f install cairo  +x86_64 -d
port -f install xercesc3  +x86_64 -d

port -f install xercesj  +x86_64 -d
port -f install f2c libf2c +x86_64 -d
port -f install p7zip keka +x86_64 -d
port -f install curl curl-ca-bundle

port -f install pcre
port -f install pcre2
port -f install pcrexx
port -f install ocaml-pcre
port -f install cl-ppcre
