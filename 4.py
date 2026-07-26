#Visualize the n-dimensional data using heat-map.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")

# Heat map
sns.heatmap(data[["Price","KM","Doors", "Weight"]].corr(),cmap='jet',annot=True)
plt.show()


# Write a program to implement Min-Max Algorithm.

def minmax(depth, nodeIndex, isMaxPlayer, values, maxDepth):
    # Base case: reached terminal node
    if depth == maxDepth:
        return values[nodeIndex]

    if isMaxPlayer:
        best = float('-inf')

        for i in range(2):
            val = minmax(depth + 1, nodeIndex * 2 + i,
                         False, values, maxDepth)
            best = max(best, val)

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = minmax(depth + 1, nodeIndex * 2 + i,
                         True, values, maxDepth)
            best = min(best, val)

        return best


# User Input
maxDepth = int(input("Enter the depth of the tree: "))

numLeaves = 2 ** maxDepth

print(f"Enter {numLeaves} terminal node values:")
values = list(map(int, input().replace(',', ' ').split()))

# values = list(map(int, input().split()))
# values = [3, 5, 2, 9, 12, 5, 23, 23]

# Validate input
if len(values) != numLeaves:
    print(f"Error: You must enter exactly {numLeaves} values.")
else:
    result = minmax(0, 0, True, values, maxDepth)
    print("Optimal Value:", result)

