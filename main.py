# task:
# 1. Rewrite the BFS algorithm so that it reads the graph from a file.
# 2. Implement A* search algorithm.
# 3. Upload solution to Student GitHub account

import ast

from Astar import Astar

# 1. Rewrite the BFS algorithm so that it reads the graph from a file.
# get data from file as dictionary
file = open('graph', 'r')
data = file.read()
graph = ast.literal_eval(data)
file.close()



visited = [] # List for visited nodes.
queue = [] # Initialize a queue
def bfs(visited, graph, node): # function for BFS
 visited.append(node)
 queue.append(node)
 while queue: # Creating loop to visit each node
    m = queue.pop(0)
    print(m, end=" ")
    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
print()
print("Following is the Breadth-First Search")
bfs(visited, graph, '5')
print()
print()

# 2. Implement A* search algorithm.
list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('D', 5)],
    'C': [('D', 12)]
}
print("The list is ", list)
print()
graph1 = Astar(list)

print("The path from A to D :")
graph1.a_star_algorithm('A', 'D')



