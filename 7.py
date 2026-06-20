#Write a program to develop the KNN classifier with Euclidean distance and Manhattan distance for the k values as 3 based on split up of training and testing dataset as 70-30 on Glass dataset

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

df = pd.read_csv("glass.csv")
X = df.drop("Type", axis=1)
y = df["Type"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

for metric in ["euclidean", "manhattan"]:
    knn = KNeighborsClassifier(n_neighbors=3, metric=metric)
    knn.fit(X_train, y_train)
    print(f"{metric.capitalize()} Accuracy:",
          accuracy_score(y_test, knn.predict(X_test)))