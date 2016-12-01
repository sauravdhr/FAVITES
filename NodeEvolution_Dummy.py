#! /usr/bin/env python3
'''
Niema Moshiri 2016

"NodeEvolution" module, dummy implementation
'''
import FAVITES_Global                   # for global access variables
from NodeEvolution import NodeEvolution # abstract NodeEvolution class
from sys import stderr                  # to write to standard error

class NodeEvolution_Dummy(NodeEvolution):
    def evolve(node):
        print('\nWARNING: Using dummy NodeEvolution implementation!\n', file=stderr)
        node.add_infection_tree(FAVITES_Global.modules['Tree']())