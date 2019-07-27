#!/bin/sh

export DYLD_LIBRARY_PATH=
export PLATFORM=mac
export wxWidgets_ROOT_DIR=/usr/local/Cellar/wxmac/3.0.4_1
export WX_LIB_LOC=$wxWidgets_ROOT_DIR/lib
export wxWidgets_LIBRARIES=$wxWidgets_ROOT_DIR/lib
export wxWidgets_INCLUDE_DIRS=$wxWidgets_ROOT_DIR/include
export SPICE_DIR=/Users/danielbeatty/projects/BeanStalk/cubsat/Dependencies/CSPICE/cspice/
export CSPICE_DIR=$SPICE_DIR/include
export CSPICE_INCLUDE_DIR=$SPICE_DIR/include/SpiceUsr.h
export F2C_LOC='/usr/local/Cellar/f2c/HEAD'
export F2C_DIR='/usr/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/Numeric'
export F2C_DEPENDS_DIR=/usr/local/include:/usr/local/lib
export PCRE_LIB_LOC=/usr/local/lib
export PATH=$F2C_LOC/bin:$PATH:$wxWidgets_ROOT_DIR/bin