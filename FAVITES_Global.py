'''
Niema Moshiri 2016

Store global variables to be accessible by all FAVITES modules.
'''

def init():
    '''
    Initialize global access variables.
    '''
    # dictionary to store which implementations of each module are available
    global list_modules
    list_modules = {
        'ContactNetwork':         ['NetworkX'],
        'Driver':                 ['Default'],
        'EndCriteria':            ['Time','Transmissions','FirstTimeTransmissions'],
        'NodeEvolution':          ['Dummy'],
        'NodeSample':             ['Perfect'],
        'PostValidation':         ['Dummy'],
        'SeedSelection':          ['Random'],
        'SeedSequence':           ['Random'],
        'SourceSample':           ['Dummy'],
        'TransmissionNodeSample': ['Random'],
        'TransmissionTimeSample': ['Fixed'],
        'Tree':                   ['DendroPy']
    }

    # dictionary to store which implementation of each module was chosen
    global modules
    modules = {}

    # ContactNetwork object
    global contact_network
    contact_network = None

    # number of seed nodes
    global num_seeds
    num_seeds = None

    # seed sequence length
    global seed_sequence_length
    seed_sequence_length = None

    # global current time
    global time
    time = 0