# Visualize the n-dimensional data using Scatter plots. 

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("ToyotaCorolla.csv")

# Scatter Plot
x = data['KM']
y = data['Price']

plt.scatter(x, y, color='blue')
plt.xlabel("KM")
plt.ylabel("Price")
plt.title("Scatter Plot")
plt.show()



# Write a program to implement Hill Climbing Algorithm.

# Maximize a function f(x) = -(x - 5) ** 2 + 25 using hill climbing algorithm.

def objective(x):
    return -(x - 5) ** 2 + 25

def hill_climbing(start):
    current = start
    i = 1
    
    while True:
        left = current - 1
        right = current + 1

        print(f"Iteration {i}: x = {current:.4f}, f(x) = {objective(current):.4f}")
        i += 1

        if objective(left) > objective(current):
            current = left
        elif objective(right) > objective(current):
            current = right
        else:
            return current, objective(current)

x = 0

x_best, best_value = hill_climbing(x)

print("\nFinal Solution:")
print(f"x = {x_best:.4f}, f(x) = {best_value:.4f}")