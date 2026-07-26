#Visualize the n-dimensional data using heat-map.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

# Heat map
sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet',annot=True)
plt.show()

# Write a program to implement Min-Max Algorithm.

def minmax(depth, nodeIndex, maximizingPlayer, values):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = minmax(depth + 1, nodeIndex * 2 + i,
                         False, values)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minmax(depth + 1, nodeIndex * 2 + i,
                         True, values)
            best = min(best, val)

        return best


# values = [3, 5, 2, 9, 12, 5, 23, 23]
# User Input
values = list(map(int, input("Enter the 8 terminal node values: ").replace(',', ' ').split()))

result = minmax(0, 0, True, values)

print("Optimal Value:", result)

