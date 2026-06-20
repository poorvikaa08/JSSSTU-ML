# Write a program to perform agglomerative clustering based on single-linkage, complete-linkage criteria.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram

X = load_iris().data[:6]

# Proximity Matrix
n = len(X)
P = np.zeros((n, n))

for i in range(n):
    for j in range(n):
        P[i, j] = np.linalg.norm(X[i] - X[j])

print("Proximity Matrix:")
print(P)

# Single Linkage
dendrogram(linkage(X, method='single'))
plt.title("Single Linkage")
plt.show()

# Complete Linkage
dendrogram(linkage(X, method='complete'))
plt.title("Complete Linkage")
plt.show()