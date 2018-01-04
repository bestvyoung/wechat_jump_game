#!/usr/bin/env bash 
echo "----make sure your device connet with computer and open developer mode----"
echo "--------------------------Download Brew--------------------------"
ruby -e "$(curl -fsSL --insecure https://raw.githubusercontent.com/Homebrew/install/master/install)"
echo "-------------------Download android-platform-tools-----------------"
brew cask install android-platform-tools
echo "---------------------------Run Script--------------------------"

