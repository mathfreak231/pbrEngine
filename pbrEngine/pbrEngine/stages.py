'''
Created on 26.09.2015

@author: Felk
'''
from . import memorymap
from copy import copy

# aliases don't work, so a copy.
Stages = copy(memorymap.values.Colosseums)
# possible enums:
# GATEWAY, MAIN_STREET, WATERFALL, NEON, CRYSTAL, SUNNY_PARK, MAGMA, COURTYARD, SUNSET, STARGAZER, LAGOON