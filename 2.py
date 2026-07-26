# Visualize the n-dimensional data using 3D surface plots.

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ToyotaCorolla.csv")

# 3d surface plot
x = data['KM']
y = data['Doors']
z = data['Price']

ax = plt.axes(projection='3d')
ax.plot_trisurf(x,y,z,cmap="jet")
ax.set_title("3D Surface Plot")

plt.show()



# Write a program to implement the Best First Search (BFS) algorithm.

def best_first_search(graph, start, goal, h):
    open_list = [(0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort(key=lambda x: h[x[1]])
        cost, node, path = open_list.pop(0)

        if node == goal:
            return cost, path

        visited.add(node)

        for nbr, c in graph[node]:
            if nbr not in visited:
                open_list.append((cost + c, nbr, path + [nbr]))

graph = {}

n = int(input("Enter the number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node {i+1}: ")
    m = int(input(f"Enter the number of neighbors of {node}: "))
    
    graph[node] = []
    for j in range(m):
        nbr = input("Neighbour: ")
        cost = int(input("Cost: "))
        graph[node].append((nbr, cost))


h = {}

print("\nEnter heuristic values:")

for node in graph:
    h[node] = int(input(f"h({node}) = "))



start = input("\nEnter start node: ")
goal = input("Enter goal node: ")

cost, path = best_first_search(graph, start, goal, h)

if path:
    print("\nPath:", path)
    print("Cost:", cost)
else:
    print("Goal not reachable.")
    
    
"""
graph = {
    'A':[('B',11),('C',14),('D',7)],
    'B':[('E',15)],
    'C':[('E',8),('F',10)],
    'D':[('F',25)],
    'E':[('H',9)],
    'F':[('G',20)],
    'G':[],
    'H':[('G',10)]
}

h = {'A':40,'B':32,'C':25,'D':35,'E':19,'F':17,'G':0,'H':10}

"""