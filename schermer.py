import cvrp_io
from classic_heuristics.parallel_savings import parallel_savings_init
from local_search import LSOPT, do_local_search
from local_search.intra_route_operators import do_2opt_move
from local_search.inter_route_operators import do_1point_move, do_2point_move
from util import sol2routes

VRDP_path = r"examples/schermer.vrp"

problem = cvrp_io.read_TSPLIB_CVRP(VRDP_path)

sol = parallel_savings_init(D=problem.distance_matrix, d=problem.customer_demands, C=problem.capacity_constraint)
print("after parallel savings")
for route_idx, route in enumerate(sol2routes(sol)):
    print("Route #%d : %s"%(route_idx+1, route))

sol = do_local_search([do_2opt_move], sol, D=problem.distance_matrix, d=problem.customer_demands, C=problem.capacity_constraint, L=None, operator_strategy=LSOPT.BEST_ACCEPT)
print("after 2-opt")
for route_idx, route in enumerate(sol2routes(sol)):
    print("Route #%d : %s"%(route_idx+1, route))

sol = do_local_search([do_1point_move], sol, D=problem.distance_matrix, d=problem.customer_demands, C=problem.capacity_constraint, L=None, operator_strategy=LSOPT.BEST_ACCEPT)
print("after SR")
for route_idx, route in enumerate(sol2routes(sol)):
    print("Route #%d : %s"%(route_idx+1, route))

sol = do_local_search([do_2point_move], sol, D=problem.distance_matrix, d=problem.customer_demands, C=problem.capacity_constraint, L=None, operator_strategy=LSOPT.BEST_ACCEPT)
print("after SE")
for route_idx, route in enumerate(sol2routes(sol)):
    print("Route #%d : %s"%(route_idx+1, route))