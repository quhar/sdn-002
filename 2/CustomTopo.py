'''
Coursera:
- Software Defined Networking (SDN) course
-- Programming Assignment 2

Professor: Nick Feamster
Teaching Assistant: Arpit Gupta, Muhammad Shahbaz
'''

from mininet.topo import Topo

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)
        
        core = self.addSwitch('c1')
        levels = ('a', 'e', 'h')
        parents = {}
        for level in levels:
            parents[level] = {}
        parents['a'][1] = parents['a'][2] = core
        opts = {'a': linkopts1, 'e': linkopts2, 'h': linkopts3}
        for level in levels:
            level_max = fanout**(levels.index(level)+1)
            for dev in xrange(1, level_max + 1):
                if level != 'h':
                    d_name = self.addSwitch("%s%s" % (level, dev))
                    parents[levels[levels.index(level)+1]][dev] = d_name
                else:
                    d_name = self.addHost("%s%s" % (level, dev))
                parent_index =(dev + fanout - 1) / fanout 
                self.addLink(d_name, parents[level][parent_index], **opts[level]) 
                    
topos = { 'custom': ( lambda: CustomTopo() ) }
