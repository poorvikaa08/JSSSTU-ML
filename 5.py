# Visualize the n-dimensional data using Box-plot.

import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ToyotaCorolla.csv")

#box plot
plt.title('Box Plot')
plt.boxplot([data["Price"],data["HP"],data["KM"]])

plt.xticks([1,2,3],["Price","HP","KM"])

plt.show()


# Write a program to implement Alpha-beta pruning algorithm.


def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, maxDepth):
    # Base case
    if depth == maxDepth:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            False, values, alpha, beta, maxDepth)

            best = max(best, val)
            alpha = max(alpha, best)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                            True, values, alpha, beta, maxDepth)

            best = min(best, val)
            beta = min(beta, best)

            # Alpha-Beta Pruning
            if alpha >= beta:
                break

        return best


# values = [3, 5, 2, 9, 12, 5, 23, 23]

# print("Enter the 8 terminal node values:")

# for i in range(8):
#     value = int(input(f"Value {i+1}: "))
#     values.append(value)

maxDepth = int(input("Enter the depth of the tree: "))

numLeaves = 2 ** maxDepth

print(f"Enter {numLeaves} terminal node values:")
values = list(map(int, input().split()))

if len(values) != numLeaves:
    print(f"Error: You must enter exactly {numLeaves} values.")
else:
    result = alphabeta(0, 0, True, values,
                       float('-inf'), float('inf'), maxDepth)

    print("The optimal value is:", result)




# User Input


# Validate input
