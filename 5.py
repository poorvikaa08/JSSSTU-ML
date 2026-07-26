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

def alphabeta(depth, nodeIndex, maximizingPlayer, values, alpha, beta):
    if depth == 3:
        return values[nodeIndex]

    if maximizingPlayer:
        best = float('-inf')
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, False, values, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)
            if alpha >= beta:
                break
        return best
    else:
        best = float('inf')
        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i, True, values, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)
            if alpha >= beta:
                break
        return best


# Example tree with depth 3 and 8 terminal nodes
# values = [3, 5, 2, 9, 12, 5, 23, 23]

# print("Enter the 8 terminal node values:")

# for i in range(8):
#     value = int(input(f"Value {i+1}: "))
#     values.append(value)

values = list(map(int, input("Enter the 8 terminal node values (space-separated): ").split()))

result = alphabeta(0, 0, True, values, float('-inf'), float('inf'))
print("The optimal value is:", result)




