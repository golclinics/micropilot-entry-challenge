
def bfs(node):
    #Model your graph as an adjacency list i.e neighbours to your node kept in a dict
    graph= {
        'A': ['B','C'],
        'B' : ['D','E'],
        'C': ['F'],
        'D':[],
        'E': ['F'],
        'F': []
    }

    queue = []
    visited = []
    queue.append(node)
    visited.append(node)

    while queue: #A    => BC
        #while traversing the queue, dequeue the first node & print it
        s = queue.pop(0) #pop B
        # find and visit the neighbours of the popped node
        for neighbour in graph[s]: #A - #B
            if neighbour not in visited:
                visited.append(neighbour) #B C  neighbors of B are D and E
                queue.append(neighbour) # B => C D E 

    return visited
print(bfs('A'))
                
