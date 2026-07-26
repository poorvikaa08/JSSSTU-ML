# Write a program to develop the Naive Bayes classifier on Titanic dataset.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Select required columns
df = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Survived']]

# Fill missing Age values
df['Age'] = df['Age'].fillna(df['Age'].median())

# Convert Gender into numbers
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Features and Target
x = df.drop('Survived', axis=1)
y = df['Survived']

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))