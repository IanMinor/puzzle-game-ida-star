def h1(state, goal, n):
    total_misplaced = 0
    
    for i in range(n*n):
        if state[i] != 0 and state[i] != goal[i]:
            total_misplaced += 1
    return total_misplaced

def h2(state, goal, n):
    distance = 0
    
    for i in range(n*n):
        if state[i] != 0 and state[i] != goal[i]:
            target_index = state[i] - 1
            current_row, current_col = divmod(i, n)
            target_row, target_col = divmod(target_index, n)
            distance += abs(current_row - target_row) + abs(current_col - target_col)
            
    return distance
            
def heuristic(state, goal, n):
    return max(h1(state, goal, n), h2(state, goal, n))          