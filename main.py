from puzzle import generate_instance, generate_goal_state, print_board
from heuristics import heuristic
from ida_star import ida_star

if __name__ == "__main__":
    n_dimension, k_movement = map(int, input().split())
    initial_state, path = generate_instance(n_dimension, k_movement)
    goal_state = generate_goal_state(n_dimension)
    
    print("Initial State:")
    print_board(initial_state, n_dimension)
    
    solution_path, cost = ida_star(initial_state, n_dimension, goal_state, heuristic)
    
    if solution_path:
        print("\nSolution found with cost:", cost)
        print("Moves:", [move for _, move in solution_path[1:]])
    else:
        print("\nNo solution found.")