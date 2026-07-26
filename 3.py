#Visualize the n-dimensional data using contour plots.

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ToyotaCorolla.csv")

#contour plot
x = data['KM']
y = data['Weight']
z = data['Price']

plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('KM')
plt.ylabel('Weight')
plt.title('Contour Plot')
plt.show()



# Write a program to implement the A* Algorithm

def astar(start, goal, graph, h):
    open_list = [(0, start, [start])]
    visited = set()

    while open_list:
        open_list.sort()
        cost, node, path = open_list.pop(0)

        if node == goal:
            return path, cost

        if node not in visited:
            visited.add(node)

            for nbr, c in graph.get(node, []):
                if nbr not in visited:
                    open_list.append((cost + c + h[nbr], nbr, path + [nbr]))

    return None, None

graph = {}

n = int(input("Enter number of nodes: "))

for i in range(n):
    node = input(f"\nEnter node {i+1}: ")
    m = int(input(f"Enter number of neighbours of {node}: "))

    graph[node] = []

    for j in range(m):
        nbr = input("Neighbour: ")
        cost = int(input("Cost: "))
        graph[node].append((nbr, cost))

# Heuristic values
h = {}

print("\nEnter heuristic values:")

for node in graph:
    h[node] = int(input(f"h({node}) = "))

start = input("\nEnter Start Node: ")
goal = input("Enter Goal Node: ")

path, cost = astar(start, goal, graph, h)

if path:
    print("\nPath:", path)
    print("Cost:", cost)
else:
    print("Goal not reachable.")