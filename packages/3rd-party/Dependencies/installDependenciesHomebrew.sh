#!/bin/sh

/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"


brew install cmake
brew install sqlite
brew install boost
brew install wxmac
brew install wxMaxima 
brew install wxpython
brew install cairo
brew install xerces-c

#port -f install f2c libf2c +x86_64 -d


#port -f install f2c libf2c +x86_64 -d
./buildLibf2c.sh

brew install p7zip
brew install curl 

brew install pcre
brew install pcre2
brew install pcre++
# brew install ocaml-pcre
# port -f install cl-ppcre
