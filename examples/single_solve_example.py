#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
""" This file is a part of the VeRyPy classical vehicle routing problem
heuristic library and demonstrates the simple use case of solving a single
TSPLIB formatted problem instance file with a single heuristic algorithm and
printing the resulting solution route by route."""
###############################################################################

import os
from VeRyPy.cvrp_io import read_TSPLIB_CVRP
from VeRyPy.classic_heuristics.parallel_savings import parallel_savings_init
from VeRyPy.cvrp_util import sol2routes

E_n51_k5_path = r"E-n51-k5.vrp" if 'examples' in os.getcwd()\
                                else r"examples/E-n51-k5.vrp"

problem = read_TSPLIB_CVRP(E_n51_k5_path)

solution = parallel_savings_init(
    D=problem.distance_matrix, 
    d=problem.customer_demands, 
    C=problem.capacity_constraint)

for route_idx, route in enumerate(sol2routes(solution)):
    print("Route #%d : %s"%(route_idx+1, route))
