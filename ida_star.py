from puzzle import is_goal, successors, cost

# todo: optimizar path_states usando un set
def search(path, g, threshold, n, goal, h_func):
    node = path[-1][0]
    path_states = [p[0] for p in path]
    f = g + h_func(node, goal, n)
    if f > threshold: return f
    if is_goal(node, goal): return 'FOUND'
    min_threshold = float('inf')
    
    for succ in successors(node, n):
        succ_state = succ[0]
        if succ_state not in path_states:
            path.append(succ)
            t = search(path, g + cost(node, succ_state), threshold, n, goal, h_func)
            if t == 'FOUND': 
                return 'FOUND'
            if t < min_threshold: 
                min_threshold = t
            path.pop()
            
    return min_threshold

def ida_star(root, n, goal, h_func):
    threshold = h_func(root, goal, n)
    path = [(root, None)]
    
    while True:
        t = search(path, 0, threshold, n, goal, h_func)
        if t == 'FOUND':
            # Retorna el path y el costo total
            return path, len(path) - 1
        if t == float('inf'):
            return None, threshold
        threshold = t