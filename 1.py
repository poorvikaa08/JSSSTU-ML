#Visualize the n-dimensional data using Scatter plots. 

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



#Write a program to implement Hill Climbing Algorithm.

import random

def objective(x):
    return -x**2 + 5

def hill_climbing(start, step, iterations):
    x = start

    for i in range(iterations):
        new_x = x + random.uniform(-step, step)

        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {objective(x):.4f}")

        if objective(new_x) > objective(x):
            x = new_x

    print("\nFinal Solution:")
    print(f"x = {x:.4f}, f(x) = {objective(x):.4f}")

hill_climbing(0.1, 0.05, 5)