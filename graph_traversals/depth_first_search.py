'''
Depth-first-search

- algorithm for traversing a finite graph
- DFS visits child vertices before visiting siblings
- a stack is generally used when implementing this algorithm


The algorithm begins with a 'root' vertex (node), and then iteratively transitions from the current vertex to an adjacent, unvisited vertex until it can go no further. 
The algorithm then backtracks until it finds a vertex connected to more uncharted territory. 

'''


'''
PSEUDOCODE!

=======================

n = number of vertices in graph
g = adjacency list representing the graph
visited = [false, false...] # size n 


function dfs(at):
    if visited[at]:
        return
    visited[at] = True

    neighbours = graph[at]
    for next in neighbours:
        dfs(next)

#start DFS at node zero
start_node = 0
dfs(start_node)
'''