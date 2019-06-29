#!/bin/sh

port -f uninstall sqlite3-tcl
port -f uninstall boost
port -f uninstall wxWidgets-3.2 wxWidgets_select wxWidgets-common wxMaxima py27-wxpython-3.0 py27-wxpython-2.8 
port -f uninstall aquaterm
port -f uninstall cairo
port -f uninstall xercesc3

port -f uninstall xercesj


port -f uninstall xercesj  +x86_64 -d
port -f uninstall f2c libf2c +x86_64 -d
port -f uninstall p7zip keka +x86_64 -d
port -f uninstall curl curl-ca-bundle

port -f uninstall pcre
port -f uninstall pcre2
port -f uninstall pcrexx
port -f uninstall ocaml-pcre
port -f uninstall cl-ppcre