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



#Write a program to implement the A* algorithm

graph = {
    'A':[('B',6),('F',3)],
    'B':[('C',3),('D',2)],
    'C':[('D',1),('E',5)],
    'D':[('C',1),('E',8)],
    'E':[('I',5),('J',5)],
    'F':[('G',1),('H',7)],
    'G':[('I',3)],
    'H':[('I',2)],
    'I':[('E',5),('J',3)],
    'J':[]
}

h = {'A':10,'B':8,'C':5,'D':7,'E':3,'F':6,'G':5,'H':3,'I':1,'J':0}

def astar(start, goal):
    open = [(0, start, [start])]
    visited = set()

    while open:
        open.sort()
        cost, node, path = open.pop(0)

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for nbr, c in graph.get(node, []):
                open.append((cost + c + h[nbr], nbr, path + [nbr]))

    return None

print("Path:", astar('A', 'J'))