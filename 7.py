#Write a program to develop the KNN classifier with Euclidean distance and Manhattan distance for the k values as 3 based on split up of training and testing dataset as 70-30 on Glass dataset

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix   

df = pd.read_csv("glass.csv")
X = df.drop("Type", axis=1)
y = df["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)


def euclidean(x, y):
    return np.sqrt(np.sum((x - y) ** 2))

def manhattan(x, y):
    return np.sum(np.abs(x - y))

distance = [("Euclidean", euclidean), ("Manhattan", manhattan)]

# Apply both distance metrics
for name, metric in distance:

    knn = KNeighborsClassifier(
        n_neighbors=3,
        metric=metric,
        algorithm="brute"
    )

    knn.fit(X_train, y_train)

    y_pred = knn.predict(X_test)
    print(f"\n--- KNN with {name} Distance ---")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))