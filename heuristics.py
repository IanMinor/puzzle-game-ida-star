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

def count_conflicts_in_line(pieces):
    count = 0
    for i in range(len(pieces)):
        for j in range(i + 1, len(pieces)):
            if pieces[i][1] < pieces[j][1] and pieces[i][0] > pieces[j][0]:
                count += 1
    return count

def h3(state, goal, n):
    tiles_on_correct_row = {}
    tiles_on_correct_col = {}
    total_conflicts = 0
    
    
    for i in range(n*n):
        if state[i] != 0:
            target_index = state[i] - 1
            current_row, current_col = divmod(i, n)
            target_row, target_col = divmod(target_index, n)
            if current_row == target_row:
                tiles_on_correct_row[current_row] = tiles_on_correct_row.get(current_row, []) + [(state[i], current_col)]
            if current_col == target_col:
                tiles_on_correct_col[current_col] = tiles_on_correct_col.get(current_col, []) + [(state[i], current_row)]

    for row, pieces in tiles_on_correct_row.items():
        count = count_conflicts_in_line(pieces)
        total_conflicts += count
    for col, pieces in tiles_on_correct_col.items():
        count = count_conflicts_in_line(pieces)
        total_conflicts += count
    
    return total_conflicts * 2

def heuristic(state, goal, n):
    return max(h1(state, goal, n), h2(state, goal, n))          