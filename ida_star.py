from puzzle import is_goal, successors, cost

def search(path, g, threshold, n, goal, h_func):
    node = path[-1][0]
    f = g + h_func(node, goal, n)
    if f > threshold: return f
    if is_goal(node, goal): return 'FOUND'
    min_threshold = float('inf')
    
    for succ in successors(node, n):
        if succ not in path:
            path.append(succ)
            t = search(path, g + cost(node, succ), threshold, n, goal, h_func)
            if t == 'FOUND': 
                return 'FOUND'
            if t < min_threshold: 
                min_threshold = t
            path.pop()
            
    return min_threshold

