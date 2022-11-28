import sys
import time
from ortools.linear_solver import pywraplp
from lib.file_parser import parse_file
from lib.scores_matrix import suitability_scores_matrix

def main():
    """Calculates the driver assignments based on SS scores and returns results."""
    drivers = parse_file(open(sys.argv[-1], encoding="UTF-8"))
    addresses = parse_file(open(sys.argv[-2], encoding="UTF-8"))
    ss_scores = suitability_scores_matrix(drivers, addresses)
    num_drivers = len(ss_scores)
    num_addresses = len(ss_scores[0])

    # SCIP (Solving Constraint Integer Programs) is a solver for mixed integer programming (MIP).
    # Pairing drivers with addresses is considered an assignment problem, and SCIP is a good tool for solving
    # this type of problem.
    solver = pywraplp.Solver.CreateSolver('SCIP')

    if not solver:
        return

    # This looks to see if a driver, d, has been assigned to an address, a.
    # If so, track_assignments stores a 1 for that combination. If not, it
    # will store a 0.
    track_assignments = {}
    for d in range(num_drivers):
        for a in range(num_addresses):
           track_assignments[d, a] = solver.IntVar(0, 1, '')

    # Assign one driver to one delivery address
    for d in range(num_drivers):
        solver.Add(solver.Sum([track_assignments[d, a] for a in range(num_addresses)]) <= 1)

    # Each delivery address is assigned to one driver
    for a in range(num_addresses):
        solver.Add(solver.Sum([track_assignments[d, a] for d in range(num_drivers)]) == 1)

    # Calculates the maximum suitability score by summing ss score for driver address pair
    # where the same combination in track_assignments is 1.
    maximum_ss = []
    for d in range(num_drivers):
        for a in range(num_addresses):
            maximum_ss.append(ss_scores[d][a] * track_assignments[d, a])
    solver.Maximize(solver.Sum(maximum_ss))

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL or status == pywraplp.Solver.FEASIBLE:
        for d in range(num_drivers):
            for a in range(num_addresses):
                if track_assignments[d, a].solution_value() == 1:
                    print(f'{d+1}. Driver {drivers[d]["first_name"]} {drivers[d]["last_name"]}' +
                          f' assigned to destination {addresses[a]["street_number"]} {addresses[a]["street_name"]}.' +
                          f' {addresses[a]["city"]}, {addresses[a]["state"]}'
                          f' SS: {ss_scores[d][a]}')
        print(f'Total SS = {solver.Objective().Value()}\n')
    else:
        print('No solution found.')


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))