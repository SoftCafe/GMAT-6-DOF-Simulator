#!/bin/sh

export DYLD_LIBRARY_PATH=
export PLATFORM=mac
export wxWidgets_ROOT_DIR=/opt/local/Library/Frameworks/wxWidgets.framework/Versions/wxWidgets/3.1
export WX_LIB_LOC=$wxWidgets_ROOT_DIR/lib
export wxWidgets_LIBRARIES=$wxWidgets_ROOT_DIR/lib
export wxWidgets_INCLUDE_DIRS=$wxWidgets_ROOT_DIR/include
export SPICE_DIR=/Users/danielbeatty/projects/BeanStalk/cubsat/Dependencies/CSPICE/cspice/
export CSPICE_DIR=$SPICE_DIR/include
export CSPICE_INCLUDE_DIR=$SPICE_DIR/include/SpiceUsr.h
export F2C_LOC='/opt/local/'
export F2C_DIR='/opt/local/Library/Frameworks/Python.framework/Versions/2.7/include/python2.7/Numeric'
export F2C_DEPENDS_DIR=/opt/local/include:/opt/local/lib
export PCRE_LIB_LOC=/opt/local
export PATH=$PATH:$wxWidgets_ROOT_DIR/bin