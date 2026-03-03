import random

INVERSE_MOVES = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}

def generate_goal_state(n):
    return tuple(list(range(1, n*n)) + [0])

def locate_zero_index(state):
    return state.index(0)

def valid_moves(state, n):
    zero_index = locate_zero_index(state)
    row = zero_index // n
    col = zero_index % n
    moves = []
    
    if row > 0:
        moves.append('U')
    if row < n - 1:
        moves.append('D')
    if col > 0:
        moves.append('L')
    if col < n - 1:
        moves.append('R')
    
    return moves

def apply_move(state, move, n):
    state = list(state)
    zero_index = locate_zero_index(state)
    
    if move == 'U':
        swap_index = zero_index - n
    elif move == 'D':
        swap_index = zero_index + n
    elif move == 'L':
        swap_index = zero_index - 1
    elif move == 'R':
        swap_index = zero_index + 1

    state[zero_index], state[swap_index] = state[swap_index], state[zero_index]
    return tuple(state)

def cost(node, successor):
    return 1

# Genera los sucesores de un estado dado
def successors(state, n):
    moves = valid_moves(state, n)
    generated_successors = []
    for move in moves:
        new_state = apply_move(state, move, n)
        generated_successors.append((new_state, move))
    return generated_successors

def generate_instance(n, k):
    state = generate_goal_state(n)
    path = []
    last_move = None
    
    for _ in range(k):
        valid = valid_moves(state, n)
        
        if last_move:
            inverse = INVERSE_MOVES[last_move]
            if inverse in valid:
                valid.remove(inverse)
        
        move = random.choice(valid)
        
        state = apply_move(state, move, n)
        
        path.append(move)
        last_move = move
    
    return state, path

def print_board(state, n):
    for i in range(n):
        print(' '.join(str(x) for x in state[i*n:(i+1)*n]))
        
def is_goal(state, goal):
    return state == goal

if __name__ == "__main__":
    n_dimension, k_movement = map(int, input().split())
    initial_state, moves = generate_instance(n_dimension, k_movement)
    goal_state = generate_goal_state(n_dimension)
    print_board(initial_state, n_dimension)
    print_board(goal_state, n_dimension)
    print(' '.join(moves))