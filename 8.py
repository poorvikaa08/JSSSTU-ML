# Write a program to perform unsupervised K-means clustering techniques on Iris dataset.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# Load Iris dataset
X = load_iris().data

# Number of clusters
k = int(input("Enter number of clusters: "))

# Initial centroids (first k points)
centroids = X[:k]

# Repeat until convergence
for _ in range(100):
    labels = []

    # Assign each point to nearest centroid
    for point in X:
        distances = []
        for centroid in centroids:
            distances.append(np.linalg.norm(point - centroid))

        labels.append(np.argmin(distances))

    labels = np.array(labels)

    # Compute new centroids
    new_centroids = []

    for i in range(k):
        new_centroids.append(X[labels == i].mean(axis=0))

    new_centroids = np.array(new_centroids)

    # Stop if centroids do not change
    if np.allclose(centroids, new_centroids):
        break

    centroids = new_centroids

print("Centroids:")
print(centroids)

# Plot clusters
plt.scatter(X[:,0], X[:,1], c=labels)

# Plot centroids
plt.scatter(centroids[:,0], centroids[:,1],
            marker='X',
            color='red',
            s=200)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()


# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans

# # Load the Iris dataset
# X = load_iris().data

# # Number of clusters
# K = 3

# kmeans = KMeans(n_clusters=K)
# labels = kmeans.fit_predict(X)
# centroids = kmeans.cluster_centers_

# print("K-means Labels:", labels)
# print("K-means Centroids:", centroids)

# # Plotting K-means results
# plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
# plt.scatter(centroids[:, 0], centroids[:, 1], marker='x', color='red', s=200)
# plt.xlabel('Sepal Length')
# plt.ylabel('Sepal Width')
# plt.title('K-means Clustering of Iris Dataset')
# plt.show()

