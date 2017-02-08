#! /usr/bin/env python3
'''
Niema Moshiri 2016

"Logging" module, where log messages are written to standard error.
'''
from Logging import Logging # abstract Logging class
import FAVITES_GlobalContext as GC
from sys import stderr as s

class Logging_STDERR(Logging):
    def init():
        pass

    def flush():
        s.flush()

    def close():
        s.flush()

    def write(message=''):
        s.write(message)
        s.flush()

    def writeln(message=''):
        s.write(message)
        s.write('\n')
        s.flush()