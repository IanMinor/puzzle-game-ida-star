from puzzle import generate_instance, generate_goal_state, print_board
from heuristics import heuristic, h2
from ida_star import ida_star
from time import perf_counter


def run_instance(n, k):
    initial_state, _ = generate_instance(n, k)
    goal_state = generate_goal_state(n)
    start = perf_counter()
    solution_path, cost = ida_star(initial_state, n, goal_state, h2, 30)
    end = perf_counter()

    return {
        'n': n,
        'k': k,
        'initial_state': initial_state,
        'goal_state': goal_state,
        'solved': solution_path is not None,
        'cost': cost,
        'time': round(end - start, 2),
        'moves': [move for _, move in solution_path[1:]] if solution_path else None
    }
    

if __name__ == "__main__":
    n_dimension, k_movement = map(int, input().split())
    result = run_instance(n_dimension, k_movement)
    
    print("Initial State:")
    print_board(result['initial_state'], n_dimension)
        
    if result['solved']:
        print("\nSolution found with cost:", result['cost'])
        print("Moves:", result['moves'])
        print("Final State:")
        print_board(result['goal_state'], n_dimension)
        print("Time taken:", result['time'])
    else:
        print("\nNo solution found.")