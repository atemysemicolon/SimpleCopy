#!/usr/bin/env python

import sys
import logging
debug = True
if debug:
    print(sys.executable)
    print(sys.argv)
    print (__file__)
import pyperclip

flag_argmode = False
flag_pipemode = False

if __file__ in sys.argv:
    sys.argv.pop(0)

if debug:
    print(sys.argv)

if len(sys.argv):
    flag_argmode = True
else:
    flag_pipemode = True

if flag_argmode:
    pyperclip.copy(sys.argv[0])

if flag_pipemode:
    pyperclip.copy(sys.stdin.readline())
