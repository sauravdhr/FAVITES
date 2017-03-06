#! /usr/bin/env python3
'''
Niema Moshiri 2016

"TransmissionTimeSample" module, where transmissions follow the SI model
'''
from TransmissionTimeSample import TransmissionTimeSample
import modules.FAVITES_ModuleFactory as MF
import FAVITES_GlobalContext as GC
from random import choice

class TransmissionTimeSample_SI(TransmissionTimeSample):
    def init():
        global exponential
        from numpy.random import exponential
        assert "TransmissionNodeSample_SI" in str(MF.modules['TransmissionNodeSample']), "Must use TransmissionNodeSample_SI module"
        GC.infection_rate = float(GC.infection_rate)
        assert GC.infection_rate > 0, "infection_rate must be positive"
        GC.trans_pq = None
        GC.trans_pq_v2trans = None

    def sample_time():
        if GC.contact_network.num_uninfected_nodes() == 0:
            GC.next_trans = None
            GC.end_time = GC.time
            return None
        # fill priority queue of infection events if empty (if possible)
        if GC.trans_pq is None:
            GC.trans_pq = GC.SortedLinkedList()
            GC.trans_pq_v2trans = dict()
            susceptible = set()
        if len(GC.trans_pq) == 0:
            for node in GC.contact_network.get_infected_nodes():
                for edge in GC.contact_network.get_edges_from(node):
                    neighbor = edge.get_to()
                    if not neighbor.is_infected():
                        susceptible.add(neighbor)
            for v in susceptible:
                infected_neighbors = [edge.get_from() for edge in GC.contact_network.get_edges_to(v) if edge.get_from().is_infected()]
                if len(infected_neighbors) > 0:
                    u = choice(infected_neighbors)
                    t = GC.time + exponential(scale=1/(GC.infection_rate*len(infected_neighbors))) # min of exponentials is exponential with sum of rates
                    GC.trans_pq.put(v,t)
                    GC.trans_pq_v2trans[v] = (u,v,t)

        # get next transmission event
        v = GC.trans_pq.getFront()
        u,v,t = GC.trans_pq_v2trans[v]
        GC.next_trans = (u,v,t)
        del GC.trans_pq_v2trans[v]
        return t