#! /usr/bin/env python3
'''
Niema Moshiri 2016

"SeedSequence" module, where seed sequences are randomly generated and infect
the node at time 0
'''
from SeedSequence import SeedSequence # abstract SeedSequence class
from ContactNetworkNode import ContactNetworkNode # to verify node
from random import choice                         # randomly choose nucleotides

class SeedSequence_Random(SeedSequence):
    '''
    Implement the ``SeedSequence'' module by randomly selecting seed sequences
    and infecting ``node'' at time 0
    '''

    def infect(user_input, node):
        assert isinstance(node, ContactNetworkNode), "ERROR: node is not a ContactNetworkNode object"
        assert 'seed_sequence_length' in user_input, "ERROR: User did not specify SeedSequenceLength"
        k = user_input['seed_sequence_length']
        sequence = ''.join([choice('ACGT') for _ in range(k)])
        node.infect(0,sequence)