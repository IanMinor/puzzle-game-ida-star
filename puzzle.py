import random

n_dimension, k_movement = map(int, input().split())

INVERSE_MOVES = {
    'U': 'D',
    'D': 'U',
    'L': 'R',
    'R': 'L'
}

def generate_goal_state(n):
    return tuple(list(range(1, n*n)) + [0])

def valid_moves(state, n):
    zero_index = state.index(0)
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
    zero_index = state.index(0)
    
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

initial_state, moves = generate_instance(n_dimension, k_movement)
print_board(initial_state, n_dimension)
print(' '.join(moves))

