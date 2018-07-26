# SimpleCopy
A simple command line tool to (allow to) pipe text output into the clipboard

# Dependencies
* pyperclip
    - Install pyperclip by doing `pip install pyperclip`

# Installation
* Just clone this repo by doing `https://github.com/atemysemicolon/SimpleCopy`
* This tool becomes useful if its in your path, or in your bin folder
    - link it to your bin `sudo ln -s <path of simplecopy.py> /usr/bin/.`
    - Maybe you can use a shortcut like *sc* with `sudo ln -s <path of simplecopy.py> /usr/bin/sc`

# Usage
Simple Copy (sc) can be used in two modes

* Regular argument mode
    - `sc "helloworld"` --> helloworld gets copied to clipboard
* Pipe Mode
    - `echo "helloworld" | sc` --> helloworld gets copied to clipboard
    - `pwd | sc` --> current path gets copied to clipboard

# License
* Refer to LICENSE.md




